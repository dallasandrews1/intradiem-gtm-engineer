#!/usr/bin/env python3
"""Reconcile a DWO live wave into the lemlist list DWO Executives, Prospects (SF) clt_FKm6KuNcgeghas73o.
Inputs in <scratch>: dwo_live_waves.json (wave rows), dwo_<wave>_email_results.json (Work Email + ZeroBounce by
clay_profile_id), dwo_w1_bridge_results.json (name -> url, batches 0-4) + dwo_w1_bridge_agent_*.jsonl (id -> url),
dwo_<wave>_apollo_results.json (optional, id -> {email,status}).
Rules: status valid -> found (loaded to lemlist with email, url when bridged, motionStatus staged); no_email / invalid /
unknown -> no_email (loaded by LinkedIn URL only when bridged, motionStatus needs_email; skipped when no email and no url);
bridge says the person now sits at another company -> held. SF rows on the list that no live person matched (by email or
by normalized name + account) get motionStatus sf_stale. Usage: reconcile_dwo_wave.py <scratch> --wave wave1 [--go]"""
import json,os,sys,re,glob,subprocess,collections,time
SP=sys.argv[1]; WAVE=sys.argv[sys.argv.index('--wave')+1]; GO='--go' in sys.argv
HERE=os.path.dirname(os.path.abspath(__file__)); LIST='clt_Fg8mhEJ7F9uRK9go3'   # DWO Executives, Live (Clay): the net-new pool; the SF list clt_FKm6KuNcgeghas73o keeps the Salesforce rows
ENV='/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/config/lemlist.env'
KEY=[l.split('=',1)[1].strip() for l in open(ENV) if l.startswith('LEMLIST_API_KEY=')][0]
def curl(m,p,b=None):
    a=['curl','-s','-u',f':{KEY}','-X',m,'https://api.lemlist.com'+p,'-H','Content-Type: application/json']
    if b is not None: a+=['-d',json.dumps(b)]
    for i in range(3):
        out=subprocess.run(a,capture_output=True,text=True).stdout
        try: return json.loads(out)
        except Exception: time.sleep(2)
    return {'raw':out}
def norm(s): return re.sub(r'[^a-z ]','',(s or '').lower().replace(',',' ')).strip()
def nkey(name):
    p=norm(name).split(); return (p[0]+' '+p[-1]) if len(p)>=2 else norm(name)
rows=[p for p in json.load(open(f'{SP}/dwo_live_waves.json'))[WAVE] if p['domain']!='unive.nl']
emails=json.load(open(f'{SP}/dwo_{WAVE}_email_results.json'))
ap=os.path.join(SP,f'dwo_{WAVE}_apollo_results.json'); apollo=json.load(open(ap)) if os.path.exists(ap) else {}
bridge_by_id={}; bridge_by_name={}
for f in glob.glob(f'{SP}/dwo_w1_bridge_agent_*.jsonl'):
    for l in open(f):
        try: r=json.loads(l)
        except Exception: continue
        if r.get('found') and r.get('url'): bridge_by_id[str(r.get('id'))]=r
        elif not r.get('found'): bridge_by_id.setdefault(str(r.get('id')),{'url':'','company':'','miss':True,'note':r.get('note') or ''})
b0=json.load(open(f'{SP}/dwo_w1_bridge_results.json')) if os.path.exists(f'{SP}/dwo_w1_bridge_results.json') else {}
for k,v in b0.items(): bridge_by_name[nkey(k)]=v
out=[]; per=collections.defaultdict(collections.Counter)
for p in rows:
    pid=str(p['clay_profile_id']); e=emails.get(pid) or apollo.get(pid) or {}
    br=bridge_by_id.get(pid) or bridge_by_name.get(nkey(p['name'])) or {}
    url=(br.get('url') or '').strip(); brco=(br.get('company') or '')
    moved=bool(re.search(r'domain differs',br.get('note') or '')) or bool(brco) and not (norm(p['account']).split(' ')[0] in norm(brco) or norm(brco).split(' ')[0] in norm(p['account']) or norm(p['company']).split(' ')[0] in norm(brco))
    if moved: st='held'; note=(br.get('note') or ('bridge: now at '+brco))
    elif br.get('miss') and not e.get('email'): st='no_email'; note='no profile match, '+('clay: '+(e.get('status') or 'no result'))
    elif e.get('status')=='valid' and e.get('email'): st='found'; note=e.get('src','clay work email valid')
    else: st='no_email'; note='clay: '+(e.get('status') or 'no result')
    out.append({**p,'email':e.get('email') if st=='found' else '','linkedinUrl':url,'result':st,'note':note})
    per[p['vertical']][st]+=1
print(f'{WAVE}: {len(rows)} rows'); tot=collections.Counter()
for v in sorted(per): print(f"  {v:20} found {per[v]['found']:4}  no_email {per[v]['no_email']:4}  held {per[v]['held']:3}"); tot.update(per[v])
print('  TOTAL',dict(tot),'| with LinkedIn URL',sum(1 for o in out if o['linkedinUrl']))
json.dump(out,open(f'{SP}/dwo_{WAVE}_reconciled.json','w'),indent=0)
if not GO: print('DRY RUN'); sys.exit(0)
# 1. upsert live people
ids=[]; c=collections.Counter()
for o in out:
    if o['result']=='held': continue
    if not o['email'] and not o['linkedinUrl']: c['skipped_no_key']+=1; continue
    body={'firstName':o['firstName'] or '','lastName':o['lastName'] or '','jobTitle':o['title'] or '','companyDomain':o['domain'],'motion':'dwo_exec','motionStatus':'staged' if o['result']=='found' else 'needs_email','parentAccount':o['account']}
    if o['email']: body['email']=o['email']
    if o['linkedinUrl']: body['linkedinUrl']=o['linkedinUrl']
    res=curl('POST','/api/contacts',body); d=res.get('data') or {}
    if d.get('_id'): ids.append(d['_id']); c['upserted']+=1
    else: c['error']+=1
for i in range(0,len(ids),500): print('  list add',str(curl('POST',f'/api/contacts/lists/{LIST}/entities',{'action':'add','contactIds':ids[i:i+500]}))[:110])
print('live upserts',dict(c))
# 2. mark unmatched SF rows on the list as sf_stale
live_emails={o['email'].lower() for o in out if o['email']}; live_names={(nkey(o['name']),norm(o['account']).split(' ')[0]) for o in out}
sf=json.load(open(f'{SP}/dwo_candidates_v2.json'))['dwo_executives']; stale=0; kept=0
for r in sf:
    k=(nkey(r['firstName']+' '+r['lastName']),norm(r['parentAccount']).split(' ')[0])
    if (r['email'] and r['email'].lower() in live_emails) or k in live_names: kept+=1; continue
    b={'email':r['email']} if r['email'] else ({'linkedinUrl':r['linkedinUrl']} if r['linkedinUrl'] else None)
    if not b: continue
    b['motionStatus']='sf_stale'; res=curl('POST','/api/contacts',b); stale+=1 if (res.get('data') or {}).get('_id') else 0
print('SF rows matched by a live person',kept,'| marked sf_stale',stale)
