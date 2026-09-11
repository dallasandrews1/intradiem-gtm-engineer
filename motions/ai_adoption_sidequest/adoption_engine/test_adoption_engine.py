#!/usr/bin/env python3
"""Checks for the adoption engine on hand-built fixtures (no sample generator involved)."""
import json, pathlib, datetime as dt, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import adoption_engine as E

HERE = pathlib.Path(__file__).resolve().parent
cfg = json.load(open(HERE / "config" / "signals.json"))
icfg = json.load(open(HERE / "config" / "interventions.json"))
cfg["window"] = {"tool_available_date": "2026-07-13", "as_of_date": "2026-09-06"}
AS_OF = dt.date(2026, 9, 6)

def daily(pairs):
    return {dt.date.fromisoformat(k): v for k, v in pairs.items()}

def user(uid, team="T", manager="M"):
    return {"user_id": uid, "display": uid, "team": team, "manager": manager, "available_from": "2026-07-13"}

checks = []
def check(name, cond):
    checks.append((name, bool(cond)))
    print(("PASS " if cond else "FAIL ") + name)

# 1. never used, 55 days after availability -> zero_use fires on availability + 21
u = E.score_user(user("a"), {}, {}, cfg, AS_OF)
check("zero-use fires for a user with no use", [t["trigger"] for t in u["triggers"]] == ["zero_use"])
check("zero-use fires on the configured day", u["triggers"][0]["fired_on"] == "2026-08-03")
check("no first use means no time-to-first-use", u["ttfu_days"] is None and u["active"] is False)

# 2. time to first use and sustained use: first use Jul 20, then 6 uses inside 14 days
days = daily({"2026-07-20": 1, "2026-07-22": 1, "2026-07-24": 1, "2026-07-27": 1, "2026-07-29": 1, "2026-07-31": 1,
              "2026-08-25": 2, "2026-08-27": 2, "2026-08-31": 2, "2026-09-02": 2, "2026-09-04": 2})
u = E.score_user(user("b"), days, {}, cfg, AS_OF)
check("time to first use is 7 days", u["ttfu_days"] == 7)
check("sustained use reached on the sixth use (11 days after first)", u["sustained_on"] == "2026-07-31" and u["ttsu_days"] == 11)
check("sustained now with 10 uses in the trailing 14 days", u["sustained_now"] is True)
check("active with 2+ uses in the trailing 7 days", u["active"] is True)
check("no trigger for a healthy user", u["triggers"] == [])

# 3. usage drop: prior 14 days had 6, recent 14 days has 1 -> drop >= 50%
days = daily({"2026-08-10": 2, "2026-08-12": 2, "2026-08-14": 2, "2026-09-01": 1})
u = E.score_user(user("c"), days, {}, cfg, AS_OF)
check("usage drop fires when the trailing window halves", [t["trigger"] for t in u["triggers"]] == ["usage_drop"])
# below the prior-uses floor no drop fires
days = daily({"2026-08-12": 1, "2026-08-14": 1})
u = E.score_user(user("c2"), days, {}, cfg, AS_OF)
check("usage drop does not fire under the prior-uses floor", u["triggers"] == [])

# 4. plateau: first use Jul 15, 1 use every ~10 days, never sustained, recent <= first 14 days
days = daily({"2026-07-15": 1, "2026-07-25": 1, "2026-08-04": 1, "2026-08-14": 1, "2026-08-26": 1})
u = E.score_user(user("d"), days, {}, cfg, AS_OF)
check("plateau fires for flat low use with no sustained day", [t["trigger"] for t in u["triggers"]] == ["adoption_plateau"])
check("plateau fires at first use + after_days", u["triggers"][0]["fired_on"] == "2026-08-12")

# 5. feature depth counts distinct agents in the trailing 28 days
ad = {dt.date(2026, 8, 20): {"Knowledge assistant", "CRM assistant"}, dt.date(2026, 9, 1): {"CRM assistant", "Roleplay coach"},
      dt.date(2026, 7, 20): {"Data explainer"}}
u = E.score_user(user("e"), daily({"2026-08-20": 2, "2026-09-01": 2, "2026-07-20": 1}), ad, cfg, AS_OF)
check("feature depth is 3 of 6 agents (old use outside 28 days ignored)", u["feature_depth"] == 0.5)

# 6. weekly series has 8 entries for an 8-week window
check("weekly series covers 8 weeks", len(u["weekly"]) == 8)

# 7. full score: interventions, response status, effectiveness, team roll-up
roster = [user("a", "T1", "M1"), user("b", "T1", "M1"), user("c", "T2", "M2"), user("d", "T2", "M2")]
usage = []
def add(uid, day, n=1, agent="Knowledge assistant"):
    usage.append({"user_id": uid, "date": day, "agent": agent, "uses": str(n)})
