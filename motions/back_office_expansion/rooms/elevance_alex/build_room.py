#!/usr/bin/env python3
"""Alex Bauer's Elevance Health expansion room, in the Cleveland Clinic save-room shape: the plan first (routes, lanes, moves,
messages), then the account facts, then the appendix (the two back-office maps, Alex's relationship map, the Salesforce-known layer).
Reads data/comms_plan_elevance.json and data/expansion_room_elevance.json. Stages to deploy-save-rooms/elevance/alex/. Never deploys."""
import json, pathlib, shutil, html as H, datetime as dt, collections
HERE = pathlib.Path(__file__).parent; BO = HERE.parent.parent; CC = HERE.parent.parent.parent / "churn_risk_save_plan"
d = json.loads((HERE / "data/expansion_room_elevance.json").read_text()); plan = json.loads((HERE / "data/comms_plan_elevance.json").read_text())
fonts = (BO / "_fonts_embed.css").read_text(); logo = (BO / "_logo_symbol.svg").read_text()
base_css = (CC / "build_page.py").read_text().split('CSS = """')[1].split('"""')[0]
inger_css = (CC / "build_save_room_inger.py").read_text().split('CSS = (HERE / "build_page.py").read_text().split(\'CSS = """\')[1].split(\'"""\')[0] + """')[1].split('"""')[0]
CSS = base_css + inger_css + """
.facts{list-style:none;margin-top:14px;border-top:1px solid var(--line);max-width:980px}
.facts li{display:grid;grid-template-columns:170px 1fr;gap:18px;padding:12px 0;border-bottom:1px solid var(--line);font-size:14.5px;color:var(--ink-2)}
.facts li b{color:var(--ink);font-weight:700}
.facts li .src{display:block;font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--green-600);margin-top:4px}
.org{margin-top:10px}
.org .row{display:grid;grid-template-columns:34px 1fr 90px;gap:12px;padding:7px 0;border-bottom:1px solid var(--line);font-size:14px;align-items:baseline}
.org .row .n{font-weight:700;color:var(--ink)}
.org .row .t{display:block;color:var(--ink-2);font-size:13px}
.org .row .up{display:block;font-size:12px;color:var(--ink-3)}
.org .row .lv{font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--green-600);text-align:right}
.pill.hold{background:#FDECD9;color:var(--orange-600)}
.mapbox{border:1px solid var(--line);border-radius:var(--r);padding:18px 22px;background:#fff;box-shadow:var(--shadow);margin-top:16px}
.mapbox h3{margin:0 0 4px}
.mapbox .k{font-family:var(--ff-mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--green-600);font-weight:600}
details.more summary{cursor:pointer;font-weight:700;color:var(--green-600);margin-top:10px;list-style:none}
details.more summary::-webkit-details-marker{display:none}
.known .grp{margin-top:14px}
.known .grp h4{font-size:15px;margin:0 0 2px}
.known .grp .meta2{font-size:12.5px;color:var(--ink-3);font-family:var(--ff-mono);letter-spacing:.04em}
.known table td{font-size:13px}
@media(max-width:760px){.facts li{grid-template-columns:1fr}.org .row{grid-template-columns:1fr}.org .row .lv{text-align:left}}
"""
def e(s): return H.escape(str(s or ""))
def link(n, u): return f'<a href="{e(u)}" target="_blank" rel="noopener">{e(n)}</a>' if u else e(n)
def wk(s_): return dt.date.fromisoformat(s_).strftime("%b %d")

held_routes = {"carelon-door"}
routes = "".join(f'<div class="route rv{" held" if r["id"] in held_routes else ""}"><div class="k">{e(r["lane"])}{" &middot; held" if r["id"] in held_routes else ""}</div><h4>{e(r["name"])}</h4><p class="via">{e(r["via"])}</p><p>{e(r["why"])}</p></div>' for r in plan["routes"])
lanes = ""
for L in plan["lanes"]:
    mv = [m for m in plan["moves"] if m["lane"] == L["lane"]]
    items = "".join(f'<li class="{m["status"]}"><span class="d">{wk(m["week"])}{" &middot; held" if m["status"]=="held" else ""}</span>{e(m["move"])}</li>' for m in mv)
    lanes += f'<div class="lanecol rv"><div class="head"><span>{e(L["role"])}</span><b>{e(L["lane"])}</b><p>{e(L["owns"])}</p></div><ul>{items}</ul></div>'
