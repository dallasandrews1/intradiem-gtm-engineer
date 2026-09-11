#!/usr/bin/env python3
"""Add a hand-picked cohort for ONE account to one of the four vertical customer-lane campaigns (or any campaign id).
Built Sep 4 2026 for Nathan's "add MAXIMUS to the BPO campaign" ask; reusable for the next "add <account>" request.
Input: cohorts/<name>.csv with columns account,vertical,companyDomain,full_name,firstName,lastName,title,linkedin_url,function
Steps (same routines the customer lane used):
  1. Salesforce presence, 0 credits: Audiences people by LinkedIn slug, then exact name (sf_check.py method). Information only.
  2. Freshness: Clay managed routine Enrich Person (function:t_0thx4ohpCNT3KNijyVo, 0.5 cr/row); no current role, or a
     current org that is not the account, = hold.
  3. Work email: Work Email + ZeroBounce workflow (workflow:wf_0tk4jo5z7RjGKo3rvR8, measured 1.05-1.6 cr/row); only a
     'valid' address at the account domain loads.
  4. Load into the vertical campaign (customer_lane_config.json campaign_ids) by POST /leads/{email}?deduplicate=true with
     firstName,lastName,linkedinUrl,companyName,companyDomain,jobTitle,function,parent_account,enterprise_line.
Dry-run by default (steps 1 only, zero credits, prints the estimate). --go runs 2-4. Never starts or activates a campaign.
Writes cohorts/<name>_result.csv and appends loaded leads to _last_customer_load.json."""
import csv,json,os,re,sys,subprocess,time,urllib.parse,collections
HERE=os.path.dirname(os.path.abspath(__file__)); GO='--go' in sys.argv
name=[a for a in sys.argv[1:] if not a.startswith('--')][0]
IN=os.path.join(HERE,'cohorts',f'{name}.csv'); OUT=os.path.join(HERE,'cohorts',f'{name}_result.csv')
cfg=json.load(open(os.path.join(HERE,'customer_lane_config.json')))
ENV='/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/config/lemlist.env'
KEY=[l.split('=',1)[1].strip() for l in open(ENV) if l.startswith('LEMLIST_API_KEY=')][0]
FRESH="function:t_0thx4ohpCNT3KNijyVo"; EMAIL="workflow:wf_0tk4jo5z7RjGKo3rvR8"
F={"company":"audf_0tkdvkhYzHJGF3NrfqG","acct":"audf_0timw68Jf4dTsQQqq38","status":"audf_0timw8mQ9wKWoXv23X5","owner":"audf_0timw93AWnwkAbNguBv","li":"linkedin_url","fn":"first_name","ln":"last_name"}
def clay(args,tries=3):
    for i in range(tries):
        r=subprocess.run(["clay"]+args,capture_output=True,text=True)
        if r.returncode==0 and r.stdout.strip():
            try: return json.loads(r.stdout)
            except Exception: pass
        time.sleep(3+3*i)
    return {}
def credits():
    d=clay(["credits"]); return d.get("balance") if isinstance(d,dict) else None
def curl(method,path,body=None):
    a=['curl','-s','-u',f':{KEY}','-X',method,'https://api.lemlist.com'+path,'-H','Content-Type: application/json']
    if body is not None: a+=['-d',json.dumps(body)]
    out=subprocess.run(a,capture_output=True,text=True).stdout
    try: return json.loads(out)
    except Exception: return {'raw':out}
def bin_(k,op,v): return {"type":"BinOp","key":k,"dataPath":["contact_entity_field_values","field",k],"operator":op,"value":v,"entityType":"CONTACT"}
def group(items): return {"type":"GroupOp","combinationMode":"And","items":items}
def search(flt,limit=5):
    d=clay(["audiences","records","search-ids","--entity-type","people","--filter",json.dumps(flt),"--limit",str(limit)]); return d.get("data",[]) if isinstance(d,dict) else []
def get(ids):
    if not ids: return []
    d=clay(["audiences","records","get","--entity-type","people","--ids",",".join(str(i) for i in ids[:20])]); return d.get("data",[]) if isinstance(d,dict) else []
def slug(u): return re.sub(r'/+$','',(u or '').lower().split('linkedin.com/in/')[-1]).strip('/')
def run_routine(rid,items,chunk):
    data=[]
    for i in range(0,len(items),chunk):
        part=items[i:i+chunk]; start=clay(["routines","runs","start",rid,"--input",json.dumps({"items":part})])
        run_id=start.get("routineRunId") if isinstance(start,dict) else None
        if not run_id: print("  start failed",str(start)[:200]); continue
        print(f"  {rid} run {run_id} ({len(part)} rows)"); got=[]; cur=None
        for _ in range(40):
            res=clay(["routines","runs","get",run_id,"--wait","60","--limit","100"]+(["--cursor",cur] if cur else []))
            if isinstance(res,dict) and res.get("status") in ("complete","completed","failed","error","processing_failed","validation_failed"):
                got+=res.get("data",[]); cur=res.get("cursor")
                if not cur: break
            else: time.sleep(5)
        data+=got
    return data

