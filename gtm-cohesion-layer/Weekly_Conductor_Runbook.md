# Weekly Conductor — The Motion Runbook
**This is the "10× = one push becomes a weekly motion."** It turns your separate engines (signal, TAM, impact) and skills into one sequenced run. Without it you have 12 tools; with it you have *an engine*.

## The one push (runs weekly, Monday AM)
```
conductor.py  →  WIP gate (0)  →  7 stages, in order, fail-closed  →  guardrail tripwires (8)
```

| # | Stage | Reads | Calls | Writes | Gate |
|---|---|---|---|---|---|
| 0 | **Spec reread + Security** | `GTM_Engine_Build_Spec.md`, `security` | hash spec, check audit cadence | north_star (spec_hash, in_scope_motion, drift_log), security (audit_overdue) | warns on spec change / overdue audit; preflight FAILS if stale |
| 1 | **Refresh** | Clay Accounts/Contacts | enrichment/refresh agent (re-run rows >30d) | last_refreshed, list_health | skip if Clay not connected |
| 2 | **Re-score** | refreshed rows | fit/intent/grade formulas | grade, intent_score, list_health.accounts_by_grade | — |
| 3 | **Scan signals** | §6 signal sources | intradiem-signal-engine | signals.top_signals, top_signal | — |
| 4 | **Draft** | A/B/C grade + fired signals | first-draft-engine → copy-sharpener (3 variants/segment) | approval_queue.items[] | **never sends — drafts only** |
| 4b | **Critic** | drafted items, north_star, copy_standards.json | objective verifier (maker≠checker) | critic{}, critic_status/reasons per item | **OBJECTIVE GATE: holds bad drafts before the human queue (deliverability, ICP, in-scope, claims, length, copy standards: banned phrases, em dashes, uncontracted tells per the Jul 9 natural-CTA standard; edit copy_standards.json to change the list)** |
| 5 | **Approve** | approval_queue (critic-passed only) | (human) Dallas approves/edits/rejects | sequence_status=queued on approved | **HARD GATE: nothing proceeds without human approval** |
| 6 | **Send** | approved + valid email | Nate's sender | sequence_status=sent | **blocked if deliverability != green** |
| 7 | **Instrument** | SF/inbox activity, resolved_ledger | reply-sync agent, compute_draft_quality | funnel, reply_status, draft_quality (acceptance rate), conductor.runs[] | warns if acceptance < 0.5 floor (draft engine is the bottleneck) |

## Fail-closed rules (the guardrails are the product)
- **Stage 5 is a hard stop.** The conductor *prepares* a send; a human releases it. "AI enriches, people judge, human approval before anything leaves the building" — their words.
- **Stage 6 is deliverability-gated.** If `deliverability.overall_health != "green"`, Send is skipped and the run logs a warning. Volume never scales onto poisoned domains (premortem P1).
- **Stage 2 before any volume:** grade/score must compute on a test slice before Stage 4 drafts at volume. Measurement before volume.
- Each stage writes status to `conductor.runs[]` so a failure is visible, not silent.

## Go-live preflight (`python conductor.py --preflight`)
One command that runs every assertion the live motion depends on and prints a PASS/FAIL report: state structure, owner identity, attribution ratified, baseline set, deliverability green, all three engine contracts intact (it actually calls each engine and checks the keys the conductor reads), WIP sane, and approval-queue attribution. Exits nonzero if not ready. **The conductor calls preflight automatically on every live run and refuses to execute until it passes** — live operation is physically gated on a green preflight, so you can't start the motion on a portfolio that would fail silently. On seeded/pre-access data it correctly reports NOT READY (attribution, baseline, deliverability not yet live), which is the to-do list for Jul 6.

