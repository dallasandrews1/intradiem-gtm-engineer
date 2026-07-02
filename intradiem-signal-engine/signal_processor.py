#!/usr/bin/env python3
"""
Intradiem GTM Signal Processor

Reads raw account usage metrics (data/accounts.csv) and threshold config
(config/thresholds.json), computes expansion and risk signals, and routes
each to AE or CSM. One source of truth: swap accounts.csv for a real
Intradiem reporting export and everything downstream recomputes.

Usage:
    python signal_processor.py                      # print summary for all accounts
    python signal_processor.py --domain centene.com # one account as JSON
    python signal_processor.py --output signals.json # write all results to JSON
    python signal_processor.py --suppress           # apply the 14-day suppression window

The CSV holds pre-aggregated 30-day rolling values, which matches the day-one
reality of a nightly export rather than a live event stream.
"""
import argparse
import csv
import json
import os
from datetime import datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CONFIG = os.path.join(HERE, "config", "thresholds.json")
DEFAULT_DATA = os.path.join(HERE, "data", "accounts.csv")
DEFAULT_STATE = os.path.join(HERE, "data", "suppression_state.json")

NUMERIC = {
    "licensed_seats", "active_seats", "total_agents", "agents_coached",
    "coaching_sessions_per_day", "available_rules", "active_rules",
    "wfm_days_active", "automation_vol_current", "automation_vol_prev1",
    "automation_vol_prev2", "days_to_renewal",
}
BOOLEAN = {"wfm_connected", "crm_connected", "champion_changed"}


def load_config(path):
    with open(path) as f:
        return json.load(f)


def get_data_source(config_path=DEFAULT_CONFIG):
    """Return the data-source tag ('mock' | 'live' | 'unknown') declared in config."""
    return load_config(config_path).get("data_source", "unknown")


def load_accounts(path):
    accounts = []
    with open(path, newline="") as f:
        for row in csv.DictReader(f):
            acct = {}
            for k, v in row.items():
                if k in NUMERIC:
                    acct[k] = float(v) if v not in ("", None) else 0.0
                elif k in BOOLEAN:
                    acct[k] = str(v).strip().lower() == "true"
                else:
                    acct[k] = v
            accounts.append(acct)
    return accounts


def _pct(part, whole):
    return round((part / whole) * 100, 1) if whole else 0.0


def evaluate_account(a, cfg):
    """Return a result dict for one account with all firing signals."""
    s = cfg["signals"]
    signals = []

    # 1. Seat utilization (expansion)
    util = _pct(a["active_seats"], a["licensed_seats"])
    if util >= s["seat_utilization"]["min_pct"]:
        signals.append({
            "type": "seat_utilization", "value": util,
            "route": s["seat_utilization"]["route"],
            "reason": f"Seats at {util}% of contract. Near capacity, expansion warranted.",
        })

    # 2. Coaching coverage (expansion)
    cov = _pct(a["agents_coached"], a["total_agents"])
    if (cov < s["coaching_coverage"]["max_pct"]
            and a["coaching_sessions_per_day"] >= s["coaching_coverage"]["min_sessions_per_day"]):
        signals.append({
            "type": "coaching_coverage", "value": cov,
            "route": s["coaching_coverage"]["route"],
            "reason": f"Coaching reaches only {cov}% of agents. Deployment gap.",
        })

    # 3. Rule engine active (expansion)
    rule = _pct(a["active_rules"], a["available_rules"])
    if rule < s["rule_engine_active"]["max_pct"]:
        signals.append({
            "type": "rule_engine_active", "value": rule,
            "route": s["rule_engine_active"]["route"],
            "reason": f"Only {rule}% of available rules active. Onboarding or use-case gap.",
        })

    # 4. CRM not connected (expansion)
    if (a["wfm_connected"] and not a["crm_connected"]
            and a["wfm_days_active"] >= s["crm_not_connected"]["min_wfm_days_active"]):
        signals.append({
            "type": "crm_not_connected", "value": int(a["wfm_days_active"]),
            "route": s["crm_not_connected"]["route"],
            "reason": f"WFM live {int(a['wfm_days_active'])} days, CRM not connected. Back-office expansion.",
        })

    # 5. Automation volume drop (risk) - requires N consecutive monthly drops
    mom2 = _pct(a["automation_vol_current"] - a["automation_vol_prev1"], a["automation_vol_prev1"])
    mom1 = _pct(a["automation_vol_prev1"] - a["automation_vol_prev2"], a["automation_vol_prev2"])
    cap = s["automation_volume_drop"]["max_mom_pct"]
    need = s["automation_volume_drop"]["consecutive_months"]
    drops = [m for m in ([mom1, mom2] if need >= 2 else [mom2]) if m <= cap]
    if len(drops) >= need:
        signals.append({
            "type": "automation_volume_drop", "value": mom2,
            "route": s["automation_volume_drop"]["route"],
            "reason": f"Automation volume down {abs(mom2)}% MoM for {need} months. Churn risk forming.",
        })

    # 6. Champion job change (risk)
    if a["champion_changed"] and a["days_to_renewal"] <= s["champion_job_change"]["max_days_to_renewal"]:
        signals.append({
            "type": "champion_job_change", "value": int(a["days_to_renewal"]),
            "route": s["champion_job_change"]["route"],
            "reason": f"Champion departed, {int(a['days_to_renewal'])} days to renewal. Rebuild the relationship.",
        })

    primary = primary_route(signals, cfg)
    return {
        "company": a["company"],
        "domain": a["domain"],
        "signals_fired": len(signals),
        "primary_routing": primary,
        "signals": signals,
    }


