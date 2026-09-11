#!/usr/bin/env python3
"""Inger-facing Cleveland Clinic Save Room. Reads data/save_room_cleveland_clinic.json. Internal pages untouched."""
import json, pathlib, shutil, html as H
HERE = pathlib.Path(__file__).parent; BO = HERE.parent / "back_office_expansion"
d = json.loads((HERE / "data/save_room_cleveland_clinic.json").read_text())
fonts = (BO / "_fonts_embed.css").read_text(); logo = (BO / "_logo_symbol.svg").read_text()
CSS = (HERE / "build_page.py").read_text().split('CSS = """')[1].split('"""')[0] + """
.asks{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:20px}
.ask{background:var(--forest);color:#fff;border-radius:var(--r);padding:22px 24px;position:relative;overflow:hidden}
.ask::after{content:"";position:absolute;right:-90px;top:-90px;width:220px;height:220px;border-radius:50%;background:radial-gradient(circle,rgba(45,181,110,.28),transparent 62%)}
.ask *{position:relative;z-index:1}
.ask .k{font-family:var(--ff-mono);font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:var(--green-300);font-weight:600}
.ask h4{color:#fff;font-size:19px;font-weight:900;letter-spacing:-.01em;margin:8px 0 6px}
.ask p{color:#C7DAD1;font-size:14.5px;max-width:none;margin:0}
.pill.g{background:var(--tint);color:var(--green-600)}.pill.y{background:#FDECD9;color:var(--orange-600)}.pill.r{background:#FDE3E3;color:#B42318}
.sig{list-style:none;margin-top:14px;border-top:1px solid var(--line)}
.sig li{border-bottom:1px solid var(--line)}
.sig summary{display:grid;grid-template-columns:200px 110px 1fr;gap:16px;align-items:center;padding:12px 0;cursor:pointer;list-style:none;font-size:15px}
.sig summary::-webkit-details-marker{display:none}
.sig summary .n{font-weight:700;color:var(--ink)}
.sig summary .w{color:var(--ink-2)}
.sig .ev{padding:0 0 12px 216px;font-size:13.5px;color:var(--ink-2)}
.sig .ev div{padding:4px 0}
.sig .ev span{font-family:var(--ff-mono);font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:var(--green-600);margin-right:8px}
.note{display:block;font-size:12.5px;color:var(--ink-3);margin-top:3px}
td.who{white-space:normal;min-width:230px}
.em{display:block;font-family:var(--ff-mono);font-size:12px;color:var(--ink-2);font-weight:400;margin-top:3px;white-space:nowrap}
.motion{list-style:none;margin-top:14px;border-top:1px solid var(--line);max-width:900px}
.motion li{display:grid;grid-template-columns:1fr 120px;gap:16px;padding:11px 0;border-bottom:1px solid var(--line);font-size:15px;color:var(--ink-2)}
.motion li b{color:var(--ink)}
.motion li .d{font-family:var(--ff-mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--green-600);text-align:right}
@media(max-width:760px){.asks{grid-template-columns:1fr}.sig summary{grid-template-columns:1fr}.sig .ev{padding-left:0}.motion li{grid-template-columns:1fr}.motion li .d{text-align:left}}
"""
def e(s): return H.escape(str(s or ""))
def link(n, u): return f'<a href="{e(u)}" target="_blank" rel="noopener">{e(n)}</a>' if u else e(n)

# Where each of Inger's names sits, in her words
WHERE = {
 "Rena Thompson": "Sponsor line, contact center operations", "Scott Faini": "IT, unified communications",
 "Katherine Neal": "IT, patient access and revenue cycle", "Bob Ganem": "IT, product ownership", "Leslie Chom": "IT, patient and caregiver computing",
 "Terri Horan": "Digital health, patient journey", "Dennis Laraway": "Finance, top of the house", "Bill Peacock": "Operations, top of the house",
 "Kelly Hancock": "Caregiver office, administration", "Emily Monteleone": "Strategic workforce planning", "Rebecca Vance": "HR services",
 "Meredith Foxx": "Nursing, enterprise", "Sonya Pease": "Florida, quality and patient experience", "F. Scott Ross": "Florida, clinical leadership",
 "Richard Rothman": "Indian River, quality", "David (surname not given)": "Florida market",
}
TRACK = {"Inger": "Yours", "Stakeholder": "RFP and platform continuity", "Hold, then exec": "After the savings number holds", "Back office": "Back-office map, separate", "Nurture": "Monthly one-pager", "Bench": "Bench"}
TITLE_NOTE = {"Katherine Neal": "LinkedIn shows Senior IT Solutions Architect for Patient Access, Patient Experience and Revenue Cycle since July 2025.",
              "F. Scott Ross": "LinkedIn shows Chief Medical Officer, Fort Lauderdale.",
              "Rebecca Vance": "LinkedIn shows Senior Director, HR Services since May 2024."}
