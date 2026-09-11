#!/usr/bin/env python3
"""AI adoption telemetry engine for the AI Change Management Side Quest.

Reads a usage log in the shape of a Greenlight export plus a roster, computes every signal in
the Success Metrics Framework v1.0 (Level 1 process integrity, Level 2 adoption / manager /
risk signals, Level 3 strategic, directional), fires the intervention triggers defined in
config/interventions.json, and writes one adoption_state.json the dashboard renders.

Config over code: every threshold is in config/signals.json. Dry-run by nature: the engine
never sends anything; it lists what fired and who owns the response.

Run:  python3 adoption_engine.py                      summary to stdout
      python3 adoption_engine.py --output data/adoption_state.json
      python3 adoption_engine.py --data data --config config
"""
import argparse, csv, json, math, pathlib, statistics, datetime as dt
from collections import defaultdict

HERE = pathlib.Path(__file__).resolve().parent

SIGNAL_SOURCES = {
    # SMF signal -> (status on this feed, what the feed needs to carry)
    "Active Usage Rate": ("computed", "per user per day: count of uses (conversations or messages)"),
    "Time-to-First-Use": ("computed", "per user: seat granted date; first logged use"),
    "Time-to-Sustained-Use": ("computed", "per user per day use counts (derived)"),
    "Workflow Deviation Rate": ("no_source", "not in usage telemetry; needs process observation or a self-report field"),
    "Escalation Pattern Shift": ("no_source", "case or call routing data from the pilot team's own system"),
    "Feature Utilization Depth": ("computed", "per use: which agent or skill was used; list of available agents"),
    "Manager Dashboard Engagement": ("computed", "access log of the manager report: who opened it, when"),
    "Coaching Conversation Rate": ("proxy", "manager-logged conversation date per at-risk user (self-report form)"),
    "Intervention Response Rate": ("computed", "manager-logged response per fired alert"),
    "Team Adoption Variance": ("computed", "roster with manager per user (derived)"),
    "Usage Drop": ("computed", "derived from per user per day counts"),
    "Adoption Plateau": ("computed", "derived from per user per day counts"),
    "Zero-Use Persistence": ("computed", "derived from roster availability date and usage"),
    "Sustained Workaround": ("no_source", "process observation or self-report; no telemetry equivalent"),
}

def d(s):
    return dt.date.fromisoformat(s)

def load(data_dir, cfg):
    data_dir = pathlib.Path(data_dir)
    roster = list(csv.DictReader(open(data_dir / "roster_sample.csv")))
    usage = list(csv.DictReader(open(data_dir / "usage_sample.csv")))
    views = list(csv.DictReader(open(data_dir / "manager_views_sample.csv")))
    responses = list(csv.DictReader(open(data_dir / "responses_sample.csv")))
    process = json.load(open(data_dir / "process_sample.json"))
    return roster, usage, views, responses, process

def build_daily(usage):
    """user_id -> {date: uses}, and user_id -> {date: set(agents)}"""
    daily = defaultdict(lambda: defaultdict(int))
    agents = defaultdict(lambda: defaultdict(set))
    for r in usage:
        day = d(r["date"]); n = int(r["uses"])
        daily[r["user_id"]][day] += n
        agents[r["user_id"]][day].add(r["agent"])
    return daily, agents

def count_between(days, start, end):
    """uses with start <= date <= end"""
    return sum(n for day, n in days.items() if start <= day <= end)

def first_sustained_day(days, first, as_of, uses, within):
    """first day on/after first use where the trailing `within`-day count reaches `uses`."""
    if first is None:
        return None
    day = first
    while day <= as_of:
        if count_between(days, day - dt.timedelta(days=within - 1), day) >= uses:
            return day
        day += dt.timedelta(days=1)
    return None

