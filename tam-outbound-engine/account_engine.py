#!/usr/bin/env python3
"""
Intradiem TAM Outbound Engine: account to action.

For every net-new target account it scores ICP fit, scores "why now" from live
triggers, estimates the recoverable labor cost (ROI), maps the buying committee
the triggers point to, and renders a persona-specific, multi-touch sequence the
owning seller can action the same day.

Runs on external data you can get on day one (firmographics, tech stack, job
postings, news), so it does not wait on internal product access.

Data (the swap-in points):
    data/tam_accounts.csv   firmographics + contact-center infra
    data/triggers.csv       detected buying triggers per account (Apollo/Clay/news/jobs)
    data/sellers.csv        who owns each account

Config (edit, never touch code):
    config/icp_weights.json  fit scoring
    config/triggers.json     trigger taxonomy, weight, Intradiem play, routing  (the moat)
    config/personas.json     buying committee + message blocks
    config/sequences.json    the cadence
    config/roi_model.json    recoverable-cost assumptions
    config/customer_denylist.json  confirmed-customer exclusion (SF report + aliases)

Usage:
    python account_engine.py                 # ranked action list + write account_plays.json
    python account_engine.py --plan amerihealthcaritas.com   # full strike plan for one account
    python account_engine.py --top 3         # just the ranked priority list
    python account_engine.py --output account_plays.json
"""
import argparse
import csv
import json
import os
import re
from datetime import datetime, date

HERE = os.path.dirname(os.path.abspath(__file__))
C = os.path.join(HERE, "config")
D = os.path.join(HERE, "data")


def load_json(name):
    with open(os.path.join(C, name)) as f:
        return json.load(f)


def load_csv(name):
    with open(os.path.join(D, name), newline="") as f:
        return list(csv.DictReader(f))


def recency_factor(d, rec, today):
    days = (today - d).days
    if days <= rec["fresh_days"]:
        return 1.0
    if days >= rec["stale_days"]:
        return rec["stale_floor"]
    span = rec["stale_days"] - rec["fresh_days"]
    return round(1.0 - (1.0 - rec["stale_floor"]) * (days - rec["fresh_days"]) / span, 3)


def fmt_money(n):
    if n >= 1_000_000:
        return f"${n/1_000_000:.1f}M"
    return f"${n:,.0f}"


def scale_points(agents, bands):
    for threshold, pts in bands:
        if agents >= threshold:
            return pts
    return 0


def tech_points(acd, wfm, t):
    acd_pts = t["acd_partner_points"] if acd in t["acd_partner"] else t["acd_other_points"]
    wfm_pts = t["wfm_present_points"] if wfm in t["wfm_present"] else t["wfm_unknown_points"]
    return min(25, acd_pts + wfm_pts)


def score_account(acct, trigs, cfg, today):
    icp, trg, roi, seq = cfg["icp"], cfg["trig"], cfg["roi"], cfg["seq"]
    agents = int(acct["agent_count"])
    industry_pts = icp["industry_points"].get(acct["industry"], icp["industry_points"]["Other"])
    scale_pts = scale_points(agents, icp["scale_bands"])
    tech_pts = tech_points(acct["acd"], acct["wfm"], icp["tech"])

    scored_trigs = []
    why_now_raw = 0.0
    fresh = False
    for t in trigs:
        meta = trg["triggers"].get(t["trigger_type"])
        if not meta:
            continue
        d = datetime.strptime(t["date"], "%Y-%m-%d").date()
        rf = recency_factor(d, trg["recency"], today)
        if (today - d).days <= trg["recency"]["fresh_days"]:
            fresh = True
        contribution = meta["weight"] * rf
        why_now_raw += contribution
        scored_trigs.append({
            "type": t["trigger_type"], "label": meta["label"], "detail": t["detail"],
            "date": t["date"], "play": meta["play"], "stakes": meta.get("stakes", ""),
            "route_personas": meta["route_personas"], "score": round(contribution, 1),
        })
    scored_trigs.sort(key=lambda x: -x["score"])
    pain_pts = min(25, round(why_now_raw * icp["pain_factor"]))
    icp_total = industry_pts + scale_pts + tech_pts + pain_pts
    tier = 1 if icp_total >= icp["tiers"]["tier1_min"] else 2 if icp_total >= icp["tiers"]["tier2_min"] else 3

    roi_annual = round(agents * (roi["idle_minutes_per_agent_hour"] / 60)
                       * roi["productive_hours_per_year"] * roi["loaded_hourly_cost"])
    roi_per_agent = round(roi_annual / agents) if agents else 0

    return {
        "company": acct["company"], "domain": acct["domain"], "industry": acct["industry"],
        "agent_count": agents, "acd": acct["acd"], "wfm": acct["wfm"],
        "dims": {"industry": industry_pts, "scale": scale_pts, "tech": tech_pts, "pain": pain_pts},
        "icp_total": icp_total, "tier": tier,
        "why_now_raw": round(why_now_raw, 1), "fresh": fresh,
        "roi_annual": roi_annual, "roi_label": fmt_money(roi_annual),
        "roi_per_agent": roi_per_agent, "roi_per_agent_label": f"${roi_per_agent:,}",
        "triggers": scored_trigs,
    }


