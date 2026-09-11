#!/usr/bin/env python3
"""Apply the proposed Email 1 opener edit to the BO Net-New campaign. Dry-run by default."""
import os,sys,json,subprocess,re
ENV='/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/config/lemlist.env'
KEY=[l.split('=',1)[1].strip() for l in open(ENV) if l.startswith('LEMLIST_API_KEY=')][0]
SEQ='seq_tegzQbC5PCQ78qHBm'; STEP='stp_fgmFp3zcdyuGEYkbF'; CAMP='cam_DNErdZPANvC2sqRCK'
HERE=os.path.dirname(os.path.abspath(__file__))
md=open(os.path.join(HERE,'E1_Opener_Proposal_Sep2.md')).read()
after=md.split('## After (chosen')[1].split('\n',1)[1].split('## The six')[0].strip()
paras=[p.strip() for p in after.split('\n\n') if p.strip()]
message=''.join(f'<p>{p}</p>' for p in paras)
payload={'type':'email','message':message,'subject':'two clocks','delay':0}
def curl(method,path,body=None):
    a=['curl','-s','-u',f':{KEY}','-X',method,'https://api.lemlist.com'+path,'-H','Content-Type: application/json']
    if body: a+=['-d',json.dumps(body)]
    return subprocess.run(a,capture_output=True,text=True).stdout
if '--go' not in sys.argv:
    print('DRY RUN. Would PATCH /api/sequences/%s/steps/%s with:'%(SEQ,STEP)); print(json.dumps(payload,indent=1)); sys.exit(0)
leads=json.loads(curl('GET',f'/api/campaigns/{CAMP}/export/leads?state=all&format=json') or '[]')
if leads: print('REFUSING: campaign holds',len(leads),'leads; step edits are not reversible once leads are reviewed'); sys.exit(1)
out=curl('PATCH',f'/api/sequences/{SEQ}/steps/{STEP}',payload); print('PATCH ->',out[:400])
seq=json.loads(curl('GET',f'/api/campaigns/{CAMP}/sequences'))
for st in seq[SEQ]['steps']:
    if st['_id']==STEP: print('STORED:',st.get('message'))
