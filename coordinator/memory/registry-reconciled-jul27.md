---
name: registry-reconciled-jul27
description: AGENT_REGISTRY.md's status column was stale since Jul 19; reconciled against live launchctl Jul 27 - 12 scheduled jobs loaded, only table-hygiene/control-tower/signals-daily unloaded, and none of the scheduling exists on the work laptop
metadata:
  type: project
---

2026-07-27: cross-checked `AGENT_REGISTRY.md` (last reconciled 2026-07-19) against live `launchctl list` on the personal Mac. 7 jobs the registry marked "built, LOAD PENDING" (meeting-capture, swarm-heartbeat, gate-integrity, pipeline-receipts, deliverability-watch, competitor-watch, stars-refresh-watch) were actually already loaded and running. Fixed the registry to reflect reality: all 12 `com.dallasandrews.gtm.*` jobs loaded, only `table-hygiene` (plist exists in `automation/`, never copied to `~/Library/LaunchAgents`), `control-tower`, and the `com.intradiem.signals.daily` cloud/local routine remain unloaded.

**DECIDED 2026-07-27:** none of this scheduled automation was ever transferred to the work MacBook (IntradiemDA), the Jul 20 `WORK_MACBOOK_SETUP.md` only covered `CLAUDE.md`, skills, the repos, and `.claude/agents`, never `~/Library/LaunchAgents`. Dallas confirmed this stays permanent, not a gap to close: the work laptop is on-demand-only (Clay UI plus ad hoc Claude Code), the personal Mac is the sole scheduling home. Never build/transfer launchd plists to the work laptop without a fresh explicit ask, since duplicating any of these 12 jobs there would double-fire the single-morning-brief rule.

**Also found via the same audit:** `clay-credit-steward/SKILL.md` and `cognitive-calibration/SKILL.md` had changed since the Jul 20 baseline in both their coordinator and global mirror copies and had not yet been transferred; included in the Jul 27 transfer zip. No subagent `.md` files changed since Jul 20, so the on-demand swarm roster is current on both machines already.

Related: [[work-laptop-sync-queued-jul27]], [[agent-registry-and-architect]].
