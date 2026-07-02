#!/usr/bin/env python3
"""
Tests for the Intradiem signal processor. Run: python test_signal_processor.py
Asserts known routing outcomes so a config or data change that breaks the
engine fails loudly instead of silently shipping wrong signals.
"""
import signal_processor as engine


def by_domain(results, domain):
    return next(r for r in results if r["domain"] == domain)


def types(result):
    return {s["type"] for s in result["signals"]}


def run():
    results = engine.process()  # no suppression, deterministic
    checks = []

    def check(name, cond):
        checks.append((name, cond))

    syn = by_domain(results, "synchrony.com")
    check("Synchrony fires seat_utilization", types(syn) == {"seat_utilization"})
    check("Synchrony seat value 88.9", syn["signals"][0]["value"] == 88.9)
    check("Synchrony routes AE", syn["primary_routing"] == "AE")

    cen = by_domain(results, "centene.com")
    check("Centene fires coaching + crm", types(cen) == {"coaching_coverage", "crm_not_connected"})
    check("Centene routes AE (AE beats CSM)", cen["primary_routing"] == "AE")

    car = by_domain(results, "caresource.com")
    check("CareSource fires automation drop", types(car) == {"automation_volume_drop"})
    check("CareSource drop value -33.3", car["signals"][0]["value"] == -33.3)
    check("CareSource routes CSM", car["primary_routing"] == "CSM")

    mol = by_domain(results, "molina.com")
    check("Molina fires rule_engine_active", types(mol) == {"rule_engine_active"})

    hig = by_domain(results, "highmark.org")
    check("Highmark fires champion_job_change", types(hig) == {"champion_job_change"})
    check("Highmark routes AE (AE+CSM)", hig["primary_routing"] == "AE")

    ally = by_domain(results, "ally.com")
    check("Ally fires nothing (clean account)", ally["signals_fired"] == 0)
    check("Ally routes HOLD", ally["primary_routing"] == "HOLD")

    check("All 6 signal types represented across the set",
          {t for r in results for t in types(r)} == {
              "seat_utilization", "coaching_coverage", "rule_engine_active",
              "crm_not_connected", "automation_volume_drop", "champion_job_change"})

    passed = sum(1 for _, c in checks if c)
    for name, cond in checks:
        print(f"  {'PASS' if cond else 'FAIL'}  {name}")
    print("-" * 52)
    print(f"{passed}/{len(checks)} passed")
    return passed == len(checks)


if __name__ == "__main__":
    import sys
    sys.exit(0 if run() else 1)
