#!/usr/bin/env python3
"""Load the ready rows of customer_lane_staging/wave1/*_remainder.csv into the four vertical campaigns
(customer_lane_config.json campaign_ids), deduped against each campaign by email. Runs AFTER load_customer_wave.py's
merge and apply_apollo_holds.py, without re-running the merge. Dry-run by default; --go loads. Never activates.
Prints loaded / held / needs_email per account and writes _last_customer_load.json."""
import csv,glob,json,os,sys,subprocess,collections
HERE=os.path.dirname(os.path.abspath(__file__)); GO='--go' in sys.argv
ENV='/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/config/lemlist.env'
KEY=[l.split('=',1)[1].strip() for l in open(ENV) if l.startswith('LEMLIST_API_KEY=')][0]
cfg=json.load(open(os.path.join(HERE,'customer_lane_config.json')))
def curl(method,path,body=None):
    a=['curl','-s','-u',f':{KEY}','-X',method,'https://api.lemlist.com'+path,'-H','Content-Type: application/json']
    if body is not None: a+=['-d',json.dumps(body)]
    out=subprocess.run(a,capture_output=True,text=True).stdout
    try: return json.loads(out)
    except Exception: return {'raw':out}
per=collections.defaultdict(collections.Counter); loaded=[]; errs=[]
for f in sorted(glob.glob(os.path.join(HERE,'customer_lane_staging','wave1','*_remainder.csv'))):
    v=os.path.basename(f).split('_')[0]; cid=cfg['campaign_ids'][v]; rows=list(csv.DictReader(open(f)))
    have={(l.get('email') or '').lower() for l in (curl('GET',f'/api/campaigns/{cid}/export/leads?state=all&format=json') or [])}
    for r in rows:
        st=r['load_status']
        if st!='ready': per[r['account']][st]+=1; continue
        if r['email'].lower() in have: per[r['account']]['already_in']+=1; continue
        dom_ok=any(r['email'].lower().split('@')[-1].endswith(d) for d in [r['companyDomain']]+[]) or True
        if not GO: per[r['account']]['would_load']+=1; continue
        body={k:r[k] for k in ('firstName','lastName','linkedinUrl','companyName','companyDomain','jobTitle','function','parent_account','enterprise_line')}
        res=curl('POST',f'/api/campaigns/{cid}/leads/{r["email"]}?deduplicate=true',body)
        if res.get('_id'): per[r['account']]['loaded']+=1; loaded.append({'email':r['email'],'leadId':res['_id'],'account':r['account'],'campaign':cid})
        else: per[r['account']]['error']+=1; errs.append((r['email'],str(res)[:140]))
print(('LOADED' if GO else 'DRY RUN')+' per account:')
for a in sorted(per): print(f"  {a:22} "+'  '.join(f"{k} {n}" for k,n in sorted(per[a].items())))
tot=collections.Counter(); [tot.update(c) for c in per.values()]; print('  TOTAL',dict(tot))
for e in errs: print('  ERR',e)
if GO:
    json.dump(loaded,open(os.path.join(HERE,'_last_customer_load.json'),'w'),indent=1)
    for v,cid in cfg['campaign_ids'].items(): print(v,cid,'now',len(curl('GET',f'/api/campaigns/{cid}/export/leads?state=all&format=json') or []),'leads')
