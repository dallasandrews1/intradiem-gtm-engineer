#!/usr/bin/env python3
"""Sep 9 2026 sweep for JW's four Canadian accounts. Clay advanced search (0 credits, quota-metered).
Writes sweeps/jw/<account>.csv in the pipeline schema: clay_profile_id, full_name, title, company_name, location, start_date, query_tag."""
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

EXEC = 'job_title contains ("chief operating", "chief operations", "chief administrative", "chief operations officer", "executive vice president", "senior vice president") or seniority = "C-suite"'
OPS  = 'job_title is_similar_to ("Vice President Operations", "Director Operations", "Head of Operations", "Senior Director Operations", "Vice President Shared Services", "Director Business Operations")'
WFM  = 'job_title contains ("workforce", "capacity planning", "resource planning", "workforce planning", "workforce management", "scheduling", "forecasting")'
TECH = 'job_title contains ("product owner", "business systems", "operations technology", "operations platform", "process automation", "intelligent automation", "operational excellence", "process excellence", "continuous improvement", "business process")'
BO   = 'job_title contains ("back office", "back-office", "middle office", "shared services", "service delivery", "operations support", "fulfillment", "transaction", "processing")'
TELCO1 = 'job_title contains ("billing", "revenue assurance", "credit", "collections", "receivables", "invoicing")'
TELCO2 = 'job_title contains ("provisioning", "activation", "order management", "service assurance", "customer operations", "client operations", "service operations", "order fulfillment")'
BANK1  = 'job_title contains ("loan operations", "lending operations", "mortgage operations", "deposit operations", "loan servicing", "mortgage servicing", "credit operations", "default", "loan administration")'
BANK2  = 'job_title contains ("payments", "payment operations", "onboarding", "kyc", "aml operations", "wealth operations", "investment operations", "securities operations", "settlement", "reconciliation", "custody", "treasury operations", "card operations")'
INS1   = 'job_title contains ("claims", "disability", "group operations", "group benefits", "group life", "health and dental", "absence")'
INS2   = 'job_title contains ("policy administration", "policy services", "new business", "plan member", "plan sponsor", "benefits administration", "underwriting operations", "contract administration", "annuit", "retirement operations")'

ACCOUNTS = {
 "bell_canada": {"co": '(company_name contains ("Bell Canada", "Bell Mobility", "Bell Business Markets", "Bell Media", "Bell Aliant", "Bell MTS", "BCE") or company_name = "Bell")', "person": ' and location_country = "Canada"',
                 "lanes": {"Q1": EXEC, "Q2": OPS, "Q3": WFM, "Q4": TECH, "Q5": BO, "Q6": TELCO1, "Q7": TELCO2},
                 "keep": re.compile(r"\bbell\b|\bbce\b", re.I), "drop": re.compile(r"taco|bell textron|bell helicopter|bell flight|bellsouth|bell labs|bell & ", re.I)},
 "telus":       {"co": '(company_name contains ("TELUS", "Telus Communications", "Telus Health", "Telus Mobility", "Telus Business", "Koodo", "Public Mobile"))',
                 "lanes": {"Q1": EXEC, "Q2": OPS, "Q3": WFM, "Q4": TECH, "Q5": BO, "Q6": TELCO1, "Q7": TELCO2},
                 "keep": re.compile(r"telus|koodo|public mobile", re.I), "drop": re.compile(r"international|digital|telus agriculture", re.I)},
 "bmo":         {"co": '(company_name contains ("BMO", "Bank of Montreal", "BMO Financial Group", "BMO Harris", "BMO Nesbitt Burns", "BMO Capital Markets", "BMO Private Wealth"))',
                 "lanes": {"Q1": EXEC, "Q2": OPS, "Q3": WFM, "Q4": TECH, "Q5": BO, "Q6": BANK1, "Q7": BANK2},
                 "keep": re.compile(r"\bbmo\b|bank of montreal", re.I), "drop": re.compile(r"^$")},
 "canada_life": {"co": '(company_name contains ("Canada Life", "Great-West Life", "Great-West Lifeco", "London Life", "Great West Life", "Canada Life Assurance"))',
                 "lanes": {"Q1": EXEC, "Q2": OPS, "Q3": WFM, "Q4": TECH, "Q5": BO, "Q6": INS1, "Q7": INS2},
                 "keep": re.compile(r"canada life|great.west|london life|lifeco", re.I), "drop": re.compile(r"irish life|putnam|empower", re.I)},
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
        time.sleep(1)
    out = os.path.join(HERE, f"{acct}.csv")
    with open(out, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["clay_profile_id", "full_name", "title", "company_name", "location", "start_date", "query_tag"])
        w.writeheader(); w.writerows(rows.values())
    print(f"{acct:12s} raw per lane {per}  -> {len(rows)} unique kept")
