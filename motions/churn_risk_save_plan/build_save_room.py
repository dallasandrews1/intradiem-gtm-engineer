#!/usr/bin/env python3
"""Renders the Cleveland Clinic Save Room from data/save_room_cleveland_clinic.json on the page system."""
import json, pathlib, shutil, html as H, re
HERE = pathlib.Path(__file__).parent; BO = HERE.parent / "back_office_expansion"
d = json.loads((HERE / "data/save_room_cleveland_clinic.json").read_text())
fonts = (BO / "_fonts_embed.css").read_text(); logo = (BO / "_logo_symbol.svg").read_text()
css_src = (HERE / "build_page.py").read_text()
CSS = css_src.split('CSS = """')[1].split('"""')[0]
CSS += """
.pill.g{background:var(--tint);color:var(--green-600)}.pill.y{background:#FDECD9;color:var(--orange-600)}.pill.r{background:#FDE3E3;color:#B42318}
.health{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px;margin-top:18px}
.hc{border:1px solid var(--line);border-radius:var(--r);padding:16px 18px;background:#fff;box-shadow:var(--shadow);border-top:4px solid var(--line)}
.hc.r{border-top-color:#B42318}.hc.y{border-top-color:var(--orange)}.hc.g{border-top-color:var(--green)}
.hc h4{font-size:16px;font-weight:700;display:flex;justify-content:space-between;align-items:center;gap:10px}
.hc ul{list-style:none;margin-top:8px}.hc li{font-size:13.5px;color:var(--ink-2);padding:5px 0;border-top:1px solid var(--line)}
.hc li .src{font-family:var(--ff-mono);font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:var(--green-600);display:block;margin-bottom:2px}
.layers{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:18px}
.layer{background:var(--forest);color:#fff;border-radius:var(--r);padding:18px 20px;position:relative;overflow:hidden}
.layer b{display:block;font-size:34px;font-weight:900;color:var(--green-300);line-height:1}
.layer span{display:block;font-family:var(--ff-mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:#9DBBAE;margin-top:8px}
.layer p{color:#C7DAD1;font-size:13.5px;margin-top:8px;max-width:none}
details{margin-top:14px;border:1px solid var(--line);border-radius:var(--r);background:#fff}
summary{cursor:pointer;padding:12px 18px;font-weight:700;font-size:15px;list-style:none}
summary::-webkit-details-marker{display:none}summary::before{content:"+ ";color:var(--green-600)}details[open] summary::before{content:"\\2013 "}
details .tablewrap{padding:0 18px 14px;margin-top:0}
td.mono{font-family:var(--ff-mono);font-size:12px;color:var(--ink-2)}
.inf{font-family:var(--ff-mono);font-size:11px;color:var(--orange-600)}
@media(max-width:760px){.layers{grid-template-columns:1fr}}
"""
def e(s): return H.escape(str(s or ""))
def pill(st):
    k = {"RED":"r","YELLOW":"y","GREEN":"g"}[st]; return f'<span class="pill {k}">{st.lower()}</span>'
def link(name, url): return f'<a href="{e(url)}" target="_blank" rel="noopener">{e(name)}</a>' if url else e(name)

hl = d["health"]
health_cards = "".join(
  f'<div class="hc {({"RED":"r","YELLOW":"y","GREEN":"g"})[c["status"]]} rv"><h4>{e(c["code"])}{pill(c["status"])}</h4><ul>' +
  "".join(f'<li><span class="src">{e(s)} &middot; {e(dt)}</span>{e(line)}</li>' for s, dt, line in c["evidence"]) + "</ul></div>"
  for c in hl["codes"])

n_new = sum(1 for r in d["inger"] if r["layer"] == "new"); n_found = sum(1 for r in d["inger"] if r["bridge"].startswith("found"))
n_nf = sum(1 for r in d["inger"] if r["bridge"] in ("not found at domain","cannot search"))
def email_cell(r):
    if r.get('email_validated'): return e(r['email_validated']) + ' <span class="pill g">validated</span>'
    if r['email']: return e(r['email'])
    if r['email_inferred']: return '<span class=inf>' + e(r['email_inferred']) + ' inferred</span>'
    return ''