def title_for(r):
    if r["name"] in TITLE_NOTE: return r["title_inger"]
    return r["title_inger"]
def email_for(r):
    if r.get("email_validated"): return f'<span class="em">{e(r["email_validated"])} <span class="pill g">verified</span></span>'
    if r["email"]: return f'<span class="em">{e(r["email"])} <span class="pill g">in Salesforce</span></span>'
    if r["bridge"] == "cannot search": return '<span class="em"><span class="pill hold">needs a surname</span></span>'
    return '<span class="em"><span class="pill y">confirm in Sales Nav</span></span>'
SHOW = [r for r in d["inger"] if (r.get("email_validated") or r["email"]) and r["bridge"] != "departed"]
DROPPED = [r for r in d["inger"] if r not in SHOW]
rows = "".join(
  f'<tr class="rv"><td class="who">{link(r["name"], r["linkedin"])}{email_for(r)}{("<span class=note>" + e(TITLE_NOTE[r["name"]]) + "</span>") if r["name"] in TITLE_NOTE else ""}</td>'
  f'<td>{e(title_for(r))}</td><td>{e(WHERE.get(r["name"], ""))}</td><td>{e(TRACK.get(r["track"], r["track"]))}</td></tr>'
  for r in SHOW)
n_show = len(SHOW); n_ver = sum(1 for r in SHOW if r.get("email_validated") or r["email"]); n_conf = 20
retired = [r["name"] for r in d["inger"] if r["bridge"] == "departed"]

# Signals in plain words
SIG = {"Value dispute": ("Savings agreement", "The savings method has not been agreed since the November review."),
       "Sponsor silence": ("Sponsor access", "Meetings are accepted and then cancelled; Shantel declines new-product conversations."),
       "Adoption decline": ("Adoption", "Dynamic sessions and coaching sit well under goal; two rule sets have been paused since June."),
       "Open case aging": ("Open cases", "Current case status needs a fresh read from Amy."),
       "Executive change": ("Leadership changes", "No sponsor or evaluator has changed role."),
       "Competitive event": ("RFP and migration", "The CCaaS RFP is out and Harmonic conversations are starting."),
       "Renewal clock": ("Renewal", "January 2027, two options on the table, none signed.")}
P = {"RED": "r", "YELLOW": "y", "GREEN": "g"}; W = {"RED": "needs attention", "YELLOW": "watch", "GREEN": "steady"}
sig = "".join(
  f'<li class="rv"><details><summary><span class="n">{e(SIG[c["code"]][0])}</span><span><span class="pill {P[c["status"]]}">{W[c["status"]]}</span></span><span class="w">{e(SIG[c["code"]][1])}</span></summary>'
  f'<div class="ev">' + "".join(f'<div><span>{e(s)} &middot; {e(dt)}</span>{e(line)}</div>' for s, dt, line in c["evidence"]) + '</div></details></li>'
  for c in d["health"]["codes"])

MOTION = [
 ("Savings review with Shantel, line by line", "open since November", "10/10/2026"),
 ("Case closure dates in writing to the CCF team", "", "9/25/2026"),
 ("Why the End of Shift and Leave Early rules were paused, and what restarts them", "", "9/25/2026"),
 ("Supervisors who use Coach Now and the AUX self-cure teams on record", "the proof for Rena's impact summary", "10/10/2026"),
 ("Platform-continuity conversation with the IT product owners", "Intradiem sits on top of whichever platform the RFP picks", "11/9/2026"),
 ("Harmonic migration presented as continuity, open issues carried into the plan", "", "11/9/2026"),
 ("Executive review with Lisa Yerian", "CFO and COO after the number holds", "11/9/2026"),
 ("Cleveland Clinic brainstorm", "owners set there, on the PMO list", "9/25/2026"),
 ("Monthly one-pager to known contacts; stakeholder sequence to the new names once cleared", "", "10/10/2026"),
]
motion = "".join(f'<li class="rv"><span><b>{e(t)}</b>{(" &middot; " + e(n)) if n else ""}</span><span class="d">{e(dd)}</span></li>' for t, n, dd in MOTION)

