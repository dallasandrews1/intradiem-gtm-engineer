---
name: context-bus-cross-laptop-aug6
description: The context bus built 2026-08-06 that carries working context from the personal Mac to the work MacBook, so the Enterprise Claude account stops starting cold; how to run both halves
metadata:
  type: project
---

2026-08-06: built the **context bus** to close the gap Dallas hit repeatedly, getting stuck mid-session on the Intradiem Enterprise account, doing the work on the personal Mac instead, then forwarding outputs to himself while the work machine's Claude kept none of the memory or context behind them.

**Shape: automated inbound, deliberate outbound.** The personal Mac publishes on a schedule. The work Mac only ever pulls. Nothing auto-uploads from the work machine. This is what keeps it consistent with the standing Jul 27 decision in `AGENT_REGISTRY.md` that the work laptop is never a second scheduling home (see [[work-machine-operational-jul20]]).

**Personal Mac (publisher), `com.dallasandrews.gtm.contextbus`, weekdays 12:30 / 17:00 / 21:00.** Three drops a day, not nightly, because the real pattern is getting stuck mid-day and switching machines the same afternoon. `automation/run_context_bus.sh` calls `automation/context_bus_stage.py`, which stages three payloads: the `~/coordinator/memory/` delta plus the live index, changed skills/agents/automation/workflows, and distilled skeletons of human Claude Code sessions. Claude then writes one digest per session into `~/context-bus/digests/` and rewrites `INBOX.md`, and the script commits and pushes to the private repo `dallasandrews1/context-bus`. It never DMs; it writes `automation/logs/context-bus-<date>.md` and the daily rundown reads it (registry rules 2 and 4). If nothing changed it exits before spending a Claude call. The watermark in `~/.context-bus-state.json` only advances on a successful push, so a failed run republishes the same delta instead of silently dropping it.

**Work Mac (ingest), by hand, pull-only.** `~/context-bus/bin/ingest.sh` pulls, expands the token, lands the memory delta into `~/coordinator/memory/`, and stages assets into `incoming/assets/` for review rather than overwriting skills the work machine may have diverged on. Then Dallas pastes the block in `~/context-bus/INGEST.md` into Claude Code. First-time setup there is `git clone https://github.com/dallasandrews1/context-bus.git ~/context-bus`, and `~/coordinator` must already be placed or the memory delta has nowhere to land (trap 1 in [[work-machine-transfer-gotchas]]).

**Reverse direction: `~/context-bus/bin/handoff.sh`, either machine.** Writes `~/Desktop/handoff-<date>-<time>.md` with the current session's prompts, decisions, and changed files. It makes **no Claude call at all**, deliberately, because the moment it is needed is the moment Enterprise usage is gone. Supersedes the manual transcript-copy procedure in [[cross-account-work-recovery]], which still explains the underlying `.jsonl` facts.

**Two design facts worth keeping:**
1. **The `{{HOME}}` token.** Everything publishes with this machine's home path replaced by `{{HOME}}`; ingest expands it to the receiving machine's real home. This permanently retires the `/Users/dallasandrews` to `/Users/IntradiemDA` rewrite pass from [[work-macbook-username-intradiemda]] for anything moving through the bus. A hard sweep runs over generated payload before every commit so a digest can't reintroduce a literal path.
2. **`entrypoint` is the only reliable way to tell a human session from a scheduled one.** Scheduled swarm runs are `entrypoint == "sdk-cli"`; human sessions are `claude-vscode` or `cli`. `promptSource` does NOT work for this: interactive VS Code sessions emit a stray `promptSource == "sdk"` record too, which silently produced zero digests on the first build. Without this filter the bus would try to digest 400+ cron transcripts.

**First live run, 2026-08-06:** 9 digests, 43 memory files, 28 assets, pushed clean. It independently surfaced the WFM Clay customer-exclusion leak (6 contacts at READY, 5 Elevance) as the top unclosed thread carried forward, which is the exact failure mode it exists to prevent.
