#!/usr/bin/env python3
"""Push the engine's US prospect rosters into lemlist Contacts, one list per motion.

Input: a candidates JSON (built by build_us_lists.py) of {list_key: [contact rows]} that has already been through
the customer-exclusion sweep (SF exclusion segment + install-base table + denylist), the US filter, and dedupe.
For every row: upsert the contact (lemlist dedupes on email or LinkedIn URL), stamp motion / motionStatus /
parentAccount unless the contact already carries a motion from another list (first motion wins, the contact is
only added to the new list), then add the contact ids to the motion's list. Creates the list if it does not exist.
No enrichment is ever requested; pushing is free. Dry-run by default; --go pushes; --only <key> limits to one list.
Writes push_results.json next to this file with ids and counts for the bridge doc."""
import json,os,sys,subprocess,time,collections
HERE=os.path.dirname(os.path.abspath(__file__))
ENV='/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/config/lemlist.env'
KEY=[l.split('=',1)[1].strip() for l in open(ENV) if l.startswith('LEMLIST_API_KEY=')][0]
CFG=json.load(open(os.path.join(HERE,'us_lists_config.json')))
cands=json.load(open(sys.argv[1]))
HAS_MOTION=set(json.load(open(sys.argv[2]))) if len(sys.argv)>2 and sys.argv[2].endswith('.json') else set()
ONLY=sys.argv[sys.argv.index('--only')+1] if '--only' in sys.argv else None
GO='--go' in sys.argv
FIX='--fix-lists' in sys.argv   # re-add saved contact ids to each list (resolves list ids by name), no upserts
def curl(m,p,b=None):
    a=['curl','-s','-u',f':{KEY}','-X',m,'https://api.lemlist.com'+p,'-H','Content-Type: application/json']
    if b is not None: a+=['-d',json.dumps(b)]
    for attempt in range(4):
        out=subprocess.run(a,capture_output=True,text=True).stdout
        try: j=json.loads(out)
        except Exception: j={'raw':out}
        if isinstance(j,dict) and (j.get('statusCode')==429 or 'Too Many' in str(j.get('raw',''))[:80]): time.sleep(2*(attempt+1)); continue
        return j
    return j
existing={l['name']:l['_id'] for l in curl('GET','/api/contacts/lists')}
RES=os.environ.get('PUSH_RESULTS') or os.path.join(HERE,'push_results.json')   # shards write their own file
results=json.load(open(RES)) if os.path.exists(RES) else {}
if FIX:
    for key,res in results.items():
        lid=existing.get(res['name']); ids=res['contact_ids']; res['list_id']=lid; added=0; already=0
        for i in range(0,len(ids),500):
            r=curl('POST',f'/api/contacts/lists/{lid}/entities',{'action':'add','contactIds':ids[i:i+500]}); added+=r.get('addedCount',0); already+=r.get('alreadyInList',0); print(key,lid,str(r)[:120])
        res['list_added']=added; res['list_already']=already
    json.dump(results,open(RES,'w'),indent=1); sys.exit(0)
for key,rows in cands.items():
    if ONLY and key!=ONLY: continue
    name=CFG['lists'][key]['name']; motion=CFG['lists'][key]['motion']; status=CFG['lists'][key].get('motionStatus','staged')
    print(f'\n== {key}: {len(rows)} rows -> list "{name}"',('exists '+existing[name]) if name in existing else '(will create)')
    if not GO: print('   sample',{k:rows[0].get(k) for k in ('firstName','lastName','email','linkedinUrl','companyName','parentAccount','jobTitle')}); continue
    lid=existing.get(name)
    if not lid:
        r=curl('POST','/api/contacts/lists',{'name':name}); print('   create response',str(r)[:160])
        existing={l['name']:l['_id'] for l in curl('GET','/api/contacts/lists')}; lid=existing.get(name); print('   created',lid)
    ids=[]; errs=[]; kept_motion=0; c=collections.Counter()
    for r in rows:
        body={k:r[k] for k in ('firstName','lastName','jobTitle') if r.get(k)}
        if r.get('email'): body['email']=r['email']
        if r.get('linkedinUrl'): body['linkedinUrl']=r['linkedinUrl']
        if r.get('companyDomain'): body['companyDomain']=r['companyDomain']
        k1=(r.get('email') or '').lower(); k2=(r.get('linkedinUrl') or '').lower().rstrip('/')
        if k1 in HAS_MOTION or k2 in HAS_MOTION: kept_motion+=1
        else: body.update({'motion':motion,'motionStatus':r.get('motionStatus') or status,'parentAccount':r.get('parentAccount') or ''})
        res=curl('POST','/api/contacts',body); d=res.get('data') or {}
        if d.get('_id'): ids.append(d['_id']); c['ok']+=1
        else: errs.append((k1 or k2,str(res)[:140])); c['err']+=1
    for i in range(0,len(ids),500):
        res=curl('POST',f'/api/contacts/lists/{lid}/entities',{'action':'add','contactIds':ids[i:i+500]}); print('   list add',len(ids[i:i+500]),str(res)[:120])
    print(f'   upserted {c["ok"]} errors {c["err"]} motion kept from another list {kept_motion}')
    for e in errs[:10]: print('   ERR',e)
    results[key]={'list_id':lid,'name':name,'rows':len(rows),'upserted':c['ok'],'errors':c['err'],'cross_motion_kept':kept_motion,'contact_ids':ids}
    json.dump(results,open(RES,'w'),indent=1)
if not GO: print('\nDRY RUN, nothing pushed')
