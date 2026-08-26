#!/usr/bin/env python3
"""Tests for the L2 intent scorer. Run: python3 test_l2_intent_scorer.py

Covers the behaviors that mirror the live Clay intent_score column: customer +
graduation kill switch, new_faller base, per-signal point contribution (so a silent
weight drift like leadership 20->10 is caught), motion filtering, recency decay,
rollup, and cap.
"""
from datetime import date
import l2_intent_scorer as m

TODAY = date(2026, 7, 11)
FRESH = "2026-07-10"   # 1 day old, full weight
CFG = m.load_config()
CHECKS = []


def check(name, cond):
    CHECKS.append((name, bool(cond)))


def by_acct(results):
    return {r["account"]: r for r in results}


def score_one(signal, star="3.5", new_faller="FALSE", customer_flag="FALSE", fired=FRESH):
    """Single-account, single-signal helper for isolating point contributions."""
    stars = [{"account": "A", "overall_star_2026": star,
              "new_faller": new_faller, "customer_flag": customer_flag}]
    sigs = [{"account": "A", "signal": signal, "fired_date": fired}] if signal else []
    return by_acct(m.score_accounts(CFG, sigs, stars, today=TODAY))["A"]


# ---- self-cleaning: graduation ---------------------------------------------
stars = [
    {"account": "GraduatedCo", "overall_star_2026": "4.0", "new_faller": "FALSE", "customer_flag": "FALSE"},
    {"account": "CliffCo", "overall_star_2026": "3.5", "new_faller": "FALSE", "customer_flag": "FALSE"},
]
sigs = [
    {"account": "GraduatedCo", "signal": "sec_filing_stars", "fired_date": FRESH},
    {"account": "CliffCo", "signal": "sec_filing_stars", "fired_date": FRESH},
]
res = by_acct(m.score_accounts(CFG, sigs, stars, today=TODAY))
check("graduated account forced to intent 0", res["GraduatedCo"]["intent_score"] == 0)
check("graduated account marked graduated", res["GraduatedCo"]["graduated"] is True)
check("graduated account dropped from motion", res["GraduatedCo"]["in_motion"] is False)
check("sub-4.0 account keeps its intent", res["CliffCo"]["intent_score"] == 30)
check("sub-4.0 account is in motion", res["CliffCo"]["in_motion"] is True)

# ---- self-cleaning: customer exclusion (the R1 leak fix) --------------------
# A customer that is ALSO a fresh faller with a strong signal must still be 0.
cust = score_one("sec_filing_stars", star="3.5", new_faller="TRUE", customer_flag="TRUE")
check("customer forced to intent 0 even with faller + signal", cust["intent_score"] == 0)
check("customer marked excluded", cust["status"] == "excluded")
check("customer flagged excluded_customer", cust["excluded_customer"] is True)
check("customer dropped from motion", cust["in_motion"] is False)

# ---- new_faller base --------------------------------------------------------
faller = score_one(None, star="3.5", new_faller="TRUE")
check("new_faller alone surfaces at base 20", faller["intent_score"] == 20)
check("new_faller alone is in motion", faller["in_motion"] is True)
faller_hot = score_one("sec_filing_stars", star="3.5", new_faller="TRUE")
check("new_faller + sec_filing = 50 (grade lift)", faller_hot["intent_score"] == 50)
check("new_faller + sec_filing grade_lift flag", faller_hot["grade_lift"] is True)

# ---- per-signal point contribution (catches weight drift) ------------------
# Each star-motion signal, fired fresh on a non-faller 3.5 account, must equal
# exactly its configured points. If someone edits a weight in config without
# intending to, one of these fails.
expected_points = {
    "sec_filing_stars": 30,
    "earnings_stars_mention": 25,
    "measure_slippage": 20,
    "quality_leadership_change": 10,
    "quality_hiring_cluster": 15,
}
for sig, pts in expected_points.items():
    got = score_one(sig)["intent_score"]
    check(f"{sig} contributes exactly {pts}", got == pts)

# ---- motion filter: back-office signal does not score in the Stars motion ---
backlog = score_one("claims_backlog_news")   # motions = ["back_office"]
check("claims_backlog ignored under star_ratings motion", backlog["intent_score"] == 0)
check("claims_backlog account is dormant, not in motion", backlog["in_motion"] is False)

# ---- recency decay ----------------------------------------------------------
# fresh signal (1 day) = full 30 pts; stale signal (>120 days) = floor 0.4 * 30 = 12
rf = score_one("sec_filing_stars", fired="2026-07-10")
rs = score_one("sec_filing_stars", fired="2026-01-01")
check("fresh signal at full weight (30)", rf["intent_score"] == 30)
check("stale signal decays to floor (12)", rs["intent_score"] == 12)

