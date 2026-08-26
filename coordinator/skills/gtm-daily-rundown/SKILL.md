---
name: gtm-daily-rundown
description: "Daily GTM Engineer rundown for Dallas. Reads the control-tower state, the morning war-room log, the credit ledger, the Clay registry, and the engine/impact state, then composes ONE Slack DM stacked most-important-first: gates and blockers, what fired overnight, motion movement, credit posture, and a strategy-ideas block. Computes deltas against yesterday's rundown and seeds a standing proposal ledger. Trigger on: daily rundown, morning brief, my daily, what matters today, run the rundown. Runs every weekday morning after the war room; this is Dallas's single consolidated morning brief, not the Naveen readout."
---

## When this skill applies

- Every weekday morning, after the war-room sweep has written its log (scheduled run at ~7:50, war room at 7:15)
- Any time Dallas asks for his daily brief, morning rundown, or "what matters today"

This is Dallas's OWN brief. It is internal, dallas-brand voice, ranked, and allowed to be blunt. It is not the Naveen readout (that stays weekly, peer-level, exec-facing). Never blend the two.

**This is the single morning DM.** The other scheduled jobs (war room, credit check, Friday readout) no longer DM Dallas; they write logs, and this rundown consolidates them into one ping. On days a job ran (credit check Thursdays, Naveen draft Fridays), surface its result here so nothing that used to arrive as its own DM goes missing. Any new scheduled agent follows the same rule: it writes a log, this brief carries the signal.

## Background

Dallas iterates fast, so he wants one consolidated morning DM that tells him what is important in his GTM Engineer world, stacked most-important at the top, plus any genuinely good idea worth acting on. The brief is a query result over the engine's own state files, not a memory exercise. Its honesty architecture is inherited: surfaced vs realized never blended, SEEDED/stale never rendered as live fact, verified-claims gate on any Intradiem number.

## Inputs (read in this order; if a file is missing or stale, SAY so in that section rather than estimating around it)

1. `control_tower_state.json` (repo root): gates (deliverability, credit, baseline), per-motion build_state + universe + funnel, blockers_and_asks (open-flagged), credit posture. The run script refreshes this via `build_control_tower.py` before this skill runs, so treat it as current.
2. `automation/logs/war-room-<today>.md`: overnight signals, priority ranks, plays, anything staged. If today's file is absent, note "war room log not found for today" in the signals section.
3. `Clay_Build_State_Registry.md`: present-tense ground truth for Clay build state and open ⚠️ blockers.
4. `gtm-cohesion-layer/engine_state.json` and `impact/impact.json`: funnel, approval queue, opportunity surfaced vs realized (never blend).
5. `clay_credit_ledger.csv` and `automation/logs/credit_pipeline_receipts.md`: the credit→pipeline receipts ledger (the renewal artifact). Also pull live credits via `clay credits`.
6. `automation/logs/credit-check-<most-recent>.md`: the weekly credit reconciliation narrative (runs Thursdays 7:00), if present.
7. `automation/logs/naveen-readout-<today>.md`: on Fridays only, the Naveen readout draft (runs Fridays 6:00). If present, surface a one-liner in the brief pointing to it.
8. `tam-outbound-engine/account_plays.json`: hot accounts, for the ideas block.
10. `automation/logs/heat-list-<today>.md` (heat-list-scorer, weekdays 7:20 and 13:00): the signal-marketing loop's Heat List. Surface Lane A rep alerts (who got pinged, approve/deny state), any customer_am hits (route to the AM clearance sheet, never cold), and the lane counts; note DRY RUN vs LIVE in the header. If absent, say "heat list log not found for today".
11. `automation/logs/cohort-cutter-<most-recent>.md` (cohort-cutter, Tuesdays 8:00, bi-weekly anchor Sep 8 2026): when a cohort was cut or is WAITING under the 300 floor, carry the cohort id, arms, clock dates (ads T0, email 1 T+5), and the files Sierra and the reps need. Off-week runs need one line at most.
9. `automation/logs/daily-rundown-<yesterday-or-most-recent>.md`: the prior brief, to compute what changed since. If none exists, this is the first run; skip deltas and say so.

