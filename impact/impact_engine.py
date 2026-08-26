#!/usr/bin/env python3
"""
Intradiem GTM Impact Scorecard

One number for ELT: the opportunity this system has already put on the table, the
activity behind it, and the realized results as deals move. It reads the outputs of
both engines (no new data entry) plus a small outcomes log you append to as things
close.

Sources (the generated outputs of the other two engines):
    ../intradiem-signal-engine/data/signals.json   install-base expansion + risk
    ../tam-outbound-engine/data/tam_plays.json      net-new strike plans
    ./outcomes.csv                                  realized meetings and pipeline

Usage:
    python impact_engine.py                 # print the scorecard
    python impact_engine.py --output impact.json

The dollar figures from the engines are surfaced opportunity (estimated recoverable
cost the system put in front of a rep), not booked revenue. Realized results live in
outcomes.csv and are the ones you grow over time. Keep the two clearly separate when
you present this.
"""
import argparse
import csv
import json
import os
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
SIGNALS = os.path.join(HERE, "..", "intradiem-signal-engine", "data", "signals.json")
TAM = os.path.join(HERE, "..", "tam-outbound-engine", "data", "tam_plays.json")
ROI_MODEL = os.path.join(HERE, "..", "tam-outbound-engine", "config", "roi_model.json")
OUTCOMES = os.path.join(HERE, "outcomes.csv")

# GTM Engineer role start. Outcomes dated before this are interview-era demo data and are
# never counted as realized. See realized_metrics().
ROLE_START = "2026-07-06"


def load_json(path):
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


def fmt_money(n):
    if n >= 1_000_000:
        return f"${n/1_000_000:.1f}M"
    if n >= 1_000:
        return f"${n/1_000:.0f}K"
    return f"${n:,.0f}"


def net_new_metrics(tam, roi_model):
    accts = tam.get("accounts", []) if tam else []
    roi = sum(a.get("roi_annual", 0) for a in accts)
    hot = [a for a in accts if a.get("fresh")]
    hot_roi = sum(a.get("roi_annual", 0) for a in hot)
    plays = len(accts)
    messages = sum(len(m.get("sequence", [])) for a in accts for m in a.get("committee", []))
    contacts = sum(len(a.get("committee", [])) for a in accts)
    rm = roi_model or {}
    idle = rm.get("idle_minutes_per_agent_hour", 3)
    hours = rm.get("productive_hours_per_year", 1700)
    cost = rm.get("loaded_hourly_cost", 28)
    per_agent = round(idle / 60 * hours * cost)
    breakdown = [{
        "company": a.get("company"), "agent_count": a.get("agent_count", 0),
        "roi_annual": a.get("roi_annual", 0), "roi_label": a.get("roi_label", fmt_money(a.get("roi_annual", 0))),
    } for a in accts]
    return {
        "accounts_targeted": len(accts), "hot_today": len(hot),
        "roi_surfaced": roi, "roi_surfaced_label": fmt_money(roi),
        "hot_roi_surfaced": hot_roi, "hot_roi_surfaced_label": fmt_money(hot_roi),
        "strike_plans": plays, "committee_contacts_mapped": contacts,
        "sequence_messages_drafted": messages,
        "assumptions": {"idle_minutes_per_agent_hour": idle, "productive_hours_per_year": hours,
                        "loaded_hourly_cost": cost, "per_agent_per_year": per_agent,
                        "per_agent_label": f"${per_agent:,}"},
        "breakdown": breakdown,
    }


def install_base_metrics(sig):
    accts = sig.get("accounts", []) if sig else []
    firing = [a for a in accts if a.get("signals_fired", 0) > 0]
    sigs = sum(a.get("signals_fired", 0) for a in accts)
    ae = sum(1 for a in accts for s in a.get("signals", []) if "AE" in s.get("route", ""))
    csm = sum(1 for a in accts for s in a.get("signals", []) if "CSM" in s.get("route", ""))
    return {
        "accounts_monitored": len(accts), "accounts_with_signal": len(firing),
        "signals_firing": sigs, "ae_routes": ae, "csm_routes": csm,
    }


def realized_metrics(path):
    # ROLE_START gate, added 2026-08-07. outcomes.csv shipped with two demo rows dated
    # 2026-06-10 and 2026-06-11, three weeks BEFORE the role started. They produced a
    # standing "1 meeting booked / $180K pipeline" that the control tower then rendered
    # under a hardcoded REALIZED label, while the receipts ledger said 0 meetings / $0.
    # Two files in one repo disagreed about whether a meeting had happened.
    # Anything dated before ROLE_START is interview-era demo data and is never counted as
    # realized. It is reported separately so the exclusion is visible rather than silent.
    meetings = 0
    pipeline = 0
    won = 0
    rows = 0
    excluded = 0
    undated = 0
    if os.path.exists(path):
        with open(path, newline="") as f:
            for r in csv.DictReader(f):
                d = (r.get("date") or "").strip()
                if not d:
                    # An undated row cannot be proven to be post-start, so it fails closed.
                    undated += 1
                    excluded += 1
                    continue
                if d < ROLE_START:
                    excluded += 1
                    continue
                rows += 1
                t = (r.get("type") or "").strip().lower()
                v = float(r.get("value") or 0)
                if t == "meeting":
                    meetings += 1
                elif t == "pipeline":
                    pipeline += v
                elif t == "won":
                    won += v
    return {
        "logged_outcomes": rows, "meetings_booked": meetings,
        "pipeline_created": pipeline, "pipeline_created_label": fmt_money(pipeline),
        "revenue_won": won, "revenue_won_label": fmt_money(won),
        "excluded_pre_role_rows": excluded,
        "excluded_undated_rows": undated,
        "role_start": ROLE_START,
    }


