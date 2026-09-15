#!/usr/bin/env python3
import csv
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parent
ENGINE_STATE_PATH = ROOT / "gtm-cohesion-layer" / "engine_state.json"
IMPACT_PATH = ROOT / "impact" / "impact.json"
CREDIT_LEDGER_PATH = ROOT / "clay_credit_ledger.csv"
CLAY_REGISTRY_PATH = ROOT / "Clay_Build_State_Registry.md"
ACCOUNT_PLAYS_PATH = ROOT / "tam-outbound-engine" / "account_plays.json"
READOUT_LOG_PATH = ROOT / "Readout_Log.md"
OUTPUT_PATH = ROOT / "control_tower_state.json"


def parse_iso(value: Optional[str]):
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except Exception:
        return None


def is_seeded_status(value: Optional[str]) -> bool:
    if not value:
        return False
    return "SEED" in value.upper() or "PLACEHOLDER" in value.upper()


def is_stale(value: Optional[str], threshold_days: int) -> bool:
    if not value:
        return True
    dt = parse_iso(value)
    if not dt:
        return True
    now = datetime.now(timezone.utc)
    age_days = (now - dt.astimezone(timezone.utc)).total_seconds() / 86400.0
    return age_days > threshold_days


def realized_trust(impact: dict) -> str:
    """REALIZED has to be earned, never assumed.

    Added 2026-08-07 after the control tower spent weeks rendering two interview-era demo
    rows (dated before the role started) as a hard realized "1 meeting / $180K", while
    automation/logs/credit_pipeline_receipts.md independently reported 0 meetings and $0.

    Returns:
      REALIZED   the impact source is present, fresh, and nothing was dropped at the gate
      UNVERIFIED anything else, including a missing, stale, or gate-filtered source
    """
    if not impact:
        return "UNVERIFIED"
    if is_stale(impact.get("generated_at"), 7):
        return "UNVERIFIED"
    if not impact.get("data_complete", False):
        return "UNVERIFIED"
    realized = impact.get("realized", {}) or {}
    if realized.get("excluded_pre_role_rows"):
        # Rows were dropped at the ROLE_START gate, so this file still carries demo data.
        return "UNVERIFIED"
    return "REALIZED"


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_credit_ledger(path: Path) -> Dict[str, Any]:
    rows: List[Dict[str, str]] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if not row:
                continue
            rows.append(row)

    non_empty = [row for row in rows if row.get("running_total") not in (None, "")]
    latest = non_empty[-1] if non_empty else None
    actual_total = 0.0
    motion_totals: Dict[str, float] = {}
    for row in rows:
        actual = row.get("credits_actual", "")
        try:
            amount = float(actual) if str(actual).strip() else 0.0
        except ValueError:
            amount = 0.0
        actual_total += amount
        if amount <= 0:
            continue
        note = row.get("note", "") or ""
        table = row.get("table", "") or ""
        motion = None
        for token in [table, note]:
            lower = token.lower()
            if "star" in lower:
                motion = "star_ratings"
                break
            if "cost" in lower and "mandate" in lower:
                motion = "cost_mandate"
                break
            if "wfm" in lower or "adjacency" in lower:
                motion = "wfm_adjacency"
                break
            if "back" in lower and "office" in lower:
                motion = "back_office"
                break
        if motion:
            motion_totals[motion] = motion_totals.get(motion, 0.0) + amount

    if latest:
        spent = float(latest.get("running_total", 0) or 0)
        remaining = float(latest.get("budget_remaining", 0) or 0)
        budget = 5000.0
    else:
        spent = 0.0
        remaining = 5000.0
        budget = 5000.0

    pct_consumed = spent / budget if budget else 0.0
    trust = "LIVE"
    if not rows:
        trust = "SEEDED"
    elif latest and latest.get("date"):
        latest_date = latest.get("date")
        if is_stale(latest_date, 7):
            trust = "STALE"

    return {
        "spent": round(spent, 1),
        "remaining": round(remaining, 1),
        "budget": budget,
        "pct_consumed": round(pct_consumed, 3),
        "flag_60pct": pct_consumed >= 0.60,
        "flag_85pct": pct_consumed >= 0.85,
        "cost_per_qualified_reply": None,
        "motion_totals": motion_totals,
        "trust": trust,
        "source_date": latest.get("date") if latest else None,
        "actual_total": round(actual_total, 1),
    }


# Canonical motion keys the rest of the tower uses. Registry rows name motions
# with decoration ("Cost-Mandate Motion", "`WFM-Adjacency Motion` (wb_...)"), so
# map by keyword rather than by an exact name match.
MOTION_KEYWORDS = [
    ("star_ratings", ("star rating", "star-rating")),
    ("cost_mandate", ("cost-mandate", "cost mandate")),
    ("wfm_adjacency", ("wfm", "adjacency")),
    ("back_office", ("back office", "back-office")),
]

WARNING_MARKER = "⚠️"


def motion_keys_for(text: str) -> List[str]:
    lower = text.lower()
    keys: List[str] = []
    for key, needles in MOTION_KEYWORDS:
        if any(needle in lower for needle in needles):
            keys.append(key)
    return keys


def normalize_status(raw: str) -> str:
    # "**BUILT / NEUTRALIZED**" / "**BUILT / LIVE, PARTIALLY REPAIRED**" -> "BUILT"
    cleaned = raw.replace("*", "").strip()
    head = re.split(r"[/,]", cleaned, 1)[0].strip()
    word = head.split()[0].upper() if head.split() else "PLANNED"
    return word if word in {"BUILT", "PLANNED", "BLOCKED"} else "PLANNED"


OPEN_SIGNALS = ("still open", "remains open", "blanks all", "not fixed", "still fails")


def split_sentences(text: str) -> List[str]:
    # Split on sentence boundaries but not on the enumerators "(1)"/"(2)" the
    # registry uses inside cells.
    return [s.strip() for s in re.split(r"(?<=[.:])\s+(?=[A-Z(])", text) if s.strip()]


