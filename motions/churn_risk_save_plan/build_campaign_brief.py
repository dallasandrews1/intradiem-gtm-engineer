#!/usr/bin/env python3
"""Nicole's campaign brief for the Cleveland Clinic high-and-wide lane, plus the verified list as CSV."""
import json, pathlib, shutil, csv, html as H
HERE = pathlib.Path(__file__).parent; BO = HERE.parent / "back_office_expansion"
d = json.loads((HERE / "data/save_room_cleveland_clinic.json").read_text()); plan = json.loads((HERE / "data/comms_plan_cleveland_clinic.json").read_text())
fonts = (BO / "_fonts_embed.css").read_text(); logo = (BO / "_logo_symbol.svg").read_text()
CSS = (HERE / "build_page.py").read_text().split('CSS = """')[1].split('"""')[0]
def e(s): return H.escape(str(s or ""))
INCLUDE_TRACKS = {"Stakeholder"}  # IT and RFP names only; sponsor line, executives, back-office and clinical names are out of the one-pager
EXCLUDE_WHY = {"Inger": "sponsor line, Inger only", "Hold, then exec": "executive note held; no marketing touch until it is sent", "Back office": "expansion track, separate sequence", "Nurture": "clinical or HR, no reason to receive a contact-center one-pager", "Bench": "clinical, out"}
# Verified list: Inger's names with verified or Salesforce email (excluding the sponsor line, which marketing never touches)
rows = []; excluded = []
for r in d["inger"]:
    em = r.get("email_validated") or r["email"]
    if not em or r["bridge"] == "departed": continue
    if r["track"] in INCLUDE_TRACKS:
        rows.append({"full_name": r["name"], "title": (r["title_live"] or r["title_inger"]).split(" (")[0], "email": em,
                     "email_source": "checked Sep 2026 (work-email verification)" if r.get("email_validated") else "Salesforce, checked Sep 2026",
                     "linkedin": r["linkedin"], "company": "Cleveland Clinic", "group": "IT and RFP", "send_as": "Amy Johnson alias", "notes": ""})
    else: excluded.append((r["name"], EXCLUDE_WHY.get(r["track"], r["track"])))
SPONSOR_LINE = {"rena thompson", "shantel adams", "linda reid", "mary kay pienta", "adam gilbert", "eric kokochak", "lisa yerian"}
known_marketable = [k for k in d["known"] if k["email"] and k["title"] and k["name"].lower() not in SPONSOR_LINE and "@" in k["email"]]
for k in known_marketable:
    rows.append({"full_name": k["name"], "title": k["title"], "email": k["email"], "email_source": "Salesforce (marketing's own records, not re-verified)", "linkedin": k["linkedin"],
                 "company": "Cleveland Clinic", "group": "Salesforce-known contact center and IT", "send_as": "Amy Johnson alias", "notes": "Pardot bounce handling applies"})
