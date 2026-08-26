---
name: clay-find-people-imports-are-free
description: Clay Find People base-row imports cost 0 credits (only enrichments bill), which means never under-source a people search on cap to save credits
metadata:
  type: reference
---

Verified live Jul 23 2026 (Back Office motion): importing Find People results into a Clay table costs **0 credits**. 226 rows imported across four searches and the balance stayed at exactly 63,203.8, confirmed page-verbatim and re-confirmed independently via `clay credits`. Only ENRICHMENTS bill — company-domain waterfall (~0.8/row, measured 13cr for 15 rows). **MEASURED ALL-IN ENRICH COST: ~4.7 credits per contact, NOT the ~1.2 the per-unit catalog rates imply.** Jul 23 run: 313 contacts enriched (Work Email waterfall + ZeroBounce + LinkedIn/standardized title), estimated 375 credits, ACTUAL spend 1,470.1 (63,203.8 → 61,733.7). The Work Email waterfall appears to bill per PROVIDER ATTEMPT, not per successful hit, which is where the ~4x gap comes from. Budget 4.7/contact for any full enrich stack; extending this motion to the full 101-account install base ≈ 10K credits.

**Consequence: never set a people-search per-company cap low to "save credits."** There is no find cost. Set caps high enough that the search is not saturated, then let dedup cut the pool, and pay enrichment only on the deduped survivors. A saturated cap (rows returned == cap × accounts) means people are being left on the table for no benefit. In the Back Office run, ops_leader saturated at 60/60 (cap 4) and exec_coo at 45/45 (cap 3), so both caps were raised (8 and 6) and re-imported free; bo_product_owner (64) and bo_claims_it (57) came in under their 90 ceilings, meaning supply was already exhausted and raising them would add nothing.

Related Clay mechanics found the same day: table-to-table row moves are a row **Action** ("Send Table Data"), NOT a "Write to Table" enrichment column — searching the enrichment catalog for it comes up empty (see [[verify-tool-capabilities-before-instructing]]). Clay has a native column-level **Dedupe**. Keyboard bulk-fill (copy cell → paste down a column) is unreliable and can paste stray system-clipboard text; use a constant Formula column instead to label every row uniformly. See [[backoffice-live-build-state-jul23]], [[clay-credit-steward]].