def extract_blocker(cell: str) -> Optional[Dict[str, Any]]:
    idx = cell.find(WARNING_MARKER)
    if idx < 0:
        return None
    frag = cell[idx + len(WARNING_MARKER):].strip().replace("**", "")
    low = frag.lower()
    is_open = any(sig in low for sig in OPEN_SIGNALS)
    # A cell that only reports work "found and fixed" (no open residue) is a
    # resolved note, not a live blocker.
    if not is_open and ("found and fixed" in low or "confirmed fixed" in low):
        return None

    # Report the full sentence that carries the open signal; else the first one.
    sentences = split_sentences(frag)
    chosen = sentences[0] if sentences else frag
    for sentence in sentences:
        if any(sig in sentence.lower() for sig in OPEN_SIGNALS):
            chosen = sentence
            break

    # A sentence that just points at another table's row (e.g. "... bug (see
    # Functions table) remains open") is a cross-reference, not its own blocker —
    # the referenced row carries the real entry.
    if "see functions table" in chosen.lower() or "see functions)" in chosen.lower():
        return None

    text = chosen.strip().strip("—").strip()
    if len(text) > 220:
        text = text[:217].rstrip() + "…"
    return {"text": text, "open": is_open}


def parse_registry(path: Path) -> Dict[str, Any]:
    text = read_text(path)
    lines = text.splitlines()
    last_verified = None
    for line in lines:
        if line.startswith("**Last verified:**"):
            last_verified = line.replace("**Last verified:**", "").strip()
            break

    motion_statuses: Dict[str, Dict[str, Any]] = {}
    blockers: List[Dict[str, Any]] = []
    current_section = None
    for line in lines:
        stripped = line.strip()
        if "## Workbooks / Tables" in line:
            current_section = "workbooks"
            continue
        if stripped.startswith("## Functions"):
            current_section = "functions"
            continue
        if stripped.startswith("## Claygents"):
            current_section = "claygents"
            continue
        if stripped.startswith("## Workflows"):
            current_section = "workflows"
            continue
        if stripped.startswith("## What an agent CAN") or stripped.startswith("## STAMP"):
            current_section = None
            continue

        if not stripped.startswith("|"):
            continue
        parts = [part.strip() for part in stripped.split("|")]
        if len(parts) < 4:
            continue
        asset, status_cell = parts[1], parts[2]
        # Skip the header row and the |---|---| separator.
        if asset in ("Asset", "Function", "Claygent", "Workflow") or set(asset) <= {"-", ":"}:
            continue

        # Motion build-state comes only from the Workbooks/Tables section, and only
        # from the per-motion tables (not the Golden/scaffold rows). Match on the
        # asset name so a filename referenced in the notes can't mis-tag the row.
        if current_section == "workbooks" and "scaffold" not in asset.lower():
            for key in motion_keys_for(asset):
                if key not in motion_statuses:
                    motion_statuses[key] = {"status": normalize_status(status_cell), "notes": parts[3]}

        if WARNING_MARKER in stripped:
            cell = next((p for p in parts if WARNING_MARKER in p), stripped)
            blocker = extract_blocker(cell)
            if blocker:
                source = re.sub(r"`|\((?:wb|wf|t)_[^)]*\)|`w[fb]_[^`]*`", "", asset).strip()
                blocker["source"] = source or "Clay registry"
                # Workbook rows name their own motion; function/workflow rows name
                # the affected motions in prose, so scan the whole cell there.
                if current_section == "workbooks":
                    blocker["motions"] = motion_keys_for(asset)
                else:
                    blocker["motions"] = motion_keys_for(cell)
                blockers.append(blocker)
    return {"last_verified": last_verified, "motion_statuses": motion_statuses, "blockers": blockers}


def parse_readout_log(path: Path) -> List[Dict[str, str]]:
    lines = [line.strip() for line in read_text(path).splitlines() if line.strip()]
    entries: List[Dict[str, str]] = []
    for line in lines:
        if line.startswith("- "):
            entry = line[2:]
            parts = entry.split(":", 1)
            if len(parts) == 2:
                date = parts[0].strip()
                rest = parts[1].strip()
                entries.append({"date": date, "headline": rest})
    return entries


SCORECARD_HISTORY_PATH = Path(__file__).resolve().parent / "automation" / "logs" / "campaign_scorecard_history.csv"
SCORECARD_LOG_GLOB = "campaign-scorecard-*.md"