## Unattended ground rules (for scheduled runs)

- Read-only over the whole repo EXCEPT `automation/logs/`. Never touch send gates, campaign settings, skills, system prompts, or any live Clay/Apollo data.
- Do not send, post, or message anyone except Dallas himself. Slack target is his own user (search for his user, not a channel).
- Never render a SEEDED or stale value as live fact. Label trust where the state files label it.
- Any Intradiem metric, ROI, or proof point must pass the verified-claims gate (Intradiem Value Repository). Mark anything else `[UNVERIFIED]`. Do not invent numbers to fill a section.
- No em dashes anywhere in the output.

## The stack (compose in this order, most-important at top)

1. **GATES + BLOCKERS.** Anything that stops a send today. Deliverability gate, credit flag, and every OPEN blocker from `blockers_and_asks` and the registry, each with the one action that clears it. If a gate is UNKNOWN or stale, say so plainly. This section leads because it is what would silently cost a day.
2. **WHAT FIRED OVERNIGHT.** The war room's Priority 1-2 signals only, each mapped to its Intradiem play and the account it hits. Note anything staged for review. Skip low-priority noise.
3. **MOTION MOVEMENT.** Per-motion build_state and funnel, and the delta since yesterday's brief (rows loaded, drafts generated, gate changes, blocker cleared). Call out the motion closest to a send. If nothing moved, say "no movement" rather than padding.
4. **CREDITS → PIPELINE RECEIPTS.** This is the renewal artifact, treat it as a first-class section, not a footnote. The ~72K credits are a ONE-TIME $5,000 proof budget (not monthly); the whole trial is whether they convert to pipeline. Show the ledger: credits spent so far (pull live via `clay credits`), credits remaining and % of the 72K burned, and against that spend the RECEIPTS, replies, booked meetings, and pipeline generated. Compute cost-per-reply and cost-per-meeting once outcomes exist. Lead with the receipts framing ("$X of the $5K proof budget spent → N replies, M meetings, $P pipeline"), because that sentence is the renewal case. Flag loudly if credits are burning with no pipeline movement, or if a planned run would spend a big slice of the trial budget without a clear pipeline path.
5. **IDEAS + STRATEGY.** 1 to 3 ideas, each surfaced from the day's state or reasoned from it. Every idea gets: the why-now (what in today's data prompts it), and the first move (the smallest next step). Prefer extending an existing workflow/motion over a net-new build. If a genuinely strong idea appears, lead this section with it and say why it is the strong one. This is the part Dallas explicitly asked for; do not phone it in, but do not manufacture an idea when the honest answer is "nothing new worth acting on today."

Keep the whole DM skimmable: bold section headers, tight bullets, no walls of text. The full detail goes in the log file; the DM is the ranked signal.

**Causal chain (per `automation/LOG_CONVENTION.md`):** in the full LOG FILE, every item carried from another job's log cites its source with a `chain:` line (e.g. `chain: war-room-2026-08-03#elevance-cms-litigation`). If the upstream item has no evt id, cite the file. Event ids are plumbing: they appear in the log file only, NEVER in the Slack DM.

## Proposal ledger (seed for the orchestrator loop)

After composing, append any idea from section 5 that implies a change to a skill, a system prompt, a gate, or a new automation to `automation/logs/proposal_ledger.md` (append-only; create with a header if missing). Format each entry: date, one-line proposal, the why-now, a `chain:` line citing the evt id (or log file) that prompted it, and the concrete change it would require (name the file/skill and the edit in words, do NOT make the edit). This is a proposal queue for Dallas to approve, not an action log. Guardrail-layer changes are never applied here; they are only proposed.

## Output

1. Write the full brief (all five sections, full detail) to `automation/logs/daily-rundown-<today>.md`. Figure out today's date yourself.
2. Send Dallas one Slack DM with the ranked brief (tight version) plus the log file path. If a top-priority gate or blocker is open, put it in the first line so it is unmissable.
3. If the run degraded (a state file missing/stale, war room log absent), say so in the DM so a silent failure never reads as "all clear."
