#!/usr/bin/env python3
"""Turn a working markdown document into a branded Intradiem page (Roboto, forest/green tokens, inline logo).

Standing rule (Sep 2 2026): anything written for Dallas ships as HTML. Markdown stays as source.

Run:  python3 md_to_page.py <doc.md> [out.html] [--eyebrow "GTM Engineering · All-hands"] [--sub "one line under the title"]
The first "# " line becomes the page title. A "> " block right after it becomes the lede.
No markdown library is needed; the parser covers headings, paragraphs, bullet and numbered lists
(one level of nesting), pipe tables, fenced code, blockquotes, horizontal rules, bold, inline code, links.
"""
import html as H
import pathlib
import re
import sys
import datetime

HERE = pathlib.Path(__file__).resolve().parent
TPL = HERE.parent / "ai_champion_product" / "_tpl"

fonts = "\n".join(l for l in (TPL / "fonts_head.html").read_text().splitlines() if l.startswith("@font-face"))
base_css = (TPL / "base.css").read_text()
logo = (TPL / "logo_symbol.html").read_text()

DOC_CSS = """
.doc{padding:34px 0 60px}
.doc h2{margin-top:34px}
.doc h2:first-child{margin-top:0}
.doc h3{font-weight:700;font-size:18px;margin:26px 0 8px}
.doc h4{font-weight:700;font-size:15px;margin:18px 0 6px;color:var(--ink-2)}
.doc p{margin:0 0 12px;max-width:80ch;font-size:15.5px}
.doc ul,.doc ol{margin:0 0 14px 22px;max-width:80ch;font-size:15.5px}
.doc li{margin:0 0 6px}
.doc li ul,.doc li ol{margin:6px 0 4px 20px}
.doc table{width:100%;border-collapse:collapse;margin:10px 0 20px;font-size:14px}
.doc th{text-align:left;font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--green-600);font-weight:600;padding:8px 10px;border-bottom:2px solid var(--line-strong);vertical-align:bottom}
.doc td{padding:9px 10px;border-bottom:1px solid var(--line);vertical-align:top}
.doc tr:nth-child(even) td{background:var(--zebra)}
.doc code{font-family:var(--ff-mono);font-size:12.5px;background:var(--sidebar);border:1px solid var(--line);border-radius:4px;padding:1px 5px}
.doc pre{background:var(--forest);color:#E7F3EC;border-radius:var(--r);padding:16px 18px;overflow-x:auto;margin:10px 0 18px;font-size:13px;line-height:1.55}
.doc pre code{background:none;border:none;color:inherit;padding:0;font-size:inherit}
.doc blockquote{border-left:4px solid var(--green);background:var(--tint-soft);padding:12px 16px;margin:0 0 16px;border-radius:0 var(--r) var(--r) 0;max-width:80ch}
.doc blockquote p:last-child{margin:0}
.doc hr{border:none;border-top:1px solid var(--line);margin:28px 0}
.doc strong{font-weight:700}
.doc .lede{font-size:16.5px;color:var(--ink-2);max-width:78ch;margin-bottom:22px}
footer.wrap{display:flex;align-items:center;gap:14px;padding:22px 30px 40px;color:var(--ink-3);font-size:12.5px}
footer .logo{height:20px}
"""

INLINE_CODE = re.compile(r"`([^`]+)`")
BOLD = re.compile(r"\*\*(.+?)\*\*")
LINK = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
URL = re.compile(r"(?<![\"'>=])\b(https?://[^\s<)\]]+)")


def inline(t: str) -> str:
    parts = []
    last = 0
    for m in INLINE_CODE.finditer(t):
        parts.append(_inline_text(t[last:m.start()]))
        parts.append(f"<code>{H.escape(m.group(1))}</code>")
        last = m.end()
    parts.append(_inline_text(t[last:]))
    return "".join(parts)


