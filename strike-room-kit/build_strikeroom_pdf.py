#!/usr/bin/env python3
"""GENERALISED green-kit strike-room PDF builder.

Proven on Bell Canada and BMO (Jul 29 2026). Supersedes build_pdf_TEMPLATE.py,
which is hard-wired to the Aflac markdown structure and will crash on any
document that uses `### The forcing function` headers instead of inline bold.

WHAT TO EDIT PER ACCOUNT: only the CONFIG block below. Nothing else.

REQUIRES in the same dir: kit.css, kit_cover.css, logo.svg, render.py, the packet .md
RUN: python3 build_strikeroom_pdf.py && python3 render.py   then merge+stamp per README

INPUT CONTRACT — the .md must use the Bell/BMO section structure:
  sections separated by `---`, in this order:
  [0] title/meta  [1] ## Account snapshot  [2] ## Buying committee
  [3] ## What reps can and cannot say  [4] ## Cadence and committee choreography
  [5] ## Sequences + contact 1   [6..n] one `### N. Name — Title` per contact
  [n+1] ## Objection quick-handles  [n+2] ## Claims basis  [n+3] ## Pre-send gates
  Touch lines must read: **Touch N (Day X) — Channel**

TWO BUGS FOUND AND FIXED Jul 29 2026 — DO NOT REINTRODUCE:
  1. The touch label must use the literal '·' character. The old template built
     the label with the HTML entity `&middot;` and then ran .upper() on it LAST,
     which produced '&MIDDOT;' and printed it as literal text in the PDF.
     Fix: literal char, and NO Python .upper() anywhere — CSS text-transform
     does the uppercasing.
  2. The Hook line starts lowercase in the md (it follows 'Hook: '). Capitalise
     the first letter explicitly or the callout reads as a sentence fragment.
  Both were invisible in the HTML and obvious in a PNG render. ALWAYS render two
  or three pages to PNG and actually look at them before shipping.
"""

# ============================ CONFIG — EDIT THIS ONLY ============================
MD_FILE   = 'CostMandate_TELUS_StrikeRoom_Sequence_v1.md'
ACCOUNT   = 'TELUS'
SEAT_COUNT = 8
COVER = dict(
    eyebrow  = 'Cost-Mandate Motion <span class="sp">///</span> New Logo',
    h1       = 'TELUS<br>Strike Room',
    sub      = 'EDIT ME: two or three sentences stating the forcing function in the '
               'prospect\'s own disclosed terms, with the deadline that makes it urgent.',
    stats    = [('$0M', 'edit me'), ('Mon 00', 'edit me'),
                ('8 / 8', 'Seats, ZeroBounce valid'), ('00', 'edit me', 'sp')],
    foot_l   = '<strong>Requested by Nathan Belfield</strong><br>July 29 2026 · Account 3 of 3',
    foot_r   = 'Built [DATE]<br>Nothing sends without approval',
)
SECTION_TITLES = [
    ('Why this account, why now', 'EDIT ME: the forcing function in one line', 'ACCOUNT SNAPSHOT'),
    ('Who we are reaching',        'EDIT ME: the committee in one line',       'BUYING COMMITTEE'),
    ('Claims discipline',          'What reps can and cannot say',             'GUARDRAILS'),
    ('How it runs',                'Cadence and committee choreography',       'CHOREOGRAPHY'),
    ('When they push back',        'Objection quick-handles',                  'OBJECTIONS'),
    ('Every number, sourced',      'Claims basis',                             'CLAIMS BASIS'),
    ('Before anything sends',      'Pre-send gates',                           'PRE-SEND GATES'),
]
# ================================ END CONFIG ====================================


import re, base64, html as H

MD = open(MD_FILE).read()
LOGO_B64 = base64.b64encode(open('logo.svg').read().encode()).decode()

CSS = open('kit.css').read()
COVER_CSS = open('kit_cover.css').read()

# ---------------- inline + block renderers ----------------

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
        if set(r.replace('|', '').strip()) <= set('-: '):
            continue
        cells = [c.strip() for c in r.strip().strip('|').split('|')]
        tag = 'th' if i == 0 else 'td'
        out.append('<tr>' + ''.join(f'<{tag}>{inline(c)}</{tag}>' for c in cells) + '</tr>')
    out.append('</table>')
    return '\n'.join(out)

