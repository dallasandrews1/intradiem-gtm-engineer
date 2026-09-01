#!/usr/bin/env python3
"""Generalized green-kit strike-room PDF builder (header-based parse).
One run: parse md -> cover.html + body.html -> render (playwright) -> merge + page numbers.
Bug fixes baked in: literal middot char (never &middot;) before any .upper(); forcing-function
and Hook lines get their first letter capitalized explicitly."""
import re, base64, html as H, io, sys

MD_FILE = "CostMandate_BMO_StrikeRoom_Sequence_v1.md"
OUT_PDF = "CostMandate_BMO_StrikeRoom_Sequence_v1.pdf"
ACCOUNT_TAG = "BANK OF MONTREAL"
MID = "·"  # literal middot, NOT the &middot; entity (Jul-29 bug 1)

MD = open(MD_FILE).read()
LOGO_B64 = base64.b64encode(open("logo.svg").read().encode()).decode()

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800;900&family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap');
:root{--forest:#16432C;--green:#1F7340;--green-bright:#25B56F;--lime:#B6D94C;--ink:#15231B;--ink-soft:#3E4D44;--dim:#7A877E;--paper:#FAFBF7;--card:#FFFFFF;--mist:#F0F4ED;--mist2:#E7EEE3;--line:#E2E7DD;--line2:#D4DCCE;--spark:#FE5000;--gold:#E0A23B;}
*{box-sizing:border-box;margin:0;padding:0}
@media print{body{zoom:1.333333}}
body{font-family:'DM Sans',system-ui,sans-serif;color:var(--ink);background:var(--paper);font-size:9.2pt;line-height:1.5;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{page-break-after:always;padding:10pt 40pt 6pt}
.page:last-child{page-break-after:auto}
.eyebrow{font-family:'JetBrains Mono',monospace;font-size:6.6pt;letter-spacing:.22em;text-transform:uppercase;color:var(--green);font-weight:600;margin-bottom:6pt}
.eyebrow .sp{color:var(--spark)}
h1.sec{font-family:'Playfair Display',serif;font-size:21pt;font-weight:800;color:var(--forest);margin-bottom:10pt;line-height:1.15}
h2.sub{font-family:'Playfair Display',serif;font-size:12.5pt;font-weight:700;color:var(--green);margin:12pt 0 6pt}
p{margin-bottom:6pt;color:var(--ink-soft)}
.page > p, .callout p{line-height:1.42}
p strong{color:var(--ink)}
ul{margin:5pt 0 8pt 16pt}
li{margin-bottom:4pt;color:var(--ink-soft);font-size:8.6pt}
li strong{color:var(--ink)}
table{width:100%;border-collapse:collapse;margin:7pt 0;font-size:7.4pt}
th{font-family:'JetBrains Mono',monospace;font-size:6.1pt;letter-spacing:.10em;text-transform:uppercase;color:var(--forest);text-align:left;padding:5pt 6pt;border-bottom:1.5pt solid var(--forest);background:var(--mist)}
td{padding:4pt 6pt;border-bottom:.6pt solid var(--line);vertical-align:top;color:var(--ink-soft)}
tr:nth-child(even) td{background:var(--mist)}
td:first-child{color:var(--ink);font-weight:500}
.callout{background:var(--mist);border-left:2.5pt solid var(--green);padding:8pt 11pt;border-radius:0 4pt 4pt 0;margin:8pt 0}
.callout p{margin-bottom:4pt}.callout p:last-child{margin-bottom:0}
.callout.spark{border-left-color:var(--spark)}
.callout.dark{background:var(--forest);border-left-color:var(--lime);color:#E8F0E9}
.callout.dark p,.callout.dark{color:#E8F0E9}
.callout.dark strong{color:var(--lime)}
.chead{background:var(--forest);color:#fff;border-radius:6pt;padding:12pt 14pt;margin-bottom:10pt;display:flex;justify-content:space-between;align-items:flex-start}
.chead .num{font-family:'JetBrains Mono',monospace;font-size:7pt;letter-spacing:.2em;color:var(--lime);margin-bottom:3pt}
.chead h3{font-family:'Playfair Display',serif;font-size:15pt;font-weight:800;line-height:1.1}
.chead .title{font-size:8.4pt;color:#CBD9CE;margin-top:3pt;max-width:330pt}
.chips{text-align:right;min-width:120pt}
.chip{display:inline-block;font-family:'JetBrains Mono',monospace;font-size:6.2pt;letter-spacing:.1em;text-transform:uppercase;padding:2.5pt 6pt;border-radius:8pt;margin:0 0 3pt 3pt;background:rgba(182,217,76,.18);color:#3E6B2E;border:.6pt solid rgba(120,160,60,.5)}
.chip.hot{background:rgba(254,80,0,.13);color:#B23800;border-color:rgba(254,80,0,.45)}
.touch{background:var(--card);border:.8pt solid var(--line2);border-radius:5pt;padding:8pt 11pt;margin-bottom:7pt;page-break-inside:avoid}
.touch .tlabel{font-family:'JetBrains Mono',monospace;font-size:6.4pt;letter-spacing:.16em;text-transform:uppercase;color:var(--green);font-weight:600;margin-bottom:3pt}
.touch .tlabel .day{color:var(--spark)}
.touch .subj{font-weight:700;color:var(--forest);font-size:9.4pt;margin-bottom:4pt;font-family:'DM Sans',sans-serif}
.touch p{margin-bottom:5pt;font-size:8.8pt}
.touch p:last-child{margin-bottom:0}
.touch.live{background:var(--mist);border-color:var(--green)}
.touch.live .tlabel{color:var(--forest)}
.script-line{margin-bottom:4.5pt;font-size:8.8pt;color:var(--ink-soft)}
.script-line em.slab{font-style:normal;font-family:'JetBrains Mono',monospace;font-size:6.6pt;letter-spacing:.08em;text-transform:uppercase;color:var(--green);font-weight:600;display:block;margin-bottom:1pt}
.sig{font-family:'JetBrains Mono',monospace;font-size:7.6pt;color:var(--dim);margin-top:4pt}
"""

COVER_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800;900&family=DM+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
@media print{body{zoom:1.333333}}
html,body{width:6.375in;height:8.25in;overflow:hidden;-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{font-family:'DM Sans',system-ui,sans-serif}
.cover{width:6.375in;height:8.25in;background:linear-gradient(160deg,#0F3322 0%,#16432C 55%,#1B5236 100%);color:#fff;padding:40pt 38pt;position:relative;overflow:hidden}
.cover:before{content:'';position:absolute;right:-120pt;top:-120pt;width:340pt;height:340pt;border-radius:50%;background:radial-gradient(circle,rgba(182,217,76,.14),transparent 65%)}
.logochip{display:inline-block;background:#fff;border-radius:6pt;padding:9pt 14pt;margin-bottom:30pt}
.logochip img{height:22pt;display:block}
.eyebrow{font-family:'JetBrains Mono',monospace;font-size:8pt;letter-spacing:.28em;text-transform:uppercase;color:#B6D94C;font-weight:600;margin-bottom:14pt}
.eyebrow .sp{color:#FE5000}
h1{font-family:'Playfair Display',serif;font-size:31pt;font-weight:900;line-height:1.06;margin-bottom:10pt}
.sub{font-size:12pt;color:#C9D8CD;max-width:400pt;line-height:1.5;margin-bottom:24pt}
.stats{display:flex;gap:9pt;margin-bottom:0}
.stat{background:rgba(255,255,255,.06);border:.8pt solid rgba(182,217,76,.35);border-radius:6pt;padding:9pt 11pt;flex:1}
.stat .v{font-family:'Playfair Display',serif;font-size:15pt;font-weight:800;color:#B6D94C;margin-bottom:2pt}
.stat .v.sp{color:#FF8A50}
.stat .k{font-family:'JetBrains Mono',monospace;font-size:5.8pt;letter-spacing:.10em;text-transform:uppercase;color:#9FB8A6;line-height:1.35}
.foot{position:absolute;bottom:32pt;left:38pt;right:38pt;display:flex;justify-content:space-between;align-items:flex-end;border-top:.8pt solid rgba(255,255,255,.18);padding-top:12pt}
.foot .l{font-size:9pt;color:#C9D8CD;line-height:1.6}
.foot .l strong{color:#fff}
.foot .r{font-family:'JetBrains Mono',monospace;font-size:7pt;letter-spacing:.18em;text-transform:uppercase;color:#9FB8A6;text-align:right;line-height:1.8}
"""

def inline(s):
    s = H.escape(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'`(.+?)`', r'<code>\1</code>', s)
    s = re.sub(r'(?<![\*A-Za-z])\*(?!\s)(.+?)(?<!\s)\*(?![\*A-Za-z])', r'<em>\1</em>', s)
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

def paras(text):
    """Blocks -> <p>, tables, blockquote callouts, and bullet lists.
    Line-aware within a block so a bold lead-in followed by '- ' bullets renders
    as <p> + <ul> (not one run-on paragraph)."""
    out = []
    for blk in re.split(r'\n\n+', text.strip()):
        blk = blk.strip()
        if not blk:
            continue
        if blk.startswith('|'):
            out.append(md_table(blk)); continue
        lines = blk.split('\n')
        if all(l.strip().startswith('> ') or not l.strip() for l in lines):
            inner = ' '.join(l.strip()[2:].strip() for l in lines if l.strip())
            out.append(f'<div class="callout"><p>{inline(inner)}</p></div>'); continue
        buf_text, buf_ul = [], []
        def flush_text():
            if buf_text:
                out.append(f'<p>{inline(" ".join(buf_text))}</p>'); buf_text.clear()
        def flush_ul():
            if buf_ul:
                out.append('<ul>' + ''.join(f'<li>{inline(x)}</li>' for x in buf_ul) + '</ul>'); buf_ul.clear()
        for l in lines:
            s = l.strip()
            if not s:
                continue
            if s.startswith('- '):
                flush_text(); buf_ul.append(s[2:].strip())
            else:
                flush_ul(); buf_text.append(s)
        flush_text(); flush_ul()
    return '\n'.join(out)

# ---- split head vs sections ----
first = re.search(r'\n## ', MD)
head = MD[:first.start()]
rest = MD[first.start():]
sections = {}
order = []
for m in re.finditer(r'\n## (.+?)\n(.*?)(?=\n## |\Z)', rest, re.S):
    name = m.group(1).strip()
    body = re.sub(r'(?m)^\s*---\s*$', '', m.group(2)).strip()  # drop standalone HR separators
    sections[name] = body
    order.append(name)

def find(sub):
    for k in sections:
        if sub.lower() in k.lower():
            return k
    return None

def head_field(label):
    m = re.search(r'\*\*'+re.escape(label)+r'\*\*(.*?)(?:\n\n|\Z)', head, re.S)
    return m.group(1).strip() if m else ''

motion = head_field('Motion:')
ff = head_field('The forcing function:')
ff = ff[0].upper()+ff[1:] if ff else ff          # Jul-29 bug 2: explicit capitalize
thesis = head_field('The one thesis every seat hears:')
thesis = thesis[0].upper()+thesis[1:] if thesis else thesis
merge = head_field('Merge fields:')

pages = []
def sec_page(eyebrow, title, body_html, foot_r):
    return (f'<div class="page"><div class="eyebrow">{H.escape(eyebrow)} <span class="sp">///</span></div>'
            f'<h1 class="sec">{H.escape(title)}</h1>{body_html}'
            f'<div class="foot" style="display:none"></div></div>')

# Page 1: forcing function + thesis + merge
body = f'<div class="callout"><p><strong>Motion.</strong> {inline(motion)}</p></div>'
body += f'<h2 class="sub">The forcing function</h2><p>{inline(ff)}</p>'
body += f'<div class="callout dark"><p><strong>The one thesis every seat hears.</strong> {inline(thesis)}</p></div>'
if merge:
    body += f'<div class="callout spark"><p><strong>Merge fields.</strong> {inline(merge)}</p></div>'
pages.append(sec_page('COST-MANDATE MOTION '+MID+' ONE-OFF STRIKE ROOM', 'Why BMO, why now', body, ''))

# Snapshot
k = find('Account snapshot')
pages.append(sec_page('ACCOUNT INTELLIGENCE', 'Account snapshot', paras(sections[k]), ''))

# Committee
k = find('Buying committee')
pages.append(sec_page('EIGHT SEATS, ONE THESIS', 'Buying committee', paras(sections[k]), ''))

# Guardrails
k = find('can and cannot say')
pages.append(sec_page('GUARDRAILS', 'What reps can and cannot say', paras(sections[k]), ''))

# Cadence
k = find('Cadence')
pages.append(sec_page('CHOREOGRAPHY', 'Cadence and committee entry', paras(sections[k]), ''))

# ---- contacts ----
seq = sections[find('Sequences')]
contacts = re.split(r'\n### ', '\n'+seq)[1:]
NC = len(contacts)
for c in contacts:
    header = c.split('\n', 1)[0].strip()
    rest_c = c.split('\n', 1)[1] if '\n' in c else ''
    hm = re.match(r'(\d+)\.\s+(.+?)\s+--\s+(.+)', header)
    num, name, titleline = hm.group(1), hm.group(2), hm.group(3)
    bits = [b.strip() for b in titleline.split(MID)]
    title = bits[0]
    chips = []
    for b in bits[1:]:
        if '@' in b or 'email' in b.lower() or 'queues' in b.lower() or 'no verified' in b.lower():
            if 'LinkedIn-led' in b:
                chips.append(('LinkedIn-led', False));
            continue
        if b.lower().startswith('tier'):
            chips.append((re.sub(r'\s*\(.*', '', b), False))
        elif b.lower().startswith('enters'):
            chips.append((b, False))
        elif 'EXTENDED' in b or 'must-win' in b:
            chips.append(('EXTENDED ARC', True))
    seen=set(); uchips=[]
    for txt,hot in chips:
        if txt not in seen:
            seen.add(txt); uchips.append((txt,hot))
    chip_html = ''.join(f'<span class="chip{" hot" if hot else ""}">{H.escape(t)}</span>' for t,hot in uchips)

    touches = re.split(r'\n\*\*(Touch [^*]+)\*\*', rest_c)
    cards = []
    for i in range(1, len(touches), 2):
        label = touches[i].strip()
        content = touches[i+1].strip()
        live = any(x in label for x in ('If they answer', 'live script', 'Live call', 'full script', 'Call #'))
        lab = H.escape(label).upper().replace(' -- ', ' '+MID+' ')
        lab = re.sub(r'\(DAY (\d+)\)', MID+r' <span class="day">DAY \1</span>', lab)  # raw \1 backref
        subj = ''
        sm = re.match(r'Subject:\s*(.+?)(\n|$)', content)
        if sm:
            subj = f'<div class="subj">Subject: {inline(sm.group(1).strip())}</div>'
            content = content[sm.end():].strip()
        if live:
            lines = []
            for ln in re.split(r'\n\n+', content):
                ln = ln.strip()
                lm = re.match(r'\*(.+?):\*\s*(.*)', ln, re.S)
                if lm:
                    lines.append(f'<div class="script-line"><em class="slab">{H.escape(lm.group(1))}</em>{inline(lm.group(2).strip())}</div>')
                elif ln:
                    lines.append(f'<div class="script-line">{inline(ln)}</div>')
            body_html = '\n'.join(lines)
        else:
            tok = re.search(r'\{\{(sender(?:_full_name)?)\}\}\s*$', content)
            if tok:
                sigtok = tok.group(1)
                content = content[:tok.start()].strip()
                body_html = paras(content) + f'<div class="sig">{{{{{sigtok}}}}}</div>'
            else:
                body_html = paras(content)
        cards.append(f'<div class="touch{" live" if live else ""}"><div class="tlabel">{lab}</div>{subj}{body_html}</div>')
    chead = (f'<div class="chead"><div><div class="num">CONTACT {num} OF {NC}</div>'
             f'<h3>{H.escape(name)}</h3><div class="title">{H.escape(title)}</div></div>'
             f'<div class="chips">{chip_html}</div></div>')
    pages.append(f'<div class="page">{chead}{"".join(cards)}'
                 f'<div class="foot" style="display:none"></div></div>')

# Objections
k = find('Objection')
pages.append(sec_page('WHEN THEY PUSH BACK', 'Objection quick-handles', paras(sections[k]), ''))

# Claims + execution notes on one page
k = find('Claims basis')
cl = paras(sections[k])
ke = find('Execution notes')
if ke:
    cl += '<h2 class="sub">Execution notes</h2>' + paras(sections[ke])
pages.append(sec_page('RECEIPTS', 'Claims basis and execution notes', cl, ''))

body_html = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{"".join(pages)}</body></html>'
open('body.html','w').write(body_html)

cover_html = f'''<!doctype html><html><head><meta charset="utf-8"><style>{COVER_CSS}</style></head><body>
<div class="cover">
<div class="logochip"><img src="data:image/svg+xml;base64,{LOGO_B64}"></div>
<div class="eyebrow">COST-MANDATE MOTION <span class="sp">///</span> ONE-OFF STRIKE ROOM</div>
<h1>Bank of Montreal</h1>
<div class="sub">Buying-committee strike sequences for the half of BMO's roughly $250M efficiency mandate that cannot come from another cut, the capacity already sitting between the forecast and the floor.</div>
<div class="stats">
<div class="stat"><div class="v">$202M</div><div class="k">Pre-tax severance, Q1 FY2026 (their release, Feb 25)</div></div>
<div class="stat"><div class="v">~$250M</div><div class="k">Annualized savings target, half due FY2026 (their CFO)</div></div>
<div class="stat"><div class="v">8 seats</div><div class="k">Committee sequenced, 1 extended arc, emails ZB-gated</div></div>
<div class="stat"><div class="v sp">Aug 25</div><div class="k">Q3 FY2026 reports, the live window</div></div>
</div>
<div class="foot">
<div class="l"><strong>Prepared for Nathan Belfield</strong><br>Dallas Andrews {MID} GTM Engineering</div>
<div class="r">JULY 29 2026<br>DRAFT {MID} HUMAN GATE ON</div>
</div>
</div></body></html>'''
open('cover.html','w').write(cover_html)
print('html built:', len(pages), 'body pages')

# ---- render both with playwright ----
from playwright.sync_api import sync_playwright
import os
cwd = os.getcwd()
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    for name, margin in [('cover', {'top':'0','bottom':'0','left':'0','right':'0'}),
                         ('body', {'top':'0.35in','bottom':'0.35in','left':'0','right':'0'})]:
        pg.goto(f'file://{cwd}/{name}.html')
        pg.wait_for_timeout(2500)
        pg.pdf(path=f'{name}.pdf', format='Letter', margin=margin, print_background=True)
    b.close()
print('rendered cover.pdf + body.pdf')

# ---- merge + stamp page numbers (cover = page 1) ----
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
cov, bod = PdfReader('cover.pdf'), PdfReader('body.pdf')
total = len(cov.pages) + len(bod.pages)
buf = io.BytesIO(); cnv = canvas.Canvas(buf, pagesize=letter)
for i in range(len(bod.pages)):
    cnv.setFont('Courier', 6.5); cnv.setFillColorRGB(0.48,0.53,0.49)
    cnv.drawString(42, 16, f'INTRADIEM . GTM ENGINEERING - {ACCOUNT_TAG} STRIKE ROOM')
    cnv.drawRightString(570, 16, f'PAGE {i+2} OF {total}'); cnv.showPage()
cnv.save(); buf.seek(0)
overlay = PdfReader(buf); w = PdfWriter(); w.add_page(cov.pages[0])
for i, pgp in enumerate(bod.pages):
    pgp.merge_page(overlay.pages[i]); w.add_page(pgp)
with open(OUT_PDF,'wb') as f: w.write(f)
print('WROTE', OUT_PDF, '->', total, 'pages')
