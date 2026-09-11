#!/usr/bin/env python3
"""Render a markdown note onto the Intradiem GTM Engineering page system.

Usage: build_md_page.py <source.md> <out.html> --eyebrow "..." --title "..." [--spark "word"] --sub "..." [--meta "K=V" ...]

Markdown subset: #/##/### headings, paragraphs, **bold**, *em*, `code`, bullet lists, numbered lists,
pipe tables, > blockquotes (rendered as message cards), ``` fenced blocks. Each ## starts a section.
CSS and the official logo symbol are lifted verbatim from motions/upt_displacement/UPT_Attack_Brief_Sep10.html
so every page reads as one product (brand kit Jul 30 2026).
"""
import argparse, html, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REF = os.path.join(ROOT, "motions", "upt_displacement", "UPT_Attack_Brief_Sep10.html")

EXTRA_CSS = """
.msg{background:var(--zebra);border:1px solid var(--line);border-left:4px solid var(--green-300);border-radius:var(--r);padding:16px 20px;margin:14px 0 6px;max-width:78ch}
.msg p{margin:0 0 10px;font-size:14.5px;color:var(--ink);max-width:none}
.msg p:last-child{margin-bottom:0}
.msg code{font-family:var(--ff-mono);font-size:12.5px;background:var(--tint-soft);padding:1px 5px;border-radius:4px;color:var(--green-600)}
code{font-family:var(--ff-mono);font-size:12.5px;background:var(--tint-soft);padding:1px 5px;border-radius:4px;color:var(--green-600)}
pre{font-family:var(--ff-mono);font-size:12.5px;background:var(--forest);color:#C7DAD1;padding:16px 20px;border-radius:var(--r);overflow-x:auto;margin-top:14px;line-height:1.5}
ul.b,ol.b{margin:10px 0 0 0;max-width:78ch;padding-left:22px}
ul.b li,ol.b li{padding:4px 0;font-size:15px;color:var(--ink-2)}
ul.b li::marker{color:var(--green-600)}
.flow{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin-top:16px}
.flow span{background:var(--tint-soft);border:1px solid var(--tint);border-radius:6px;padding:8px 12px;font-family:var(--ff-mono);font-size:11.5px;color:var(--forest);font-weight:600}
.flow i{color:var(--green-600);font-style:normal;font-weight:700}
h3{margin-top:26px}
"""

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![\w*])\*([^*]+)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', s)
    return s

def render_table(lines):
    rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lines]
    head, body = rows[0], [r for r in rows[2:] if any(r)]
    out = ['<div class="tablewrap"><table><thead><tr>'] + [f"<th>{inline(h)}</th>" for h in head] + ["</tr></thead><tbody>"]
    for r in body:
        out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)

def render_block(lines):
    """Blockquote -> message card. Lines already stripped of '> '."""
    paras, cur = [], []
    for l in lines:
        if l.strip() == "":
            if cur: paras.append(" ".join(cur)); cur = []
        else:
            cur.append(l.strip())
    if cur: paras.append(" ".join(cur))
    return '<div class="msg">' + "".join(f"<p>{inline(p)}</p>" for p in paras) + "</div>"

def md_to_sections(text):
    """Returns (title_h1, [(h2, html_body)])."""
    lines = text.splitlines()
    h1, sections, cur_h, buf = None, [], None, []
    def flush():
        nonlocal buf
        if cur_h is not None or buf:
            sections.append((cur_h, body_html(buf)))
        buf = []
    for l in lines:
        if l.startswith("# ") and h1 is None:
            h1 = l[2:].strip(); continue
        if l.startswith("## "):
            flush(); cur_h = l[3:].strip(); continue
        buf.append(l)
    flush()
    return h1, sections

