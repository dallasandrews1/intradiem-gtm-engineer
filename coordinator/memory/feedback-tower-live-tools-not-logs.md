---
name: feedback-tower-live-tools-not-logs
description: "Dallas, Sep 15 2026: the control tower is useless unless it actively checks the live tools at build time; a stale or wrong number (the 693-credit ledger figure) in front of Naveen would destroy his credibility. Live pulls first, logs only as dated carries."
metadata:
  type: feedback
---

Sep 15 2026, after the tower showed "693 credits used" from the CSV ledger while the workspace had consumed ~22,200: "the 693 credits is not true, I've spent thousands" and "the tower is useless if it is not actively checking all the live tools we have access to and paid for. If Naveen were to see that it would destroy my credibility."

**Why:** the tower is a credibility surface. Any leadership-facing number must come from the tool that owns it, pulled at build time and stamped with the pull time; a log from last week is a carry, not a read, and the page has to say so.

**How to apply:** `build_control_tower.py` pulls live at every build: `clay credits` (consumed = made-available from `automation/config/clay_credits.json` minus balance), real rows from the send tables in `automation/config/tower_live_tables.json` (READY, HOLD, customer flags, leaks), lemlist campaigns through `campaign_scorecard.live_read()` in a subprocess (five-minute cap, DEGRADED when more than a quarter of exports fail, then the history is carried and labelled), `launchctl list` for the swarm. Connector-only tools (Otter, Outlook, Slack, Salesforce via Clay Audiences, Monday, Apollo) appear on the live-checks strip as "agent read" dated by their newest log, never as live. The CSV credit ledger feeds nothing on the page. Same standard for any future dashboard: pull, stamp, or say it is carried. See [[control-tower-animated-rebuild-sep15]].
