# UI sheet: land the VodafoneThree ops layer as a standing Clay table

~5 minutes. Table creation is UI-only (no CLI/API path), so this is the one step that needs your hands. Steps verified against Clay University's current CSV-import guide (clay.com/university/guide/csv-import-overview) on Aug 18 2026; if a button label differs, the flow is the thing to trust.

**File to import:** `motions/jack/named_accounts/vodafonethree_ops_layer/VodafoneThree_OpsLayer_v1.1.csv` (106 rows, 23 columns, enrichment already merged so the import itself spends nothing)

## Steps, in order

1. Workspace Home → **+ Create new** → search "**CSV**" and pick the CSV import option.
2. Drag in `VodafoneThree_OpsLayer_v1.1.csv` (or Browse Files to it).
3. Destination: **Create new table**. Name it exactly `VodafoneThree Ops Layer (Jack)` so it sorts beside the other motion tables and the registry can reference it unambiguously.
4. Column mapping screen. Clay pre-suggests from the header row; check these specific mappings and leave the rest as Text:
   - `linkedin_url` → **URL** type (not Text; this is what makes any future enrichment column able to consume it)
   - `work_email` → **Email** type if offered, else Text
   - `mobile_phone` → Text (keep the + prefix intact; don't let it become a number type)
   - `clay_profile_id` → Text (NOT number; leading precision matters and it's an identifier)
5. Row settings: choose **Save and don't run** (label per the current import flow; it's the option that loads data without triggering any auto-run). Nothing in this file needs re-enriching; the credits are already spent and merged.
6. Import. Expect 106 rows.

## After import, two 30-second checks

7. Filter `verify_verdict` = `LEFT_COMPANY` → should be exactly 2 rows (Sam Bantu, Gareth James). They're kept for the record; they must never enter a campaign.
8. Filter `email_flag` contains `SUSPECT` → should be exactly 4 rows (McIlwaine, McGuire, Gary Stewart, Rupert Thomas). Their emails send cleanly but are stale or wrong-entity; mobile or LinkedIn only until manually re-verified.

## What NOT to do in this table

- No enrichment columns on top of it yet; the data's already enriched and every added column is spend. If a re-verify pass is ever needed, that's a new ledger row first.
- Don't blend it into `Contact Intake (All Sources)`; this is a standing motion universe (source once, wave from it), and Jack's lane needs its own table for wave tracking.
- When wave 1 gets picked, add `wave_number` / `wave_status` columns then, per the wave runbook, 30 to 50 rows per slice.
