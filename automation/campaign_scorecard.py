#!/usr/bin/env python3
"""campaign-scorecard: the per-campaign funnel the receipts ledger never had.

Built Sep 13 2026 from the strategy review: eight campaigns had been sending for nine days and
no file in the repo could say how many leads were contacted, how many replied, or where the
sequences were stuck. This script reads lemlist directly (REST routes that are NOT plan-gated:
campaigns list, per-campaign lead export, open tasks) plus the relay's hourly stats snapshot, and
writes three things a human or the rundown can act on:

  1. automation/logs/campaign-scorecard-<date>.md   (rundown source; STALLED lines lead)
  2. automation/logs/campaign_scorecard_history.csv (one row per campaign per day, the trend)
  3. motions/pipeline_council/GTM_Engineering_Scorecard_<YYYY-MM>.csv (OKR O1 KR2, the council row)

It also appends automation/logs/receipts_candidates.csv whenever a campaign's replied, interested
or meetings count rises since the prior day, so a real reply can never vanish between hourly relay
runs and the hand-kept receipts ledger. It NEVER edits credit_pipeline_receipts.md or
impact/outcomes.csv; those stay Dallas's hand. Read-only on lemlist, 0 Clay credits, no Slack, no
DM. Chained after lemlist_pulse.py inside the hourly relay wrapper; history keeps the latest read
of each day.

Usage:
  campaign_scorecard.py                       live read, writes the three outputs
  campaign_scorecard.py --fixture f.json      offline (tests), no network
  campaign_scorecard.py --out-dir DIR         redirect logs/history/candidates (tests)
  campaign_scorecard.py --council-dir DIR     redirect the council CSV (tests)
  campaign_scorecard.py --date YYYY-MM-DD     stamp a date (tests)
  campaign_scorecard.py --no-seed             skip seeding open-task history from lemlist-pulse logs
  campaign_scorecard.py --capacity f.json     send-capacity config (default config/send_capacity.json)
"""
import csv
import glob
import json
import os
import re
import math
import subprocess
import sys
from collections import Counter
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
API = "https://api.lemlist.com/api"
LOG_FAMILY = "campaign-scorecard"

REPLIED_STATES = {"emailsReplied", "linkedinReplied", "smsReplied", "whatsappReplied", "replied"}
INTERESTED_STATES = {"interested", "emailsInterested", "linkedinInterested", "meetingBooked"}
BOUNCED_STATES = {"emailsBounced", "bounced"}
NOT_LAUNCHED_SYSTEMS = {"review", "reviewed", "toReview", "imported"}
# A running campaign counts as stalled when nothing about its leads has moved for this many days.
STALL_DAYS = 3

MOTION_RULES = [
    (re.compile(r"^stars", re.I), "Star Ratings"),
    (re.compile(r"^blitz", re.I), "Keegan Blitz"),
    (re.compile(r"^bo expansion", re.I), "Back Office (customer lanes)"),
    (re.compile(r"^bo net-new", re.I), "Back Office (net-new)"),
    (re.compile(r"^dwo exec", re.I), "DWO Executives"),
    (re.compile(r"^wfm present", re.I), "WFM Present"),
    (re.compile(r"^genesys", re.I), "Genesys Present"),
    (re.compile(r"^uk -", re.I), "UK named accounts"),
]

HISTORY_COLS = ["date", "campaign_id", "campaign", "motion", "rep", "status", "leads", "not_launched",
                "in_progress", "email_touch", "li_touch", "replied", "interested", "bounced",
                "unsubscribed", "meetings", "li_accepted", "open_tasks", "fingerprint", "mailbox", "waiting"]
COUNCIL_COLS = ["Campaign", "Motion", "Rep", "Status", "Leads loaded", "Leads launched", "Leads at email step",
                "Leads at LinkedIn step", "Replies", "Interested", "Meetings booked",
                "Opportunities (Salesforce)", "Bounced", "Unsubscribed", "Open rep tasks",
                "Clay credits", "Cost per meeting", "Mailbox", "Days to drain (alone)", "Source", "As of"]
