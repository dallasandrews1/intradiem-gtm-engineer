#!/usr/bin/env python3
"""EMEA channel partner map for the partner team (Frank's Sep 2 ask).

Reads landscape/data/<region>.json (built by merge_landscape.py from the research fan-out)
and writes landscape/<Region>_Channel_Partner_Map.html plus a CSV of every partner row.
Same visual family as the account briefs (brief_template.html), no engine dependencies,
so the page can be shared as one file or deployed as is.

Run: python3 build_landscape.py            (region emea)
     python3 build_landscape.py apac       (another region file, when one exists)
"""
import csv, datetime, html as H, json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
TPL = HERE / "frank_selfserve/skills/partner-account-brief/brief_template.html"
TODAY = datetime.date.today()
region = sys.argv[1] if len(sys.argv) > 1 else "emea"
d = json.loads((HERE / "landscape/data" / f"{region}.json").read_text())

VENDORS = d["vendor_order"]                     # slugs in display order
VN = {v["slug"]: v["name"] for v in d["vendors"]}
TYPE_LABEL = {"distributor": "Distributor", "reseller": "Reseller", "systems_integrator": "Systems integrator",
              "msp": "Managed service provider", "carrier": "Carrier / telco", "bpo_cx_outsourcer": "BPO / CX outsourcer",
              "consultancy": "Consultancy", "referral": "Referral agent"}
E = lambda s: H.escape(str(s if s is not None else ""), quote=True)


def short_url(u):
    return re.sub(r"^https?://(www\.)?", "", u)[:60]


def src_html(sources, limit=3):
    out = []
    for s in sources[:limit]:
        if isinstance(s, str):
            u, dt = s, ""
        else:
            u, dt = s.get("url", ""), s.get("date", "")
        if not u:
            continue
        out.append(f'<a href="{E(u)}" target="_blank" rel="noopener">{E(short_url(u))}</a>' + (f' ({E(dt)})' if dt else ""))
    return " &middot; ".join(out)


partners = sorted(d["partners"], key=lambda p: (-len(p["carries"]), p["name"].lower()))
multi = [p for p in partners if len(p["carries"]) >= 2]
countries = sorted({c for p in partners for c in p.get("emea_coverage", [])})
types_present = [t for t in TYPE_LABEL if any(p["partner_type"] == t for p in partners)]

# ---------- body ----------
B = []
A = B.append

A('<section><p class="label">In one screen</p><ul>')
for t in d["tldr"]:
    A(f"<li>{t}</li>")
A("</ul></section>")

# market share
A('<section><p class="label">Market share, what is actually published</p>')
A(f'<h2>{d["share_h2"]}</h2>')
A(f'<p>{d["share_intro"]}</p>')
A('<div class="splist">')
for sp in d["share_points"]:
    reg = sp["region"]
    rcls = "glob" if reg.upper().startswith("GLOBAL") else ("eu" if reg.lower().startswith(("europe", "emea")) else "")
    A(f'<div class="sp"><div class="spl"><b>{E(sp["vendor"])}</b><span class="pill {rcls}">{E(reg)}</span><span class="pill">{E(sp["measured_as"])}</span></div>'
      f'<div class="spr"><div class="spv">{E(sp["value"])}</div><div class="spm">{E(sp["metric"])}' + (f'. {E(sp["note"])}' if sp.get("note") else "") + '</div>'
      f'<div class="sps"><a href="{E(sp["source_url"])}" target="_blank" rel="noopener">{E(short_url(sp["source_url"]))}</a> ({E(sp["source_date"])})</div></div></div>')
A("</div>")
if d.get("share_note"):
    A(f'<div class="callout" style="margin-top:14px"><ul>' + "".join(f"<li>{n}</li>" for n in d["share_note"]) + "</ul></div>")
A("</section>")

# vendor cards
A('<section><p class="label">The seven platforms in EMEA</p>')
A(f'<h2>{d["vendors_h2"]}</h2><div class="vgrid">')
for v in d["vendors"]:
    n = sum(1 for p in partners if v["slug"] in p["carries"])
    A(f'<div class="vc" id="v-{v["slug"]}"><div class="vh"><b>{E(v["name"])}</b><span class="cnt">{n} partners mapped</span></div>')
    A(f'<p>{v["context"]}</p>')
    if v.get("program"):
        A(f'<p class="prog"><span>Program</span>{v["program"]}</p>')
    if v.get("share"):
        A(f'<p class="prog"><span>Share</span>{v["share"]}</p>')
    A("</div>")
A("</div></section>")

