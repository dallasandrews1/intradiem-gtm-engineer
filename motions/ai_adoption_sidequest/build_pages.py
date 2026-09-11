#!/usr/bin/env python3
"""Assemble the side-quest pages from their .src.html files on the shared page system.

Placeholders: <!--FONTS--> <!--LOGO--> <!--PRESENT--> (from ../ai_champion_product/_tpl) and
<!--STATE--> (adoption_engine/data/adoption_state.json, inlined as JSON).
Run:  python3 build_pages.py          python3 build_pages.py --check
"""
import pathlib, re, sys, json

HERE = pathlib.Path(__file__).resolve().parent
TPL = HERE.parent / "ai_champion_product" / "_tpl"
STATE = HERE / "adoption_engine" / "data" / "adoption_state.json"

fonts = "\n".join(l for l in (TPL / "fonts_head.html").read_text().splitlines() if l.startswith("@font-face"))
base_css = (TPL / "base.css").read_text()
logo = (TPL / "logo_symbol.html").read_text()
present = (TPL / "present.js").read_text()
state = json.dumps(json.load(open(STATE)), separators=(",", ":")).replace("</", "<\\/")

def build(src):
    html = src.read_text()
    html = html.replace("<!--FONTS-->", "<style>\n" + fonts + "\n" + base_css + "</style>")
    html = html.replace("<!--LOGO-->", logo)
    html = html.replace("<!--PRESENT-->", "<script>\n" + present + "</script>")
    html = html.replace("<!--STATE-->", state)
    out = src.with_name(src.name.replace(".src.html", ".html"))
    out.write_text(html)
    return out

def check(out):
    t = out.read_text(); problems = []
    body = re.sub(r"data:font/woff2;base64,[A-Za-z0-9+/=]+", "", t)
    if "—" in body: problems.append("em dash present")
    for ph in ("<!--FONTS-->", "<!--LOGO-->", "<!--PRESENT-->", "<!--STATE-->"):
        if ph in t: problems.append(f"placeholder left: {ph}")
    if "<!doctype" not in t.lower(): problems.append("missing doctype")
    return problems

if __name__ == "__main__":
    ok = True
    for src in sorted(HERE.glob("*.src.html")):
        out = build(src); probs = check(out) if "--check" in sys.argv else []
        print(f"{out.name}: {out.stat().st_size:,} bytes" + (f"  PROBLEMS: {probs}" if probs else ""))
        ok = ok and not probs
    sys.exit(0 if ok else 1)
