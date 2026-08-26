# Execution Brief: Final Customer-Exclusion Wire in Clay (Jul 10 2026)

You are executing a pre-ratified spec in the Clay UI via the Chrome extension. Every decision has already been made. Your job is clicks, pastes, and verification, not judgment. If anything mid-flight requires a judgment call, STOP and ask Dallas; do not improvise on live tables.

## Context (read once, don't re-derive)

- Workspace: Intradiem Clay account, GTM Engine workbook. Tables you will touch: **Accounts (Master)** and **Contacts (Buying Committee)** (137 rows), plus the email campaign's **Leads** tab in Clay's sequencer.
- Source of truth for everything below: `greenlight-pack/12_Customer_Exclude_Final_Jul10.md` (the ratified wire) and `greenlight-pack/10_Sequencer_Prep_Runbook_Jul10.md` (gate order). Read both before starting.
- The active-customer list comes from Nate's Salesforce report (101 accounts): `greenlight-pack/Active_Customers_SF_Jul10.csv`. The file wins over any verbal history. HCSC IS a customer per this file.
- Net effect when done: 26 new-logo-eligible parents (was 27). Excluded set: UnitedHealth Group/UnitedHealthcare, Humana, CVS/Aetna, Elevance, Molina, Kaiser, SCAN, and HCSC. Centene stays IN (confirmed clean).

## Hard guardrails (non-negotiable)

1. **Additive only on Clay tables.** Flag flips, new columns, formula edits. Never delete a row from Accounts or Contacts. The ONLY sanctioned deletion is the campaign Leads purge in Step 1, which is in the sequencer campaign, not a table.
2. **Do not touch, edit, or Regenerate any QBP column** on either table. Regenerating them breaks hand-keyed formula wiring.
3. **Zero credit spend.** Formula columns and formula edits are free. If any action shows a credit estimate or a "this will run enrichment" prompt, STOP, do not confirm, report back.
4. **The sync runs once, and only at Step 6, only after Dallas confirms in this thread that he has completed the approval pass himself.** Never check a `human_approved` box yourself; that judgment is Dallas's per the Approval SOP. Never launch the campaign under any circumstances: launch stays gated on mailbox warmup (2 to 3 weeks) and the Nate walk-through meeting, and a loaded-but-unlaunched campaign cannot send, which is the whole point of stopping there.
5. **Verify UI against reality, not memory.** Clay formulas are written by pasting plain-English text into the AI formula generator. Moving rows between tables is "Send Table Data" under Actions (there is no "Write to Table" column type). If the UI doesn't match what a step describes, STOP and report what you see instead of forcing it.

## Steps, in gate order

### Step 1: purge the pre-gate draft leads
Clay auto-pushed 10 rows into the campaign as drafts when it was created, before any gate existed; some are customer parents. Open the campaign → **Leads** tab → remove ALL of them (don't cherry-pick; a future gated resync reloads everything that legitimately qualifies). Acceptance: Leads tab shows 0 leads.

### Step 2: finalize `customer_exclude` on Accounts (Master)
The column exists with provisional verbal-list flags. Replace its logic with the ratified version. Paste this into the AI formula generator as the plain-English description:

> Return TRUE if parent_org or company domain matches any of: UnitedHealth, UnitedHealthcare, Humana, CVS, Aetna, Kaiser, Elevance, Molina, SCAN Health, Health Care Service Corporation (HCSC). Otherwise FALSE.

Update the column note to: "FINAL Jul 10, wired to Nate's SF Active Customer report (101 accounts)." (A lookup-table version against the CSV is the planned future upgrade; do NOT build it in this session.)

### Step 3: wire it into `motion_exclude`
Edit the existing `motion_exclude` formula on Accounts to add `customer_exclude = TRUE` as an OR condition. Nothing else in that formula changes. Contacts inherit through the existing account lookup, so HCSC's contacts fall out of Wave 1 automatically and park for the expansion lane. No manual row moves needed.

### Step 4: update the sync run condition (save only)
On Contacts, open the `Sync leads to campaign` column (already remapped to `email_final`, saved Jul 9, never run). Set its run condition to:

> Only run if send_ready equals "READY" and bdr_claimed is not true and customer_exclude is not true and Account Forgone QBP is greater than zero.

SAVE. Do not run.

### Step 5: add `persona_key` to Contacts
New formula column. Paste as the plain-English description:

> If Job Title contains Stars, Quality, CAHPS, HEDIS, or Member Experience, return "stars_quality". Else if it contains CFO, Finance, Actuary, Treasurer, or Financial, return "coo_finance". Else if it contains Operations, Contact Center, Customer Service, Member Services, Claims, or COO, return "cc_ops". Otherwise return "stars_quality".

### Step 6 (conditional): load the sequencer, once

Do NOT start this step until Dallas types confirmation in this thread that his approval pass is done (his review of a ~10% sample plus edge rows, then bulk-checking `human_approved`; `send_ready` recomputes to READY for those rows). Then:

1. Preflight the copy: campaign templates come from `Message_Variant_Starter_Pack.md`. If any template was pasted into the campaign before Jul 10, repaste variants 1B and 2B from the pack (they were rewritten Jul 10 for v2.2 compliance; the old versions name a retired measure).
2. In the campaign **Setup** tab, confirm the `Lead email address` field points at `email_final`. If it points anywhere else, STOP and report.
3. Run the `Sync leads to campaign` column ONCE on Contacts.
4. Verify in the campaign **Leads** tab: row count matches the READY set, no excluded parents present (search for HCSC, Humana, UnitedHealth, CVS, Aetna, Kaiser, Elevance, Molina, SCAN by name), merge fields render with no blanks.

Loaded is the end state of this session. Nate can read every rendered email, spot-edit with the pencil icon, and claim contacts via `bdr_claimed` the same day. **Launch stays off.**

## Acceptance checks (run all, report results verbatim)

1. Accounts (Master): count of `customer_exclude = FALSE` among Tier A+B parents is **26**. Centene reads FALSE. HCSC reads TRUE. Report the full TRUE list; expected TRUE count is 6 of the 32 parents — if it isn't 6, do not adjust anything, report the discrepancy.
2. Contacts: HCSC's contacts (expected 4 rows) show excluded from the motion (blocked from `send_ready = READY` via the inherited exclusion). Report the exact count.
3. Contacts: report the count of committee contacts at eligible (non-excluded) parents. Dallas is carrying **121** in the CRO preread as an assumption; this number confirms or corrects it.
4. Contacts: `persona_key` populated on all 137 rows, only the three values present. Report the distribution (cc_ops should be at least 43, the Jul 9 gap-fill cohort).
5. If Step 6 did NOT run: campaign Leads tab shows 0 leads and the sync column's run history shows it was never run. If Step 6 DID run: Leads count equals the READY count on Contacts, zero excluded-parent leads, merge fields render clean, and the campaign status still reads unlaunched.
6. Confirm zero credits were spent this session (ledger/credit counter unchanged).

## Stop-and-ask triggers

Any credit-spend prompt. Any UI that doesn't match a step. Formula preview producing a TRUE/FALSE split that contradicts check 1. A missing column this brief names (`customer_exclude`, `motion_exclude`, `email_final`, `send_ready`, `bdr_claimed`). Anything that would require deleting table rows. When triggered: stop, screenshot, describe, wait.
