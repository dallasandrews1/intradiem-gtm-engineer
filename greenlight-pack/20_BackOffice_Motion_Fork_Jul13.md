# Motion #2 — Back-office fork stood up (Jul 13 2026)

Executes section C of `18_L2_NextBuild_Spec` (the motion fork) ahead of the ICP being ratified, so the engine is ready the moment Scott's edits land. The whole fork is 0 credits; the only paid steps (sourcing the 200, the monthly signal sweep) stay held for explicit go. Operating on the v0 straw-man ICP (`BackOffice_ICP_v0.md`) as the working assumption, not waiting on the Scott conversation to begin the build.

## The design call: fork, not copy

The Stars motion and the back-office motion share one config and one scorer but run **opposite kill switches**. That is the whole reason this is a second motion and not a second table:

| | Star Ratings (new-logo) | Back office (install-base) |
|---|---|---|
| customer_flag | **excludes** (drop to 0) | **not an exclusion** — the customer's back office is the target |
| graduation (>=4.0) | drops to 0 | n/a |
| suppression | — | front-office risk (`fo_risk_flag`) → 0 |
| warm base | new_faller (20) | install_base (10) |
| send gate | — | `owner_cleared` (AE/CSM sign-off) → `pending_owner` until cleared |
| signals scored | 5 Stars signals | 6 back-office signals |

Encoded additively in `motion_overrides.back_office`; the Stars motion is byte-for-byte unchanged (parity test included).

## What's built (repo side, 0 credits, done)

1. **Signal taxonomy** — 6 back-office signals in `l2_intent_signals.json`, `motions: ["back_office"]`: `bo_cost_mandate` (20/T1), `sla_penalty_backlog` (20/T1), `bo_hiring_cluster` (15/T2), `bpo_transition` (15/T2), `claims_backlog_news` (10/T2, pre-existing), `transaction_volume_surge` (10/T2).
2. **Inverted self-clean** — `motion_overrides.back_office` (customer-inversion, `fo_risk_flag` suppression, `install_base` base term, `owner_cleared` send gate).
3. **Scorer** — `l2_intent_scorer.py` made motion-aware additively (`_motion_selfclean`), plus `--motion / --signals / --stars` CLI so both motions run from one config. New output fields: `at_risk`, `sendable`.
4. **Fixtures** — `data/l2_accounts_backoffice.csv`, `data/l2_signals_backoffice.csv` (6-account demo).
5. **Tests** — suite 37 → 61 checks, all green. Covers inversion, risk suppression, owner gate, base term, both-direction motion filter, per-signal weights, and Stars parity.
6. **Credit plan** — `cadence.back_office` block; both paid steps flagged held.

Runnable now:
```
python3 l2_intent_scorer.py --motion back_office \
  --signals data/l2_signals_backoffice.csv --stars data/l2_accounts_backoffice.csv
```
Demo output — same account, opposite outcome across the two motions:
```
Humana              intent 45  grade_lift      (back office: top target)
Humana              intent  0  excluded        (stars: customer)
UnitedHealth Group  intent  0  suppressed_risk (fo_risk_flag)
Elevance Health     intent 25  pending_owner   (AE/CSM not cleared)
Cigna               intent 10  in_motion       (install-base warm base)
```

## Clay-side turnkey (mirrors the Stars build, Dallas runs in the Clay UI; 0 credits to stand up)

1. New table in the GTM Engine workbook: `Back Office Targets (L2)`, one row per install-base parent. Seed from the Active Customer report (`greenlight-pack/Active_Customers_SF_Jul10.csv`) — these are the front-office customers whose back offices we target. Dedup on `parent_key`.
2. Carry the tag columns from row one: `universe` (=install_base), `fo_risk_flag` (lookup the signal engine risk read), `owner_cleared` (default FALSE until the AE/CSM signs off), plus `persona_key`, `function`, `fte_band` once contacts attach.
3. Stand up an `intent_score_bo` / `intent_status_bo` formula pair reading the six back-office signal columns — same formula shape as the live Stars `intent_score`, with the inverted gate: **do not** zero on `customer_flag`; zero on `fo_risk_flag`; add 10 for `install_base`; mark `pending_owner` when `owner_cleared == FALSE`.
4. Set the table's `active_motion = back_office`. One config, one scorer, two motions.
5. Signal columns (`bo_cost_mandate`, `sla_penalty_backlog`, etc.) are the paid enrichments — build the column definitions now, leave run-conditions OFF until go.

## The one paid step, held: persona pull for the 200

Held until ICP v1 (post-Scott). When cleared:
1. Spec the pull from ICP v1: title strings per `persona_key`, caps per account, dedup keys, `universe = install_base`.
2. Credit-steward pre-check; cheap columns before premium waterfalls; **sample 50, review with Scott + the relevant CSM, then scale.**
3. Every sourced contact carries the full tag set so the 200 is countable from contact one.

Pre-estimate and log to the ledger before any spend. Nothing has been sourced; nothing has been charged.

## Sequence from here

1. Scott ratifies ICP → v1. *(gate)*
2. Spec + sample the persona pull (50), review, scale to 200. *(paid, held)*
3. Contacts land → run through first-draft-engine + copy-sharpener on the pain map → sequences.
4. Wire the closed loop (outcomes writeback) once the sequencer produces events, same as the Stars motion.

Everything above the persona-pull line is done and free. The fork is ready; it waits on the ICP, not on more engineering.
