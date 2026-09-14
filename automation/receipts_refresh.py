#!/usr/bin/env python3
"""receipts-refresh: a proposed receipts-ledger block, weekly, for Dallas to approve.

Built Sep 13 2026. The receipts ledger (automation/logs/credit_pipeline_receipts.md) is the renewal
artifact and it is written by hand, which is why it sat 56 days stale while eight campaigns sent.
This script reads what the engine already knows and drafts the block; it NEVER writes the ledger or
impact/outcomes.csv. Approval is a reply in the rundown thread; on approval the block is pasted in by
hand (or by a session on Dallas's word). Deterministic, no Claude call, 0 Clay credits, no DM.

Reads:
  automation/logs/campaign_scorecard_history.csv   latest row per campaign, aggregated per motion
  automation/logs/receipts_candidates.csv          unconfirmed replied/interested/meeting rises
  Clay_Credit_Ledger.md (repo root)                dated spend entries since the ledger's last date
  automation/logs/credit_pipeline_receipts.md      only to find the last 'As of' date and headline
  clay credits (CLI, optional, --no-clay skips)    live balance for the spend-log row

Writes:
  automation/logs/receipts-refresh-<date>.md       rundown source; PROPOSED BLOCK + approve line
  automation/logs/receipts_refresh_pending.json    the block and its id, for the thread listener

Usage: receipts_refresh.py [--date YYYY-MM-DD] [--out-dir DIR] [--ledger PATH] [--receipts PATH]
                           [--history PATH] [--candidates PATH] [--no-clay]
"""
import csv
import json
import os
import re
import shutil
import subprocess
import sys
from collections import defaultdict
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LOG_FAMILY = "receipts-refresh"
DATE_RX = re.compile(r"(20\d\d-\d\d-\d\d)")
CREDIT_RX = re.compile(r"(\d[\d,]*\.?\d*)\s*(?:Clay\s+)?credits?\b", re.I)


def opt(args, flag, default=None):
    return args[args.index(flag) + 1] if flag in args else default


def last_receipts_date(receipts_path):
    """The newest date anywhere in the receipts ledger; that is where the proposed block starts."""
    if not os.path.exists(receipts_path):
        return None, ""
    text = open(receipts_path).read()
    dates = sorted(set(DATE_RX.findall(text)))
    head = ""
    m = re.search(r"^As of (20\d\d-\d\d-\d\d):(.*)$", text, re.M)
    if m:
        head = m.group(0)[:200]
    return (dates[-1] if dates else None), head


def ledger_entries_since(ledger_path, since):
    """Dated entries in Clay_Credit_Ledger.md newer than `since`: (date, credits or None, purpose)."""
    out = []
    if not os.path.exists(ledger_path):
        return out
    for raw in open(ledger_path):
        line = raw.strip()
        m = re.match(r"^(20\d\d-\d\d-\d\d)\s*[·|]\s*(.*)$", line)
        if not m:
            m2 = re.match(r"^\|\s*(20\d\d-\d\d-\d\d)\s*\|(.*)$", line)
            if not m2:
                continue
            date, rest = m2.group(1), m2.group(2)
        else:
            date, rest = m.group(1), m.group(2)
        if since and date <= since:
            continue
        credits = None
        cm = CREDIT_RX.search(rest)
        if cm:
            try:
                credits = float(cm.group(1).replace(",", ""))
            except ValueError:
                credits = None
        purpose = re.sub(r"\s+", " ", rest.replace("|", " ").replace("**", "")).strip()[:140]
        out.append((date, credits, purpose))
    return out


def latest_per_campaign(history_path):
    rows = {}
    if not os.path.exists(history_path):
        return rows
    for r in csv.DictReader(open(history_path)):
        cid = r.get("campaign_id")
        if not cid:
            continue
        if cid not in rows or r["date"] > rows[cid]["date"]:
            rows[cid] = r
    return rows


def to_int(v):
    try:
        return int(float(v or 0))
    except ValueError:
        return 0


def live_balance():
    clay = shutil.which("clay")
    if not clay:
        cands = sorted(__import__("glob").glob(os.path.expanduser("~/.claude/plugins/cache/clay-plugins/clay/*/bin/clay")))
        clay = cands[-1] if cands else None
    if not clay:
        return None
    try:
        out = subprocess.run([clay, "credits"], capture_output=True, text=True, timeout=60).stdout
    except (subprocess.TimeoutExpired, OSError):
        return None
    m = re.search(r"(\d[\d,]*\.?\d*)", out.replace("\n", " "))
    try:
        return float(m.group(1).replace(",", "")) if m else None
    except ValueError:
        return None