# the map
A('<section><p class="label">The map</p>')
A(f'<h2>{d["map_h2"]}</h2><p>{d["map_intro"]}</p>')
A('<div class="filters">')
A('<div class="fg"><span class="fl">Platform</span>' + "".join(f'<button type="button" class="chip" data-f="v" data-v="{s}">{E(VN[s])}</button>' for s in VENDORS) + '</div>')
A('<div class="fg"><span class="fl">Type</span>' + "".join(f'<button type="button" class="chip" data-f="t" data-v="{t}">{E(TYPE_LABEL[t])}</button>' for t in types_present) + '</div>')
A('<div class="fg"><span class="fl">Carries</span><button type="button" class="chip" data-f="m" data-v="2">2+ platforms</button><button type="button" class="chip" data-f="m" data-v="3">3+ platforms</button></div>')
A('<input id="q" type="search" placeholder="Search partner, country, or region" autocomplete="off">')
A('<div id="count"></div></div>')
A('<div id="list">')
for p in partners:
    cov = ", ".join(p.get("emea_coverage", []))
    hay = " ".join([p["name"], p.get("hq_country", ""), cov, TYPE_LABEL.get(p["partner_type"], "")]).lower()
    vs = " ".join(p["carries"].keys())
    A(f'<div class="rec" data-h="{E(hay)}" data-v="{vs}" data-t="{p["partner_type"]}" data-m="{len(p["carries"])}">')
    A(f'<div class="rh"><b>{E(p["name"])}</b><span class="pill ty">{E(TYPE_LABEL.get(p["partner_type"], p["partner_type"]))}</span>'
      + (f'<span class="pill hq">{E(p["hq_country"])}</span>' if p.get("hq_country") else "")
      + (f'<span class="pill mv">{len(p["carries"])} platforms</span>' if len(p["carries"]) >= 2 else "") + "</div>")
    if cov:
        A(f'<div class="rm">Covers: {E(cov)}</div>')
    A('<div class="vrow">')
    for s in VENDORS:
        if s in p["carries"]:
            c = p["carries"][s]
            conf = c.get("confidence", "").upper()
            rel = c.get("relationship", ""); rel = rel if len(rel) <= 170 else rel[:167].rsplit(" ", 1)[0] + "..."
            A(f'<div class="vt c-{conf.lower()}"><span class="vn">{E(VN[s])}</span><span class="rel">{E(rel)}</span>'
              f'<span class="ev">{E(c.get("evidence", ""))}</span><span class="sr">{src_html(c.get("sources", []), 2)}'
              + (f' &middot; <i>{conf.lower()} confidence</i>' if conf else "") + '</span></div>')
    A("</div>")
    if p.get("scale_signal") and p["scale_signal"].lower() not in ("none found", "none"):
        A(f'<div class="rn"><span>Scale</span>{E(p["scale_signal"])}</div>')
    if p.get("share_statement") and p["share_statement"].lower() not in ("none", "none found", ""):
        A(f'<div class="rn"><span>Share signal</span>{E(p["share_statement"])}</div>')
    if p.get("also_carries"):
        A(f'<div class="rn"><span>Also carries</span>{E(", ".join(p["also_carries"]))}</div>')
    A("</div>")
A("</div></section>")

# where to start
A('<section><p class="label">Where to start</p>')
A(f'<h2>{d["start_h2"]}</h2>')
A('<div class="start">')
for i, s in enumerate(d["start"], 1):
    A(f'<div class="st"><span class="n">{i}</span><div><b>{s["title"]}</b><p>{s["body"]}</p></div></div>')
A("</div></section>")

# how this was built
A('<section><p class="label">How this map was built</p>')
A(f'<h2>{d["method_h2"]}</h2><p>{d["method_intro"]}</p>')
A('<table class="meth"><thead><tr><th>Platform</th><th>Read in full</th><th>Plus</th><th>EMEA partners on the map</th></tr></thead><tbody>')
for v in d["vendors"]:
    n = sum(1 for p in partners if v["slug"] in p["carries"])
    A(f'<tr><td class="nm">{E(v["name"])}</td><td>{v.get("method_read", "")}</td><td>{v.get("method_plus", "")}</td><td><b>{n}</b></td></tr>')
A('</tbody></table>')
if d.get("method_notes"):
    A('<ul style="margin-top:14px">' + "".join(f"<li>{n}</li>" for n in d["method_notes"]) + "</ul>")
A("</section>")