def build(today=None):
    # SOURCE HEALTH: load_json returns None for a missing file, and the metric helpers treat
    # that as "empty" -> $0. That is a SILENT failure (a missing upstream export looks identical
    # to a real zero). So we record which inputs were actually present and expose data_complete;
    # the conductor refuses to present these numbers as healthy if any source is missing.
    tam_raw = load_json(TAM)
    sig_raw = load_json(SIGNALS)
    sources = {
        "tam_plays": tam_raw is not None,
        "signals": sig_raw is not None,
        "outcomes": os.path.exists(OUTCOMES),
    }
    nn = net_new_metrics(tam_raw, load_json(ROI_MODEL))
    ib = install_base_metrics(sig_raw)
    rz = realized_metrics(OUTCOMES)
    return {
        "generated_at": (today or datetime.now()).isoformat() if not isinstance(today, str) else today,
        "headline_opportunity_surfaced": nn["roi_surfaced"],
        "headline_opportunity_label": fmt_money(nn["roi_surfaced"]),
        "net_new": nn, "install_base": ib, "realized": rz,
        "sources": sources,
        "data_complete": all(sources.values()),
        # Added 2026-08-07. The surfaced total is produced by roi_model.json, whose defaults
        # the repo's own docs flag as placeholder assumptions. Nothing downstream could tell
        # a placeholder dollar from a verified one, so the basis now travels WITH the number.
        "surfaced_basis": "VERIFIED" if (load_json(ROI_MODEL) or {}).get("_verified") else "UNVERIFIED",
    }


def print_scorecard(d):
    nn, ib, rz = d["net_new"], d["install_base"], d["realized"]
    line = "=" * 64
    print(line)
    print("INTRADIEM GTM IMPACT SCORECARD")
    print(line)
    print(f"\nOPPORTUNITY SURFACED (estimated recoverable cost in front of reps)")
    print(f"  Net-new recoverable ROI surfaced ....... {nn['roi_surfaced_label']:>8}   across {nn['accounts_targeted']} target accounts")
    print(f"  Of that, hot today ..................... {nn['hot_roi_surfaced_label']:>8}   across {nn['hot_today']} accounts with a fresh trigger")
    print(f"\nSYSTEM ACTIVITY (what ran with no extra headcount)")
    print(f"  Strike plans generated ................. {nn['strike_plans']:>8}")
    print(f"  Committee contacts mapped .............. {nn['committee_contacts_mapped']:>8}")
    print(f"  Sequence messages drafted .............. {nn['sequence_messages_drafted']:>8}")
    print(f"  Install base accounts scored ........... {ib['accounts_monitored']:>8}")
    print(f"  Expansion / risk signals firing ........ {ib['signals_firing']:>8}   ({ib['ae_routes']} to AE, {ib['csm_routes']} to CSM)")
    print(f"\nREALIZED (from outcomes.csv, the number you grow)")
    print(f"  Meetings booked ........................ {rz['meetings_booked']:>8}")
    print(f"  Pipeline created ....................... {rz['pipeline_created_label']:>8}")
    print(f"  Revenue won ............................ {rz['revenue_won_label']:>8}")
    print("\n" + line)
    basis = d.get("surfaced_basis", "UNVERIFIED")
    tag = "" if basis == "VERIFIED" else " [UNVERIFIED]"
    print(f"Headline for ELT: the system has surfaced {nn['roi_surfaced_label']}{tag} in recoverable")
    print(f"customer cost and {ib['signals_firing']} live expansion signals, with {rz['meetings_booked']} meeting(s) and")
    print(f"{rz['pipeline_created_label']} in pipeline realized so far.")
    if basis != "VERIFIED":
        print("")
        print("SURFACED IS UNVERIFIED. It derives from roi_model.json placeholder assumptions,")
        print("not from Intradiem-verified figures. Never blend it with the realized line above,")
        print("and never put it in a leadership readout without the [UNVERIFIED] marker.")
    if rz.get("excluded_pre_role_rows"):
        print("")
        print(f"NOTE: {rz['excluded_pre_role_rows']} outcome row(s) dated before {rz['role_start']} were")
        print("excluded as pre-role demo data and are NOT in the realized figures above.")
    print(line)


def main():
    ap = argparse.ArgumentParser(description="GTM impact scorecard")
    ap.add_argument("--output", help="write the scorecard to a JSON file")
    args = ap.parse_args()
    d = build()
    if args.output:
        with open(args.output, "w") as f:
            json.dump(d, f, indent=2)
        print(f"Wrote scorecard to {args.output}\n")
    print_scorecard(d)


if __name__ == "__main__":
    main()