def read_live_campaigns() -> Dict[str, Any]:
    """Live campaign funnel from campaign_scorecard_history.csv (Sep 13 2026): latest row per campaign,
    engine campaigns aggregated per motion, plus the STALLED and capacity lines from the newest scorecard log.
    This is the block that replaces the seeded per-motion funnel wherever it is present."""
    import csv
    out: Dict[str, Any] = {"trust": "MISSING", "as_of": None, "per_motion": {}, "campaigns": [], "stalled": [], "capacity": []}
    if not SCORECARD_HISTORY_PATH.exists():
        return out
    # Sep 15 2026: a degraded lemlist export writes a zero row for every campaign it could not read
    # (39 of 39 that morning). Keep every row per campaign, then pick the newest row that is not a
    # zero-after-nonzero drop, and say which date it was carried from. Leads do not vanish overnight.
    history: Dict[str, List[Dict[str, str]]] = {}
    with SCORECARD_HISTORY_PATH.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            cid = row.get("campaign_id")
            if cid:
                history.setdefault(cid, []).append(row)
    if not history:
        return out
    export_errors: set = set()
    newest_log = sorted(SCORECARD_HISTORY_PATH.parent.glob(SCORECARD_LOG_GLOB))
    if newest_log:
        for line in newest_log[-1].read_text(encoding="utf-8").splitlines():
            if line.startswith("- EXPORT ERROR on"):
                names = line.split("counts above exclude them:", 1)[-1]
                export_errors = {n.strip().rstrip(".") for n in names.split(", ") if n.strip()}
    latest: Dict[str, Dict[str, str]] = {}
    carried: List[str] = []
    for cid, rows in history.items():
        rows.sort(key=lambda r: r["date"])
        pick = rows[-1]
        prev = rows[-2] if len(rows) > 1 else None
        def leads_of(r: Dict[str, str]) -> float:
            try:
                return float(r.get("leads") or 0)
            except ValueError:
                return 0.0
        degraded = (pick.get("campaign") in export_errors) or (prev is not None and leads_of(pick) == 0 and leads_of(prev) > 0)
        if degraded and prev is not None:
            for r in reversed(rows[:-1]):
                if leads_of(r) > 0 or r is rows[0]:
                    pick = r; break
            carried.append(pick["date"])
        latest[cid] = pick
    out["degraded"] = {"export_errors": len(export_errors), "carried_campaigns": len(carried), "carried_from": max(carried) if carried else None}
    def num(v: Optional[str]) -> int:
        try:
            return int(float(v or 0))
        except ValueError:
            return 0
    as_of = max(r["date"] for r in latest.values())
    per: Dict[str, Dict[str, int]] = {}
    for r in latest.values():
        motion = r.get("motion") or "Rep-built"
        m = per.setdefault(motion, {"campaigns": 0, "running": 0, "leads": 0, "launched": 0, "in_progress": 0, "replies": 0, "interested": 0, "meetings": 0, "bounced": 0, "unsubscribed": 0, "open_tasks": 0, "waiting": 0})
        m["campaigns"] += 1
        m["running"] += 1 if r.get("status") == "running" else 0
        m["leads"] += num(r.get("leads")); m["launched"] += num(r.get("leads")) - num(r.get("not_launched"))
        m["in_progress"] += num(r.get("in_progress")); m["replies"] += num(r.get("replied")); m["interested"] += num(r.get("interested"))
        m["meetings"] += num(r.get("meetings")); m["bounced"] += num(r.get("bounced")); m["unsubscribed"] += num(r.get("unsubscribed"))
        m["open_tasks"] += num(r.get("open_tasks")); m["waiting"] += num(r.get("waiting"))
        out["campaigns"].append({"id": r["campaign_id"], "name": r.get("campaign"), "motion": motion, "rep": r.get("rep"), "status": r.get("status"),
                                 "leads": num(r.get("leads")), "launched": num(r.get("leads")) - num(r.get("not_launched")), "replies": num(r.get("replied")),
                                 "meetings": num(r.get("meetings")), "open_tasks": num(r.get("open_tasks")), "mailbox": r.get("mailbox", "")})
    out["per_motion"] = per
    out["as_of"] = as_of
    out["trust"] = "STALE" if is_stale(as_of, 2) else "LIVE"
    logs = sorted(SCORECARD_HISTORY_PATH.parent.glob(SCORECARD_LOG_GLOB))
    if carried and logs:
        # The newest log is the degraded one; read STALLED and capacity from the log the rows were carried from.
        clean = [l for l in logs if l.stem.endswith(max(carried))]
        logs = clean or logs
    if logs:
        section = None
        for line in logs[-1].read_text(encoding="utf-8").splitlines():
            if line.startswith("## STALLED"):
                section = "stalled"; continue
            if line.startswith("## Send capacity"):
                section = "capacity"; continue
            if line.startswith("## "):
                section = None; continue
            if section == "stalled" and line.startswith("- STALLED"):
                out["stalled"].append(line[2:])
            if section == "capacity" and line.startswith("- "):
                out["capacity"].append(line[2:])
    return out


LOGS_DIR = Path(__file__).resolve().parent / "automation" / "logs"


def _newest_log(prefix: str) -> Optional[Path]:
    """Newest date-stamped log for a family. Only names of the form <prefix>-YYYY-MM-DD*.md count, sorted by
    that date, so a one-off like war-room-fanout-2026-07-27.md can never outrank today's run (Sep 15 2026)."""
    import re
    if not LOGS_DIR.exists():
        return None
    pat = re.compile(r"^" + re.escape(prefix) + r"-(\d{4}-\d{2}-\d{2})")
    dated = [(m.group(1), f.name, f) for f in LOGS_DIR.glob(f"{prefix}-*.md") for m in [pat.match(f.name)] if m]
    return sorted(dated)[-1][2] if dated else None


def read_swarm() -> Dict[str, Any]:
    """Swarm posture from the newest swarm-health log (Sep 15 2026): loaded launchd jobs with lifetime
    run counts, today's job_guard failures, staged-by-design jobs and the drift line. Read-only."""
    import re
    out: Dict[str, Any] = {"trust": "MISSING", "as_of": None, "jobs": [], "failures": [], "staged": [], "drift": None, "loaded": 0, "versioned": 0}
    log = _newest_log("swarm-health")
    if not log:
        return out
    out["as_of"] = log.stem.replace("swarm-health-", "")
    section = None
    for line in log.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            section = line[3:].strip().lower(); continue
        if section and section.startswith("loaded jobs") and line.startswith("- "):
            m = re.match(r"- (\S+): runs=(\d+)", line)
            if m:
                out["jobs"].append({"job": m.group(1).replace("com.dallasandrews.gtm.", ""), "runs": int(m.group(2))})
        elif section and section.startswith("output integrity") and line.startswith("- ["):
            out["failures"].append(line[2:])
        elif section and section.startswith("swarm drift") and line.startswith("- "):
            if "STAGED" in line:
                m = re.search(r"(com\.dallasandrews\.gtm\.\S+) is not loaded", line)
                if m:
                    out["staged"].append(m.group(1).replace("com.dallasandrews.gtm.", ""))
            elif "drift" in line:
                out["drift"] = line[2:]
                m = re.search(r"(\d+) loaded, (\d+) versioned", line)
                if m:
                    out["loaded"], out["versioned"] = int(m.group(1)), int(m.group(2))
    out["trust"] = "STALE" if is_stale(out["as_of"], 2) else "LIVE"
    return out


def read_deliverability_watch() -> Dict[str, Any]:
    """Per-mailbox bounce read from the newest deliverability-watch log (lemlist through the connector plus the
    scorecard history). Replaces the seeded EXAMPLE domains from engine_state wherever it is present."""
    import re
    out: Dict[str, Any] = {"trust": "MISSING", "as_of": None, "mailboxes": [], "floor_bounce": 0.03}
    log = _newest_log("deliverability-watch")
    if not log:
        return out
    out["as_of"] = log.stem.replace("deliverability-watch-", "")
    for line in log.read_text(encoding="utf-8").splitlines():
        m = re.match(r"- \*\*([a-z0-9._-]+@[a-z0-9.-]+)\*\*[^:]*: (\d+) campaigns?, (\d+) leads launched, (\d+) bounced → \*\*([0-9.]+%|n/a)\*\*", line)
        if m:
            launched, bounced = int(m.group(3)), int(m.group(4))
            rate = (bounced / launched) if launched else None
            out["mailboxes"].append({"mailbox": m.group(1), "campaigns": int(m.group(2)), "launched": launched, "bounced": bounced,
                                     "bounce_rate": rate, "above_floor": bool(rate is not None and rate > out["floor_bounce"])})
    out["trust"] = "STALE" if is_stale(out["as_of"], 3) else "LIVE"
    return out



