#!/usr/bin/env python3
"""One rep set's back-office maps, one page. Reads the set's build sheet (--set <name>, sets/<name>.json).
First screen: headline, one line, four numbers. Then twelve account cards: senior executives, a top-down tree
drawn on scroll, full names under a toggle. No asks, no internal vocabulary."""
import csv, html, os, re
from collections import OrderedDict
from bo_set import load_set
HERE = os.path.dirname(os.path.abspath(__file__))
CFG = load_set(); P = CFG["_paths"]
OUT = P["page_out"]
DATE = CFG["date"]; AM = CFG["rep"]; REP_LABEL = CFG.get("rep_label", "Account manager")
E = lambda s: html.escape(s or "")
fonts = open(os.path.join(HERE, "_fonts_embed.css")).read()
logo = open(os.path.join(HERE, "_logo_symbol.svg")).read()
slug = lambda a: re.sub(r"[^a-z0-9]+", "_", a.lower()).strip("_")
BUILT = set(CFG.get("built", []))
LV = {"C": "C-level", "EVP": "EVP", "SVP": "SVP", "VP": "VP", "AVP": "AVP", "Director": "Director"}
FUNC = {"Operations": "Operations", "Finance & shared services": "Finance and shared services", "Claims": "Claims",
        "Administration & supply chain": "Administration and supply chain", "Billing, payments & revenue": "Billing, payments and revenue",
        "Fraud, credit & disputes": "Fraud, credit and disputes", "Underwriting operations": "Underwriting operations"}
FUNC.update({lbl: lbl.replace(" & ", " and ") for lbl, _ in CFG.get("func_extra", [])})

