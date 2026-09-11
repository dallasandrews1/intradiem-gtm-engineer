#!/usr/bin/env python3
"""Seed lemlist contact lists from the staged rosters (upsert by email/LinkedIn, then add to the motion's list).
Custom fields motion / motion_status are stamped only if they exist on the team (GET /api/fields); otherwise
the list carries the motion and the CSV carries the status until Dallas creates the two fields in lemlist settings."""
import csv,json,os,sys,subprocess,time
HERE=os.path.dirname(os.path.abspath(__file__))
ENV='/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/config/lemlist.env'
KEY=[l.split('=',1)[1].strip() for l in open(ENV) if l.startswith('LEMLIST_API_KEY=')][0]
LISTS={'bo_netnew':('clt_QCnnNJDQ3WcpMKLed',os.path.join(HERE,'lemlist_seed_bo_netnew.csv')),'bo_customer':('clt_YXPqEq2yJSLqzsXcB',os.path.join(HERE,'customer_lane_staging','lemlist_seed_bo_customer.csv'))}
def curl(m,p,b=None):
    a=['curl','-s','-u',f':{KEY}','-X',m,'https://api.lemlist.com'+p,'-H','Content-Type: application/json']
    if b is not None: a+=['-d',json.dumps(b)]
    out=subprocess.run(a,capture_output=True,text=True).stdout
    try: return json.loads(out)
    except Exception: return {'raw':out}
fields={f['name'] for f in curl('GET','/api/fields')['data']['contact']}
custom_ok={'motion','motionStatus','parentAccount'} <= fields
print('custom fields present:',custom_ok)
only=sys.argv[1] if len(sys.argv)>1 else None
for motion,(lid,path) in LISTS.items():
    if only and only!=motion: continue
    rows=list(csv.DictReader(open(path))); ids=[]; errs=0; created=updated=0
    for r in rows:
        if not r['email'] and not r['linkedinUrl']: continue
        body={k:r[k] for k in ('firstName','lastName','jobTitle') if r[k]}
        if r['email']: body['email']=r['email']
        if r['linkedinUrl']: body['linkedinUrl']=r['linkedinUrl']
        if r['companyDomain']: body['companyDomain']=r['companyDomain']
        if custom_ok: body.update({'motion':r['motion'],'motionStatus':r['motion_status'],'parentAccount':r['parent_account']})
        res=curl('POST','/api/contacts',body)
        d=res.get('data') or {}
        if d.get('_id'): ids.append(d['_id'])
        else: errs+=1; print('  ERR',r['email'] or r['linkedinUrl'],str(res)[:140])
    for i in range(0,len(ids),500):
        res=curl('POST',f'/api/contacts/lists/{lid}/entities',{'action':'add','contactIds':ids[i:i+500]})
        print('  list add',lid,len(ids[i:i+500]),str(res)[:160])
    print(motion,'rows',len(rows),'upserted',len(ids),'errors',errs)