inger_rows = "".join(
  f'<tr class="rv"><td class="who">{link(r["name"], r["linkedin"])}</td><td>{e(r["title_inger"])}</td><td>{e(r["title_live"]) or "<span class=inf>not matched</span>"}</td>'
  f'<td class="st">{e(r["bridge"])}</td><td>{e(r["role"])}</td><td><span class="pill {"go" if r["track"] in ("Stakeholder","Back office") else "now" if "Hold" in r["track"] else "hold"}">{e(r["track"])}</span></td>'
  f'<td class="mono">{email_cell(r)}</td></tr>'
  for r in d["inger"])
bo_rows = "".join(f'<tr class="rv"><td class="mono">{e(r["card"])}</td><td class="who">{link(r["name"], r["linkedin"])}</td><td>{e(r["title"])}</td><td class="st">{e(r["level"])}</td><td>{e(r["function"])}</td><td>{e(r["reports_to"])}</td><td class="inf">{e(r["flag"])}</td></tr>' for r in d["bo_map"])
known_sorted = sorted(d["known"], key=lambda r: (r["title"] == "", r["name"]))
known_rows = "".join(f'<tr><td class="who">{e(r["name"])}</td><td>{e(r["title"])}</td><td class="mono">{e(r["email"])}</td><td class="st">{e(r["lead_status"])}</td></tr>' for r in known_sorted)
plan_rows = "".join(f'<li class="rv"><div class="d">{e(a)}</div><div class="e">{e(b)}</div><div class="r">{e(c)}</div></li>' for a, b, c in d["plan"])
item_rows = "".join(
  f'<tr class="rv"><td class="who">{e(i["Task Name"])}</td><td>{e(i["Task Description"])}</td><td class="st">{e(i["Task Due Date"])}</td><td class="st">{e(i["Task Progress"])}</td><td>{e(i["Assigned To"]).replace(";", ", ")}</td><td>{e(i["Notes"])}</td></tr>'
  for i in d["open_items"])
red = sum(1 for c in hl["codes"] if c["status"] == "RED")