out_csv = HERE / "data/Cleveland_Clinic_Verified_List_Nicole_Sep11.csv"
with open(out_csv, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
shutil.copy(out_csv, pathlib.Path.home() / "Desktop/Intradiem Deliverables/Cleveland Clinic - Verified List for Nicole - Sep 11.csv")
n_send = sum(1 for r in rows if r["group"] == "IT and RFP")
list_rows = "".join(f'<tr class="rv"><td class="who">{e(r["full_name"])}</td><td>{e(r["title"])}</td><td class="st">{e(r["email"])}</td><td>{e(r["group"])}</td><td>{e(r["email_source"])}</td></tr>' for r in rows if r["group"] == "IT and RFP")
excl_rows = "".join(f'<li class="rv"><b>{e(n)}</b>: {e(w)}</li>' for n, w in excluded)
mk = [m for m in plan["moves"] if m["lane"] == "Nicole and marketing"]
cal = "".join(f'<li class="rv"><div class="d">{e(m["due"])}</div><div class="e">{e(m["move"])}</div><div class="r"></div></li>' for m in mk)
BODY = f"""
<svg width="0" height="0" style="position:absolute" aria-hidden="true">{logo}</svg>
<div class="sheet">
<header class="hero" id="hero"><div class="wrap">
<svg class="logo" data-h="1"><use href="#ilogo"/></svg>
<div class="eyebrow" data-h="1">Campaign brief &middot; Cleveland Clinic &middot; high and wide</div>
<h1 data-h="2">Cleveland Clinic, <span class="spark">the high-and-wide lane.</span></h1>
<p class="sub" data-h="3">Monthly one-pager to the people who are not in the room while the save runs. Nothing account-specific, nothing to reply to, sent as Amy's alias. The same shape as the ADT campaign.</p>
<div class="hstats" data-h="4">
<div><b data-n="{n_send}">{n_send}</b><span>IT and RFP names, emails checked</span></div>
<div><b data-n="{len(known_marketable)}">{len(known_marketable)}</b><span>Salesforce contact-center and IT records</span></div>
<div><b data-n="3">3</b><span>sends: Oct 6, Nov 3, Dec 1</span></div>
</div>
<div class="meta" data-h="4"><div><span>For</span>Nicole Garcia</div><div><span>From</span>Dallas Andrews</div><div><span>Account manager</span>Inger Escamilla</div><div><span>Date</span>Sep 11 2026</div></div>
</div></header>

<section><div class="wrap">
<div class="tldr rv"><div class="k">The brief</div><ul>
<li><b>Job:</b> keep Intradiem in front of every Cleveland Clinic leader outside the sponsor line through the January renewal, without adding to Inger's or Amy's threads.</li>
<li><b>Audience:</b> the {n_send} IT and RFP names below, emails checked this month, plus the {len(known_marketable)} Salesforce contact-center and IT records, which are marketing's own data and have not been re-verified; Pardot's bounce handling covers them. The sponsor line, the executives, the back-office leaders and the clinical names are out, each for a reason listed below.</li>
<li><b>Shape:</b> one one-pager a month, three sends from Pardot as Amy Johnson's alias. No account-specific copy from marketing; the account messages are Inger's and Amy's.</li>
<li><b>Timing:</b> this brief and the list come to you after Inger's brainstorm confirms the lanes, week of Sep 29. First send Oct 6.</li>
<li><b>Content:</b> what the hubs run and what it returns, in the customer's own adoption numbers, and the platform line for the RFP season: Intradiem runs on top of the WFM and integrates with Genesys Cloud, NICE and the other platforms.</li>
<li><b>Gate:</b> every claim traces to the Value Repository or the customer's own adoption review. The disputed savings figures do not appear.</li>
</ul></div>
</div></section>

<section><div class="wrap">
<div class="eyebrow">Sends</div>
<h2>Dates</h2>
<ul class="cal">{cal}</ul>
<div class="gate rv"><h4>Claims that can go in</h4><p>Humana by name: partnership since 2020, 7X ROI five years in, about 2 hours of capacity per agent per month in 2025, AHT down 45 seconds (Value Repository, VERIFIED). Cleveland Clinic's own August adoption numbers when addressed to Cleveland Clinic: 79.6% coaching acceptance, 93.8% AUX self-cure, 4,461 leave-early offers accepted. Platform line: runs on top of the existing WFM, integrates with Genesys Cloud, NICE and others, nothing replaced. A 2022 Forrester study: 342 percent ROI.</p></div>
<div class="callout rv"><h4>Claims that stay out</h4><p>The $719K YTD savings and 1.9x figures until the method is agreed with the customer. Any customer name other than Humana, Virgin Media or Optum. Any idle-time percentage. Any implementation timeline.</p></div>
</div></section>

<section><div class="wrap">
<div class="eyebrow">List</div>
<h2>The list</h2>
<p>The IT and RFP names, each with a checked work email. The CSV beside this page carries these rows plus the {len(known_marketable)} Salesforce records, with a source column on every row.</p>
<div class="tablewrap"><table><thead><tr><th>Name</th><th>Title</th><th>Email</th><th>Group</th><th>Email source</th></tr></thead><tbody>{list_rows}</tbody></table></div>
<h3>Left out on purpose</h3>
<ul class="threads">{excl_rows}</ul>
</div></section>

<footer class="foot"><svg class="logo"><use href="#ilogo"/></svg><span>GTM Engineering &middot; Cleveland Clinic campaign brief &middot; Sep 11 2026</span><span>Internal to Intradiem.</span></footer>
</div>
<script>(function(){{var h=document.getElementById('hero');setTimeout(function(){{h.classList.add('on')}},60);setTimeout(function(){{document.querySelectorAll('.rv').forEach(function(el){{el.classList.add('on')}})}},300);}})();</script>
"""
html = '<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>Cleveland Clinic Campaign Brief</title><style>' + fonts + CSS + '.rv.on{opacity:1;transform:none}</style></head><body>' + BODY + '</body></html>'
out = HERE / "Cleveland_Clinic_Campaign_Brief_Nicole_Sep11.html"; out.write_text(html)
shutil.copy(out, pathlib.Path.home() / "Desktop/Intradiem Deliverables/Cleveland Clinic Campaign Brief (Nicole) - Sep 11.html")
dep = pathlib.Path.home() / "Desktop/Intradiem Deliverables/deploy-save-rooms/cleveland-clinic/campaign-brief"; dep.mkdir(parents=True, exist_ok=True); shutil.copy(out, dep / "index.html")
print(out, "list rows", len(rows), "one-pager", n_send, "known marketable", len(known_marketable))
