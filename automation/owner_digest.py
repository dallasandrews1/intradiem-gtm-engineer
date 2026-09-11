#!/usr/bin/env python3
"""Owner digest composer. Deterministic: reads tracker rows + newest account-health log, groups open items by owner,
writes automation/logs/owner-digest-<date>.md containing (a) one section per owner, (b) a DRAFTS block the agent turns
into Outlook drafts (never sends), (c) the rundown block for Dallas, (d) unrouted owners. Usage: --date YYYY-MM-DD --dry-run"""
import json, csv, glob, pathlib, datetime, argparse, re, html as H
ROOT = pathlib.Path(__file__).resolve().parent.parent
ap = argparse.ArgumentParser(); ap.add_argument("--date"); ap.add_argument("--dry-run", action="store_true"); a = ap.parse_args()
today = datetime.date.fromisoformat(a.date) if a.date else datetime.date.today()
cfg = json.loads((ROOT / "automation/config/owner_digest.json").read_text())
# Verified contacts per account, from the save-room data (only verified or Salesforce emails ever leave this composer)
def verified_contacts(acct):
    p = ROOT / "motions/churn_risk_save_plan/data" / f"save_room_{acct.lower().replace(' ', '_')}.json"
    if not p.exists(): return []
    d = json.loads(p.read_text()); out = []
    for r in d.get("inger", []):
        em = r.get("email_validated") or r.get("email")
        if em and r.get("bridge") != "departed":
            out.append((r["name"], r.get("title_live") or r.get("title_inger", ""), em, r.get("track", "")))
    return out

def parse_due(s):
    for f in ("%m/%d/%Y", "%Y-%m-%d", "%m/%d/%y"):
        try: return datetime.datetime.strptime(s.strip(), f).date()
        except Exception: pass
    return None

rows = []
paths = [ROOT / p for p in cfg["tracker_sources"]] + [pathlib.Path(p) for p in glob.glob(str(ROOT / cfg["tracker_export_glob"]))]
for p in paths:
    if not p.exists(): continue
    for r in csv.DictReader(open(p, encoding="utf-8-sig")):
        if r.get("Project Name", "").strip() in cfg["accounts"] and r.get("Task Progress", "").strip() not in ("Completed", "N/A") and r.get("Archive?", "No").strip() != "Yes":
            r["_src"] = p.name; rows.append(r)
# dedupe on account+task+description
seen = set(); items = []
for r in rows:
    k = (r["Project Name"], r["Task Name"].strip(), r["Task Description"].strip()[:80])
    if k in seen: continue
    seen.add(k); items.append(r)

# newest health log: overall + red codes + newest evidence per account
fam = cfg["health_log_family"]; logs = sorted((ROOT / "automation/logs").glob(f"{fam}-*.md"))
health = {}
if logs:
    cur = None
    for l in logs[-1].read_text().splitlines():
        m = re.match(r"## (.+?): (RED|YELLOW|GREEN) \((.+?)\)", l)
        if m: cur = m.group(1); health[cur] = {"overall": m.group(2), "detail": m.group(3), "reds": [], "log": logs[-1].name}
        m2 = re.match(r"- \*\*(.+?): RED\*\*", l)
        if m2 and cur: health[cur]["reds"].append(m2.group(1))
    health_age = (today - datetime.date.fromisoformat(logs[-1].name[len(fam)+1:-3])).days
else: health_age = None

by_owner = {}
for r in items:
    for o in [x.strip() for x in (r["Assigned To"] + ";" + r.get("Additional Assignees", "")).split(";") if x.strip()]:
        by_owner.setdefault(o, []).append(r)

def status_line(acct):
    h = health.get(acct)
    if not h: return f"{acct}: no health log."
    return f"{acct}: {h['overall']} ({h['detail']}); red: {', '.join(h['reds']) or 'none'}."

L = [f"# Owner digest, {today}", "", f"RUN COMPLETE {datetime.datetime.now():%H:%M} (composer). Items: {len(items)} open across {len(cfg['accounts'])} account(s); health log age {health_age} days." if health_age is not None else "No health log found.", ""]
drafts = []
for owner, its in sorted(by_owner.items()):
    route = cfg["owners"].get(owner, {"channel": "unrouted"})
    overdue = [r for r in its if (d := parse_due(r["Task Due Date"])) and d < today]
    L += [f"## {owner} ({route['channel']}): {len(its)} open, {len(overdue)} overdue"]
    for r in its:
        d = parse_due(r["Task Due Date"]); flag = " OVERDUE" if d and d < today else ""
        L.append(f"- [{r['Project Name']}] {r['Task Name']}: {r['Task Description']} (due {r['Task Due Date'] or 'none'}, {r['Task Progress']}){flag}")
    L.append("")
    if route["channel"] == "outlook_draft":
        accts = sorted({r["Project Name"] for r in its})
        first = owner.split()[0]
        body = [f"<p>Hi {H.escape(first)},</p>", "<p>Your open items this week:</p>", "<ul>"]
        for r in its:
            d = parse_due(r["Task Due Date"]); od = " <b>(overdue)</b>" if d and d < today else ""
            body.append(f"<li><b>{H.escape(r['Task Name'])}</b>: {H.escape(r['Task Description'])}. Due {H.escape(r['Task Due Date'] or 'not set')}.{od}</li>")
        body.append("</ul>")
        for acct in accts:
            body.append(f"<p>{H.escape(status_line(acct))}</p>")
            vc = verified_contacts(acct)
            if vc and route.get("contacts_block", True):
                body.append(f"<p>Verified contacts at {H.escape(acct)} (emails checked, ready to use):</p><ul>")
                for n, t, em, tr in vc: body.append(f"<li><b>{H.escape(n)}</b>, {H.escape(t.split(' (')[0])}: {H.escape(em)}</li>")
                body.append("</ul>")
        body.append(f"<p>Everything above is also at {H.escape(cfg.get('room_url', ''))}. Reply here if an item is wrong or done.</p>")
        drafts.append({"owner": owner, "to": route["email"], "email_status": route.get("email_status", ""), "subject": cfg["subject_template"].format(account=", ".join(accts)), "bodyType": "html", "body": "".join(body)})
L += ["## Rundown block (Dallas, carried by gtm-daily-rundown; no separate DM)"]
for acct in cfg["accounts"]: L.append(f"- {status_line(acct)}")
for r in by_owner.get("Dallas Andrews", []): L.append(f"- mine: {r['Task Name']}: {r['Task Description']} (due {r['Task Due Date']})")
un = [o for o in by_owner if cfg["owners"].get(o, {}).get("channel", "unrouted") == "unrouted"]
L += ["", f"## Unrouted owners (receive nothing until added to owner_digest.json): {', '.join(un) or 'none'}", ""]
L += ["## Rollup (" + cfg["rollup"]["to"] + ", " + cfg["rollup"]["channel"] + ")"]
for acct in cfg["accounts"]:
    od = sum(1 for r in items if r["Project Name"] == acct and (d := parse_due(r["Task Due Date"])) and d < today)
    L.append(f"- {status_line(acct)} Overdue items: {od}.")
L += ["", "## DRAFTS (the agent creates each as an Outlook draft; never sends; appends draft id + webLink under each)", "```json", json.dumps(drafts, indent=1), "```", "", "Nobody was messaged by this composer."]
text = "\n".join(L) + "\n"
out = ROOT / "automation/logs" / f"owner-digest-{today}.md"
if a.dry_run: print(text)
else: out.write_text(text); print(f"wrote {out.relative_to(ROOT)}; drafts to create: {len(drafts)}; unrouted: {un}")
