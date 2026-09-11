#!/usr/bin/env python3
"""Merge the customer-lane wave-1 freshness + email results, hold leavers and foreign-domain moves,
then load ready rows into the four vertical campaigns. Dry-run by default; --go loads. Never activates."""
import csv,json,os,sys,re,subprocess,collections,glob
HERE=os.path.dirname(os.path.abspath(__file__)); SP=sys.argv[1]
ENV='/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/config/lemlist.env'
KEY=[l.split('=',1)[1].strip() for l in open(ENV) if l.startswith('LEMLIST_API_KEY=')][0]
cfg=json.load(open(os.path.join(HERE,'customer_lane_config.json')))
exec(open(os.path.join(HERE,'build_customer_wave1.py')).read().split("def phrase")[0].split("cfg=json.load")[0].replace("HERE=os.path.dirname(os.path.abspath(__file__)); SP=sys.argv[1]",""))  # reuse DOM/PA
src=open(os.path.join(HERE,'build_customer_wave1.py')).read()
DOM=eval(src.split("DOM=")[1].split("\nPA=")[0]); 
def slug(u): return re.sub(r'/+$','',(u or '').lower().split('linkedin.com/in/')[-1]).strip('/')
import urllib.parse
fresh={}; 
for it in json.load(open(f'{SP}/cust_fresh_result.json')).get('data',[]):
    r=(it.get('result') or {}).get('Enrich person') or {}
    fresh[urllib.parse.unquote(it['id'])]={'ok':it.get('status')=='complete','cur':r.get('current_experience') or [],'org':r.get('org'),'headline':r.get('headline'),'title':r.get('title')}
emails={}
for it in json.load(open(f'{SP}/cust_email_result.json')).get('data',[]):
    r=it.get('result') or {}; emails[it['id']]={'email':r.get('email') or '','status':r.get('status') or ('failed' if it.get('status')=='failed' else '')}
def curl(method,path,body=None):
    a=['curl','-s','-u',f':{KEY}','-X',method,'https://api.lemlist.com'+path,'-H','Content-Type: application/json']
    if body is not None: a+=['-d',json.dumps(body)]
    return subprocess.run(a,capture_output=True,text=True).stdout
ALIAS={a.lower() for a in ['aetna','cvs','elevance','anthem','carelon','molina','unitedhealth','uhc','optum','humana','conviva','cigna','evernorth','goldman','jpmorgan','jp morgan','j.p. morgan','chase','wells fargo','synchrony','u.s. bank','us bank','u.s. bancorp','us bancorp','elavon','metlife','prudential','assurant','guardian','travelers','zurich','capita','foundever','sitel']}
summary=collections.Counter(); rows_by_v={}
for f in sorted(glob.glob(os.path.join(HERE,'customer_lane_staging','wave1','*.csv'))):
    v=os.path.basename(f)[:-4].split('_')[0]; rows=list(csv.DictReader(open(f)))
    for r in rows:
        k=slug(r['linkedinUrl']); fr=fresh.get(k)
        if fr is not None:
            if not fr['ok'] or not fr['cur']: r['load_status']='hold'; r['email_note']+='; freshness: no current role returned'
            else:
                org=(fr['org'] or '').lower()+' '+' '.join(((c.get('company_name') or c.get('org') or '')).lower() for c in fr['cur'])
                if not any(a in org for a in ALIAS): r['load_status']='hold'; r['email_note']+='; freshness: now at '+(fr['org'] or '?')
        er=emails.get(k) or emails.get(r['firstName'].lower()+'-'+r['lastName'].lower())
        if er and er['email']:
            e=er['email'].lower(); ok=er['status']=='valid' and any(e.split('@')[-1].endswith(d) for d in DOM.get(r['account'],[]))
            if not r['email']:
                if ok: r['email']=e; r['email_note']='clay work email valid'
                else: r['email_note']+='; clay returned %s (%s)'%(e,er['status'])
            elif ok and e!=r['email'].lower(): r['email_note']+='; clay variant %s adopted (jul26 %s)'%(e,r['email']); r['email']=e
            elif ok: r['email_note']+='; clay match'
        elif er and r['email'] and er['status'] in ('failed','') and 'verify' in str(er): pass
        if not r['load_status']: r['load_status']='ready' if r['email'] else 'needs_email'
        summary[(v,r['load_status'])]+=1
    w=csv.DictWriter(open(f,'w',newline=''),fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows); rows_by_v.setdefault(v,[]).extend(rows)
for k,n in sorted(summary.items()): print(k,n)
for v,rows in rows_by_v.items():
    for r in rows:
        if r['load_status']!='ready': print('  ',v,r['account'],r['firstName'],r['lastName'],'|',r['load_status'],'|',r['email_note'][:90])
if '--go' not in sys.argv: print('DRY RUN, nothing loaded'); sys.exit(0)
for v,rows in rows_by_v.items():
    cid=cfg['campaign_ids'][v]; have={(l.get('email') or '').lower() for l in json.loads(curl('GET',f'/api/campaigns/{cid}/export/leads?state=all&format=json') or '[]')}
    ok=0
    for r in rows:
        if r['load_status']!='ready' or r['email'] in have: continue
        body={k:r[k] for k in ('firstName','lastName','linkedinUrl','companyName','companyDomain','jobTitle','function','parent_account','enterprise_line')}
        out=curl('POST',f'/api/campaigns/{cid}/leads/{r["email"]}?deduplicate=true',body)
        try: ok+=1 if json.loads(out).get('_id') else 0
        except Exception: print('ERR',r['email'],out[:150])
    print(v,cid,'loaded',ok)
