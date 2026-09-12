#!/usr/bin/env python3
"""Offline tests for universe_from_audiences.py (fixture records, no Clay)."""
import csv, json, os, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); ENG = os.path.dirname(HERE)
sys.path.insert(0, ENG)
import universe_from_audiences as u

def run():
    checks = []
    def check(name, cond): checks.append((name, cond))
    out = tempfile.mkdtemp()
    r = subprocess.run([sys.executable, os.path.join(ENG, "universe_from_audiences.py"), "--fixture",
                        os.path.join(HERE, "fixture_audiences_records.json"), "--out", out], capture_output=True, text=True)
    check("builder exits 0 on the fixture", r.returncode == 0)
    acc = {a["domain"]: a for a in csv.DictReader(open(os.path.join(out, "tam_accounts.csv")))}
    sel = {s["domain"]: s for s in csv.DictReader(open(os.path.join(out, "sellers.csv")))}
    trg = list(csv.DictReader(open(os.path.join(out, "triggers.csv"))))
    summ = json.load(open(os.path.join(out, "universe_build.json")))
    check("navient excluded by config (motion fit)", "navient.com" not in acc and any("navient" in e for e in summ["excluded"]))
    check("record with no employee count is excluded, not guessed", "noemp.com" not in acc)
    check("truist: filing fact overrides the Audiences employee_count", acc["truist.com"]["employees"] == "38711" and "sec.gov" in acc["truist.com"]["source"])
    check("truist: agent_count is a labelled banded ESTIMATE", "banded ESTIMATE" in acc["truist.com"]["source"] and int(acc["truist.com"]["agent_count"]) > 0)
    check("truist: tech read carries predictleads source + observed date", acc["truist.com"]["acd"] == "RingCentral" and acc["truist.com"]["acd_source"].startswith("predictleads:") and acc["truist.com"]["acd_observed"] == "2024-03-18")
    check("example payer: Audiences employee_count used and cited when no fact exists", acc["example-payer.com"]["employees"] == "4200" and "Clay Audiences company record" in acc["example-payer.com"]["source"])
    check("example payer: industry mapped Healthcare Insurance -> Health Insurance", acc["example-payer.com"]["industry"] == "Health Insurance")
    check("example payer: latest read per lane (Avaya 2026-05-06 over Five9 2025-01-01; Verint wfm)", acc["example-payer.com"]["acd"] == "Avaya" and acc["example-payer.com"]["wfm"] == "Verint" and acc["example-payer.com"]["wfm_observed"] == "2026-05-27")
    check("every row has a non-empty source and positive agent_count", all(a["source"].strip() and int(a["agent_count"]) > 0 for a in acc.values()))
    check("seller mapped from sf_owners (Keegan on fidelity)", sel.get("fidelity.com", {}).get("seller_name") == "Keegan Sanders")
    check("unmapped owner id reported, not invented", "005VUNMAPPED000001" in summ["unmapped_owner_ids"] and "example-payer.com" not in sel)
    check("facts-ledger triggers merged for universe domains only", any(t["domain"] == "truist.com" for t in trg) and not any(t["domain"] == "navient.com" for t in trg))
    check("merged triggers all carry a non-empty source", all(t["source"].strip() for t in trg))
    check("triggers added from the facts ledger carry a URL", all("http" in t["source"] for t in trg if "retrieved 2026-09-11" in t["source"]))
    ok = all(c for _, c in checks)
    for n, c in checks: print(f"  {'PASS' if c else 'FAIL'}  {n}")
    print("-" * 56); print(f"{sum(1 for _, c in checks if c)}/{len(checks)} passed")
    return ok

if __name__ == "__main__":
    sys.exit(0 if run() else 1)
