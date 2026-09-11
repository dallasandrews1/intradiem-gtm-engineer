#!/usr/bin/env python3
"""Customer-lane wave 1 (Dallas, Sep 2: AM clearance filter removed; Nate reviews names in lemlist after load).
Six per account, executives first, from customer_lane_staging/*.csv. Writes customer_lane_staging/wave1/<vertical>.csv
plus the freshness and email input files. Emails: Jul 26 validated address at the account domain, else the Clay run."""
import csv,json,os,re,sys,collections
HERE=os.path.dirname(os.path.abspath(__file__)); SP=sys.argv[1]
cfg=json.load(open(os.path.join(HERE,'customer_lane_config.json'))); ncfg=json.load(open(os.path.join(HERE,'netnew_package_config.json')))
DOM={'Maximus':['maximus.com'],'Aetna':['aetna.com','cvshealth.com'],'Elevance Health':['elevancehealth.com','anthem.com','carelon.com'],'Molina Healthcare':['molinahealthcare.com'],'UnitedHealthcare':['uhc.com','optum.com','uhg.com','unitedhealthgroup.com'],'Humana':['humana.com','convivaphysicians.com'],'Cigna':['cigna.com','evernorth.com','cignahealthcare.com'],'Goldman Sachs':['gs.com','goldmansachs.com'],'JPMorgan':['jpmorgan.com','jpmchase.com','chase.com'],'Wells Fargo':['wellsfargo.com'],'Synchrony Financial':['syf.com','synchrony.com','synchronyfinancial.com'],'US Bancorp':['usbank.com','elavon.com'],'MetLife':['metlife.com'],'Prudential Financial':['prudential.com'],'Assurant':['assurant.com'],'Guardian Life':['glic.com','guardianlife.com'],'Travelers':['travelers.com'],'Zurich North America':['zurichna.com','zurich.com'],'Capita':['capita.com','capita.co.uk'],'Foundever':['foundever.com','sitel.com']}
PA={'Maximus':'Maximus','Aetna':'Aetna','Elevance Health':'Elevance','Molina Healthcare':'Molina','UnitedHealthcare':'UnitedHealthcare','Humana':'Humana','Cigna':'Cigna','Goldman Sachs':'Goldman Sachs','JPMorgan':'JPMorgan','Wells Fargo':'Wells Fargo','Synchrony Financial':'Synchrony','US Bancorp':'U.S. Bank','MetLife':'MetLife','Prudential Financial':'Prudential','Assurant':'Assurant','Guardian Life':'Guardian','Travelers':'Travelers','Zurich North America':'Zurich','Capita':'Capita','Foundever':'Foundever'}
def phrase(title):
    t=title.lower()
    for rule in ncfg['phrase_rules']:
        if all(re.search(r'\b'+re.escape(k)+r'\b',t) for k in rule['all']) and not any(re.search(r'\b'+re.escape(k)+r'\b',t) for k in rule.get('none',[])): return rule['phrase']
    return 'operations'
def band(title):
    t=title.lower()
    if re.search(r'\bchief|\bevp\b|executive vice',t): return 0
    if re.search(r'\bsvp\b|senior vice|\bhead of\b|managing director',t): return 1
    if re.search(r'\bvp\b|vice president|\bavp\b',t): return 2
    if 'director' in t: return 3
    return 4
def slug(u): return re.sub(r'/+$','',(u or '').lower().split('linkedin.com/in/')[-1]).strip('/')
live=json.load(open(f'{SP}/lemlist_all_leads.json'))
live_email={(l.get('email') or '').lower() for l in live}; live_slug={slug(l.get('linkedinUrl')) for l in live if l.get('linkedinUrl')}
out=collections.defaultdict(list); fresh=[]; need_email=[]; collisions=[]
for v in ('hc','fs','ins','bpo'):
    rows=list(csv.DictReader(open(os.path.join(HERE,'customer_lane_staging',f'BO_Customer_{v}_Staged_Sep2.csv'))))
    by=collections.defaultdict(list)
    for r in rows: by[r['account']].append(r)
    for acct,lst in by.items():
        lst.sort(key=lambda r:(band(r['title']),0 if r['email'] else 1,r['full_name']))
        n=0
        for r in lst:
            if n>=6: break
            e=r['email'].lower()
            if (e and e in live_email) or (slug(r['linkedinUrl']) and slug(r['linkedinUrl']) in live_slug):
                collisions.append((acct,r['full_name'],e)); continue
            dom_ok=e and any(e.split('@')[-1].endswith(d) for d in DOM.get(acct,[]))
            row={'firstName':r['firstName'],'lastName':' '.join(re.sub(r',.*$','',r['full_name']).split()[1:]),'email':e if dom_ok else '','linkedinUrl':r['linkedinUrl'],
                 'companyName':acct,'companyDomain':DOM.get(acct,[''])[0],'jobTitle':r['title'],'function':phrase(r['title']),'parent_account':PA.get(acct,acct),
                 'enterprise_line':cfg['neutral_line'][v],'brand_safe':'FALSE','account':acct,'vertical':v,'band':band(r['title']),'source':r['source'],
                 'email_note':('jul26 validated' if dom_ok else ('REJECTED foreign domain '+e if e else 'no email')),'load_status':''}
            out[v].append(row); n+=1
            if r['linkedinUrl']: fresh.append({'id':slug(r['linkedinUrl']) or r['full_name'],'inputs':{'Professional Profile URL':r['linkedinUrl']}})
            if not row['email']: need_email.append({'id':slug(r['linkedinUrl']) or r['full_name'].replace(' ','-').lower(),'inputs':{'full_name':r['full_name'],'company_name':acct,'company_domain':DOM.get(acct,[''])[0],'title':r['title'],'seniority':'','kind':'bo_customer_wave1','clay_profile_id':''}})
os.makedirs(os.path.join(HERE,'customer_lane_staging','wave1'),exist_ok=True)
cols=['firstName','lastName','email','linkedinUrl','companyName','companyDomain','jobTitle','function','parent_account','enterprise_line','brand_safe','account','vertical','band','source','email_note','load_status']
for v,lst in out.items():
    w=csv.DictWriter(open(os.path.join(HERE,'customer_lane_staging','wave1',f'{v}.csv'),'w',newline=''),fieldnames=cols); w.writeheader(); w.writerows(lst)
    print(v,len(lst),'with email',sum(1 for r in lst if r['email']),collections.Counter(r['account'] for r in lst))
json.dump({'items':fresh},open(f'{SP}/cust_fresh.json','w')); json.dump({'items':need_email},open(f'{SP}/cust_email.json','w'))
print('freshness rows',len(fresh),'need email',len(need_email),'collisions',collisions)