extra = """
  .splist{margin-top:4px}
  .sp{display:grid;grid-template-columns:200px 1fr;gap:6px 18px;padding:12px 0;border-top:1px solid var(--rule)}
  .sp:first-child{border-top:none;padding-top:4px}
  .spl b{display:block;color:var(--forest);font-size:14px;margin-bottom:6px}
  .spl .pill{margin-right:4px}
  .pill.glob{background:rgba(245,130,32,.12);border-color:transparent;color:#B25E12}
  .pill.eu{background:rgba(45,181,110,.14);border-color:transparent;color:var(--deep)}
  .spv{font-weight:700;color:var(--ink);font-size:14.5px;line-height:1.4}
  .spm{font-size:13px;color:var(--ink2);margin-top:3px}
  .sps{font-size:11.5px;color:var(--mut);margin-top:3px}
  .sps a{color:var(--deep);text-decoration:none}
  @media(max-width:700px){.sp{grid-template-columns:1fr}}
  .vgrid{display:grid;grid-template-columns:1fr 1fr;gap:14px}
  .vc{border:1px solid var(--rule);border-radius:8px;padding:14px 16px;background:#fff}
  .vc .vh{display:flex;justify-content:space-between;align-items:baseline;gap:10px;margin-bottom:6px}
  .vc .vh b{color:var(--forest);font-size:16px}
  .vc .cnt{font-family:'Roboto Mono',monospace;font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:var(--deep);white-space:nowrap}
  .vc p{font-size:13.5px;line-height:1.5}
  .vc .prog{font-size:12.5px;color:var(--mut);margin-top:6px}
  .vc .prog span{font-family:'Roboto Mono',monospace;font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--deep);margin-right:8px}
  .filters{margin:0 0 6px}
  .fg{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin-bottom:8px}
  .fl{font-family:'Roboto Mono',monospace;font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:var(--mut);width:64px}
  .chip{font-family:'Roboto',sans-serif;font-size:12.5px;padding:5px 11px;border-radius:999px;border:1px solid var(--rule);background:#fff;color:var(--ink2);cursor:pointer}
  .chip.on{background:var(--forest);border-color:var(--forest);color:#fff}
  #q{width:100%;padding:11px 14px;font-family:inherit;font-size:14.5px;border:1px solid var(--rule);border-radius:8px;color:var(--ink);background:#fff;margin-top:6px}
  #q:focus{outline:2px solid var(--green);outline-offset:1px}
  #count{font-family:'Roboto Mono',monospace;font-size:11px;color:var(--mut);margin:10px 0 2px;letter-spacing:.06em;text-transform:uppercase}
  .rec{padding:14px 0;border-top:1px solid var(--rule)}
  .rh{display:flex;align-items:baseline;gap:8px;flex-wrap:wrap}
  .rh b{color:var(--forest);font-size:15.5px}
  .rm{font-size:12.5px;color:var(--mut);margin-top:2px}
  .rn{font-size:13px;color:var(--ink2);margin-top:6px}
  .rn span{font-family:'Roboto Mono',monospace;font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--deep);margin-right:8px}
  .pill{font-family:'Roboto Mono',monospace;font-size:9.5px;letter-spacing:.06em;text-transform:uppercase;font-weight:600;padding:2px 8px;border-radius:999px;border:1px solid var(--rule);color:var(--mut)}
  .pill.mv{background:var(--forest);border-color:transparent;color:#fff}
  .pill.hq{background:#F0EFED;border-color:transparent}
  .vrow{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:8px}
  .vt{border-left:3px solid var(--green);padding:6px 10px;background:#FAFAF9;border-radius:0 6px 6px 0;font-size:12.5px;line-height:1.45}
  .vt.c-low{border-left-color:var(--orange)}
  .vt.c-medium{border-left-color:#7BD3A0}
  .vt .vn{display:inline-block;font-weight:700;color:var(--forest);margin-right:6px}
  .vt .rel{display:inline-block;font-family:'Roboto Mono',monospace;font-size:10px;color:var(--deep);letter-spacing:.03em}
  .vt .ev{display:block;color:var(--ink2);margin-top:2px}
  .vt .sr{display:block;font-size:11px;color:var(--mut);margin-top:2px}
  .vt .sr a{color:var(--deep);text-decoration:none}
  table.meth td{font-size:13px}
  table.meth td.nm{white-space:nowrap}
  .start .st{display:grid;grid-template-columns:34px 1fr;gap:12px;padding:12px 0;border-top:1px solid var(--rule)}
  .start .st:first-child{border-top:none;padding-top:0}
  .start .n{width:28px;height:28px;border-radius:50%;background:var(--forest);color:#fff;font-family:'Roboto Mono',monospace;font-size:12px;font-weight:600;display:flex;align-items:center;justify-content:center}
  .start b{color:var(--forest);display:block;margin-bottom:3px}
  .start p{font-size:13.5px;margin:0}
  @media(max-width:700px){.vgrid,.vrow{grid-template-columns:1fr}}
  @media print{.filters{display:none}.rec{break-inside:avoid}}
"""
script = """
<script>
(function(){
  var q=document.getElementById('q'),recs=[].slice.call(document.querySelectorAll('.rec')),c=document.getElementById('count');
  var chips=[].slice.call(document.querySelectorAll('.chip')),f={v:[],t:[],m:0};
  function run(){var v=q.value.trim().toLowerCase(),n=0;
    recs.forEach(function(r){var ok=!v||r.getAttribute('data-h').indexOf(v)>-1;
      if(ok&&f.v.length){var vs=r.getAttribute('data-v').split(' ');ok=f.v.every(function(x){return vs.indexOf(x)>-1;});}
      if(ok&&f.t.length){ok=f.t.indexOf(r.getAttribute('data-t'))>-1;}
      if(ok&&f.m){ok=+r.getAttribute('data-m')>=f.m;}
      r.hidden=!ok;if(ok)n++;});
    c.textContent=n+' of '+recs.length+' partners';}
  chips.forEach(function(ch){ch.addEventListener('click',function(){var k=ch.getAttribute('data-f'),val=ch.getAttribute('data-v');
    if(k==='m'){var was=ch.classList.contains('on');chips.filter(function(x){return x.getAttribute('data-f')==='m';}).forEach(function(x){x.classList.remove('on');});f.m=was?0:+val;if(!was)ch.classList.add('on');}
    else{ch.classList.toggle('on');var i=f[k].indexOf(val);if(i>-1)f[k].splice(i,1);else f[k].push(val);}
    run();});});
  q.addEventListener('input',run);run();
})();
</script>
"""
page = (TPL.read_text()
        .replace("{{ACCOUNT}}", d["title"])
        .replace("{{ANGLE}}", d["angle"])
        .replace("{{SUBHEAD}}", d["subhead"])
        .replace("{{DATE}}", TODAY.strftime("%b %-d %Y"))
        .replace("{{BODY}}", "\n".join(B))
        .replace("</style>", extra + "</style>")
        .replace("</body>", script + "</body>")
        .replace(f"<title>{d['title']} | Account brief</title>", f"<title>{d['title']}</title>")
        .replace('<p class="eyebrow">Partner channel &middot; Account brief</p>', '<p class="eyebrow">Partner channel &middot; Channel landscape</p>')
        .replace("<span>Internal working document &middot; sources and flags as marked</span>", "<span>Internal working document &middot; public sources, confidence as marked &middot; not a vendor-endorsed list</span>"))