CANDIDATE_COLS = ["date", "campaign_id", "campaign", "metric", "prior", "now", "evt"]


def slug(text):
    s = re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-")
    return "-".join(s.split("-")[:4]) or "campaign"


def motion_for(name):
    for rx, label in MOTION_RULES:
        if rx.search(name or ""):
            return label
    return "Rep-built"


# ---------- lemlist reads (live) ----------

def load_key():
    path = os.path.join(HERE, "config", "lemlist.env")
    with open(path) as f:
        for line in f:
            if line.startswith("LEMLIST_API_KEY="):
                return line.split("=", 1)[1].strip()
    sys.exit("LEMLIST_API_KEY not found in config/lemlist.env")


def rest_get(key, path):
    out = subprocess.run(["curl", "-s", "-u", f":{key}", f"{API}{path}"],
                         capture_output=True, text=True, timeout=90)
    try:
        return json.loads(out.stdout)
    except json.JSONDecodeError:
        return {"_error": out.stdout[:200]}


def live_read():
    key = load_key()
    chan = json.load(open(os.path.join(HERE, "config", "lemlist_channels.json")))
    cmap = chan.get("campaign_channel_map", {})
    camps = rest_get(key, "/campaigns?version=v2&limit=100")
    clist = camps.get("campaigns", []) if isinstance(camps, dict) else camps
    names = {}
    if isinstance(clist, list):
        for c in clist:
            if c.get("_id"):
                names[c["_id"]] = {"name": c.get("name"), "status": c.get("status")}
    if not names:  # plan-gated or empty: fall back to the pulse's last state file
        try:
            names = json.load(open(os.path.join(HERE, "config", "lemlist_pulse_state.json")))
        except (FileNotFoundError, json.JSONDecodeError):
            names = {}
    tasks_resp = rest_get(key, "/tasks?filters=%5B%5D")
    tasks = tasks_resp.get("results", []) if isinstance(tasks_resp, dict) else []
    open_tasks = Counter(t.get("campaignId") for t in tasks if t.get("campaignId"))
    unmapped_tasks = sum(1 for t in tasks if not t.get("campaignId"))
    relay = {}
    try:
        relay = json.load(open(os.path.join(HERE, "logs", ".lemlist-relay-stats.json"))).get("campaigns", {})
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    campaigns = {}
    for cid, rep in cmap.items():
        leads = rest_get(key, f"/campaigns/{cid}/export/leads?state=all&format=json")
        if not isinstance(leads, list):
            leads = []
            err = True
        else:
            err = False
        meta = names.get(cid, {})
        campaigns[cid] = {
            "name": meta.get("name") or cid, "status": meta.get("status") or "unknown", "rep": rep,
            "leads": [{"state": x.get("state"), "stateSystem": x.get("stateSystem")} for x in leads],
            "open_tasks": open_tasks.get(cid, 0), "export_error": err,
        }
    return {"campaigns": campaigns, "relay": relay, "unmapped_open_tasks": unmapped_tasks,
            "total_open_tasks": len(tasks)}


# ---------- metrics ----------

def summarize(cid, c, relay):
    leads = c.get("leads", [])
    states = Counter(x.get("state") or "?" for x in leads)
    systems = Counter(x.get("stateSystem") or "?" for x in leads)
    not_launched = sum(n for s, n in systems.items() if s in NOT_LAUNCHED_SYSTEMS)
    in_progress = systems.get("inProgress", 0)
    email_touch = sum(n for s, n in states.items() if s.startswith("emails") and s not in BOUNCED_STATES)
    li_touch = sum(n for s, n in states.items() if s.startswith("linkedin"))
    replied = sum(n for s, n in states.items() if s in REPLIED_STATES)
    interested = sum(n for s, n in states.items() if s in INTERESTED_STATES)
    bounced = sum(n for s, n in states.items() if s in BOUNCED_STATES)
    unsub = systems.get("unsubscribed", 0)
    r = relay.get(cid, {}) if relay else {}
    fingerprint = "|".join(f"{k}={v}" for k, v in sorted(states.items()))
    return {
        "campaign_id": cid, "campaign": c.get("name") or cid, "motion": motion_for(c.get("name")),
        "rep": c.get("rep") or "?", "status": c.get("status") or "unknown", "leads": len(leads),
        "not_launched": not_launched, "in_progress": in_progress, "email_touch": email_touch,
        "li_touch": li_touch, "replied": replied, "interested": interested, "bounced": bounced,
        "unsubscribed": unsub, "meetings": int(r.get("meetingBooked", 0) or 0),
        "li_accepted": int(r.get("linkedinInvitationAccepted", 0) or 0),
        "open_tasks": int(c.get("open_tasks", 0) or 0), "fingerprint": fingerprint,
        "export_error": bool(c.get("export_error")),
    }


