---
name: gtm-daily-rundown-jul18
description: Daily GTM rundown Slack DM built Jul 18 (skill + launchd job); phase 1 of the supervised orchestrator loop.
metadata:
  type: project
  date: 2026-07-18
---

Dallas wants ONE consolidated daily Slack DM as GTM Engineer: everything important stacked most-important-first, plus surfaced/invented strategy ideas. Daily, not weekly (his iteration rate). Confirmed via AskUserQuestion: **supervised loop** (not self-rewriting) and **daily rundown first**.

**Built 2026-07-18 (phase 1):**
- Skill `gtm-daily-rundown` at `coordinator/.claude/skills/gtm-daily-rundown/SKILL.md`, mirrored to `~/.claude/skills/`. Reads control_tower_state.json, today's war-room log, Clay registry, engine_state/impact, credit ledger, account_plays; composes a 5-section ranked brief (1 gates+blockers, 2 what fired overnight, 3 motion movement w/ deltas vs yesterday, 4 credit posture, 5 ideas+strategy); writes `automation/logs/daily-rundown-<date>.md`; posts ONE Slack DM to Dallas; seeds `automation/logs/proposal_ledger.md` (append-only proposal queue = head start on the orchestrator's phase 2).
- `automation/run_daily_rundown.sh` mirrors the war-room job pattern (claude -p headless + unattended ground rules). Refreshes control-tower state via `build_control_tower.py` first, so gates/blockers/motions are current even though the control-tower launchd job stays parked.
- `automation/com.dallasandrews.gtm.dailyrundown.plist`: weekdays 7:50 AM (after the 7:15 war room lands its log).

**First live run delivered 2026-07-18** (interactive test at Dallas's request): full chain worked, DM sent to Dallas's own Slack (U0BB0VCHDCH). Degradations handled correctly (today's war-room log absent → used 07-17, labeled; no prior rundown → no deltas; account_plays.json stale Jun 13 → not used). Wrote daily-rundown-2026-07-18.md + seeded proposal_ledger.md (1 entry: teach tower the live WFM 524-row count). Known instrumentation gap surfaced: tower shows WFM universe 0/SEEDED because engine_state.accounts_by_motion lacks a wfm count, while live L3 = 524.

**ACTIVATED 2026-07-18:** Dallas pasted the 3 commands, classifier allowed them under explicit instruction. `com.dallasandrews.gtm.dailyrundown` is loaded in launchctl (verified, exit 0) alongside warroom/creditcheck/fridayreadout; plist in `~/Library/LaunchAgents/`. Fires weekday mornings 7:50. Control-tower job still NOT loaded (parked, as planned).

**Open flag:** war room DMs top-5 at ~7:20 AND the rundown DMs at ~7:55 = two morning pings. Rundown is the superset. Offered to mute the standalone war-room DM so the rundown is the single morning brief; Dallas's call (not yet decided).

**Credit→pipeline receipts ledger added to the daily DM (Dallas, 2026-07-18):** section 4 reframed from "credit posture" to "CREDITS → PIPELINE RECEIPTS" — the renewal artifact. Leads with "$X of the $5K one-time proof budget → N replies, M meetings, $P pipeline." Reads `automation/logs/credit_pipeline_receipts.md` + live `clay credits`. The 72K is a ONE-TIME $5K proof budget (see [[credit-budget-correction-jul18]]); the DM tracks credits-in vs pipeline-out as the renewal case.

**DMs consolidated 2026-07-18:** Dallas asked to end all standalone morning DMs and wrap them into the one brief. Muted the DM step in run_war_room.sh, run_credit_check.sh, run_friday_readout.sh (they now write logs only). The rundown skill reads the credit-check log and, on Fridays, surfaces the Naveen readout draft path. Schedule already sequences the rundown last (credit check Thu 7:00, Friday readout Fri 6:00, war room daily 7:15, rundown daily 7:50). **STANDING RULE added to both CLAUDE.md files (Working conventions):** the gtm-daily-rundown is Dallas's ONLY automated morning ping; any new scheduled agent writes a log and never DMs him independently, and gets wired as a source the rundown reads.

**Still standalone (outside launchd, not yet folded):** the Weekly Automation Strategist cloud routine (trig_0176q8Xh2HohHkdCdCG7hAMo, Mon 7am CT) still DMs 2-3 automation ideas + saves a backlog. To fold it: disable its DM in the routine and have Monday's rundown read its saved backlog. Flagged to Dallas.

**Phase 2 (not built):** the supervised orchestrator loop. Guardrail-layer edits (skills, system prompts, send gates) become one-tap DM proposals with diffs; non-guardrail state (priorities, hot accounts, its ledger, read-only scheduling) the loop updates freely. Local launchd only (repo has no git remote, cloud RemoteTrigger can't reach it). See [[control-tower-build-status]].