EM = d["emails"]
def email_line(name):
    v = EM.get(name)
    if not v: return ""
    if v["status"] == "validated": return f' <span class="em">{e(v["email"])} <span class="pill g">verified</span></span>'
    if v["status"].startswith("validated"): return f' <span class="em">{e(v["email"])} <span class="pill y">surname differs, confirm</span></span>'
    return ' <span class="em"><span class="pill y">email not found; confirm in Sales Nav</span></span>'
msgs = ""
for m in plan["messages"]:
    claims = "".join(f'<div>{e(c)}<br><span style="color:var(--ink-3)">{e(src)}</span></div>' for c, src in m["claims"])
    body_html = "".join(f'<pre>to: {e(r["to_first"])}\nsubject: {e(m["subject"])}\n\n{e(r["body"])}</pre>' for r in m["renders"]) if m.get("renders") else f'<pre>subject: {e(m["subject"])}\n\n{e(m["body"])}</pre>'
    flag = f'<span class="pill y">waits for {e(m["waits_for"])}</span>' if m.get("waits_for") else ('<span class="pill y">held</span>' if m["id"] == "m4" else "")
    msgs += (f'<details class="msg rv"><summary><b>{e(m["name"])} {flag}</b><span>{e(m["from"])} &middot; {e(m["when"])}</span></summary><div class="in">'
             f'<div>{body_html}</div><div class="side"><b>To</b>{e(m["to"])}<b>The one idea</b>{e(m["one_idea"])}<b>Claims and where they come from</b>{claims}<b>Check</b>{e(m["qc"])}</div></div></details>')
rules = "".join(f'<li class="rv">{e(r)}</li>' for r in plan["rules"])
ml = plan["marketing_lane"]
mkt = (f'<h3>The marketing lane</h3><p>The list for marketing is beside this page: {e(d["marketing_csv"]["included"])} of the {e(d["known_total"])} Salesforce-known people, the sponsor line and contact-center titles left out with the reason on each row. '
       f'{e(ml["tool"])}. Sends {e(", ".join(s_.split(":")[0] for s_ in ml["sends"]))}.</p>'
       f'<div class="tablewrap"><table><thead><tr><th>In the one-pager</th><th>Never</th></tr></thead><tbody><tr><td>' + "".join(f'<div>{e(c)}</div>' for c in ml["claims_in"]) + '</td><td>' + "".join(f'<div>{e(c)}</div>' for c in ml["claims_out"]) + '</td></tr></tbody></table></div>')
facts = "".join(f'<li class="rv"><b>{e(f["k"])}</b><span>{e(f["line"])}<span class="src">{e(f["source"])}</span></span></li>' for f in d["facts"])

# Appendix: the two back-office maps as indented org rows
def org_rows(rows):
    out = ""
    for r in rows:
        flag = ""
        if r["flag"].startswith("VERIFY:"): flag = f' <span class="pill y">confirm</span>'
        elif r["flag"].startswith("IN_SF:"): flag = ' <span class="pill g">in Salesforce</span>'
        elif r["flag"]: flag = ' <span class="pill y">same name in Salesforce</span>'
        pad = 18 * r["depth"]
        out += (f'<div class="row"><span style="color:var(--ink-3);font-family:var(--ff-mono);font-size:11px">{r["card"]}</span>'
                f'<span style="padding-left:{pad}px"><span class="n">{link(r["name"], r["linkedin"])}</span>{flag}{email_line(r["name"])}<span class="t">{e(r["title"])}</span>'
                f'<span class="up">{"reports up to " + e(r["reports_to"]) if r["reports_to"] and r["reports_to"] != "Top of the map" else "top of the map"}{(" &middot; " + e(r["note"])) if r["note"] else ""}</span></span>'
                f'<span class="lv">{e(r["level"])}</span></div>')
    return out
