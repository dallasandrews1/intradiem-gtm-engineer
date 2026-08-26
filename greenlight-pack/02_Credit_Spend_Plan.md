# Clay Credit Spend Plan, Green-Light Sequence
**Prepared:** Jul 8 2026 · **Budget:** 5,000 credits allocated to this motion · **Consumed to date:** 0 (Clay Usage page verified Jul 8)
**Pricing basis:** Clay 2026 credit model, checked against current published rates Jul 8: single-provider email lookup 2-3 credits; multi-provider waterfall 4-8 credits per FOUND row; failed lookups are not charged. Actuals drift by provider mix, so every run below starts with a 10-row calibration sample before the full run. Ledger of record: clay_credit_ledger.csv (append-only).

## Run 1: complete the 22 (5 missing emails)
- **Motion:** star_ratings_cliff_edge · **Table:** Contacts (Buying Committee)
- **Scope:** 5 rows failing the critic (Riddlesworth, Portela, Taliaferro, Wadsworth, plus the Moore domain check)
- **Estimate:** 20-40 credits (5 rows x 4-8 waterfall; misses free)
- **Expected yield:** up to 5 more sequence-ready contacts; committee goes 17 to as many as 22 send-ready pending human approval
- **Budget impact:** under 1%. Recommend GO the moment credits are green-lit; cheapest possible first receipt.

## Run 2: Tier A+B buying-committee expansion
- **Motion:** star_ratings_cliff_edge · **Tables:** Accounts (Master) 98-row + Contacts
- **Scope:** 32 parents to holistic committee depth (8-12 per parent), minus the 22 existing; roughly 230-300 net-new contacts. Sourced per the persona rubric (Director+ only, EXCLUDE rows never sourced), Molina product-line check at step 0.
- **Per-contact estimate:** find-person ~1 credit + waterfall email 4-8 on the ~70% that resolve = ~5 credits average
- **Estimate:** 1,150-1,500 credits full run. **Phase it:** Tier A first (10 parents, ~120 contacts, 500-700 credits), read yield, then Tier B.
- **Expected yield:** full buying committees on every Tier A+B parent; feeds the 15-meetings mandate directly.

## Run 3: back-office persona pull (Mandate 3, 200+ contacts)
- **Motion:** back_office_boo · **Gated on:** ICP confirm with Scott Kemme (spec in 06_BackOffice_ICP_Spec.md)
- **Scope:** 200-250 contacts across claims ops, appeals/UM, payment/document ops, shared services
- **Estimate:** 1,000-1,400 credits at the same ~5/contact average
- **Expected yield:** the 200-contact mandate delivered with attribution tags from day one.

## Budget picture if all three run
| Run | Low | High |
|---|---|---|
| 1. Five emails | 20 | 40 |
| 2. Tier A+B expansion | 1,150 | 1,500 |
| 3. Back-office pull | 1,000 | 1,400 |
| **Total** | **2,170** | **2,940** |

Worst case lands just under the 3,000-credit (60%) flag, which is the built-in mid-burn review point. That is deliberate: all three mandate-critical runs fit inside 60%, leaving 40%+ for signal enrichment, re-verification, and whatever the mid-burn review says earned more. Nothing here spends without a pre-run estimate logged to the ledger and your go.

## Standing order of operations
1. Green light lands. Run 1 same day (40 credits max).
2. Import the 98-row Accounts pack (free), wire Accounts to Contacts (free), THEN Run 2 Tier A phase, so every sourced contact lands pre-scored and attributed.
3. Kemme ICP conversation. Then Run 3.
4. At 3,000 consumed: mid-burn review, yield per motion, kill or scale.