def body_html(lines):
    out, i, n = [], 0, len(lines)
    while i < n:
        l = lines[i]
        if l.strip() == "":
            i += 1; continue
        if l.startswith("### "):
            out.append(f"<h3>{inline(l[4:].strip())}</h3>"); i += 1; continue
        if l.startswith("```"):
            j = i + 1; code = []
            while j < n and not lines[j].startswith("```"):
                code.append(lines[j]); j += 1
            out.append("<pre>" + html.escape("\n".join(code)) + "</pre>"); i = j + 1; continue
        if l.lstrip().startswith("|"):
            j = i; tbl = []
            while j < n and lines[j].lstrip().startswith("|"):
                tbl.append(lines[j]); j += 1
            out.append(render_table(tbl)); i = j; continue
        if l.startswith(">"):
            j = i; q = []
            while j < n and (lines[j].startswith(">") or lines[j].strip() == ""):
                if lines[j].strip() == "" and (j + 1 >= n or not lines[j + 1].startswith(">")):
                    break
                q.append(re.sub(r"^>\s?", "", lines[j])); j += 1
            out.append(render_block(q)); i = j; continue
        if re.match(r"^\s*[-*] ", l):
            j = i; items = []
            while j < n and re.match(r"^\s*[-*] ", lines[j]):
                item = re.sub(r"^\s*[-*] ", "", lines[j]); j += 1
                while j < n and lines[j].startswith("  ") and not re.match(r"^\s*[-*] ", lines[j]):
                    item += " " + lines[j].strip(); j += 1
                items.append(item)
            out.append('<ul class="b">' + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>"); i = j; continue
        if re.match(r"^\s*\d+\. ", l):
            j = i; items = []
            while j < n and re.match(r"^\s*\d+\. ", lines[j]):
                item = re.sub(r"^\s*\d+\. ", "", lines[j]); j += 1
                while j < n and lines[j].startswith("  ") and not re.match(r"^\s*\d+\. ", lines[j]):
                    item += " " + lines[j].strip(); j += 1
                items.append(item)
            out.append('<ol class="b">' + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ol>"); i = j; continue
        # paragraph
        j = i; p = []
        while j < n and lines[j].strip() != "" and not re.match(r"^(#{1,3} |```|\||>|\s*[-*] |\s*\d+\. )", lines[j]):
            p.append(lines[j].strip()); j += 1
        out.append(f"<p>{inline(' '.join(p))}</p>"); i = j
    return "\n".join(out)

def shell(css, logo, eyebrow, title, spark, sub, meta, sections, foot):
    if spark and spark in title:
        title_html = inline(title).replace(inline(spark), f'<span class="spark">{inline(spark)}</span>', 1)
    else:
        title_html = inline(title)
    meta_html = "".join(f"<div><span>{html.escape(k)}</span>{inline(v)}</div>" for k, v in meta)
    secs, idx = [], 0
    for h, body in sections:
        if h is None:
            secs.append(f'<section><div class="wrap">{body}</div></section>'); continue
        idx += 1
        h = re.sub(r"^\d+\.\s+", "", h)
        secs.append(f'<section class="rv"><div class="wrap"><div class="eyebrow">{idx:02d}</div><h2>{inline(h)}</h2>{body}</div></section>')
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{html.escape(title)}</title>
<style>{css}{EXTRA_CSS}</style></head><body>
<svg width="0" height="0" style="position:absolute" aria-hidden="true">{logo}</svg>
<div class="sheet">
<header class="hero on"><div class="wrap">
<svg class="logo" data-h="1"><use href="#ilogo"/></svg>
<div class="eyebrow" data-h="2">{inline(eyebrow)}</div>
<h1 data-h="3">{title_html}</h1>
<p class="sub" data-h="4">{inline(sub)}</p>
<div class="meta" data-h="5">{meta_html}</div>
</div></header>
{''.join(secs)}
<div class="foot"><svg class="logo"><use href="#ilogo"/></svg><span>{html.escape(foot)}</span></div>
</div>
<script>
(function(){{var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');io.unobserve(e.target);}}}});}},{{threshold:.05}});document.querySelectorAll('.rv').forEach(function(el){{io.observe(el);}});}})();
</script>
</body></html>"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("out")
    ap.add_argument("--eyebrow", required=True); ap.add_argument("--title", required=True)
    ap.add_argument("--spark", default=""); ap.add_argument("--sub", required=True)
    ap.add_argument("--meta", action="append", default=[])
    ap.add_argument("--foot", default="GTM Engineering · Intradiem")
    a = ap.parse_args()
    ref = open(REF, encoding="utf-8").read()
    css = re.search(r"<style>(.*?)</style>", ref, re.S).group(1)
    # drop the reference page's present-mode chrome, keep fonts + system
    css = re.sub(r"/\* PRESENT MODE \*/.*", "", css, flags=re.S)
    logo = re.search(r'<symbol id="ilogo".*?</symbol>', ref, re.S).group(0)
    text = open(a.src, encoding="utf-8").read()
    h1, sections = md_to_sections(text)
    meta = [tuple(m.split("=", 1)) for m in a.meta]
    page = shell(css, logo, a.eyebrow, a.title, a.spark, a.sub, meta, sections, a.foot)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    open(a.out, "w", encoding="utf-8").write(page)
    print(f"wrote {a.out} ({len(page)//1024} KB, {len(sections)} sections)")

if __name__ == "__main__":
    main()
