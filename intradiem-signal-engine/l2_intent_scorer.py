#!/usr/bin/env python3
"""L2 intent scorer for the Star Ratings cliff-edge motion.

Turns external market signals into a per-account intent_score (0-100) that layers
on top of the L1 cliff-edge fit. Two behaviors define the layer:

  * Point rollup with recency decay - each fired signal contributes its config
    points, decayed by how stale the trigger is (full weight inside fresh_days,
    linear down to stale_floor by stale_days).
  * Self-cleaning - an account whose star has reached graduated_star (4.0) no
    longer has the problem: intent is forced to 0, status = graduated, and it
    drops out of the motion. The list shrinks itself; no manual pruning.

Config over code: all points/tiers/thresholds live in
config/l2_intent_signals.json. This file only implements the math.

Usage:
    python3 l2_intent_scorer.py                 # summary table, mock fixtures
    python3 l2_intent_scorer.py --json          # full JSON
    python3 l2_intent_scorer.py --output data/l2_intent.json
    python3 l2_intent_scorer.py --active-only   # hide graduated accounts
"""
import argparse
import csv
import json
import os
from datetime import date, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG = os.path.join(HERE, "config", "l2_intent_signals.json")
SIGNALS_CSV = os.path.join(HERE, "data", "l2_signals.csv")
STARS_CSV = os.path.join(HERE, "data", "l2_accounts_stars.csv")


def load_config(path=CONFIG):
    with open(path) as f:
        return json.load(f)


def _parse_date(s):
    return datetime.strptime(s.strip(), "%Y-%m-%d").date()


def decay_factor(fired_date, today, recency):
    """1.0 inside fresh_days, linear to stale_floor by stale_days, floor after."""
    age = (today - fired_date).days
    fresh, stale = recency["fresh_days"], recency["stale_days"]
    floor = recency["stale_floor"]
    if age <= fresh:
        return 1.0
    if age >= stale:
        return floor
    # linear interpolation between fresh (1.0) and stale (floor)
    span = stale - fresh
    return 1.0 - (1.0 - floor) * ((age - fresh) / span)


def _truthy(v):
    """Clay stores these flags as the text 'TRUE'/'FALSE'. Match the live behavior."""
    return str(v).strip().upper() == "TRUE"


def _motion_selfclean(config, active_motion):
    """Global self_cleaning merged with any per-motion override.

    The Star Ratings motion self-cleans on (customer OR graduated). The install-base
    back-office motion INVERTS the customer rule - the customer's back office IS the
    target - so it turns customer_is_exclusion off and instead suppresses on
    front-office risk. One config, one scorer, two motions with opposite kill switches.
    """
    global_sc = config.get("self_cleaning", {})
    mo = config.get("motion_overrides", {}).get(active_motion, {})
    msc = mo.get("self_cleaning", {})
    return global_sc, msc, mo


