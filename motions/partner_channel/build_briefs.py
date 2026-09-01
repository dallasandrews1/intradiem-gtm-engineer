#!/usr/bin/env python3
"""Account briefs for the partner channel, two versions per account from one JSON.

Reads briefs/data/<slug>.json and writes briefs/<Slug>_Brief_Internal.src.html and
briefs/<Slug>_Brief_Partner.src.html, then compiles both with the shared template
(../ai_champion_product/_tpl via build_page.py logic). Partner-safe rules are applied in
code, not by hand: no item marked internal_only, no UNVERIFIED or EMPLOYEE SENTIMENT
flag, no dollar figure, no Verint-replacement language (the partner angle is a separate
field), no scenario table. Also builds briefs/Compare_<date>.src.html from
briefs/data/compare.json when present.

Run:  python3 build_briefs.py            (all accounts)
      python3 build_briefs.py ally       (one slug)
"""
import html, json, pathlib, re, sys, datetime

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE / "briefs" / "data"
OUT = HERE / "briefs"
TPL = HERE.parent / "ai_champion_product" / "_tpl"
TODAY = datetime.date.today().isoformat()

fonts = "\n".join(l for l in (TPL / "fonts_head.html").read_text().splitlines() if l.startswith("@font-face"))
base_css = (TPL / "base.css").read_text()
logo = (TPL / "logo_symbol.html").read_text()
present = (TPL / "present.js").read_text()

E = lambda s: html.escape(str(s if s is not None else ""), quote=True)
BAD_FLAGS = {"UNVERIFIED", "EMPLOYEE SENTIMENT"}

HUD = """<div id="hud">
  <div class="brand">Intradiem &middot; Partner channel</div>
  <div class="dots" id="pdots"></div>
  <div class="nav">
    <button class="ab" type="button" id="pprev" aria-label="Previous">&larr;</button>
    <span class="cnt" id="pcount">1 / 5</span>
    <button class="ab" type="button" id="pnext" aria-label="Next">&rarr;</button>
    <button class="esc" type="button" id="pexit">Esc exits</button>
  </div>
</div>"""

CSS = """
.items{list-style:none;margin:10px 0 0;padding:0}
.items li{padding:9px 0;border-top:1px solid var(--line);font-size:14px;line-height:1.5;color:var(--ink-2)}
.items li:first-child{border-top:none;padding-top:2px}
.items li:before,.items li::before{content:none!important;display:none!important}
.items li{padding-left:0!important}
.items li b{color:var(--ink)}
.flag{display:inline-block;font-family:var(--ff-mono);font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;font-weight:600;padding:2px 7px;border-radius:999px;margin-left:6px;vertical-align:1px;border:1px solid var(--line);color:var(--ink-3)}
.flag.est{background:var(--otint);border-color:transparent;color:#B25E12}
.flag.inf{background:var(--tint);border-color:transparent;color:var(--green-600)}
.flag.unv,.flag.sen{background:#F5F4F2}
.src{display:block;margin-top:3px;font-family:var(--ff-mono);font-size:10.5px;color:var(--ink-3);letter-spacing:.02em;word-break:break-all}
.src a{color:var(--green-600);text-decoration:none}
.src a:hover{text-decoration:underline}
.role{font-family:var(--ff-mono);font-size:10px;letter-spacing:.1em;text-transform:uppercase;font-weight:600;color:var(--green-600);white-space:nowrap}
.role.vito{color:#B25E12}
td.nm{white-space:nowrap;font-weight:700;color:var(--ink)}
.ldr th:nth-child(1){width:15%}.ldr th:nth-child(2){width:26%}.ldr th:nth-child(3){width:15%}.ldr th:nth-child(4){width:14%}.ldr th:nth-child(5){width:30%}
.ldr td{vertical-align:top;font-size:13.5px;line-height:1.45}
td.nm a{color:inherit;text-decoration:none;border-bottom:1px solid var(--green-300)}
.fresh{font-family:var(--ff-mono);font-size:10.5px;color:var(--ink-3);white-space:nowrap}
.q{counter-reset:q;list-style:none;padding:0;margin:14px 0 0}
.q li{counter-increment:q;position:relative;padding:12px 0 12px 44px;border-top:1px solid var(--line);font-size:15px;color:var(--ink);line-height:1.5}
.q li:first-child{border-top:none}
.q li:before{content:counter(q);position:absolute;left:0;top:10px;width:28px;height:28px;border-radius:50%;background:var(--forest);color:#fff;font-family:var(--ff-mono);font-size:12px;font-weight:600;display:flex;align-items:center;justify-content:center}
.q small{display:block;color:var(--ink-3);font-size:12.5px;margin-top:3px}
.conf{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}
.conf span{font-family:var(--ff-mono);font-size:11px;padding:5px 10px;border-radius:999px;border:1px solid var(--line);color:var(--ink-2)}
.conf span.h{background:var(--tint);border-color:transparent;color:var(--green-600)}
.conf span.l{background:var(--otint);border-color:transparent;color:#B25E12}
.srcs{columns:2;column-gap:28px;font-size:12.5px;color:var(--ink-3);margin-top:12px}
.srcs div{break-inside:avoid;padding:4px 0;border-top:1px solid var(--line)}
.srcs a{color:var(--green-600);text-decoration:none}
.stamp{display:inline-block;font-family:var(--ff-mono);font-size:10px;letter-spacing:.12em;text-transform:uppercase;font-weight:600;padding:4px 10px;border-radius:4px;background:rgba(255,255,255,.14);color:#fff;margin-bottom:14px}
.stamp.int{background:var(--orange);color:#fff}
.cmp td:first-child{font-weight:700;color:var(--ink);white-space:nowrap}
.cmp td{vertical-align:top;font-size:13.5px}
@media(max-width:900px){.srcs{columns:1}}
"""


