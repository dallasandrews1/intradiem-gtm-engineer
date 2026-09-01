#!/usr/bin/env python3
"""One-file artifact: the NEW back-office map per account (senior executives -> leads by function) + lead table.
Reads BO_Map_Build_Sheets_Inger.csv. No AM-map content on the page."""
import csv, html, os, re
from collections import defaultdict, OrderedDict
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "account_maps", "inger_backoffice_maps.html")
DATE = "August 25, 2026"; AM = "Inger Escamilla"
E = lambda s: html.escape(s or "")
fonts = open(os.path.join(HERE, "_fonts_embed.css")).read()
logo = open(os.path.join(HERE, "_logo_symbol.svg")).read()
slug = lambda a: re.sub(r"[^a-z0-9]+", "_", a.lower()).strip("_")
def short(t, n=46):
    t = (t or "").strip()
    return t if len(t) <= n else t[:n-1].rstrip() + "…"

rows = list(csv.DictReader(open(os.path.join(HERE, "BO_Map_Build_Sheets_Inger.csv"))))
by = OrderedDict()
for r in rows:
    by.setdefault(r["account"], []).append(r)
acct_type = {}
p = os.path.join(HERE, "inger_known_layer_companies.csv")
if os.path.exists(p):
    for r in csv.DictReader(open(p)):
        a = r.get("account", "")
        for k in by:
            if k.lower().split()[0] in a.lower() and (k not in acct_type or (r.get("account_type") or "").lower() == "customer"):
                acct_type[k] = r.get("account_type") or acct_type.get(k, "")

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
.hero{background:var(--forest);color:#fff;padding:44px 0 36px;position:relative;overflow:hidden}
.hero::after{content:"";position:absolute;right:-160px;top:-120px;width:440px;height:440px;border-radius:50%;background:radial-gradient(circle,rgba(45,181,110,.30),transparent 62%)}
.hero .wrap{position:relative;z-index:1}
.hero .logo{height:46px;margin-bottom:24px;color:#fff}
.hero .eyebrow{color:var(--green-300)}
.hero h1{font-weight:900;font-size:40px;line-height:1.06;margin:14px 0 14px;letter-spacing:-.02em;max-width:24ch;text-wrap:balance}
.hero h1 .spark{color:var(--green-300)}
.hero p.sub{font-size:17px;max-width:68ch;color:#C7DAD1}
.hero .meta{margin-top:26px;display:grid;grid-template-columns:repeat(4,auto);gap:14px 44px;justify-content:start}
.hero .meta div{color:#fff;font-size:14.5px;font-weight:500}
.hero .meta div span{display:block;font-family:var(--ff-mono);color:var(--green-300);font-size:10px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;margin-bottom:5px}
.nav{font-family:var(--ff-mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;line-height:2.2;margin-top:18px}
.nav a{color:var(--green-300);text-decoration:none}
section{padding:36px 0;border-bottom:1px solid var(--line)}
section > .wrap > .eyebrow{color:var(--green-600)}
h2{font-weight:900;font-size:28px;line-height:1.12;margin:10px 0 6px;letter-spacing:-.02em}
.lede{font-size:15px;color:var(--ink-2);margin-bottom:18px;max-width:78ch}
.idx{list-style:none;margin-top:18px;border-top:1px solid var(--line)}
.idx li{display:grid;grid-template-columns:1.6fr 110px 90px 90px 130px;gap:16px;align-items:center;padding:11px 0;border-bottom:1px solid var(--line);font-size:14.5px}
.idx li.h{font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--green-600);font-weight:600;padding:0 0 10px}
.idx li a{color:var(--ink);font-weight:700;text-decoration:none;border-bottom:1px solid var(--green-100)}
.idx li .num{font-variant-numeric:tabular-nums;color:var(--ink-2)}
.idx li .st.built{color:var(--green-600)}
.idx li .st{font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3)}
.gate{background:var(--tint-soft);border:1px solid var(--tint);border-left:4px solid var(--green);border-radius:var(--r);padding:18px 24px;margin-top:18px}
.gate p,.callout p{font-size:14.5px;color:var(--ink-2);margin:0;max-width:none}
.gate p b,.callout p b{color:var(--ink)}
.callout{background:var(--otint);border:1px solid var(--otint-line);border-left:4px solid var(--orange);border-radius:var(--r);padding:16px 22px;margin-top:16px}
/* account block */
.acct{border-top:6px solid var(--forest)}
.acct .head{display:flex;justify-content:space-between;align-items:flex-end;gap:20px;flex-wrap:wrap}
.acct .head .mapname{font-family:var(--ff-mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);font-weight:600}
.acct .head .mapname b{color:var(--forest)}
.stats{display:flex;gap:26px;font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);font-weight:600}
.stats b{display:block;font-family:var(--ff);font-size:24px;font-weight:900;color:var(--forest);letter-spacing:-.01em;line-height:1.1;margin-bottom:4px}
/* org chart, Sales Navigator style: manager above, reports in a row below, connectors */
.org{overflow-x:auto;padding:18px 30px 10px;margin-top:4px}
.org+.org{border-top:1px dashed var(--line);margin-top:10px}
.org ul{display:flex;justify-content:center;list-style:none;margin:0;padding:26px 0 0;position:relative}
.org ul.roots{justify-content:flex-start;padding-top:0;gap:28px}
.org ul.roots > li{padding-top:0}
.org ul.roots > li::before,.org ul.roots > li::after{display:none}
.org li{position:relative;padding:26px 7px 0;display:flex;flex-direction:column;align-items:center}
.org li::before,.org li::after{content:"";position:absolute;top:0;right:50%;width:50%;height:26px;border-top:2px solid var(--line-strong)}
.org li::after{right:auto;left:50%;border-left:2px solid var(--line-strong)}
.org li:only-child::before,.org li:only-child::after{border-top:0}
.org li:only-child::after{border-left:2px solid var(--line-strong)}
.org li:first-child::before,.org li:last-child::after{border-top:0}
.org li:last-child::before{border-right:2px solid var(--line-strong);border-radius:0 6px 0 0}
.org li:first-child::after{border-radius:6px 0 0 0}
.org ul ul::before{content:"";position:absolute;top:0;left:50%;width:0;height:26px;border-left:2px solid var(--line-strong)}
.card{width:186px;background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:9px 11px 8px;box-shadow:var(--shadow);text-align:left}
.card.toplevel{border-color:var(--forest);border-width:2px;background:var(--tint-soft)}
.card .cn{font-weight:700;font-size:13px;color:var(--ink);line-height:1.25}
.card .cn a{color:var(--forest);text-decoration:none}
.card .ct{font-size:11.5px;color:var(--ink-2);line-height:1.3;margin-top:3px}
.card .cm{margin-top:6px;display:flex;gap:5px;flex-wrap:wrap;align-items:center}
.card .lv{font-family:var(--ff-mono);font-size:9px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-3)}
.card .warn,.card .insf{margin-top:0}
/* vertical stack for long rows of direct reports */
.org ul.stack{flex-direction:column;align-items:flex-start;padding:14px 0 0 34px;gap:8px}
.org ul.stack::before{height:calc(100% - 30px);left:16px}
.org ul.stack::after{content:"";position:absolute;top:0;left:16px;width:calc(50% - 16px);height:0;border-top:2px solid var(--line-strong)}
.org ul.stack > li{padding:0 0 0 18px;align-items:flex-start}
.org ul.stack > li::before{top:50%;left:-18px;right:auto;width:18px;height:0;border-top:2px solid var(--line-strong);border-right:0;border-radius:0}
.org ul.stack > li::after{display:none}
.org ul.stack > li:last-child::before{border-right:0;border-radius:0}
/* legacy */
.chart{display:grid;gap:18px;margin-top:22px}
.branch{border:1px solid var(--line);border-radius:var(--r);background:var(--bg);box-shadow:var(--shadow);overflow:hidden}
.root{background:var(--forest);color:#fff;padding:14px 20px;display:flex;justify-content:space-between;align-items:baseline;gap:16px;flex-wrap:wrap}
.root .n{font-weight:900;font-size:18px;letter-spacing:-.01em}
.root .n a{color:#fff;text-decoration:none;border-bottom:1px solid rgba(255,255,255,.35)}
.root .t{color:#C7DAD1;font-size:13.5px}
.root .k{font-family:var(--ff-mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--green-300);font-weight:600}
.groups{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:0}
.group{padding:14px 18px 16px;border-right:1px solid var(--line);border-top:1px solid var(--line)}
.group:last-child{border-right:none}
.group .g{font-family:var(--ff-mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:var(--green-600);font-weight:600;margin-bottom:8px}
.lead .n a{color:inherit;text-decoration:none;border-bottom:1px solid var(--green-100)}
.lead .lv{font-family:var(--ff-mono);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-3);margin-left:6px}
.treewrap{padding:10px 18px 14px}
.tree{list-style:none;margin:0;padding-left:0}
.tree .tree{padding-left:26px;border-left:2px solid var(--green-100);margin-left:9px}
.tree li{margin:0}
.lead{display:flex;flex-wrap:wrap;column-gap:10px;align-items:baseline;padding:7px 0 6px 12px;border-left:2px solid var(--green);margin:6px 0}
.lead.d1{border-left-color:var(--green-600)} .lead.d2{border-left-color:var(--green)} .lead.d3{border-left-color:var(--green-300)}
.lead .n{font-weight:700;color:var(--ink);font-size:14px}
.lead .fn{font-family:var(--ff-mono);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--green-600)}
.lead .t{flex-basis:100%;color:var(--ink-2);font-size:12.5px}
.warn{font-family:var(--ff-mono);font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--orange-600);background:var(--otint);border:1px solid var(--otint-line);border-radius:4px;padding:1px 6px;display:inline-block;margin-top:2px}
.insf{font-family:var(--ff-mono);font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--green-600);background:var(--tint-soft);border:1px solid var(--tint);border-radius:4px;padding:1px 6px;display:inline-block;margin-top:2px}
.active{font-family:var(--ff-mono);font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;color:#fff;background:var(--green-600);border-radius:4px;padding:1px 6px;display:inline-block;margin-top:2px}
.note{font-family:var(--ff-mono);font-size:9.5px;letter-spacing:.04em;color:var(--orange-600);margin-top:4px;line-height:1.3}
.card .ln{font-family:var(--ff-mono);font-size:9px;letter-spacing:.08em;text-transform:uppercase;color:var(--green-600)}
.solo{padding:10px 18px 12px;font-size:12.5px;color:var(--ink-3);font-family:var(--ff-mono);letter-spacing:.06em;text-transform:uppercase}
/* table */
.tablewrap{overflow-x:auto;margin-top:20px}
table{width:100%;border-collapse:collapse;font-size:14px;min-width:760px}
th{font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--green-600);text-align:left;padding:0 14px 9px 0;border-bottom:1px solid var(--line);font-weight:600}
td{padding:9px 14px 9px 0;border-bottom:1px solid var(--line);color:var(--ink-2);vertical-align:top}
tbody tr:nth-child(even){background:var(--zebra)}
td.who{white-space:nowrap;color:var(--ink);font-weight:700}
td.who a{color:inherit;text-decoration:none;border-bottom:1px solid var(--green-100)}
td.b{font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3);white-space:nowrap}
td.clr{white-space:nowrap}
.box{display:inline-block;width:13px;height:13px;border:1.5px solid var(--line-strong);border-radius:3px;vertical-align:-2px;margin-right:5px}
.clr span{font-family:var(--ff-mono);font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3);margin-right:12px}
.top{font-family:var(--ff-mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--green-600);margin-top:14px}
.top a{color:inherit;text-decoration:none}
.foot{padding:26px 0 46px;text-align:center;color:var(--ink-3);font-family:var(--ff-mono);font-size:11px;letter-spacing:.08em;background:var(--bg);text-transform:uppercase}
.foot .logo{height:26px;display:inline-block;margin:0 auto 12px;opacity:.85}
.foot span{display:block;margin-top:4px}
@media(max-width:860px){.hero h1{font-size:30px}.hero .meta{grid-template-columns:1fr 1fr}.idx li{grid-template-columns:1fr 1fr}.groups{grid-template-columns:1fr}.group{border-right:none}}
@media print{body{background:#fff;-webkit-print-color-adjust:exact;print-color-adjust:exact}@page{margin:12mm}.branch,tr,.gate{break-inside:avoid}section.acct{break-before:page}}
"""

BUILT = {"Assurant","Cleveland Clinic","Cox Communications","DIRECTV"}
LV = {"C":"C-level","EVP":"EVP","SVP":"SVP","VP":"VP","AVP":"AVP","Director":"Director"}
def lead_html(r):
    name = f'<a href="{E(r["linkedin_url"])}">{E(r["full_name"])}</a>' if r["linkedin_url"] else E(r["full_name"])
    return f'<div class="lead"><span class="n">{name}</span><span class="lv">{E(LV.get(r["level"], r["level"]))}</span><span class="t">{E(r["title"])}</span></div>'

WARN = '<span class="warn">confirm CRM badge</span>'
INSF = '<span class="insf">in Salesforce</span>'
ACTIVE = '<span class="active">active on LinkedIn</span>'
def tag(r):
    v = r.get("badge_check") or ""
    t = INSF if v.startswith("IN_SF:") else (WARN if v else "")
    if v.startswith("VERIFY:"): t = '<span class="warn">confirm current role</span>'
    return (ACTIVE if (r.get("li_active") or "").lower() == "yes" else "") + t
def warn_div(r):
    v = r.get("badge_check") or ""
    note = ('<div class="note">' + E(r["note"]) + '</div>') if r.get("note") else ""
    if not v: return note
    if v.startswith("VERIFY:"): return '<div class="warn">' + E(v[7:]) + '</div>' + note
    return (('<div class="insf">' + E(v[6:]) + '</div>') if v.startswith("IN_SF:") else ('<div class="warn">' + E(v) + '</div>')) + note

def card(r, top=False):
    name = f'<a href="{E(r["linkedin_url"])}">{E(r["full_name"])}</a>' if r["linkedin_url"] else E(r["full_name"])
    return (f'<div class="card{" toplevel" if top else ""}"><div class="cn">{name}</div><div class="ct">{E(r["title"])}</div>'
            f'<div class="cm"><span class="lv">{E(LV.get(r["level"], r["level"]))}</span><span class="ln">{E(r.get("lane",""))}</span>{tag(r)}</div>'
            f'{("<div class=%snote%s>%s</div>" % (chr(34), chr(34), E(r["note"]))) if r.get("note") else ""}</div>')

def org_ul(rs, parent, depth):
    kids = [r for r in rs if r["reports_up_to"] == parent and int(r["depth"]) == depth]
    if not kids: return ""
    leaves = all(not [x for x in rs if x["reports_up_to"] == k["full_name"]] for k in kids)
    if leaves and len(kids) > 4:   # long row of direct reports: stack them under the manager instead of one very wide row
        return '<ul class="stack">' + "".join(f'<li>{card(k)}</li>' for k in kids) + '</ul>'
    return '<ul>' + "".join(f'<li>{card(k)}{org_ul(rs, k["full_name"], depth + 1)}</li>' for k in kids) + '</ul>'

def account_section(acct, rs):
    tops = [r for r in rs if int(r["depth"]) == 0]
    chart = "".join(f'<div class="org"><ul class="roots"><li>{card(t, True)}{org_ul(rs, t["full_name"], 1)}</li></ul></div>' for t in tops)
    trs = "".join(
        f'<tr><td class="who" style="padding-left:{int(r["depth"])*22}px">{("<a href=%s>%s</a>" % (E(r["linkedin_url"]), E(r["full_name"]))) if r["linkedin_url"] else E(r["full_name"])}</td>'
        f'<td>{E(r["title"])}{warn_div(r)}</td><td class="b">{E(r.get("lane",""))}</td><td class="b">{E(LV.get(r["level"], r["level"]))}</td>'
        f'<td class="b">{"top of the map" if r["reports_up_to"]=="Top of the map" else E(r["reports_up_to"])}</td>'
        f'<td class="b">{("<a href=%s>profile</a>" % E(r["linkedin_url"])) if r["linkedin_url"] else ""}</td></tr>' for r in rs)
    at = acct_type.get(acct, "")
    flag = f'<div class="callout"><p><b>Salesforce lists this account as {E(at)}.</b> Same map; treat it as new logo and start with the senior executives.</p></div>' if at and at.lower() != "customer" else ""
    funcs = sorted({r["function"] for r in rs})
    return f"""<section class="acct" id="{slug(acct)}"><div class="wrap">
<div class="head"><div><div class="eyebrow">Back office map{" &middot; built in Sales Nav" if acct in BUILT else ""}</div><h2>{E(acct)}</h2><div class="mapname">Sales Navigator map name: <b>{E(acct)} - Back Office</b></div></div>
<div class="stats"><div><b>{len(rs)}</b>leads</div><div><b>{len(tops)}</b>top cards</div><div><b>{len(funcs)}</b>functions</div></div></div>
{flag}
</div>
{chart}
<div class="wrap">
<div class="tablewrap"><table><thead><tr><th>Lead (indented by level)</th><th>Title</th><th>Lane</th><th>Level</th><th>Reports up to (inferred)</th><th>LinkedIn</th></tr></thead><tbody>{trs}</tbody></table></div>
<div class="top"><a href="#top">Back to top</a></div>
</div></section>"""

total = len(rows)
BUILT = {"Assurant","Cleveland Clinic","Cox Communications","DIRECTV"}
idx = "".join(f'<li><a href="#{slug(a)}">{E(a)}</a><span class="st">{E(acct_type.get(a) or "not matched")}</span><span class="num">{len(rs)}</span><span class="num">{sum(1 for r in rs if r["reports_up_to"]=="Top of the map")}</span><span class="st{" built" if a in BUILT else ""}">{"built in Sales Nav" if a in BUILT else "to build"}</span></li>' for a, rs in by.items())
nav = " &middot; ".join(f'<a href="#{slug(a)}">{E(a)}</a>' for a in by)
page = f"""<title>Back Office Maps, Inger's Twelve</title>
<style>{fonts}{CSS}</style>
<svg width="0" height="0" style="position:absolute" aria-hidden="true">{logo}</svg>
<div class="sheet">
<header class="hero" id="top"><div class="wrap">
<svg class="logo"><use href="#ilogo"/></svg>
<div class="eyebrow">GTM Engineering &middot; Back office expansion</div>
<h1>Back office maps, <span class="spark">Inger's twelve</span></h1>
<p class="sub">One new Sales Navigator map per account, built top-down and covering the four back-office lanes from the July lists: operations executives, operations leaders, workforce planning and product owners, and operations technology. Nobody here is on the existing Relationship Maps, and every name was checked against all of Salesforce. "In Salesforce" marks a person Intradiem already has a record for but who is not part of the current front-office relationship; they stay on the map because they run the back office. "Confirm CRM badge" marks a common name that exists in Salesforce at another company.</p>
<div class="meta"><div><span>Account manager</span>{E(AM)}</div><div><span>Prepared by</span>Dallas Andrews</div><div><span>Date</span>{DATE}</div><div><span>Leads</span>{total} across 12 maps</div></div>
<div class="nav">{nav}</div>
</div></header>
<section><div class="wrap">
<ul class="idx"><li class="h"><span>Account</span><span>Salesforce</span><span>Leads</span><span>Executives</span><span>Map status</span></li>{idx}</ul>
<div class="gate"><p><b>Build order.</b> Create the map, add the senior executives first, then add each lead under the executive shown. Reporting lines are inferred from titles; adjust in Sales Navigator where the account shows otherwise. Once the twelve maps are built, Inger reviews them and picks the key contacts for outreach.</p></div>
</div></section>
{"".join(account_section(a, rs) for a, rs in by.items())}
<div class="foot"><svg class="logo"><use href="#ilogo"/></svg><span>GTM Engineering &middot; Back office expansion &middot; {DATE}</span><span>Source: BO_Map_Build_Sheets_Inger.csv</span></div>
</div>"""
open(OUT, "w").write(page)
print("written", OUT, total, "leads")