rows=list(csv.DictReader(open(IN)))
acct=rows[0]['account']; v=rows[0]['vertical']; cid=cfg['campaign_ids'][v]; dom=rows[0]['companyDomain']
aliases=[acct.lower(),acct.split()[0].lower()]
for r in rows:
    r.update({'in_salesforce':'no','sf_note':'','fresh':'','email':'','email_status':'','load_status':'','lead_id':''})
    ids=search(group([bin_(F['li'],'Contain','/in/'+slug(r['linkedin_url']))])) if r['linkedin_url'] else []
    method='linkedin' if ids else ''
    if not ids and r['firstName'] and r['lastName']:
        ids=search(group([bin_(F['fn'],'Equal',r['firstName']),bin_(F['ln'],'Equal',r['lastName'])]),10); method='name' if ids else ''
    recs=get(ids)
    if recs:
        f=recs[0]['fields']; comp=str(f.get(F['company']) or '')
        r['in_salesforce']='yes' if method=='linkedin' else 'possible'
        r['sf_note']=f"{method} match: {comp} | status {f.get(F['status']) or ''} | owner {f.get(F['owner']) or ''}"
have={(l.get('email') or '').lower() for l in (curl('GET',f'/api/campaigns/{cid}/export/leads?state=all&format=json') or [])}
print(f"{acct} -> {v} {cid} ({len(have)} leads in campaign now) | {len(rows)} in cohort")
for r in rows: print(f"  {r['full_name']:22} {r['title'][:52]:52} SF {r['in_salesforce']:8} {r['sf_note'][:70]}")
print(f"estimate: freshness {len(rows)} x 0.5 = {len(rows)*0.5:.1f} | email {len(rows)} x 1.05-1.6 = {len(rows)*1.05:.1f}-{len(rows)*1.6:.1f} | total {len(rows)*1.55:.1f}-{len(rows)*2.1:.1f} credits")
if not GO: sys.exit(0)
b0=credits(); print('credits before',b0)
fr=run_routine(FRESH,[{'id':slug(r['linkedin_url']),'inputs':{'Professional Profile URL':r['linkedin_url']}} for r in rows],20)
fres={}
for it in fr:
    res=(it.get('result') or {}).get('Enrich person') or {}
    fres[urllib.parse.unquote(it['id'])]={'ok':it.get('status')=='complete','cur':res.get('current_experience') or [],'org':res.get('org'),'title':res.get('title')}
for r in rows:
    f=fres.get(slug(r['linkedin_url']))
    if not f or not f['ok'] or not f['cur']: r['load_status']='hold'; r['fresh']='no current role returned'; continue
    org=' '.join(str((c or {}).get('company') or (c or {}).get('org') or (c or {}).get('name') or '') for c in f['cur']).lower()+' '+str(f['org'] or '').lower()
    if not any(a in org for a in aliases): r['load_status']='hold'; r['fresh']='now at '+(f['org'] or org.strip()[:40] or '?')
    else: r['fresh']='current at '+acct+(f" ({f['title']})" if f['title'] else '')
print('freshness done, credits now',credits())
todo=[r for r in rows if r['load_status']!='hold']
em=run_routine(EMAIL,[{'id':slug(r['linkedin_url']),'inputs':{'full_name':r['full_name'],'company_name':acct,'company_domain':dom,'title':r['title'],'seniority':'','kind':f'bo_cohort_{name}','clay_profile_id':''}} for r in todo],100)
eres={it['id']:(it.get('result') or {}) for it in em}
for r in todo:
    e=eres.get(slug(r['linkedin_url']),{}); addr=(e.get('email') or '').lower(); st=e.get('status') or ''
    r['email']=addr; r['email_status']=st
    if st=='valid' and addr.endswith('@'+dom): r['load_status']='ready'
    else: r['load_status']='needs_email'
print('email done, credits now',credits())
loaded=[]
for r in rows:
    if r['load_status']!='ready': continue
    if r['email'] in have: r['load_status']='already_in'; continue
    body={'firstName':r['firstName'],'lastName':r['lastName'],'linkedinUrl':r['linkedin_url'],'companyName':acct,'companyDomain':dom,'jobTitle':r['title'],
          'function':r['function'],'parent_account':cfg['parent_account'].get(acct,acct),'enterprise_line':cfg['neutral_line'][v]}
    res=curl('POST',f'/api/campaigns/{cid}/leads/{r["email"]}?deduplicate=true',body)
    if res.get('_id'): r['load_status']='loaded'; r['lead_id']=res['_id']; loaded.append({'email':r['email'],'leadId':res['_id'],'account':acct,'campaign':cid})
    else: r['load_status']='error '+str(res)[:100]
b1=credits(); print('credits after',b1,'spent',round((b0 or 0)-(b1 or 0),1))
for r in rows: print(f"  {r['full_name']:22} {r['load_status']:12} {r['email']:40} {r['fresh'][:50]}")
w=csv.DictWriter(open(OUT,'w',newline=''),fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
lp=os.path.join(HERE,'_last_customer_load.json'); prev=json.load(open(lp)) if os.path.exists(lp) else []
json.dump(prev+loaded,open(lp,'w'),indent=1)
print(v,cid,'now',len(curl('GET',f'/api/campaigns/{cid}/export/leads?state=all&format=json') or []),'leads')