def render_block(text):
    """Sections: ### subheads, tables, bullets, numbered lists, blockquotes, paras."""
    out = []
    for blk in re.split(r'\n\n+', text.strip()):
        b = blk.strip()
        if not b:
            continue
        if b.startswith('### '):
            head, *rest = b.split('\n')
            out.append(f'<h2 class="sub">{inline(head[4:].strip())}</h2>')
            if rest:
                out.append(render_block('\n'.join(rest)))
        elif b.startswith('## '):
            head, *rest = b.split('\n')
            out.append(f'<h2 class="sub">{inline(head[3:].strip())}</h2>')
            if rest:
                out.append(render_block('\n'.join(rest)))
        elif b.startswith('|'):
            out.append(md_table(b))
        elif b.startswith('> '):
            body = ' '.join(l.lstrip('> ').strip() for l in b.split('\n'))
            out.append(f'<div class="callout"><p>{inline(body)}</p></div>')
        elif re.match(r'^-\s', b):
            items = re.split(r'\n(?=-\s)', b)
            stripped = [re.sub(r'^-\s+', '', i.strip()) for i in items]
            lis = ''.join('<li>' + inline(s) + '</li>' for s in stripped)
            out.append(f'<ul>{lis}</ul>')
        elif re.match(r'^\d+\.\s', b):
            items = re.split(r'\n(?=\d+\.\s)', b)
            stripped = [re.sub(r'^\d+\.\s+', '', i.strip()) for i in items]
            lis = ''.join('<li>' + inline(s) + '</li>' for s in stripped)
            out.append(f'<ol>{lis}</ol>')
        else:
            out.append(f'<p>{inline(b)}</p>')
    return '\n'.join(out)

# ---------------- contact pages ----------------

LIVE_MARKERS = ('Live-answer', 'full script', 'Call #')

def render_touch(label, body):
    """One touch card. label e.g. 'Touch 3 (Day 4) - Voicemail'."""
    # BUG 1 FIX: literal middot, and no Python .upper() anywhere.
    m = re.match(r'(Touch \d+)\s*\((Day \d+)\)\s*[—\-]\s*(.+)', label.strip())
    if m:
        lab = (f'{m.group(1)} <span class="day">· {m.group(2)} ·</span> '
               f'{m.group(3)}')
    else:
        lab = inline(label.strip())

    live = any(k in label for k in LIVE_MARKERS)
    parts = [f'<div class="touch{" live" if live else ""}">',
             f'<div class="tlabel">{lab}</div>']

    for blk in re.split(r'\n\n+', body.strip()):
        b = blk.strip()
        if not b:
            continue
        if b.startswith('Subject:'):
            parts.append(f'<div class="subj">{inline(b[8:].strip())}</div>')
        elif b == '{{sender}}':
            parts.append('<p class="sig">{{sender}}</p>')
        elif re.match(r'^\*[^*]+:\*', b):
            # stage direction, e.g. *Opener:* text
            sm = re.match(r'^\*([^*]+):\*\s*(.*)$', b, re.S)
            parts.append(f'<div class="script-line"><em class="slab">{inline(sm.group(1))}</em>'
                         f'{inline(sm.group(2).strip())}</div>')
        else:
            parts.append(f'<p>{inline(b)}</p>')
    parts.append('</div>')
    return '\n'.join(parts)

