# Sequencer Prep Runbook (Jul 10 2026)

Goal: Nate opens the campaign and finds real, readable emails already loaded, without anything becoming sendable. Order matters; each step gates the next. Clay mechanics verified against university.clay.com/docs/email-sequencer, Jul 10.

Key safety fact: leads in an UNLAUNCHED campaign cannot send. Loading the sequencer and going live are separate acts, and launch stays off until the walk-through meeting and warmup are done.

## Step 0: chase the flagged customer file (blocker for step 2)

Naveen committed on Jul 8 to sending the Star Ratings file with current customers flagged. As of today there's no record of it landing. Nudge him today; it's the source of truth for the exclusion wire. Per the Jul 8 discipline note, do not build the final exclusion from memory of the call.

## Step 1: purge the 10 pre-gate draft leads

Clay auto-pushed 10 rows into the campaign as draft material when the campaign was created (that's Clay's default `Sync leads to campaign` behavior), before the gate existed. Some are existing-customer parents.

1. Open the campaign → **Leads** tab.
2. Remove all 10. Don't cherry-pick; the resync in step 4 reloads everything that legitimately qualifies.

## Step 2: wire the exclusion (provisional now, final when the file lands)

Provisional wire, safe because it can only over-exclude:

1. On Accounts (Master), add a `customer_exclude` column. Set TRUE for the Jul 8 verbal list: UnitedHealthcare, Humana, CVS/Aetna, Kaiser, Elevance, Molina, Scan Health. Mark the column note "provisional, verbal list Jul 8, reconcile against flagged file."
2. Wire it into the existing `motion_exclude` formula so excluded parents can't reach `send_ready = READY` (free formula work, no credits).
3. Contacts inherit via the existing account lookup; Humana/UHC/CVS contacts fall out of Wave 1 automatically and stay parked for the expansion motion.
4. When Naveen's file lands: replace the provisional flags with the file's, row by row. Anything the file clears that the verbal list excluded comes back into Wave 1.

## Step 3: approval pass (per 07_Approval_SOP.md, Lane 1)

On the Wave-1-eligible set (non-customer parents, `email_final` deliverable, `bdr_claimed` unchecked):

1. Open a filtered view of the wave.
2. Review a ~10% sample plus every edge row (blank merge fields, odd names, out-of-range QBP numbers).
3. Bulk-check `human_approved` on the reviewed selection. `send_ready` recomputes to READY for those rows.

This is approval to LOAD, not to send; the campaign stays unlaunched and the mailbox isn't warm yet. If holding the letter of the Jul 8 "approvals HOLD until the file lands" line matters more than sequencer preview this week, run steps 1 and 2 now and park step 3 until the file arrives. Judgment call; the provisional over-exclusion in step 2 is what makes the early version defensible.

## Step 4: run the resynced sync once

The `Sync leads to campaign` column is already remapped to `email_final` (saved Jul 9, never run). Run condition: `send_ready == "READY" && bdr_claimed != true`.

1. Confirm the campaign's `Lead email address` field points at `email_final` in the campaign **Setup** tab.
2. Run the sync column once on the Contacts table.
3. Verify in the campaign **Leads** tab: row count matches the READY set, no excluded parents present, merge fields render.

## Step 5: what Nate can do the same day

- **Read every email:** campaign → **Leads** tab shows the full rendered message per lead; the pencil icon spot-edits an individual lead's copy. **Preview** toggle in Message sequence renders templates against live source rows.
- **Claim contacts:** `bdr_claimed` checkbox on Contacts (live since Jul 8). Checking it blocks the contact from the campaign and auto-pauses them if already sequenced.
- **Draft 1:1s:** the first-draft-engine → copy-sharpener skill pair, writing from the row and approved claims only.

## Copy standard confirmation

Campaign templates come from Message_Variant_Starter_Pack.md, which passed a v2.2 compliance check Jul 10: variants 1B and 2B rewritten (both named the retired Call Center measure as a movable lever; now CAHPS/complaints/appeals per the v2.2 core position). If any template text was already pasted into the campaign before today, repaste 1B and 2B from the pack before running step 4.

## What stays off

- Campaign **Launch**: off until warmup is green (2 to 3 weeks) and the walk-through meeting happens.
- Back-office variants (Segment 3): gated on the Scott Kemme ICP conversation.
- Any credit-spending enrichment: per-run pre-estimate + explicit go, unchanged.
