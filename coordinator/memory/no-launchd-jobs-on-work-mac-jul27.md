---
name: no-launchd-jobs-on-work-mac-jul27
description: PERMANENT RULE (Jul 27 2026) - never build, copy, or load a launchd scheduled job (.plist in ~/Library/LaunchAgents) on the work MacBook without an explicit fresh ask from Dallas; the personal Mac is the sole home for all 12 scheduled swarm jobs
metadata:
  type: feedback
---

Standing rule, permanent as of 2026-07-27: never build, copy, or load a launchd scheduled job (a `.plist` in `~/Library/LaunchAgents`) on the work MacBook (IntradiemDA / this machine) without an explicit fresh ask from Dallas in the moment.

**Why:** the work laptop is on-demand-only by deliberate decision. The personal Mac is the sole home for all 12 scheduled swarm jobs (war room, daily rundown, credit check, Friday readout, agent-architect, credit check, gate-integrity, pipeline-receipts, deliverability, competitor-watch, stars-refresh, table-hygiene, swarm-heartbeat). Duplicating any of them here would double-fire the single-morning-brief rule, producing two Slack DMs instead of one, which breaks [[gtm-daily-rundown-jul18]]'s single-ping contract.

**How to apply:** this holds even when a future task seems to call for "just scheduling this one check" or "loading this one plist so it fires here too." Ask first, every time. On-demand invocation of subagents/skills/workflows on the work Mac is fine; scheduled launchd jobs are the specific thing that stays off unless Dallas explicitly asks in that session. Relates to [[work-machine-operational-jul20]] (work Mac mirrors personal but plists not loaded there) and the [[nobody-but-dallas-routing-rule]].