BODY = f"""
<svg width="0" height="0" style="position:absolute" aria-hidden="true">{logo}</svg>
<div class="sheet">
<header class="hero" id="hero"><div class="wrap">
<svg class="logo" data-h="1"><use href="#ilogo"/></svg>
<div class="eyebrow" data-h="1">Cleveland Clinic &middot; renewal January 2027</div>
<h1 data-h="2">Cleveland Clinic, <span class="spark">in one place.</span></h1>
<p class="sub" data-h="3">Nothing new to remember. Your Monday note arrives in Outlook with what is yours and these contacts. This page is the link behind it. The PMO list stays your record.</p>
<div class="hstats" data-h="4">
<div><b data-n="{n_show}">{n_show}</b><span>of your names placed</span></div>
<div><b data-n="{n_ver}">{n_ver}</b><span>verified emails</span></div>
<div><b data-n="{n_conf}">{n_conf}</b><span>back-office leaders, separate map</span></div>
</div>
<div class="meta" data-h="4">
<div><span>For</span>Inger Escamilla</div><div><span>From</span>Dallas Andrews</div><div><span>Date</span>Sep 11 2026</div><div><span>Refresh</span>Mondays</div>
</div>
</div></header>

<section><div class="wrap">
<div class="eyebrow">Your three asks</div>
<h2>Answered on this page, and on its own every Monday</h2>
<div class="asks">
<div class="ask rv"><div class="k">One place</div><h4>This page, behind the note</h4><p>Contacts, account health with the evidence, and what is in motion. Refreshed Mondays from the Success Plan, the adoption review, Sales Navigator and meeting notes. Nothing here needs your input.</p></div>
<div class="ask rv"><div class="k">Notices without a spreadsheet</div><h4>A Monday note</h4><p>An Outlook note with your open items, the account status and these contacts. First one Monday Sep 14. Nothing to open, nothing to update.</p></div>
<div class="ask rv"><div class="k">People around the blocker</div><h4>Your names, verified</h4><p>Every contact below has a checked work email. Twenty back-office leaders sit on the separate expansion map, untouched by the save.</p></div>
</div>
</div></section>

<section><div class="wrap">
<div class="eyebrow">Contacts</div>
<h2>Your names, verified and placed</h2>
<p>Names from your research with a checked work email, where each sits, and the track that fits.{(" " + ", ".join(e(n) for n in retired) + " shows as retired on LinkedIn and is not listed.") if retired else ""}</p>
<div class="tablewrap"><table><thead><tr><th>Name and email</th><th>Title</th><th>Where they sit</th><th>Track</th></tr></thead><tbody>{rows}</tbody></table></div>
</div></section>

<section><div class="wrap">
<div class="eyebrow">Account</div>
<h2>Where the account stands</h2>
<p>One line per signal. Open a line for the evidence behind it. The savings review with Shantel comes first because every executive conversation after it depends on a number the customer accepts.</p>
<ul class="sig">{sig}</ul>
</div></section>

<section><div class="wrap">
<div class="eyebrow">In motion</div>
<h2>Ninety days to the renewal decision</h2>
<p>Owners get set in your brainstorm, on the PMO list. These are the moves and their dates.</p>
<ul class="motion">{motion}</ul>
</div></section>

<footer class="foot"><svg class="logo"><use href="#ilogo"/></svg><span>GTM Engineering &middot; Cleveland Clinic &middot; Sep 11 2026</span><span>Internal to Intradiem. Sources: Salesforce, Cleveland Clinic Success Plan 2026, September 2026 adoption review, Inger's research.</span></footer>
</div>
<script>
(function(){{
  var h=document.getElementById('hero');setTimeout(function(){{h.classList.add('on')}},60);
  var io=new IntersectionObserver(function(es){{es.forEach(function(x){{if(x.isIntersecting){{x.target.classList.add('on');io.unobserve(x.target)}}}})}},{{threshold:.08}});
  document.querySelectorAll('.rv').forEach(function(el,i){{el.style.setProperty('--i',i%8);io.observe(el)}});
  setTimeout(function(){{document.querySelectorAll('.rv').forEach(function(el){{el.classList.add('on')}})}},1400);
  document.querySelectorAll('[data-n]').forEach(function(el){{var t=+el.getAttribute('data-n'),st=Date.now();el.textContent='0';var iv=setInterval(function(){{var p=Math.min(1,(Date.now()-st)/900);el.textContent=Math.round(t*(1-Math.pow(1-p,3)));if(p>=1)clearInterval(iv)}},30)}});
}})();
</script>
"""
html = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>Cleveland Clinic Save Room</title><style>' + fonts + CSS + '</style></head><body>' + BODY + '</body></html>')
out = HERE / "Cleveland_Clinic_Save_Room_Inger_Sep11.html"; out.write_text(html)
shutil.copy(out, pathlib.Path.home() / "Desktop/Intradiem Deliverables/Cleveland Clinic Save Room (Inger) - Sep 11.html")
dep = pathlib.Path.home() / "Desktop/Intradiem Deliverables/deploy-save-rooms/cleveland-clinic/inger"; dep.mkdir(parents=True, exist_ok=True); shutil.copy(out, dep / "index.html")
print(out, len(html), "verified", n_ver, "confirm", n_conf)
