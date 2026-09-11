#!/usr/bin/env python3
"""Second pass after push_us_lists.py: pull every lemlist contact once, find candidate rows that never landed
(lemlist rejected the Salesforce LinkedIn URL as malformed), re-upsert them by email with the URL dropped unless it is a
clean linkedin.com/in/ form, and add them to their list. Usage: retry_missing.py <candidates.json> <has_motion_keys.json> [--go]"""
import json,os,sys,subprocess,re,collections,time
HERE=os.path.dirname(os.path.abspath(__file__))
ENV='/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/config/lemlist.env'
KEY=[l.split('=',1)[1].strip() for l in open(ENV) if l.startswith('LEMLIST_API_KEY=')][0]
CFG=json.load(open(os.path.join(HERE,'us_lists_config.json'))); cands=json.load(open(sys.argv[1])); HAS=set(json.load(open(sys.argv[2]))); GO='--go' in sys.argv
def curl(m,p,b=None):
    a=['curl','-s','-u',f':{KEY}','-X',m,'https://api.lemlist.com'+p,'-H','Content-Type: application/json']
    if b is not None: a+=['-d',json.dumps(b)]
    out=subprocess.run(a,capture_output=True,text=True).stdout
    try: return json.loads(out)
    except Exception: return {'raw':out}
have={}; off=0
while True:
    d=curl('GET',f'/api/contacts?limit=500&offset={off}'); d=d.get('data',d) if isinstance(d,dict) else d
    for c in d:
        if c.get('email'): have[c['email'].lower()]=c['_id']
        if c.get('linkedinUrl'): have[c['linkedinUrl'].lower().rstrip('/')]=c['_id']
    if len(d)<500: break
    off+=500
print('lemlist contacts indexed',len(have))
lists={l['name']:l['_id'] for l in curl('GET','/api/contacts/lists')}
RES=os.environ.get('PUSH_RESULTS') or os.path.join(HERE,'push_results.json'); results=json.load(open(RES))
for key,rows in cands.items():
    name=CFG['lists'][key]['name']; motion=CFG['lists'][key]['motion']; lid=lists[name]
    missing=[r for r in rows if not ((r['email'].lower() in have) or (r['linkedinUrl'].lower().rstrip('/') in have))]
    print(f'{key}: {len(missing)} of {len(rows)} not in lemlist')
    if not GO or not missing: continue
    ids=[]; errs=collections.Counter(); nolanding=[]
    for r in missing:
        body={k:r[k] for k in ('firstName','lastName','jobTitle') if r.get(k)}
        if r['email']: body['email']=r['email']
        li=r['linkedinUrl']
        if li and re.match(r'^https?://(www\.)?linkedin\.com/in/[^/?#]+/?$',li): body['linkedinUrl']=li
        if not body.get('email') and not body.get('linkedinUrl'): nolanding.append(r); continue
        if r.get('companyDomain'): body['companyDomain']=r['companyDomain']
        k1=r['email'].lower(); k2=li.lower().rstrip('/')
        if not (k1 in HAS or k2 in HAS): body.update({'motion':motion,'motionStatus':'staged','parentAccount':r.get('parentAccount') or ''})
        res=curl('POST','/api/contacts',body); d=res.get('data') or {}
        if d.get('_id'): ids.append(d['_id'])
        else: errs[str((res.get('error') or {}).get('message') or res)[:80]]+=1
    for i in range(0,len(ids),500):
        res=curl('POST',f'/api/contacts/lists/{lid}/entities',{'action':'add','contactIds':ids[i:i+500]}); print('  list add',str(res)[:110])
    print(f'  retried {len(missing)}: upserted {len(ids)}, still failing {sum(errs.values())} {dict(errs)}, no usable id {len(nolanding)}')
    results[key]['retry_upserted']=len(ids); results[key]['retry_failed']=sum(errs.values())+len(nolanding); results[key]['contact_ids']+=ids
json.dump(results,open(RES,'w'),indent=1)
