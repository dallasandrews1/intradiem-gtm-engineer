#!/usr/bin/env python3
"""Push colleagueFirst / colleagueLine onto DWO leads. Dry run by default; --go writes. --limit N for a test slice."""
import csv,json,os,sys,time,urllib.request,base64
HERE=os.path.dirname(os.path.abspath(__file__))
CAMP='cam_SiD4KmWcRuhiF6uhL'
env={}
for p in [os.path.join(HERE,'..','..','automation','config','lemlist.env'),'/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/config/lemlist.env']:
    if os.path.exists(p):
        for line in open(p):
            if '=' in line and not line.startswith('#'): k,v=line.strip().split('=',1); env[k]=v.strip().strip('"')
        break
KEY=env.get('LEMLIST_API_KEY'); assert KEY, 'no LEMLIST_API_KEY'
AUTH='Basic '+base64.b64encode((':'+KEY).encode()).decode()
def req(method,path,body=None):
    r=urllib.request.Request('https://api.lemlist.com'+path,data=json.dumps(body).encode() if body is not None else None,method=method,headers={'Authorization':AUTH,'Content-Type':'application/json','User-Agent':'intradiem-gtm/1.0'})
    try:
        with urllib.request.urlopen(r,timeout=30) as resp: return resp.status,json.loads(resp.read() or b'null')
    except urllib.error.HTTPError as e: return e.code,e.read().decode()[:200]
go='--go' in sys.argv; lim=int(sys.argv[sys.argv.index('--limit')+1]) if '--limit' in sys.argv else None
rows=list(csv.DictReader(open(os.path.join(HERE,'DWO_Colleague_Map_Sep4.csv'))))[:lim]
ok=miss=fail=0; log=[]
for i,r in enumerate(rows):
    st,lead=req('GET','/api/leads/'+r['email'])
    lid=None
    if st==200:
        cands=lead if isinstance(lead,list) else [lead]
        for c in cands:
            if isinstance(c,dict) and c.get('campaignId')==CAMP and c.get('_id'): lid=c['_id']
        if not lid and cands and isinstance(cands[0],dict): lid=cands[0].get('_id') if cands[0].get('campaignId') in (None,CAMP) else None
    if i==0: print('sample GET status',st,'id',lead.get('_id') if isinstance(lead,dict) else None,'campaign',lead.get('campaignId') if isinstance(lead,dict) else None)
    if not lid: miss+=1; log.append((r['email'],'no lead in campaign',st)); continue
    if go:
        body={'colleagueFirst':r['colleagueFirst'],'colleagueLine':r['colleagueLine']}
        st2,res=req('POST',f'/api/leads/{lid}/variables',body)
        if st2!=200: st2,res=req('PATCH',f'/api/leads/{lid}/variables',body)
        if st2==200: ok+=1
        else: fail+=1; log.append((r['email'],'patch',st2,str(res)[:120]))
        time.sleep(0.15)
    else: ok+=1
print(('WROTE' if go else 'DRY RUN resolved'),ok,'missing',miss,'failed',fail,'of',len(rows))
for l in log[:15]: print(' ',l)
