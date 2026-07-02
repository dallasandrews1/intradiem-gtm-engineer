# GTM Engine — Cohesion Layer
**The connective tissue that turns your 12 point-tools into one motion.** Built Jun 24 2026, pre-access. Everything here runs in dry-run / seeded mode now and goes live on Jul 6 by wiring the marked TODO hooks — no structural change.

## The problem this fixes
You had strong *engines* (signal, TAM, impact), strong *skills*, and strong *dashboards* — but they were separate, each with its own state, and the credit line + send guardrail weren't instrumented. This layer wires them into a single loop with one source of truth.

## Files
| File | What it is | Why it matters |
|---|---|---|
| `control_tower.html` | **Open this first.** One screen: headline numbers, the 7-step line diagram, and a tile that opens each window (with an exec talk-track per window). | Where you SEE and demo the whole engine. |
| `engine_state.json` | **Single source of truth.** Every dashboard reads it; conductor + agents write it. | Kills dashboard drift (gap #5). |
| `variant_tracker.html` | Which message wins, by qualified-reply rate per segment; conductor promotes winners / retires losers. | Closes the messaging loop (Rippling proof). |
| `Clay_Build_Pack.md` | Click-by-click Clay build below the Build Spec: tables, columns in order, waterfalls, fit/intent/grade formulas, signal columns, source-tag writes, webhooks. | Day-1 = rebuild in ~2 hrs, not design from scratch. |
| `Attribution_Loop_Spec.md` | Reply-sync agent: reply → classify → `reply_status` → funnel, source-scoped. | **The credit-war keystone.** |
| `attribution_dashboard.html` | Live two-motion funnel; credit line highlighted; Week-1 ratification gate. | Makes attribution an instrument, not a claim. |
| `Weekly_Conductor_Runbook.md` | The 7-stage motion + fail-closed/human/deliverability gates. | The "10× = one weekly push." |
| `conductor.py` | Runnable orchestrator (dry-run now). Sequences all stages, logs each run to state. | The actual engine. Verified: all gates fire. |
| `approval_queue.html` | Human approve/edit/reject before anything sends. | The "people keep judgment" guardrail, operational. |
| `deliverability_monitor.html` | Domain health vs. the floor; green = the send gate. | Premortem P1 (protects the 157 warm contacts). |

## How it flows
```
Clay (Build Pack) ──enrich/score──▶ engine_state.json ◀──writes── conductor.py (weekly push)
                                          │                              │
        attribution_dashboard ◀──reads────┤                     Stage 4: draft
        approval_queue        ◀──reads────┤                     Stage 5: HUMAN approves  ← approval_queue.html
        deliverability_monitor◀──reads────┘                     Stage 6: send (gated)    ← deliverability_monitor.html
                                                                Stage 7: reply-sync → funnel
```

## Day-1 / Week-1 order of operations
1. **Ratify attribution in writing with Naveen** (credit line + 3 SF fields + 1× baseline). Set the flags in `engine_state.json`. *Do-nothing-else move.*
2. Build Clay from `Clay_Build_Pack.md` on a 10-row test slice; confirm scoring/ICP with Naveen + Scott Kemme.
3. Stand up deliverability warmup → monitor green before any volume.
4. Flip `conductor.py` `DRY_RUN=False`; wire Clay/sender/SF hooks; schedule Monday 8am.
5. First real run: small, 3 variants/segment, human-approved, instrumented.

> Governing principle, baked into every gate: **measurement before volume, ICP before sourcing, human before send.**

## Conductor is wired (Jun 24)
`conductor.py` now actually calls your three existing engines (read-only, seeded data, safe to run today):
- Stage 2 Re-score → `tam-outbound-engine/account_engine.py` (`build_plays`) → writes grade distribution.
- Stage 3 Signals → `intradiem-signal-engine/signal_processor.py` (`process`) → writes top firing accounts.
- Stage 7 Instrument → `impact/impact_engine.py` (`build`) → writes the impact scorecard ($ surfaced, signals, pipeline).
Engine calls are best-effort: if one isn't available pre-access, that stage logs "skip" and the run continues.

## Loop-engineering hardening (Jun 25) — gaps 1–4 closed
Pressure-tested the motion against the "loop engineering" discipline (Anthropic eng docs + Osmani). Four upgrades, all wired into `conductor.py` + `engine_state.json` + `approval_queue.html`, verified in dry-run:

1. **Cost per accepted change** (`draft_quality`). The loop's real health metric: `clean_accept` (sent with no edit — the loop saved the work) vs `edited_then_approved` (you rewrote it — it didn't) vs `rejected`. Below the 0.5 floor = the **draft engine** is the bottleneck, not the gate. Recomputed every run from `approval_queue.resolved_ledger`; surfaced as a tile on the Approval Queue.
2. **Independent critic** (Stage 4b, `stage_critic`). The agent that *drafts* is not the agent that *passes*. An **objective** pre-human gate (deliverability, ICP/persona, in-scope motion, verified-claims, length) holds bad drafts *before* they reach your queue — so the human gate isn't the first filter and your bottleneck shrinks. Objective by design, never "two optimists agreeing." Live TODO: add a verifier subagent for subjective brand/voice on top of the hard objective gate.
3. **Spec reread** (Stage 0, `stage_spec_reread` + `north_star`). State says where the engine *is*; the standing spec (`GTM_Engine_Build_Spec.md`) says where it's *going*. The conductor rereads + hashes it every run and logs drift, so "don't do X" constraints can't silently evaporate over a multi-week sequence. It also re-asserts the single in-scope motion — which is why an out-of-scope Back Office draft is now correctly **held** while Star Ratings is the scaling motion.
4. **Security cadence** (`security` + `check_security` + preflight). An unattended loop is an unattended attack surface. Enforced as a **cadence**, not memory: 30-day permission re-audit, log-sanitization, audit-skill-sources-before-install. A stale audit or disabled sanitization is now a **go-live FAIL** in preflight.

