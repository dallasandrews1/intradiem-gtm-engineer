#!/usr/bin/env python3
"""Render one Back Office Account Map page per account (plus an index) from the roster.

Inputs  (same folder)
  BO_AccountMap_Roster_Inger.csv        from build_inger_roster.py
  inger_backoffice_candidates.csv       optional, from the 0-credit sourcing pull (rows with empty excluded_reason)
  inger_known_layer_companies.csv       SF account type per account
  _fonts_embed.css, _logo_symbol.svg    lifted from the Aug 25 operating-process page so the family matches

Output
  account_maps/<slug>.html   and   account_maps/index.html
Nothing here touches Clay, Lemlist, or Sales Navigator.
"""
import csv, html, os, re
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "account_maps")
os.makedirs(OUT, exist_ok=True)
DATE = "August 25, 2026"
AM = "Inger Escamilla"

fonts = open(os.path.join(HERE, "_fonts_embed.css")).read()
logo = open(os.path.join(HERE, "_logo_symbol.svg")).read()

def E(s):
    return html.escape(s or "", quote=True)

def slug(a):
    return re.sub(r"[^a-z0-9]+", "_", a.lower()).strip("_")

def clean_title(t):
    t = (t or "").strip()
    return t[:-3].rstrip() + "…" if t.endswith("...") else t

# ---------------- data ----------------
ALIASES = {"assurant": "Assurant", "cleveland": "Cleveland Clinic", "cox": "Cox Communications", "directv": "DIRECTV",
           "guardian": "Guardian Life", "goldman": "Goldman Sachs", "mckesson": "McKesson", "metlife": "MetLife",
           "prudential": "Prudential Financial", "rogers": "Rogers Communications", "travelers": "Travelers", "zurich": "Zurich North America"}
def canon(a):
    for k, v in ALIASES.items():
        if k in (a or "").lower():
            return v
    return a
roster = list(csv.DictReader(open(os.path.join(HERE, "BO_AccountMap_Roster_Inger.csv"))))
acct_type = {}
p = os.path.join(HERE, "inger_known_layer_companies.csv")
if os.path.exists(p):
    for r in csv.DictReader(open(p)):
        k = canon((r.get("requested_account") or r.get("account") or "").strip())
        v = (r.get("account_type") or r.get("Account Type") or "").strip()
        if k and (k not in acct_type or v.lower() == "customer"):
            acct_type[k] = v or acct_type.get(k, "")
known_count = defaultdict(int)
p = os.path.join(HERE, "inger_known_layer_people.csv")
if os.path.exists(p):
    for r in csv.DictReader(open(p)):
        known_count[r["account"]] += 1

sourced = defaultdict(list)
p = os.path.join(HERE, "inger_backoffice_candidates.csv")
if os.path.exists(p):
    for r in csv.DictReader(open(p)):
        if (r.get("excluded_reason") or "").strip():
            continue
        sourced[r["account"]].append(r)

FUNC_LABEL = {"back_office": "Back office", "contact_center": "Contact center", "tech_or_other": "Tech / other",
              "unknown": "", "shared_services": "Shared services", "claims": "Claims",
              "payment_billing": "Payments / billing", "fraud": "Fraud", "finance_ops": "Finance ops",
              "admin_ops": "Administration", "operations_general": "Operations", "top_officer": "Top officer"}


by_acct = defaultdict(list)
for r in roster:
    by_acct[canon(r["account"])].append(r)
for a, rows in list(sourced.items()):
    if canon(a) != a:
        sourced[canon(a)].extend(rows); del sourced[a]