def score_accounts(config, signal_rows, star_rows, today=None):
    """signal_rows: list of dicts {account, signal, fired_date}.
    star_rows: list of dicts {account, overall_star_2026, new_faller?, customer_flag?, ...}.
    Returns list of per-account result dicts.

    Mirrors the live Clay intent_score column:
      * kill switch (motion-aware): the Star Ratings motion drops an existing customer
        OR a graduated (>=4.0) account to intent 0. A motion_override can invert this:
        the install-base back-office motion does NOT exclude customers and instead
        suppresses accounts flagged with front-office risk.
      * base term: a fresh faller (stars) or an install-base account (back office)
        surfaces at a base intent with zero external signals.
      * motion filter: only signals whose 'motions' list contains active_motion count,
        so the same config/scorer serves the Star Ratings and back-office motions.
      * capped point rollup with reference-only recency decay.
    """
    today = today or date.today()
    sig_defs = config["signals"]
    recency = config["recency"]
    scale = config["intent_scale"]
    active_motion = config.get("active_motion", "star_ratings")
    sc, msc, mo = _motion_selfclean(config, active_motion)
    grad_star = sc.get("graduated_star", 4.0)

    # motion-aware self-clean switches (Stars defaults; back office overrides)
    customer_is_exclusion = msc.get("customer_is_exclusion", True)
    graduation_applies = msc.get("graduation_applies", True)
    risk_field = msc.get("risk_field")
    risk_status = msc.get("risk_status", "suppressed_risk")
    cleared_field = msc.get("cleared_field")
    uncleared_status = msc.get("uncleared_status", "pending_owner")

    # base term: stars = new_faller_base; a motion may define its own (install_base)
    nf = config.get("new_faller_base", {})
    nf_field = nf.get("field", "new_faller")
    nf_points = nf.get("points", 0)
    mo_base = mo.get("base_term", {})
    base_field = mo_base.get("field")
    base_points = mo_base.get("points", 0)

    def _star(v):
        return float(v) if v not in (None, "") else None

    stars = {r["account"]: _star(r.get("overall_star_2026")) for r in star_rows}
    fallers = {r["account"]: _truthy(r.get(nf_field)) for r in star_rows}
    customers = {r["account"]: _truthy(r.get("customer_flag")) for r in star_rows}
    risks = {r["account"]: _truthy(r.get(risk_field)) for r in star_rows} if risk_field else {}
    cleared = {r["account"]: _truthy(r.get(cleared_field)) for r in star_rows} if cleared_field else {}
    bases = {r["account"]: _truthy(r.get(base_field)) for r in star_rows} if base_field else {}

    accounts = {}
    for row in signal_rows:
        acct = row["account"]
        sig = row["signal"]
        if sig not in sig_defs:
            continue  # unknown signal names are ignored, never crash
        if active_motion not in sig_defs[sig].get("motions", ["star_ratings"]):
            continue  # signal belongs to a different motion, do not score it here
        fired = _parse_date(row["fired_date"])
        factor = decay_factor(fired, today, recency)
        pts = sig_defs[sig]["points"] * factor
        entry = accounts.setdefault(acct, {"raw": 0.0, "fired": [], "tier1": False})
        entry["raw"] += pts
        entry["fired"].append({
            "signal": sig,
            "tier": sig_defs[sig]["tier"],
            "points": round(pts, 1),
            "age_days": (today - fired).days,
        })
        if sig_defs[sig]["tier"] == 1:
            entry["tier1"] = True

    # include accounts that have a star row but no signals (so graduation / faller /
    # customer exclusion / risk suppression still surface)
    for acct in stars:
        accounts.setdefault(acct, {"raw": 0.0, "fired": [], "tier1": False})

    results = []
    for acct, e in accounts.items():
        star = stars.get(acct)
        is_customer = customers.get(acct, False)
        graduated = graduation_applies and star is not None and star >= grad_star
        is_faller = fallers.get(acct, False)
        at_risk = risks.get(acct, False)
        has_base = bases.get(acct, False)
        # send gate: cleared defaults True when the motion defines no owner gate
        is_cleared = cleared.get(acct, True) if cleared_field else True

        raw = e["raw"]
        if is_faller:
            raw += nf_points
        if has_base:
            raw += base_points

        excluded_customer = customer_is_exclusion and is_customer

        if excluded_customer:
            intent = sc["on_customer"]["force_intent"]
            status = sc["on_customer"]["status"]
        elif graduated:
            intent = sc["on_graduate"]["force_intent"]
            status = sc["on_graduate"]["status"]
        elif at_risk:
            intent = 0
            status = risk_status
        else:
            intent = min(scale["max"], max(scale["min"], round(raw)))
            if intent >= scale["grade_lift_threshold"]:
                status = "grade_lift"
            elif intent > 0:
                status = uncleared_status if (cleared_field and not is_cleared) else "in_motion"
            else:
                status = "dormant"

        dropped = excluded_customer or graduated or at_risk
        results.append({
            "account": acct,
            "overall_star_2026": star,
            "new_faller": is_faller,
            "customer": is_customer,
            "intent_score": intent,
            "status": status,
            "graduated": graduated,
            "excluded_customer": excluded_customer,
            "at_risk": at_risk,
            "grade_lift": (not dropped) and intent >= scale["grade_lift_threshold"],
            "tier1_fired": e["tier1"] and not dropped,
            "in_motion": (not dropped) and intent > 0,
            "sendable": (not dropped) and intent > 0 and is_cleared,
            "signals_fired": sorted(e["fired"], key=lambda x: -x["points"]),
        })
    results.sort(key=lambda r: (-r["intent_score"], r["account"]))
    return results


def _read_csv(path):
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return list(csv.DictReader(f))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", help="emit full JSON")
    ap.add_argument("--output", help="write JSON to this path")
    ap.add_argument("--active-only", action="store_true", help="hide graduated accounts")
    ap.add_argument("--motion", help="override active_motion (e.g. back_office)")
    ap.add_argument("--signals", help="signals CSV (default Stars fixtures)")
    ap.add_argument("--stars", help="accounts CSV (default Stars fixtures)")
    args = ap.parse_args()

    config = load_config()
    if args.motion:
        config["active_motion"] = args.motion
    signals_csv = args.signals or SIGNALS_CSV
    stars_csv = args.stars or STARS_CSV
    results = score_accounts(config, _read_csv(signals_csv), _read_csv(stars_csv))
    if args.active_only:
        results = [r for r in results if not r["graduated"]]

    if args.output:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=2)
        print(f"wrote {len(results)} accounts to {args.output}")
        return
    if args.json:
        print(json.dumps(results, indent=2))
        return

    print(f"{'account':28} {'star':>5} {'intent':>7}  status")
    print("-" * 60)
    for r in results:
        star = "-" if r["overall_star_2026"] is None else f"{r['overall_star_2026']:.1f}"
        tag = "  <- customer, excluded" if r["excluded_customer"] else (
            "  <- graduated, dropped" if r["graduated"] else (
            "  <- grade lift" if r["grade_lift"] else ""))
        print(f"{r['account'][:28]:28} {star:>5} {r['intent_score']:>7}  {r['status']}{tag}")


if __name__ == "__main__":
    main()