assert "—" not in page and "{{" not in page, "placeholder or em dash left"
out = HERE / "landscape" / f"{region.upper()}_Channel_Partner_Map.html"
out.write_text(page)

# CSV
csv_path = HERE / "landscape" / f"{region.upper()}_Channel_Partners.csv"
with open(csv_path, "w", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["partner", "hq_country", "partner_type", "emea_coverage", "platforms_carried", "platform_count"]
               + [f"{VN[s]} relationship" for s in VENDORS] + [f"{VN[s]} confidence" for s in VENDORS]
               + ["also_carries", "scale_signal", "share_statement", "sources"])
    for p in partners:
        w.writerow([p["name"], p.get("hq_country", ""), TYPE_LABEL.get(p["partner_type"], p["partner_type"]),
                    "; ".join(p.get("emea_coverage", [])), "; ".join(VN[s] for s in VENDORS if s in p["carries"]), len(p["carries"])]
                   + [p["carries"].get(s, {}).get("relationship", "") for s in VENDORS]
                   + [p["carries"].get(s, {}).get("confidence", "") for s in VENDORS]
                   + ["; ".join(p.get("also_carries", [])), p.get("scale_signal", ""), p.get("share_statement", ""),
                      "; ".join((s if isinstance(s, str) else s.get("url", "")) for s in p.get("sources", []))])
# skill template: same head, CSS and filter script, slots instead of content
tpl = (TPL.read_text()
       .replace("</style>", extra + "</style>")
       .replace("</body>", script + "</body>")
       .replace("<title>{{ACCOUNT}} | Account brief</title>", "<title>{{TITLE}}</title>")
       .replace("<h1>{{ACCOUNT}}: {{ANGLE}}</h1>", "<h1>{{TITLE}}: {{ANGLE}}</h1>")
       .replace('<p class="eyebrow">Partner channel &middot; Account brief</p>', '<p class="eyebrow">Partner channel &middot; Channel landscape</p>')
       .replace("<span>Internal working document &middot; sources and flags as marked</span>", "<span>Internal working document &middot; public sources, confidence as marked &middot; not a vendor-endorsed list</span>"))
(HERE / "frank_selfserve/skills/partner-channel-landscape/landscape_template.html").write_text(tpl)
print(f"{out.name}: {len(page):,} bytes, {len(partners)} partners ({len(multi)} multi-platform), {len(d['share_points'])} share points; {csv_path.name}")
