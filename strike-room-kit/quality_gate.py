#!/usr/bin/env python3
"""Strike-room copy quality gate. Proven on Bell + BMO, Jul 29 2026.

RUN: python3 quality_gate.py <packet.md>

Checks, in order:
  1. em-dashes in PROSPECT PROSE only (structural markdown headers/labels/tables
     are the house convention and are correctly excluded — an unscoped em-dash
     count reports ~69 false positives and tells you nothing)
  2. humility clause used at most once across the whole committee
  3. banned terms inside the ## Sequences block only (guardrail sections legitimately
     name the things the copy may not say)
  4. subject-line uniqueness ('leaving it here' on breakups is the convention)
  5. word counts: Touch-1 email 80-120, voicemail 45-70, LinkedIn 40-80
  6. every voicemail has a live-answer script behind it
  7. TEMPLATE CREEP: substantive shared 8-grams between every pair of contacts,
     with intentional scaffolding excluded. THIS IS THE CHECK THAT FINDS REAL
     DEFECTS. On BMO it caught six of seven Touch-1 emails closing on a near-
     identical product paragraph, and two seats sharing the same hail-mary.
     Word counts and banned-word scans found nothing; this found three things.
"""
import re, sys, itertools, collections

MD = sys.argv[1] if len(sys.argv) > 1 else 'packet.md'
txt = open(MD).read()
fails = []

# scaffolding that is SUPPOSED to be identical across seats
BOILERPLATE = [
    'live answer script', 'breakup email', 'with intradiem i sent',
    'the email is easy to reply', 'thirty seconds', 'am at and the email',
    'left a voicemail', 'left you a voicemail', 'work around your calendar',
    'if he picks up', 'if she picks up', 'twenty minutes', 'i will let you go',
    'one question and i', 'tell me whether to keep going', 'the short version is',
    'a voicemail too the short version', 'a voicemail as well the short version',
    'and i will stop if he pushes', 'minutes and i will stop',
]

print(f"QUALITY GATE — {MD}\n" + "=" * 60)

# 1. em-dash, prose only
prose = [l for l in txt.split('\n') if not l.strip().startswith(('#', '|', '**', '- ', '*'))]
em = sum(l.count('—') for l in prose)
print(f"[1] em-dash in prospect prose: {em}")
if em: fails.append(f"{em} em-dash in prose")

# 2. humility clause
h = [l for l in txt.split('\n') if re.search(r'better than I do from the outside|you know your own', l, re.I)]
print(f"[2] humility clause: {len(h)} (max 1)")
if len(h) > 1: fails.append("humility clause used more than once")

seq = txt[txt.index('## Sequences'):txt.index('## Objection quick-handles')]

# 3. banned in copy
BAN = {
    'platform-headcount (350k)': r'350[, ]?000',
    'net retention / NRR':       r'114\s?%|net retention',
    'idle-time stat':            r'idle[- ]time',
    'Greenlight/Zuar CTO':       r'\bCTO\b',
    '$529.6M savings':           r'529\.6',
    'Humana in a cold touch':    None,   # handled below
}
print("[3] banned terms in prospect copy:")
for k, p in BAN.items():
    if p is None: continue
    n = len(re.findall(p, seq))
    print(f"      {k:26s} {n}")
    if n: fails.append(f"{k} appears in copy")

# customer names: none may appear in copy (Humana allowed in objection handles only)
CUSTOMERS = ['RBC', 'Royal Bank', 'CIBC', 'Canadian Imperial', 'TD Bank', 'Rogers',
             'JPMorgan', 'Wells Fargo', 'Citicorp', 'PNC', 'US Bancorp', 'TIAA',
             'Humana', 'Aetna', 'CVS', 'UnitedHealth', 'Cigna', 'Elevance', 'MetLife',
             'Goldman', 'Charter', 'AT&T', 'Kaiser', 'Synchrony', 'Assurant', 'Molina']
named = [c for c in CUSTOMERS if re.search(re.escape(c), seq, re.I)]
print(f"      {'customer names in copy':26s} {named if named else 'none'}")
if named: fails.append(f"customer named in prospect copy: {named}")

# 4. subjects
subs = re.findall(r'^Subject: (.+)$', txt, re.M)
c = collections.Counter(subs)
dupes = {s: n for s, n in c.items() if n > 1 and s != 'leaving it here'}
print(f"[4] subjects: {len(subs)} total / {len(c)} unique; non-breakup reuse: {dupes or 'none'}")
if dupes: fails.append(f"subject reuse: {dupes}")

# 5 + 6. per-contact
secs = re.split(r'\n### \d+\. ', seq)[1:]
print("[5] word counts:")
for s in secs:
    who = s.split('\n')[0].split('—')[0].strip()[:22]
    parts = re.split(r'\n\*\*(Touch [^*]+)\*\*\n', s)
    for i in range(1, len(parts), 2):
        lab, body = parts[i], re.split(r'\n\*\*|\n---|\n### ', parts[i + 1])[0]
        b = re.sub(r'\{\{sender\}\}|\[number\]|^Subject:.*$', '', body, flags=re.M).strip()
        n = len([w for w in b.split() if w])
        if 'Touch 1' in lab and 'Email' in lab:        lo, hi, t = 80, 120, 'Email'
        elif 'Voicemail' in lab:                       lo, hi, t = 45, 70, 'Voicemail'
        elif 'connection request' in lab:              lo, hi, t = 40, 80, 'LI conn'
        elif 'LinkedIn message' in lab:                lo, hi, t = 40, 80, 'LI msg'
        else: continue
        ok = lo <= n <= hi
        print(f"      {'OK ' if ok else 'FAIL'} {who:22s} {t:9s} {n:3d}w ({lo}-{hi})")
        if not ok: fails.append(f"{who} {t}={n}w, need {lo}-{hi}")

print("[6] voicemail / live-answer pairing:")
for s in secs:
    who = s.split('\n')[0].split('—')[0].strip()[:22]
    vm, la = len(re.findall(r'Voicemail\*\*', s)), len(re.findall(r'Live-answer script', s))
    print(f"      {'OK ' if vm == la else 'FAIL'} {who:22s} vm={vm} live={la}")
    if vm != la: fails.append(f"{who}: {vm} voicemail / {la} live-answer")

# 7. template creep — the check that matters
def nrm(t):
    t = re.sub(r'\{\{sender\}\}|\[number\]', '', t)
    return [w for w in re.sub(r'[^a-z ]', ' ', t.lower()).split() if w]

C = {s.split('\n')[0].split('—')[0].strip(): s for s in secs}
G = {n: set(tuple(nrm(v)[i:i + 8]) for i in range(len(nrm(v)) - 7)) for n, v in C.items()}
tot = 0
print("[7] substantive shared 8-grams (scaffolding excluded):")
for a, b in itertools.combinations(C, 2):
    ov = [" ".join(x) for x in G[a] & G[b]]
    ov = [o for o in ov if not any(bp in o for bp in BOILERPLATE)]
    if ov:
        tot += len(ov)
        print(f"      {a} <-> {b}: {len(ov)}")
        for o in ov[:3]: print(f"          {o}")
print(f"      total across all pairs: {tot}  (target: 0)")
if tot: fails.append(f"{tot} substantive shared phrases between seats")

print("\n" + "=" * 60)
print("QUALITY GATE: " + ("PASS" if not fails else "FAIL"))
for f in fails: print("  - " + f)
sys.exit(1 if fails else 0)
