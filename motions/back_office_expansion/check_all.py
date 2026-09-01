#!/usr/bin/env python3
"""Pre-publish gate for the back-office maps. Exit 1 on any failure. Run after every rebuild, before any publish."""
import csv,re,subprocess,sys,os
from bo_set import load_set
HERE=os.path.dirname(os.path.abspath(__file__)); os.chdir(HERE)
CFG=load_set(); P=CFG["_paths"]; SET=["--set",CFG["_name"]]
rows=list(csv.DictReader(open(P["build_sheets_csv"])))
fail=[]; warn=[]
# 1 every lead has a LinkedIn URL and a title
for r in rows:
    if not r["linkedin_url"]: fail.append(f"no URL: {r['account']} | {r['full_name']}")
    if not r["title"].strip(): fail.append(f"no title: {r['account']} | {r['full_name']}")
# 2 level sanity
LVL={"C":0,"EVP":1,"SVP":2,"VP":3,"AVP":4,"Director":5}
n={(r["account"],r["full_name"]):r for r in rows}
for r in rows:
    t=r["title"].lower()
    if r["level"]=="C" and re.search(r"vice|avp|director",t) and "chief" not in t: fail.append(f"C-level misparse: {r['account']} | {r['full_name']} | {r['title'][:50]}")
    b=n.get((r["account"],r["reports_up_to"]))
    if b and LVL.get(b["level"],9)>LVL.get(r["level"],9): fail.append(f"level inversion: {r['account']} | {r['full_name']} ({r['level']}) under {b['full_name']} ({b['level']})")
    if r["reports_up_to"]!="Top of the map" and not b: fail.append(f"dangling manager: {r['account']} | {r['full_name']} -> {r['reports_up_to']}")
# 3 cap and density
from collections import Counter,defaultdict
per=Counter(r["account"] for r in rows)
for a,c in per.items():
    if c>30: fail.append(f"over cap: {a} {c}")
sib=defaultdict(int)
for r in rows: sib[(r["account"],r["reports_up_to"],r["level"],r["function"])]+=1
for k,c in sib.items():
    if c>3 and k[2] in ("Director","AVP"): warn.append(f"sibling density {c}: {k[0]} under {k[1]} ({k[2]}, {k[3]})")
# 4 generic titles that name no function
for r in rows:
    t=re.sub(r"\s+"," ",r["title"]).strip()
    if re.match(r"^(vice president|vp|senior vice president|svp|managing director)\s*[-,|]?\s*(platform solutions)?$",t,re.I): fail.append(f"generic title on map: {r['account']} | {r['full_name']} | {t}")
# 5 excluded people must not be on a map
SUBST=re.compile(r"retired|no longer|left |spectrum|stale|not found|does not match|profile url|sold to|title_excluded|off_target|clay record",re.I)
cand=list(csv.DictReader(open(P["candidates"])))
kept={(r["account"],r["full_name"]) for r in cand if not r["excluded_reason"].strip()}
ex={(r["account"],r["full_name"]) for r in cand if SUBST.search(r["excluded_reason"]) and (r["account"],r["full_name"]) not in kept}
for r in rows:
    if (r["account"],r["full_name"]) in ex: fail.append(f"excluded person on map: {r['account']} | {r['full_name']}")
# 6 AM-map people must not be on a map
am={(r["account"],r["full_name"]) for r in csv.DictReader(open(P["roster"])) if r["source"].startswith("am_map")} if P["roster"] and os.path.exists(P["roster"]) else set()
for r in rows:
    if (r["account"],r["full_name"]) in am: fail.append(f"AM-map person on a back-office map: {r['account']} | {r['full_name']}")
# 6a people in another live sequence at the account never land on a map
for r in rows:
    if (r["account"],r["full_name"]) in CFG["_collision"]: fail.append(f"sequence collision on map: {r['account']} | {r['full_name']} ({CFG['_collision'][(r['account'],r['full_name'])]})")
# 6b nothing lost: every kept candidate with a URL is on a map or on the bench
bench={(r["account"],r["full_name"]) for r in csv.DictReader(open(P["bench_csv"]))} if os.path.exists(P["bench_csv"]) else set()
onmap={(r["account"],r["full_name"]) for r in rows}
for r in cand:
    if not r["excluded_reason"].strip() and r["linkedin_url"] and r["full_name"] not in CFG["_drop"] and (r["account"],r["full_name"]) not in onmap and (r["account"],r["full_name"]) not in bench:
        fail.append(f"kept candidate lost (not on map, not benched): {r['account']} | {r['full_name']}")
# 7 built-map regression gate
out=subprocess.run([sys.executable,"diff_built_maps.py"]+SET,capture_output=True,text=True).stdout
changed="ANY CHANGE: True" in out
for line in out.splitlines():
    if line.startswith("- REMOVE") or line.startswith("- MOVE"): fail.append("built map altered: "+line[2:])
# 8 audit
aud=subprocess.run([sys.executable,"audit_maps.py"]+SET,capture_output=True,text=True).stdout.strip().splitlines()[-1]
print(f"leads {len(rows)} | {aud} | built maps changed: {changed}")
for w in warn: print("  warn:",w)
for f in fail: print("  FAIL:",f)
if changed: print(out)
sys.exit(1 if fail else 0)