def _clip(text: str, limit: int = 230) -> str:
    """Cut at a sentence boundary under the limit, else at the limit with an ellipsis."""
    text = text.strip()
    if len(text) <= limit:
        return text
    cut = text[:limit]
    dot = max(cut.rfind(". "), cut.rfind("; "))
    return (cut[:dot].rstrip(";") + "." if dot > 80 else cut.rstrip() + "…")


def read_gate_integrity() -> Dict[str, Any]:
    """Customer-exclusion posture from the newest gate-integrity log (Sep 15 2026). The auditor reads REAL rows
    weekly; the tower sums READY leaks across every table section, reads the union size, the per-table verdicts
    and the oldest standing item. Replaces the hardcoded 'no leak found' gate card."""
    import re
    out: Dict[str, Any] = {"trust": "MISSING", "as_of": None, "ready_leaks": 0, "union_domains": None, "union_names": None,
                           "verdicts": [], "flags": 0, "passes": 0, "stop_the_line_clean": None, "standing": [], "findings": 0}
    log = _newest_log("gate-integrity")
    if not log:
        return out
    out["as_of"] = log.stem.replace("gate-integrity-", "")
    text = log.read_text(encoding="utf-8")
    out["ready_leaks"] = sum(int(n) for n in re.findall(r"READY leaks: (\d+)", text))
    m = re.search(r"Final union used[^\n]*?(\d+)\s+(?:normalized\s+)?domains,?\s+(\d+)\s+(?:normalized\s+)?names", text)
    if m:
        out["union_domains"], out["union_names"] = int(m.group(1)), int(m.group(2))
    out["stop_the_line_clean"] = bool(re.search(r"No STOP-THE-LINE", text))
    section = None
    for line in text.splitlines():
        if line.startswith("## "):
            section = line[3:].strip().lower(); continue
        if section == "verdicts" and line.startswith("- **"):
            body = line[4:]
            name, _, rest = body.partition(":")
            v = re.search(r"\b(PASS|FLAG|UNVERIFIED|n/a)\b", rest or body)
            out["verdicts"].append({"table": name.strip("* "), "verdict": v.group(1) if v else "n/a"})
    out["flags"] = sum(1 for v in out["verdicts"] if v["verdict"] == "FLAG")
    out["passes"] = sum(1 for v in out["verdicts"] if v["verdict"] == "PASS")
    m = re.search(r"GATE INERT[^\n]*?(\d+) days unresolved \((\d{4}-\d{2}-\d{2})", text)
    if m:
        out["standing"].append({"item": "WFM-Adjacency L3 customer lookup inert", "days": int(m.group(1)), "since": m.group(2)})
    out["findings"] = len(re.findall(r"^evt: ", text, re.M))
    out["trust"] = "STALE" if is_stale(out["as_of"], 9) else "LIVE"  # weekly job, so nine days before it reads stale
    return out


def read_signal_review() -> Dict[str, Any]:
    """Staged-signal approval queue from the newest signal-review log: rows staged, awaiting APPROVE/DENY in the
    rundown thread, approved and denied. This is the live read behind the human-approval gate."""
    import re
    out: Dict[str, Any] = {"trust": "MISSING", "as_of": None, "staged": 0, "new": 0, "parked": 0, "awaiting": 0, "approved": 0, "denied": 0, "items": []}
    log = _newest_log("signal-review")
    if not log:
        return out
    text = log.read_text(encoding="utf-8")
    m = re.search(r"Ran (\S+): (\d+) staged rows read, (\d+) new unreviewed, (\d+) newly parked, (\d+) awaiting review, (\d+) approved, (\d+) denied", text)
    if m:
        out["as_of"] = m.group(1)
        out["staged"], out["new"], out["parked"], out["awaiting"], out["approved"], out["denied"] = (int(m.group(i)) for i in range(2, 8))
    else:
        out["as_of"] = log.stem.replace("signal-review-", "")
    for m in re.finditer(r'^- (sig-\S+) \| (.+?) \((\S+?)\) \| (\S+) \| (\d{4}-\d{2}-\d{2}) \| "(.*?)"', text, re.M):
        out["items"].append({"id": m.group(1), "company": m.group(2), "domain": m.group(3), "trigger": m.group(4), "date": m.group(5), "quote": m.group(6)})
    out["trust"] = "STALE" if is_stale(out["as_of"], 2) else "LIVE"
    return out


HEAT_NAMES = {"unitedhealthgroup.com": "UnitedHealth Group", "molinahealthcare.com": "Molina Healthcare", "hcsc.com": "HCSC",
              "nationalgrid.com": "National Grid", "lincolnfinancial.com": "Lincoln Financial", "t-mobilethuis.nl": "T-Mobile Thuis",
              "cvshealth.com": "CVS Health", "blueshieldca.com": "Blue Shield of California", "breadfinancial.com": "Bread Financial",
              "statefarm.com": "State Farm", "point32health.org": "Point32Health", "cambiahealth.com": "Cambia Health Solutions"}