# ---------- send capacity ----------

def effective_cap(mb, date):
    cap = int(mb.get("daily_cap", 0) or 0)
    for step in sorted(mb.get("ramp", []), key=lambda s: s.get("from", "")):
        if step.get("from", "") <= date:
            cap = int(step.get("daily_cap", cap) or cap)
    return cap


def capacity_plan(rows, cfg, today):
    """Assign each campaign a mailbox and compute days to drain the waiting (never launched) leads,
    per campaign alone and per mailbox in aggregate. Pure arithmetic on the config; no network."""
    mboxes = cfg.get("mailboxes", {})
    by_rep = cfg.get("default_mailbox_by_rep", {})
    explicit = cfg.get("campaign_mailbox", {})
    per_mb = {}
    for r in rows:
        name = explicit.get(r["campaign_id"]) or by_rep.get(r["rep"]) or ""
        r["mailbox"] = name
        r["waiting"] = r["not_launched"]
        mb = mboxes.get(name)
        if not mb:
            r["days_alone"] = ""
            continue
        start = mb.get("active_from", "") or today
        cap = effective_cap(mb, max(today, start))
        r["days_alone"] = math.ceil(r["waiting"] / cap) if cap and r["waiting"] else 0
        agg = per_mb.setdefault(name, {"waiting": 0, "campaigns": 0, "cap": cap, "start": start, "mb": mb})
        agg["waiting"] += r["waiting"]
        agg["campaigns"] += 1 if r["waiting"] else 0
    lines = []
    for name, agg in sorted(per_mb.items()):
        cap = agg["cap"]
        days = math.ceil(agg["waiting"] / cap) if cap and agg["waiting"] else 0
        when = f"starts {agg['start']}, then" if agg["start"] > today else "from today,"
        ramp = agg["mb"].get("ramp")
        ramp_txt = " (ramp: " + ", ".join(f"{s['daily_cap']}/day from {s['from']}" for s in ramp) + ")" if ramp else ""
        note = agg["mb"].get("note", "")
        unverified = " UNVERIFIED cap" if "UNVERIFIED" in note.upper() else ""
        lines.append(f"- {name}: {agg['waiting']} waiting leads across {agg['campaigns']} campaigns, {when} {days} days for one touch at {cap}/day{ramp_txt}{unverified}")
    return lines


# ---------- history ----------

def read_history(path):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return list(csv.DictReader(f))


def write_history(path, rows):
    rows = sorted(rows, key=lambda r: (r["date"], r["campaign_id"]))
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=HISTORY_COLS, extrasaction="ignore")
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in HISTORY_COLS})


def seed_from_pulse(logs_dir, today, known):
    """Seed open-task history from prior lemlist-pulse logs (per-campaign '- <cid> | <type>: N open')
    so the stall rule has a real trend on the first run instead of waiting three days."""
    rows = []
    rx = re.compile(r"^- (cam_\w+) \| [\w?]+: (\d+) open")
    for path in sorted(glob.glob(os.path.join(logs_dir, "lemlist-pulse-????-??-??.md"))):
        date = os.path.basename(path)[len("lemlist-pulse-"):-3]
        if date >= today:
            continue
        per = Counter()
        status = {}
        with open(path) as f:
            for line in f:
                m = rx.match(line.strip())
                if m:
                    per[m.group(1)] += int(m.group(2))
                m2 = re.match(r"^- (.+?) \| status: (\w+) \| id: (cam_\w+)", line.strip())
                if m2:
                    status[m2.group(3)] = m2.group(2)
        for cid in known:
            if cid in per or cid in status:
                rows.append({"date": date, "campaign_id": cid, "campaign": known[cid],
                             "status": status.get(cid, ""), "open_tasks": per.get(cid, 0),
                             "fingerprint": ""})
    return rows


