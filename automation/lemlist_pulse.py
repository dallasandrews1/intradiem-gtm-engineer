#!/usr/bin/env python3
"""lemlist-pulse: read-only pull of Lemlist trial activity into a log the daily rundown reads.
Never DMs anyone (single-morning-brief rule)."""
import json
import os
import subprocess
import sys
from collections import Counter
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
API = "https://api.lemlist.com/api"


def load_key():
    with open(os.path.join(HERE, "config", "lemlist.env")) as f:
        for line in f:
            if line.startswith("LEMLIST_API_KEY="):
                return line.split("=", 1)[1].strip()
    sys.exit("LEMLIST_API_KEY not found in config/lemlist.env")


def get(key, path):
    out = subprocess.run(
        ["curl", "-s", "-u", f":{key}", f"{API}{path}"],
        capture_output=True, text=True, timeout=60,
    )
    try:
        return json.loads(out.stdout)
    except json.JSONDecodeError:
        return {"_error": out.stdout[:200]}


PLAN_GATE = "route is available starting"


def is_plan_gated(resp):
    return PLAN_GATE in str(resp)


def main():
    key = load_key()
    lines = [f"# Lemlist pulse - {datetime.now().strftime('%Y-%m-%d %H:%M')}", ""]

    lines.append("## Campaigns")
    camps = get(key, "/campaigns?version=v2&limit=50")
    campaigns = camps.get("campaigns", []) if isinstance(camps, dict) else camps
    if isinstance(campaigns, str):
        campaigns = []
    for c in campaigns:
        lines.append(f"- {c.get('name')} | status: {c.get('status')} | id: {c.get('_id')}")
    if not campaigns:
        if is_plan_gated(camps):
            lines.append("- PLAN-GATED: /api/campaigns needs emailPro (trial ended Aug 13). This is NOT zero campaigns; the relay's MCP path covers campaign state. Do not read this as all-quiet.")
        else:
            lines.append(f"- none (raw: {str(camps)[:150]})")

    lines.append("")
    lines.append("## Activity (last 100 events)")
    acts = get(key, "/activities?limit=100")
    activities = acts if isinstance(acts, list) else acts.get("activities", [])
    if isinstance(activities, str) or is_plan_gated(acts):
        activities = []
        lines.append("- PLAN-GATED: /api/activities needs emailPro. Reply detection now rides the relay's MCP inbox check; if that also logs BLOCKED, nothing is watching replies and the rundown must flag it.")
    counts = Counter(a.get("type", "unknown") for a in activities)
    for t, n in counts.most_common():
        lines.append(f"- {t}: {n}")
    if not activities and not is_plan_gated(acts):
        lines.append("- no activity yet")

    lines.append("")
    lines.append("## Open tasks (/api/tasks, not plan-gated)")
    tasks_resp = get(key, "/tasks?filters=%5B%5D")
    tasks = tasks_resp.get("results", []) if isinstance(tasks_resp, dict) else []
    by_kind = Counter(
        f"{t.get('campaignId', '?')} | {t.get('type', '?')}" for t in tasks
    )
    for k, n in by_kind.most_common():
        lines.append(f"- {k}: {n} open")
    if not tasks:
        lines.append(f"- none open (raw: {str(tasks_resp)[:120]})" if not isinstance(tasks_resp, dict) else "- none open")
    else:
        lines.append(f"- TOTAL open manual tasks: {len(tasks)} (sequences stall until these are done or removed)")

    replies = [a for a in activities if "replied" in str(a.get("type", "")).lower()]
    if replies:
        lines.append("")
        lines.append("### REPLIES (surface these in the rundown)")
        for r in replies:
            lines.append(
                f"- {r.get('leadFirstName', '?')} {r.get('leadLastName', '?')} "
                f"<{r.get('leadEmail', '?')}> in {r.get('campaignName', '?')} at {r.get('date', '?')}"
            )

    lines.append("")
    log = os.path.join(HERE, "logs", f"lemlist-pulse-{datetime.now().strftime('%Y-%m-%d')}.md")
    with open(log, "w") as f:
        f.write("\n".join(lines))
    print(f"wrote {log}")


if __name__ == "__main__":
    main()