def _inline_text(t: str) -> str:
    t = H.escape(t, quote=False)
    t = LINK.sub(lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', t)
    t = URL.sub(lambda m: f'<a href="{m.group(1)}">{m.group(1)}</a>', t)
    t = BOLD.sub(r"<strong>\1</strong>", t)
    return t


def render(md: str):
    lines = md.splitlines()
    out = []
    title, lede = "", ""
    i = 0
    # title
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i < len(lines) and lines[i].startswith("# "):
        title = lines[i][2:].strip()
        i += 1
        while i < len(lines) and not lines[i].strip():
            i += 1
        if i < len(lines) and lines[i].startswith("> "):
            buf = []
            while i < len(lines) and lines[i].startswith(">"):
                buf.append(lines[i].lstrip("> ").strip())
                i += 1
            lede = " ".join(buf)

    def flush_para(buf):
        if buf:
            out.append(f"<p>{inline(' '.join(buf))}</p>")
            buf.clear()

    para = []
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if not s:
            flush_para(para); i += 1; continue
        if s.startswith("```"):
            flush_para(para)
            code = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code.append(lines[i]); i += 1
            i += 1
            out.append(f"<pre><code>{H.escape(chr(10).join(code))}</code></pre>")
            continue
        m = re.match(r"^(#{2,4})\s+(.*)$", s)
        if m:
            flush_para(para)
            lvl = len(m.group(1))
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>")
            i += 1; continue
        if s in ("---", "***"):
            flush_para(para); out.append("<hr>"); i += 1; continue
        if s.startswith(">"):
            flush_para(para)
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip().lstrip(">").strip()); i += 1
            out.append(f"<blockquote><p>{inline(' '.join(buf))}</p></blockquote>")
            continue
        if s.startswith("|"):
            flush_para(para)
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i].strip()); i += 1
            cells = [[c.strip() for c in r.strip("|").split("|")] for r in rows]
            body = [c for c in cells if not all(re.fullmatch(r":?-{2,}:?", x or "--") for x in c)]
            if body:
                head, rest = body[0], body[1:]
                t = ["<table><thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead><tbody>"]
                for r in rest:
                    t.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
                t.append("</tbody></table>")
                out.append("".join(t))
            continue
        lm = re.match(r"^(\s*)([-*•]|\d+[.)])\s+(.*)$", ln)
        if lm:
            flush_para(para)
            # collect list block
            items = []
            while i < len(lines):
                mm = re.match(r"^(\s*)([-*•]|\d+[.)])\s+(.*)$", lines[i])
                if mm:
                    items.append((len(mm.group(1)), mm.group(2), mm.group(3))); i += 1
                elif lines[i].strip() and lines[i].startswith("  ") and items:
                    d, k, txt = items[-1]; items[-1] = (d, k, txt + " " + lines[i].strip()); i += 1
                else:
                    break
            out.append(_list(items))
            continue
        para.append(s); i += 1
    flush_para(para)
    return title, lede, "\n".join(out)


def _list(items):
    def tag(k):
        return "ol" if k[0].isdigit() else "ul"
    html = []
    stack = []  # (indent, tag)
    for d, k, txt in items:
        t = tag(k)
        if not stack:
            stack.append((d, t)); html.append(f"<{t}>")
        elif d > stack[-1][0]:
            stack.append((d, t)); html.append(f"<{t}>")
        else:
            while len(stack) > 1 and d < stack[-1][0]:
                html.append(f"</li></{stack.pop()[1]}>")
            html.append("</li>")
        html.append(f"<li>{inline(txt)}")
    while stack:
        html.append(f"</li></{stack.pop()[1]}>")
    return "".join(html)


def build(src: pathlib.Path, out: pathlib.Path, eyebrow: str, sub: str):
    title, lede, body = render(src.read_text())
    date = datetime.date.today().strftime("%b %-d, %Y")
    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>{H.escape(title)}</title>
<style>
{fonts}
{base_css}
{DOC_CSS}
</style></head><body>
{logo}
<div class="sheet">
<div class="hero on"><div class="wrap">
  <svg class="logo"><use href="#ilogo"/></svg>
  <div class="eyebrow">{H.escape(eyebrow)}</div>
  <h1>{inline(title)}</h1>
  {f'<p class="sub">{inline(sub)}</p>' if sub else ''}
  <div class="meta"><div><span>Prepared by</span>Dallas Andrews</div><div><span>Date</span>{date}</div></div>
</div></div>
<section class="doc"><div class="wrap">
{f'<p class="lede">{inline(lede)}</p>' if lede else ''}
{body}
</div></section>
<footer class="wrap"><svg class="logo"><use href="#ilogo"/></svg><span>GTM Engineering &middot; Dallas Andrews &middot; {date}</span></footer>
</div>
</body></html>"""
    assert "—" not in page.replace(fonts, ""), "em dash in output"
    out.write_text(page)
    return out


if __name__ == "__main__":
    args = sys.argv[1:]
    eyebrow, sub = "GTM Engineering", ""
    if "--eyebrow" in args:
        j = args.index("--eyebrow"); eyebrow = args[j + 1]; del args[j:j + 2]
    if "--sub" in args:
        j = args.index("--sub"); sub = args[j + 1]; del args[j:j + 2]
    src = pathlib.Path(args[0])
    out = pathlib.Path(args[1]) if len(args) > 1 else src.with_suffix(".html")
    print(build(src, out, eyebrow, sub))