def read_heat_list() -> Dict[str, Any]:
    """Account heat from the newest heat-list log: run mode (dry run or live stamp), companies scored per lane,
    the top 15 by heat with lane and evidence, and the lane A rep alerts. Names come from the lane A block where
    the log carries them; otherwise the domain label stands in, which the page shows as-is."""
    import re
    out: Dict[str, Any] = {"trust": "MISSING", "as_of": None, "mode": None, "scored": 0, "lanes": {}, "top": [], "rep_alerts": []}
    log = _newest_log("heat-list")
    if not log:
        return out
    text = log.read_text(encoding="utf-8")
    m = re.search(r"^# Heat List: (\S+)(?: \((.*?)\))?", text, re.M)
    out["as_of"] = m.group(1) if m else log.stem.replace("heat-list-", "")
    out["mode"] = (m.group(2) or "").split(";")[0].strip().lower() if m else None
    m = re.search(r"- ran, (\d+) companies scored: (.*)", text)
    if m:
        out["scored"] = int(m.group(1))
        for part in m.group(2).split(","):
            k, _, v = part.strip().rpartition(" ")
            if k and v.isdigit():
                out["lanes"][k] = int(v)
    names: Dict[str, str] = {}
    section = None
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("## "):
            section = line[3:].strip().lower(); continue
        if section and section.startswith("lane a") and re.match(r"- \S+ -> ", line):
            mm = re.match(r"- (\S+) -> (#\S+) \((.+)\)", line)
            if not mm:
                continue
            alert = {"domain": mm.group(1), "channel": mm.group(2), "reason": mm.group(3), "name": None, "heat": None, "saw": None}
            for follow in lines[i + 1:i + 4]:
                fm = re.match(r"\s*\*(.+?)\* is warm \(heat (\d+)\)", follow)
                if fm:
                    alert["name"], alert["heat"] = fm.group(1), int(fm.group(2))
                sm = re.match(r"\s*What we saw: (.*)", follow)
                if sm:
                    alert["saw"] = _clip(sm.group(1), 160)
            if alert["name"]:
                names[alert["domain"]] = alert["name"]
            out["rep_alerts"].append(alert)
        elif section and section.startswith("top 15") and line.startswith("- "):
            mm = re.match(r"- (\S+) (\d+) \[(\w+)\] ?(.*)", line)
            if mm:
                dom = mm.group(1)
                out["top"].append({"domain": dom, "name": names.get(dom) or HEAT_NAMES.get(dom) or dom.split(".")[0].replace("-", " ").title(),
                                   "heat": int(mm.group(2)), "lane": mm.group(3), "evidence": _clip(mm.group(4), 140)})
    out["trust"] = "STALE" if is_stale(out["as_of"], 2) else "LIVE"
    return out


def read_war_room() -> Dict[str, Any]:
    """What fired overnight, from the newest war-room log: Priority 1 and 2 items (name plus the first sentence),
    the executive summary, the count of still-open judgment calls in the action list, and the dated watch list
    the log carries as 'Recheck dates to hold'. Read-only; the war room already did the research."""
    import re
    out: Dict[str, Any] = {"trust": "MISSING", "as_of": None, "run_complete": None, "p1": [], "p2": [], "p3": [], "summary": None,
                           "open_calls": 0, "actions": 0, "dates": [], "p1_note": None}
    log = _newest_log("war-room")
    if not log:
        return out
    out["as_of"] = log.stem.replace("war-room-", "")
    text = log.read_text(encoding="utf-8")
    m = re.search(r"RUN COMPLETE (\d\d:\d\d)", text)
    out["run_complete"] = m.group(1) if m else None
    section = None
    for line in text.splitlines():
        if line.startswith("## "):
            head = line[3:].strip().lower()
            section = ("p1" if head.startswith("priority 1") else "p2" if head.startswith("priority 2") else "p3" if head.startswith("priority 3")
                       else "summary" if head.startswith("executive summary") else "actions" if head.startswith("today's action list") else None)
            continue
        if not section:
            continue
        s = line.strip()
        if section in ("p1", "p2", "p3"):
            mm = re.match(r"- \*\*(.+?)\*\*\s*[—–-]\s*(.*)", s)
            if mm:
                out[section].append({"name": mm.group(1).strip(), "text": _clip(mm.group(2))})
            elif section == "p1" and s.startswith("None") and not out["p1_note"]:
                out["p1_note"] = _clip(s, 200)
        elif section == "summary" and s and not out["summary"]:
            out["summary"] = _clip(s, 260)
        elif section == "actions":
            mm = re.match(r"\d+\. (.*)", s)
            if mm:
                out["actions"] += 1
                body = mm.group(1)
                if "still-open judgment call" in body:
                    out["open_calls"] += 1
                if body.lower().startswith("recheck dates to hold:"):
                    tail = body.split(":", 1)[1]
                    out["dates"] = [d.strip().rstrip(".") for d in re.split(r",\s*(?![^()]*\))", tail) if d.strip()]
    out["trust"] = "STALE" if is_stale(out["as_of"], 2) else "LIVE"
    return out


def read_naveen_readout() -> Dict[str, Any]:
    """Newest Friday readout draft (naveen-readout log): date and the BLUF's first sentence. Replaces the
    Readout_Log.md ask, which had been frozen at Jul 17 (Sep 15 2026)."""
    out: Dict[str, Any] = {"as_of": None, "bluf": None}
    log = _newest_log("naveen-readout")
    if not log:
        return out
    out["as_of"] = log.stem.replace("naveen-readout-", "")
    section = None
    for line in log.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            section = line[3:].strip().lower(); continue
        if section and "bluf" in section and line.strip() and not out["bluf"]:
            out["bluf"] = _clip(line.strip(), 260)
    return out


def gate_integrity_asks(as_of: Optional[str]) -> List[Dict[str, Any]]:
    """The auditor closes with 'Three things for Dallas to act on, in priority order: (1) ... (2) ...'. Each
    numbered clause becomes an open ask on the blockers panel, sourced to that audit date."""
    import re
    log = _newest_log("gate-integrity")
    if not log:
        return []
    m = re.search(r"things for Dallas to act on[^:]*:\s*(.*)", log.read_text(encoding="utf-8"))
    if not m:
        return []
    parts = [c.strip(" ;.") for c in re.split(r"\(\d\)\s*", m.group(1)) if c.strip(" ;.")]
    return [{"type": "ask", "source": f"Gate integrity {as_of}", "text": _clip(c.replace("`", ""), 220) + ".", "open": True} for c in parts[:3]]


def stamp_heat(accounts: Dict[str, Any], heat: Dict[str, Any]) -> None:
    """Attach the heat read to accounts-in-motion cards: a domain label or the first word of the heat name,
    word-bounded, against the account name. Leaves the card untouched when nothing matches."""
    import re
    for a in accounts.get("accounts", []):
        name = a["account"].lower()
        for h in heat.get("top", []):
            label = h["domain"].split(".")[0].lower()
            first = h["name"].split(" ")[0].lower()
            needles = [label] + ([first] if len(first) >= 4 else [])
            if any(re.search(r"\b" + re.escape(n) + r"\b", name) for n in needles):
                a["heat"] = {"heat": h["heat"], "lane": h["lane"]}
                break