def main(argv):
    args = argv[1:]
    today = opt(args, "--date", datetime.now().strftime("%Y-%m-%d"))
    out_dir = opt(args, "--out-dir", os.path.join(HERE, "logs"))
    ledger_path = opt(args, "--ledger", os.path.join(ROOT, "Clay_Credit_Ledger.md"))
    receipts_path = opt(args, "--receipts", os.path.join(HERE, "logs", "credit_pipeline_receipts.md"))
    history_path = opt(args, "--history", os.path.join(HERE, "logs", "campaign_scorecard_history.csv"))
    cand_path = opt(args, "--candidates", os.path.join(HERE, "logs", "receipts_candidates.csv"))
    os.makedirs(out_dir, exist_ok=True)

    since, old_head = last_receipts_date(receipts_path)
    entries = ledger_entries_since(ledger_path, since)
    spent = sum(c for _, c, _ in entries if c is not None)
    unpriced = sum(1 for _, c, _ in entries if c is None)
    latest = latest_per_campaign(history_path)
    by_motion = defaultdict(lambda: {"campaigns": 0, "leads": 0, "launched": 0, "replied": 0,
                                     "interested": 0, "meetings": 0, "bounced": 0, "unsubscribed": 0})
    for r in latest.values():
        m = by_motion[r.get("motion") or "Rep-built"]
        m["campaigns"] += 1
        m["leads"] += to_int(r.get("leads"))
        m["launched"] += to_int(r.get("leads")) - to_int(r.get("not_launched"))
        for k in ("replied", "interested", "meetings", "bounced", "unsubscribed"):
            m[k] += to_int(r.get(k))
    candidates = []
    if os.path.exists(cand_path):
        candidates = [c for c in csv.DictReader(open(cand_path)) if not since or c["date"] > since]
    balance = None if "--no-clay" in args else live_balance()
    as_of = max([today] + [r["date"] for r in latest.values()]) if latest else today

    block_id = f"receipts-{today}"
    eng = {k: v for k, v in by_motion.items() if k != "Rep-built"}
    tot = lambda k: sum(v[k] for v in eng.values())
    replies = tot("replied")
    meetings = tot("meetings")
    cpr = f"{spent / replies:,.0f} credits per reply" if replies and spent else "n/a"
    cpm = f"{spent / meetings:,.0f} credits per meeting" if meetings and spent else "n/a (0 meetings)"

    B = []
    B.append(f"## Headline (proposed {today}, block {block_id})")
    B.append(f"As of {as_of}: {spent:,.1f} credits logged in Clay_Credit_Ledger.md since {since or 'the start'}"
             + (f" ({unpriced} dated entries carry no credit figure)" if unpriced else "")
             + (f"; live balance {balance:,.1f}" if balance is not None else "")
             + f" -> engine campaigns: {tot('leads'):,} leads loaded, {tot('launched'):,} launched, "
             f"{replies} replies, {tot('interested')} interested, {meetings} booked meetings, $0 logged pipeline (outcomes.csv is Dallas's hand).")
    B.append("")
    B.append("## Spend by motion (engine funnel per campaign_scorecard_history.csv, latest read per campaign)")
    B.append("| Motion | Campaigns | Leads | Launched | Replies | Interested | Meetings | Bounced | Unsub |")
    B.append("|---|---|---|---|---|---|---|---|---|")
    for name, v in sorted(by_motion.items(), key=lambda kv: (kv[0] == "Rep-built", kv[0])):
        B.append(f"| {name} | {v['campaigns']} | {v['leads']} | {v['launched']} | {v['replied']} | {v['interested']} | {v['meetings']} | {v['bounced']} | {v['unsubscribed']} |")
    B.append("")
    B.append("## Spend log (proposed rows)")
    B.append("| Date | `clay credits` balance | Note |")
    B.append("|---|---|---|")
    for date, credits, purpose in entries:
        B.append(f"| {date} | | {('%.1f credits: ' % credits) if credits is not None else ''}{purpose} |")
    if balance is not None:
        B.append(f"| {today} | {balance:,.1f} | live balance at refresh |")
    B.append("")
    B.append("## Receipts (proposed rows, CANDIDATES until confirmed)")
    B.append("| Date | Motion | Account / Contact | Type | Status |")
    B.append("|---|---|---|---|---|")
    if candidates:
        for c in candidates:
            B.append(f"| {c['date']} | {c['campaign']} | (confirm lead in lemlist) | {c['metric']} {c['prior']} -> {c['now']} | CANDIDATE, unconfirmed ({c['evt']}) |")
    else:
        B.append("| | | | | no new candidates since " + (since or "the start") + " |")
    B.append("")
    B.append("## Metrics")
    B.append(f"- Cost per reply: {cpr}.")
    B.append(f"- Cost per booked meeting: {cpm}.")
    B.append("- Pipeline $ generated: $0 logged (only outcomes.csv rows count, and this script never writes them).")

    L = [f"# Receipts refresh {today} {datetime.now().strftime('%H:%M')}", "",
         "Deterministic weekly draft of the receipts ledger. This run wrote NOTHING to credit_pipeline_receipts.md, "
         "Clay_Credit_Ledger.md or impact/outcomes.csv. Approve the block below with `APPROVE " + block_id +
         "` in the rundown thread; on approval the block is pasted into the ledger by hand or by a session on Dallas's word.", "",
         f"- Receipts ledger last dated entry: {since or 'none found'}" + (f" ({old_head[:120]})" if old_head else ""),
         f"- Ledger entries since then: {len(entries)} dated lines, {spent:,.1f} credits with a figure, {unpriced} without.",
         f"- Scorecard history: {len(latest)} campaigns with a latest read" + (f", newest {as_of}" if latest else ", none (scorecard has not run)") + ".",
         f"- Receipts candidates since {since or 'the start'}: {len(candidates)}.",
         "", f"evt: {LOG_FAMILY}-{today}#{block_id}", "",
         "----- PROPOSED LEDGER BLOCK (paste on approval) -----", ""] + B + ["", "----- END BLOCK -----", ""]
    log_path = os.path.join(out_dir, f"{LOG_FAMILY}-{today}.md")
    open(log_path, "w").write("\n".join(L))
    json.dump({"id": block_id, "date": today, "since": since, "spent": spent, "replies": replies,
               "meetings": meetings, "candidates": len(candidates), "block": "\n".join(B),
               "status": "pending", "approve_with": f"APPROVE {block_id}"},
              open(os.path.join(out_dir, "receipts_refresh_pending.json"), "w"), indent=2)
    print(f"wrote {log_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
