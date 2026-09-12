#!/usr/bin/env python3
"""Offline tests for signal_review.py (fixture staged file, --no-clay, scratch ledger)."""
import json, os, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); AUTO = os.path.dirname(HERE)
SR = os.path.join(AUTO, "signal_review.py")

def run():
    checks = []
    def check(n, c): checks.append((n, c))
    tmp = tempfile.mkdtemp(); led = os.path.join(tmp, "ledger.json"); log = os.path.join(tmp, "log.md")
    # seed a domain cache so --no-clay can resolve the known orgs
    dc = os.path.join(tmp, "cache.json"); json.dump({"centene corporation": "centene.com", "point32health": "point32health.org", "humana inc.": "humana.com"}, open(dc, "w"))
    r = subprocess.run([sys.executable, SR, "sync", "--no-clay", "--staged", os.path.join(HERE, "fixture_staged_signals.csv"), "--ledger", led, "--log", log, "--domain-cache", dc], capture_output=True, text=True)
    first_log = open(log).read()
    check("sync exits 0", r.returncode == 0)
    d = json.load(open(led))
    by = {s["org"]: s for s in d["signals"]}; parked = {p["org"]: p for p in d["parked"]}
    check("Centene CFO row classifies leadership_change, not Stars (quote outweighs angle)", by.get("Centene Corporation", {}).get("trigger_type") == "leadership_change")
    check("Point32Health cost quote classifies cost_mandate", by.get("Point32Health", {}).get("trigger_type") == "cost_mandate")
    check("Humana is parked as a customer (denylist alias)", "Humana Inc." in parked and "customer" in parked["Humana Inc."]["reason"])
    check("NON-TARGET row is parked with the war room's reason", any("non-target" in p["reason"] for p in d["parked"] if p["org"].startswith("Citizens")))
    check("unknown org is parked for no domain, never served", "Mystery Org Nobody Knows" in parked and "no domain" in parked["Mystery Org Nobody Knows"]["reason"])
    check("dates parsed from prose fiscal periods", by.get("Centene Corporation", {}).get("date") == "2026-08-17")
    check("ids are stable across runs", subprocess.run([sys.executable, SR, "sync", "--no-clay", "--staged", os.path.join(HERE, "fixture_staged_signals.csv"), "--ledger", led, "--log", log, "--domain-cache", dc], capture_output=True, text=True).returncode == 0 and len(json.load(open(led))["signals"]) == len(d["signals"]))
    sid = by["Centene Corporation"]["id"]
    r = subprocess.run([sys.executable, SR, "decide", "--id", sid, "--state", "approved", "--via", "rundown thread 1.0", "--ledger", led], capture_output=True, text=True)
    d2 = json.load(open(led)); s2 = next(s for s in d2["signals"] if s["id"] == sid)
    check("decide records state, date and channel", r.returncode == 0 and s2["state"] == "approved" and s2["decided_via"].startswith("rundown thread") and s2.get("decided_at"))
    pid = parked["Mystery Org Nobody Knows"]["id"]
    r = subprocess.run([sys.executable, SR, "resolve", "--id", pid, "--domain", "www.mystery.com", "--ledger", led], capture_output=True, text=True)
    d3 = json.load(open(led))
    check("resolve un-parks a signal once it has a domain", r.returncode == 0 and any(s["id"] == pid and s["state"] == "unreviewed" and s["domain"] == "mystery.com" for s in d3["signals"]))
    check("decide on an unknown id fails loudly", subprocess.run([sys.executable, SR, "decide", "--id", "sig-nope", "--state", "denied", "--ledger", led], capture_output=True, text=True).returncode == 2)
    check("first-run log lists awaiting signals with ids and an evt anchor", "Awaiting review" in first_log and "evt: signal-review-" in first_log)
    ok = all(c for _, c in checks)
    for n, c in checks: print(f"  {'PASS' if c else 'FAIL'}  {n}")
    print("-" * 56); print(f"{sum(1 for _, c in checks if c)}/{len(checks)} passed")
    return ok

if __name__ == "__main__":
    sys.exit(0 if run() else 1)
