---
name: naveen-weekly-readout
description: "Friday readout generator for Naveen. Reads engine_state.json, impact.json, the Clay credit ledger, and the week's war-room logs, then drafts the weekly manager readout in two formats: a Slack-length message and a one-page brief. Enforces the operating posture: surfaced vs realized never blended, provisional targets co-shaped never defended, risks flagged early, peer-level tone with zero domain explainers, head-start framing never finished-product framing. Trigger on: Friday readout, weekly readout, update for Naveen, draft my manager update, what do I tell Naveen this week. Run every Friday; load proactively when Friday work begins."
---

## When this skill applies

- Every Friday (the standing cadence)
- Before any 1:1 with Naveen where a status is expected
- After any week milestone worth reporting early (do not sit on wins or risks until Friday)

## Background

Manager visibility is career insurance, and its quality depends on consistency and honesty, not volume. This skill turns the engine's own state files into the readout so the update is a query result, not a memory exercise, and so the honesty architecture (surfaced vs realized) is structurally impossible to violate.

## Inputs (read in this order)

1. `gtm-cohesion-layer/engine_state.json`: funnel counts, gate statuses, approval queue, deliverability
2. `impact/impact.json`: opportunity surfaced vs realized (never blend)
3. `Clay_Credit_Ledger.md`: weekly burn block from clay-credit-steward
4. This week's `Daily_War_Room_*.md` files: signals fired, plays run
5. `outcomes.csv`: any realized rows added this week

If a file is missing or stale, say so in the readout rather than estimating around it.

## Posture rules (hard requirements)

- **Provisional numbers, co-shape framing.** The Q3 targets are Naveen's rough sketch. Progress is reported against "the shape we're converging on," never "my quota." No defensiveness, ever.
- **Surfaced vs realized never blended.** Two columns, always labeled. If the realized column is thin, it stays thin and visible; that honesty IS the credibility.
- **Risks flagged early.** Anything trending toward a gate or tripwire (Day-75 rule: escalate at under ~10 of 15 by Sep 19) appears the week it becomes visible, never at the QBR.
- **Peer-level, no domain explainers.** Naveen defined the role; never explain GTM engineering, Stars mechanics, or Clay basics back to him. What is built, how it maps, the sequence, what I want his read on.
- **Head-start framing, never finished.** Never "done" or "nothing left to build." The continuous engineering is the job.
- **House style:** no em dashes, no AI-isms, no self-narration, no bullet spam. Short and dense.
- **Asks are explicit.** Every readout ends with 0-3 asks, each one decision-shaped ("your read on X," "approve Y," "intro to Z").

## Structure

**Slack version (under 150 words):**
BLUF line → 3-4 leading indicators I own (sends, qualified replies, meetings sourced, signals fired) → realized column status → one risk or gate note → the ask.

**One-page brief (`Readout_[Date].md`):**
1. BLUF (2 sentences: the week in one claim + the one thing that needs his attention)
2. Leading indicators (engine outputs I own), week over week
3. Lagging indicators (realized, from outcomes.csv only)
4. Gate and tripwire status (the four preflight blockers, deliverability, Day-75 distance)
5. Credit stewardship block (from the ledger)
6. Signals and plays of the week (war room highlights, 3 lines max)
7. Next week, committed
8. Risks flagged early
9. Asks (0-3, decision-shaped)

## Workflow

1. Read the inputs. Compute week-over-week deltas from the prior readout file.
2. Draft the one-pager first, compress to the Slack version second (the Slack version is a summary of the brief, never a separate story).
3. Re-check posture rules against the draft, especially co-shape framing and the blend ban.
4. Save both; nothing lives only in chat.
5. **Surface sync (mandatory final step).** After the readout is saved, update the three eyes-only surfaces to match what actually shipped: `GTM_Function_Roadmap.html` (chips, horizons, living-protocol entries; anything slipped gets a reason on the page, never a silent re-date), `Grand_Plan_Master.html` (asset map rows, gates, story bank if a new narrative emerged this week), and `Start_Here_Index.html` (asset map entries and statuses). If the page and the readout log disagree, the log wins. The readout is not complete until the surfaces match it.

## Output

- `Readout_[Date].md` in the project folder
- Slack-ready block in chat for copy-paste
- A one-line delta note appended to a running `Readout_Log.md` (date, headline, ask, response when known) so the quarter's narrative is reconstructable at QBR time