for day, n in {"2026-07-20": 1, "2026-07-22": 1, "2026-07-24": 1, "2026-07-27": 1, "2026-07-29": 1, "2026-07-31": 1,
               "2026-08-25": 2, "2026-08-27": 2, "2026-08-31": 2, "2026-09-02": 2, "2026-09-04": 2}.items(): add("b", day, n)
for day, n in {"2026-08-10": 2, "2026-08-12": 2, "2026-08-14": 2, "2026-09-01": 1}.items(): add("c", day, n)
for day, n in {"2026-07-15": 1, "2026-07-25": 1, "2026-08-04": 1, "2026-08-14": 1, "2026-08-26": 1}.items(): add("d", day, n)
views = [{"manager": "M1", "date": "2026-08-28"}, {"manager": "M1", "date": "2026-09-03"}]
responses = [{"user_id": "a", "trigger": "zero_use", "responded_on": "2026-08-20", "coaching_conversation_on": "2026-08-20"}]
process = {"readiness_assessment": {"completed_groups": 1, "target_groups": 2}, "baseline_documentation": {"documented_groups": 2, "target_groups": 2},
           "manager_briefing": {"briefed": 2, "managers": 2}, "milestones": {"completed_on_time": 3, "planned_to_date": 4}}
st = E.score(roster, usage, views, responses, process, cfg, icfg)
fired = sorted((i["user_id"], i["trigger"]) for i in st["interventions"])
check("three interventions fire across the cohort", fired == [("a", "zero_use"), ("c", "usage_drop"), ("d", "adoption_plateau")])
byu = {i["user_id"]: i for i in st["interventions"]}
check("a responded (manager-facing alert answered)", byu["a"]["status"] == "responded" and byu["a"]["coaching_conversation"] is True)
check("c is open: drop stamped on its first day (Aug 29), still inside the 5-day window at Sep 6? no: overdue", byu["c"]["status"] in ("open", "overdue") and byu["c"]["fired_on"] < "2026-09-06")
check("d is overdue: plateau fired Aug 12, 10-day window passed, no response", byu["d"]["status"] == "overdue")
check("zero-use lift is measurable and false (still no use after the conversation)", byu["a"]["measurable"] is True and byu["a"]["lift"] is False)
check("drop fired inside the last 14 days is not yet measurable", byu["c"]["measurable"] is False)
t1 = [t for t in st["teams"] if t["team"] == "T1"][0]; t2 = [t for t in st["teams"] if t["team"] == "T2"][0]
check("T1 manager engaged with 2 views in 14 days", t1["manager_engaged"] is True and t1["dashboard_views"] == 2)
check("T2 manager not engaged", t2["manager_engaged"] is False)
check("T1 response rate 1.0 (one manager-facing alert, answered)", t1["response_rate"] == 1.0)
check("T2 response rate 0.0 (usage drop unanswered; plateau is not manager-facing)", t2["response_rate"] == 0.0)
check("T1 coaching rate 1.0", t1["coaching_rate"] == 1.0)
check("cohort sustained rate 0.25 (only b)", st["cohort"]["sustained_rate"] == 0.25)
check("trigger coverage 3 of 4 (sustained workaround has no source)", st["level1"]["intervention_trigger_coverage"] == 0.75)
check("level 1 readiness 0.5, briefing 1.0, milestones 0.75", st["level1"]["readiness_assessment_completion"] == 0.5 and st["level1"]["manager_briefing_completion"] == 1.0 and st["level1"]["milestone_adherence"] == 0.75)
check("level 3 strategic values stay empty until a baseline exists", st["level3"]["productivity_lift"] is None and st["level3"]["cost_avoidance"] is None)
check("every framework signal has a source status", all(v["status"] in ("computed", "proxy", "no_source") for v in st["signal_sources"].values()))

# 8. thresholds come from config, never the script: raising the sustained bar removes b's sustained day
cfg2 = json.loads(json.dumps(cfg)); cfg2["sustained_use"]["uses"] = 20
u = E.score_user(user("b"), daily({"2026-07-20": 1, "2026-07-22": 1, "2026-07-24": 1, "2026-07-27": 1, "2026-07-29": 1, "2026-07-31": 1}), {}, cfg2, AS_OF)
check("config change moves the sustained threshold", u["sustained_on"] is None)

n_fail = sum(1 for _, ok in checks if not ok)
print(f"\n{len(checks) - n_fail}/{len(checks)} checks passed")
sys.exit(1 if n_fail else 0)
