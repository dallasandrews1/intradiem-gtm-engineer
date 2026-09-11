#!/usr/bin/env python3
"""Load BO_NetNew_Wave1_Load_Sep2.csv into BO Net-New - Back Office (Nate). Dry-run by default.
Refuses to load if the campaign already holds leads or has no sender. Never activates anything."""
import os,sys,csv,json,subprocess
ENV='/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/config/lemlist.env'
KEY=[l.split('=',1)[1].strip() for l in open(ENV) if l.startswith('LEMLIST_API_KEY=')][0]
CAMP='cam_DNErdZPANvC2sqRCK'; HERE=os.path.dirname(os.path.abspath(__file__))
rows=list(csv.DictReader(open(os.path.join(HERE,'BO_NetNew_Wave1_Load_Sep2.csv'))))
def curl(method,path,body=None):
    a=['curl','-s','-u',f':{KEY}','-X',method,'https://api.lemlist.com'+path,'-H','Content-Type: application/json']
    if body is not None: a+=['-d',json.dumps(body)]
    return subprocess.run(a,capture_output=True,text=True).stdout
camp=json.loads(curl('GET',f'/api/campaigns/{CAMP}?version=v2'))
leads=json.loads(curl('GET',f'/api/campaigns/{CAMP}/export/leads?state=all&format=json') or '[]')
print('campaign',camp.get('name'),camp.get('status'),'senders',camp.get('senders'),'leads now',len(leads),'rows to load',len(rows))
if '--go' not in sys.argv:
    print('DRY RUN. First payload would be:'); r=rows[0]
    print(json.dumps({k:r[k] for k in ('firstName','lastName','email','linkedinUrl','companyName','companyDomain','jobTitle','function','parent_account','opener_line')},indent=1)); sys.exit(0)
if leads: print('REFUSING: campaign already holds leads'); sys.exit(1)
if not camp.get('senders'): print('WARNING: no sender assigned yet (UI sheet Part 1); leads load into the draft and nothing can send until Nathan is set')
ok=0
for r in rows:
    body={k:r[k] for k in ('firstName','lastName','linkedinUrl','companyName','companyDomain','jobTitle','function','parent_account','opener_line')}
    out=curl('POST',f'/api/campaigns/{CAMP}/leads/{r["email"]}?deduplicate=true',body)
    try: j=json.loads(out); ok+=1 if j.get('_id') else 0; print('OK ' if j.get('_id') else 'ERR',r['email'],out[:120] if not j.get('_id') else '')
    except Exception: print('ERR',r['email'],out[:200])
print('loaded',ok,'of',len(rows),'; campaign stays DRAFT, nothing activated')