def score_user(u, days, agent_days, cfg, as_of):
    avail = d(u["available_from"])
    first = min(days) if days else None
    su = cfg["sustained_use"]; au = cfg["active_usage"]; ud = cfg["usage_drop"]
    ap = cfg["adoption_plateau"]; zu = cfg["zero_use"]; fd = cfg["feature_depth"]
    period_start = as_of - dt.timedelta(days=au["period_days"] - 1)
    uses_period = count_between(days, period_start, as_of)
    sustained_on = first_sustained_day(days, first, as_of, su["uses"], su["within_days"])
    # currently sustained: trailing window meets the bar today
    sustained_now = count_between(days, as_of - dt.timedelta(days=su["within_days"] - 1), as_of) >= su["uses"]
    cd = ud["compare_days"]
    recent = count_between(days, as_of - dt.timedelta(days=cd - 1), as_of)
    prior = count_between(days, as_of - dt.timedelta(days=2 * cd - 1), as_of - dt.timedelta(days=cd))
    first14 = count_between(days, first, first + dt.timedelta(days=13)) if first else 0
    lb = cfg["team_variance"]["lookback_days"]
    uses_lookback = count_between(days, as_of - dt.timedelta(days=lb - 1), as_of)
    used_agents = set()
    for day, s in agent_days.items():
        if as_of - dt.timedelta(days=27) <= day <= as_of:
            used_agents |= s
    triggers = []
    if first is None and (as_of - avail).days >= zu["after_days"]:
        triggers.append(("zero_use", avail + dt.timedelta(days=zu["after_days"])))
    def drop_on(day):
        r = count_between(days, day - dt.timedelta(days=cd - 1), day)
        p = count_between(days, day - dt.timedelta(days=2 * cd - 1), day - dt.timedelta(days=cd))
        return p >= ud["min_prior_uses"] and r <= p * (1 - ud["drop_pct"] / 100)
    if first is not None and drop_on(as_of):
        # stamp the first day of the current run of the condition, not the day we looked
        fired = as_of
        while fired > avail + dt.timedelta(days=2 * cd) and drop_on(fired - dt.timedelta(days=1)):
            fired -= dt.timedelta(days=1)
        triggers.append(("usage_drop", fired))
    if first is not None and (as_of - first).days >= ap["after_days"] and sustained_on is None and recent <= first14:
        triggers.append(("adoption_plateau", first + dt.timedelta(days=ap["after_days"])))
    weekly = []
    wk_end = as_of
    while wk_end > avail:
        wk_start = wk_end - dt.timedelta(days=6)
        weekly.append(count_between(days, wk_start, wk_end))
        wk_end = wk_start - dt.timedelta(days=1)
    weekly.reverse()
    return {
        "user_id": u["user_id"], "display": u["display"], "team": u["team"], "manager": u["manager"],
        "first_use": first.isoformat() if first else None,
        "ttfu_days": (first - avail).days if first else None,
        "sustained_on": sustained_on.isoformat() if sustained_on else None,
        "ttsu_days": (sustained_on - first).days if sustained_on else None,
        "sustained_now": bool(sustained_now),
        "active": uses_period >= au["min_uses_per_period"],
        "uses_period": uses_period, "uses_recent": recent, "uses_prior": prior,
        "uses_lookback": uses_lookback, "total_uses": sum(days.values()),
        "feature_depth": round(len(used_agents) / len(fd["available_agents"]), 2),
        "agents_used": sorted(used_agents),
        "weekly": weekly,
        "daily": [[day.isoformat(), n] for day, n in sorted(days.items())],
        "triggers": [{"trigger": t, "fired_on": when.isoformat()} for t, when in triggers],
    }

def median(xs):
    xs = [x for x in xs if x is not None]
    return statistics.median(xs) if xs else None

def pstdev(xs):
    return round(statistics.pstdev(xs), 2) if len(xs) > 1 else 0.0