def committee_for(scored, cfg):
    personas = {p["id"]: p for p in cfg["per"]["personas"]}
    ids = list(cfg["per"]["core_committee"])
    for t in scored["triggers"]:
        for pid in t["route_personas"]:
            if pid not in ids:
                ids.append(pid)
    order = [p["id"] for p in cfg["per"]["personas"]]
    return [personas[i] for i in sorted(ids, key=lambda x: order.index(x)) if i in personas]


def pick_trigger(scored, persona_id):
    """The trigger most relevant to this persona, not just the account's top one."""
    cands = [t for t in scored["triggers"] if persona_id in t.get("route_personas", [])]
    if cands:
        return max(cands, key=lambda x: x["score"])
    return scored["triggers"][0] if scored["triggers"] else {"detail": "your contact center is scaling"}


def render_vars(scored, seller, rel, proof):
    po = proof.get("peer_outcome_by_industry", {})
    return {
        "company": scored["company"], "agent_count": f"{scored['agent_count']:,}",
        "industry_lower": scored["industry"].lower(),
        "roi_annual": scored["roi_label"], "roi_per_agent": scored["roi_per_agent_label"],
        "trigger_detail": rel["detail"], "trigger_short": rel["detail"],
        "stakes": rel.get("stakes", ""),
        "idle_benchmark": proof.get("idle_benchmark", ""),
        "insight_tail": proof.get("insight_tail", ""),
        "peer_outcome": po.get(scored["industry"], po.get("Other", "")),
        "acd": scored["acd"], "wfm": scored["wfm"],
        "first_name": "[First name]", "seller_first": seller["seller_name"].split()[0] if seller else "your AE",
    }


def fill(text, v):
    for k, val in v.items():
        text = text.replace("{" + k + "}", str(val))
    return text


def render_sequence(persona, cadence, v):
    sv = {**v, "subj": fill(persona.get("subj", ""), v)}
    steps = []
    for step in cadence:
        body = "\n\n".join(fill(persona[b], v) for b in step["blocks"] if persona.get(b))
        touch = {
            "day": step["day"], "channel": step["channel"],
            "subject": fill(step["subject"], sv) if step["subject"] else "",
            "body": body,
        }
        if step["channel"] == "Call":
            # body stays the voicemail (backward compatible); live_script is the
            # if-they-answer script from the persona's call_live block.
            touch["voicemail"] = body
            if persona.get("call_live"):
                touch["live_script"] = fill(persona["call_live"], v)
        steps.append(touch)
    return steps


def norm_name(s):
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower())
    s = re.sub(r"\b(inc|llc|plc|ltd|corp|corporation|company|co|group|holdings)\b", " ", s)
    return " ".join(s.split())


def load_customer_denylist():
    dl = load_json("customer_denylist.json")
    sf_names = set()
    sf_path = os.path.join(HERE, dl.get("sf_report_csv", ""))
    if dl.get("sf_report_csv") and os.path.exists(sf_path):
        with open(sf_path, newline="") as f:
            sf_names = {norm_name(r["account_name"]) for r in csv.DictReader(f)}
    return {
        "domains": set(dl.get("domains", [])),
        "aliases": [norm_name(a) for a in dl.get("name_aliases", [])],
        "sf_names": sf_names,
    }


def customer_match(acct, dl):
    """Why this account is a confirmed customer, or None if it's clean."""
    if acct["domain"] in dl["domains"]:
        return f"domain {acct['domain']} on denylist"
    name = norm_name(acct["company"])
    if name in dl["sf_names"]:
        return "exact name match in SF customer report"
    for a in dl["aliases"]:
        if re.search(r"\b" + re.escape(a) + r"\b", name):
            return f"name matches customer alias '{a}'"
    return None


def build_plays(cfg, today):
    accounts = load_csv("tam_accounts.csv")
    trig_rows = load_csv("triggers.csv")
    sellers = {s["domain"]: s for s in load_csv("sellers.csv")}
    by_domain = {}
    for r in trig_rows:
        by_domain.setdefault(r["domain"], []).append(r)

    denylist = load_customer_denylist()
    plays = []
    excluded = []
    cadence = cfg["seq"]["cadence"]
    for acct in accounts:
        reason = customer_match(acct, denylist)
        if reason:
            excluded.append({"company": acct["company"], "domain": acct["domain"],
                             "customer_excluded": True, "match": reason,
                             "route": "install-base expansion, never cold"})
            continue
        scored = score_account(acct, by_domain.get(acct["domain"], []), cfg, today)
        seller = sellers.get(acct["domain"])
        committee = []
        for p in committee_for(scored, cfg):
            rel = pick_trigger(scored, p["id"])
            v = render_vars(scored, seller, rel, cfg["proof"])
            committee.append({
                "persona_id": p["id"], "role": p["role"],
                "relevant_trigger": rel.get("type"),
                "sequence": render_sequence(p, cadence, v),
            })
        scored["seller"] = seller
        scored["committee"] = committee
        plays.append(scored)

    plays.sort(key=lambda x: (x["fresh"], x["tier"] == 1, x["icp_total"], x["why_now_raw"]), reverse=True)
    return plays, excluded


