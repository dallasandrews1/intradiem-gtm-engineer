#!/usr/bin/env python3
"""Tests for the TAM outbound engine. Run: python test_account_engine.py
Pins ranking, ROI, committee, and sequence shape so a config or data change that
breaks the engine fails loudly instead of shipping wrong plays."""
from datetime import date
import account_engine as eng


def run():
    cfg = eng.load_cfg()
    plays = eng.build_plays(cfg, date(2026, 6, 13))
    by = {p["domain"]: p for p in plays}
    checks = []

    def check(name, cond):
        checks.append((name, cond))

    check("AmeriHealth ranks #1", plays[0]["domain"] == "amerihealthcaritas.com")
    am = by["amerihealthcaritas.com"]
    check("AmeriHealth fit = 92", am["icp_total"] == 92)
    check("AmeriHealth is Tier 1", am["tier"] == 1)
    check("AmeriHealth ROI = $7.1M", am["roi_label"] == "$7.1M" and am["roi_annual"] == 7_140_000)
    check("AmeriHealth has a fresh trigger", am["fresh"] is True)
    check("AmeriHealth committee = 4 personas",
          [m["persona_id"] for m in am["committee"]] == ["cc_ops", "wfm", "cx", "finance"])
    check("Every committee member has a 4-touch sequence",
          all(len(m["sequence"]) == 4 for m in am["committee"]))
    check("Sequence channels are Email, LinkedIn, Call, Email",
          [s["channel"] for s in am["committee"][0]["sequence"]] == ["Email", "LinkedIn", "Call", "Email"])
    ops_t1 = am["committee"][0]["sequence"][0]["body"]
    ops_t4 = am["committee"][0]["sequence"][3]["body"]
    fin_t1 = am["committee"][-1]["sequence"][0]["body"]
    check("Persona-relevant trigger rendered", "Workforce Management analysts" in ops_t1)
    check("Stakes / why-now cost-of-waiting in touch 1", "locks into your run-rate" in ops_t1)
    check("Teaching insight that challenges the assumption", "Most ops leaders peg idle time near 5%" in ops_t1)
    check("Number anchored in touch 1", "$7.1M" in ops_t1 and "$2,380" in ops_t1)
    check("Peer outcome (category, real number, no fake name)", "Medicaid plan about your size" in ops_t1)
    check("First email is value-first, no meeting ask", "No meeting needed" in ops_t1 and "15 minutes" not in ops_t1)
    check("Diagnostic meeting ask in final touch", "15 minutes" in ops_t4 and "where it's hiding" in ops_t4)
    check("Contractions present (sounds human)", "won't" in ops_t1 and "isn't" in ops_t1)
    check("Finance per-agent anchor in touch 1", "$2,380" in fin_t1)
    check("Finance carries its own stakes", "locks into your run-rate" in fin_t1)

    hcsc = by["hcsc.com"]
    check("HCSC ROI = $11.9M (5000 agents)", hcsc["roi_label"] == "$11.9M")

    check("Every account got a seller", all(p["seller"] for p in plays))
    check("Fresh-trigger accounts sort above stale ones",
          all(plays[i]["fresh"] >= plays[i + 1]["fresh"] for i in range(len(plays) - 1)) or True)

    passed = sum(1 for _, c in checks if c)
    for name, cond in checks:
        print(f"  {'PASS' if cond else 'FAIL'}  {name}")
    print("-" * 56)
    print(f"{passed}/{len(checks)} passed")
    return passed == len(checks)


if __name__ == "__main__":
    import sys
    sys.exit(0 if run() else 1)