rows = list(csv.DictReader(open(P["build_sheets_csv"])))
by = OrderedDict()
GROUP = "map_name" if CFG.get("group_by") == "map_name" else "account"   # a page of several maps for one account groups by map name
for r in rows: by.setdefault(r[GROUP], []).append(r)
acct_type = {}
p = P["known_companies"]
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
body{font-family:var(--ff);background:var(--bg);color:var(--ink);line-height:1.6;-webkit-font-smoothing:antialiased}
.sheet{max-width:none;margin:0;background:var(--bg)}
.wrap{max-width:none;margin:0;padding:0 40px}
.eyebrow{font-family:var(--ff-mono);text-transform:uppercase;letter-spacing:.16em;font-size:11px;font-weight:600}
.logo{height:26px;width:auto;display:block;color:#014637}
a{color:var(--green-600)}
/* hero */
.hero{background:var(--forest);color:#fff;padding:44px 0 36px;position:relative;overflow:hidden}
.hero::after{content:"";position:absolute;right:-160px;top:-120px;width:440px;height:440px;border-radius:50%;background:radial-gradient(circle,rgba(45,181,110,.30),transparent 62%)}
.hero .wrap{position:relative;z-index:1}
.hero .logo{height:46px;margin-bottom:24px;color:#fff}
.hero .eyebrow{color:var(--green-300)}
.hero h1{font-weight:900;font-size:40px;line-height:1.06;margin:14px 0 12px;letter-spacing:-.02em;max-width:24ch;text-wrap:balance}
.hero h1 .spark{color:var(--green-300)}
.hero p.sub{font-size:16.5px;max-width:64ch;color:#C7DAD1}
.hero h1{max-width:none}
.hstats{display:grid;grid-template-columns:repeat(4,auto);gap:14px 48px;justify-content:start;margin-top:24px}
.hstats div b{display:block;font-weight:900;font-size:34px;color:var(--green-300);letter-spacing:-.02em;line-height:1;font-variant-numeric:tabular-nums}
.hstats div > span{display:block;font-family:var(--ff-mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:#9DBBAE;font-weight:600;margin-top:7px}
.hero .meta{margin-top:26px;display:grid;grid-template-columns:repeat(3,auto);gap:14px 44px;justify-content:start}
.hero .meta div{color:#fff;font-size:14.5px;font-weight:500}
.hero .meta div span{display:block;font-family:var(--ff-mono);color:var(--green-300);font-size:10px;letter-spacing:.14em;text-transform:uppercase;font-weight:600;margin-bottom:5px}
.nav{margin-top:22px;display:flex;flex-wrap:wrap;gap:8px}
.nav a{font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;font-weight:600;color:#DDE9E3;text-decoration:none;border:1px solid rgba(255,255,255,.22);border-radius:100px;padding:6px 12px}
.nav a.b{border-color:rgba(123,211,160,.7);color:#C4ECD4}
.hero [data-h]{opacity:0;transform:translateY(14px);transition:opacity .7s ease,transform .7s ease}
.hero [data-h="1"]{transition-delay:.05s}.hero [data-h="2"]{transition-delay:.2s}.hero [data-h="3"]{transition-delay:.4s}.hero [data-h="4"]{transition-delay:.6s}.hero [data-h="5"]{transition-delay:.8s}
.hero.on [data-h]{opacity:1;transform:none}
/* legend */
.legend{padding:18px 0;border-bottom:1px solid var(--line);font-size:14px;color:var(--ink-2)}
.legend b{color:var(--ink)}
/* account block */
section.acct{padding:40px 0 34px;border-bottom:1px solid var(--line)}
.acct .head{display:flex;justify-content:space-between;align-items:flex-end;gap:20px;flex-wrap:wrap}
.acct h2{font-weight:900;font-size:30px;line-height:1.1;letter-spacing:-.02em;margin:0 0 4px}
.acct .mapname{font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);font-weight:600}
.acct .mapname b{color:var(--forest)}
.pill{display:inline-block;font-family:var(--ff-mono);font-size:10px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;padding:4px 10px;border-radius:6px;white-space:nowrap;margin-left:10px;vertical-align:middle}
.pill.go{background:var(--tint);color:var(--green-600)}
.pill.now{background:#fff;color:var(--green-600);border:1px solid var(--green)}
.pill.sf{background:var(--zebra);color:var(--ink-3);border:1px solid var(--line)}
.stats{display:flex;gap:26px;font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);font-weight:600}
.stats b{display:block;font-family:var(--ff);font-size:24px;font-weight:900;color:var(--forest);letter-spacing:-.01em;line-height:1.1;margin-bottom:4px}
.execs{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px;margin-top:20px}
.exec{background:var(--forest);color:#fff;border-radius:var(--r);padding:16px 18px;position:relative;overflow:hidden}
.exec::after{content:"";position:absolute;right:-90px;top:-90px;width:220px;height:220px;border-radius:50%;background:radial-gradient(circle,rgba(45,181,110,.28),transparent 62%)}
.exec > *{position:relative;z-index:1}
.exec .k{font-family:var(--ff-mono);font-size:9.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--green-300);font-weight:600;margin-bottom:6px}
.exec .n{font-weight:900;font-size:17px;letter-spacing:-.01em;line-height:1.2}
.exec .n a{color:#fff;text-decoration:none}
.exec .t{color:#C7DAD1;font-size:13px;margin-top:4px;line-height:1.35}
.exec .r{font-family:var(--ff-mono);font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;color:#9DBBAE;margin-top:8px}
/* tree */
.org{overflow-x:auto;padding:18px 40px 6px;margin-top:6px}
.org+.org{border-top:1px dashed var(--line);margin-top:10px}
.org ul{display:flex;justify-content:center;list-style:none;margin:0;padding:26px 0 0;position:relative}
.org ul.roots{justify-content:flex-start;padding-top:0;gap:28px}
.org ul.roots > li{padding-top:0}
.org ul.roots > li::before,.org ul.roots > li::after{display:none}
.org li{position:relative;padding:26px 5px 0;display:flex;flex-direction:column;align-items:center}
.org li::before,.org li::after{content:"";position:absolute;top:0;right:50%;width:50%;height:26px;border-top:2px solid var(--line-strong)}
.org li::after{right:auto;left:50%;border-left:2px solid var(--line-strong)}
.org li:only-child::before,.org li:only-child::after{border-top:0}
.org li:only-child::after{border-left:2px solid var(--line-strong)}
.org li:first-child::before,.org li:last-child::after{border-top:0}
.org li:last-child::before{border-right:2px solid var(--line-strong);border-radius:0 6px 0 0}
.org li:first-child::after{border-radius:6px 0 0 0}
.org ul ul::before{content:"";position:absolute;top:0;left:50%;width:0;height:26px;border-left:2px solid var(--line-strong)}
.card{width:172px;background:var(--bg);border:1px solid var(--line);border-radius:6px;padding:9px 11px 8px;box-shadow:var(--shadow);text-align:left}
.card.toplevel{border-color:var(--forest);border-width:2px;background:var(--tint-soft)}
.card .cn{font-weight:700;font-size:13px;color:var(--ink);line-height:1.25}
.card .cn a{color:var(--forest);text-decoration:none}
.card .ct{font-size:11.5px;color:var(--ink-2);line-height:1.3;margin-top:3px}
.card .cm{margin-top:6px;display:flex;gap:5px;flex-wrap:wrap;align-items:center}
.card .fn{font-family:var(--ff-mono);font-size:9px;letter-spacing:.08em;text-transform:uppercase;color:var(--green-600)}
.org ul.stack{flex-direction:column;align-items:flex-start;padding:14px 0 0 34px;gap:8px}
.org ul.stack::before{height:calc(100% - 30px);left:16px}
.org ul.stack::after{content:"";position:absolute;top:0;left:16px;width:calc(50% - 16px);height:0;border-top:2px solid var(--line-strong)}
.org ul.stack > li{padding:0 0 0 18px;align-items:flex-start}
.org ul.stack > li::before{top:50%;left:-18px;right:auto;width:18px;height:0;border-top:2px solid var(--line-strong);border-right:0;border-radius:0}
.org ul.stack > li::after{display:none}
.org ul.stack > li:last-child::before{border-right:0;border-radius:0}
/* reveal: cards fade in top-down as the account scrolls into view */
.org .card{opacity:0;transform:translateY(10px);transition:opacity .5s ease,transform .5s ease;transition-delay:calc(var(--i,0)*.06s)}
.org.in .card{opacity:1;transform:none}
.execs .exec{opacity:0;transform:translateY(12px);transition:opacity .6s ease,transform .6s ease;transition-delay:calc(var(--i,0)*.1s)}
.execs.in .exec{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){.org .card,.execs .exec,.hero [data-h]{opacity:1;transform:none;transition:none}}
/* badges */
.insf,.warn,.active{font-family:var(--ff-mono);font-size:9px;letter-spacing:.08em;text-transform:uppercase;border-radius:4px;padding:1px 6px;display:inline-block}
.insf{color:var(--green-600);background:var(--tint-soft);border:1px solid var(--tint)}
.warn{color:var(--orange-600);background:var(--otint);border:1px solid var(--otint-line)}
.active{color:#fff;background:var(--green-600)}
/* show all */
details.all{margin:18px 40px 0}
details.all summary{cursor:pointer;list-style:none;font-family:var(--ff-mono);font-size:11px;letter-spacing:.1em;text-transform:uppercase;font-weight:600;color:var(--green-600);padding:10px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line)}
details.all summary::-webkit-details-marker{display:none}
details.all summary::before{content:"+";display:inline-block;width:18px;font-weight:700}
details.all[open] summary::before{content:"\\2013"}
.tablewrap{overflow-x:auto;margin-top:6px}
table{width:100%;border-collapse:collapse;font-size:13.5px;min-width:700px}
th{font-family:var(--ff-mono);font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:var(--green-600);text-align:left;padding:8px 14px 8px 0;border-bottom:1px solid var(--line);font-weight:600}
td{padding:8px 14px 8px 0;border-bottom:1px solid var(--line);color:var(--ink-2);vertical-align:top}
tbody tr:nth-child(even){background:var(--zebra)}
td.who{white-space:nowrap;color:var(--ink);font-weight:700}
td.who a{color:inherit;text-decoration:none;border-bottom:1px solid var(--green-100)}
td.b{font-family:var(--ff-mono);font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3);white-space:nowrap}
.top{font-family:var(--ff-mono);font-size:11px;letter-spacing:.06em;text-transform:uppercase;color:var(--green-600);margin-top:16px}
.top a{color:inherit;text-decoration:none}
.foot{padding:26px 0 46px;text-align:center;color:var(--ink-3);font-family:var(--ff-mono);font-size:11px;letter-spacing:.08em;background:var(--bg);text-transform:uppercase}
.foot .logo{height:26px;display:inline-block;margin:0 auto 12px;opacity:.85}
.foot span{display:block;margin-top:4px}
@media(max-width:860px){.hero h1{font-size:30px}.hstats{grid-template-columns:1fr 1fr}.hero .meta{grid-template-columns:1fr 1fr}.execs{grid-template-columns:1fr}}
@media print{body{background:#fff;-webkit-print-color-adjust:exact;print-color-adjust:exact}@page{margin:12mm}.org .card,.execs .exec{opacity:1;transform:none}section.acct{break-before:page}details.all{display:none}}
"""

def badge(r):
    v = r.get("badge_check") or ""
    out = '<span class="active">active on LinkedIn</span>' if (r.get("li_active") or "").lower() == "yes" else ""
    if v.startswith("IN_SF:"): out += '<span class="insf">in Salesforce</span>'
    elif v.startswith("VERIFY:") and "headline still reads" in v: out += f'<span class="warn" title="{E(v[7:])}">LinkedIn profile out of date</span>'
    elif v.startswith("VERIFY:"): out += '<span class="warn">confirm current role</span>'
    elif v: out += '<span class="warn">same name elsewhere in Salesforce</span>'
    return out

def name_link(r, cls=""):
    return f'<a href="{E(r["linkedin_url"])}" target="_blank" rel="noopener">{E(r["full_name"])}</a>' if r["linkedin_url"] else E(r["full_name"])

counter = {"i": 0}
def card(r, top=False):
    counter["i"] += 1
    return (f'<div class="card{" toplevel" if top else ""}" style="--i:{counter["i"]}"><div class="cn">{name_link(r)}</div><div class="ct">{E(r["title"])}</div>'
            f'<div class="cm"><span class="fn">{E(FUNC.get(r["function"], r["function"]))}</span>{badge(r)}</div></div>')

def org_ul(rs, parent, depth):
    kids = [r for r in rs if r["reports_up_to"] == parent and int(r["depth"]) == depth]
    if not kids: return ""
    leaves = all(not [x for x in rs if x["reports_up_to"] == k["full_name"]] for k in kids)
    if leaves and len(kids) > 4:
        return '<ul class="stack">' + "".join(f'<li>{card(k)}</li>' for k in kids) + '</ul>'
    return '<ul>' + "".join(f'<li>{card(k)}{org_ul(rs, k["full_name"], depth + 1)}</li>' for k in kids) + '</ul>'

TRIMS = {}
for a, n, why in CFG.get("trim", []):
    TRIMS.setdefault(a, []).append((n, why))
TRIM_TITLES = {}
try:
    for r in csv.DictReader(open(P["candidates"])):
        TRIM_TITLES[(r["account"], r["full_name"])] = r["title"]
except Exception: pass

def account_section(acct, rs):
    counter["i"] = 0
    tops = [r for r in rs if int(r["depth"]) == 0]
    execs = "".join(f'<div class="exec" style="--i:{i}"><div class="k">{E(LV.get(t["level"], t["level"]))} &middot; {E(FUNC.get(t["function"], t["function"]))}</div><div class="n">{name_link(t)}</div><div class="t">{E(t["title"])}</div>'
                    f'<div class="r">{sum(1 for r in rs if r["executive"] == t["full_name"]) - 1} people under them{(" &middot; in Salesforce" if (t.get("badge_check") or "").startswith("IN_SF:") else "")}</div></div>' for i, t in enumerate(tops))
    chart = "".join(f'<div class="org"><ul class="roots"><li>{card(t, True)}{org_ul(rs, t["full_name"], 1)}</li></ul></div>' for t in tops)
    trs = "".join(
        f'<tr><td class="who" style="padding-left:{int(r["depth"])*18}px">{name_link(r)}</td><td>{E(r["title"])}</td>'
        f'<td class="b">{E(FUNC.get(r["function"], r["function"]))}</td><td class="b">{E(LV.get(r["level"], r["level"]))}</td>'
        f'<td class="b">{"top of the map" if r["reports_up_to"]=="Top of the map" else E(r["reports_up_to"])}</td><td>{badge(r)}</td></tr>' for r in rs)
    at = acct_type.get(acct, "")
    built = acct in BUILT
    status = '<span class="pill go">Built in Sales Navigator</span>' if built else '<span class="pill now">Ready to build</span>'
    sfp = f'<span class="pill sf">{E(at)} in Salesforce</span>' if at and at.lower() != "customer" else ""
    return f"""<section class="acct" id="{slug(acct)}"><div class="wrap">
<div class="head"><div><h2>{E(acct)}{status}{sfp}</h2><div class="mapname">In Sales Navigator: <b>{E(acct if GROUP == "map_name" else acct + " - " + CFG.get("map_suffix","Back Office"))}</b></div></div>
<div class="stats"><div><b>{len(rs)}</b>people</div><div><b>{len(tops)}</b>senior executives</div></div></div>
<div class="execs">{execs}</div>{(chr(10) + '<p class="note">' + E(CFG.get("account_notes", {}).get(acct, "")) + '</p>') if CFG.get("account_notes", {}).get(acct) else ''}
</div>
{chart}
<details class="all"><summary>Show all {len(rs)}</summary>
<div class="tablewrap"><table><thead><tr><th>Name</th><th>Title</th><th>Function</th><th>Level</th><th>Reports up to</th><th></th></tr></thead><tbody>{trs}</tbody></table></div>
</details>{removed_block(acct)}
<div class="wrap"><div class="top"><a href="#top">Back to top</a></div></div></section>"""

def removed_block(acct):
    t = TRIMS.get(acct, [])
    if not t: return ""
    lis = "".join(f'<tr><td class="who">{E(n)}</td><td>{E(TRIM_TITLES.get((acct, n), ""))}</td><td>{E(why)}</td></tr>' for n, why in t)
    return (f'<details class="all"><summary>Removed in review ({len(t)}) — take these OFF the Sales Navigator map if already placed</summary>'
            f'<div class="tablewrap"><table><thead><tr><th>Name</th><th>Title</th><th>Why removed</th></tr></thead><tbody>{lis}</tbody></table></div></details>')

total = len(rows); built_n = len(BUILT); todo_n = len(by) - built_n; execs_n = sum(1 for r in rows if int(r["depth"]) == 0)
nav = "".join(f'<a class="b" href="#{slug(a)}">{E(a)}</a>' for a in by)
JS = """
<script>
(function(){
  var hero=document.querySelector('.hero'); if(hero){ setTimeout(function(){hero.classList.add('on');},80); }
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  setTimeout(function(){ [].forEach.call(document.querySelectorAll('.hero .hc[data-to]'),function(el){ var to=+el.getAttribute('data-to'); if(reduce){el.textContent=to;return;} var start=Date.now(); var iv=setInterval(function(){ var p=Math.min(1,(Date.now()-start)/1000); el.textContent=Math.round((1-Math.pow(1-p,3))*to); if(p>=1)clearInterval(iv); },24); }); },600);
  var targets=[].slice.call(document.querySelectorAll('.org,.execs'));
  if(!('IntersectionObserver' in window)){targets.forEach(function(el){el.classList.add('in');});return;}
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},{threshold:.08,rootMargin:'0px 0px -5% 0px'});
  targets.forEach(function(el){io.observe(el);});
  function park(){ [].forEach.call(document.querySelectorAll('.org'),function(org){ var top=org.querySelector('.card.toplevel'); if(!top)return; var want=top.offsetLeft-40; if(want>0) org.scrollLeft=want; }); }
  park(); window.addEventListener('load',park); window.addEventListener('resize',park);
})();
</script>"""
SIB = CFG.get("sibling_links") or []
sib = ('<div class="sib" data-h="5"><span>%s</span>%s</div>' % (E(CFG.get("sibling_label","Also for you")), "".join(f'<a href="{E(h)}">{E(t)}</a>' for t, h in SIB))) if SIB else ""
SIB_CSS = '.sib{margin-top:20px;display:flex;flex-wrap:wrap;gap:10px;align-items:center}\n.sib span{font-family:var(--ff-mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;color:#9DBBAE;font-weight:600}\n.sib a{font-size:13.5px;font-weight:500;color:#C4ECD4;text-decoration:none;border-bottom:1px solid rgba(123,211,160,.45);padding-bottom:1px}\n.sib a:hover{color:#fff;border-color:#fff}\n' if SIB else ""
NOTE_CSS = ".note{margin:16px 0 0;font-size:14px;color:var(--ink-2);max-width:90ch;border-left:3px solid var(--orange);padding-left:12px}" if CFG.get("account_notes") else ""
page = f"""<title>{CFG["title"]}</title>
<style>{fonts}{CSS}{SIB_CSS}{NOTE_CSS}</style>
<svg width="0" height="0" style="position:absolute" aria-hidden="true">{logo}</svg>
<div class="sheet">
<header class="hero" id="top"><div class="wrap">
<svg class="logo"><use href="#ilogo"/></svg>
<div class="eyebrow" data-h="1">{E(CFG.get("eyebrow","GTM Engineering · Back office expansion")).replace("·","&middot;")}</div>
<h1 data-h="2">{CFG["headline_html"]}</h1>
<p class="sub" data-h="3">{E(CFG["sub"])}</p>
<div class="hstats" data-h="4"><div><b class="hc" data-to="{len(by)}">0</b><span>accounts</span></div><div><b class="hc" data-to="{total}">0</b><span>people</span></div><div><b class="hc" data-to="{execs_n}">0</b><span>senior executives</span></div><div><b class="hc" data-to="{built_n if built_n else todo_n}">0</b><span>{"maps built in Sales Navigator" if built_n else "maps ready to build"}</span></div></div>
<div class="meta" data-h="5"><div><span>{E(REP_LABEL)}</span>{E(AM)}</div><div><span>Prepared by</span>Dallas Andrews</div><div><span>Date</span>{DATE}</div></div>
{sib}<div class="nav" data-h="5">{nav}</div>
</div></header>
<div class="legend"><div class="wrap">{CFG.get("legend_html", '<b>In Salesforce:</b> Intradiem already has a record for this person; they stay on the map because they run the back office. <b>Same name elsewhere in Salesforce:</b> a record with this name exists at another company.')}</div></div>
{"".join(account_section(a, rs) for a, rs in by.items())}
<div class="foot"><svg class="logo"><use href="#ilogo"/></svg><span>{E(CFG.get("eyebrow","GTM Engineering · Back office expansion")).replace("·","&middot;")} &middot; {DATE}</span></div>
</div>
{JS}"""
open(OUT, "w").write(page)
print("written", OUT, total, "people", len(by), "accounts", built_n, "built")
