#!/usr/bin/env python3
"""Join the wave-1 per-lead copy (wave1_variables_batch*.json) to the Audiences pull (the candidates CSV
passed as argv[1]) by name, run the doctrine QC, and write WFM_Present_Wave1_Load_Sep5.csv.
Emails always come from Audiences, never from the copy files. Nothing is loaded into lemlist here."""
import csv, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
cand_path = sys.argv[1]
cand = {(r["first_name"].strip().lower(), r["last_name"].strip().lower()): r
        for r in csv.DictReader(open(cand_path))}
b1 = json.load(open(os.path.join(HERE, "wave1_variables_batch1.json")))
b2 = json.load(open(os.path.join(HERE, "wave1_variables_batch2.json")))
shared = b1["_shared"]
rows, missing, issues = [], [], []
for L in b1["leads"] + b2["leads"]:
    r = cand.get((L["firstName"].lower(), L["lastName"].lower()))
    if not r:
        m = [v for k, v in cand.items() if k[1] == L["lastName"].lower()]
        r = m[0] if len(m) == 1 else None
    if not r:
        missing.append(f"{L['firstName']} {L['lastName']}")
        continue
    row = {"email": r["email"], "firstName": r["first_name"], "lastName": r["last_name"], "companyName": L["company"],
           "jobTitle": r["title"], "linkedinUrl": r["linkedin_url"], "opener": L["opener"], "angleIdea": L["angleIdea"],
           "angleProof": shared["angleProof"], "angleAsk": L["angleAsk"], "peak": L["peak"], "workTeams": L["workTeams"],
           "wfmPlatform": L["wfmPlatform"], "acdPlatform": L["acdPlatform"], "colleagueFirst": L.get("colleagueFirst", ""),
           "colleagueLine": L.get("colleagueLine", ""), "motion": "wfm_present", "motionStatus": "wave1_staged",
           "domain": r["domain"], "acdLastSeen": r["acd_seen"]}
    e1 = " ".join([row["opener"], row["angleIdea"], row["angleProof"], row["angleAsk"]])
    words = len(e1.split()) + 3
    if words > 110:
        issues.append((row["email"], "E1 words", words))
    for k in ("opener", "angleIdea", "angleAsk", "colleagueLine"):
        if "—" in row[k]:
            issues.append((row["email"], "em dash", k))
        if re.search(r"hope you're well|sorry|leverage|comparing notes|I'll be quick", row[k], re.I):
            issues.append((row["email"], "banned phrase", k))
    if row["angleAsk"].count("?") != 1:
        issues.append((row["email"], "ask must be one question", row["angleAsk"]))
    rows.append(row)
out = os.path.join(HERE, "WFM_Present_Wave1_Load_Sep5.csv")
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
print(f"rows {len(rows)} | unmatched {missing} | QC issues {issues or 'none'} | wrote {out}")
