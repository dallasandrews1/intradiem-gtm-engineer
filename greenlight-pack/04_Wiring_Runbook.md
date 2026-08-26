# Accounts-to-Contacts Wiring Runbook (gated step, zero credits)
**Verified against Clay's current docs Jul 8 2026** (university.clay.com/docs/send-table-data and lookup-rows). Two things changed vs our earlier notes: the feature now lives under **Exports → Send table data** (not Actions), and table connections are **linear only, max 20 tables, no loops**. That last constraint dictates the design below.

## Design principle: push people, look up context
Send Table Data pushes rows one direction only. If Accounts pushed to Contacts AND Contacts wrote decision_maker_found back to Accounts, that would be a loop, which Clay does not allow. So:
- **Send Table Data** is reserved for the sourcing flow only (new contacts flowing IN).
- **Lookup Rows** handles everything bidirectional-looking, because it pulls without modifying the source and creates no connection loop.

## Step 0: join key (do this during the 98-row import)
Contacts are keyed by Company Domain (humana.com, uhc.com); Accounts are keyed by contract_id/parent_org. Add a `parent_domain` text column to Accounts (Master) after importing the 98-row pack: humana.com, uhc.com, aetna.com + cvshealth.com, centene.com, medica.com for the live six; fill the rest as parents get sourced. Static text, free, 5 minutes for the active parents.

## Wire 1: decision_maker_found (Accounts pulls from Contacts)
- On Accounts (Master): add **Lookup Multiple Rows in Other Table** targeting Contacts (Buying Committee), match `parent_domain` to Company Domain, condition: critic_email_valid = PASS and Seniority Tier in (A, B).
- Add a formula column: count >= 1 returns "TRUE" else "FALSE", and point the existing decision_maker_found at it (or replace the static column with this formula).
- Effect: fit_star gains its +25 automatically the moment a verified Director+ contact exists; grades recompute live (Humana rows 40 to 65, C to B). This is the demo moment: source a contact, watch the account re-grade itself.

## Wire 2: account context into Contacts (for MessageGen tokens)
- On Contacts: add **Lookup Single Row in Other Table** targeting Accounts (Master), match Company Domain to `parent_domain`, pull addr_2028_musd, addr_2029plus_musd, grade, tier, contract_id (largest by addr_2028 where a parent has several: sort the lookup or use Lookup Multiple + max formula).
- These feed the MessageGen tokens per 03_MessageGen_Deployment_Sheet.md. Non-destructive, no loop.

## Wire 3: sourcing flow (the only Send Table Data)
- The persona pull lands in a staging table (find-people output). From staging: **Exports → Send table data → destination Contacts (Buying Committee) → Send row for each item in a list**.
- Map: name/title/company/domain/LinkedIn plus the attribution trio (GTM Engine Sourced = TRUE, Source Motion, Sourced Date) set as constants on the staging table before sending.
- Settings: Update existing rows on re-run ON (dedupe by contact), Auto-extract new columns OFF (Contacts schema is deliberate; map to existing columns via the destination dropdown so the L5 gate columns are never duplicated).
- New rows arrive with critic_email_valid evaluating immediately and send_ready = HOLD by construction. The gate needs no re-wiring.

## Order of operations on green-light day
1. Import GTM_Engine_Accounts_TierAB_98_Import.csv into Accounts (Master) (formulas recompute automatically; expect 3 B / 85 C / 7 D / 3 Excluded until Wire 1 lands).
2. Add parent_domain (step 0). 3. Wire 1, then Wire 2 (both free). 4. Verify on the existing 22 contacts: Humana/UHC/Centene/CVS/Medica accounts should flip decision_maker_found TRUE and re-grade. 5. Only then any credit-spending sourcing (per 02_Credit_Spend_Plan.md), landing through Wire 3.

## Also noticed during doc verification (flag, not blocker)
Clay_Day1_Build_Order.md specifies the L0 seed as StarRatings_Universe_2026_TimePhased.csv (carries the 5 time-phased columns); the live CMS Star Ratings Import was built from the Canonical file instead (no addr_2028/addr_2029plus at L0). Harmless today because the Accounts layer carries those columns for Tier A+B, but MessageGen lookups for any contact OUTSIDE Tier A+B would find no window dollar. Free fix when convenient: re-import L0 from the TimePhased file or add the five columns to it. Logged here so it does not surprise anyone later.
