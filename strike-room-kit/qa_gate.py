#!/usr/bin/env python3
import re, sys

PATH = "/Users/intradiemDA/Claude/Projects/Intradiem GTM Engineer/CostMandate_BMO_StrikeRoom_Sequence_v1.md"
md = open(PATH).read()

problems = []
notes = []

# ---- em dashes / en dashes (hard rule: zero em dashes anywhere) ----
em = md.count("—")
en = md.count("–")
print(f"EM-DASH (U+2014) count: {em}  {'OK' if em==0 else 'FAIL'}")
print(f"EN-DASH (U+2013) count: {en}  (informational)")
if em: problems.append(f"{em} em dashes present")

# ---- banned words / phrases ----
banned = ["leverage","synergy","seamless","robust","transform","transformation","empower",
          "best-in-class","cutting-edge","comprehensive","innovative","paradigm","catalyst",
          "circle back","touch base","pick your brain","compare notes","at the end of the day",
          "companies like yours","plans your size","leaders in your space","I help organizations"]
print("\n--- banned word/phrase scan ---")
any_ban=False
for b in banned:
    hits = [m.start() for m in re.finditer(re.escape(b), md, re.I)]
    if hits:
        any_ban=True
        print(f"  BANNED '{b}': {len(hits)}x")
        problems.append(f"banned '{b}' x{len(hits)}")
if not any_ban: print("  clean")

# ---- cliche 'reach out' family (sharpener flags it) ----
print("\n--- 'reach(ed) out' scan (sharpener cliche) ---")
ro = [m.group(0) for m in re.finditer(r'\breach(?:ed|ing)?\s+out\b', md, re.I)]
print(f"  count: {len(ro)}")
if ro: notes.append(f"'reach out' family x{len(ro)} (review)")

# ---- humility clause count (must be <=1 across committee) ----
print("\n--- humility clause scan (<=1 across committee) ---")
hum_pat = re.compile(r'(better than I|you.?ll (?:know|see)|far better than|exact (?:internal )?picture)', re.I)
# count DISTINCT sentences containing a humility marker (one clause can trip 2 patterns)
sentences = re.split(r'(?<=[.?!])\s+', md)
hum_sents = [sent.strip()[:80] for sent in sentences if hum_pat.search(sent)]
print(f"  humility sentences: {len(hum_sents)} -> {hum_sents}")
if len(hum_sents) > 1: problems.append(f"humility clause in {len(hum_sents)} sentences (max 1)")

# ---- isolate the Sequences section and parse contacts/touches ----
seq = md.split("## Sequences",1)[1].split("## Objection quick-handles",1)[0]
contacts = re.split(r'\n### ', seq)[1:]
print(f"\n--- parsed {len(contacts)} contacts ---")

def wc(s): return len(re.findall(r"\S+", s))

intradiem_in_early = []
touch1_emails=[]; voicemails=[]; linkedins=[]; other_emails=[]
for c in contacts:
    header = c.split("\n",1)[0]
    name = header.split(" -- ")[0].strip()
    touches = re.split(r'\n\*\*(Touch [^*]+)\*\*', c)
    for i in range(1,len(touches),2):
        label = touches[i].strip()
        body = touches[i+1].strip()
        # day number
        dm = re.search(r'Day (\d+)', label)
        day = int(dm.group(1)) if dm else None
        # strip subject + signature tokens for word count
        b = re.sub(r'^Subject:[^\n]*\n?', '', body).strip()
        b = re.sub(r'\{\{sender(?:_full_name)?\}\}', '', b).strip()
        # for live scripts strip the *Label:* markers
        b_words = re.sub(r'\*[^*]+:\*', '', b)
        n = wc(b_words)
        kind=None
        if 'If they answer' in label or 'live script' in label or 'Live call' in label:
            kind='live'
        elif 'Voicemail' in label:
            kind='vm'; voicemails.append((name,label,n))
        elif 'connection request' in label:
            kind='li'; linkedins.append((name,label,n))
        elif 'LinkedIn message' in label:
            kind='li'; linkedins.append((name,label,n))
        elif 'Email' in label:
            if 'Touch 1' in label: touch1_emails.append((name,label,n))
            else: other_emails.append((name,label,n))
        # Intradiem in Days 1-5 non-voicemail/non-live?
        if day is not None and day<=5 and re.search(r'Intradiem', b):
            if kind not in ('vm','live'):
                intradiem_in_early.append((name,label))

print("\n--- Touch 1 email word counts (target 80-120) ---")
for name,label,n in touch1_emails:
    ok = 80<=n<=120
    print(f"  {name:16} {n:4}  {'OK' if ok else 'FAIL'}")
    if not ok: problems.append(f"Touch1 {name} {n}w out of 80-120")

print("\n--- follow-up/breakup email word counts (target <=150) ---")
for name,label,n in other_emails:
    ok = n<=150
    tag = label.split(' -- ')[0] if ' -- ' in label else label
    print(f"  {name:16} {label[:22]:22} {n:4}  {'OK' if ok else 'CHECK'}")
    if n>150: problems.append(f"email {name} {label} {n}w >150")

print("\n--- voicemail word counts (target 45-70) ---")
for name,label,n in voicemails:
    ok = 45<=n<=70
    print(f"  {name:16} {n:4}  {'OK' if ok else 'FAIL'}")
    if not ok: problems.append(f"voicemail {name} {n}w out of 45-70")

print("\n--- LinkedIn word counts (target 40-80) ---")
for name,label,n in linkedins:
    ok = 40<=n<=80
    print(f"  {name:16} {label[:26]:26} {n:4}  {'OK' if ok else 'FAIL'}")
    if not ok: problems.append(f"LinkedIn {name} {label[:20]} {n}w out of 40-80")

print("\n--- Intradiem named in a Day 1-5 email/LinkedIn (brand-light) ---")
if intradiem_in_early:
    for name,label in intradiem_in_early:
        print(f"  FLAG {name} {label}")
        problems.append(f"Intradiem in early {name} {label}")
else:
    print("  clean (voicemail/live-script caller-ID uses are allowed per strike-sequence reference)")

# ---- subject-line uniqueness (breakups may share 'leaving it here') ----
print("\n--- subject lines ---")
subs = re.findall(r'Subject:\s*(.+)', md)
from collections import Counter
cnt = Counter(s.strip().lower() for s in subs)
for s,c in cnt.items():
    flag = '' if (c==1 or 'leaving it here' in s) else '  <-- DUP (non-breakup)'
    print(f"  {c}x  {s}{flag}")
    if c>1 and 'leaving it here' not in s: problems.append(f"dup subject '{s}'")

print("\n"+"="*50)
if problems:
    print("QA RESULT: ISSUES")
    for p in problems: print("  - "+p)
else:
    print("QA RESULT: PASS (all hard checks)")
if notes:
    print("REVIEW NOTES:")
    for nn in notes: print("  * "+nn)