def score(roster, usage, views, responses, process, cfg, icfg):
    as_of = d(cfg["window"]["as_of_date"])
    daily, agent_days = build_daily(usage)
    users = [score_user(u, daily[u["user_id"]], agent_days[u["user_id"]], cfg, as_of) for u in roster]
    n = len(users)
    # interventions
    resp_by = {(r["user_id"], r["trigger"]): r for r in responses}
    lw = cfg["intervention_effect"]["lift_window_days"]
    interventions = []
    for u in users:
        for t in u["triggers"]:
            spec = icfg["triggers"][t["trigger"]]
            fired = d(t["fired_on"])
            r = resp_by.get((u["user_id"], t["trigger"]))
            responded = bool(r and r.get("responded_on"))
            coached = bool(r and r.get("coaching_conversation_on"))
            lift = None
            if (as_of - fired).days >= lw:
                after = count_between(daily[u["user_id"]], fired + dt.timedelta(days=1), fired + dt.timedelta(days=lw))
                before = count_between(daily[u["user_id"]], fired - dt.timedelta(days=lw), fired - dt.timedelta(days=1))
                lift = after > before
            due = fired + dt.timedelta(days=spec["response_window_days"])
            interventions.append({
                "user_id": u["user_id"], "display": u["display"], "team": u["team"], "manager": u["manager"],
                "trigger": t["trigger"], "label": spec["label"], "fired_on": t["fired_on"],
                "action": spec["action"], "owner_role": spec["owner_role"], "manager_facing": spec["manager_facing"],
                "response_due": due.isoformat(),
                "status": "responded" if responded else ("overdue" if as_of > due else "open"),
                "responded_on": r["responded_on"] if responded else None,
                "coaching_conversation": coached,
                "measurable": lift is not None, "lift": lift,
            })
    # teams / managers
    me = cfg["manager_engagement"]
    views_by = defaultdict(list)
    for v in views:
        views_by[v["manager"]].append(d(v["date"]))
    teams = []
    for team in sorted({u["team"] for u in users}):
        tu = [u for u in users if u["team"] == team]
        mgr = tu[0]["manager"]
        ti = [i for i in interventions if i["team"] == team]
        mf = [i for i in ti if i["manager_facing"]]
        at_risk = {i["user_id"] for i in ti}
        coached = {i["user_id"] for i in ti if i["coaching_conversation"]}
        vcount = sum(1 for day in views_by[mgr] if as_of - dt.timedelta(days=me["dashboard_views_period_days"] - 1) <= day <= as_of)
        teams.append({
            "team": team, "manager": mgr, "users": len(tu),
            "active_rate": round(sum(u["active"] for u in tu) / len(tu), 2),
            "sustained_rate": round(sum(u["sustained_now"] for u in tu) / len(tu), 2),
            "never_used": sum(1 for u in tu if u["first_use"] is None),
            "median_ttfu": median([u["ttfu_days"] for u in tu]),
            "median_ttsu": median([u["ttsu_days"] for u in tu]),
            "feature_depth": round(sum(u["feature_depth"] for u in tu) / len(tu), 2),
            "variance": pstdev([u["uses_lookback"] for u in tu]),
            "open_alerts": sum(1 for i in ti if i["status"] != "responded"),
            "fired": len(ti),
            "response_rate": round(sum(1 for i in mf if i["status"] == "responded") / len(mf), 2) if mf else None,
            "coaching_rate": round(len(coached) / len(at_risk), 2) if at_risk else None,
            "dashboard_views": vcount,
            "manager_engaged": vcount >= me["engaged_min_views"],
            "weekly": [sum(w) for w in zip(*[u["weekly"] for u in tu])],
        })
    mf_all = [i for i in interventions if i["manager_facing"]]
    measurable = [i for i in interventions if i["measurable"]]
    trig_specs = icfg["triggers"]
    monitored = sum(1 for t in trig_specs.values() if t["source"])
    p = process
    level1 = {
        "readiness_assessment_completion": round(p["readiness_assessment"]["completed_groups"] / p["readiness_assessment"]["target_groups"], 2),
        "baseline_documentation_rate": round(p["baseline_documentation"]["documented_groups"] / p["baseline_documentation"]["target_groups"], 2),
        "manager_briefing_completion": round(p["manager_briefing"]["briefed"] / p["manager_briefing"]["managers"], 2),
        "intervention_trigger_coverage": round(monitored / len(trig_specs), 2),
        "trigger_coverage_detail": f"{monitored} of {len(trig_specs)} defined triggers have a telemetry source",
        "milestone_adherence": round(p["milestones"]["completed_on_time"] / p["milestones"]["planned_to_date"], 2),
    }
    cohort = {
        "users": n,
        "active_rate": round(sum(u["active"] for u in users) / n, 2),
        "sustained_rate": round(sum(u["sustained_now"] for u in users) / n, 2),
        "ever_used": sum(1 for u in users if u["first_use"]),
        "never_used": sum(1 for u in users if u["first_use"] is None),
        "median_ttfu": median([u["ttfu_days"] for u in users]),
        "median_ttsu": median([u["ttsu_days"] for u in users]),
        "feature_depth": round(sum(u["feature_depth"] for u in users) / n, 2),
        "managers_engaged": sum(1 for t in teams if t["manager_engaged"]),
        "managers": len(teams),
        "interventions_fired": len(interventions),
        "interventions_open": sum(1 for i in interventions if i["status"] != "responded"),
        "interventions_overdue": sum(1 for i in interventions if i["status"] == "overdue"),
        "response_rate": round(sum(1 for i in mf_all if i["status"] == "responded") / len(mf_all), 2) if mf_all else None,
        "effectiveness_rate": round(sum(1 for i in measurable if i["lift"]) / len(measurable), 2) if measurable else None,
        "effectiveness_n": len(measurable),
        "weekly": [sum(w) for w in zip(*[u["weekly"] for u in users])],
        "by_trigger": {k: sum(1 for i in interventions if i["trigger"] == k) for k in trig_specs},
    }
    level3 = {
        "adoption_rate_now": cohort["sustained_rate"],
        "time_to_sustained_median_days": cohort["median_ttsu"],
        "intervention_effectiveness": cohort["effectiveness_rate"],
        "retention_of_gains": None, "retention_note": "measured 60 to 90 days after close",
        "productivity_lift": None, "productivity_note": "needs a baseline from the pilot team and Finance",
        "cost_avoidance": None, "cost_note": "needs a Finance baseline",
        "sentiment_shift": None, "sentiment_note": "needs the pre-pilot survey",
    }
    return {
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "sample_data": True,
        "window": cfg["window"],
        "thresholds": {k: v for k, v in cfg.items() if k != "window"},
        "cohort": cohort, "teams": teams, "users": users, "interventions": interventions,
        "level1": level1, "level3": level3,
        "trigger_specs": trig_specs,
        "signal_sources": {k: {"status": s, "needs": w} for k, (s, w) in SIGNAL_SOURCES.items()},
    }

