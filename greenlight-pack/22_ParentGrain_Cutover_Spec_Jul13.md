# Parent-grain cutover — exact remaining steps (Jul 13 2026)

State: the parent-grain hiring surface is BUILT and CORRECT. Only the live `intent_score` cutover remains. This spec is written so the cutover is executed flawlessly in one clean, focused pass (it edits the LIVE scoring core that both Wave 1 campaigns sit on, so it must not be rushed).

## What is already done (correct, verified)
- **Helper `Parent_Signals_L2_seed`** (t_0ti3etjYeyuQBiTR9r7): 29 parents = 24 eligible + 5 customers tagged `seed_status`.
- **`parent_domain` column added**, populated for the 24 ELIGIBLE parents only (customers blank). This gates the paid enrichments *by construction* (blank domain → enrichment skips the row). This is the fix for the Clay run-condition quirk (typed `{{col}}` run conditions do NOT persist via automation — they need the live `{{` column-picker).
- **`Job Openings` (Company Job Openings, Waterfall) enrichment built on the helper**, Company Domain = `parent_domain`, same 9 quality keywords as Accounts (CAHPS, member experience, Stars, quality improvement, HEDIS, workforce management, RTA, quality analyst, member services). RUN on the 24 eligible (~48cr). Verified values: Centene 28, Devoted 28, Cambia 30, Clover 4, CHPW 6, etc. Customers skipped (blank).
- **Accounts (Master)** (t_0thuumoUcu6wAAhovti) intent layer is UNTOUCHED and still fully working at contract grain (customers excluded/0, eligible in_motion/grade_lift). The existing "Lookup Single Row in Other Table" on Accounts points to CMS_Star_Movement_25v26 (measure_slippage) — do NOT edit it.

## Scope decision
Migrate ONLY the hiring signal to parent grain (high-value, deterministic). Leave the leadership signal ("Use AI result" / "Recent Medicare Quality Leader") at contract grain — the audit says it over-calls and it's a 10pt Tier-2 nudge; not worth ~48cr to replicate at parent grain. So the `intent_score` edit is a SINGLE term change.

## Cutover steps (do in one careful pass)
1. **Add a Lookup on Accounts (Master) → the helper.** Fastest: on Accounts, right-click the existing "Lookup Single Row in Other Table" column → **Duplicate**. Then Edit the duplicate:
   - Table to Search: **Parent_Signals_L2_seed**
   - Target Column: **parent_key**
   - Filter Operator: **Equals**
   - Row Value: Accounts **parent_key**
   - Rename the column **`parent_hiring_lookup`**.
   - Run it (free/internal lookup, 0 credits) → every contract resolves its parent's row.
   - Verify: a Centene contract's lookup shows the helper row with Job Openings = 28; a customer contract (parent humana) → 0 Records / null (fine, customers forced to 0 anyway).
2. **Repoint `intent_score`** (the one live-core edit). Open Accounts `intent_score` (formula column). It currently contains:
   `... + (Number({{Job Openings}}) >= 3 ? 15 : 0))`
   Change ONLY `{{Job Openings}}` in the HIRING term to read the lookup's Job Openings field, e.g. `Number({{parent_hiring_lookup}}?.["Job Openings"]) >= 3 ? 15 : 0` (use the live `{{` picker to insert the reference so it resolves — do not just type it; the picker is required, same quirk as run conditions). Leave every other term unchanged (new_faller, sig_sec_filing, sig_earnings, Use AI result leadership, the customer/graduated kill switch).
   - **TEST immediately** on 2-3 rows: Centene contracts should still show intent_score with the +15 hiring; customers still 0/excluded; a no-hiring eligible parent unchanged. If anything reads 0/errors across the board, **cmd+z / revert the formula** — the contract-grain version keeps working.
3. **Retire the contract-grain hiring** once step 2 verifies: Accounts "Job Openings" column → **Hide** (do not delete; it's referenced history). This stops the expensive 98-row refresh; the 24-row parent surface is now the refresh source (~4x cheaper).
4. **Turn on auto-refresh** on the helper's Job Openings (Clay-native monthly), safe because the surface is eligible-only (customers blank).

## Guardrails
- Do NOT edit the existing Accounts "Lookup Single Row in Other Table" (CMS/measure_slippage).
- Do NOT delete columns; Hide only.
- The `intent_score` edit is the only risky action — single term, test-then-revert.
- Credits: steps 1-4 are ~0 (lookup + formula + hide); the ~48cr hiring run is already spent. Ledger running total ~342 / 5,000 monthly.