# ---------------- page pieces ----------------
CSS = """
:root{--green:#2DB56E;--green-600:#228752;--green-300:#7BD3A0;--green-100:#C4ECD4;--forest:#014637;--orange:#F58220;--orange-600:#D96D12;
--ink:#202020;--ink-2:#5A5A5A;--ink-3:#9A9A9A;--bg:#FFFFFF;--sidebar:#F5F4F2;--zebra:#FAFAFA;--tint:rgba(45,181,110,.12);--tint-soft:rgba(45,181,110,.08);
--otint:rgba(245,130,32,.10);--otint-line:rgba(245,130,32,.28);--line:#E0E0E0;--line-strong:#BDBDBD;--r:8px;
--ff:'Roboto',-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;--ff-mono:'Roboto Mono',ui-monospace,SFMono-Regular,Menlo,monospace;--shadow:0 1px 2px rgba(20,30,25,.04)}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:var(--ff);background:var(--sidebar);color:var(--ink);line-height:1.6;-webkit-font-smoothing:antialiased}
.sheet{max-width:1120px;margin:0 auto;background:var(--bg)}
.wrap{max-width:1060px;margin:0 auto;padding:0 30px}
.eyebrow{font-family:var(--ff-mono);text-transform:uppercase;letter-spacing:.16em;font-size:11px;font-weight:600}
.logo{height:26px;width:auto;display:block;color:#014637}
.hero{background:var(--forest);color:#fff;padding:44px 0 40px;position:relative;overflow:hidden}
.hero::after{content:"";position:absolute;right:-160px;top:-120px;width:440px;height:440px;border-radius:50%;background:radial-gradient(circle,rgba(45,181,110,.30),transparent 62%)}
.hero .wrap{position:relative;z-index:1}
.hero .logo{height:46px;margin-bottom:24px;color:#fff}
.hero .eyebrow{color:var(--green-300)}
.hero h1{font-weight:900;font-size:40px;line-height:1.06;margin:14px 0 14px;letter-spacing:-.02em;max-width:24ch;text-wrap:balance}
.hero h1 .spark{color:var(--green-300)}
.hero p.sub{font-size:17px;max-width:68ch;color:#C7DAD1}
.hero p.sub b{color:#fff;font-weight:700}
.hero .meta{margin-top:26px;display:grid;grid-template-columns:repeat(4,auto);gap:14px 44px;justify-content:start}
.hero .meta div{color:#fff;font-size:14.5px;font-weight:500}
.hero .meta div span{display:block;font-family:var(--ff-mono);color:var(--green-300);font-size:10px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;margin-bottom:5px}
.hero a{color:#fff}
section{padding:36px 0;border-bottom:1px solid var(--line)}
section:last-of-type{border-bottom:none}
section > .wrap > .eyebrow{color:var(--green-600)}
h2{font-weight:900;font-size:28px;line-height:1.12;margin:10px 0 8px;letter-spacing:-.02em;text-wrap:balance}
h2 + .lede{font-size:15.5px;color:var(--ink-2);margin-bottom:18px;max-width:78ch}
p{color:var(--ink-2);max-width:78ch;margin-top:10px;font-size:15.5px}
p b{color:var(--ink);font-weight:700}
.statband{display:grid;grid-template-columns:repeat(4,1fr);gap:26px;background:var(--forest);border-radius:var(--r);padding:24px 32px;margin-top:22px;position:relative;overflow:hidden}
.statband::after{content:"";position:absolute;right:-130px;top:-150px;width:360px;height:360px;border-radius:50%;background:radial-gradient(circle,rgba(45,181,110,.22),transparent 62%)}
.statband > div{position:relative;z-index:1}
.statband .n{font-weight:900;font-size:28px;color:var(--green-300);letter-spacing:-.01em;line-height:1.1;font-variant-numeric:tabular-nums}
.statband .l{font-family:var(--ff-mono);font-size:10px;letter-spacing:.1em;color:#9DBBAE;text-transform:uppercase;margin-top:9px;line-height:1.6}
.tree{list-style:none;margin-top:16px;border-top:1px solid var(--line)}
.tree li{display:grid;grid-template-columns:1fr 150px 92px;gap:16px;align-items:baseline;padding:9px 0;border-bottom:1px solid var(--line);font-size:14.5px}
.tree li .who{color:var(--ink);font-weight:700}
.tree li .who i{font-style:normal;font-family:var(--ff-mono);color:var(--line-strong);font-weight:400;font-size:12px;margin-right:6px;letter-spacing:.06em}
.tree li .t{color:var(--ink-2);font-weight:400;margin-left:6px}
.tree li .fn,.tree li .crm{font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;font-weight:600;color:var(--ink-3)}
.tree li .crm.yes{color:var(--green-600)}
.tree li.leader .who{color:var(--forest)}
.pills{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.pill{font-family:var(--ff-mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;font-weight:600;padding:6px 12px;border-radius:6px;background:var(--otint);color:var(--orange-600);border:1px solid var(--otint-line)}
.gate{background:var(--tint-soft);border:1px solid var(--tint);border-left:4px solid var(--green);border-radius:var(--r);padding:18px 24px;margin-top:18px}
.gate p{font-size:14.5px;margin-top:0;max-width:none}
.callout{background:var(--otint);border:1px solid var(--otint-line);border-left:4px solid var(--orange);border-radius:var(--r);padding:18px 24px;margin-top:18px}
.callout p{font-size:14.5px;margin-top:0;max-width:none}
.tablewrap{overflow-x:auto;margin-top:16px}
table{width:100%;border-collapse:collapse;font-size:14.5px;min-width:720px}
th{font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--green-600);text-align:left;padding:0 16px 10px 0;border-bottom:1px solid var(--line);font-weight:600}
td{padding:11px 16px 11px 0;border-bottom:1px solid var(--line);color:var(--ink-2);vertical-align:top}
tbody tr:nth-child(even){background:var(--zebra)}
td.who{white-space:nowrap;color:var(--ink);font-weight:700}
td.who a{color:inherit;text-decoration:none;border-bottom:1px solid var(--green-100)}
td.b{font-family:var(--ff-mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3);white-space:nowrap}
td.top{color:var(--forest);font-weight:700}
td.clr{white-space:nowrap}
.box{display:inline-block;width:14px;height:14px;border:1.5px solid var(--line-strong);border-radius:3px;vertical-align:-2px;margin-right:6px}
.clr span{font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3);margin-right:14px}
.foot{padding:26px 0 46px;text-align:center;color:var(--ink-3);font-family:var(--ff-mono);font-size:11px;letter-spacing:.08em;background:var(--bg);text-transform:uppercase}
.foot .logo{height:26px;display:inline-block;margin:0 auto 12px;opacity:.85}
.foot span{display:block;margin-top:4px}
.idx{list-style:none;margin-top:18px;border-top:1px solid var(--line)}
.idx li{display:grid;grid-template-columns:1.4fr 120px 90px 90px 110px 110px;gap:16px;align-items:center;padding:12px 0;border-bottom:1px solid var(--line);font-size:14.5px}
.idx li.h{font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--green-600);font-weight:600;padding:0 0 10px}
.idx li a{color:var(--ink);font-weight:700;text-decoration:none;border-bottom:1px solid var(--green-100)}
.idx li .num{font-variant-numeric:tabular-nums;color:var(--ink-2)}
.idx li .st{font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3)}
@media(max-width:860px){.hero h1{font-size:30px}.hero .meta{grid-template-columns:1fr 1fr}.statband{grid-template-columns:1fr 1fr}.tree li{grid-template-columns:1fr}.idx li{grid-template-columns:1fr 1fr}}
@media print{body{background:#fff;-webkit-print-color-adjust:exact;print-color-adjust:exact}@page{margin:14mm}.statband,.gate,.callout,.tree li,tr{break-inside:avoid}}
"""

