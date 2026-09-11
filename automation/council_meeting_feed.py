#!/usr/bin/env python3
"""Monthly meeting feed for the Pipeline Council, in Genna's Cold outreach data schema
(Name | Account | Date of Meeting | Category | AE | ISR | Meeting Complete | Status | Source | Stage | Channel).
Sources: impact/outcomes.csv (type = meeting), automation/logs/credit_pipeline_receipts.md (booked-meeting lines),
automation/logs/meeting-capture-*.md (Name, AE, Status when present). Source and Channel are always GTM Engineering.
Category = Anchor for TAM tier A accounts (tam-outbound-engine/data/tam_accounts.csv tier column when present), Core otherwise.
Usage: council_meeting_feed.py --month 2026-09 [--out <csv>]   (read-only, writes one CSV)"""
import csv,os,sys,re,glob,datetime
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN='/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer'
month=sys.argv[sys.argv.index('--month')+1] if '--month' in sys.argv else datetime.date.today().strftime('%Y-%m')
out=sys.argv[sys.argv.index('--out')+1] if '--out' in sys.argv else os.path.join(ROOT,'motions','pipeline_council',f'GTM_Engineering_Meetings_{month}.csv')
COLS=['Name','Account','Date of Meeting','Category','AE','ISR','Meeting Complete','Status','Source','Stage','Channel']
tier={}
tp=os.path.join(ROOT,'tam-outbound-engine','data','tam_accounts.csv')
if os.path.exists(tp):
    for r in csv.DictReader(open(tp)):
        t=(r.get('tier') or r.get('Tier') or '').strip().upper(); d=(r.get('domain') or '').lower(); n=(r.get('account') or r.get('company') or r.get('name') or '').lower()
        if t: tier[d]=t; tier[n]=t
rows=[]
op=os.path.join(ROOT,'impact','outcomes.csv')
for r in csv.DictReader(open(op)) if os.path.exists(op) else []:
    if (r.get('type') or '').strip().lower()!='meeting' or not (r.get('date') or '').startswith(month): continue
    note=r.get('note') or ''
    def pick(k):
        m=re.search(k+r'\s*[:=]\s*([^;|]+)',note,re.I); return m.group(1).strip() if m else ''
    acct=r.get('account') or ''
    rows.append({'Name':pick('name') or pick('contact'),'Account':acct,'Date of Meeting':r['date'],'Category':'Anchor' if tier.get(acct.lower())=='A' else 'Core','AE':pick('ae'),'ISR':pick('isr') or 'Nate','Meeting Complete':pick('complete') or '','Status':pick('status') or 'Scheduled','Source':'GTM Engineering','Stage':pick('stage') or '','Channel':'GTM Engineering'})
rp=os.path.join(MAIN,'automation','logs','credit_pipeline_receipts.md')
if os.path.exists(rp):
    for l in open(rp):
        m=re.match(r'^\|\s*(\d{4}-\d{2}-\d{2})\s*\|(.+)\|\s*$',l.strip())
        if not m or not m.group(1).startswith(month): continue
        cells=[c.strip() for c in m.group(2).split('|')]
        if not any(re.search(r'meeting (booked|held|set)',c,re.I) for c in cells): continue
        acct=cells[0] if cells else ''
        if any(x['Account']==acct and x['Date of Meeting']==m.group(1) for x in rows): continue
        rows.append({'Name':'','Account':acct,'Date of Meeting':m.group(1),'Category':'Anchor' if tier.get(acct.lower())=='A' else 'Core','AE':'','ISR':'Nate','Meeting Complete':'','Status':'Scheduled','Source':'GTM Engineering','Stage':'','Channel':'GTM Engineering'})
os.makedirs(os.path.dirname(out),exist_ok=True)
w=csv.DictWriter(open(out,'w',newline=''),fieldnames=COLS); w.writeheader(); w.writerows(rows)
print(f'{month}: {len(rows)} GTM Engineering meetings -> {out}')
