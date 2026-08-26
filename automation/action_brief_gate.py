#!/usr/bin/env python3
"""action-brief gate: deterministic decider for the Daily Action Brief job.
Prints a JSON list of rep keys due RIGHT NOW (weekday in the rep's timezone,
local time inside the post window, nothing posted yet today). The composing
step only runs for reps this gate emits, so the LLM never does timezone math.
BRIEF_FORCE=all (env) forces every rep due, used by the fixture dry-run."""
import json
import os
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
CFG = os.path.join(HERE, "config", "action_brief.json")


def main():
    with open(CFG) as f:
        cfg = json.load(f)

    if os.environ.get("BRIEF_FORCE") == "all":
        print(json.dumps(sorted(cfg["reps"].keys())))
        return

    start = cfg["post_window_local"]["start"]
    end = cfg["post_window_local"]["end"]
    last = cfg["state"].get("last_posted", {})
    due = []
    for rep, spec in cfg["reps"].items():
        now = datetime.now(ZoneInfo(spec["timezone"]))
        if now.weekday() >= 5:
            continue
        hhmm = now.strftime("%H:%M")
        if not (start <= hhmm <= end):
            continue
        if last.get(rep) == now.strftime("%Y-%m-%d"):
            continue
        due.append(rep)
    print(json.dumps(sorted(due)))


if __name__ == "__main__":
    sys.exit(main())