def head(title):
    return f"""<title>{E(title)}</title>
<style>{fonts}{CSS}</style>
<svg width="0" height="0" style="position:absolute" aria-hidden="true">{logo}</svg>"""

def foot():
    return f"""<div class="foot"><svg class="logo"><use href="#ilogo"/></svg><span>GTM Engineering &middot; Back office expansion &middot; {DATE}</span><span>Roster: BO_AccountMap_Roster_Inger.csv &middot; clearance state mirrors owner_cleared</span></div>"""

def band_label(b):
    return {"C": "C-level", "EVP": "EVP", "SVP": "SVP", "VP": "VP", "Director": "Director", "Manager": "Manager", "Unknown": ""}.get(b, b)

def render_account(acct, rows):
    canvas = [r for r in rows if r["source"] == "am_map:map"]
    parent = {r["full_name"]: r["reports_to"] for r in canvas}
    kids = defaultdict(list)
    for r in canvas:
        kids[r["reports_to"]].append(r)
    leaders = [r for r in canvas if r["tree_depth"] == "0" or kids.get(r["full_name"])]
    leader_names = {r["full_name"] for r in leaders}

    # candidates: roster CANDIDATE rows (Jul 26 pull + recommended) + sourced rows from the 0-credit pull
    cands = []
    for r in rows:
        if r["gate_result"] == "CANDIDATE":
            cands.append({"name": r["full_name"], "title": clean_title(r["title"]), "func": r["function"], "band": r["band"],
                          "src": "Clay, Jul 26 pull" if r["source"].startswith("clay_jul26") else "Sales Nav suggestion",
                          "url": r.get("linkedin_url", ""), "top": r["band"] in ("C", "EVP")})
    seen = {c["name"].lower() for c in cands}
    for r in sourced.get(acct, []):
        if r["full_name"].lower() in seen:
            continue
        cands.append({"name": r["full_name"], "title": clean_title(r["title"]), "func": r.get("function_guess", ""), "band": r.get("band_guess", ""),
                      "src": "Clay search", "url": r.get("linkedin_url", ""), "top": r.get("function_guess") == "top_officer" or r.get("band_guess") in ("C", "EVP")})
    order = {"C": 0, "EVP": 1, "SVP": 2, "VP": 3, "Director": 4}
    cands.sort(key=lambda c: (not c["top"], order.get(c["band"], 9), c["name"]))

    # tree (depth-first)
    tree_items = []
    def walk(name, depth):
        for r in sorted(kids.get(name, []), key=lambda x: x["full_name"]):
            tree_items.append((r, depth)); walk(r["full_name"], depth + 1)
    walk("", 0)
    placed = {r["full_name"] for r, _ in tree_items}
    for r in canvas:  # orphans whose parent card was off-screen
        if r["full_name"] not in placed:
            tree_items.append((r, 0))

    tree_html = "".join(
        f'<li class="{"leader" if r["full_name"] in leader_names else ""}"><span class="who"><i>{"&middot;&nbsp;" * d}</i>{E(r["full_name"])}'
        f'<span class="t">{E(clean_title(r["title"]))}</span></span>'
        f'<span class="fn">{E(FUNC_LABEL.get(r["function"], r["function"]))}</span>'
        f'<span class="crm {"yes" if r["crm_badge"].upper() == "CRM" else ""}">{"In Salesforce" if r["crm_badge"].upper() == "CRM" else ("Not in SF" if r["crm_badge"] else "Placeholder")}</span></li>'
        for r, d in tree_items)

    pills = "".join(f'<span class="pill">{E(r["full_name"])}</span>' for r in leaders)

    cand_rows = "".join(
        f'<tr><td class="who{" top" if c["top"] else ""}">{("<a href=%s>%s</a>" % (E(c["url"]), E(c["name"]))) if c["url"] else E(c["name"])}</td>'
        f'<td>{E(c["title"])}</td><td class="b">{E(FUNC_LABEL.get(c["func"], c["func"]))}</td><td class="b">{E(band_label(c["band"]))}</td>'
        f'<td class="b">{E(c["src"])}</td><td class="clr"><span class="box"></span><span>Clear</span><span class="box"></span><span>Hold</span></td></tr>'
        for c in cands)

    atype = acct_type.get(acct, "")
    sf_known = known_count.get(acct, 0)
    not_customer = atype and atype.lower() != "customer"
    posture = (f"<div class=\"callout\"><p><b>Salesforce lists this account as {E(atype)}, not Customer.</b> Names below are treated with the new-logo posture (start at the top) until the account record is confirmed.</p></div>" if not_customer else "")
    cand_note = ("" if cands else "<div class=\"callout\"><p><b>No back-office candidates yet.</b> The map covers the contact-center line only; the back-office sourcing pull for this account is the next step.</p></div>")

    return f"""{head(f"{acct} back office map")}
<div class="sheet">
<header class="hero"><div class="wrap">
<svg class="logo"><use href="#ilogo"/></svg>
<div class="eyebrow">GTM Engineering &middot; Back office expansion &middot; <a href="index.html" style="text-decoration:none">All accounts</a></div>
<h1>{E(acct)}: <span class="spark">back office account map</span></h1>
<p class="sub">Your map is the off-limits layer. Anyone under the same leaders is yours to call. The names at the bottom are new back-office leaders, one column to clear or hold.</p>
<div class="meta"><div><span>Account manager</span>{E(AM)}</div><div><span>Prepared by</span>Dallas Andrews</div><div><span>Date</span>{DATE}</div><div><span>Salesforce</span>{E(atype or "not matched")} &middot; {sf_known:,} known contacts</div></div>
</div></header>

<section><div class="wrap">
<div class="statband">
<div><div class="n">{len(canvas)}</div><div class="l">On your Sales Nav map<br>off limits</div></div>
<div><div class="n">{len(leaders)}</div><div class="l">Leaders whose reports<br>need your call</div></div>
<div><div class="n">{len(cands)}</div><div class="l">Back-office names<br>for clearance</div></div>
<div><div class="n">0</div><div class="l">Cleared so far</div></div>
</div>
{posture}
</div></section>

<section><div class="wrap">
<div class="eyebrow">Layer 1</div><h2>Your map, as shared</h2>
<p class="lede">Every card on your Relationship Map, in its reporting line. None of these people receive anything from this motion.</p>
<ul class="tree">{tree_html}</ul>
</div></section>

<section><div class="wrap">
<div class="eyebrow">Layer 2</div><h2>Sponsor lines</h2>
<p class="lede">Anyone who reports into one of these leaders is held until you say otherwise.</p>
<div class="pills">{pills}</div>
</div></section>

<section><div class="wrap">
<div class="eyebrow">Layer 3</div><h2>Back-office names for clearance</h2>
<p class="lede">Shared services, claims, payments, fraud, administration. SVP to Director, plus a top officer where the line is separate from yours. Mark each Clear or Hold; nothing goes out until the column is filled.</p>
{cand_note}
<div class="tablewrap"><table><thead><tr><th>Name</th><th>Title</th><th>Function</th><th>Level</th><th>Found via</th><th>Your call</th></tr></thead><tbody>{cand_rows}</tbody></table></div>
<div class="gate"><p><b>Wave 1 takes six per account</b>: two at the top, four in the VP to Director band. Email first, then LinkedIn, then a call only on names you cleared. Intradiem is named only where you say the brand is known outside the contact center.</p></div>
</div></section>
{foot()}
</div>"""

