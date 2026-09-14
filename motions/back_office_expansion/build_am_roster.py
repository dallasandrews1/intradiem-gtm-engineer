#!/usr/bin/env python3
"""Set-driven Back Office Account Map roster for a customer account (the Inger variant, generalised Sep 11 2026 for Alex Bauer).
Inputs (from sets/<name>.json): am, am_inbox (transcribed AM Relationship Map CSVs, map_*.csv), files.known_people (Salesforce-known
contacts from Audiences, 0 credits). Outputs: files.roster, files.roster_summary. Same gates as build_inger_roster.py:
  1 known_to_intradiem   : every card on the AM's map (placeholders included), or a Salesforce-known contact by name/email
  2 sponsor_line_conflict: reports to the same leader as a known contact (map cards only)
  3 band                 : SVP..Director in a back-office function, or a distinct-line top officer
Nothing here spends a credit. Run: python3 build_am_roster.py --set alex"""
import csv, glob, os, re, sys
from collections import defaultdict
from bo_set import load_set
from build_inger_roster_lib import infer_band, infer_function, in_band, norm   # shared title rules
CFG = load_set(); P = CFG["_paths"]
INBOX = os.path.expanduser(CFG["am_inbox"]); AM = CFG["am"]
ACCOUNTS = list(CFG["accounts"].keys())
def canon_account(name):
    n = (name or "").lower()
    for a in ACCOUNTS:
        if a.lower() in n or n in a.lower(): return a
    return (name or "").strip()
known_names = defaultdict(set); known_emails = set(); known_rows = 0
if P.get("known_people") and os.path.exists(P["known_people"]):
    for r in csv.DictReader(open(P["known_people"])):
        known_rows += 1; known_names[canon_account(r.get("account"))].add(norm(r.get("full_name")))
        e = (r.get("email") or "").strip().lower()
        if e: known_emails.add(e)
maps = []
for f in sorted(glob.glob(os.path.join(INBOX, "map_*.csv"))):
    for r in csv.DictReader(open(f)):
        r["_file"] = os.path.basename(f); r["account"] = canon_account(r.get("account")); maps.append(r)
cols = ["account","am_owner","full_name","title","title_truncated","function","band","reports_to","tree_depth","source","crm_badge",
        "known_to_intradiem","sponsor_line_conflict","band_ok","gate_result","owner_cleared","sequence_state","email","linkedin_url","notes"]
out = []; by_acct = defaultdict(list)
for r in maps: by_acct[r["account"]].append(r)
for acct, rows in by_acct.items():
    canvas = [r for r in rows if (r.get("source") or "map") == "map"]
    parent_of = {r["full_name"]: (r.get("reports_to") or "") for r in canvas}
    is_known = {r["full_name"]: True for r in canvas}
    sponsor_leaders = {parent_of[n] for n, k in is_known.items() if k and parent_of.get(n)}
    for r in rows:
        name = r["full_name"]; src = r.get("source") or "map"
        k = is_known.get(name, norm(name) in known_names.get(acct, set()))
        leader = parent_of.get(name, "")
        conflict = "yes" if (leader and leader in sponsor_leaders) or (name in sponsor_leaders) else ("no" if src == "map" else "unknown")
        band = infer_band(r.get("title")); func = infer_function(r.get("title"))
        band_ok = "yes" if in_band(band) else ("top_officer" if band in ("C","EVP") else "no")
        gate = "KNOWN_do_not_touch" if k else ("CONFLICT_am_decides" if conflict == "yes" else ("HOLD_below_band" if band_ok == "no" else ("HOLD_contact_center_line" if func == "contact_center" else "CANDIDATE")))
        out.append({"account":acct,"am_owner":AM,"full_name":name,"title":r.get("title",""),"title_truncated":r.get("title_truncated",""),"function":func,"band":band,
                    "reports_to":leader,"tree_depth":r.get("tree_depth",""),"source":f"am_map:{src}","crm_badge":r.get("crm_status",""),"known_to_intradiem":"yes" if k else "no",
                    "sponsor_line_conflict":conflict,"band_ok":band_ok,"gate_result":gate,"owner_cleared":"pending_owner" if gate=="CANDIDATE" else "","sequence_state":"",
                    "email":"","linkedin_url":"","notes":r.get("notes","")})
out.sort(key=lambda r: (r["account"], r["gate_result"] != "CANDIDATE", r["band"], r["full_name"]))
with open(P["roster"], "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(out)
lines = [f"# {CFG['rep_short']} roster summary\n", f"Known layer rows loaded: {known_rows}. Map files: {len(glob.glob(os.path.join(INBOX,'map_*.csv')))}. Roster rows: {len(out)}.\n",
         "| Account | map cards | known | conflict | candidates | held (band/CC) |", "|---|---|---|---|---|---|"]
accts = sorted({r["account"] for r in out})
for a in accts:
    rs = [r for r in out if r["account"] == a]
    lines.append(f"| {a} | {sum(1 for r in rs if r['source'].startswith('am_map:map'))} | {sum(1 for r in rs if r['gate_result']=='KNOWN_do_not_touch')} | {sum(1 for r in rs if r['gate_result']=='CONFLICT_am_decides')} | {sum(1 for r in rs if r['gate_result']=='CANDIDATE')} | {sum(1 for r in rs if r['gate_result'].startswith('HOLD'))} |")
lines.append("\n## Sponsor-line leaders per account (rule 1: nobody who reports into these is touched without the AM)\n")
for a in accts:
    canvas = [r for r in out if r["account"] == a and r["source"] == "am_map:map"]
    leaders = [f"{r['full_name']} ({r['title'][:40]})" for r in canvas if r["tree_depth"] == "0" or any(c["reports_to"] == r["full_name"] for c in canvas)]
    lines.append(f"- **{a}**: {'; '.join(leaders)}. Map functions: {', '.join(sorted({r['function'] for r in canvas}))}.")
missing = [a for a in ACCOUNTS if a not in accts]
if missing: lines.append(f"\nNo AM map transcribed for: {', '.join(missing)} (net-new-style build for that account: no sponsor line to protect beyond the parent map)")
open(P["roster_summary"], "w").write("\n".join(lines) + "\n"); print("\n".join(lines))
