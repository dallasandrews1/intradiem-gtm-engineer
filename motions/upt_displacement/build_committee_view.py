#!/usr/bin/env python3
"""Build UPT_Committee_View_Sep10.html: the buying committee at the ten module-confirmed
accounts, from lists/committee_roster_sep10.csv and lists/sku_signals.json.
Intradiem brand kit (Jul 30 2026). Run from motions/upt_displacement/."""
import csv, json, html, re, datetime, pathlib, shutil

HERE = pathlib.Path(__file__).parent
rows = list(csv.DictReader(open(HERE / "lists/committee_roster_sep10.csv")))
sku = json.load(open(HERE / "lists/sku_signals.json"))
logo = open("/tmp/ilogo.svg").read()

ORDER = ["The Hartford Financial Services Group", "Blue Shield of California (BSCA)", "Verizon",
         "Allstate Corporation", "New York Life Insurance Company", "Maximus", "Teleperformance UK",
         "Gainwell Technologies", "Blue Cross Blue Shield of Louisiana", "TTEC"]
LANES = ["Champion (WFM / real-time)", "Ops owner (contact center)", "Evaluator (performance / op-ex)",
         "Back-office leader", "Technology gatekeeper", "Executive (COO / CAO)"]
DOMAIN = {r["account"]: r["domain"] for r in rows}
VENDOR = {"bcbsla.com": "Verint DPA", "newyorklife.com": "Verint DPA", "blueshieldca.com": "Verint Desktop Analytics",
          "verizon.com": "Verint Desktop Analytics", "thehartford.com": "Verint DPA", "gainwelltechnologies.com": "Verint DPA",
          "maximus.com": "Verint DPA", "ttec.com": "NICE Desktop Analytics", "teleperformance.com": "NICE Desktop Analytics",
          "tp.com": "NICE Desktop Analytics", "allstate.com": "Desktop analytics, vendor not named"}
EVIDENCE = {
    "bcbsla.com": "Vendor case study names the module at the account.",
    "newyorklife.com": "Head of Workforce Management's own profile: expanding Desktop Process Analytics.",
    "blueshieldca.com": "Workforce lead's profile lists Verint Desktop Analytics.",
    "verizon.com": "Profile: Verint support for 60K subscribers including Desktop Analytics. The stack read shows NICE CXone only.",
    "thehartford.com": "Technical lead holds a Verint Desktop Process Analytics certification. The stack read shows NICE only.",
    "gainwelltechnologies.com": "Head of Contact Center Technologies' profile owns Desktop Process Analytics.",
    "maximus.com": "Rep read (Sep 4) plus a matching blinded vendor story. Verint in the back office.",
    "ttec.com": "Vendor case study: Desktop Analytics and Desktop Automation.",
    "teleperformance.com": "Vendor case studies: Desktop Analytics at six UK sites and for back-office agents.",
    "allstate.com": "A Speech and Desktop Analytics consultant on staff. NICE CXone estate, vendor not named on the profile.",
}

def esc(s): return html.escape(s or "")

by_acct = {}
for r in rows:
    by_acct.setdefault(r["account"], []).append(r)

seq = [r for r in rows if r["role"] in ("owner", "deputy")]
n_seq = len(seq)
n_email = sum(1 for r in seq if r["email"])
n_bench = sum(1 for r in rows if r["role"] == "bench")
n_new = sum(1 for r in seq if r["source"].startswith("Sourced"))
n_exec = sum(1 for r in rows if r["lane"].startswith("Executive"))