maps_html = ""
for acct in ("Elevance Health", "Carelon"):
    rows = [r for r in d["bo_maps"] if r["account"] == acct]
    tops = [r for r in rows if r["depth"] == 0]
    lanes_ct = collections.Counter(r["lane"] for r in rows)
    maps_html += (f'<div class="mapbox rv"><div class="k">In Sales Navigator: {e(rows[0]["map"])}</div><h3>{e(acct)}: {len(rows)} people</h3>'
                  f'<p style="margin:0 0 6px">{e(", ".join(t["name"] for t in tops))} at the top. {e(lanes_ct.get("Operations leaders", 0))} operations leaders, {e(lanes_ct.get("Workforce planning & product owners", 0))} workforce planning, {e(lanes_ct.get("Operations technology", 0))} operations technology. Every card live-checked Sep 11 2026.</p>'
                  f'<details class="more"><summary>Show the map</summary><div class="org">{org_rows(rows)}</div></details></div>')
removed_map = [r for r in d["removed"] if r["why"].startswith(("no longer", "live title"))]
removed_html = "".join(f'<tr><td>{e(r["account"])}</td><td>{e(r["name"])}</td><td>{e(r["title"])}</td><td>{e(r["why"])}</td></tr>' for r in removed_map)

# Alex's own map
am_rows = ""
for a in d["am_map"]:
    pill = ' <span class="pill y">refresh</span>' if a["stale"] else (' <span class="pill hold">placeholder</span>' if a["placeholder"] else "")
    am_rows += f'<tr><td class="who">{e(a["name"])}{pill}{("<span class=note>" + e(a["stale"]) + "</span>") if a["stale"] else ""}</td><td>{e(a["title"])}{(" (" + e(a["entity"]) + ")") if a["entity"] else ""}</td><td>{e(a["reports_to"] or "top of the map")}</td></tr>'

# Salesforce-known layer, grouped by plan account
known_html = ""
for g in d["known_groups"]:
    ppl = "".join(f'<tr><td>{e(p["name"])}</td><td>{e(p["title"])}</td><td>{e(p["email"])}</td><td>{e(p["lead_status"])}</td></tr>' for p in g["people"])
    known_html += (f'<div class="grp"><h4>{e(g["sf_company"])} <span class="pill g">{len(g["people"])}</span></h4><div class="meta2">{e(g["side"])} side &middot; Salesforce {e(g["sf_account_id"])} &middot; Account Type {e(g["account_type"])}</div>'
                   f'<details class="more"><summary>Show {len(g["people"])}</summary><div class="tablewrap"><table><thead><tr><th>Name</th><th>Title</th><th>Email</th><th>Lead status</th></tr></thead><tbody>{ppl}</tbody></table></div></details></div>')