ACCOUNTS_CFG = Path(__file__).resolve().parent / "automation" / "config" / "accounts_in_motion.json"
SEND_CAPACITY_CFG = Path(__file__).resolve().parent / "automation" / "config" / "send_capacity.json"


def read_accounts_in_motion(live: Dict[str, Any]) -> Dict[str, Any]:
    """Accounts the engine has already been pointed at: every rep set under motions/back_office_expansion/sets,
    Inger's roster, plus config extras (blitz campaigns, save rooms). One entry per account, lanes and reps merged,
    room link per set, live campaign attached when a campaign name carries the account. Config: accounts_in_motion.json."""
    import csv
    out: Dict[str, Any] = {"trust": "MISSING", "accounts": [], "reps": {}, "count": 0}
    if not ACCOUNTS_CFG.exists():
        return out
    cfg = json.loads(ACCOUNTS_CFG.read_text(encoding="utf-8"))
    root = Path(__file__).resolve().parent
    acc: Dict[str, Dict[str, Any]] = {}
    def add(name: str, rep: str, lane: str, vertical: Optional[str], room: Optional[str], date: Optional[str]) -> None:
        key = name.strip().lower()
        e = acc.setdefault(key, {"account": name.strip(), "reps": [], "lanes": [], "vertical": vertical, "rooms": [], "since": date})
        if rep and rep not in e["reps"]: e["reps"].append(rep)
        if lane and lane not in e["lanes"]: e["lanes"].append(lane)
        if room and room not in e["rooms"]: e["rooms"].append(room)
        if vertical and not e["vertical"]: e["vertical"] = vertical
    sets_dir = root / cfg.get("sets_dir", "")
    for f in sorted(sets_dir.glob("*.json")) if sets_dir.exists() else []:
        if f.stem in cfg.get("skip_sets", []):
            continue
        d = json.loads(f.read_text(encoding="utf-8"))
        lane = cfg.get("lane_by_mode", {}).get(d.get("mode") or "back_office", "account map")
        room = cfg.get("rooms", {}).get(f.stem)
        for name, meta in (d.get("accounts") or {}).items():
            add(name, d.get("rep", ""), lane, (meta or {}).get("vertical"), room, d.get("date"))
    for stem, r in cfg.get("roster_sets", {}).items():
        rp = root / r["file"]
        if rp.exists():
            with rp.open(encoding="utf-8") as handle:
                for row in csv.DictReader(handle):
                    if row.get(r["account_col"]):
                        add(row[r["account_col"]], r.get("rep", ""), r.get("lane", "account map"), None, cfg.get("rooms", {}).get(stem), None)
    for x in cfg.get("extra", []):
        add(x["account"], x.get("rep", ""), x.get("lane", ""), x.get("vertical"), x.get("room"), None)
        if x.get("campaign_match"):
            acc[x["account"].strip().lower()]["campaign_match"] = x["campaign_match"]
    camps = live.get("campaigns", []) or []
    for e in acc.values():
        import re as _re
        needle = _re.compile(r"\b" + _re.escape(e.get("campaign_match") or e["account"]) + r"\b", _re.I)
        hits = [c for c in camps if needle.search(c.get("name") or "")]
        if hits:
            e["campaign"] = {"name": hits[0]["name"], "status": hits[0]["status"], "leads": hits[0]["leads"], "launched": hits[0]["launched"], "replies": hits[0]["replies"]}
        e.pop("campaign_match", None)
    out["accounts"] = sorted(acc.values(), key=lambda e: (e["reps"][0] if e["reps"] else "", e["account"]))
    for e in out["accounts"]:
        for r in e["reps"]:
            out["reps"][r] = out["reps"].get(r, 0) + 1
    out["count"] = len(out["accounts"])
    out["trust"] = "LIVE" if out["accounts"] else "MISSING"
    return out


def fill_capacity_lanes(live: Dict[str, Any]) -> None:
    """Every mailbox in send_capacity.json gets a lane on the tower, even before the scorecard has assigned it a
    campaign (Sep 15 2026, Jack's second-domain mailbox). Synthesized lines use the scorecard's own wording."""
    if not SEND_CAPACITY_CFG.exists():
        return
    cfg = json.loads(SEND_CAPACITY_CFG.read_text(encoding="utf-8"))
    lines = live.setdefault("capacity", [])
    total = [l for l in lines if l.startswith("Engine total")]
    lanes = [l for l in lines if not l.startswith("Engine total")]
    for mb, m in (cfg.get("mailboxes") or {}).items():
        if any(l.startswith(mb + ":") for l in lanes):
            continue
        ramp = m.get("ramp") or []
        cap = ramp[0]["daily_cap"] if ramp else m.get("daily_cap", 0)
        start = m.get("active_from")
        when = f"starts {start}, then" if start and start > datetime.now(timezone.utc).strftime("%Y-%m-%d") else "from today,"
        ramp_txt = (" (ramp: " + ", ".join(f"{r['daily_cap']}/day from {r['from']}" for r in ramp) + ")") if ramp else ""
        lanes.append(f"{mb}: 0 waiting leads across 0 campaigns, {when} 0 days for one touch at {cap}/day{ramp_txt}")
    live["capacity"] = lanes + total