def primary_route(signals, cfg):
    routes = set()
    for sig in signals:
        for r in sig["route"].split("+"):
            routes.add(r)
    for r in cfg.get("routing_priority", ["AE", "CSM", "HOLD"]):
        if r in routes:
            return r
    return "HOLD"


def apply_suppression(results, cfg, state_path, now=None):
    """Drop signals fired within the suppression window; record fresh fires."""
    now = now or datetime.now(timezone.utc)
    window = timedelta(days=cfg.get("suppression_days", 14))
    state = {}
    if os.path.exists(state_path):
        with open(state_path) as f:
            state = json.load(f)
    for res in results:
        kept = []
        acct_state = state.setdefault(res["domain"], {})
        for sig in res["signals"]:
            last = acct_state.get(sig["type"])
            if last and now - datetime.fromisoformat(last) < window:
                continue  # suppressed
            acct_state[sig["type"]] = now.isoformat()
            kept.append(sig)
        res["signals"] = kept
        res["signals_fired"] = len(kept)
        res["primary_routing"] = primary_route(kept, cfg)
    os.makedirs(os.path.dirname(state_path), exist_ok=True)
    with open(state_path, "w") as f:
        json.dump(state, f, indent=2)
    return results


def process(data_path=DEFAULT_DATA, config_path=DEFAULT_CONFIG, suppress=False, state_path=DEFAULT_STATE):
    cfg = load_config(config_path)
    results = [evaluate_account(a, cfg) for a in load_accounts(data_path)]
    if suppress:
        results = apply_suppression(results, cfg, state_path)
    return results


def main():
    p = argparse.ArgumentParser(description="Intradiem GTM signal processor")
    p.add_argument("--data", default=DEFAULT_DATA)
    p.add_argument("--config", default=DEFAULT_CONFIG)
    p.add_argument("--domain", help="evaluate a single account by domain")
    p.add_argument("--output", help="write all results to this JSON file")
    p.add_argument("--suppress", action="store_true", help="apply the suppression window")
    args = p.parse_args()

    results = process(args.data, args.config, suppress=args.suppress)

    if args.domain:
        match = next((r for r in results if r["domain"] == args.domain), None)
        print(json.dumps(match or {"error": f"{args.domain} not monitored"}, indent=2))
        return

    source = get_data_source(args.config)

    if args.output:
        with open(args.output, "w") as f:
            json.dump({"generated_at": datetime.now(timezone.utc).isoformat(),
                       "data_source": source,
                       "accounts": results}, f, indent=2)
        print(f"Wrote {len(results)} accounts to {args.output}")

    fired = sum(r["signals_fired"] for r in results)
    print(f"\ndata source: {source.upper()}")
    print(f"{len(results)} accounts scored, {fired} signals firing\n" + "-" * 52)
    for r in sorted(results, key=lambda x: -x["signals_fired"]):
        tag = r["primary_routing"] if r["signals_fired"] else "no signal"
        print(f"  {r['company']:<24} {r['signals_fired']} signal(s)  -> {tag}")
        for sig in r["signals"]:
            print(f"      {sig['type']:<24} {sig['value']:>7}  {sig['route']}")


if __name__ == "__main__":
    main()