def lane_block(acct):
    rs = by_acct.get(acct, [])
    out = []
    for lane in LANES:
        lr = [r for r in rs if r["lane"] == lane]
        owner = next((r for r in lr if r["role"] == "owner"), None)
        deputy = next((r for r in lr if r["role"] == "deputy"), None)
        bench = [r for r in lr if r["role"] == "bench"]
        execs = [r for r in lr if r["role"].startswith("covered")]
        if lane.startswith("Executive"):
            if execs:
                names = "; ".join(f"{esc(x['name'])}, {esc(x['title'])}" for x in execs)
                cell = f"<td class='who'>{names}</td><td class='note'>Already in the DWO Executives campaign. Air cover only, no second sequence.</td>"
            else:
                cell = "<td class='who muted'>No COO or CAO in the executive pool</td><td class='note'></td>"
            out.append(f"<tr><th>{esc(lane)}</th>{cell}</tr>")
            continue
        if not owner:
            out.append(f"<tr><th>{esc(lane)}</th><td class='who muted'>Nobody in this role found</td><td class='note'>Lane skipped for this account.</td></tr>")
            continue
        def person(r, tag):
            src = "new" if r["source"].startswith("Sourced") else "sf"
            badge = "<span class='badge new'>sourced Sep 10</span>" if src == "new" else "<span class='badge sf'>in Salesforce</span>"
            mail = "<span class='ok'>email verified</span>" if r["email"] else "<span class='warn'>email pending</span>"
            return f"<div class='p'><span class='tag'>{tag}</span><strong>{esc(r['name'])}</strong><span class='t'>{esc(r['title'])}</span><span class='meta'>{badge} {mail}</span></div>"
        who = person(owner, "Owner") + (person(deputy, "Deputy") if deputy else "")
        note = f"{len(bench)} more on file in this lane" if bench else "No bench beyond the owner"
        out.append(f"<tr><th>{esc(lane)}</th><td class='who'>{who}</td><td class='note'>{note}</td></tr>")
    return "\n".join(out)

sections = []
for acct in ORDER:
    rs = by_acct.get(acct, [])
    dom = DOMAIN.get(acct, "")
    s = [r for r in rs if r["role"] in ("owner", "deputy")]
    with_mail = sum(1 for r in s if r["email"])
    new = sum(1 for r in s if r["source"].startswith("Sourced"))
    lanes_filled = len({r["lane"] for r in s})
    sub = f"{len(s)} to sequence across {lanes_filled} of 5 roles · {with_mail} with a verified email" + (f" · {new} sourced today" if new else "")
    sections.append(f"""
<section class="acct" id="{esc(dom.split('.')[0])}">
  <div class="acct-head">
    <div><div class="eyebrow">{esc(VENDOR.get(dom, ''))}</div><h2>{esc(acct.replace(' (BSCA)', ''))}</h2>
    <p class="sub">{esc(sub)}</p></div>
    <p class="evidence"><span class="mono">Why it's confirmed</span> {esc(EVIDENCE.get(dom, ''))}</p>
  </div>
  <table class="lanes"><thead><tr><th>Role</th><th>Who</th><th>Bench</th></tr></thead><tbody>
  {lane_block(acct)}
  </tbody></table>
</section>""")