def stall_verdict(today_row, history):
    """STALLED when a running campaign with leads in flight and open rep tasks has shown no lead
    movement for STALL_DAYS+ days. Returns (verdict, days, note)."""
    if today_row["status"] != "running":
        return ("", 0, "")
    if today_row["in_progress"] == 0 and today_row["not_launched"] == today_row["leads"]:
        return ("", 0, "")
    prior = sorted([h for h in history if h["campaign_id"] == today_row["campaign_id"]
                    and h["date"] < today_row["date"]], key=lambda h: h["date"])
    if not prior:
        return ("WATCH", 0, "first read, no history yet")
    same = []
    for h in reversed(prior):
        fp_same = (h.get("fingerprint") or "") in ("", today_row["fingerprint"])
        tasks_same = int(h.get("open_tasks") or 0) >= today_row["open_tasks"] and today_row["open_tasks"] > 0
        moved = (h.get("fingerprint") and h["fingerprint"] != today_row["fingerprint"])
        if moved or (not fp_same and not tasks_same):
            break
        same.append(h["date"])
    if not same:
        return ("", 0, "")
    d0 = datetime.strptime(same[-1], "%Y-%m-%d")
    d1 = datetime.strptime(today_row["date"], "%Y-%m-%d")
    days = (d1 - d0).days
    if days >= STALL_DAYS and today_row["open_tasks"] > 0:
        return ("STALLED", days, f"no lead movement since {same[-1]}, {today_row['open_tasks']} open rep tasks")
    return ("WATCH", days, f"unchanged since {same[-1]}")


# ---------- outputs ----------

def council_rows(rows, today, spend):
    out = []
    for r in rows:
        credits = spend.get(r["campaign_id"], "")
        cpm = ""
        if credits != "" and r["meetings"]:
            try:
                cpm = f"{float(credits) / r['meetings']:.1f}"
            except (TypeError, ValueError):
                cpm = ""
        out.append({
            "Campaign": r["campaign"], "Motion": r["motion"], "Rep": r["rep"], "Status": r["status"],
            "Leads loaded": r["leads"], "Leads launched": r["leads"] - r["not_launched"],
            "Leads at email step": r["email_touch"], "Leads at LinkedIn step": r["li_touch"], "Replies": r["replied"],
            "Interested": r["interested"], "Meetings booked": r["meetings"],
            "Opportunities (Salesforce)": "", "Bounced": r["bounced"], "Unsubscribed": r["unsubscribed"],
            "Open rep tasks": r["open_tasks"], "Clay credits": credits, "Cost per meeting": cpm,
            "Mailbox": r.get("mailbox", ""), "Days to drain (alone)": r.get("days_alone", ""),
            "Source": "GTM Engineering", "As of": today,
        })
    return out


