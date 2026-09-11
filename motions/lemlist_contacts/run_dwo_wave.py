#!/usr/bin/env python3
"""Work Email + ZeroBounce (workflow routine wf_0tk4jo5z7RjGKo3rvR8, measured 1.6 credits a row) on a DWO live wave.
JPMorgan rule: bank-class domains new to the routine get a two-row PROBE first; a domain that returns nothing on both
probes is routed to Apollo (people match by name + domain) instead of the waterfall, which bills every provider attempt.
Usage: run_dwo_wave.py <scratch> --wave <wave1|wave2> --probe        (probes only, writes <scratch>/dwo_<wave>_routing.json)
       run_dwo_wave.py <scratch> --wave <wave1|wave2> --main         (everything not routed to Apollo, skips rows already run)
Results accumulate in <scratch>/dwo_<wave>_email_results.json keyed by clay_profile_id."""
import json,os,sys,subprocess,time,collections,re
SP=sys.argv[1]; WAVE=sys.argv[sys.argv.index('--wave')+1]; MODE='probe' if '--probe' in sys.argv else 'main'
EMAIL="workflow:wf_0tk4jo5z7RjGKo3rvR8"
BANK=re.compile(r'bank|barclays|blackrock|capitalone|fanniemae|freddiemac|hsbc|\bml\.com|morganstanley|navyfederal|raymondjames|ubs\.com|key\.com|santander|bmo\.com|flagstar|wsfs|firsthorizon|lpl\.com|mtb\.com|scotia|sc\.com|vanguard|fiserv|schwab|citizens|jpm|chase|truist|pnc|goldman|wellsfargo|usbank|synchrony|regions|huntington|bnymellon|statestreet|northerntrust|amex|discover|ally\.com|sofi|corebridge|transamerica',re.I)
RESOLVED={'citizensbank.com','thehartford.com','truist.com','regions.com','fidelity.com','paychex.com','centene.com','nationalgrid.com','gs.com','wellsfargo.com','syf.com','usbank.com','metlife.com','prudential.com','assurant.com','capita.com','foundever.com','aetna.com','cigna.com','elevancehealth.com','molinahealthcare.com','uhc.com','humana.com','blueshieldca.com','point32health.org','carefirst.com','vnshealth.org','devoted.com','medica.com'}
SKIP_DOMAINS={'unive.nl'}
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
def run_rows(rows):
    """rows: wave people. Returns {clay_profile_id: {email,status,raw}}"""
    out={}
    for i in range(0,len(rows),100):
        part=rows[i:i+100]
        items=[{'id':str(p['clay_profile_id']),'inputs':{'full_name':p['name'],'company_name':p['account'],'company_domain':p['domain'],'title':p['title'] or '','seniority':'','kind':'dwo_'+WAVE,'clay_profile_id':str(p['clay_profile_id'])}} for p in part]
        start=clay(["routines","runs","start",EMAIL,"--input",json.dumps({"items":items})]); rid=start.get("routineRunId")
        if not rid: print("  start failed",str(start)[:200]); continue
        print(f"  run {rid} ({len(part)} rows)",flush=True)
        # wait up to ~8 minutes; a run with all but a few rows finished for 2 minutes is harvested as is (hung rows happen)
        got=[]; t0=time.time(); near=None
        while time.time()-t0<480:
            res=clay(["routines","runs","get",rid,"--wait","30","--limit","100"])
            st=res.get("status"); fin=res.get("finished",0); tot=res.get("total",len(part))
            if st in ("complete","completed","failed","error","processing_failed","validation_failed"): break
            if fin>=tot-3: near=near or time.time()
            if near and time.time()-near>120: print(f"  {rid} stuck at {fin}/{tot}, moving on (rows re-run later if it never completes)"); routing.setdefault('pending_runs',[]).append(rid); break
        cur=None
        while True:
            res=clay(["routines","runs","get",rid,"--limit","100"]+(["--cursor",cur] if cur else []))
            got+=[it for it in res.get("data",[]) if it.get("status") in ("complete","failed")]; cur=res.get("cursor")
            if not cur: break
        for it in got:
            r=it.get('result') or {}; out[it['id']]={'email':r.get('email') or '','status':r.get('status') or ('failed' if it.get('status')=='failed' else '')}
        if len(got)<len(part): print(f"  WARNING {rid}: {len(got)} of {len(part)} results")
        # save progress after every run
        _rp=os.path.join(SP,f'dwo_{WAVE}_email_results.json'); _prev=json.load(open(_rp)) if os.path.exists(_rp) else {}; _prev.update(out); json.dump(_prev,open(_rp,'w'),indent=0)
    return out
waves=json.load(open(os.path.join(SP,'dwo_live_waves.json'))); rows=[p for p in waves[WAVE] if p['domain'] not in SKIP_DOMAINS]
rp=os.path.join(SP,f'dwo_{WAVE}_email_results.json'); results=json.load(open(rp)) if os.path.exists(rp) else {}
routp=os.path.join(SP,f'dwo_{WAVE}_routing.json'); routing=json.load(open(routp)) if os.path.exists(routp) else {'apollo_domains':[],'probed':{}}
by_dom=collections.defaultdict(list)
for p in rows: by_dom[p['domain']].append(p)
bank_new=[d for d,ps in by_dom.items() if BANK.search(d) and d not in RESOLVED and len(ps)>=3]
if MODE=='probe':
    todo=[]
    for d in bank_new:
        if d in routing['probed']: continue
        todo+=by_dom[d][:2]
    print(f'probing {len(bank_new)} bank domains, {len(todo)} rows, est {len(todo)*1.6:.0f} credits'); b0=credits()
    got=run_rows(todo); results.update(got)
    for d in bank_new:
        ids=[str(p['clay_profile_id']) for p in by_dom[d][:2]]; hits=sum(1 for i in ids if (got.get(i) or {}).get('email'))
        routing['probed'][d]=hits
        if hits==0: routing['apollo_domains'].append(d)
    b1=credits(); print('probe cost',round((b0 or 0)-(b1 or 0),1),'| domains to Apollo (0 of 2):',routing['apollo_domains'])
    print('probe hits by domain',routing['probed'])
else:
    todo=[p for p in rows if str(p['clay_profile_id']) not in results and p['domain'] not in routing['apollo_domains']]
    print(f'main run: {len(todo)} rows (skipping {len(rows)-len(todo)} already run or routed to Apollo), est {len(todo)*1.6:.0f}'); b0=credits()
    got=run_rows(todo); results.update(got)
    # merge any earlier hung runs that have since completed, before anything is re-run
    for rid in list(routing.get('pending_runs',[])):
        res=clay(["routines","runs","get",rid,"--limit","100"])
        if res.get('status') in ('complete','completed'):
            for it in res.get('data',[]):
                r=it.get('result') or {}; results.setdefault(it['id'],{'email':r.get('email') or '','status':r.get('status') or ''})
            routing['pending_runs'].remove(rid); print('  merged completed run',rid)
    b1=credits(); print('main cost',round((b0 or 0)-(b1 or 0),1))
json.dump(results,open(rp,'w'),indent=0); json.dump(routing,open(routp,'w'),indent=1)
c=collections.Counter(v['status'] or 'none' for v in results.values()); print('results so far',len(results),dict(c))