# ---- rollup + tier ----------------------------------------------------------
res2 = by_acct(m.score_accounts(CFG, [
    {"account": "CliffCo", "signal": "sec_filing_stars", "fired_date": FRESH},
    {"account": "CliffCo", "signal": "quality_hiring_cluster", "fired_date": FRESH},
], [{"account": "CliffCo", "overall_star_2026": "3.5", "new_faller": "FALSE", "customer_flag": "FALSE"}], today=TODAY))
# CliffCo: 30 (sec, tier1) + 15 (hiring, tier2) = 45
check("multi-signal rollup sums points", res2["CliffCo"]["intent_score"] == 45)
check("tier1 fired flag set", res2["CliffCo"]["tier1_fired"] is True)
check("grade lift at intent >= 40", res2["CliffCo"]["grade_lift"] is True)

# ---- cap at 100 -------------------------------------------------------------
# 30 + 25 + 20 + 10 + 15 = 100 exactly across the five star-motion signals
many = [{"account": "HotCo", "signal": s, "fired_date": FRESH}
        for s in ["sec_filing_stars", "earnings_stars_mention", "measure_slippage",
                  "quality_leadership_change", "quality_hiring_cluster"]]
rh = by_acct(m.score_accounts(CFG, many, [{"account": "HotCo", "overall_star_2026": "3.0",
             "new_faller": "FALSE", "customer_flag": "FALSE"}], today=TODAY))
check("five star signals sum to exactly 100", rh["HotCo"]["intent_score"] == 100)
many.append({"account": "HotCo", "signal": "sec_filing_stars", "fired_date": FRESH})
rh2 = by_acct(m.score_accounts(CFG, many, [{"account": "HotCo", "overall_star_2026": "3.0",
              "new_faller": "FALSE", "customer_flag": "FALSE"}], today=TODAY))
check("intent capped at 100", rh2["HotCo"]["intent_score"] == 100)

# ---- robustness -------------------------------------------------------------
junk = score_one("not_a_real_signal")
check("unknown signal ignored, no crash", junk["intent_score"] == 0)
check("account with star but no valid signal is dormant", junk["status"] == "dormant")

# ---- config integrity -------------------------------------------------------
check("15 signals defined (6 stars-era + 5 back-office + 4 install-base)", len(CFG["signals"]) == 15)
check("self-clean threshold is 4.0", CFG["self_cleaning"]["graduated_star"] == 4.0)
check("customer kill switch configured", CFG["self_cleaning"]["customer_field"] == "customer_flag")
check("leadership weight is 10", CFG["signals"]["quality_leadership_change"]["points"] == 10)
check("new_faller base is 20", CFG["new_faller_base"]["points"] == 20)
check("claims_backlog is back-office motion", CFG["signals"]["claims_backlog_news"]["motions"] == ["back_office"])
check("monthly budget is 5000", CFG["cadence"]["budget_credits_per_month"] == 5000)
check("steady state <= budget", CFG["cadence"]["steady_state_est_credits_per_month"] <= 5000)
check("back_office override inverts customer exclusion",
      CFG["motion_overrides"]["back_office"]["self_cleaning"]["customer_is_exclusion"] is False)
check("back_office base term is install_base @ 10",
      CFG["motion_overrides"]["back_office"]["base_term"]["field"] == "install_base"
      and CFG["motion_overrides"]["back_office"]["base_term"]["points"] == 10)
check("all 5 new back-office signals scoped to back_office motion",
      all(CFG["signals"][s]["motions"] == ["back_office"] for s in
          ["bo_cost_mandate", "bo_hiring_cluster", "sla_penalty_backlog",
           "bpo_transition", "transaction_volume_surge"]))

# ---- back-office motion fork: the inverted self-clean -----------------------
# The fork is a fork, not a copy: under back_office, customer_flag is NOT an
# exclusion (the customer's back office is the target), risk suppresses instead,
# install_base is the warm base, and owner_cleared is a send gate.
import copy as _copy
BO = _copy.deepcopy(CFG)
BO["active_motion"] = "back_office"


def score_bo(accts, sigs):
    return by_acct(m.score_accounts(BO, sigs, accts, today=TODAY))


