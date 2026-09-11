#!/usr/bin/env python3
"""Generate SAMPLE telemetry in the shape the engine expects from a Greenlight export.

Everything here is synthetic and deterministic (seeded). It exists so the dashboard has a
shape to render before the real feed lands. No row describes a real person or a real team.

Writes into data/:
  roster_sample.csv        user_id, display, team, manager, available_from
  usage_sample.csv         user_id, date, agent, uses          (one row per user-day-agent)
  manager_views_sample.csv manager, date                        (one row per dashboard open)
  responses_sample.csv     user_id, trigger, responded_on, coaching_conversation_on
  process_sample.json      Level 1 process-integrity inputs from project records
"""
import csv, json, random, pathlib, datetime as dt

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE / "data"
cfg = json.load(open(HERE / "config" / "signals.json"))
AVAIL = dt.date.fromisoformat(cfg["window"]["tool_available_date"])
END = dt.date.fromisoformat(cfg["window"]["as_of_date"])
AGENTS = cfg["feature_depth"]["available_agents"]
DAYS = (END - AVAIL).days + 1

rng = random.Random(20260909)

# Four synthetic teams with different adoption mixes. Archetypes:
#   early   first use in days 0-3, rising to 4-7 uses a week, broad agent use
#   steady  first use days 4-14, settles at 2-4 a week
#   plateau first use early, stays at about 1 a week, never reaches sustained use
#   drop    adopts like steady, then falls off over the last three weeks
#   never   no use at all
TEAMS = [
    ("Sample team A", "Sample manager A", {"early": 4, "steady": 4, "plateau": 1, "drop": 1, "never": 0}),
    ("Sample team B", "Sample manager B", {"early": 1, "steady": 3, "plateau": 3, "drop": 1, "never": 2}),
    ("Sample team C", "Sample manager C",  {"early": 3, "steady": 3, "plateau": 2, "drop": 2, "never": 0}),
    ("Sample team D", "Sample manager D",  {"early": 0, "steady": 2, "plateau": 2, "drop": 1, "never": 5}),
]

def weekly_rate(arch, week_idx, weeks_since_first):
    if arch == "early":
        return min(7, 3 + weeks_since_first * 0.8 + rng.uniform(-1, 1))
    if arch == "steady":
        return 2 + min(2, weeks_since_first * 0.5) + rng.uniform(-0.8, 0.8)
    if arch == "plateau":
        return 0.9 + rng.uniform(-0.4, 0.4)
    if arch == "drop":
        base = 2.5 + min(1.5, weeks_since_first * 0.5)
        if week_idx >= 5:
            base *= max(0.0, 1 - (week_idx - 4) * 0.45)
        return base + rng.uniform(-0.5, 0.5)
    return 0

roster, usage, views, responses = [], [], [], []
resp_rate = {"Sample team A": 0.9, "Sample team C": 0.75, "Sample team B": 0.4, "Sample team D": 0.0}
uid = 0
for team, manager, mix in TEAMS:
    for arch, n in mix.items():
        for _ in range(n):
            uid += 1
            user_id = f"user{uid:02d}@sample.invalid"
            roster.append({"user_id": user_id, "display": f"Pilot user {uid:02d}", "team": team,
                           "manager": manager, "available_from": AVAIL.isoformat(), "_arch": arch})
            # a manager response, decided up front so usage can show a recovery after the conversation
            recovery_from = None
            if arch in ("drop", "never", "plateau") and rng.random() < resp_rate[team]:
                trig = {"drop": "usage_drop", "never": "zero_use", "plateau": "adoption_plateau"}[arch]
                # drop alerts fire late in the window, so their responses land in the last days; the rest earlier
                when = END - dt.timedelta(days=rng.randint(1, 4) if arch == "drop" else rng.randint(6, 20))
                coached = rng.random() < 0.8
                responses.append({"user_id": user_id, "trigger": trig, "responded_on": when.isoformat(),
                                  "coaching_conversation_on": when.isoformat() if coached else ""})
                if coached and rng.random() < 0.7:
                    recovery_from = when
            if arch == "never":
                if recovery_from:
                    for dd in range((recovery_from - AVAIL).days + 1, DAYS):
                        day = AVAIL + dt.timedelta(days=dd)
                        if day.weekday() < 5 and rng.random() < 0.35:
                            usage.append({"user_id": user_id, "date": day.isoformat(), "agent": rng.choice(AGENTS), "uses": 1})
                continue
            first = {"early": rng.randint(0, 3), "steady": rng.randint(4, 14),
                     "plateau": rng.randint(1, 10), "drop": rng.randint(3, 10)}[arch]
            depth = {"early": 5, "steady": 3, "plateau": 1, "drop": 2}[arch]
            fav = rng.sample(AGENTS, depth)
            for d in range(first, DAYS):
                day = AVAIL + dt.timedelta(days=d)
                week_idx = d // 7
                wsf = (d - first) / 7
                rate = max(0.0, weekly_rate(arch, week_idx, wsf)) / 5.0  # uses per working day
                if recovery_from and day > recovery_from:
                    rate = max(rate, 0.55)  # coaching conversation landed; usage picks back up
                if day.weekday() >= 5:
                    continue
                if d == first or rng.random() < rate:
                    uses = 1 if rng.random() < 0.7 else 2
                    usage.append({"user_id": user_id, "date": day.isoformat(),
                                  "agent": rng.choice(fav), "uses": uses})
    # manager dashboard opens: North and East weekly-ish, South rarely, West never
    opens = {"Sample team A": 0.35, "Sample team B": 0.08, "Sample team C": 0.28, "Sample team D": 0.0}[team]
    for d in range(21, DAYS):
        day = AVAIL + dt.timedelta(days=d)
        if day.weekday() < 5 and rng.random() < opens:
            views.append({"manager": manager, "date": day.isoformat()})


DATA.mkdir(exist_ok=True)
with open(DATA / "roster_sample.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["user_id", "display", "team", "manager", "available_from"]); w.writeheader()
    for r in roster: w.writerow({k: r[k] for k in w.fieldnames})
with open(DATA / "usage_sample.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["user_id", "date", "agent", "uses"]); w.writeheader(); w.writerows(usage)
with open(DATA / "manager_views_sample.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["manager", "date"]); w.writeheader(); w.writerows(views)
with open(DATA / "responses_sample.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["user_id", "trigger", "responded_on", "coaching_conversation_on"]); w.writeheader(); w.writerows(responses)
json.dump({
    "_note": "Level 1 process-integrity inputs come from project records, not telemetry. SAMPLE values.",
    "readiness_assessment": {"completed_groups": 3, "target_groups": 4},
    "baseline_documentation": {"documented_groups": 4, "target_groups": 4},
    "manager_briefing": {"briefed": 3, "managers": 4},
    "milestones": {"completed_on_time": 5, "planned_to_date": 6}
}, open(DATA / "process_sample.json", "w"), indent=2)
print(f"roster {len(roster)}  usage rows {len(usage)}  manager opens {len(views)}  responses {len(responses)}")
