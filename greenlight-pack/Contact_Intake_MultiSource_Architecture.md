# Contact Intake — Multi-Source Architecture

How new contacts enter the Star Ratings pipeline, regardless of how they were sourced. Written Jul 13 2026, reflects the live Clay build.

## The problem this fixes

The pipeline was built around one sourcing method. The intake layer was named `SalesNav Staging (Persona Pull)` and its columns defaulted to "Sales Navigator export," so any contact that did not come from a Sales Navigator pull had no clean place to land. When contacts were sourced through Clay prospecting instead, there was no lane for them, which invited one-off side tables that broke the "one table feeds the next" model and left people asking why a batch of contacts lived off on its own.

The fix is to make the intake source-agnostic: one on-ramp that every sourcing method feeds, with provenance tracked so the origin of any contact is always visible, and one gated exit into Contacts.

## The pipeline

```
Sales Navigator persona pulls ─┐
                               ├─►  Contact Intake (All Sources)  ──►  Contacts (Buying Committee)  ──►  Stars QBP Wave 1 campaign
Clay prospecting ──────────────┘         (provenance + dedup)          (enrichment + gate + sync)
```

- **Contact Intake (All Sources)** is the single intake table (formerly `SalesNav Staging (Persona Pull)`, renamed Jul 13). Every sourced contact lands here first, no matter the method. It pushes to Contacts through its existing `Send table data` column.
- **Contacts (Buying Committee)** is unchanged. It reads from the intake, applies enrichment, computes `parent_key` and `customer_exclude`, and holds the send gate (`send_ready`, `human_approved`, `critic_email_valid`). It then syncs approved rows to the campaign.
- Nothing downstream of the intake changed. The rename and the new lane are transparent to Contacts and the campaign.

## Provenance: the `sourced_by` seam

`sourced_by` is the column that makes multi-source coherent. Every row carries its origin:

- `salesnav` for Sales Navigator persona pulls
- `clay_prospecting` for contacts found through Clay's Find People plus email waterfall
- `manual` for one-off hand additions

This is how anyone can answer "where did this contact come from" without guessing from the table name. The six Clay-sourced contacts added Jul 13 carry `sourced_by = clay_prospecting` and a Data Source Note of "Clay prospecting (Find People + email waterfall), Jul 13," distinguishing them cleanly from the Sales Nav cohort.

## The two lanes

**Sales Navigator** stays the primary lane for broad persona sweeps. When the job is "pull every Stars/Quality and Finance leader across the target parents," Sales Nav's boolean filtering, account-list targeting, and visual qualification are the right tool. Those pulls land in the persona-pull tables and flow into the intake exactly as they do today.

**Clay prospecting** is the lane for targeted gap-fill and in-pipeline enrichment. When the job is "find the one Stars lead at each of these seven parents," Clay's Find People returns them across all companies in a single call with email waterfall attached. Those results are added to the intake tagged `clay_prospecting`, with `Source Motion = star_ratings` and the persona set, then pushed to Contacts through the same `Send table data` mechanism.

Both lanes converge on the same intake, inherit the same gate in Contacts, and are told apart by `sourced_by`.

## Dedup discipline

Because contacts can now arrive from two doors, a person must not be able to enter twice. The operating rule before adding any batch: check the intake for the same person by `parent_key` plus last name (or LinkedIn URL) and skip anyone already present. The Jul 13 batch was dedup-checked this way — Solis and HMSA already had operations contacts in the intake, but none were the six new Finance and Stars leads, so all six were genuinely net-new. `Promote Gate Status` on the intake remains the promotion control into Contacts.

## Credit routing

Sales Nav pulls are effectively free against the seat. Clay prospecting enrichment burns Clay credits. So the routing that keeps the 5,000 monthly budget pointed at high-leverage work is: Sales Nav for volume sweeps, Clay for surgical gap-fill and enrichment where speed is worth the credits. The Jul 13 gap-fill cost roughly 15 to 20 Clay credits to source and verify six contacts that closed two parents.

## What is live as of Jul 13

- The intake is renamed to `Contact Intake (All Sources)`; Clay updated every downstream reference automatically.
- Six Clay-prospected contacts (Solis and HMSA Finance and Stars, CHPW and ATRIO Stars) were routed through the intake into Contacts using the real pipeline, not a side table. They are rows 138-143 in Contacts, gated (`send_ready = HOLD`, `customer_exclude = FALSE`, `human_approved` unchecked), with `parent_key` auto-resolved and account context populated.
- `sourced_by = clay_prospecting` is set on those six, activating the provenance seam.

The one open step on those six is ZeroBounce validation of their emails; `critic_email_valid` reads FAIL until that runs, and the gate correctly holds them until it does.

## Operating rule going forward

New contacts, whatever the source, are added to `Contact Intake (All Sources)`, tagged with `sourced_by`, dedup-checked, and pushed to Contacts through `Send table data`. No per-batch tables. One intake, provenance-tagged, one gate.
