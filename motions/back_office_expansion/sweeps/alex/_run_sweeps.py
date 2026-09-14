#!/usr/bin/env python3
"""Sep 11 2026 sweep for Alex Bauer's Elevance Health family (customer, back-office expansion). Clay advanced search (0 credits, quota-metered).
Writes sweeps/alex/<account>.csv in the pipeline schema: clay_profile_id, full_name, title, company_name, location, start_date, query_tag.
US-located people only: the offshore back office (Carelon Global Solutions) is not the buyer for a Sales Nav map."""
import csv, json, os, re, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
def clay(args, tries=4):
    for i in range(tries):
        r = subprocess.run(["clay"] + args, capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip():
            try: return json.loads(r.stdout)
            except Exception: pass
        if "rate" in (r.stderr + r.stdout).lower(): time.sleep(12 + 6 * i); continue
        time.sleep(2)
    return {}
def search(q):
    d = clay(["search", "query-mode", "create", "--query", q])
    sid = d.get("searchId")
    if not sid: print("   CREATE FAILED:", d, "\n   q:", q[:160]); return []
    out = []
    while True:
        p = clay(["search", "query-mode", "run", sid, "--limit", "500"])
        out += p.get("data", []) or []
        if not p.get("hasMore"): break
    return out

EXEC = 'job_title contains ("chief operating", "chief operations", "chief administrative", "chief operations officer", "executive vice president", "senior vice president", "staff vice president", "staff vp") or seniority = "C-suite"'
OPS  = 'job_title is_similar_to ("Vice President Operations", "Director Operations", "Head of Operations", "Senior Director Operations", "Vice President Shared Services", "Director Business Operations", "Staff Vice President Operations")'
WFM  = 'job_title contains ("workforce", "capacity planning", "resource planning", "workforce planning", "workforce management", "scheduling", "forecasting")'
TECH = 'job_title contains ("product owner", "business systems", "operations technology", "operations platform", "process automation", "intelligent automation", "operational excellence", "process excellence", "continuous improvement", "business process")'
BO   = 'job_title contains ("back office", "back-office", "shared services", "service delivery", "operations support", "fulfillment", "transaction", "processing")'
PAY1 = 'job_title contains ("claims", "enrollment", "billing", "membership", "appeals", "grievance", "utilization management", "provider data", "provider operations", "provider services", "payment integrity", "cost containment", "recovery")'
PAY2 = 'job_title contains ("pharmacy operations", "pharmacy services", "benefits administration", "encounter", "eligibility", "premium", "reconciliation", "correspondence", "document", "intake", "configuration", "benefit configuration", "quality operations", "service operations", "care operations")'

CO = '(company_name contains ("Elevance Health", "Elevance", "Anthem, Inc", "Anthem Inc", "Anthem Blue Cross", "Anthem BlueCross", "Anthem Health", "Anthem National", "Carelon", "CarelonRx", "Carelon Behavioral Health", "Carelon Services", "Carelon Insights", "Wellpoint", "Amerigroup", "Empire BlueCross", "Empire Blue Cross", "Beacon Health Options", "IngenioRx", "Healthy Blue", "Simply Healthcare", "UniCare", "Paragon Healthcare", "myNEXUS", "Aspire Health", "Blue Cross Blue Shield of Georgia", "Anthem Blue Cross and Blue Shield", "Kroger Specialty Pharmacy") or company_name = "Anthem")'
ACCOUNTS = {
 "elevance_health": {"co": CO, "person": ' and location_country = "United States"',
                     "lanes": {"Q1": EXEC, "Q2": OPS, "Q3": WFM, "Q4": TECH, "Q5": BO, "Q6": PAY1, "Q7": PAY2},
                     "keep": re.compile(r"elevance|\banthem\b|carelon|wellpoint|amerigroup|empire blue|beacon health|ingenio|healthy blue|simply healthcare|unicare|paragon healthcare|mynexus|aspire health|kroger specialty", re.I),
                     "drop": re.compile(r"anthem (sports|entertainment|press|music|technolog|ventures|properties|biosciences|group|media|marketing|capital|security|cyber)|anthemis|anthem\.co|beacon health system|anthem, ohio|anthem az|anthem arizona|wellpoint health networks", re.I)},
}
only = [a for a in sys.argv[1:] if a in ACCOUNTS] or list(ACCOUNTS)
for acct in only:
    spec = ACCOUNTS[acct]; rows = {}; per = {}
    for tag, lane in spec["lanes"].items():
        q = f'select from people where experiences.any(is_current = true and {spec["co"]} and ({lane})){spec.get("person","")}'
        res = search(q); per[tag] = len(res)
        for p in res:
            for e in p.get("matched_experiences", []):
                co = e.get("company") or ""
                if not spec["keep"].search(co) or spec["drop"].search(co): continue
                pid = p["clay_profile_id"]
                if pid in rows: continue
                rows[pid] = {"clay_profile_id": pid, "full_name": p.get("name") or "", "title": e.get("title") or "", "company_name": co,
                             "location": (p.get("location") or {}).get("name") or "", "start_date": e.get("start_date") or "", "query_tag": tag}
                break
        print(f"   {tag}: {len(res)} raw, {len(rows)} unique so far", flush=True)
        time.sleep(1)
    out = os.path.join(HERE, f"{acct}.csv")
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["clay_profile_id", "full_name", "title", "company_name", "location", "start_date", "query_tag"])
        w.writeheader(); w.writerows(rows.values())
    print(f"{acct:16s} raw per lane {per}  -> {len(rows)} unique kept")
