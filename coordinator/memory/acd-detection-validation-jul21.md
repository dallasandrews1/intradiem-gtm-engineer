---
name: acd-detection-validation-jul21
description: ACD-detection accuracy test result (Jul 21) — Clay/HG Insights detects a company's ACD at only ~50%, too vendor-dependent to back the "match customer story to their ACD" play at scale; usable as a high-confidence Cisco/Five9 signal + research aid only
metadata:
  type: project
---

Ran the ACD-detection validation test Josh asked for on 2026-07-21 (his exact ask: run tech-detection against known customers, measure accuracy % before trusting it). Built Clay workflow **"ACD Detection Validation Test" `wf_0tijlph5krgoogGbHmg`** (domain-find → HG Insights verify → BuyerCaddy verify → match-score), ran it blind against a stratified 39-row set of existing customers whose true ACD is known from Nathan's Jul 10 SF export. Test set: [ACD_Validation_TestSet_v1.csv]; raw grade: ACD_Validation_Results_v1.csv (both in Intradiem GTM Engineer project folder).

**Result:**
- **HG Insights: 17/39 = 44% raw (~50% deduped** for Kaiser sub-entities that collapse to one domain). Per-vendor: Cisco 5/5 (100%), Five9 4/5 (80%), Aspect 1/2, Amazon Connect 2/5, Genesys ~50% deduped, Avaya 2/8 (25%), NICE 0/2. HG returns real product/vendor/category detail and can distinguish products (not just vendor).
- **BuyerCaddy: 0/39.** Returned "not in use" for all 9 candidate products on every row incl. Goldman Sachs, CVS, Home Depot. Either genuinely blind to back-office ACD, or our plain-string product names never matched BuyerCaddy's catalog (only HG's numeric IDs were verified). Unresolved — a 5-min UI catalog check would settle it.
- 44% is a FLOOR: 4 rows had domain-resolution failures caused by vendor tags in the test-set account names (e.g. "Wells Fargo (Five9)" → resolved to cxtoday.com / alvaria.com). 11 rows are "mixed-platform" (HG found a real but different ACD on giants like UHG/Aetna/Home Depot/Kaiser) — big enterprises run 3-4 ACDs, so "which ACD" often isn't one answer.

**VERDICT (the strategic point):** ACD detection is NOT accurate enough to be the backbone of the "match a customer story to their ACD" flagship play that Naveen + Josh got excited about (see [[josh-intro-strategy-call-jul21]]). A confidently-wrong ACD guess in cold copy destroys the exact credibility the social-proof play is meant to earn. Two viable uses instead: (1) a NARROW play — fire the ACD-matched message only when HG detects Cisco or Five9 (80-100% there); (2) an internal research/prioritization column a human verifies before send. Do NOT wire it as blanket automated personalization. Report to Naveen/Josh as: test proved the flagship version needs a better data source before it's safe at scale — a finding that saved the team from building a marquee play on a 50% foundation.

**Credits:** ~486 spent on the full batch (per-row ~12.4cr, higher than the ~310 estimate because BuyerCaddy verifies 9 products/call + HG pulls up to 20). Ledgered under motion ACD-Validation in Clay_Credit_Ledger.md. Optional cleanup not yet done: re-run the 4 broken-domain rows with cleaned names (~30cr) to lock HG's true number; strategic verdict holds either way.
