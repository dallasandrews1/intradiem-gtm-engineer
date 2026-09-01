#!/usr/bin/env python3
"""Bridge: turn a markdown account brief (the pre-HTML skill output) into the branded page.

The partner-account-brief skill now emits HTML directly, so this exists for briefs that
were produced before that change, and for anyone who hands over a brief as markdown.

Run:  python3 md_to_brief_html.py <brief.md> <out.html> "Account Name" "the angle phrase"
"""
import html as H
import pathlib
import re
import sys
import datetime

TPL = pathlib.Path(__file__).resolve().parent / "frank_selfserve/skills/partner-account-brief/brief_template.html"
FLAG = re.compile(r"\((ESTIMATED|INFERRED|UNVERIFIED|EMPLOYEE SENTIMENT[^)]*)\)")
MDLINK = re.compile(r"\[([^\]]+)\]\((https?://[^)]+)\)")
TRAIL = re.compile(r"\s*\[([^\]]+)\]\s*$")


def inline(t):
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = MDLINK.sub(lambda m: f'<a href="{m.group(2)}">{m.group(1)}</a>', t)
    return t.strip()


def split_source(t):
    """Pull a trailing [ ... ] citation off a bullet, return (body, source_html)."""
    m = TRAIL.search(t)
    if not m:
        return t, ""
    body, raw = t[: m.start()].strip(), m.group(1).strip()
    urls = re.findall(r"https?://\S+?(?=[,\s\]]|$)", raw)
    if urls:
        u = urls[0].rstrip(",")
        rest = raw.replace(u, "")
        rest = re.sub(r"\s*(and|,)\s*(?=,|$)", "", rest)
        rest = re.sub(r"[,\s]{2,}", ", ", rest).strip(" ,and")
        # any further URLs in the citation become links, never raw text
        rest = re.sub(r"(https?://\S+?)(?=[,\s]|$)",
                      lambda mm: f'<a href="{mm.group(1)}">{re.sub(chr(94)+"https?://(www.)?", "", mm.group(1))[:40]}...</a>', rest)
        label = re.sub(r"^https?://(www\.)?", "", u)
        label = (label[:58] + "...") if len(label) > 61 else label
        src = f'<span class="src"><a href="{u}">{label}</a>{" · " + rest if rest else ""}</span>'
    else:
        src = f'<span class="src">{inline(raw)}</span>'
    return body, src


def flagify(t):
    """Turn (INFERRED)/(UNVERIFIED)/etc into pills; returns (text, pill_html)."""
    pills = []
    def sub(m):
        f = m.group(1)
        cls = {"ESTIMATED": "est", "INFERRED": "inf"}.get(f.split(",")[0], "")
        pills.append(f'<span class="flag {cls}">{H.escape(f)}</span>')
        return ""
    t = FLAG.sub(sub, t)
    return re.sub(r"\s{2,}", " ", t).strip(" ,."), "".join(pills)


def bullet(line):
    t = line[2:].strip()
    body, src = split_source(t)
    body, pills = flagify(body)
    # bold a short lead sentence when the author wrote one
    m = re.match(r"^([A-Z][^.]{2,44}\.)\s+(.*)$", body)
    if m and "<strong>" not in body:
        body = f"<strong>{m.group(1)}</strong> {m.group(2)}"
    return f"        <li>{inline(body)}{pills}{src}</li>"


def parse(md):
    lines = md.splitlines()
    h1 = next((l[2:].strip() for l in lines if l.startswith("# ")), "")
    sub = next((l.strip("_ ").strip() for l in lines if l.startswith("_")), "")
    secs, cur = [], None
    for l in lines:
        if l.startswith("## "):
            cur = (l[3:].strip(), [])
            secs.append(cur)
        elif cur is not None:
            cur[1].append(l)
    return h1, sub, secs


