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
    latest: Dict[str, Dict[str, str]] = {}
    with SCORECARD_HISTORY_PATH.open(encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            cid = row.get("campaign_id")
            if cid and (cid not in latest or row["date"] > latest[cid]["date"]):
                latest[cid] = row
    if not latest:
        return out
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
    readout = readout_entries[-1] if readout_entries else None
    if readout:
        blockers_and_asks.append({
            "type": "ask",
            "source": f"Readout {readout['date']}",
            "text": f"{readout['headline']} — Response: pending"
        })

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
        "live_campaigns": read_live_campaigns(),
        "blockers_and_asks": blockers_and_asks,
        "sources": [
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
                "name": "readout_log",
                "last_updated": readout_entries[-1].get("date") if readout_entries else None,
                "status": "LIVE" if readout_entries else "SEEDED",
                "stale": is_stale(readout_entries[-1].get("date") if readout_entries else None, 7),
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