## Silent-failure elimination (no-silent-errors audit, Jun 24 2026)
A real ENT deployment can't have failures that look like success. Five fixes close that gap:
- **Send attribution assertion (Stage 6, live).** Before any approved row is sent, every item must carry a `released_by` that resolves to a known operator. A blank/unknown value aborts the whole batch **fail-closed** (run status `failed`, nothing sends) — an unattributed send would silently corrupt both the bottleneck share and the operator-test streak.
- **Measurement before volume (Stage 4).** If scoring (Stage 2) or signals (Stage 3) degrade, the engine has no trustworthy targeting, so drafting is held to a **test slice** and `approval_queue.volume_blocked=true`. Volume never rides on missing measurement.
- **Degraded runs are flagged, not hidden.** Any stage that can't produce real output calls `mark_degraded()`; the run finishes but its status carries `— DEGRADED (stage…)` so a partial run never reads as healthy.
- **Impact source health.** `impact_engine.build()` reports `sources` + `data_complete`; a missing upstream export (TAM/signals/outcomes) is flagged and degrades the run instead of silently rendering `$0` as if it were real.
- **Dashboard load-error banner.** All five HTML windows show a red "could not load engine_state.json — placeholder data, not live" banner on fetch failure, instead of silently rendering seeded zeros as truth.

## Premortem guardrails (the overhaul-survives-contact layer)
Three tripwires wrap the motion so the named failure modes from the day-one premortem can't materialize unseen. They live in `engine_state.json → guardrails`, recompute every run, and surface on the Control Tower + Approval Queue. The point is they **fail loud and early** — week 2–4, not at the 90-day review.

| Tripwire | Where it fires | What it catches | Trigger |
|---|---|---|---|
| **WIP-of-one** (stage 0) | `check_wip()` before the motion | Sprawl — building everything at once and shipping nothing (Failure #3) | `violation=true` if more than one motion is `scaling`. All other motions + the standing modernize-the-engine OKR sit in `backlog` until the scaling motion passes its operator-test. |
| **Throughput-by-operator** (stage 8) | `stage_guardrails()` | You become the bottleneck — the engine is operable-by-Dallas, not the team (Failure #1) | `alarm=true` if Dallas's share of weekly releases exceeds `dallas_share_ceiling` (20%). Alarm = do **not** scale; fix operability. |
| **Operator-test** (stage 8 + approval queue) | `stage_guardrails()` + `released_by` on each approval | "Done" meaning *works when Dallas runs it* instead of *the team runs it unaided* (Failure #1) | A motion flips to `operable` only after `required_team_releases` (2) consecutive batches released by a non-Dallas operator. **Every Dallas release resets that motion's streak to 0.** |

**Definition of done changes here.** A motion is not overhauled because it works — it is overhauled when Genna or Nate releases its weekly batch without you, two weeks running, and the bottleneck alarm stays green. The approval queue makes this physical: every release stamps `released_by`, and choosing yourself throws an owner-warning and resets the streak. The dashboards do the policing so you don't have to remember to.

**The one rule the guardrails encode:** *you are the owner who designs the motion; the team are the operators who run it.* Build for operable-by-the-team or the tripwires turn red.

## What "one push" means operationally
You run (or schedule) `conductor.py` once. Stages 1–4 + 7 are automated. Stage 5 surfaces a queue you clear in ~15 min. Stage 6 fires only what you approved. The dashboards update from `engine_state.json`. That's the weekly motion the rest of the org copies — "the team that pilots it becomes the blueprint."

## Scheduling
Run as a scheduled task every Monday 8:00 AM (see `com.intradiem.conductor.weekly` / the schedule skill). Pre-access: it runs in **dry-run** mode (logs intended actions, writes seeded state) so the wiring is proven before Jul 6.

## Pre-access vs live
- **Now (dry-run):** conductor sequences the stages, calls existing local engines where present, writes seeded `engine_state.json`, prints the plan. Proves the orchestration.
- **Jul 6 (live):** flip `DRY_RUN=False`, wire stage 1/6/7 to Clay + sender + SF. No structural change.