n_routes = len(plan["routes"]); n_moves = len(plan["moves"]); n_bo = len(d["bo_maps"]); n_ver = sum(1 for v in EM.values() if v["status"].startswith("validated"))
BODY = f"""
<svg width="0" height="0" style="position:absolute" aria-hidden="true">{logo}</svg>
<div class="sheet">
<header class="hero" id="hero"><div class="wrap">
<svg class="logo" data-h="1"><use href="#ilogo"/></svg>
<div class="eyebrow" data-h="1">Elevance Health &middot; expansion plan &middot; the groups not using Intradiem</div>
<h1 data-h="2">Into the operations groups <span class="spark">by December.</span></h1>
<p class="sub" data-h="3">Six ways into the parts of Elevance that never touched the contract, four lanes with an owner each, dated moves through December, and the messages written and checked. The two back-office maps and the Salesforce layer sit behind the plan as the appendix. Built on the shape of the Cleveland Clinic room and the rules for expansion inside a customer: a distinct line from the sponsor, the account manager clears, the sponsor line untouched.</p>
<div class="hstats" data-h="4">
<div><b data-n="{n_routes}">{n_routes}</b><span>ways in</span></div>
<div><b data-n="4">4</b><span>lanes, one owner each</span></div>
<div><b data-n="{n_moves}">{n_moves}</b><span>dated moves to Dec 12</span></div>
<div><b data-n="{n_bo}">{n_bo}</b><span>back-office leaders, live-checked</span></div>
</div>
<div class="meta" data-h="4">
<div><span>For</span>Alex Bauer</div><div><span>From</span>Dallas Andrews</div><div><span>Date</span>Sep 11 2026</div><div><span>Refresh</span>After the record is reconciled</div>
</div>
</div></header>

<section><div class="wrap">
<div class="eyebrow">Ways in</div>
<h2>Six routes into the groups the contract never reached</h2>
<div class="routes">{routes}</div>
</div></section>

<section><div class="wrap">
<div class="eyebrow">Lanes</div>
<h2>Who does what, by week</h2>
<p>Four voices, one plan, Alex's. Each lane has an owner by role. Dates are the week the move belongs to; the record reconciliation on Sep 25 is the gate every later move waits on.</p>
<div class="lanes">{lanes}</div>
{mkt}
</div></section>

<section><div class="wrap">
<div class="eyebrow">Messages</div>
<h2>Written, checked, ready to match to the sender's voice</h2>
<p><b>{e(plan["senders_note"])}</b> Each message has one idea, opens on their world, names what we do in concrete terms without a product name, and ends on one question. Every number traces to the Value Repository or a dated public source. Open one to read it with its claims.</p>
<div class="msgs">{msgs}</div>
<h3 style="margin-top:28px">Account rules</h3>
<ul class="rules">{rules}</ul>
</div></section>

<section><div class="wrap">
<div class="eyebrow">Account</div>
<h2>What is known, and where it comes from</h2>
<p>The record on our side is the open item. Everything below is sourced; Alex's account plan is the starting point and is marked as a first run by Alex himself.</p>
<ul class="facts">{facts}</ul>
</div></section>

<section><div class="wrap">
<div class="eyebrow">Appendix, the maps</div>
<h2>The two back-office maps</h2>
<p>One new Sales Navigator map per company, because Carelon is its own company page. Every card carries a live LinkedIn profile checked Sep 11 2026 and its Salesforce status; "confirm" marks a placement or a badge for Alex to confirm as he adds the card. {n_ver} recipients carry a validated work email.</p>
{maps_html}
<details class="more" style="margin-top:14px"><summary>Removed after the live check ({len(removed_map)})</summary><div class="tablewrap"><table><thead><tr><th>Map</th><th>Name</th><th>Title</th><th>Why</th></tr></thead><tbody>{removed_html}</tbody></table></div></details>
</div></section>

<section><div class="wrap">
<div class="eyebrow">Appendix, the relationship map</div>
<h2>Alex's Elevance Health map, as shared</h2>
<p>Thirty cards on the contact-center line, the sponsor line this plan never touches. Four cards show a stale employer or a departure and are marked for a refresh; placeholder cards are the Carelon people Alex noted.</p>
<div class="tablewrap"><table><thead><tr><th>Name</th><th>Title</th><th>Reports to</th></tr></thead><tbody>{am_rows}</tbody></table></div>
</div></section>

<section class="known"><div class="wrap">
<div class="eyebrow">Appendix, Salesforce</div>
<h2>The {d["known_total"]} people Salesforce already knows</h2>
<p>Grouped by the plan or subsidiary account they sit under. This is the layer the marketing one-pager reaches; the CSV beside this page carries the same rows with an include flag and a reason on each exclusion. Salesforce presence is information, never a reason to leave someone off a map.</p>
{known_html}
</div></section>

<footer class="foot"><svg class="logo"><use href="#ilogo"/></svg><span>GTM Engineering &middot; Elevance Health &middot; Sep 11 2026</span><span>Internal to Intradiem. Sources: Alex's account plan (Sep 11 2026), Elevance Health newsroom (Feb 26 and Mar 31 2026), Elevance Q2 2026 results, Salesforce via Audiences, Sales Navigator, LinkedIn live checks, the Intradiem Value Repository.</span></footer>
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
html = ('<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>Elevance Health Expansion Room</title><style>' + fonts + CSS + '</style></head><body>' + BODY + '</body></html>')
out = HERE / "Elevance_Expansion_Room_Alex_Sep11.html"; out.write_text(html)
shutil.copy(out, pathlib.Path.home() / "Desktop/Intradiem Deliverables/Elevance Health Expansion Room (Alex) - Sep 11.html")
dep = pathlib.Path.home() / "Desktop/Intradiem Deliverables/deploy-save-rooms/elevance/alex"; dep.mkdir(parents=True, exist_ok=True); shutil.copy(out, dep / "index.html")
print(out, len(html), "bytes; staged at", dep, "(not deployed)")