def load_cfg():
    return {
        "icp": load_json("icp_weights.json"),
        "trig": load_json("triggers.json"),
        "per": load_json("personas.json"),
        "seq": load_json("sequences.json"),
        "roi": load_json("roi_model.json"),
        "proof": load_json("proof.json"),
    }


def get_data_source():
    """Return the data-source tag ('mock' | 'live' | 'unknown') declared in config/meta.json."""
    try:
        return load_json("meta.json").get("data_source", "unknown")
    except FileNotFoundError:
        return "unknown"


def print_ranked(plays, n=None):
    rows = plays[:n] if n else plays
    print(f"\n{'ACCOUNT':<32}{'FIT':>5}{'TIER':>6}{'WHY-NOW':>9}{'ROI/YR':>10}  TOP TRIGGER")
    print("-" * 96)
    for p in rows:
        tg = p["triggers"][0]["label"] if p["triggers"] else "no trigger"
        flag = " *" if p["fresh"] else "  "
        print(f"{p['company'][:31]:<32}{p['icp_total']:>5}{('T'+str(p['tier'])):>6}"
              f"{p['why_now_raw']:>9}{p['roi_label']:>10}{flag} {tg}")
    print("\n* = a fresh trigger fired inside the recency window. Work these today.")


def print_plan(p):
    line = "=" * 78
    print(line)
    print(f"ACCOUNT STRIKE PLAN  |  {p['company']}  ({p['domain']})")
    print(line)
    print(f"Fit score: {p['icp_total']}/100  (industry {p['dims']['industry']}, scale {p['dims']['scale']}, "
          f"tech {p['dims']['tech']}, pain {p['dims']['pain']})   Tier {p['tier']}")
    print(f"Contact center: ~{p['agent_count']:,} agents on {p['acd']} / {p['wfm']}")
    print(f"Recoverable labor cost (ROI): {p['roi_label']} per year")
    if p.get("seller"):
        print(f"Owner: {p['seller']['seller_name']}  ({p['seller']['seller_slack']})")
    print("\nWHY NOW")
    for t in p["triggers"]:
        print(f"  - [{t['label']}] {t['detail']} ({t['date']})")
        print(f"      Play: {t['play']}")
    print("\nBUYING COMMITTEE + SEQUENCES")
    for m in p["committee"]:
        print("\n" + "-" * 78)
        print(f"{m['role']}")
        print("-" * 78)
        for s in m["sequence"]:
            head = f"Day {s['day']} | {s['channel']}"
            if s["subject"]:
                head += f" | Subject: {s['subject']}"
            print("\n" + head)
            print(s["body"])
    print("\n" + line)


def main():
    ap = argparse.ArgumentParser(description="Intradiem TAM outbound engine")
    ap.add_argument("--plan", help="print the full strike plan for one account domain")
    ap.add_argument("--top", type=int, help="print the top N ranked accounts")
    ap.add_argument("--output", help="write all plays to a JSON file")
    ap.add_argument("--date", help="override today (YYYY-MM-DD) for testing")
    args = ap.parse_args()

    today = datetime.strptime(args.date, "%Y-%m-%d").date() if args.date else date.today()
    cfg = load_cfg()
    plays, excluded = build_plays(cfg, today)

    if args.plan:
        shut = next((e for e in excluded if e["domain"] == args.plan), None)
        if shut:
            print(f"{shut['company']} is a confirmed customer ({shut['match']}): "
                  f"no cold strike plan. Route as install-base expansion.")
            return
        match = next((p for p in plays if p["domain"] == args.plan), None)
        if not match:
            print(f"{args.plan} not in the target set")
            return
        print_plan(match)
        return

    if args.output:
        with open(args.output, "w") as f:
            json.dump({"generated_at": datetime.now().isoformat(), "accounts": plays,
                       "excluded_customers": excluded}, f, indent=2)
        print(f"Wrote {len(plays)} account plays to {args.output} "
              f"({len(excluded)} confirmed customer(s) excluded)")

    print_ranked(plays, args.top)
    for e in excluded:
        print(f"EXCLUDED (customer): {e['company']} ({e['domain']}) - {e['match']}; {e['route']}")


if __name__ == "__main__":
    main()
