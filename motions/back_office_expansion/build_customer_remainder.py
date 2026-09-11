#!/usr/bin/env python3
"""Customer lane, remainder: every staged candidate (four vertical staged CSVs) not yet freshness- or email-checked
in customer_lane_staging/wave1/*.csv. Writes customer_lane_staging/wave1/<v>_remainder.csv in the wave-1 column layout
(load_status blank until checked) and emits the paid-run inputs into <scratch>:
  remainder_fresh.json   Enrich Person by LinkedIn URL (0.5 cr/run) for every row with a URL
  remainder_email.json   Work Email + ZeroBounce workflow rows (find on no-email rows, two-source verify on Jul 26 rows),
                         EXCLUDING the Apollo domains (JPMorgan rule: the Clay waterfall bills on domains it cannot resolve)
  remainder_apollo.json  people to match in Apollo by LinkedIn URL (JPMorgan today; any domain the probe rule adds)
  remainder_probe.json   two-row probes for domains the Work Email routine has never resolved before
Usage: build_customer_remainder.py <scratch> ; sizing only, zero credits."""
import csv,json,os,re,sys,glob,collections,urllib.parse
HERE=os.path.dirname(os.path.abspath(__file__)); SP=sys.argv[1]
src=open(os.path.join(HERE,'build_customer_wave1.py')).read()
DOM=eval(src.split("DOM=")[1].split("\nPA=")[0]); PA=eval(src.split("PA=")[1].split("\ndef phrase")[0])
cfg=json.load(open(os.path.join(HERE,'customer_lane_config.json'))); ncfg=json.load(open(os.path.join(HERE,'netnew_package_config.json')))
APOLLO_ACCOUNTS={'JPMorgan'}                      # Work Email waterfall is a stop here (ledger 2026-09-03)
RESOLVED_BEFORE=set(DOM)-{'Guardian Life','Zurich North America'}   # every other customer domain returned addresses on Sep 2-3
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
checked=set()
for f in glob.glob(os.path.join(HERE,'customer_lane_staging','wave1','*.csv')):
    if f.endswith('_remainder.csv'): continue
    for r in csv.DictReader(open(f)): checked.add(slug(r['linkedinUrl']) or (r['firstName']+' '+r['lastName']).lower())
cols=['firstName','lastName','email','linkedinUrl','companyName','companyDomain','jobTitle','function','parent_account','enterprise_line','brand_safe','account','vertical','band','source','email_note','load_status']
out=collections.defaultdict(list); fresh=[]; email=[]; apollo=[]; probe=[]; size=collections.Counter(); probed=set()
for v in ['hc','fs','ins','bpo']:
    rows=[r for r in csv.DictReader(open(os.path.join(HERE,'customer_lane_staging',f'BO_Customer_{v}_Staged_Sep2.csv'))) if (slug(r['linkedinUrl']) or r['full_name'].lower()) not in checked]
    rows.sort(key=lambda r:(r['account'],band(r['title']),0 if r['email'] else 1,r['full_name']))
    for r in rows:
        acct=r['account']; e=r['email'].lower(); dom_ok=e and any(e.split('@')[-1].endswith(d) for d in DOM.get(acct,[]))
        row={'firstName':r['firstName'],'lastName':' '.join(re.sub(r',.*$','',r['full_name']).split()[1:]),'email':e if dom_ok else '','linkedinUrl':r['linkedinUrl'],'companyName':acct,'companyDomain':DOM.get(acct,[''])[0],'jobTitle':r['title'],'function':phrase(r['title']),'parent_account':PA.get(acct,acct),'enterprise_line':cfg['neutral_line'][v],'brand_safe':'FALSE','account':acct,'vertical':v,'band':band(r['title']),'source':'remainder:'+r['source'],'email_note':('jul26 validated' if dom_ok else ('REJECTED foreign domain '+e if e else 'no email')),'load_status':''}
        out[v].append(row); size[acct]+=1
        li=r['linkedinUrl']
        if li: fresh.append({'id':urllib.parse.quote(slug(li),safe='-_.')[:80],'inputs':{'Professional Profile URL':urllib.parse.quote(li,safe=':/?=&%-_.~')}})
        item={'id':slug(li) or r['full_name'].lower(),'inputs':{'full_name':r['full_name'],'company_name':acct,'company_domain':DOM.get(acct,[''])[0],'title':r['title'],'seniority':'','kind':'bo_customer_remainder'+('_verify' if row['email'] else ''),'clay_profile_id':''}}
        if acct in APOLLO_ACCOUNTS:
            if li: apollo.append({'id':slug(li),'linkedin_url':li,'name':r['full_name'],'account':acct,'jul26_email':row['email']})
        elif acct not in RESOLVED_BEFORE and acct not in probed and len([p for p in probe if p['inputs']['company_name']==acct])<2: probe.append(item)
        else: email.append(item)
        if acct not in RESOLVED_BEFORE and len([p for p in probe if p['inputs']['company_name']==acct])>=2: probed.add(acct)
for v,lst in out.items():
    w=csv.DictWriter(open(os.path.join(HERE,'customer_lane_staging','wave1',f'{v}_remainder.csv'),'w',newline=''),fieldnames=cols); w.writeheader(); w.writerows(lst)
json.dump({'items':fresh},open(f'{SP}/remainder_fresh.json','w')); json.dump({'items':email},open(f'{SP}/remainder_email.json','w')); json.dump(apollo,open(f'{SP}/remainder_apollo.json','w')); json.dump({'items':probe},open(f'{SP}/remainder_probe.json','w'))
print('per account:',dict(sorted(size.items())))
tot=sum(size.values())
print(f'rows {tot} | freshness runs {len(fresh)} (0.5 cr) | work-email rows {len(email)} (measured 1.05-1.6 cr) | probes {len(probe)} | apollo matches {len(apollo)} (Apollo credits, ~1 per hit)')
print(f'estimate at 1.5/row all-in: {tot*1.5:.0f} credits; component estimate {len(fresh)*0.5+len(email)*1.05:.0f} low / {len(fresh)*0.5+len(email)*1.6:.0f} high')