def render_contact(raw, idx):
    lines = raw.strip().split('\n')
    headline = lines[0].strip()
    num_name, _, title = headline.partition('—')
    num, _, name = num_name.strip().partition('.')
    rest = '\n'.join(lines[1:])

    # tier / entry line
    tier = ''
    tm = re.search(r'^\*\*(.+?)\*\*$', rest, re.M)
    if tm:
        tier = tm.group(1)
        rest = rest.replace(tm.group(0), '', 1)

    chips = []
    for pat, cls in [(r'Tier (\d)', ''), (r'(Entry Day \d+)', ''),
                     (r'(Extended arc)', 'hot'), (r'(LinkedIn.only)', 'hot'),
                     (r'(humility clause)', 'hot')]:
        cm = re.search(pat, tier, re.I)
        if cm:
            txt = cm.group(0) if pat.startswith(r'Tier') else cm.group(1)
            chips.append(f'<span class="chip {cls}">{H.escape(txt)}</span>')
    role = re.search(r'Tier \d,\s*([^.]+)\.', tier)
    if role:
        chips.insert(1, f'<span class="chip">{H.escape(role.group(1).strip())}</span>')

    # hook
    hook_html = ''
    hm = re.search(r'^Hook:\s*(.+?)(?=\n\n)', rest, re.S | re.M)
    if hm:
        hook = ' '.join(hm.group(1).split())
        hook = hook[0].upper() + hook[1:]   # BUG 2 FIX
        hook_html = f'<div class="callout"><p><strong>Hook.</strong> {inline(hook)}</p></div>'
        rest = rest.replace(hm.group(0), '', 1)

    touches = []
    parts = re.split(r'\n\*\*(Touch [^*]+)\*\*\n', rest)
    lead = parts[0].strip()
    lead_html = render_block(lead) if lead and not lead.startswith('Hook:') else ''
    for i in range(1, len(parts), 2):
        touches.append(render_touch(parts[i], parts[i + 1]))

    return f'''<div class="page">
<div class="chead">
  <div><div class="num">SEAT {num.strip()} OF {SEAT_COUNT}</div>
  <h3>{H.escape(name.strip())}</h3>
  <div class="title">{H.escape(title.strip())}</div></div>
  <div class="chips">{''.join(chips)}</div>
</div>
{hook_html}
{lead_html}
{''.join(touches)}
<div class="foot"><span>INTRADIEM · GTM ENGINEERING</span><span>{H.escape(name.strip())}</span></div>
</div>'''

# ---------------- assemble ----------------

m = re.split(r'\n---\n', MD)
head, snapshot, committee, cansay, cadence = m[0], m[1], m[2], m[3], m[4]
seq_intro = m[5]
contacts_raw = [seq_intro.split('## Sequences')[1]] + m[6:13]
objections, claims, gates = m[13], m[14], m[15]

def sec_page(eyebrow, title, body_html, foot_r):
    return (f'<div class="page"><div class="eyebrow">{eyebrow} <span class="sp">///</span></div>'
            f'<h1 class="sec">{title}</h1>{body_html}'
            f'<div class="foot"><span>INTRADIEM · GTM ENGINEERING</span>'
            f'<span>{foot_r}</span></div></div>')

pages = []
_S = SECTION_TITLES
pages.append(sec_page(_S[0][0], _S[0][1], render_block(snapshot.split('## Account snapshot')[1]), _S[0][2]))
pages.append(sec_page(_S[1][0], _S[1][1], render_block(committee.split('## Buying committee')[1]), _S[1][2]))
pages.append(sec_page(_S[2][0], _S[2][1], render_block(cansay.split('## What reps can and cannot say')[1]), _S[2][2]))
pages.append(sec_page(_S[3][0], _S[3][1], render_block(cadence.split('## Cadence and committee choreography')[1]), _S[3][2]))

first = contacts_raw[0]
first = first[first.index('### ') + 4:]
pages.append(render_contact(first, 1))
for i, c in enumerate(contacts_raw[1:], start=2):
    pages.append(render_contact(c.strip()[4:], i))

pages.append(sec_page(_S[4][0], _S[4][1], render_block(objections.split('## Objection quick-handles')[1]), _S[4][2]))
pages.append(sec_page(_S[5][0], _S[5][1], render_block(claims.split('## Claims basis')[1]), _S[5][2]))
pages.append(sec_page(_S[6][0], _S[6][1], render_block(gates.split('## Pre-send gates')[1]), _S[6][2]))

open('body.html', 'w').write(
    f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>'
    f'<body>{"".join(pages)}</body></html>')

_tiles = ''.join(
    f'<div class="stat"><div class="v{" sp" if len(t)>2 else ""}">{t[0]}</div>'
    f'<div class="k">{t[1]}</div></div>' for t in COVER['stats'])
COVER_HTML = f'''<!doctype html><html><head><meta charset="utf-8"><style>{COVER_CSS}</style></head><body>
<div class="cover">
  <div class="logochip"><img src="data:image/svg+xml;base64,{LOGO_B64}"></div>
  <div class="eyebrow">{COVER['eyebrow']}</div>
  <h1>{COVER['h1']}</h1>
  <div class="sub">{COVER['sub']}</div>
  <div class="stats">{_tiles}</div>
  <div class="foot"><div class="l">{COVER['foot_l']}</div><div class="r">{COVER['foot_r']}</div></div>
</div></body></html>'''
open('cover.html', 'w').write(COVER_HTML)
print(f'built body.html ({len(pages)} pages) + cover.html for {ACCOUNT}')