def build_motion_rows(engine_state: Dict[str, Any], impact: Dict[str, Any], registry: Dict[str, Any], credit_data: Dict[str, Any], play_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    motion_definitions = [
        ("star_ratings", "Star Ratings"),
        ("cost_mandate", "Cost-Mandate"),
        ("wfm_adjacency", "WFM-Adjacency"),
        ("back_office", "Back Office"),
    ]
    rows: List[Dict[str, Any]] = []
    funnel = engine_state.get("funnel", {}) or {}
    list_health = engine_state.get("list_health", {}) or {}
    accounts_by_motion = list_health.get("accounts_by_motion", {}) or {}
    for key, label in motion_definitions:
        motion_funnel = funnel.get(key, {}) if isinstance(funnel, dict) else {}
        universe = accounts_by_motion.get(key, 0)
        contacts = 0
        if key == "star_ratings":
            contacts = int(funnel.get("targets", {}).get("back_office_contacts", 0)) if isinstance(funnel.get("targets", {}), dict) else 0
        sent = motion_funnel.get("messages_sent", 0) if isinstance(motion_funnel, dict) else 0
        delivered = motion_funnel.get("delivered", 0) if isinstance(motion_funnel, dict) else 0
        replies = motion_funnel.get("replies", 0) if isinstance(motion_funnel, dict) else 0
        qualified_replies = motion_funnel.get("qualified_replies", 0) if isinstance(motion_funnel, dict) else 0
        meetings_booked = motion_funnel.get("meetings_booked", 0) if isinstance(motion_funnel, dict) else 0
        registry_entry = registry.get("motion_statuses", {}).get(key, {})
        # Stars is the origin motion the whole engine was built from; the registry
        # tabulates the cloned motions but not Stars itself, so default it to BUILT.
        default_state = "BUILT" if key == "star_ratings" else "PLANNED"
        build_state = (registry_entry.get("status") or default_state).upper().replace("**", "")
        if build_state not in {"BUILT", "PLANNED", "BLOCKED"}:
            build_state = default_state
        blockers = [b["text"] for b in registry.get("blockers", []) if key in b.get("motions", [])]
        next_action = "—"
        if key == "star_ratings":
            next_action = "Review seeded funnel, keep warmup and baseline blockers visible"
        elif key == "cost_mandate":
            next_action = "Re-source the proof-slice accounts against real-fit signals"
        elif key == "wfm_adjacency":
            next_action = "Keep workflow proof and registry bug visibility intact"
        elif key == "back_office":
            next_action = "Use install-base archetype as the next build reference"
        rows.append({
            "key": key,
            "label": label,
            "build_state": build_state,
            "universe": universe,
            "universe_trust": "LIVE" if universe else "SEEDED",
            "contacts": contacts,
            "funnel": {"sent": sent, "delivered": delivered, "replies": replies, "qualified_replies": qualified_replies, "meetings_booked": meetings_booked},
            "funnel_trust": "SEEDED" if sent == 0 and (not motion_funnel.get("messages_sent") or motion_funnel.get("messages_sent") == 0) else "LIVE",
            "next_action": next_action,
            "blockers": blockers,
        })
    return rows


def build_state() -> Dict[str, Any]:
    engine_state = read_json(ENGINE_STATE_PATH)
    impact = read_json(IMPACT_PATH)
    credit_data = parse_credit_ledger(CREDIT_LEDGER_PATH)
    registry = parse_registry(CLAY_REGISTRY_PATH)
    account_plays = read_json(ACCOUNT_PLAYS_PATH)
    readout_entries = parse_readout_log(READOUT_LOG_PATH)

    overall_posture = "BUILD"
    funnel_total_sent = 0
    for motion in engine_state.get("funnel", {}).values():
        if isinstance(motion, dict):
            funnel_total_sent += int(motion.get("messages_sent", 0) or 0)
    if funnel_total_sent > 0:
        overall_posture = "LAUNCHING"

    headline = f"{len([m for m in engine_state.get('funnel', {}).keys() if isinstance(engine_state.get('funnel', {}).get(m), dict)])} motions in build, {funnel_total_sent} sends by design, {credit_data['spent']:.0f} credits used"
    if funnel_total_sent > 0:
        headline = f"{funnel_total_sent} sends live, {credit_data['spent']:.0f} credits used, funnel still needs live verification"

    live = read_live_campaigns()
    fill_capacity_lanes(live)
    if live.get("per_motion"):
        engine = {k: v for k, v in live["per_motion"].items() if k != "Rep-built"}
        loaded = sum(m["leads"] for m in engine.values()); launched = sum(m["launched"] for m in engine.values())
        waiting = sum(m["waiting"] for m in engine.values()); replies = sum(m["replies"] for m in engine.values())
        meetings = sum(m["meetings"] for m in engine.values())
        overall_posture = "LAUNCHING" if launched else "BUILD"
        headline = (f"{loaded:,} leads loaded across {sum(m['campaigns'] for m in engine.values())} engine campaigns, "
                    f"{launched:,} launched, {waiting:,} waiting on first-touch capacity, {replies} replies, {meetings} meetings, "
                    f"{credit_data['spent']:.0f} credits used")

    deliverability = engine_state.get("deliverability", {}) or {}
    domains = deliverability.get("domains", []) or []
    non_example_domains = [d for d in domains if not d.get("example")]
    if not non_example_domains:
        non_example_domains = domains
    overall_health = deliverability.get("overall_health", "warming")
    last_checked = deliverability.get("last_checked", "")
    if last_checked and is_stale(last_checked, 1):
        gate = "UNKNOWN"
    elif overall_health.lower() in {"green", "healthy"}:
        gate = "GREEN"
    elif overall_health.lower() in {"amber", "warming"}:
        gate = "AMBER"
    else:
        gate = "RED"

    baseline_ratified = bool(engine_state.get("baseline", {}).get("ratified_with_naveen", False))

    motions = build_motion_rows(engine_state, impact, registry, credit_data, account_plays)

    signals = []
    for account in account_plays.get("accounts", [])[:8]:
        triggers = account.get("triggers") or []
        highest_trigger = None
        for trigger in triggers:
            if highest_trigger is None or trigger.get("score", 0) > highest_trigger.get("score", 0):
                highest_trigger = trigger
        signals.append({
            "company": account.get("company"),
            "tier": account.get("tier"),
            "why_now": account.get("why_now_raw"),
            "roi_label": account.get("roi_label"),
            "top_play": highest_trigger.get("play") if highest_trigger else "—",
            "fresh": bool(account.get("fresh")),
        })

    gate_integrity = read_gate_integrity()
    signal_review = read_signal_review()
    heat = read_heat_list()
    war_room = read_war_room()
    accounts = read_accounts_in_motion(live)
    stamp_heat(accounts, heat)

    blockers_and_asks = []
    registry_blockers = registry.get("blockers", [])
    # Open blockers first, then any resolved-but-noted ones.
    ordered_blockers = sorted(registry_blockers, key=lambda b: not b.get("open", False))
    for blocker in ordered_blockers[:4]:
        blockers_and_asks.append({
            "type": "blocker",
            "source": blocker.get("source", "Clay registry"),
            "text": blocker.get("text", ""),
            "open": blocker.get("open", False),
        })
    blockers_and_asks.extend(gate_integrity_asks(gate_integrity["as_of"]))
    readout = read_naveen_readout()
    if readout.get("bluf"):
        blockers_and_asks.append({"type": "readout", "source": f"Friday readout draft {readout['as_of']}", "text": readout["bluf"], "open": False})

    state = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "overall": {
            "posture": overall_posture,
            "headline": headline,
            "gates": {
                "deliverability": gate,
                "credit_budget": "GREEN" if credit_data["pct_consumed"] < 0.60 else "AMBER" if credit_data["pct_consumed"] < 0.85 else "RED",
                "baseline_ratified": baseline_ratified,
            },
        },
        "motions": motions,
        "funnel_surfaced": {
            "roi_surfaced_label": impact.get("headline_opportunity_label", "$0"),
            "strike_plans": impact.get("net_new", {}).get("strike_plans", 0),
            "messages_drafted": impact.get("net_new", {}).get("sequence_messages_drafted", 0),
            "committee_contacts": impact.get("net_new", {}).get("committee_contacts_mapped", 0),
            "trust": "SEEDED",
        },
        # REALIZED was hardcoded here until 2026-08-07. That meant any number impact.json
        # happened to contain rendered as a hard realized result, including the two
        # interview-era demo rows dated before the role started. The label now has to be
        # earned: the impact source must be present, must not be stale, and must not have
        # dropped rows at the ROLE_START gate. Anything else reads UNVERIFIED, which is the
        # honest state, rather than silently borrowing the authority of "REALIZED".
        "funnel_realized": {
            "meetings_booked": impact.get("realized", {}).get("meetings_booked", 0),
            "pipeline_label": impact.get("realized", {}).get("pipeline_created_label", "$0"),
            "revenue_label": impact.get("realized", {}).get("revenue_won_label", "$0"),
            "logged_outcomes": impact.get("realized", {}).get("logged_outcomes", 0),
            "excluded_pre_role_rows": impact.get("realized", {}).get("excluded_pre_role_rows", 0),
            "trust": realized_trust(impact),
        },
        "deliverability": {
            "overall": deliverability.get("overall_health", "warming"),
            "last_checked": deliverability.get("last_checked", ""),
            "domains": domains,
            "floor": engine_state.get("baseline", {}).get("deliverability_floor", {}),
            "trust": "STALE" if is_stale(deliverability.get("last_checked"), 1) else "LIVE",
        },
        "credits": {
            "spent": credit_data["spent"],
            "remaining": credit_data["remaining"],
            "budget": credit_data["budget"],
            "pct_consumed": credit_data["pct_consumed"],
            "flag_60pct": credit_data["flag_60pct"],
            "cost_per_qualified_reply": None,
            "trust": credit_data["trust"],
        },
        "approval_queue": {
            "pending": engine_state.get("approval_queue", {}).get("pending", 0),
            "approved_today": engine_state.get("approval_queue", {}).get("approved_today", 0),
            "rejected_today": engine_state.get("approval_queue", {}).get("rejected_today", 0),
            "items": [item for item in engine_state.get("approval_queue", {}).get("items", []) if not item.get("example")],
            "trust": "SEEDED" if engine_state.get("approval_queue", {}).get("pending", 0) == 0 else "LIVE",
        },
        "signals": signals,
        "live_campaigns": live,
        "deliverability_watch": read_deliverability_watch(),
        "swarm": read_swarm(),
        "accounts_in_motion": accounts,
        "gate_integrity": gate_integrity,
        "signal_review": signal_review,
        "heat_list": heat,
        "war_room": war_room,
        "blockers_and_asks": blockers_and_asks,
        "sources": [
            {"name": "gate_integrity", "last_updated": gate_integrity["as_of"], "status": gate_integrity["trust"], "stale": gate_integrity["trust"] != "LIVE", "feeds": "customer exclusion gate"},
            {"name": "signal_review", "last_updated": signal_review["as_of"], "status": signal_review["trust"], "stale": signal_review["trust"] != "LIVE", "feeds": "human approval gate"},
            {"name": "war_room", "last_updated": war_room["as_of"], "status": war_room["trust"], "stale": war_room["trust"] != "LIVE", "feeds": "signals, dates to hold"},
            {"name": "heat_list", "last_updated": heat["as_of"], "status": heat["trust"], "stale": heat["trust"] != "LIVE", "feeds": "heat, account cards"},
            {
                "name": "engine_state",
                "last_updated": engine_state.get("_meta", {}).get("last_updated"),
                "status": engine_state.get("_meta", {}).get("status"),
                "stale": is_stale(engine_state.get("_meta", {}).get("last_updated"), 7),
            },
            {
                "name": "impact",
                "last_updated": impact.get("generated_at"),
                "status": "LIVE" if impact.get("generated_at") else "SEEDED",
                "stale": is_stale(impact.get("generated_at"), 7),
            },
            {
                "name": "clay_credit_ledger",
                "last_updated": credit_data.get("source_date"),
                "status": credit_data["trust"],
                "stale": credit_data["trust"] == "STALE",
            },
            {
                "name": "clay_build_registry",
                "last_updated": registry.get("last_verified"),
                "status": "LIVE" if registry.get("last_verified") else "SEEDED",
                "stale": is_stale(registry.get("last_verified"), 3),
            },
            {
                "name": "account_plays",
                "last_updated": account_plays.get("generated_at"),
                "status": "LIVE" if account_plays.get("generated_at") else "SEEDED",
                "stale": is_stale(account_plays.get("generated_at"), 3),
            },
            {
                "name": "naveen_readout",
                "last_updated": readout.get("as_of"),
                "status": "LIVE" if readout.get("as_of") else "MISSING",
                "stale": is_stale(readout.get("as_of"), 9),
                "feeds": "readout line on blockers",
            },
        ],
    }
    return state


def main() -> None:
    state = build_state()
    with OUTPUT_PATH.open("w", encoding="utf-8") as handle:
        json.dump(state, handle, indent=2)
        handle.write("\n")
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
