#!/usr/bin/env python3
"""Partner account lookup: every pre-pipeline record, searchable, for the partner team.

Answers the one question the Claude project cannot: has this account already been
registered, by whom, at what stage, and which Intradiem AE owns the record. Registration
is context for coordination, never a stop; current customers are the one case that routes
to the AM instead of a cold sequence.

Run: python3 build_lookup.py   (reads the newest sf_prepipeline run + the customer segment)
"""
import csv, datetime, html as H, json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
TPL = HERE / "frank_selfserve/skills/partner-account-brief/brief_template.html"
INBOX = pathlib.Path.home() / "Claude/Projects/Intradiem GTM Engineer/automation/inbox/partners/sf_prepipeline"
TODAY = datetime.date.today()

run = max(INBOX.glob("run_*"), key=lambda p: p.name)
rows = list(csv.DictReader(open(run / "sf_prepipeline.csv")))
seg = max(HERE.glob("ref/sf_customer_partner_segment_*.csv"), key=lambda p: p.name)
cust = []
for r in csv.DictReader(open(seg)):
    name = (r.get("name") or r.get("company") or r.get("Company") or "").strip()
    typ = " ".join(v for v in r.values() if v and ("ustomer" in v or "artner" in v))
    if name:
        cust.append((name.lower(), "Customer" if "ustomer" in typ else "Partner"))

STAGE_CLS = {"Register Lead": "reg", "CAM to AE Intro": "reg", "Delivered 12 Minute Meeting": "mtg",
             "Customer Meet": "mtg", "Converted to Opportunity": "opp", "Disqualified": "dq"}


def cust_flag(prospect):
    p = prospect.lower().strip()
    for n, t in cust:
        if p and n and (p == n or (len(p) > 5 and p in n) or (len(n) > 5 and n in p)):
            return t
    return ""


cards = []
for r in sorted(rows, key=lambda r: (r["prospect"].lower(), r["created"])):
    age = int(r["age_days"] or 0)
    stale = age > 45 and r["status"] in ("Register Lead", "CAM to AE Intro")
    cf = cust_flag(r["prospect"])
    people = " &middot; ".join(x for x in [
        f'AE {H.escape(r["intradiem_ae"])}' if r["intradiem_ae"] else "AE not parsed",
        f'partner rep {H.escape(r["partner_ae"])}' if r["partner_ae"] else ""] if x)
    note = ""
    if r["status"] == "Converted to Opportunity":
        note = "Opportunity is live. Coordinate with the AE, no cold outreach."
    elif r["status"] == "Disqualified":
        note = "History, not a block. Can be reworked with fresh context."
    elif stale:
        note = f"Registered {age} days ago and still short of a 12 minute meeting. This is what the pilot exists to accelerate."
    else:
        note = "Live registered lead. Loop in the Intradiem AE before outreach."
    if cf == "Customer":
        note = "Current Intradiem customer. Routes to the account manager for expansion, not a cold sequence."
    cards.append({
        "acct": r["prospect"] or r["name"], "partner": r["partner"], "status": r["status"],
        "cls": STAGE_CLS.get(r["status"], ""), "created": r["created"], "age": age,
        "people": people, "cat": r["category"], "pri": r["priority"], "note": note,
        "cust": cf, "stale": stale, "record": r["name"],
    })

body = ['    <section>\n      <p class="label">How to read this</p>\n      <ul>',
        '        <li><strong>Registration is context, not a stop.</strong> Every record here is a lead a partner registered so it would be worked. Finding an account means loop in the Intradiem AE on the record, not stand down.</li>',
        '        <li><strong>The one caution.</strong> Outreach on an account registered by one partner never names a different partner.</li>',
        '        <li><strong>Current customers are the exception.</strong> Those route to the account manager for expansion instead of a cold sequence, and they are flagged in orange below.</li>',
        f'        <li><strong>Snapshot, not a live feed.</strong> {len(rows)} records as exported {run.name.replace("run_","")}. Stages move; re-export from Salesforce when it matters.</li>',
        "      </ul>\n    </section>"]
