#!/usr/bin/env python3
"""
context-bus stager (personal Mac side).

Collects everything that changed since the last publish and lays it out in
~/context-bus/ ready for the digest step and the git push.

Three payloads:
  1. memory delta   -> bus/memory/         (new/changed ~/coordinator/memory/*.md + the index)
  2. asset delta    -> bus/assets/         (changed skills, agents, automation scripts, registry)
  3. session skeletons -> bus/.staging/    (compact, uncommitted; input to the LLM digest step)

Every text file is written with /Users/<user> replaced by the {{HOME}} token, so the
work Mac (/Users/IntradiemDA) never needs a path-rewrite pass on arrival.

Scheduled swarm runs are skipped: they carry promptSource == "sdk". Only interactive
sessions become digests.

Writes .staging/stage_manifest.json describing what it staged.
Read-only against every source. Never deletes anything outside bus/.staging and bus/memory.
"""

import json
import os
import shutil
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

HOME = Path.home()
TOKEN = "{{HOME}}"
BUS = Path(os.environ.get("CONTEXT_BUS_DIR", HOME / "context-bus"))
STATE = HOME / ".context-bus-state.json"

COORDINATOR = HOME / "coordinator"
MEMORY_SRC = COORDINATOR / "memory"
ENGINE = HOME / "Claude" / "Projects" / "Intradiem GTM Engineer"

# Caps so a busy day can never produce an unreadable or unpushable payload.
MAX_SKELETON_CHARS = 14_000      # per session
MAX_TOTAL_SKELETON_CHARS = 90_000
MAX_SESSIONS = 12
MAX_ASSET_BYTES = 400_000        # skip anything larger; it isn't context, it's a binary

ASSET_SOURCES = [
    (COORDINATOR / ".claude" / "skills", "skills", {".md", ".json", ".py", ".sh", ".txt"}),
    (HOME / ".claude" / "agents", "agents", {".md"}),
    (ENGINE / "automation", "automation", {".sh", ".py", ".plist", ".md"}),
    (ENGINE / ".claude" / "workflows", "workflows", {".js", ".md"}),
]
ASSET_SINGLES = [
    (COORDINATOR / "CLAUDE.md", "CLAUDE.md"),
    (COORDINATOR / "AGENT_REGISTRY.md", "AGENT_REGISTRY.md"),
    (ENGINE / "automation" / "LOG_CONVENTION.md", "LOG_CONVENTION.md"),
]

SKIP_DIR_PARTS = {".git", "node_modules", "__pycache__", ".wrangler", "logs", ".staging"}


def tokenize(text: str) -> str:
    """Replace this machine's home path with a portable token."""
    return text.replace(str(HOME), TOKEN)


def load_state() -> dict:
    if STATE.exists():
        try:
            return json.loads(STATE.read_text())
        except Exception:
            pass
    # First run: look back a week so the first bundle is genuinely useful.
    return {"last_publish": (datetime.now(timezone.utc) - timedelta(days=7)).isoformat()}


def since_ts(state: dict) -> float:
    try:
        return datetime.fromisoformat(state["last_publish"]).timestamp()
    except Exception:
        return time.time() - 7 * 86400


def copy_text(src: Path, dst: Path) -> bool:
    """Copy a text file with path tokenization. Returns False if it isn't usable text."""
    try:
        raw = src.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(tokenize(raw), encoding="utf-8")
    return True


def stage_memory(cutoff: float) -> list:
    """New or changed memory files since cutoff, plus the real index every time."""
    out_dir = BUS / "memory"
    out_dir.mkdir(parents=True, exist_ok=True)
    staged = []
    if not MEMORY_SRC.is_dir():
        return staged
    for f in sorted(MEMORY_SRC.glob("*.md")):
        # memory/MEMORY.md is the live 25KB index and always ships; the near-empty
        # coordinator/MEMORY.md at the repo root is stale and deliberately not a source.
        if f.name == "MEMORY.md" or f.stat().st_mtime > cutoff:
            if copy_text(f, out_dir / f.name):
                staged.append({"name": f.name, "mtime": f.stat().st_mtime,
                               "new": f.stat().st_mtime > cutoff})
    return staged


def stage_assets(cutoff: float) -> list:
    out_dir = BUS / "assets"
    staged = []
    for root, label, exts in ASSET_SOURCES:
        if not root.is_dir():
            continue
        for f in root.rglob("*"):
            if not f.is_file() or f.suffix not in exts:
                continue
            if SKIP_DIR_PARTS & set(f.parts):
                continue
            try:
                st = f.stat()
            except OSError:
                continue
            if st.st_mtime <= cutoff or st.st_size > MAX_ASSET_BYTES:
                continue
            rel = f.relative_to(root)
            if copy_text(f, out_dir / label / rel):
                staged.append({"path": f"{label}/{rel}", "mtime": st.st_mtime})
    for src, name in ASSET_SINGLES:
        if src.is_file() and src.stat().st_mtime > cutoff:
            if copy_text(src, out_dir / name):
                staged.append({"path": name, "mtime": src.stat().st_mtime})
    return staged


def _text_of(block) -> str:
    if isinstance(block, str):
        return block
    if isinstance(block, dict):
        if block.get("type") == "text":
            return block.get("text", "")
        if block.get("type") == "tool_use":
            inp = block.get("input") or {}
            target = inp.get("file_path") or inp.get("path") or inp.get("command") or ""
            return f"[tool:{block.get('name')}] {str(target)[:160]}"
    return ""


