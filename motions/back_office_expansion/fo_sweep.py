#!/usr/bin/env python3
"""Zero-credit front-office sourcing for a rep set: (1) Clay query-mode sweeps per account per lane (current role at the
account domain, US), (2) the Salesforce-known layer from Audiences (people on the account's SF Account ID whose title
names a front-office function). Writes sweeps/<set>/<account>.csv in the sweep schema plus a linkedin_url column
(Audiences rows carry it; search rows get it from the bridge). Run: fo_sweep.py --set nate_front"""
import csv,json,os,re,subprocess,sys,time
from bo_set import load_set
HERE=os.path.dirname(os.path.abspath(__file__)); CFG=load_set()
LANES={
 "Q1":["Chief Customer Officer","Chief Experience Officer","Chief Operating Officer","SVP Customer Service","SVP Customer Experience","SVP Contact Center Operations","SVP Member Services","EVP Customer Service","Head of Customer Operations","Head of Customer Service"],
 "Q2":["Vice President Contact Center Operations","Director Contact Center Operations","VP Customer Service Operations","Director of Call Center Operations","Director Customer Care","VP Customer Care","Director Member Services","Director Client Services","VP Service Delivery","Director of Customer Support"],
 "Q3":["Director of Workforce Management","Vice President Workforce Management","Director Workforce Planning","Director Real Time Operations","Director Capacity Planning","Head of Workforce Optimization","Director Forecasting and Scheduling"],
 "Q4":["Director Contact Center Technology","VP Contact Center Technology","Director Customer Experience Technology","Director Customer Service Technology","VP CCaaS","Director Telephony","Director Digital Customer Service","VP Customer Experience Platforms"]}
FO_TITLE=["contact center","call center","customer service","customer care","customer experience","customer operations","member services","client services","workforce","real time","real-time","intraday","capacity planning","forecasting","service delivery","customer support","telephony","ivr","ccaas","omnichannel","service center","customer engagement"]
def clay(a,tries=4):
    for i in range(tries):
        r=subprocess.run(["clay"]+a,capture_output=True,text=True)
        if r.returncode==0 and r.stdout.strip():
            try: return json.loads(r.stdout)
            except Exception: pass
        if "rate" in (r.stderr+r.stdout).lower(): time.sleep(8+5*i); continue
        time.sleep(2)
    return {}
def bin_(k,op,v): return {"type":"BinOp","key":k,"dataPath":["contact_entity_field_values","field",k],"operator":op,"value":v,"entityType":"CONTACT"}
COLS=["clay_profile_id","full_name","title","company_name","location","start_date","query_tag","linkedin_url","sf_status"]
for acct,spec in CFG["accounts"].items():
    rows={}; doms=spec["domains"]
    for tag,titles in LANES.items():
        q='select from people where experiences.any(is_current = true and company.domain in (%s) and job_title is_similar_to (%s)) and location_country = "United States"'%(", ".join('"%s"'%d for d in doms), ", ".join('"%s"'%t for t in titles))
        s=clay(["search","query-mode","create","--query",q]); sid=s.get("searchId") if isinstance(s,dict) else None
        if not sid: print(acct,tag,"create failed",str(s)[:160]); continue
        n=0
        for _ in range(6):
            d=clay(["search","query-mode","run",sid,"--limit","500"]); data=d.get("data",[]) if isinstance(d,dict) else []
            for p in data:
                ex=(p.get("matched_experiences") or [{}])[0]; key=re.sub(r"[^a-z ]","",p.get("name","").lower()).strip()
                if key in rows: rows[key]["query_tag"]+=","+tag; continue
                rows[key]={"clay_profile_id":p.get("clay_profile_id",""),"full_name":p.get("name",""),"title":ex.get("title",""),"company_name":ex.get("company",""),"location":(p.get("location") or {}).get("name",""),"start_date":ex.get("start_date",""),"query_tag":tag,"linkedin_url":"","sf_status":""}
            n+=len(data)
            if not (isinstance(d,dict) and d.get("hasMore")): break
        print(acct,tag,n,"rows"); time.sleep(1.5)
    # Salesforce-known layer (0 credits)
    sf=0
    for sid in spec.get("sf_account_ids",[]):
        flt={"type":"GroupOp","combinationMode":"And","items":[bin_("audf_0timw68Jf4dTsQQqq38","Equal",sid),{"type":"GroupOp","combinationMode":"Or","items":[bin_("title","Contain",w) for w in FO_TITLE]}]}
        ids=clay(["audiences","records","search-ids","--entity-type","people","--filter",json.dumps(flt),"--limit","1000"]).get("data",[])
        for i in range(0,len(ids),100):
            for r in clay(["audiences","records","get","--entity-type","people","--ids",",".join(str(x) for x in ids[i:i+100])]).get("data",[]):
                f=r["fields"]; name=f"{f.get('first_name') or ''} {f.get('last_name') or ''}".strip(); key=re.sub(r"[^a-z ]","",name.lower()).strip()
                if not name or not f.get("title"): continue
                if key in rows:
                    rows[key]["query_tag"]+=",SF"; rows[key]["linkedin_url"]=rows[key]["linkedin_url"] or (f.get("linkedin_url") or ""); rows[key]["sf_status"]=str(f.get("audf_0timw8mQ9wKWoXv23X5") or ""); continue
                rows[key]={"clay_profile_id":"","full_name":name,"title":f.get("title") or "","company_name":str(f.get("audf_0tkdvkhYzHJGF3NrfqG") or acct),"location":", ".join(x for x in [f.get("location_city"),f.get("location_state")] if x),"start_date":"","query_tag":"SF","linkedin_url":f.get("linkedin_url") or "","sf_status":str(f.get("audf_0timw8mQ9wKWoXv23X5") or "")}
                sf+=1
    print(acct,"SF-known added",sf,"| total",len(rows))
    with open(os.path.join(HERE,spec["sweep"]),"w",newline="") as fh:
        w=csv.DictWriter(fh,fieldnames=COLS); w.writeheader(); w.writerows(rows.values())