today = datetime.date(2026, 9, 10).strftime("%b %-d, %Y")
page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>UPT Displacement Committees</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&family=Roboto+Mono:wght@500;600&display=swap" rel="stylesheet">
<style>
:root{{--forest:#014637;--green:#2DB56E;--green-600:#228752;--green-300:#7BD3A0;--orange:#F58220;--ink:#202020;--sidebar:#F5F4F2;--line:#E0E0E0;--r:8px}}
*{{box-sizing:border-box}} body{{margin:0;font-family:Roboto,system-ui,sans-serif;color:var(--ink);background:#fff;line-height:1.45}}
.mono{{font-family:'Roboto Mono',monospace;font-weight:600;text-transform:uppercase;letter-spacing:.06em;font-size:11px}}
.wrap{{max-width:1100px;margin:0 auto;padding:0 24px}}
header.hero{{background:radial-gradient(900px 420px at 15% 0%,rgba(45,181,110,.35),transparent 60%),var(--forest);color:#fff;padding:48px 0 40px}}
header .logo{{width:150px;height:auto;color:#fff;display:block;margin-bottom:34px}}
.eyebrow{{font-family:'Roboto Mono',monospace;font-weight:600;text-transform:uppercase;letter-spacing:.08em;font-size:12px;color:var(--green-600)}}
header .eyebrow{{color:var(--green-300)}}
h1{{font-weight:900;letter-spacing:-.02em;font-size:40px;line-height:1.08;margin:10px 0 14px;max-width:820px}}
header p.lede{{font-size:18px;max-width:760px;margin:0 0 30px;opacity:.95}}
.statband{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:14px}}
.stat{{border:1px solid rgba(255,255,255,.18);border-radius:var(--r);padding:14px 16px}}
.stat b{{display:block;font-size:34px;font-weight:900;letter-spacing:-.02em;color:var(--green-300);line-height:1}}
.stat span{{display:block;margin-top:6px;font-size:13px;opacity:.9}}
main{{padding:36px 0 60px}}
h2{{font-weight:900;letter-spacing:-.02em;font-size:26px;margin:4px 0 4px}}
.sub{{margin:0;color:#555;font-size:14px}}
.how{{display:grid;grid-template-columns:1.2fr 1fr;gap:24px;margin-bottom:36px}}
.gate{{border-left:4px solid var(--green);background:var(--sidebar);border-radius:var(--r);padding:14px 18px}}
.callout{{border-left:4px solid var(--orange);background:var(--sidebar);border-radius:var(--r);padding:14px 18px}}
.how ul{{margin:8px 0 0;padding-left:18px}} .how li{{margin:4px 0}}
.acct{{border-top:1px solid var(--line);padding:28px 0 8px}}
.acct-head{{display:grid;grid-template-columns:1.1fr 1fr;gap:24px;align-items:end;margin-bottom:14px}}
.evidence{{margin:0;font-size:14px;color:#444;background:var(--sidebar);border-radius:var(--r);padding:12px 14px}}
.evidence .mono{{display:block;color:var(--green-600);margin-bottom:4px}}
table.lanes{{width:100%;border-collapse:collapse;margin-bottom:12px}}
table.lanes thead th{{font-family:'Roboto Mono',monospace;font-weight:600;text-transform:uppercase;letter-spacing:.06em;font-size:11px;text-align:left;color:#666;padding:6px 10px;border-bottom:1px solid var(--line)}}
table.lanes tbody th{{text-align:left;font-weight:700;font-size:14px;padding:12px 10px;vertical-align:top;width:210px;border-bottom:1px solid var(--line)}}
table.lanes td{{padding:12px 10px;vertical-align:top;border-bottom:1px solid var(--line);font-size:14px}}
td.note{{color:#666;width:190px}} .muted{{color:#888}}
.p{{display:grid;grid-template-columns:64px 1fr;gap:2px 10px;margin-bottom:8px}} .p:last-child{{margin-bottom:0}}
.p .tag{{font-family:'Roboto Mono',monospace;font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:.06em;color:var(--green-600);padding-top:3px}}
.p strong{{grid-column:2}} .p .t{{grid-column:2;color:#555}} .p .meta{{grid-column:2;font-size:12px;margin-top:2px}}
.badge{{display:inline-block;border-radius:4px;padding:1px 6px;font-family:'Roboto Mono',monospace;font-size:10px;font-weight:600;text-transform:uppercase;letter-spacing:.05em;margin-right:6px}}
.badge.sf{{background:#E8F5EE;color:var(--green-600)}} .badge.new{{background:#FDEBD9;color:#B85A0D}}
.ok{{color:var(--green-600)}} .warn{{color:#B85A0D}}
.next{{border-top:1px solid var(--line);padding-top:28px;margin-top:20px}}
.next ol{{padding-left:20px}} .next li{{margin:6px 0}}
footer{{color:#777;font-size:12px;padding:20px 0 40px;border-top:1px solid var(--line)}}
@media (max-width:760px){{.how,.acct-head{{grid-template-columns:1fr}} h1{{font-size:30px}} table.lanes tbody th{{width:auto}} td.note{{width:auto}}}}
</style></head>
<body>
<svg width="0" height="0" style="position:absolute">{logo}</svg>
<header class="hero"><div class="wrap">
  <svg class="logo" viewBox="0 0 187 46"><use href="#ilogo"/></svg>
  <div class="eyebrow">UPT displacement · Verint attack, NICE attack · {today}</div>
  <h1>The buying committee at each of the ten confirmed accounts</h1>
  <p class="lede">Ten accounts have the desktop-analytics module in writing. This is who holds each committee role at each one, who is already in Salesforce, who was sourced today, and who has a verified email. Reach-out is sized by committee, not by a seat count.</p>
  <div class="statband">
    <div class="stat"><b>10</b><span>accounts, module confirmed</span></div>
    <div class="stat"><b>{n_seq}</b><span>committee members to sequence</span></div>
    <div class="stat"><b>{n_email}</b><span>with a verified work email</span></div>
    <div class="stat"><b>{n_new}</b><span>sourced today, not in Salesforce</span></div>
    <div class="stat"><b>{n_bench}</b><span>on the bench behind them</span></div>
    <div class="stat"><b>{n_exec}</b><span>executives covered by the exec campaign</span></div>
  </div>
</div></header>
<main><div class="wrap">
  <div class="how">
    <div class="gate"><div class="eyebrow">How a committee is built</div>
      <ul>
        <li><strong>Champion:</strong> Head of Workforce Management or Real-Time. Reads the desktop report, owns the renewal.</li>
        <li><strong>Ops owner:</strong> VP or Director of Contact Center Operations.</li>
        <li><strong>Evaluator:</strong> Director of Operational Excellence, Performance or Quality.</li>
        <li><strong>Back-office leader:</strong> VP or Director of Claims, Shared Services or Payment Operations.</li>
        <li><strong>Technology gatekeeper:</strong> the contact-center platform or telephony lead.</li>
        <li><strong>Executive:</strong> COO or CAO, covered by the DWO Executives campaign, never sequenced twice.</li>
      </ul>
      <p style="margin:10px 0 0;font-size:14px">Whoever holds the role is in. A role nobody holds is skipped. A deputy is added where an account has five or more people in the lane.</p>
    </div>
    <div class="callout"><div class="eyebrow" style="color:#B85A0D">Before anything loads</div>
      <ul>
        <li>Nate or the AE confirms the module per account.</li>
        <li>Everyone sourced today was checked current on Sep 10. Salesforce rows are re-checked at load.</li>
        <li>Verified email is the load gate. Two emails are still pending.</li>
        <li>Phones are sourced on wave-1 seats before the campaign starts.</li>
      </ul>
    </div>
  </div>
  {''.join(sections)}
  <section class="next">
    <div class="eyebrow">What happens next</div>
    <h2>From committee to wave 1</h2>
    <ol>
      <li>Rep confirmation on the ten, then the same committee build on each vendor-confirmed account as it clears.</li>
      <li>Phones on wave-1 seats; the two pending emails re-run.</li>
      <li>Wave 1, Verint accounts, week of Sep 21, from Nate's warm mailbox. Every seat at an account starts the same day.</li>
    </ol>
  </section>
</div></main>
<footer><div class="wrap">Roster: motions/upt_displacement/lists/committee_roster_sep10.csv · counts from Audiences (Salesforce sync) and the Clay free sourcing path, Sep 10 2026 · Intradiem GTM Engineering</div></footer>
</body></html>"""

out = HERE / "UPT_Committee_View_Sep10.html"
out.write_text(page)
desk = pathlib.Path.home() / "Desktop/Intradiem Deliverables/UPT_Committee_View_Sep10.html"
desk.parent.mkdir(parents=True, exist_ok=True)
shutil.copy(out, desk)
print("wrote", out, "and", desk, "| seq", n_seq, "email", n_email, "new", n_new, "bench", n_bench)