body.append('    <section>\n      <p class="label">Find an account</p>\n      <input id="q" type="search" placeholder="Type an account name, partner, or AE" autocomplete="off">\n      <div id="count"></div>\n      <div id="list">')
for c in cards:
    tags = f'<span class="pill {c["cls"]}">{H.escape(c["status"])}</span>'
    if c["cust"] == "Customer":
        tags += '<span class="pill cust">Current customer</span>'
    if c["stale"]:
        tags += f'<span class="pill old">{c["age"]} days</span>'
    hay = H.escape(" ".join([c["acct"], c["partner"], c["people"], c["record"]]).lower())
    body.append(f'        <div class="rec" data-h="{hay}">'
                f'<div class="rh"><b>{H.escape(c["acct"])}</b>{tags}</div>'
                f'<div class="rm">{H.escape(c["partner"])} &middot; registered {c["created"]} &middot; {c["people"]}'
                + (f' &middot; {H.escape(c["cat"])}' if c["cat"] else "") + "</div>"
                f'<div class="rn">{H.escape(c["note"])}</div></div>')
body.append("      </div>\n    </section>")

extra = """
  #q{width:100%;padding:12px 14px;font-family:inherit;font-size:15px;border:1px solid var(--rule);border-radius:8px;color:var(--ink);background:#fff}
  #q:focus{outline:2px solid var(--green);outline-offset:1px}
  #count{font-family:'Roboto Mono',monospace;font-size:11px;color:var(--mut);margin:10px 0 4px;letter-spacing:.06em;text-transform:uppercase}
  .rec{padding:12px 0;border-top:1px solid var(--rule)}
  .rh{display:flex;align-items:baseline;gap:8px;flex-wrap:wrap}
  .rh b{color:var(--forest);font-size:15px}
  .rm{font-size:12.5px;color:var(--mut);margin-top:2px}
  .rn{font-size:13.5px;color:var(--ink2);margin-top:4px}
  .pill{font-family:'Roboto Mono',monospace;font-size:9.5px;letter-spacing:.06em;text-transform:uppercase;font-weight:600;padding:2px 8px;border-radius:999px;border:1px solid var(--rule);color:var(--mut)}
  .pill.reg{background:rgba(45,181,110,.12);border-color:transparent;color:var(--deep)}
  .pill.mtg{background:rgba(45,181,110,.22);border-color:transparent;color:var(--forest)}
  .pill.opp{background:var(--forest);border-color:transparent;color:#fff}
  .pill.dq{background:#F0EFED;border-color:transparent}
  .pill.cust{background:rgba(245,130,32,.14);border-color:transparent;color:#B25E12}
  .pill.old{background:rgba(245,130,32,.10);border-color:transparent;color:#B25E12}
"""
script = """
<script>
(function(){
  var q=document.getElementById('q'),recs=[].slice.call(document.querySelectorAll('.rec')),c=document.getElementById('count');
  function run(){var v=q.value.trim().toLowerCase(),n=0;
    recs.forEach(function(r){var hit=!v||r.getAttribute('data-h').indexOf(v)>-1;r.hidden=!hit;if(hit)n++;});
    c.textContent=v?(n+' of '+recs.length+' records'):(recs.length+' records');}
  q.addEventListener('input',run);run();
})();
</script>
"""
page = (TPL.read_text()
        .replace("{{ACCOUNT}}", "Partner account lookup")
        .replace("{{ANGLE}}", "who registered it, what stage, who to loop in")
        .replace("{{SUBHEAD}}", "Every record in the Salesforce partner pre-pipeline, searchable. Use it before working an account so the outreach lands with the partner rep and the Intradiem AE, not around them.")
        .replace("{{DATE}}", TODAY.strftime("%b %-d %Y"))
        .replace("{{BODY}}", "\n".join(body))
        .replace("</style>", extra + "</style>")
        .replace("</body>", script + "</body>")
        .replace("<title>Partner account lookup | Account brief</title>", "<title>Partner account lookup</title>")
        .replace('<p class="eyebrow">Partner channel &middot; Account brief</p>', '<p class="eyebrow">Partner channel &middot; Lookup</p>')
        .replace("<h1>Partner account lookup: who registered it, what stage, who to loop in</h1>",
                 "<h1>Has this account already been registered?</h1>"))
assert "—" not in page and "{{" not in page
out = HERE / "Partner_Account_Lookup.html"
out.write_text(page)
print(f"{out.name}: {len(page):,} bytes, {len(cards)} records, {sum(1 for c in cards if c['cust']=='Customer')} customer-flagged")
