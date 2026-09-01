#!/usr/bin/env python3
"""Structural audit of a set's build sheet (--set <name>): prints, per account, the defects Dallas keeps finding."""
import csv,sys,os
from collections import defaultdict
from bo_set import load_set
CFG=load_set()
rows=list(csv.DictReader(open(CFG["_paths"]["build_sheets_csv"])))
LVL={"C":0,"EVP":1,"SVP":2,"VP":3,"AVP":4,"Director":5}
by=defaultdict(list)
for r in rows: by[r["account"]].append(r)
total=0
for a,rs in by.items():
    n={r["full_name"]:r for r in rs}
    issues=[]; notes=[]
    for r in rs:
        boss=n.get(r["reports_up_to"])
        if r["level"]=="Director" and (boss is None or boss["level"] in ("C","EVP")):
            issues.append(f"director with no VP/AVP above: {r['full_name']} ({r['title'][:40]}) -> {r['reports_up_to']}")
        if boss and LVL.get(boss["level"],9)>LVL.get(r["level"],9):
            issues.append(f"level inversion: {r['full_name']} ({r['level']}) reports to {boss['full_name']} ({boss['level']})")
        elif boss and LVL.get(boss["level"],9)==LVL.get(r["level"],9):
            notes.append(f"same level, broad remit: {r['full_name']} under {boss['full_name']} (inferred, confirm)")
    for r in rs:
        if r["reports_up_to"]=="Top of the map" and not [x for x in rs if x["reports_up_to"]==r["full_name"]] and r["level"] not in ("C","EVP"):
            issues.append(f"floating card (no manager, no reports): {r['full_name']} ({r['level']}, {r['title'][:36]})")
    tops=[r for r in rs if r["reports_up_to"]=="Top of the map"]
    if len([t for t in tops if t["level"] not in ("C","EVP")])>2: issues.append(f"{len(tops)} top cards, several below EVP; missing an executive above them")
    total+=len(issues)
    print(f"\n{a}: {len(rs)} leads, {len(issues)} issues")
    for i in issues: print("  -",i)
    for i in notes: print("  ~",i)
print("\nTOTAL issues:",total)
