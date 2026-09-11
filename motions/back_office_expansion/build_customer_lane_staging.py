#!/usr/bin/env python3
"""Stage the four AM-gated customer-lane CSVs (one per vertical lemlist campaign) with
brand_safe / enterprise_line computed per BO_Lemlist_Campaign_Copy_Sep2.md, plus the
clearance rollup. Nothing here is load-ready: every row carries owner_cleared and only
owner_cleared == TRUE rows may ever be loaded. Config in customer_lane_config.json."""
import csv, json, os, re, collections
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(HERE,'..','..'))
MAIN='/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer'
cfg=json.load(open(os.path.join(HERE,'customer_lane_config.json')))
def first(full):
    full=re.sub(r',.*$','',full).strip(); return full.split()[0] if full else ''
rows=[]
for f,lens in cfg['jul26_lists'].items():
    for r in csv.DictReader(open(os.path.join(MAIN,f))):
        acct=r['Company'].strip(); v=cfg['account_vertical'].get(acct)
        rows.append({'account':acct,'am_owner':cfg['am_owner'].get(acct,'unresolved (Savannah confirms)'),'full_name':r['Full Name'],'firstName':first(r['Full Name']),
            'title':r['Job Title'],'email':r['Work Email'].strip(),'linkedinUrl':r['LinkedIn Profile'].strip(),'source':'jul26:'+lens,'vertical':v,
            'known_to_intradiem':'','sponsor_line_conflict':'unknown','owner_cleared':'pending_owner','brand_safe':'FALSE'})
# Inger map CANDIDATE rows for accounts that fit a vertical campaign
for r in csv.DictReader(open(os.path.join(HERE,'BO_AccountMap_Roster_Inger.csv'))):
    if r['gate_result']!='CANDIDATE': continue
    v=cfg['account_vertical'].get(r['account'])
    rows.append({'account':r['account'],'am_owner':r['am_owner'],'full_name':r['full_name'],'firstName':first(r['full_name']),'title':r['title'],
        'email':r['email'],'linkedinUrl':r['linkedin_url'],'source':'inger_map:'+r['source'],'vertical':v,'known_to_intradiem':r['known_to_intradiem'],
        'sponsor_line_conflict':r['sponsor_line_conflict'],'owner_cleared':r['owner_cleared'] or 'pending_owner','brand_safe':'FALSE'})
# normalize account names and dedupe (Jul 26 list vs Inger map) by LinkedIn slug, then by name
import re as _re
def _slug(u): return _re.sub(r'/+$','',(u or '').lower().split('linkedin.com/in/')[-1]).strip('/')
def _nm(s): return _re.sub(r'[^a-z ]','',(s or '').lower()).strip()
seen={}; dedup=[]
for r in rows:
    r['account']=cfg['parent_account'].get(r['account'],r['account'])
    k=_slug(r['linkedinUrl']) or ('name:'+_nm(r['full_name'])+'@'+r['account'])
    if k in seen:
        o=seen[k]
        if not o['email'] and r['email']: o['email']=r['email']
        o['source']+=' + '+r['source']; continue
    seen[k]=r; dedup.append(r)
rows=dedup
for r in rows:
    r['function']=cfg['function_phrase_default']
    r['parent_account']=cfg['parent_account'].get(r['account'],r['account'])
    bs=r['brand_safe'].upper()=='TRUE' and r['owner_cleared'].upper()=='TRUE'
    r['enterprise_line']=cfg['enterprise_line_brand_safe'] if bs else cfg['neutral_line'].get(r['vertical'] or '', '')
    r['load_status']='HOLD: AM clearance pending' if r['owner_cleared'].upper()!='TRUE' else ('needs_email' if not r['email'] else 'clearable')
cols=['firstName','email','linkedinUrl','function','parent_account','enterprise_line','brand_safe','owner_cleared','load_status','account','am_owner','full_name','title','vertical','source','known_to_intradiem','sponsor_line_conflict']
os.makedirs(os.path.join(HERE,'customer_lane_staging'),exist_ok=True)
byv=collections.defaultdict(list)
for r in rows: byv[r['vertical'] or 'no_campaign'].append(r)
for v,lst in byv.items():
    p=os.path.join(HERE,'customer_lane_staging',f'BO_Customer_{v}_Staged_Sep2.csv')
    w=csv.DictWriter(open(p,'w',newline=''),fieldnames=cols); w.writeheader(); w.writerows(sorted(lst,key=lambda r:(r['account'],r['full_name'])))
    print(v,len(lst),'campaign',cfg['campaign_ids'].get(v,'NONE'))
roll=collections.defaultdict(lambda:collections.Counter())
for r in rows: roll[(r['account'],r['am_owner'],r['vertical'] or 'no_campaign')][r['owner_cleared']]+=1
with open(os.path.join(HERE,'customer_lane_staging','Clearance_Rollup_Sep2.csv'),'w',newline='') as f:
    w=csv.writer(f); w.writerow(['account','vertical_campaign','am_owner','candidates','cleared','held','pending_owner','emails_on_hand'])
    for (a,am,v),c in sorted(roll.items()):
        em=sum(1 for r in rows if r['account']==a and r['email'])
        w.writerow([a,v,am,sum(c.values()),c.get('TRUE',0),c.get('HOLD',0)+c.get('FALSE',0),c.get('pending_owner',0),em])
        print(f"{a:22} {v:12} {am[:28]:28} cand={sum(c.values()):3} cleared={c.get('TRUE',0)} held={c.get('HOLD',0)+c.get('FALSE',0)} pending={c.get('pending_owner',0)} emails={em}")
