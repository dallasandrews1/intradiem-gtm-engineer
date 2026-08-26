#!/usr/bin/env python3
# STRIKE ROOM PDF TEMPLATE (green kit) — per-account edits, marked below:
#   1. MD filename (line starting MD = open(...))
#   2. Front page: sec_page eyebrow/title + footer strings (search "Why Aflac")
#   3. Committee section header string if the md heading differs
#   4. Objections header string if the md heading differs
#   5. COVER block: eyebrow, h1, sub, 4 stat tiles, AE lane in .foot
# Then: python3 build_pdf_TEMPLATE.py && python3 render.py && merge+stamp (see README).

"""Build the branded green-kit PDF for the Blue Shield of CA strike room.
Pipeline per Cardinal Health v2 precedent: cover + body rendered separately
(playwright, print zoom 1.333333), merged with pypdf, page numbers stamped
via reportlab counting the cover."""
import re, base64, html as H

MD = open('CostMandate_Aflac_StrikeRoom_Sequence_v1.md').read()
LOGO = open('logo.svg').read()
LOGO_B64 = base64.b64encode(LOGO.encode()).decode()

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800;900&family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap');
:root{--forest:#16432C;--green:#1F7340;--green-bright:#25B56F;--lime:#B6D94C;--ink:#15231B;--ink-soft:#3E4D44;--dim:#7A877E;--paper:#FAFBF7;--card:#FFFFFF;--mist:#F0F4ED;--mist2:#E7EEE3;--line:#E2E7DD;--line2:#D4DCCE;--spark:#FE5000;--gold:#E0A23B;}
*{box-sizing:border-box;margin:0;padding:0}
@media print{body{zoom:1.333333}}
body{font-family:'DM Sans',system-ui,sans-serif;color:var(--ink);background:var(--paper);font-size:9.2pt;line-height:1.5}
.page{page-break-after:always;padding:10pt 40pt 6pt}
.page:last-child{page-break-after:auto}
.eyebrow{font-family:'JetBrains Mono',monospace;font-size:6.6pt;letter-spacing:.22em;text-transform:uppercase;color:var(--green);font-weight:600;margin-bottom:6pt}
.eyebrow .sp{color:var(--spark)}
h1.sec{font-family:'Playfair Display',serif;font-size:21pt;font-weight:800;color:var(--forest);margin-bottom:10pt;line-height:1.15}
h2.sub{font-family:'Playfair Display',serif;font-size:12.5pt;font-weight:700;color:var(--green);margin:12pt 0 6pt}
p{margin-bottom:7pt;color:var(--ink-soft)}
p strong{color:var(--ink)}
table{width:100%;border-collapse:collapse;margin:7pt 0;font-size:7.8pt}
th{font-family:'JetBrains Mono',monospace;font-size:6.4pt;letter-spacing:.12em;text-transform:uppercase;color:var(--forest);text-align:left;padding:5pt 7pt;border-bottom:1.5pt solid var(--forest);background:var(--mist)}
td{padding:4pt 6pt;border-bottom:.6pt solid var(--line);vertical-align:top;color:var(--ink-soft)}
tr:nth-child(even) td{background:var(--mist)}
td:first-child{color:var(--ink);font-weight:500}
.callout{background:var(--mist);border-left:2.5pt solid var(--green);padding:8pt 11pt;border-radius:0 4pt 4pt 0;margin:8pt 0}
.callout.spark{border-left-color:var(--spark)}
.callout.dark{background:var(--forest);border-left-color:var(--lime);color:#E8F0E9}
.callout.dark p, .callout.dark{color:#E8F0E9}
.callout.dark strong{color:var(--lime)}
/* contact pages */
.chead{background:var(--forest);color:#fff;border-radius:6pt;padding:12pt 14pt;margin-bottom:10pt;display:flex;justify-content:space-between;align-items:flex-start}
.chead .num{font-family:'JetBrains Mono',monospace;font-size:7pt;letter-spacing:.2em;color:var(--lime);margin-bottom:3pt}
.chead h3{font-family:'Playfair Display',serif;font-size:15pt;font-weight:800;line-height:1.1}
.chead .title{font-size:8.6pt;color:#CBD9CE;margin-top:2pt}
.chips{text-align:right}
.chip{display:inline-block;font-family:'JetBrains Mono',monospace;font-size:6.2pt;letter-spacing:.1em;text-transform:uppercase;padding:2.5pt 6pt;border-radius:8pt;margin:0 0 3pt 3pt;background:rgba(182,217,76,.18);color:var(--lime);border:.6pt solid rgba(182,217,76,.5)}
.chip.hot{background:rgba(254,80,0,.15);color:#FFB08A;border-color:rgba(254,80,0,.5)}
.touch{background:var(--card);border:.8pt solid var(--line2);border-radius:5pt;padding:8pt 11pt;margin-bottom:7pt;page-break-inside:avoid}
.touch .tlabel{font-family:'JetBrains Mono',monospace;font-size:6.4pt;letter-spacing:.16em;text-transform:uppercase;color:var(--green);font-weight:600;margin-bottom:3pt}
.touch .tlabel .day{color:var(--spark)}
.touch .subj{font-weight:700;color:var(--forest);font-size:9.4pt;margin-bottom:4pt;font-family:'DM Sans',sans-serif}
.touch p{margin-bottom:5pt;font-size:8.8pt}
.touch p:last-child{margin-bottom:0}
.touch.live{background:var(--mist);border-color:var(--green)}
.touch.live .tlabel{color:var(--forest)}
.script-line{margin-bottom:4.5pt;font-size:8.8pt}
.script-line em.slab{font-style:normal;font-family:'JetBrains Mono',monospace;font-size:6.6pt;letter-spacing:.08em;text-transform:uppercase;color:var(--green);font-weight:600;display:block;margin-bottom:1pt}
.sig{font-family:'JetBrains Mono',monospace;font-size:7.6pt;color:var(--dim)}
.foot{display:none}
"""

COVER_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800;900&family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
@media print{body{zoom:1.333333}}
html,body{width:6.375in;height:8.25in;overflow:hidden}
body{font-family:'DM Sans',system-ui,sans-serif}
.cover{width:6.375in;height:8.25in;background:linear-gradient(160deg,#0F3322 0%,#16432C 55%,#1B5236 100%);color:#fff;padding:40pt 38pt;position:relative;overflow:hidden}
.cover:before{content:'';position:absolute;right:-120pt;top:-120pt;width:340pt;height:340pt;border-radius:50%;background:radial-gradient(circle,rgba(182,217,76,.14),transparent 65%)}
.logochip{display:inline-block;background:#fff;border-radius:6pt;padding:9pt 14pt;margin-bottom:30pt}
.logochip img{height:22pt;display:block}
.eyebrow{font-family:'JetBrains Mono',monospace;font-size:8pt;letter-spacing:.28em;text-transform:uppercase;color:#B6D94C;font-weight:600;margin-bottom:14pt}
.eyebrow .sp{color:#FE5000}
h1{font-family:'Playfair Display',serif;font-size:31pt;font-weight:900;line-height:1.06;margin-bottom:10pt}
.sub{font-size:12.5pt;color:#C9D8CD;max-width:400pt;line-height:1.5;margin-bottom:26pt}
.stats{display:flex;gap:10pt;margin-bottom:0}
.stat{background:rgba(255,255,255,.06);border:.8pt solid rgba(182,217,76,.35);border-radius:6pt;padding:10pt 13pt;flex:1}
.stat .v{font-family:'Playfair Display',serif;font-size:16.5pt;font-weight:800;color:#B6D94C;margin-bottom:2pt}
.stat .v.sp{color:#FF8A50}
.stat .k{font-family:'JetBrains Mono',monospace;font-size:6.2pt;letter-spacing:.14em;text-transform:uppercase;color:#9FB8A6}
.foot{position:absolute;bottom:32pt;left:38pt;right:38pt;display:flex;justify-content:space-between;align-items:flex-end;border-top:.8pt solid rgba(255,255,255,.18);padding-top:12pt}
.foot .l{font-size:9pt;color:#C9D8CD;line-height:1.6}
.foot .l strong{color:#fff}
.foot .r{font-family:'JetBrains Mono',monospace;font-size:7pt;letter-spacing:.18em;text-transform:uppercase;color:#9FB8A6;text-align:right;line-height:1.8}
"""

def inline(s):
    s = H.escape(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'\*(.+?)\*', r'<em>\1</em>', s)
    s = re.sub(r'`(.+?)`', r'<code>\1</code>', s)
    return s

def md_table(block):
    rows = [r for r in block.strip().split('\n') if r.strip().startswith('|')]
    out = ['<table>']
    for i, r in enumerate(rows):
        if set(r.replace('|','').strip()) <= set('-: '):
            continue
        cells = [c.strip() for c in r.strip().strip('|').split('|')]
        tag = 'th' if i == 0 else 'td'
        out.append('<tr>' + ''.join(f'<{tag}>{inline(c)}</{tag}>' for c in cells) + '</tr>')
    out.append('</table>')
    return '\n'.join(out)

def paras(text, cls=''):
    out = []
    for blk in re.split(r'\n\n+', text.strip()):
        if not blk.strip(): continue
        if blk.strip().startswith('|'):
            out.append(md_table(blk))
        else:
            c = f' class="{cls}"' if cls else ''
            out.append(f'<p{c}>{inline(blk.strip())}</p>')
    return '\n'.join(out)

# ---- split the md ----
m = re.split(r'\n---\n', MD)
head = m[0]; snapshot = m[1]; committee = m[2]; cansay = m[3]; cadence = m[4]
seq_and_rest = '\n---\n'.join(m[5:])
seq_body = seq_and_rest.split('## Objection quick-handles')[0]
objections = '## Objection quick-handles' + seq_and_rest.split('## Objection quick-handles')[1].split('## Claims basis')[0]
claims = '## Claims basis' + seq_and_rest.split('## Claims basis')[1]

contacts = re.split(r'\n### ', seq_body)[1:]

def sec_page(eyebrow, title, body_html, foot_r):
    return f'''<div class="page"><div class="eyebrow">{eyebrow} <span class="sp">///</span></div><h1 class="sec">{title}</h1>{body_html}<div class="foot"><span>INTRADIEM · GTM ENGINEERING</span><span>{foot_r}</span></div></div>'''

pages = []

# Page: forcing function
ff = re.search(r'\*\*The forcing function:\*\*(.*?)\n\n', head, re.S).group(1).strip()
ff = ff[0].upper()+ff[1:]
thesis = re.search(r'\*\*The one thesis every seat hears:\*\*(.*?)\n\n', head, re.S).group(1).strip()
thesis = thesis[0].upper()+thesis[1:]
meta = re.search(r'\*\*Motion:\*\*(.*?)\n', head).group(1).strip()
body = f'<div class="callout"><p><strong>Motion:</strong> {inline(meta)}</p></div>'
body += f'<h2 class="sub">The forcing function</h2><p>{inline(ff)}</p>'
body += f'<div class="callout dark"><strong>The one thesis every seat hears:</strong> {inline(thesis)}</div>'
body += '<div class="callout spark"><p><strong>Merge fields:</strong> <code>{{sender}}</code> first name, Touches 1-3 and voicemail intros · <code>{{sender_full_name}}</code> Touches 4-5.</p></div>'
pages.append(sec_page('COST-MANDATE MOTION · ONE-OFF STRIKE ROOM', 'Why Aflac, why now', body, 'AFLAC'))

# Page: snapshot
snap_body = paras(snapshot.replace('## Account snapshot','').strip())
pages.append(sec_page('ACCOUNT INTELLIGENCE', 'Account snapshot', snap_body, 'SOURCES: AFLAC Q1 2026 RELEASE + CALL'))

# Page: committee
com_body = paras(committee.replace('## Buying committee (pulled and enriched in Clay, Jul 16; emails 8/8 first-pass waterfall)','').strip())
pages.append(sec_page('EIGHT SEATS, ONE THESIS', 'Buying committee', com_body, 'PULLED + FULLY ENRICHED IN CLAY · JUL 16 2026'))

# Page: guardrails + choreography
g_body = paras(cansay.replace('## What reps can and cannot say','').strip())
c_body = paras(cadence.replace('## Cadence and committee choreography','').replace('## Sequences','').strip())
pages.append(sec_page('GUARDRAILS', 'What reps can and cannot say', g_body, 'VERIFIED-CLAIMS GATE · CUSTOMER-EXCLUSION GATE'))
pages.append(sec_page('CHOREOGRAPHY', 'Cadence and committee entry', c_body, 'FIVE-TOUCH CORE · EXTENDED ARC ON MUST-WINS'))

# Contact pages
for c in contacts:
    header, rest = c.split('\n', 1)
    hm = re.match(r'(\d+)\. (.+?) — (.+)', header)
    num, name, titleline = hm.group(1), hm.group(2), hm.group(3)
    bits = [b.strip() for b in titleline.split('·')]
    title = bits[0]
    chips = ''.join(f'<span class="chip{" hot" if ("EXTENDED" in b or "must-win" in b or "contract-specific" in b) else ""}">{H.escape(b)}</span>' for b in bits[1:])
    touches = re.split(r'\n\*\*(Touch [^*]+)\*\*', rest)
    cards = []
    for i in range(1, len(touches), 2):
        label = touches[i].strip()
        content = touches[i+1].strip().rstrip('-').strip()
        live = 'If they answer' in label
        lab = re.sub(r'\(Day (\d+)\)', r'· <span class="day">DAY \1</span> ·', H.escape(label).replace(' — ',' · ').upper())
        subj = ''
        smatch = re.match(r'Subject: (.+?)(\n|$)', content)
        if smatch:
            subj = f'<div class="subj">Subject: {inline(smatch.group(1))}</div>'
            content = content[smatch.end():].strip()
        if live or content.startswith('*Opener'):
            lines = []
            for ln in re.split(r'\n\n+', content):
                ln = ln.strip()
                lm = re.match(r'\*(.+?):\*\s*(.*)', ln, re.S)
                if lm:
                    lines.append(f'<div class="script-line"><em class="slab">{H.escape(lm.group(1))}</em>{inline(lm.group(2))}</div>')
                elif ln:
                    lines.append(f'<div class="script-line">{inline(ln)}</div>')
            body_html = '\n'.join(lines)
        else:
            tok = re.search(r'\{\{(sender(?:_full_name)?)\}\}\s*$', content)
            if tok:
                content = content[:tok.start()].strip()
                body_html = paras(content) + '<div class="sig">{{' + tok.group(1) + '}}</div>'
            else:
                body_html = paras(content)
        cards.append(f'<div class="touch{" live" if live else ""}"><div class="tlabel">{lab}</div>{subj}{body_html}</div>')
    chead = f'''<div class="chead"><div><div class="num">CONTACT {num} OF 8</div><h3>{H.escape(name)}</h3><div class="title">{H.escape(title)}</div></div><div class="chips">{chips}</div></div>'''
    pages.append(f'<div class="page">{chead}{"".join(cards)}<div class="foot"><span>INTRADIEM · GTM ENGINEERING</span><span>{H.escape(name.upper())} · SEQUENCE</span></div></div>')

# Objections page
ob_body = paras(objections.replace('## Objection quick-handles (Cost-Mandate standard, Aflac flavor)','').replace('> ','').strip())
pages.append(sec_page('WHEN THEY PUSH BACK', 'Objection quick-handles', ob_body, 'REFRAME: ACKNOWLEDGE · PIVOT · SOFT CTA'))

# Claims page
cl_body = paras(claims.replace('## Claims basis','**Claims basis.**').replace('## Execution notes (one-off account strategy, stays out of the Clay workbooks)','**Execution notes (one-off, stays out of the Clay workbooks).**').strip())
pages.append(sec_page('RECEIPTS', 'Claims basis and execution notes', cl_body, 'NOTHING SENDS WITHOUT HUMAN APPROVAL'))

body_html = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
open('body.html','w').write(body_html)

cover_html = f'''<!doctype html><html><head><meta charset="utf-8"><style>{COVER_CSS}</style></head><body>
<div class="cover">
<div class="logochip"><img src="data:image/svg+xml;base64,{LOGO_B64}"></div>
<div class="eyebrow">COST-MANDATE MOTION <span class="sp">///</span> ONE-OFF STRIKE ROOM</div>
<h1>Aflac</h1>
<div class="sub">Buying-committee strike sequences for a book growing fastest exactly where service intensity is highest, against an expense envelope Aflac's own release holds flat.</div>
<div class="stats">
<div class="stat"><div class="v">+25%</div><div class="k">Group life, absence, disability, Q1 26 (their call)</div></div>
<div class="stat"><div class="v sp">-1.5%</div><div class="k">Total opex $1.29B, held flat (their release)</div></div>
<div class="stat"><div class="v">8 seats</div><div class="k">Committee sequenced, 2 extended arcs, 8/8 emails</div></div>
<div class="stat"><div class="v">Q4 clock</div><div class="k">Enrollment season, the heaviest weeks of the year</div></div>
</div>
<div class="foot">
<div class="l"><strong>Prepared for Nathan Belfield</strong> · AE lane: Mike Regan<br>Dallas Andrews · GTM Engineering</div>
<div class="r">JULY 16 2026<br>DRAFT · HUMAN GATE ON</div>
</div>
</div></body></html>'''
open('cover.html','w').write(cover_html)
print('html built:', len(body_html), 'bytes,', len(pages), 'body pages')