def render(secs):
    out = []
    for title, body in secs:
        rows = [l for l in body if l.strip()]
        if not rows:
            continue
        low = title.lower()
        out.append(f'    <section>\n      <p class="label">{H.escape(title)}</p>')
        if low.startswith("who to reach"):
            trs = [r for r in rows if r.startswith("|") and "---" not in r]
            hdr = [c.strip() for c in trs[0].strip("|").split("|")]
            out.append("      <table><thead><tr>" + "".join(f"<th>{H.escape(c)}</th>" for c in hdr) + "</tr></thead><tbody>")
            for r in trs[1:]:
                cells = [c.strip() for c in r.strip("|").split("|")]
                tds = []
                for i, c in enumerate(cells):
                    c2, pills = flagify(c)
                    v = inline(c2) + pills
                    if i == 0:
                        tds.append(f'<td class="nm">{v}</td>')
                    elif i == 2:
                        tds.append(f'<td><span class="role">{v}</span></td>')
                    else:
                        tds.append(f"<td>{v}</td>")
                out.append("        <tr>" + "".join(tds) + "</tr>")
            out.append("      </tbody></table>")
            for p in [r for r in rows if not r.startswith("|")]:
                out.append(f"      <p>{inline(p)}</p>")
        elif low.startswith("timing"):
            for r in rows:
                if not r.startswith("- "):
                    body_p, pills = flagify(r)
                    out.append(f"      <p>{inline(body_p)}{pills}</p>")
                    continue
                t = r[2:].strip()
                m = re.match(r"^(\*\*)?([A-Z][a-z]{2} \d{1,2},? \d{4}|[A-Z][a-z]{2} \d{4}|\d{4})(\*\*)?\s*\(?[^)]*\)?\s*[:.]\s*(.*)$", t)
                when, rest = (m.group(2), m.group(4)) if m else ("", t)
                parts = re.split(r"\bSo what[:,]\s*", rest, maxsplit=1)
                what = parts[0].strip()
                so = parts[1].strip() if len(parts) > 1 else ""
                what, p1 = flagify(what)
                so, p2 = flagify(so)
                out.append(f'      <div class="trig"><span class="d">{H.escape(when)}</span>'
                           f"<span><b>{inline(what)}</b>{p1}</span>"
                           + (f'<span class="so">{inline(so)}{p2}</span>' if so else "") + "</div>")
        elif low.startswith("discovery"):
            out.append('      <ol class="q">')
            for r in rows:
                m = re.match(r"^\d+\.\s*(.*)$", r.strip())
                if not m:
                    continue
                q = m.group(1)
                fm = re.search(r"\(from:\s*(.+?)\)\s*$", q)
                frm = fm.group(1) if fm else ""
                q = FLAG.sub("", q[: fm.start()] if fm else q).strip()
                out.append(f"        <li>{inline(q)}" + (f"<small>from: {H.escape(frm)}</small>" if frm else "") + "</li>")
            out.append("      </ol>")
        elif low.startswith("confidence"):
            txt = " ".join(rows)
            out.append('      <div class="conf">')
            for m in re.finditer(r"([A-Za-z][A-Za-z &()a-z,\-]*?):\s*(High|Medium|Low)", txt):
                cls = {"High": "h", "Low": "l"}.get(m.group(2), "")
                out.append(f'        <span class="{cls}">{H.escape(m.group(1).strip())}: {m.group(2)}</span>')
            out.append("      </div>")
        elif low.startswith("gaps"):
            out.append('      <div class="callout"><ul>')
            for r in rows:
                if r.startswith("- "):
                    out.append(bullet(r))
            out.append("      </ul></div>")
        elif low.startswith("sources"):
            out.append('      <div class="srcs">')
            for r in rows:
                m = MDLINK.search(r)
                if m:
                    out.append(f'        <div><a href="{m.group(2)}">{H.escape(m.group(1))}</a></div>')
            out.append("      </div>")
        else:
            bl = [r for r in rows if r.startswith("- ")]
            ps = [r for r in rows if not r.startswith("- ") and r.strip()]
            if bl:
                out.append("      <ul>")
                out += [bullet(r) for r in bl]
                out.append("      </ul>")
            for p in ps:
                pp, pills = flagify(p)
                out.append(f"      <p>{inline(pp)}{pills}</p>")
        out.append("    </section>")
    return "\n".join(out)


def main():
    src, dst, account, angle = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    h1, sub, secs = parse(pathlib.Path(src).read_text())
    page = (TPL.read_text()
            .replace("{{ACCOUNT}}", H.escape(account))
            .replace("{{ANGLE}}", angle)
            .replace("{{SUBHEAD}}", inline(sub))
            .replace("{{DATE}}", datetime.date.today().strftime("%b %-d %Y"))
            .replace("{{BODY}}", render(secs)))
    assert "—" not in page, "em dash in output"
    pathlib.Path(dst).write_text(page)
    print(f"{dst}: {len(page):,} bytes, {len(secs)} sections")


if __name__ == "__main__":
    main()