BODY = f"""
<svg width="0" height="0" style="position:absolute" aria-hidden="true">{logo}</svg>
<div class="sheet">
<header class="hero" id="hero"><div class="wrap">
<svg class="logo" data-h="1"><use href="#ilogo"/></svg>
<div class="eyebrow" data-h="1">Save Room &middot; Cleveland Clinic &middot; renewal January 2027</div>
<h1 data-h="2">Cleveland Clinic, <span class="spark">{red} of 7 signals red.</span></h1>
<p class="sub" data-h="3">Every contact we hold, the health read with its evidence, the ninety days to the renewal decision, and the open items in the PMO tracker's own columns.</p>
<div class="hstats" data-h="4">
<div><b data-n="{len(d['known'])}">{len(d['known'])}</b><span>contacts in Salesforce</span></div>
<div><b data-n="16">16</b><span>names from Inger's research</span></div>
<div><b data-n="20">20</b><span>back-office leaders mapped</span></div>
<div><b data-n="{len(d['open_items'])}">{len(d['open_items'])}</b><span>open items, owners proposed</span></div>
</div>
<div class="meta" data-h="4">
<div><span>Account manager</span>{e(d['am'])}</div><div><span>Success manager</span>{e(d['success_manager'])}</div><div><span>Sponsor / customer owner</span>{e(d['sponsor'])} / {e(d['customer_owner'])}</div><div><span>As of</span>Sep 10 2026</div>
</div>
</div></header>

<section><div class="wrap">
<div class="eyebrow">Health</div>
<h2>Seven signals, each with its evidence</h2>
<p>Status is set by the weekly watcher from the Success Plan notes, the monthly adoption deck, Sales Navigator alerts, meeting notes and Salesforce. A change in status always carries the line that caused it.</p>
<div class="health">{health_cards}</div>
<div class="callout rv"><h4>Sequence</h4><p>The savings dispute is the first item because every other move depends on it. Widening to the CFO or COO with a number the customer rejected in November speeds the exit. Settle the number, get the Coach Now supervisors on record, then widen with platform continuity while the RFP runs.</p></div>
</div></section>

<section><div class="wrap">
<div class="eyebrow">Contacts</div>
<h2>Three layers, no overlap</h2>
<div class="layers">
<div class="layer rv"><b>{len(d['known'])}</b><span>in Salesforce</span><p>Pulled from Audiences by the Salesforce account ID at zero credits. Mostly contact center, IT and Success contacts, many with no title. Do not touch without the AM.</p></div>
<div class="layer rv"><b>16</b><span>Inger's research</span><p>2 in Salesforce, 2 on the back-office map, {n_new} new to every list. Free bridge found {n_found} with LinkedIn profiles, {n_nf} did not match at the domain.</p></div>
<div class="layer rv"><b>20</b><span>back-office map</span><p>Operations, finance, revenue cycle, supply chain and HR shared services leaders on a distinct line from the sponsor. Expansion track, kept separate from the save.</p></div>
</div>
<h3>Inger's sixteen, placed</h3>
<div class="tablewrap"><table><thead><tr><th>Name</th><th>Title in research</th><th>Title live (Salesforce or LinkedIn)</th><th>Bridge</th><th>Role in the save</th><th>Track</th><th>Email</th></tr></thead><tbody>{inger_rows}</tbody></table></div>
<div class="gate rv"><h4>Emails</h4><p>Salesforce emails are real. All twelve searchable names from Inger's research were verified Sep 10 and 11 2026 through the Clay Work Email routine: 12 of 12 found for 6.9 credits. Three differ from the name pattern (rganem, scottr, rr), which is why inferred addresses never send. Leslie Chom shows retired on LinkedIn and is off the list; the Florida David has no surname.</p></div>
<details class="rv"><summary>Back-office map, 20 cards</summary><div class="tablewrap"><table><thead><tr><th>#</th><th>Name</th><th>Title</th><th>Level</th><th>Function</th><th>Reports to</th><th>Flag</th></tr></thead><tbody>{bo_rows}</tbody></table></div></details>
<details><summary>Salesforce-known contacts, {len(d['known'])}</summary><div class="tablewrap"><table><thead><tr><th>Name</th><th>Title</th><th>Email</th><th>Lead status</th></tr></thead><tbody>{known_rows}</tbody></table></div></details>
</div></section>

<section><div class="wrap">
<div class="eyebrow">Plan</div>
<h2>Ninety days to the renewal decision</h2>
<ul class="cal">{plan_rows}</ul>
</div></section>

<section><div class="wrap">
<div class="eyebrow">Open items</div>
<h2>Twelve rows in the PMO tracker's columns</h2>
<p>Same columns as the Project Task Tracker export (Project Name, Task Name, Task Description, Task Due Date, Task Progress, Assigned To, Notes). Owners are proposed and get confirmed in Inger's brainstorm. The import file is beside this page.</p>
<div class="tablewrap"><table><thead><tr><th>Task</th><th>Description</th><th>Due</th><th>Progress</th><th>Assigned to (proposed)</th><th>Notes</th></tr></thead><tbody>{item_rows}</tbody></table></div>
</div></section>

<footer class="foot"><svg class="logo"><use href="#ilogo"/></svg><span>GTM Engineering &middot; Cleveland Clinic Save Room &middot; Sep 10 2026</span><span>Internal. Sources: Salesforce via Audiences, Cleveland Clinic Success Plan 2026, September 2026 adoption review, Inger's research, Sep 10 call.</span></footer>
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
out = HERE / "Cleveland_Clinic_Save_Room_Sep10.html"; out.write_text(html)
dest = pathlib.Path.home() / "Desktop/Intradiem Deliverables/Cleveland Clinic Save Room - Sep 10.html"; shutil.copy(out, dest)
shutil.copy(HERE / "data/Cleveland_Clinic_PMO_Tracker_Import.csv", pathlib.Path.home() / "Desktop/Intradiem Deliverables/Cleveland Clinic - PMO Tracker Import - Sep 10.csv")
print(out, len(html)); print(dest)
