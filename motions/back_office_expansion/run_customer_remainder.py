#!/usr/bin/env python3
"""Run the paid checks for the customer-lane remainder (inputs from build_customer_remainder.py) and write the two
result files load_customer_wave.py merges: <scratch>/cust_fresh_result.json and <scratch>/cust_email_result.json.
  freshness : Clay managed routine Enrich Person (function:t_0thx4ohpCNT3KNijyVo, 0.5 cr/run, 20 per inline run)
  email     : Work Email + ZeroBounce workflow (workflow:wf_0tk4jo5z7RjGKo3rvR8, measured 1.05-1.6 cr/row, 100 per run)
  apollo    : rows in remainder_apollo.json are NOT sent to the Clay waterfall (JPMorgan rule); their Apollo matches are
              merged from <scratch>/remainder_apollo_results.json ({slug: {"email":..,"status":"valid"|""}}) written by
              the session after apollo_people_bulk_match, into cust_email_result.json with status valid.
Usage: run_customer_remainder.py <scratch> [--go] [--skip-fresh] [--skip-email]   (no --go = estimate only)
Then: load_customer_wave.py <scratch> [--go] merges every wave1/*.csv (remainder files included) and loads ready rows."""
import json,os,sys,subprocess,time
SP=sys.argv[1]; GO='--go' in sys.argv
FRESH="function:t_0thx4ohpCNT3KNijyVo"; EMAIL="workflow:wf_0tk4jo5z7RjGKo3rvR8"
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
def run_routine(rid,items,chunk):
    data=[]
    for i in range(0,len(items),chunk):
        part=items[i:i+chunk]
        start=clay(["routines","runs","start",rid,"--input",json.dumps({"items":part})])
        run_id=start.get("routineRunId") if isinstance(start,dict) else None
        if not run_id: print("  start failed",str(start)[:200]); continue
        print(f"  {rid} run {run_id} ({len(part)} rows)")
        got=[]; cur=None
        for _ in range(40):
            res=clay(["routines","runs","get",run_id,"--wait","60","--limit","100"]+(["--cursor",cur] if cur else []))
            if isinstance(res,dict) and res.get("status") in ("complete","completed","failed","error","processing_failed","validation_failed"):
                got+=res.get("data",[]); cur=res.get("cursor")
                if not cur: break
            else: time.sleep(5)
        if len(got)<len(part): print(f"  WARNING {run_id}: {len(got)} of {len(part)} results")
        data+=got
    return data
fresh=json.load(open(f"{SP}/remainder_fresh.json"))["items"]; email=json.load(open(f"{SP}/remainder_email.json"))["items"]; apollo=json.load(open(f"{SP}/remainder_apollo.json"))
print(f"freshness {len(fresh)} x 0.5 = {len(fresh)*0.5:.0f} | email {len(email)} x 1.05-1.6 = {len(email)*1.05:.0f}-{len(email)*1.6:.0f} | apollo {len(apollo)} (Apollo pool)")
if not GO: sys.exit(0)
b0=credits(); print("credits before",b0)
if "--skip-fresh" not in sys.argv:
    d=run_routine(FRESH,fresh,20); json.dump({"data":d},open(f"{SP}/cust_fresh_result.json","w")); print("freshness results",len(d),"credits now",credits())
if "--skip-email" not in sys.argv:
    d=run_routine(EMAIL,email,100)
    ap=os.path.join(SP,"remainder_apollo_results.json")
    if os.path.exists(ap):
        for k,v in json.load(open(ap)).items(): d.append({"id":k,"status":"complete","result":{"email":v.get("email",""),"status":v.get("status","")}})
    json.dump({"data":d},open(f"{SP}/cust_email_result.json","w")); print("email results",len(d))
b1=credits(); print("credits after",b1,"spent",round((b0 or 0)-(b1 or 0),1))
