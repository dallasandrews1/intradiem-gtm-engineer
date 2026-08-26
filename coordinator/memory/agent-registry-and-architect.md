---
name: agent-registry-and-architect
description: AGENT_REGISTRY.md (coordinator root) is the single source of truth for Dallas's whole autonomous swarm; agent-architect subagent proposes new agents into the proposal ledger
metadata:
  type: project
---

Built Jul 19 2026. Two pieces of the "swarm that runs without being prompted" goal.

**`coordinator/AGENT_REGISTRY.md`** — the compiled list of everything working for Dallas: scheduled launchd jobs (warroom/dailyrundown/creditcheck/fridayreadout LOADED; controltower + intradiem.signals.daily plists exist but NOT loaded), on-demand subagents (clay-operator, credit-strategist, gtm-copy-reviewer, signal-researcher, agent-architect), workflows (gtm-proposal-sweep, war-room-fanout, motion-workflow-build), and the Mem0 catch-up cloud routine. Lives in coordinator so it travels with every workspace. Reconcile with `launchctl list | grep -iE "gtm|intradiem"`. Update it whenever an agent is added/loaded/unloaded.

**`agent-architect` subagent** (in ~/.claude/agents + coordinator mirror) — the brainstorming/strategy agent. Reads the registry (so it never proposes a duplicate) + memory + skills + logs, finds recurring toil / blind spots / handoff seams / skills-that-want-to-be-agents, and proposes 2-4 build-ready new-agent specs per run. Read-only, proposes never builds. Routes proposals into `automation/logs/proposal_ledger.md` tagged `[AGENT]` so the daily rundown surfaces them (no new notification path).

**Wired DAILY + LOADED (Jul 19):** `run_agent_architect.sh` + `com.dallasandrews.gtm.agentarchitect.plist` in `automation/`, weekdays 7:35 (after war room 7:15, before rundown 7:50 so proposals are in the ledger when the brief composes). Loaded into ~/Library/LaunchAgents; `launchctl list | grep agentarchitect` confirms. Same launchd/`claude -p --dangerously-skip-permissions` pattern as the other jobs. NOTE: when Dallas pastes the chmod/cp/launchctl commands himself, they run fine (user-authorized) — the classifier only blocks Claude self-initiating them. First unattended run: next weekday 7:35.

Finding surfaced to Dallas: controltower (intentional hold) and intradiem.signals.daily plists are NOT loaded, so those two are not actually running despite existing. See [[control-tower-build-status]], [[gtm-daily-rundown-jul18]], [[harness-capabilities-activated-jul18]], [[credit-strategist-agent]].

**Firing reality (verified Jul 19, Sunday):** all 5 loaded jobs show `runs=0` in launchctl — CORRECT, not broken. Loaded Fri Jul 17 PM; Sat/Sun have no weekday schedule; first real unattended fire is Mon Jul 20. The live agent-architect run FALSE-ALARMED this as "jobs broken, should have fired" without checking the weekend — do not repeat; verify runs=0 against the calendar+load-date. Scripts all executable, claude binary present. Repeating wake set `pmset repeat wakepoweron MTWRF 05:55` (launchd won't wake a sleeping Mac; Mac sleeps after 1min idle) so all morning jobs fire on time; undo `sudo pmset repeat cancel`. Monday proof = dated logs war-room-2026-07-20.md / daily-rundown-2026-07-20.md appear after ~8am. See [[validate-before-handoff]].
