# Manual Fallback Register (Aug 2 2026)

One system, two data sources. This register records the Aug 2 decision so nobody (including a future session) rebuilds a parallel method.

## The decision

The Daily Action Brief is the ONLY rep-facing delivery method, in both worlds. Lemlist is the system of record and executor while the trial runs and if the purchase is approved (decision expected around trial end, ~Aug 13 2026). If funding is not approved, the SAME brief format, channels, and DONE/SKIP/HOLD loop keep running; only the composer's data source changes. Reps never learn a second system, and the reversion is invisible to them except for losing the automated sends.

## What is ACTIVE

- Lemlist campaigns (Nate: Resurrection cam_sh3JCJoxtEHyjGrsw, Quality cam_viEbB6HkYsCPtxKbi, Finance cam_2gy9hmEvMjYEuPZ8A; Jack: Insurance/FS cam_nwKASgttBM6QT8XGq, Airlines cam_fHGtNHbbj7LmThFgX) as the task queue and send engine.
- Daily Action Brief (spec v2.4) composing from the Lemlist API, plus the relay and brief-thread-ingest loops.
- The copy and playbook docs stay CANONICAL SOURCES in both worlds (they feed Lemlist loads and brief objection handles): StarRatings_Wave1_Persona_Sequences_Jul13.md, motions/star_ratings/Lemlist_Variable_Stage_Jul31.md, motions/uk_airlines/UK_Airlines_Wave1_Variable_Stage_Aug1.md, motions/uk_insurance_fs/UK_Insurance_FS_Motion_Spec_v1.md, motions/shared/Cold_Call_Playbook_Aug2.md. These are NOT parked; only the manual delivery method is.

## What is PARKED (fallback-only, do not run while Lemlist is live)

- The pre-trial manual quarterbacking method: hand-composed daily playbooks / "daily blitz" coordination where Dallas assembles each rep's day by hand from the strike-room sequence docs.
- The strike-room 10-day manual cadence execution sheets as a DELIVERY mechanism (CostMandate_CardinalHealth_StrikeRoom_Sequence v1/v2, StarRatings_BlueShieldCA_StrikeRoom_Sequence_v1, CostMandate_TELUS_StrikeRoom_Sequence_v1, and the Centene reference). Their copy remains reusable source material; their manual send-and-track choreography is superseded.
- Do not delete any of these. They are the contingency and the before-picture that shows what the tool replaces.

## Reversion runbook (only if the Lemlist purchase is NOT approved)

1. Composer source switches from the Lemlist API to staged per-day task lists built from the motion sequence docs (same shape the fixture already proves; the 10-day cadence in each sequence doc defines the day-by-day tasks).
2. Same brief format, same channels, same footer loop; thread-ingest keeps reading DONE/SKIP/HOLD. Autopilot section disappears (no automated sends); calls, voicemails, DMs, voice notes, connects become fully manual tasks in the brief.
3. Sends move back to the rep's own inbox and LinkedIn by hand; the brief carries the full copy per touch (the sequence docs are the source).
4. The relay's Lemlist polling is disabled; reply capture falls back to reps pasting replies into their channel thread (the reply-triage agent still drafts responses).
5. Wave discipline, claims gates, and customer-exclusion gates are unchanged; they never depended on Lemlist.

## Receipts for the funding decision (~Aug 13)

The purchase case is usage receipts from the live trial, packaged by the Friday readout and pipeline-receipts pass, sourced from: relay logs (replies captured, drafts served), brief-thread-ingest logs (DONE/SKIP/HOLD rates), Lemlist campaign stats (sends, opens, replies, tasks completed), and any meetings booked. Every live trial day compounds this case; that is why go-live speed matters more than polish this week.