def summary(state):
    c = state["cohort"]
    print(f"AI adoption telemetry  as of {state['window']['as_of_date']}  ({'SAMPLE DATA' if state['sample_data'] else 'live'})")
    print(f"  users {c['users']}  active {c['active_rate']:.0%}  sustained {c['sustained_rate']:.0%}  never used {c['never_used']}")
    print(f"  median time to first use {c['median_ttfu']} d  to sustained use {c['median_ttsu']} d  feature depth {c['feature_depth']:.0%}")
    print(f"  interventions fired {c['interventions_fired']}  open {c['interventions_open']}  overdue {c['interventions_overdue']}  response rate {c['response_rate']}  effectiveness {c['effectiveness_rate']} (n={c['effectiveness_n']})")
    print(f"  managers engaged {c['managers_engaged']}/{c['managers']}")
    for t in state["teams"]:
        print(f"  {t['team']:<6} users {t['users']:>2}  active {t['active_rate']:.0%}  sustained {t['sustained_rate']:.0%}  fired {t['fired']}  open {t['open_alerts']}  resp {t['response_rate']}  views {t['dashboard_views']}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", default=str(HERE / "data"))
    ap.add_argument("--config", default=str(HERE / "config"))
    ap.add_argument("--output")
    a = ap.parse_args()
    cfg = json.load(open(pathlib.Path(a.config) / "signals.json"))
    icfg = json.load(open(pathlib.Path(a.config) / "interventions.json"))
    state = score(*load(a.data, cfg), cfg, icfg)
    if a.output:
        json.dump(state, open(a.output, "w"), indent=1)
        print(f"wrote {a.output}")
    summary(state)

if __name__ == "__main__":
    main()
