# Attribution Loop — Reply-Sync Agent Spec
**The credit-war keystone.** Turns the static funnel schema into a live instrument. Without this, Week-1 attribution is a claim, not a number.

## What it does
Closes the loop from *reply → classification → `reply_status` → funnel → dashboard*, scoped strictly to engine-sourced records so the credit line is defensible.

## Inputs
- **Salesforce** (or inbox/sequencer): new activity on Contacts/Leads where `gtm_engine_sourced == true`.
- **`engine_state.json`** (current funnel state).
- The ratified definitions (vetted meeting, qualified reply) from the attribution contract.

## Logic (runs daily, or on reply webhook)
1. Pull activity since `funnel.*.last_sync` on engine-sourced contacts only.
2. Match activity → contact by email/id. Ignore any non-engine-sourced record (reps' own adds never inflate the engine number).
3. Classify reply with an AI pass into the dropdown values:
   - `reply` — any human response.
   - `qualified reply` — response indicating interest/fit per ratified rubric (asks a question, requests info, books time, forwards internally). Not OOO/unsubscribe/not-the-right-person.
   - `meeting` — calendar event booked **and confirmed** with a persona-match contact at a target account.
4. **Write `reply_status` back** onto the Clay Contact row (reverse webhook) and onto SF.
5. Recompute `funnel.<motion>` counts from tagged records and write to `engine_state.json`.
6. Recompute `10x` as qualified_replies/week ÷ ratified 1x baseline; flag if deliverability floor breached (number is void if spam/bounce out of bounds).

## Outputs
- Updated `reply_status` on every touched record.
- Updated `engine_state.json` → every dashboard reflects it instantly.
- Weekly attribution digest (Slack/email): replies, qualified replies, meetings sourced this week, by motion, vs. baseline.

## Guardrails / why it survives a credit fight
- **Source-scoped:** only `gtm_engine_sourced == true` rows count toward the engine. Reps keep conversion credit from the reply forward — both true at once.
- **Confirmed, not held:** meetings count only when booked-and-confirmed with a persona match. No vanity.
- **Human override:** any auto-classification can be corrected by Dallas; corrections are logged. AI classifies, human judges.
- **Read-only tags:** `gtm_engine_sourced / source_motion / sourced_date` are never written by this agent — only `reply_status`. The source tag is locked at creation.

## Week-1 dependency (do this before the agent matters)
Get Naveen to ratify, in writing: the engine is credited at the qualified-reply/meeting-*sourced* line; the three SF fields exist; the 1x baseline number. Set `attribution_contract.ratified_in_writing = true` in state. **The agent instruments the contract — it can't substitute for it.**

## Build note
Pre-access this runs on seeded state. On Jul 6, wire input #1 to the real SF/sequencer and the reverse webhook to Clay (§7 of the Clay Build Pack). The dashboard (`attribution_dashboard.html`) already reads `engine_state.json`, so it goes live the moment the agent starts writing.
