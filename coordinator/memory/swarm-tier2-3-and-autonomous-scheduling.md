---
name: swarm-tier2-3-and-autonomous-scheduling
description: Jul 19 build — Tier 2/3 agents + scheduled wrappers making the whole swarm autonomous (log-to-rundown), including retro-scheduling the Tier 1 agents
metadata:
  type: project
---

Built Jul 19 2026 after Dallas's directive that the swarm must run without him remembering to launch anything (see [[swarm-default-autonomous]]). Everything writes a dated log to `automation/logs/` and the daily rundown consolidates; nobody-but-Dallas + single-morning-brief held throughout.

New agent defs (~/.claude/agents + coordinator mirror): meeting-capture (Otter transcripts -> outcomes/follow-up drafts/missing-record flags), deliverability-watch, competitor-displacement-watch (reads war-room logs, no web re-scan, builds displacement briefs), stars-refresh-watcher (watches CMS for the Stars release, stages the October refresh, go daily from Sept).

**deliverability-watch source RESOLVED Jul 19:** sending mailbox = nathan.belfield@Intradiem.com; warmup status (Status/Reputation/Daily sends) lives on Clay's Campaigns -> Email accounts surface, which is NOT exposed to the Clay MCP or CLI (verified: surfaces_list only does audience/function; `clay --help` has no campaign command). So it's mirrored into `automation/logs/deliverability_status.md`, hand-updated by Dallas when it changes (rare, warmup is slow). Seeded Jul 19 with real values: Warming up, reputation 96%, 20/20 daily sends, warming since Jul 13, 5 campaigns, 23 emails already sent on campaign 1. CORRECTION (Dallas, Jul 19): "warming up" does NOT mean sends are off — the mailbox warms BY sending at a capped daily volume and campaign 1 is LIVE. The gate is a VOLUME GOVERNOR, not on/off: keep to the warmup cap, watch reputation (>=~90%), do not blast the full universe in one wave until warm/established. Human gate stays = Draft + Nathan review (not the send_ready column). Agent must never report sends as "off." All 7 new jobs confirmed LOADED Jul 19 and `pmset -c sleep 0` (never-sleep on AC) confirmed set — swarm fires on the clock.

New scheduled launchd jobs (all `built, LOAD PENDING`, scripts + plists in automation/, all passed plutil + zsh -n):
- meetingcapture weekdays 7:05
- swarmheartbeat weekdays 7:45 (PURE BASH, no LLM — checks each job's launchctl runs + today's logs, writes swarm-health-<date>.md)
- gateintegrity Mon 7:20 (Tier 1 retro-scheduled; also on-demand before a wave)
- pipelinereceipts Thu 7:20 (Tier 1 retro-scheduled; ready for Fri readout)
- deliverabilitywatch Mon 7:10
- competitorwatch Wed 7:10
- starsrefreshwatch Mon 6:40

Wired: run_daily_rundown.sh prompt expanded to read all new logs and LEAD the brief with the swarm-health line (which jobs fired / MISSING). reply-triage stays on-demand only until an inbox-watch source is wired.

Activation (Dallas runs in his OWN terminal, one block): chmod +x the 7 new scripts, cp the 7 plists to ~/Library/LaunchAgents, launchctl load each, grep to confirm. Classifier blocks Claude from chmod-on-skip-perms + ~/Library writes. First fires: next matching weekday, on the clock once `sudo pmset -c sleep 0` is set. See [[tier1-swarm-agents-built]], [[agent-registry-and-architect]], [[validate-before-handoff]].