bo_accts = [
    {"account": "CustWarm", "customer_flag": "TRUE", "install_base": "TRUE", "fo_risk_flag": "FALSE", "owner_cleared": "TRUE"},
    {"account": "CustRisk", "customer_flag": "TRUE", "install_base": "TRUE", "fo_risk_flag": "TRUE", "owner_cleared": "TRUE"},
    {"account": "CustUncleared", "customer_flag": "TRUE", "install_base": "TRUE", "fo_risk_flag": "FALSE", "owner_cleared": "FALSE"},
    {"account": "CustBaseOnly", "customer_flag": "TRUE", "install_base": "TRUE", "fo_risk_flag": "FALSE", "owner_cleared": "TRUE"},
]
bo_sigs = [
    {"account": "CustWarm", "signal": "bo_cost_mandate", "fired_date": FRESH},
    {"account": "CustWarm", "signal": "bo_hiring_cluster", "fired_date": FRESH},
    {"account": "CustRisk", "signal": "bo_cost_mandate", "fired_date": FRESH},
    {"account": "CustUncleared", "signal": "bo_hiring_cluster", "fired_date": FRESH},
]
bo = score_bo(bo_accts, bo_sigs)
check("BO: customer NOT excluded (inversion)", bo["CustWarm"]["excluded_customer"] is False)
check("BO: install_base(10) + cost_mandate(20) + hiring(15) = 45", bo["CustWarm"]["intent_score"] == 45)
check("BO: warm cleared account is sendable", bo["CustWarm"]["sendable"] is True)
check("BO: grade lift at >= 40", bo["CustWarm"]["grade_lift"] is True)
check("BO: fo_risk suppresses hot account to 0", bo["CustRisk"]["intent_score"] == 0)
check("BO: fo_risk status is suppressed_risk", bo["CustRisk"]["status"] == "suppressed_risk")
check("BO: risk-suppressed dropped from motion", bo["CustRisk"]["in_motion"] is False)
check("BO: uncleared account still scores (25)", bo["CustUncleared"]["intent_score"] == 25)
check("BO: uncleared status is pending_owner", bo["CustUncleared"]["status"] == "pending_owner")
check("BO: uncleared in motion but NOT sendable",
      bo["CustUncleared"]["in_motion"] is True and bo["CustUncleared"]["sendable"] is False)
check("BO: install_base base alone surfaces at 10", bo["CustBaseOnly"]["intent_score"] == 10)
check("BO: base-only account is sendable", bo["CustBaseOnly"]["sendable"] is True)

# motion filter both directions: a Stars signal must not score under back_office
bo_cross = score_bo(
    [{"account": "X", "customer_flag": "TRUE", "install_base": "FALSE", "fo_risk_flag": "FALSE", "owner_cleared": "TRUE"}],
    [{"account": "X", "signal": "sec_filing_stars", "fired_date": FRESH}])
check("BO: star signal ignored under back_office motion", bo_cross["X"]["intent_score"] == 0)

# per-signal back-office point contribution (catches weight drift, install_base off)
bo_expected = {
    "bo_cost_mandate": 20, "bo_hiring_cluster": 15, "sla_penalty_backlog": 20,
    "bpo_transition": 15, "transaction_volume_surge": 10, "claims_backlog_news": 10,
}
for sig, pts in bo_expected.items():
    r = score_bo(
        [{"account": "P", "customer_flag": "TRUE", "install_base": "FALSE", "fo_risk_flag": "FALSE", "owner_cleared": "TRUE"}],
        [{"account": "P", "signal": sig, "fired_date": FRESH}])
    check(f"BO: {sig} contributes exactly {pts}", r["P"]["intent_score"] == pts)

# ---- install-base expansion motion fork (added Jul 14 2026) -----------------
# Third motion on the same spine: front-office EXPANSION inside current customers.
# Same inverted kill switch as back_office (customer NOT excluded, fo_risk
# suppresses, owner_cleared gates sends, install_base warm base @ 10), but its
# signal set is first-party L1 telemetry (0 credits): seat utilization, CRM
# attach, coaching coverage, rule-engine power use. The L1 risk signals feed
# fo_risk_flag, never expansion intent.
IB = _copy.deepcopy(CFG)
IB["active_motion"] = "install_base"


def score_ib(accts, sigs):
    return by_acct(m.score_accounts(IB, sigs, accts, today=TODAY))


ib_accts = [
    {"account": "SeatsFull", "customer_flag": "TRUE", "install_base": "TRUE", "fo_risk_flag": "FALSE", "owner_cleared": "TRUE"},
    {"account": "RiskySave", "customer_flag": "TRUE", "install_base": "TRUE", "fo_risk_flag": "TRUE", "owner_cleared": "TRUE"},
    {"account": "Uncleared", "customer_flag": "TRUE", "install_base": "TRUE", "fo_risk_flag": "FALSE", "owner_cleared": "FALSE"},
    {"account": "WarmOnly", "customer_flag": "TRUE", "install_base": "TRUE", "fo_risk_flag": "FALSE", "owner_cleared": "TRUE"},
]
ib_sigs = [
    {"account": "SeatsFull", "signal": "seat_utilization_headroom", "fired_date": FRESH},
    {"account": "SeatsFull", "signal": "crm_not_connected", "fired_date": FRESH},
    {"account": "RiskySave", "signal": "seat_utilization_headroom", "fired_date": FRESH},
    {"account": "Uncleared", "signal": "coaching_coverage_gap", "fired_date": FRESH},
]
ib = score_ib(ib_accts, ib_sigs)
check("IB: customer NOT excluded (inversion)", ib["SeatsFull"]["excluded_customer"] is False)
check("IB: install_base(10) + seats(20) + crm(15) = 45", ib["SeatsFull"]["intent_score"] == 45)
check("IB: hot cleared account is sendable + grade lift",
      ib["SeatsFull"]["sendable"] is True and ib["SeatsFull"]["grade_lift"] is True)