def render_index(summary):
    li = "".join(
        f'<li><a href="{s["slug"]}.html">{E(s["acct"])}</a><span class="st">{E(s["type"] or "not matched")}</span>'
        f'<span class="num">{s["map"]}</span><span class="num">{s["leaders"]}</span><span class="num">{s["cands"]}</span><span class="st">pending</span></li>'
        for s in summary)
    tot = sum(s["cands"] for s in summary)
    return f"""{head("Inger's accounts: back office maps")}
<div class="sheet">
<header class="hero"><div class="wrap">
<svg class="logo"><use href="#ilogo"/></svg>
<div class="eyebrow">GTM Engineering &middot; Back office expansion</div>
<h1>Back office account maps, <span class="spark">Inger's twelve</span></h1>
<p class="sub">One page per account: the Relationship Map as shared, the sponsor lines it implies, and the new back-office names waiting on a clear or hold.</p>
<div class="meta"><div><span>Account manager</span>{E(AM)}</div><div><span>Prepared by</span>Dallas Andrews</div><div><span>Date</span>{DATE}</div><div><span>Status</span>{len(summary)} maps in &middot; {tot} names for clearance &middot; 0 cleared</div></div>
</div></header>
<section><div class="wrap">
<ul class="idx"><li class="h"><span>Account</span><span>Salesforce</span><span>On map</span><span>Leaders</span><span>For clearance</span><span>Clearance</span></li>{li}</ul>
<div class="gate"><p><b>How this runs.</b> You mark Clear or Hold on each page (or the shared sheet). Cleared names load into the customer sequence, six per account, Nate as sender. Held names never leave the roster.</p></div>
</div></section>
{foot()}
</div>"""