> The framing that matters for Naveen: *I don't automate the judgment — I automate everything around it and put a hard gate where the judgment lives.* Maker (draft engine) → objective checker (critic) → human (you). Three layers, not one.

## Clay: build in your free trial, template into Intradiem
You CAN carry the configuration over. Workflow:
1. Build the tables from `Clay_Build_Pack.md` in your **free-trial** workspace **on a tiny test slice** (protect trial credits).
2. Per table: **Actions → Share as template → Turn on sharing** → copy link.
3. In your Intradiem workspace (Jul 6), open each template link to recreate the table.
**What transfers:** table structure + columns + formulas + 1 sample row. **What does NOT:** your data (re-import via CSV or write-to-table) and provider/integration auth (re-connect API keys in the new workspace). So design once now, re-instantiate clean later — run real volume only in Intradiem on the 5,000 credits.

## Live artifacts: not yet — here's why
Keep these as HTML files for now. They read `engine_state.json` and refresh on every conductor run; a sandboxed Cowork artifact can't read that local file, so promoting them today would actually *freeze* them on seeded data. Promote the attribution dashboard to a live artifact at Jul 6, wired to Salesforce via connector. Your daily human view (`dallas-mission-control`) already covers the "check it each morning" need.

## Live-wire checklist (the only edits needed Jul 6)
- `conductor.py`: set `DRY_RUN=False`; fill the `TODO(live)` hooks in stages 1, 3, 4b (critic subagent), 6, 7.
- `Attribution_Loop_Spec`: point input #1 at SF/sequencer; reverse webhook → Clay.
- `engine_state.json`: replace all `EXAMPLE`/seeded values; flip ratification + field flags as they become true.
- `security`: run the first permission audit (set `last_permission_audit`), review every `connector_scopes` entry to least-privilege (`least_privilege_reviewed=true`), enable `log_sanitization_enabled`. **Preflight FAILS `security_audit_current` until all three are true** — and re-audit every 30 days thereafter (the conductor warns when overdue).
- `north_star.approved_claims`: seed the verified figures the critic should allow (everything else — any $/%/"N points" — is held for verification against `intradiem-verified-metrics`).

### Go-live gate — run preflight first
**Step 0: `python conductor.py --preflight`.** It runs every assertion the live motion depends on (state structure, owner identity, attribution ratified, baseline set, deliverability green, all three engine contracts intact, WIP sane, approval-queue attribution) and prints a PASS/FAIL report. It must say **READY** before you flip `DRY_RUN=False`. The conductor also calls preflight automatically on every live run and **refuses to execute** (fail-closed) until it passes — you cannot start the live motion on a portfolio that would fail silently.

### Guardrail integrity at go-live (do NOT skip — these fail silently if wrong)
The three premortem tripwires are only trustworthy if their inputs are clean. Before flipping `DRY_RUN=False`:
1. **`released_by` must be the REAL human who clicked release**, captured from the production release handler (SSO/Salesforce user), not auto-stamped and not free text. Constrain it to the `operators` controlled vocabulary. A wrong or blank `released_by` corrupts both the bottleneck share and the operator-test streak.
2. **Exactly one operator carries `is_owner: true`** (Dallas). The owner is matched by this flag, never by name string — if zero or multiple operators are flagged, the conductor raises `integrity_error` and forces the alarm on (fail-loud). Verify the flag survives any re-seed of `engine_state.json`.
3. **Operator-test streak authority moves to the conductor.** The per-item streak increment in `approval_queue.html` is PREVIEW-ONLY. At go-live, advance `consecutive_team_releases` **once per weekly run** from a per-motion release ledger (`released_by` + `motion` + week): if the owner released any item of that motion in the week → reset to 0; else if the team released it → +1. Do not let per-item front-end clicks drive the multi-week streak.
4. **Weekly throughput window is live.** `roll_weekly_window()` runs only when `DRY_RUN=False`; confirm `window_start` is set on first live run so `released_this_week` resets each week instead of accumulating into a lifetime total.
5. **Re-verify after wiring:** run the conductor and confirm `0 Window` rolls, `0 WIP` gates, and `8 Guardrails` reports a real (non-seeded) share, operator-test status, and no `integrity_error`.