check("IB: fo_risk suppresses hot account to 0", ib["RiskySave"]["intent_score"] == 0)
check("IB: fo_risk status is suppressed_risk", ib["RiskySave"]["status"] == "suppressed_risk")
check("IB: risk-suppressed dropped from motion", ib["RiskySave"]["in_motion"] is False)
check("IB: uncleared account still scores (25)", ib["Uncleared"]["intent_score"] == 25)
check("IB: uncleared status is pending_owner", ib["Uncleared"]["status"] == "pending_owner")
check("IB: uncleared in motion but NOT sendable",
      ib["Uncleared"]["in_motion"] is True and ib["Uncleared"]["sendable"] is False)
check("IB: warm base alone surfaces at 10", ib["WarmOnly"]["intent_score"] == 10)

# motion filter both directions: Stars and back-office signals never score here
ib_cross = score_ib(
    [{"account": "X", "customer_flag": "TRUE", "install_base": "FALSE", "fo_risk_flag": "FALSE", "owner_cleared": "TRUE"}],
    [{"account": "X", "signal": "sec_filing_stars", "fired_date": FRESH},
     {"account": "X", "signal": "bo_cost_mandate", "fired_date": FRESH}])
check("IB: stars + back-office signals ignored under install_base", ib_cross["X"]["intent_score"] == 0)

# per-signal install-base point contribution (catches weight drift)
ib_expected = {
    "seat_utilization_headroom": 20, "crm_not_connected": 15,
    "coaching_coverage_gap": 15, "rule_engine_active": 10,
}
for sig, pts in ib_expected.items():
    r = score_ib(
        [{"account": "P", "customer_flag": "TRUE", "install_base": "FALSE", "fo_risk_flag": "FALSE", "owner_cleared": "TRUE"}],
        [{"account": "P", "signal": sig, "fired_date": FRESH}])
    check(f"IB: {sig} contributes exactly {pts}", r["P"]["intent_score"] == pts)

# install-base signals never leak into the other two motions
il = score_one("seat_utilization_headroom")   # star_ratings motion
check("IB signal ignored under star_ratings motion", il["intent_score"] == 0)
ib_in_bo = score_bo(
    [{"account": "Y", "customer_flag": "TRUE", "install_base": "FALSE", "fo_risk_flag": "FALSE", "owner_cleared": "TRUE"}],
    [{"account": "Y", "signal": "seat_utilization_headroom", "fired_date": FRESH}])
check("IB signal ignored under back_office motion", ib_in_bo["Y"]["intent_score"] == 0)

# config integrity for the new motion
check("install_base override inverts customer exclusion",
      CFG["motion_overrides"]["install_base"]["self_cleaning"]["customer_is_exclusion"] is False)
check("install_base base term is install_base @ 10",
      CFG["motion_overrides"]["install_base"]["base_term"]["field"] == "install_base"
      and CFG["motion_overrides"]["install_base"]["base_term"]["points"] == 10)
check("all 4 install-base signals scoped to install_base motion",
      all(CFG["signals"][s]["motions"] == ["install_base"] for s in ib_expected))
check("install-base signals are all 0-credit first-party",
      all(CFG["signals"][s]["est_credits_per_account"] == 0 for s in ib_expected))

# parity guard: the Stars motion is byte-for-byte unchanged by the forks
parity = score_one("sec_filing_stars")
check("Stars parity: sec_filing still 30 after fork", parity["intent_score"] == 30)
check("Stars parity: customer still excluded", score_one("sec_filing_stars", customer_flag="TRUE")["excluded_customer"] is True)
# back-office parity: unchanged by the install_base fork
bo_parity = score_bo(
    [{"account": "Z", "customer_flag": "TRUE", "install_base": "TRUE", "fo_risk_flag": "FALSE", "owner_cleared": "TRUE"}],
    [{"account": "Z", "signal": "bo_cost_mandate", "fired_date": FRESH}])
check("BO parity: base + cost_mandate still 30 after install_base fork", bo_parity["Z"]["intent_score"] == 30)

# ---- report -----------------------------------------------------------------
passed = sum(1 for _, ok in CHECKS if ok)
for name, ok in CHECKS:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
print(f"\n{passed}/{len(CHECKS)} checks passed")
raise SystemExit(0 if passed == len(CHECKS) else 1)