summary = []
for acct in sorted(by_acct):
    rows = by_acct[acct]
    page = render_account(acct, rows)
    s = slug(acct)
    open(os.path.join(OUT, f"{s}.html"), "w").write(page)
    canvas = [r for r in rows if r["source"] == "am_map:map"]
    kids = defaultdict(int)
    for r in canvas:
        kids[r["reports_to"]] += 1
    leaders = [r for r in canvas if r["tree_depth"] == "0" or kids.get(r["full_name"])]
    ncand = sum(1 for r in rows if r["gate_result"] == "CANDIDATE") + len(sourced.get(acct, []))
    summary.append({"acct": acct, "slug": s, "type": acct_type.get(acct, ""), "map": len(canvas), "leaders": len(leaders), "cands": ncand})
open(os.path.join(OUT, "index.html"), "w").write(render_index(summary))
for s in summary:
    print(f"{s['acct']:<24} {s['type'] or '-':<10} map {s['map']:>2}  leaders {s['leaders']:>2}  candidates {s['cands']:>3}")
print("pages:", len(summary) + 1, "->", OUT)

# ---------------- combined single-file page (for the Artifact link) ----------------
def render_combined(summary):
    tot = sum(s["cands"] for s in summary)
    nav = " &middot; ".join(f'<a href="#{s["slug"]}">{E(s["acct"])}</a>' for s in summary)
    li = "".join(
        f'<li><a href="#{s["slug"]}">{E(s["acct"])}</a><span class="st">{E(s["type"] or "not matched")}</span>'
        f'<span class="num">{s["map"]}</span><span class="num">{s["leaders"]}</span><span class="num">{s["cands"]}</span><span class="st">pending</span></li>'
        for s in summary)
    parts = [f"""{head("Inger's accounts: back office maps")}
<style>.acct{{border-top:6px solid var(--forest);margin-top:12px}} .acct .hero{{padding:30px 0 26px}} .acct .hero h1{{font-size:30px}} .nav{{font-family:var(--ff-mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;line-height:2.2;margin-top:18px}} .nav a{{color:var(--green-600);text-decoration:none}} .hero .nav a{{color:var(--green-300)}}</style>
<div class="sheet">
<header class="hero"><div class="wrap">
<svg class="logo"><use href="#ilogo"/></svg>
<div class="eyebrow">GTM Engineering &middot; Back office expansion</div>
<h1>Back office account maps, <span class="spark">Inger's twelve</span></h1>
<p class="sub">One section per account: the Relationship Map as shared, the sponsor lines it implies, and the new back-office names waiting on a clear or hold.</p>
<div class="meta"><div><span>Account manager</span>{E(AM)}</div><div><span>Prepared by</span>Dallas Andrews</div><div><span>Date</span>{DATE}</div><div><span>Status</span>{len(summary)} maps in &middot; {tot} names for clearance &middot; 0 cleared</div></div>
<div class="nav">{nav}</div>
</div></header>
<section><div class="wrap">
<ul class="idx"><li class="h"><span>Account</span><span>Salesforce</span><span>On map</span><span>Leaders</span><span>For clearance</span><span>Clearance</span></li>{li}</ul>
<div class="gate"><p><b>How this runs.</b> Inger marks Clear or Hold per name. Cleared names load into the customer sequence, six per account, Nate as sender. Held names never leave the roster. Every name on her map, and everyone under the same leaders, is off limits by default.</p></div>
</div></section>
</div>"""]
    for s in summary:
        page = render_account(s["acct"], by_acct[s["acct"]])
        body = page.split("</svg>", 1)[1]  # drop the per-page head + logo symbol
        body = body.replace('<div class="sheet">', f'<div class="sheet acct" id="{s["slug"]}">', 1)
        body = body.replace('<a href="index.html" style="text-decoration:none">All accounts</a>', '<a href="#top" style="text-decoration:none">Top</a>')
        parts.append(body)
    return "\n".join(parts).replace('<header class="hero">', '<header class="hero" id="top">', 1)

open(os.path.join(OUT, "inger_all_accounts.html"), "w").write(render_combined(summary))
print("combined page written")
