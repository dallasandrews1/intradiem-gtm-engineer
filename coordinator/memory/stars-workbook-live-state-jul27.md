---
name: stars-workbook-live-state-jul27
description: "Live-confirmed facts about the Star Ratings Motion workbook (wb_0thtlocqNeb46szQtAf) from the Jul 27 cleanup-pass dependency sweep: table ids, what's actually still wired, corrected campaign table names"
metadata:
  type: project
---

From a read-only clay-operator sweep (Jul 27 2026) done to support a table-cleanup/rename pass on the Star Ratings Motion workbook (`wb_0thtlocqNeb46szQtAf`, workspace 1180800). Corrects assumptions made from a canvas screenshot alone — treat these as live-confirmed, higher confidence than the screenshot read.

**Table ids discovered:**
- Accounts (Master) = `t_0thuumoUcu6wAAhovti`
- Contact Intake (All Sources) = `t_0thv091MYjvv9FRbJuN` — this table was renamed from **"SalesNav Staging (Persona Pull)" on Jul 13**; a source field on Contacts still carries the pre-rename label as a fossil.
- Signals - Parent Account (Seed) = `t_0ti3etjYeyuQBiTR9r7`
- Contacts (Buying Committee) = `t_0thtm73HHxyiupTuepK` (per [[contacts-table-finalized-jul9]], 143 rows as of that session)
- Star Ratings 5-Touch Send-Readiness workflow = `wf_0tiegzuo3PzJ4UtUGFA`, 29 nodes

**CMS_Star_Movement_25v26 is NOT dead weight — it's live-wired.** Accounts (Master) field `f_0ti3vw95FqaatfkXFrQ` ("Lookup Single Row in Other Table") points at it, keyed on `contract_id`, feeding `sig_measure_slippage` and a +20 term inside `intent_score`. It just has no visible canvas line because the reference is a Lookup, not a rendered wire. Do not delete; safe to rename only.

**Contact Intake (All Sources) is NOT a redundant/bypassed hop — it's still doing real work.** It has a live `Send table data` action (field `f_0thv1axARarBBsJFs66`) gated on `Promote Gate Status == "ready"`, targeting Contacts (Buying Committee) by name. Manual button trigger, not scheduled. Keep it; no evidence found of a separate `StarRatings_BuyingCommittee_Clay_Import` CSV feeding Contacts directly instead (though that table's id wasn't available to fully rule out).

**Campaign table naming reality (corrects the "every campaign has a paired events table" assumption):** the three "Stars QBP Updated Messaging" campaigns are confirmed by exact name as **"Stars QBP Updated Messaging - Finance"**, **"- Operations"**, and **"- Quality"** (not "Financial"/"Operations" guesses) — and per Contacts's own live config, these campaign tables receive the message copy directly. No separate paired results/events table was found for any of the three; they are NOT structured like the Wave 1/Wave 2 Persona campaigns, which do have separate "events" tables downstream.

**Still unresolved (need Dallas to supply node/table ids from the canvas, no enumeration path exists — see [[clay-tables-cli-observability-gated-jul27]]):**
- The 3-row "Healthcare Quality Leadership" Source node's own id, last-run date, and whether it duplicates one of the 4 "Find people" searches. (Did confirm the 128-row merge table's exact live name via a fossil field label: "Rows from: Healthcare Quality Leadership, Medicare Stars".)
- Whether "News & Fundraising Events" (0 rows) is actually wired/triggered — Signals - Parent Account (Seed) was read in full live and has zero fields referencing news/fundraising, only a Lookup into Accounts (Master) plus a Job Openings waterfall. This leans toward the signal path being dormant/disconnected, but wasn't directly confirmed since the Signal node's own id wasn't available.
- The 4 generic "Find people" Source nodes' actual search criteria (title terms/persona) and which row count (22/18/45/44) maps to which — need their ids to open live.

**How to apply:** [[stars-motion-cleanup-jul27]] cleanup pass should update to reflect CMS_Star_Movement_25v26 and Contact Intake as confirmed-keep (not verify-candidates), correct the two campaign titles, and note the events-table structure differs between the Wave campaigns and the Updated Messaging campaigns.