def flag_cls(f):
    return {"ESTIMATED": "est", "INFERRED": "inf", "UNVERIFIED": "unv", "EMPLOYEE SENTIMENT": "sen"}.get(f or "", "")


def keep(item, partner):
    if not partner:
        return not item.get("partner_only")
    if item.get("internal_only"):
        return False
    if (item.get("f") or "") in BAD_FLAGS:
        return False
    if any("$" in str(v) for k, v in item.items() if isinstance(v, str) and k not in ("s", "linkedin")):
        return False
    return True


def li(item):
    f = item.get("f")
    src = ""
    if item.get("s"):
        u = item["s"]
        label = re.sub(r"^https?://(www\.)?", "", u)[:70]
        src = f'<span class="src"><a href="{E(u)}" target="_blank" rel="noopener">{E(label)}</a>{(" · " + E(item["d"])) if item.get("d") else ""}</span>'
    elif item.get("d"):
        src = f'<span class="src">{E(item["d"])}</span>'
    fl = f'<span class="flag {flag_cls(f)}">{E(f)}</span>' if f else ""
    return f"<li>{item['t']}{fl}{src}</li>"


def page(d, partner):
    mode = "Partner-safe" if partner else "Internal"
    stamp = ('<span class="stamp">Partner-safe · no estimates, no unverified items</span>' if partner
             else '<span class="stamp int">Internal · not for partner distribution</span>')
    angle = d["angle"]["partner" if partner else "internal"]
    tldr = d["tldr"]["partner" if partner else "internal"]
    stats = [s for s in d.get("stats", []) if keep(s, partner)][:4]
    sections = []
    for sec in d["sections"]:
        items = [i for i in sec["items"] if keep(i, partner)]
        if items:
            sections.append((sec, items))
    leaders = [l for l in d.get("leaders", []) if keep(l, partner)]
    triggers = [t for t in d.get("triggers", []) if keep(t, partner)]
    say = [s for s in d.get("we_can_say", []) if (not partner or s.get("tier") == "1:many")]
    sources = d.get("sources", [])

    h = []
    A = h.append
    A(f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">
<title>{E(d["short"])} account brief ({mode})</title>
<!--FONTS--><style>{CSS}</style></head><body><!--LOGO-->
<button id="presentBtn" type="button" aria-label="Open present mode">Present</button><div id="prog"></div>
<div class="sheet">
<header class="hero"><div class="wrap">
  <svg class="logo"><use href="#ilogo"/></svg>
  <div class="eyebrow" data-h="1">GTM Engineering &middot; Partner channel &middot; Account brief</div>
  <h1 data-h="2">{E(d["account"])}: <span class="spark">{angle}</span></h1>
  <p class="sub" data-h="3">{d["sub"]}</p>
  <div class="hstats" data-h="4">''')
    for s in stats:
        A(f'<div><b>{E(s["n"])}</b><span>{E(s["l"])}</span></div>')
    A('</div><div class="meta" data-h="5">')
    A(f'<div><span>Version</span>{stamp}</div>')
    A(f'<div><span>Partner</span>{E(d["partner_line"])}</div>')
    A(f'<div><span>Basis</span>{E(d["basis"])}</div>')
    A(f'<div><span>By</span>GTM Engineering, {TODAY}</div>')
    A('</div></div></header>')

    A('<section><div class="wrap"><div class="tldr"><div class="k">In one screen</div><ul>')
    for t in tldr:
        A(f"<li>{t}</li>")
    A('</ul></div></div></section>')

    A('<section><div class="wrap"><div class="eyebrow">What we found</div>')
    A(f'<h2>{d["h2_findings"]}</h2><div class="grid">')
    for i, (sec, items) in enumerate(sections):
        A(f'<div class="card rv" style="--i:{i % 3}"><span class="tag">{E(sec["eyebrow"])}</span><h4>{E(sec["title"])}</h4><ul class="items">')
        for it in items:
            A(li(it))
        A('</ul></div>')
    A('</div></div></section>')

    if leaders:
        A('<section><div class="wrap"><div class="eyebrow">Who to talk to</div>')
        A(f'<h2>{d["h2_leaders"]}</h2>')
        A('<div class="tablewrap"><table class="ldr"><thead><tr><th>Name</th><th>Title</th><th>Likely role</th><th>Status</th><th>Why them</th></tr></thead><tbody>')
        for l in leaders:
            nm = f'<a href="{E(l["linkedin"])}" target="_blank" rel="noopener">{E(l["name"])}</a>' if l.get("linkedin") else E(l["name"])
            rc = "vito" if "VITO" in l.get("role", "") else ""
            A(f'<tr class="rv"><td class="nm">{nm}</td><td>{E(l["title"])}</td><td><span class="role {rc}">{E(l["role"])}</span></td><td><span class="fresh">{E(l.get("status",""))}{(" · " + E(l["fresh"])) if l.get("fresh") else ""}</span></td><td>{l.get("note","")}</td></tr>')
        A('</tbody></table></div>')
        A(f'<p style="margin-top:12px;font-size:13px;color:var(--ink-3)">{d["leaders_note"]}</p></div></section>')

    if triggers:
        A('<section><div class="wrap"><div class="eyebrow">Timing</div>')
        A(f'<h2>{d["h2_triggers"]}</h2><ul class="cal">')
        for t in triggers:
            fl = f'<span class="flag {flag_cls(t.get("f"))}">{E(t["f"])}</span>' if t.get("f") else ""
            src = f' <a class="src" style="display:inline" href="{E(t["s"])}" target="_blank" rel="noopener">source</a>' if t.get("s") else ""
            A(f'<li class="rv"><span class="d">{E(t["when"])}</span><span class="e">{t["what"]}{fl}</span><span class="r">{t.get("so","")}{src}</span></li>')
        A('</ul></div></section>')

    if say:
        A('<section><div class="wrap"><div class="eyebrow">What Intradiem can say</div>')
        A(f'<h2>{d["h2_say"]}</h2><div class="gate rv"><ul class="items">')
        for s in say:
            A(f'<li>{s["t"]}<span class="src">{E(s["s"])} · {E(s["tier"])}</span></li>')
        A('</ul></div>')
        if not partner and d.get("scenario_note"):
            A(f'<div class="callout rv"><h4>On the savings table in the 3xG brief</h4><p>{d["scenario_note"]}</p></div>')
        A('</div></section>')

    A('<section><div class="wrap"><div class="eyebrow">First conversation</div>')
    A(f'<h2>{d["h2_questions"]}</h2><ol class="q">')
    for q in d["questions"]:
        A(f'<li>{q["q"]}<small>{q.get("from","")}</small></li>')
    A('</ol></div></section>')

    A('<section><div class="wrap"><div class="eyebrow">Confidence and gaps</div>')
    A(f'<h2>{d["h2_conf"]}</h2><div class="conf">')
    for c in d["confidence"]:
        cls = {"High": "h", "Low": "l"}.get(c["level"], "")
        A(f'<span class="{cls}">{E(c["section"])}: {E(c["level"])}</span>')
    A('</div><div class="callout rv" style="margin-top:16px"><h4>Still to get</h4><ul class="items">')
    for g in d["gaps"]:
        if partner and g.get("internal_only"):
            continue
        A(f'<li>{g["t"]}</li>')
    A('</ul></div>')
    if sources:
        A('<h4 style="margin-top:22px">Sources</h4><div class="srcs">')
        for s in sources:
            A(f'<div><a href="{E(s["u"])}" target="_blank" rel="noopener">{E(s["t"])}</a>{(" · " + E(s["d"])) if s.get("d") else ""}</div>')
        A('</div>')
    A('</div></section>')

    A(f'<footer class="foot"><svg class="logo"><use href="#ilogo"/></svg><span>{"Partner-safe" if partner else "Internal"} &middot; GTM Engineering &middot; Partner channel</span><span>{E(d["short"])} brief &middot; {TODAY}</span></footer></div>')

    # deck
    A('<div id="deck" aria-label="Presentation">')
    A(f'<section class="pslide" data-title="Title"><svg class="logo" style="height:40px;color:#fff;margin-bottom:26px" data-a="1"><use href="#ilogo"/></svg><div class="pe" data-a="2">Account brief &middot; {mode}</div><h1 data-a="3">{E(d["account"])}: <span class="spark">{angle}</span></h1><p class="pl" data-a="4">{d["sub"]}</p></section>')
    if stats:
        A('<section class="pslide" data-title="Footprint"><div class="pe" data-a="1">Footprint</div>')
        A(f'<h2 data-a="2">{d["deck"]["footprint"]}</h2><div class="pgrid c3" data-a="3">')
        for s in stats[:3]:
            A(f'<div><i class="big">{E(s["n"])}</i><b>{E(s["l"])}</b></div>')
        A('</div></section>')
    if leaders:
        A('<section class="pslide" data-title="People"><div class="pe" data-a="1">Who to talk to</div>')
        A(f'<h2 data-a="2">{d["deck"]["people"]}</h2><ul class="plist" data-a="3">')
        for l in leaders[:5]:
            A(f'<li><span class="d">{E(l["role"].split(" (")[0])}</span><span><b>{E(l["name"])}</b>, {E(l["title"])}</span></li>')
        A('</ul></section>')
    if triggers:
        A('<section class="pslide" data-title="Timing"><div class="pe" data-a="1">Timing</div>')
        A(f'<h2 data-a="2">{d["deck"]["timing"]}</h2><ul class="plist" data-a="3">')
        for t in triggers[:4]:
            A(f'<li><span class="d">{E(t["when"])}</span><span>{t["what"]}</span></li>')
        A('</ul></section>')
    A('<section class="pslide" data-title="Questions"><div class="pe" data-a="1">First conversation</div>')
    A(f'<h2 data-a="2">{d["deck"]["questions"]}</h2><ul class="plist" data-a="3">')
    for q in d["questions"][:4]:
        A(f'<li><span class="d">Ask</span><span>{q["q"]}</span></li>')
    A('</ul></section></div>')
    A(HUD)
    A('<!--PRESENT--></body></html>')
    return "\n".join(h)


def compile_(src_html: str) -> str:
    out = src_html.replace("<!--FONTS-->", "<style>\n" + fonts + "\n" + base_css + "</style>")
    out = out.replace("<!--LOGO-->", logo).replace("<!--PRESENT-->", "<script>\n" + present + "</script>")
    return out


def check(t: str, name: str):
    body = re.sub(r"data:font/woff2;base64,[A-Za-z0-9+/=]+", "", t)
    probs = []
    if "—" in body: probs.append("em dash")
    for ph in ("<!--FONTS-->", "<!--LOGO-->", "<!--PRESENT-->"):
        if ph in t: probs.append("placeholder " + ph)
    if 'id="ilogo"' not in t: probs.append("no logo")
    if "Partner" in name and re.search(r"\$\s?\d", body): probs.append("dollar figure in partner-safe page")
    if "Partner" in name and re.search(r"replac\w+ (passive )?Verint|instead of Verint|rip and replace", body, re.I): probs.append("Verint-replacement language in partner-safe page")
    if "Partner" in name and re.search(r"UNVERIFIED|EMPLOYEE SENTIMENT", body): probs.append("unverified flag in partner-safe page")
    return probs


def build_compare():
    f = DATA / "compare.json"
    if not f.exists():
        return
    c = json.loads(f.read_text())
    h = [f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex">
<title>{E(c["title"])}</title><!--FONTS--><style>{CSS}</style></head><body><!--LOGO-->
<button id="presentBtn" type="button" aria-label="Open present mode">Present</button><div id="prog"></div>
<div class="sheet"><header class="hero"><div class="wrap"><svg class="logo"><use href="#ilogo"/></svg>
<div class="eyebrow">GTM Engineering &middot; Partner channel &middot; Side by side</div>
<h1>{c["h1"]}</h1><p class="sub">{c["sub"]}</p><div class="hstats">''']
    for s in c["stats"]:
        h.append(f'<div><b>{E(s["n"])}</b><span>{E(s["l"])}</span></div>')
    h.append('</div></div></header>')
    h.append(f'<section><div class="wrap"><div class="tldr"><div class="k">In one screen</div><ul>' + "".join(f"<li>{t}</li>" for t in c["tldr"]) + '</ul></div></div></section>')
    h.append(f'<section><div class="wrap"><div class="eyebrow">Same two accounts, same day</div><h2>{c["h2"]}</h2><div class="tablewrap"><table class="cmp"><thead><tr><th>Aspect</th><th>3xG brief (Gemini deep research, Aug 31)</th><th>Engine brief (Sep 1)</th></tr></thead><tbody>')
    for r in c["rows"]:
        h.append(f'<tr class="rv"><td>{E(r["a"])}</td><td>{r["j"]}</td><td>{r["e"]}</td></tr>')
    h.append('</tbody></table></div></div></section>')
    h.append(f'<section><div class="wrap"><div class="eyebrow">What changes for Frank</div><h2>{c["h2_next"]}</h2><div class="grid">')
    for i, card in enumerate(c["cards"]):
        h.append(f'<div class="card rv" style="--i:{i}"><span class="tag {card.get("tag_cls","")}">{E(card["tag"])}</span><h4>{E(card["title"])}</h4><p>{card["p"]}</p></div>')
    h.append('</div></div></section>')
    h.append(f'<footer class="foot"><svg class="logo"><use href="#ilogo"/></svg><span>Internal &middot; GTM Engineering &middot; Partner channel</span><span>{TODAY}</span></footer></div>')
    h.append('<div id="deck" aria-label="Presentation">')
    h.append(f'<section class="pslide" data-title="Title"><svg class="logo" style="height:40px;color:#fff;margin-bottom:26px" data-a="1"><use href="#ilogo"/></svg><div class="pe" data-a="2">Partner channel &middot; Side by side</div><h1 data-a="3">{c["h1"]}</h1><p class="pl" data-a="4">{c["sub"]}</p></section>')
    h.append('<section class="pslide" data-title="Numbers"><div class="pe" data-a="1">Same two accounts, same day</div><h2 data-a="2">What the engine run cost and returned.</h2><div class="pgrid c3" data-a="3">')
    for s_ in c["stats"][:3]:
        h.append(f'<div><i class="big">{E(s_["n"])}</i><b>{E(s_["l"])}</b></div>')
    h.append('</div></section>')
    h.append('<section class="pslide" data-title="Next"><div class="pe" data-a="1">What changes</div><h2 data-a="2">' + c["h2_next"] + '</h2><ul class="plist" data-a="3">')
    for card in c["cards"]:
        h.append(f'<li><span class="d">{E(card["tag"])}</span><span><b>{E(card["title"])}.</b> {card["p"]}</span></li>')
    h.append('</ul></section></div>')
    h.append(HUD)
    h.append('<!--PRESENT--></body></html>')
    src = "\n".join(h)
    (OUT / f"Compare_Briefs_{TODAY}.src.html").write_text(src)
    out = OUT / f"Compare_Briefs_{TODAY}.html"
    out.write_text(compile_(src))
    print(f"{out.name}: {out.stat().st_size:,} bytes", check(out.read_text(), out.name) or "")


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    ok = True
    for f in sorted(DATA.glob("*.json")):
        if f.name == "compare.json" or (only and f.stem != only):
            continue
        d = json.loads(f.read_text())
        for partner in (False, True):
            name = f'{d["short"]}_Brief_{"Partner" if partner else "Internal"}'
            src = page(d, partner)
            (OUT / f"{name}.src.html").write_text(src)
            out = OUT / f"{name}.html"
            out.write_text(compile_(src))
            probs = check(out.read_text(), name)
            ok = ok and not probs
            print(f"{out.name}: {out.stat().st_size:,} bytes", probs or "")
    build_compare()
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
