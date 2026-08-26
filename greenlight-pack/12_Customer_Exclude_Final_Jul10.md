# Customer Exclusion: Final Wire (Jul 10 2026)

Source of truth: Nate Belfield's Salesforce report "Active Customer Account Report" (Jul 10, 101 active customer accounts; filters: Active Customer = True, Type = Customer). Saved here as Active_Customer_Account_Report_Jul10.xlsx + Active_Customers_SF_Jul10.csv. This replaces the provisional verbal-list wire from runbook 10 step 2.

## Reconciliation vs the Jul 8 verbal list

- All seven verbal-list parents CONFIRMED customers on the file: UnitedHealth Group/UnitedHealthcare, Humana, CVS/Aetna (7 entities), Kaiser (10 entities), Elevance, Molina, SCAN. Nothing the provisional wire excluded comes back.
- **ONE CONTRADICTION: Health Care Service Corporation is on the active customer list.** The Jul 8 call had HCSC as confirmed NOT a customer. The file wins per the agreed discipline. HCSC (Tier A, 4 contacts, 1 valid email) moves OUT of the new-logo motion; its contacts join the expansion lane bucket with the other install-base contacts. Flag to Naveen; if his read differs it's a one-flag flip back.
- Centene confirmed clean (not on the file). The must-include stays in.
- No other eligible parent matches. Checked all 26 remaining against all 101 accounts including fuzzy variants; near-misses that are NOT matches: Canadian Imperial Bank ≠ Imperial Health Plan, Baylor Scott & White ≠ Baystate, BCBS North Carolina ≠ Blue Shield of California/CareFirst, Vibrant Emotional Health ≠ VNS.

## Net Wave 1 universe

26 new-logo-eligible parents (was 27). Install-base/excluded set is now: Humana, UHG/UHC, CVS/Aetna, Elevance, Molina, Kaiser, SCAN, **HCSC**.

## Clay wiring (your clicks, paste-ready logic)

Clay formulas are written through the AI formula generator; paste these as the plain-English description.

**1. customer_exclude on Accounts (Master)** (replaces the provisional):
> Return TRUE if parent_org or company domain matches any of: UnitedHealth, UnitedHealthcare, Humana, CVS, Aetna, Kaiser, Elevance, Molina, SCAN Health, Health Care Service Corporation (HCSC). Otherwise FALSE.

Or (cleaner, survives future refreshes): import Active_Customers_SF_Jul10.csv as a small lookup table and set customer_exclude = TRUE when a Lookup Row against it finds a name match on parent_org. Re-export the SF report quarterly and re-import; the wire then updates itself.

**2. motion_exclude:** add `customer_exclude = TRUE` as an OR condition to the existing formula.

**3. Sync condition on the campaign sync column** (load sheet item 3):
> Only run if send_ready equals "READY" and bdr_claimed is not true and customer_exclude is not true and Account Forgone QBP is greater than zero.

**4. persona_key formula column on Contacts** (load sheet item 4, from doc 03 spec):
> If Job Title contains Stars, Quality, CAHPS, HEDIS, or Member Experience, return "stars_quality". Else if it contains CFO, Finance, Actuary, Treasurer, or Financial, return "coo_finance". Else if it contains Operations, Contact Center, Customer Service, Member Services, Claims, or COO, return "cc_ops". Otherwise return "stars_quality".

Campaign 1 sync adds: persona_key equals "stars_quality". Campaign 2 (Finance clone) adds: persona_key equals "coo_finance". cc_ops rows stay out of both until their copy exists.

## What this unlocks

The Jul 8 HOLD condition ("nothing sent, approvals held, until the customer file lands") is now satisfied. Gate order from runbook 10 still applies: purge, wire (this doc), approval pass, sync once. Sends still wait on warmup + launch.

## Bonus intel in the file (for later, not Wave 1)

The report carries ACD Vendor, WFM Vendor, WFM Version, and Features (Contracted vs Deployed) per account. That's a ready-made expansion-motion dataset: contracted-but-not-deployed feature gaps are literally a whitespace list for Mary Ann and Rachel's lane. Parked; worth a pass when the expansion motion spins up.
