#!/usr/bin/env python3
"""Stage the BO Net-New (Nate) lemlist lead package from the six back-office map rosters.

Config over code: tiers, wave size, and phrase rules live in netnew_package_config.json.
Reads BO_Map_Build_Sheets_Nate.csv, nate_sf_check.csv, nate_live_check.csv and writes
BO_NetNew_Leads_Staged_Sep2.csv (all rows, wave-numbered) plus a per-wave summary.
Emails come only from (a) Salesforce records at the account's own domain with a high
match, or (b) a Clay Work Email run written into netnew_email_results.csv. Nothing is
pattern-guessed. Rows with no email stay in the file with load_status=needs_email."""
import csv, json, re, sys, collections, os
HERE=os.path.dirname(os.path.abspath(__file__))
cfg=json.load(open(os.path.join(HERE,'netnew_package_config.json')))
sets=json.load(open(os.path.join(HERE,'sets','nate.json')))['accounts']
rows=list(csv.DictReader(open(os.path.join(HERE,'BO_Map_Build_Sheets_Nate.csv'))))
sf={r['linkedin_url']:r for r in csv.DictReader(open(os.path.join(HERE,'nate_sf_check.csv')))}
live={r['linkedin_url']:r for r in csv.DictReader(open(os.path.join(HERE,'nate_live_check.csv')))}
emailres={}
p=os.path.join(HERE,'netnew_email_results.csv')
if os.path.exists(p):
    for r in csv.DictReader(open(p)): emailres[r['linkedin_url']]=r

def first_name(full):
    m=re.match(r'^([A-Z][a-z]+),\s*([A-Z][a-z]+)$',full.strip())
    if m: return m.group(2)
    full=re.sub(r',.*$','',full).strip()
    full=re.sub(r'\b(MBA|CPHQ|SPHR|CEBS|CFA|JD|CPSM|CAMS|AMLP|AMP|POPM|LSSGB|GPHR|MACS|MSSF|CCP)\b\.?','',full).strip()
    if ',' in full: return full.split(',')[0].strip()
    parts=full.split()
    return parts[0] if parts else full

def phrase(title, func):
    t=title.lower()
    for rule in cfg['phrase_rules']:
        if all(re.search(r'\b'+re.escape(k)+r'\b',t) for k in rule['all']) and not any(re.search(r'\b'+re.escape(k)+r'\b',t) for k in rule.get('none',[])):
            return rule['phrase']
    return cfg['function_default'].get(func, 'operations')

def tier(r):
    t=re.sub(r'vice president','vp',r['title'].lower()); lvl=r['level']
    if any(re.search(r'\b'+k+r'\b',t) for k in cfg['tier3_title_keys']): return 3
    if lvl=='C' and not any(k in t for k in cfg['ops_exec_keys']): return 3
    if lvl=='C': return 2
    if lvl in ('EVP','SVP','VP','AVP'): return 1
    return 2

