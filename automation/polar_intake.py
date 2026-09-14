#!/usr/bin/env python3
"""polar-intake: log what Polar (the AI browser on Dallas's personal Mac) saved to the inbox.

Deterministic, no Claude call. Dry run by default; --apply writes the log and the state file.

    python3 automation/polar_intake.py            # dry run: print what would be logged
    python3 automation/polar_intake.py --apply    # append automation/logs/polar-intake-<date>.md, update .intake-state
    python3 automation/polar_intake.py --task wfm-l3-lookup-rebind --apply   # one task folder only

What it does
  1. Walks automation/inbox/polar/<task-slug>/ for files not yet in .intake-state (by sha256).
  2. Looks the slug up in automation/config/polar_tasks.json for the title, the expected files and the
     verifier that closes the task (a Polar report is a claim; the CLI/connector read is proof).
  3. Appends a log block per task with the files, the missing expected files, the first lines of report.md
     if Polar wrote one, and a VERIFICATION OWED line naming the verifier agent and its read.
  4. Mints  evt: polar-intake-<date>#<task-slug>  once per task per day (LOG_CONVENTION.md) and cites the
     task's chain: if the registry has one.

What it never does: load a row into Clay, lemlist or Salesforce, spend a credit, flip a gate, message anyone.
The daily rundown reads the log. Unknown slugs are logged as UNREGISTERED and left for Dallas.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INBOX = ROOT / "automation" / "inbox" / "polar"
DOWNLOADS = pathlib.Path.home() / "Downloads" / "polar"   # where Dallas drops files downloaded from Polar's workspace
CONFIG = ROOT / "automation" / "config" / "polar_tasks.json"
LOGS = ROOT / "automation" / "logs"
STATE = INBOX / ".intake-state"
SKIP = {".intake-state", ".gitkeep", "README.md", ".DS_Store"}
REPORT_LINES = 12


def sha256(p: pathlib.Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def load_json(p: pathlib.Path, default):
    if not p.exists():
        return default
    try:
        return json.loads(p.read_text())
    except json.JSONDecodeError as e:
        sys.exit(f"{p}: invalid JSON ({e})")


def scan(inbox: pathlib.Path, state: dict, only: str | None) -> dict[str, list[dict]]:
    """Return {slug: [ {path, sha, size, mtime} ]} for files not in state."""
    seen = {f["sha"] for f in state.get("files", [])}
    found: dict[str, list[dict]] = {}
    if not inbox.exists():
        return found
    for task_dir in sorted(p for p in inbox.iterdir() if p.is_dir()):
        slug = task_dir.name
        if only and slug != only:
            continue
        for f in sorted(p for p in task_dir.rglob("*") if p.is_file()):
            if f.name in SKIP:
                continue
            digest = sha256(f)
            if digest in seen:
                continue
            found.setdefault(slug, []).append({
                "path": str(f.relative_to(ROOT)) if f.is_relative_to(ROOT) else str(f),
                "name": f.name,
                "sha": digest,
                "size": f.stat().st_size,
                "mtime": dt.datetime.fromtimestamp(f.stat().st_mtime).strftime("%Y-%m-%d %H:%M"),
            })
    return found


def report_excerpt(task_dir: pathlib.Path) -> list[str]:
    rp = task_dir / "report.md"
    if not rp.exists():
        return []
    lines = [l.rstrip() for l in rp.read_text(errors="replace").splitlines() if l.strip()]
    return lines[:REPORT_LINES]


def block(slug: str, files: list[dict], reg: dict | None, today: str, inbox: pathlib.Path = INBOX) -> str:
    names = {f["name"] for f in files}
    out = []
    if reg is None:
        out.append(f"### {slug}: UNREGISTERED task folder")
        out.append("Not in automation/config/polar_tasks.json. Files are logged and left in place; Dallas names the task or removes the folder.")
    else:
        out.append(f"### {slug}: {reg.get('title', slug)}")
        out.append(f"Sheet: `{reg.get('sheet', 'n/a')}` · system {reg.get('system', '?')} · registry status {reg.get('status', '?')}")
    out.append("Files Polar saved:")
    for f in files:
        out.append(f"- `{f['path']}` ({f['size']} bytes, {f['mtime']})")
    if reg is not None:
        expect = reg.get("expect", [])
        missing = [e for e in expect if e not in names]
        if missing:
            out.append(f"Missing from what the sheet asked for: {', '.join(missing)}")
        elif expect:
            out.append("All files the sheet asked for are present.")
        else:
            out.append("The sheet expects the report as a pasted REPORT block; these files are optional downloads.")
    excerpt = report_excerpt(inbox / slug)
    if excerpt:
        out.append("Polar's report (first lines, a claim until verified):")
        out.extend(f"> {l}" for l in excerpt)
    if reg is not None:
        out.append(f"VERIFICATION OWED ({reg.get('verifier_agent', 'Claude Code')}): {reg.get('verifier', 'read the live system before closing')}")
        if reg.get("credits"):
            out.append(f"Credits: {reg['credits']}")
    out.append("Next: the verifier read closes it; until then the registry status stays as is and nothing downstream acts on this.")
    out.append(f"evt: polar-intake-{today}#{slug}")
    if reg is not None and reg.get("chain"):
        out.append(f"chain: {reg['chain']}")
    return "\n".join(out) + "\n"


def paste_block(slug: str, text: str, reg: dict | None, today: str) -> str:
    out = []
    if reg is None:
        out.append(f"### {slug}: UNREGISTERED task (pasted report)")
        out.append("Not in automation/config/polar_tasks.json. Logged and left for Dallas.")
    else:
        out.append(f"### {slug}: {reg.get('title', slug)}")
        out.append(f"Sheet: `{reg.get('sheet', 'n/a')}` · system {reg.get('system', '?')} · registry status {reg.get('status', '?')}")
    lines = [l.rstrip() for l in text.splitlines() if l.strip()]
    out.append("Polar's REPORT block as pasted (a claim until verified):")
    out.extend(f"> {l}" for l in lines[:40])
    if len(lines) > 40:
        out.append(f"> ... ({len(lines) - 40} more lines)")
    if reg is not None:
        out.append(f"VERIFICATION OWED ({reg.get('verifier_agent', 'Claude Code')}): {reg.get('verifier', 'read the live system before closing')}")
        if reg.get("credits"):
            out.append(f"Credits: {reg['credits']}")
    out.append("Next: the verifier read closes it; until then the registry status stays as is and nothing downstream acts on this.")
    out.append(f"evt: polar-intake-{today}#{slug}")
    if reg is not None and reg.get("chain"):
        out.append(f"chain: {reg['chain']}")
    return "\n".join(out) + "\n"


def paste_mode(slug: str, apply: bool) -> int:
    text = sys.stdin.read()
    if not text.strip():
        sys.exit("--paste needs the REPORT block on stdin")
    registry = load_json(CONFIG, {"tasks": {}}).get("tasks", {})
    today = dt.date.today().isoformat()
    body = paste_block(slug, text, registry.get(slug), today) + "\n"
    print(f"polar-intake {today} [{'APPLY' if apply else 'DRY RUN'}]: pasted report for {slug}\n")
    print(body)
    if not apply:
        print("(dry run: nothing written; add --apply to log it)")
        return 0
    write_log(body, today)
    return 0


def write_log(body: str, today: str) -> None:
    LOGS.mkdir(parents=True, exist_ok=True)
    log = LOGS / f"polar-intake-{today}.md"
    header = f"# polar-intake {today}\n\nPolar report-backs (pasted REPORT blocks and any downloaded files). Each block ends with the verification that closes the task; a Polar report is a claim until that read lands.\n\n"
    if log.exists():
        log.write_text(log.read_text() + f"\n## Run {dt.datetime.now().strftime('%H:%M')}\n\n" + body)
    else:
        log.write_text(header + body)
    print(f"wrote {log.relative_to(ROOT)}")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="write the log and the state file (default: dry run)")
    ap.add_argument("--task", help="only this task slug (inbox subfolder)")
    ap.add_argument("--inbox", default=str(INBOX), help=argparse.SUPPRESS)
    ap.add_argument("--paste", metavar="SLUG", help="log a REPORT block pasted from Polar (text on stdin) for this task slug; no files needed")
    args = ap.parse_args()

    if args.paste:
        return paste_mode(args.paste, args.apply)

    inbox = pathlib.Path(args.inbox)
    state_path = inbox / ".intake-state"
    state = load_json(state_path, {"files": []})
    registry = load_json(CONFIG, {"tasks": {}}).get("tasks", {})
    today = dt.date.today().isoformat()

    found = scan(inbox, state, args.task)
    if args.inbox == str(INBOX) and DOWNLOADS.exists():
        for slug, files in scan(DOWNLOADS, state, args.task).items():
            found.setdefault(slug, []).extend(files)
    if not found:
        print(f"polar-intake {today}: nothing new in {inbox.relative_to(ROOT) if inbox.is_relative_to(ROOT) else inbox} or {DOWNLOADS}")
        return 0

    body = "".join(block(slug, files, registry.get(slug), today, inbox) + "\n" for slug, files in found.items())
    mode = "APPLY" if args.apply else "DRY RUN"
    print(f"polar-intake {today} [{mode}]: {sum(len(v) for v in found.values())} new file(s) across {len(found)} task folder(s)\n")
    print(body)

    if not args.apply:
        print("(dry run: nothing written; add --apply to log and record state)")
        return 0

    write_log(body, today)
    for slug, files in found.items():
        for f in files:
            state["files"].append({"task": slug, "path": f["path"], "sha": f["sha"], "processed": today})
    state_path.write_text(json.dumps(state, indent=2) + "\n")
    print(f"state: {state_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