def main(argv):
    args = argv[1:]
    def opt(flag, default=None):
        return args[args.index(flag) + 1] if flag in args else default
    today = opt("--date", datetime.now().strftime("%Y-%m-%d"))
    out_dir = opt("--out-dir", os.path.join(HERE, "logs"))
    council_dir = opt("--council-dir", os.path.join(ROOT, "motions", "pipeline_council"))
    fixture = opt("--fixture")
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(council_dir, exist_ok=True)

    data = json.load(open(fixture)) if fixture else live_read()
    relay = data.get("relay", {})
    rows = [summarize(cid, c, relay) for cid, c in data["campaigns"].items()]
    for r in rows:
        r["date"] = today

    hist_path = os.path.join(out_dir, "campaign_scorecard_history.csv")
    history = read_history(hist_path)
    if not history and "--no-seed" not in args and not fixture:
        history = seed_from_pulse(out_dir, today, {r["campaign_id"]: r["campaign"] for r in rows})
    if fixture and not history and data.get("seed_history"):
        history = data["seed_history"]

    # stall verdicts and receipts candidates use history BEFORE today's rows are merged
    verdicts = {r["campaign_id"]: stall_verdict(r, history) for r in rows}
    candidates = []
    for r in rows:
        prior = sorted([h for h in history if h["campaign_id"] == r["campaign_id"] and h["date"] < today],
                       key=lambda h: h["date"])
        if not prior:
            continue
        last = prior[-1]
        for metric in ("replied", "interested", "meetings"):
            try:
                before = int(last.get(metric) or 0)
            except ValueError:
                before = 0
            if r[metric] > before:
                candidates.append({"date": today, "campaign_id": r["campaign_id"], "campaign": r["campaign"],
                                   "metric": metric, "prior": before, "now": r[metric],
                                   "evt": f"{LOG_FAMILY}-{today}#{slug(r['campaign'])}-{metric}"})

    cap_path = opt("--capacity", os.path.join(HERE, "config", "send_capacity.json"))
    try:
        cap_cfg = json.load(open(cap_path))
    except (FileNotFoundError, json.JSONDecodeError):
        cap_cfg = {}
    capacity_lines = capacity_plan(rows, cap_cfg, today)
    merged = [h for h in history if not (h["date"] == today and h["campaign_id"] in {r["campaign_id"] for r in rows})]
    merged.extend(rows)
    write_history(hist_path, merged)

    cand_path = os.path.join(out_dir, "receipts_candidates.csv")
    if candidates and os.path.exists(cand_path):  # hourly re-runs on the same day must not re-mint
        seen = {(c["date"], c["campaign_id"], c["metric"], c["now"]) for c in csv.DictReader(open(cand_path))}
        candidates = [c for c in candidates if (c["date"], c["campaign_id"], c["metric"], str(c["now"])) not in seen]
    if candidates:
        new_file = not os.path.exists(cand_path)
        with open(cand_path, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=CANDIDATE_COLS)
            if new_file:
                w.writeheader()
            for c in candidates:
                w.writerow(c)

    spend = {}
    spend_path = os.path.join(HERE, "config", "campaign_spend.json")
    if os.path.exists(spend_path):
        try:
            spend = json.load(open(spend_path)).get("credits_by_campaign", {})
        except json.JSONDecodeError:
            spend = {}
    council_path = os.path.join(council_dir, f"GTM_Engineering_Scorecard_{today[:7]}.csv")
    with open(council_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COUNCIL_COLS)
        w.writeheader()
        for row in council_rows(sorted(rows, key=lambda r: (r["motion"], r["campaign"])), today, spend):
            w.writerow(row)

    # ---------- the log ----------
    eng = [r for r in rows if r["motion"] != "Rep-built"]
    by_status = Counter(r["status"] for r in eng)
    L = [f"# Campaign scorecard {today} {datetime.now().strftime('%H:%M')}", "",
         "Read-only lemlist read (campaign list, lead export, open tasks) plus the relay stats snapshot. "
         "0 Clay credits, nothing sent, nobody messaged. History: campaign_scorecard_history.csv. "
         "Council CSV: " + os.path.relpath(council_path, ROOT) + ". Receipts candidates never edit the ledger.", ""]
    L.append("## Headline")
    L.append(f"- Engine campaigns mapped: {len(eng)} ({', '.join(f'{k} {v}' for k, v in by_status.most_common())}); "
             f"rep-built mapped: {len(rows) - len(eng)}.")
    tot = lambda k, pool: sum(r[k] for r in pool)
    L.append(f"- Engine funnel, lifetime: leads loaded {tot('leads', eng)}, launched {tot('leads', eng) - tot('not_launched', eng)}, "
             f"last touch email {tot('email_touch', eng)}, last touch LinkedIn {tot('li_touch', eng)} (current lead state, not cumulative sends), replies {tot('replied', eng)}, "
             f"interested {tot('interested', eng)}, meetings {tot('meetings', eng)}, bounced {tot('bounced', eng)}, "
             f"unsubscribed {tot('unsubscribed', eng)}.")
    L.append(f"- Loaded but never launched (engine): {tot('not_launched', eng)} leads across "
             f"{sum(1 for r in eng if r['not_launched'] == r['leads'] and r['leads'])} campaigns.")
    L.append(f"- Open rep tasks across mapped campaigns: {sum(r['open_tasks'] for r in rows)}"
             + (f" (+{data.get('unmapped_open_tasks', 0)} on unmapped campaigns)" if data.get("unmapped_open_tasks") else "") + ".")
    errs = [r["campaign"] for r in rows if r.get("export_error")]
    if errs:
        L.append(f"- EXPORT ERROR on {len(errs)} campaign(s), counts above exclude them: {', '.join(errs)}.")
    L.append("")
    L.append("## Send capacity (waiting = loaded, never launched; caps from config/send_capacity.json)")
    if capacity_lines:
        L.extend(capacity_lines)
        combined = sum(r["waiting"] for r in eng)
        L.append(f"- Engine total waiting: {combined} leads. First-touch capacity is the binding constraint until the second mailbox is live; wave sizing comes from these lines, not from list size.")
    else:
        L.append("- no capacity config found (config/send_capacity.json)")
    L.append("")
    stalled = [(r, verdicts[r["campaign_id"]]) for r in rows if verdicts[r["campaign_id"]][0] == "STALLED"]
    watch = [(r, verdicts[r["campaign_id"]]) for r in rows if verdicts[r["campaign_id"]][0] == "WATCH"]
    L.append("## STALLED (running campaign, leads in flight, no movement for 3+ days, rep tasks open)")
    if stalled:
        for r, (v, days, note) in stalled:
            L.append(f"- STALLED {days}d: {r['campaign']} ({r['rep']}) | {r['in_progress']} leads in flight, {note}")
            L.append(f"  evt: {LOG_FAMILY}-{today}#{slug(r['campaign'])}-stalled")
    else:
        L.append("- none")
    if watch:
        L.append("")
        L.append("## WATCH (running, unchanged, under the 3-day line or first read)")
        for r, (v, days, note) in watch:
            L.append(f"- {r['campaign']} ({r['rep']}) | {r['in_progress']} in flight, {r['open_tasks']} open tasks, {note}")
    L.append("")
    L.append("## Receipts candidates (new since the prior day; confirm before they reach the ledger)")
    if candidates:
        for c in candidates:
            L.append(f"- {c['campaign']}: {c['metric']} {c['prior']} -> {c['now']}")
            L.append(f"  evt: {c['evt']}")
    else:
        L.append("- none")
    L.append("")
    L.append("## Per campaign")
    L.append("| Campaign | Motion | Rep | Status | Leads | Launched | At email | At LinkedIn | Replies | Interested | Meetings | Bounced | Unsub | Open tasks | Verdict |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in sorted(rows, key=lambda r: (r["motion"] == "Rep-built", r["motion"], r["campaign"])):
        v = verdicts[r["campaign_id"]]
        vtxt = f"{v[0]} {v[1]}d" if v[0] else ""
        L.append(f"| {r['campaign']} | {r['motion']} | {r['rep']} | {r['status']} | {r['leads']} | {r['leads'] - r['not_launched']} | "
                 f"{r['email_touch']} | {r['li_touch']} | {r['replied']} | {r['interested']} | {r['meetings']} | {r['bounced']} | "
                 f"{r['unsubscribed']} | {r['open_tasks']} | {vtxt} |")
    L.append("")
    log_path = os.path.join(out_dir, f"{LOG_FAMILY}-{today}.md")
    with open(log_path, "w") as f:
        f.write("\n".join(L) + "\n")
    print(f"wrote {log_path}")
    print(f"wrote {council_path}")
    if stalled:
        print(f"STALLED: {len(stalled)}")
    if candidates:
        print(f"receipts candidates: {len(candidates)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
