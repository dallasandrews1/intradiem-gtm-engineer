#!/usr/bin/env python3
"""Assemble the AI Champion (Product) pages from their .src.html files.

Each source keeps its own <title>, page CSS, and body. Placeholders:
  <!--FONTS-->   embedded Roboto + Roboto Mono (woff2 data URIs) plus the shared base.css
  <!--LOGO-->    the inline Intradiem logo <symbol id="ilogo">
  <!--PRESENT--> the shared present-mode + reveal script
Run:  python3 build_pages.py            (writes X.html next to X.src.html)
      python3 build_pages.py --check    (also greps the outputs for em dashes and stray placeholders)
"""
import pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent
TPL = HERE / "_tpl"

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
    html = re.sub(r"<!--/?S(?::[A-Z]+)?-->", "", html)  # live-stat markers (pmo_rows.py) never ship
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
    return problems

if __name__ == "__main__":
    ok = True
    for src in sorted(HERE.glob("*.src.html")):
        out = build(src)
        probs = check(out) if "--check" in sys.argv else []
        print(f"{out.name}: {out.stat().st_size:,} bytes" + (f"  PROBLEMS: {probs}" if probs else ""))
        ok = ok and not probs
    sys.exit(0 if ok else 1)
