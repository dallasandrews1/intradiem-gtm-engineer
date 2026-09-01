#!/usr/bin/env python3
"""Assemble the partner channel pages from their .src.html files.

Reuses the shared page system in ../ai_champion_product/_tpl (fonts, base.css,
logo symbol, present-mode script) so the page reads as one product with the
operating map and the Product pages.

Run:  python3 build_page.py            (writes X.html next to X.src.html)
      python3 build_page.py --check    (also greps outputs for em dashes and stray placeholders)
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
TPL = HERE.parent / "ai_champion_product" / "_tpl"

fonts_lines = (TPL / "fonts_head.html").read_text().splitlines()
fonts = "\n".join(l for l in fonts_lines if l.startswith("@font-face"))
base_css = (TPL / "base.css").read_text()
logo = (TPL / "logo_symbol.html").read_text()
present = (TPL / "present.js").read_text()


def build(src: pathlib.Path) -> pathlib.Path:
    html = src.read_text()
    html = html.replace("<!--FONTS-->", "<style>\n" + fonts + "\n" + base_css + "</style>")
    html = html.replace("<!--LOGO-->", logo)
    html = html.replace("<!--PRESENT-->", "<script>\n" + present + "</script>")
    out = src.with_name(src.name.replace(".src.html", ".html"))
    out.write_text(html)
    return out


def check(out: pathlib.Path) -> list:
    t = out.read_text()
    problems = []
    body = re.sub(r"data:font/woff2;base64,[A-Za-z0-9+/=]+", "", t)
    if "—" in body:
        problems.append("em dash present")
    for ph in ("<!--FONTS-->", "<!--LOGO-->", "<!--PRESENT-->"):
        if ph in t:
            problems.append(f"placeholder left: {ph}")
    if "<!doctype" not in t.lower():
        problems.append("missing doctype")
    if 'id="ilogo"' not in t:
        problems.append("logo symbol missing")
    return problems


if __name__ == "__main__":
    ok = True
    for src in sorted(HERE.glob("*.src.html")):
        out = build(src)
        probs = check(out) if "--check" in sys.argv else []
        print(f"{out.name}: {out.stat().st_size:,} bytes" + (f"  PROBLEMS: {probs}" if probs else ""))
        ok = ok and not probs
    sys.exit(0 if ok else 1)
