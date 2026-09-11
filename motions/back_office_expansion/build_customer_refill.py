#!/usr/bin/env python3
"""Refill held customer-lane seats: for each account with holds in wave 1, pick the next candidates
(executives first) not already staged, write customer_lane_staging/wave1/<v>_refill.csv, and emit the
freshness + email inputs. Usage: python3 build_customer_refill.py <scratch>"""
import csv,json,os,re,sys,glob,collections,urllib.parse
HERE=os.path.dirname(os.path.abspath(__file__)); SP=sys.argv[1]
src=open(os.path.join(HERE,'build_customer_wave1.py')).read()
DOM=eval(src.split("DOM=")[1].split("\nPA=")[0]); PA=eval(src.split("PA=")[1].split("\ndef phrase")[0])
cfg=json.load(open(os.path.join(HERE,'customer_lane_config.json'))); ncfg=json.load(open(os.path.join(HERE,'netnew_package_config.json')))
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
staged={}; holds=collections.Counter()
for f in glob.glob(os.path.join(HERE,'customer_lane_staging','wave1','*.csv')):
    for r in csv.DictReader(open(f)):
        staged[slug(r['linkedinUrl']) or (r['firstName']+' '+r['lastName']).lower()]=1
        if r['load_status']=='hold': holds[(r['vertical'],r['account'])]+=1
out=collections.defaultdict(list); fresh=[]; need=[]
for (v,acct),n in holds.items():
    rows=[r for r in csv.DictReader(open(os.path.join(HERE,'customer_lane_staging',f'BO_Customer_{v}_Staged_Sep2.csv'))) if r['account']==acct]
    rows=[r for r in rows if (slug(r['linkedinUrl']) or r['full_name'].lower()) not in staged]
    rows.sort(key=lambda r:(band(r['title']),0 if r['email'] else 1,r['full_name']))
    for r in rows[:n]:
        e=r['email'].lower(); dom_ok=e and any(e.split('@')[-1].endswith(d) for d in DOM.get(acct,[]))
        row={'firstName':r['firstName'],'lastName':' '.join(re.sub(r',.*$','',r['full_name']).split()[1:]),'email':e if dom_ok else '','linkedinUrl':r['linkedinUrl'],'companyName':acct,'companyDomain':DOM.get(acct,[''])[0],'jobTitle':r['title'],'function':phrase(r['title']),'parent_account':PA.get(acct,acct),'enterprise_line':cfg['neutral_line'][v],'brand_safe':'FALSE','account':acct,'vertical':v,'band':band(r['title']),'source':'refill:'+r['source'],'email_note':('jul26 validated' if dom_ok else ('REJECTED foreign domain '+e if e else 'no email')),'load_status':''}
        out[v].append(row)
        if r['linkedinUrl']: fresh.append({'id':urllib.parse.quote(slug(r['linkedinUrl']),safe='-_.')[:80],'inputs':{'Professional Profile URL':urllib.parse.quote(r['linkedinUrl'],safe=':/?=&%-_.~')}})
        if not row['email'] and r['linkedinUrl']: need.append({'id':slug(r['linkedinUrl']),'inputs':{'full_name':r['full_name'],'company_name':acct,'company_domain':DOM.get(acct,[''])[0],'title':r['title'],'seniority':'','kind':'bo_customer_refill','clay_profile_id':''}})
        # even validated jul26 addresses get the two-source check
        if row['email'] and r['linkedinUrl']: need.append({'id':slug(r['linkedinUrl']),'inputs':{'full_name':r['full_name'],'company_name':acct,'company_domain':DOM.get(acct,[''])[0],'title':r['title'],'seniority':'','kind':'bo_customer_refill_verify','clay_profile_id':''}})
cols=['firstName','lastName','email','linkedinUrl','companyName','companyDomain','jobTitle','function','parent_account','enterprise_line','brand_safe','account','vertical','band','source','email_note','load_status']
for v,lst in out.items():
    w=csv.DictWriter(open(os.path.join(HERE,'customer_lane_staging','wave1',f'{v}_refill.csv'),'w',newline=''),fieldnames=cols); w.writeheader(); w.writerows(lst)
    print(v,len(lst),collections.Counter(r['account'] for r in lst))
json.dump({'items':fresh},open(f'{SP}/refill_fresh.json','w')); json.dump({'items':need},open(f'{SP}/refill_email.json','w'))
print('freshness',len(fresh),'email runs',len(need))
