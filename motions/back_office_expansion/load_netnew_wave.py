#!/usr/bin/env python3
"""Load every ready row of BO_NetNew_Leads_Staged_Sep2.csv into BO Net-New - Back Office (Nate).
Wave gate retired Sep 3 2026 (Dallas): the wave column is reporting-only. Every load_status=ready row not already in the
campaign loads; holds and needs_email rows never load. Optional --wave N restricts to one wave for reporting or a partial
reload. Dry-run by default; --go loads. Dedupes against the campaign by email. Checks the email domain against the
account domain before every POST. Never activates anything."""
import os,sys,csv,json,subprocess
ENV='/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/config/lemlist.env'
KEY=[l.split('=',1)[1].strip() for l in open(ENV) if l.startswith('LEMLIST_API_KEY=')][0]
CAMP='cam_DNErdZPANvC2sqRCK'; HERE=os.path.dirname(os.path.abspath(__file__))
WAVE=sys.argv[sys.argv.index('--wave')+1] if '--wave' in sys.argv else None
rows=[r for r in csv.DictReader(open(os.path.join(HERE,'BO_NetNew_Leads_Staged_Sep2.csv'))) if r['load_status']=='ready' and (WAVE is None or r['wave']==WAVE)]
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
have={ (l.get('email') or '').lower() for l in leads }
rows=[r for r in rows if r['email'].lower() not in have]
import collections; print('wave',WAVE or 'all','new rows after dedupe',len(rows),dict(collections.Counter(r['wave'] for r in rows)))
ncfg=json.load(open(os.path.join(HERE,'netnew_package_config.json'))); extra={ncfg['parent_account'].get(k,k):v for k,v in ncfg['extra_domains'].items()}
def dom_ok(r):
    d=r['email'].lower().split('@')[-1]; return d.endswith(r['companyDomain'].lower()) or any(d.endswith(x) for x in extra.get(r['parent_account'],[]))
bad=[r['email'] for r in rows if not dom_ok(r)]
if bad: print('STOP: email domain does not match account domain on',bad); sys.exit(1)
if not camp.get('senders'): print('WARNING: no sender assigned yet (UI sheet Part 1); leads load into the draft and nothing can send until Nathan is set')
ok=0; loaded=[]
for r in rows:
    body={k:r[k] for k in ('firstName','lastName','linkedinUrl','companyName','companyDomain','jobTitle','function','parent_account','opener_line')}
    out=curl('POST',f'/api/campaigns/{CAMP}/leads/{r["email"]}?deduplicate=true',body)
    try: j=json.loads(out); ok+=1 if j.get('_id') else 0; print('OK ' if j.get('_id') else 'ERR',r['email'],r['parent_account'],'wave',r['wave'],j.get('_id','') if j.get('_id') else out[:120]); loaded.append({'email':r['email'],'leadId':j.get('_id'),'parent_account':r['parent_account'],'wave':r['wave']})
    except Exception: print('ERR',r['email'],out[:200])
print('loaded',ok,'of',len(rows),'; campaign not started, nothing activated')
json.dump(loaded,open(os.path.join(HERE,'_last_netnew_load.json'),'w'),indent=1)