def skeleton_of(path: Path):
    """Compact an interactive transcript into prompts + decisions + files touched.

    Returns None for scheduled swarm runs and for sessions with no real user turns.
    """
    turns, files_touched, cwds = [], set(), set()
    is_sdk = False
    title = None
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return None

    for line in lines:
        try:
            d = json.loads(line)
        except Exception:
            continue
        # entrypoint is the reliable discriminator. Scheduled swarm runs are "sdk-cli";
        # human sessions are "claude-vscode" or "cli". promptSource is NOT usable here:
        # interactive VS Code sessions emit a stray promptSource=="sdk" record too.
        if d.get("entrypoint") == "sdk-cli":
            is_sdk = True
            break
        if d.get("isSidechain"):
            continue
        if d.get("type") == "ai-title" and d.get("aiTitle"):
            title = d["aiTitle"]
        if d.get("cwd"):
            cwds.add(d["cwd"])

        typ = d.get("type")
        if typ not in ("user", "assistant"):
            continue
        content = (d.get("message") or {}).get("content")
        parts = content if isinstance(content, list) else [content]
        chunks = [t for t in (_text_of(p) for p in parts) if t and t.strip()]
        if not chunks:
            continue
        text = "\n".join(chunks).strip()
        if text.startswith("<") and "system-reminder" in text[:200]:
            continue

        for p in parts:
            if isinstance(p, dict) and p.get("type") == "tool_use":
                fp = (p.get("input") or {}).get("file_path")
                if fp and p.get("name") in ("Write", "Edit", "NotebookEdit"):
                    fp = str(fp)
                    # Scratchpad churn is noise, not context worth carrying across machines.
                    if "/scratchpad/" in fp or fp.startswith("/private/tmp/"):
                        continue
                    files_touched.add(tokenize(fp))

        # Keep the user's words nearly whole; assistant turns compress hard.
        turns.append({"role": typ, "text": text[:2400] if typ == "user" else text[:700]})

    if is_sdk or not any(t["role"] == "user" for t in turns):
        return None

    body, total = [], 0
    for t in turns:
        line = f"{t['role'].upper()}: {t['text']}"
        if total + len(line) > MAX_SKELETON_CHARS:
            body.append("... [session truncated for length]")
            break
        body.append(line)
        total += len(line)

    return {
        "session_id": path.stem,
        "project": path.parent.name,
        "title": title,
        "mtime": path.stat().st_mtime,
        "when": datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d %H:%M"),
        "cwds": sorted(tokenize(c) for c in cwds),
        "files_written": sorted(files_touched)[:40],
        "skeleton": "\n\n".join(body),
    }


def stage_sessions(cutoff: float) -> list:
    staging = BUS / ".staging"
    if staging.exists():
        shutil.rmtree(staging)
    (staging / "skeletons").mkdir(parents=True, exist_ok=True)

    candidates = []
    for f in HOME.glob(".claude/projects/*/*.jsonl"):
        try:
            if f.stat().st_mtime > cutoff:
                candidates.append(f)
        except OSError:
            continue
    candidates.sort(key=lambda p: p.stat().st_mtime, reverse=True)

    staged, total = [], 0
    for f in candidates:
        if len(staged) >= MAX_SESSIONS or total >= MAX_TOTAL_SKELETON_CHARS:
            break
        sk = skeleton_of(f)
        if not sk:
            continue
        out = staging / "skeletons" / f"{sk['session_id']}.md"
        header = (f"# session {sk['session_id']}\n"
                  f"when: {sk['when']}\nproject: {sk['project']}\n"
                  f"title: {sk['title'] or '(untitled)'}\n"
                  f"cwd: {', '.join(sk['cwds']) or '(unknown)'}\n"
                  f"files written: {', '.join(sk['files_written']) or '(none)'}\n\n---\n\n")
        out.write_text(tokenize(header + sk["skeleton"]), encoding="utf-8")
        total += len(sk["skeleton"])
        staged.append({k: sk[k] for k in
                       ("session_id", "when", "project", "title", "files_written")})
    return staged


def main() -> int:
    if not COORDINATOR.is_dir():
        print(f"context-bus: no coordinator at {COORDINATOR}, nothing to stage", file=sys.stderr)
        return 1
    BUS.mkdir(parents=True, exist_ok=True)

    state = load_state()
    cutoff = since_ts(state)
    now = datetime.now(timezone.utc)

    memory = stage_memory(cutoff)
    assets = stage_assets(cutoff)
    sessions = stage_sessions(cutoff)

    manifest = {
        "published_at": now.isoformat(),
        "published_date": datetime.now().strftime("%Y-%m-%d"),
        "since": state.get("last_publish"),
        "source_machine": "personal",
        "memory": memory,
        "memory_new_count": sum(1 for m in memory if m.get("new")),
        "assets": assets,
        "sessions": sessions,
        "counts": {"memory_new": sum(1 for m in memory if m.get("new")),
                   "assets": len(assets), "sessions": len(sessions)},
    }
    (BUS / ".staging" / "stage_manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8")
    (BUS / "MANIFEST.json").write_text(
        json.dumps({k: manifest[k] for k in
                    ("published_at", "published_date", "since", "source_machine", "counts")},
                   indent=2), encoding="utf-8")

    print(json.dumps(manifest["counts"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