out=[]
for r in rows:
    url=r['linkedin_url']; acct=r['account']; cfgA=sets[acct]
    s=sf.get(url,{}); l=live.get(url,{})
    dom_ok=lambda e: any(e.lower().split('@')[-1].endswith(d) for d in cfgA['domains']+cfg['extra_domains'].get(acct,[]))
    email=''; email_src=''; alt=''
    sfe=s.get('sf_email','') if (s.get('in_salesforce')=='yes' and s.get('match_confidence') in ('high','medium') and s.get('sf_email') and dom_ok(s['sf_email'])) else ''
    er=emailres.get(url)
    ce=(er or {}).get('email','') if er else ''
    cst=(er or {}).get('status','') if er else ''
    if ce and cst=='valid' and dom_ok(ce):
        email=ce; email_src='clay_work_email'
        if sfe and sfe.lower()!=ce.lower(): email_src='clay_work_email (sf alternate %s)'%sfe
        elif sfe: email_src='clay_work_email + salesforce match'
    elif ce and not dom_ok(ce):
        email=''; email_src='REJECTED foreign domain %s'%ce; alt=ce
    elif sfe and (not er or cst in ('failed','')):
        email=sfe; email_src='salesforce_single_source'
    elif ce and cst!='valid':
        email=''; email_src='clay %s %s'%(cst,ce)
    known='yes' if s.get('in_salesforce')=='yes' else ('possible' if s.get('in_salesforce')=='possible' else 'no')
    out.append({
        'firstName':first_name(r['full_name']),'lastName':(re.match(r'^([A-Z][a-z]+),\s*[A-Z][a-z]+$',r['full_name'].strip()).group(1) if re.match(r'^([A-Z][a-z]+),\s*[A-Z][a-z]+$',r['full_name'].strip()) else ' '.join(re.sub(r',.*$','',r['full_name']).split()[1:])),
        'email':email,'linkedinUrl':url,'function':phrase(r['title'],r['function']),
        'parent_account':cfg['parent_account'][acct],'companyName':cfg['company_name'][acct],'companyDomain':cfgA['domains'][0],
        'jobTitle':r['title'],'level':r['level'],'lane':r['lane'],'map_order':r['order'],
        'tier':tier(r),'wave':0,'email_source':email_src,'known_to_intradiem':known,
        'live_status':l.get('status',''),'live_refresh':(l.get('last_refresh') or '')[:10],'li_active':'unmeasured',
        'customer_exclusion':'clear','badge':r['badge_check'],'load_status':''})
# wave slicing: per account, tier 1 by map order, cap per wave
per=collections.defaultdict(list)
for o in sorted(out,key=lambda o:(o['tier'],int(o['map_order']))): per[o['parent_account']].append(o)
for acct,lst in per.items():
    cap=cfg['wave1_cap_per_account']; n=0
    for o in lst:
        if o['tier']==3: o['wave']=cfg['tier3_wave']; continue
        n+=1; o['wave']=1 if n<=cap else 2 if n<=cap*2 else 3 if n<=cap*3 else 4
for o in out:
    o['opener_line']=cfg.get('opener_line',{}).get(o['parent_account'],'')
    o['hold_reason']=cfg.get('holds',{}).get(o['linkedinUrl'],'')
    o['verify_note']=cfg.get('verify_notes',{}).get(o['linkedinUrl'],'')
    if o['hold_reason']: o['load_status']='hold'
    elif o['email_source']=='salesforce_single_source': o['load_status']='hold'; o['hold_reason']='Salesforce address with no second source yet (Clay found nothing); validate before load'
    elif o['email_source'].startswith('REJECTED'): o['load_status']='hold'; o['hold_reason']='Clay returned an address at another company (%s); possible move, check Sales Nav'%o['email_source'].split()[-1]
    else: o['load_status']='ready' if o['email'] and o['live_status']=='current' and o['customer_exclusion']=='clear' else ('needs_email' if not o['email'] else 'hold')
cols=['firstName','email','linkedinUrl','function','parent_account','opener_line','companyName','companyDomain','lastName','jobTitle','level','lane','wave','tier','load_status','hold_reason','verify_note','email_source','known_to_intradiem','live_status','live_refresh','li_active','customer_exclusion','badge','map_order']
w=csv.DictWriter(open(os.path.join(HERE,'BO_NetNew_Leads_Staged_Sep2.csv'),'w',newline=''),fieldnames=cols); w.writeheader(); w.writerows(sorted(out,key=lambda o:(o['wave'],o['parent_account'],o['tier'],int(o['map_order']))))
summ=collections.Counter((o['wave'],o['load_status']) for o in out)
print('rows',len(out)); 
for wv in sorted({o['wave'] for o in out}): print('wave',wv,{k[1]:v for k,v in summ.items() if k[0]==wv}, collections.Counter(o['parent_account'] for o in out if o['wave']==wv))
print('phrases',collections.Counter(o['function'] for o in out).most_common())
