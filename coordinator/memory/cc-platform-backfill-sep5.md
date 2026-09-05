---
name: cc-platform-backfill-sep5
description: Sep 5 2026 - full Prospect queue tech-stack backfill done (1,763 companies, 1,875 credits); 44% ACD hit rate not the 80% projected, 581 fresh enough to name in copy; DWO overlap 59%
metadata:
  type: project
---

Ran workflow `wf_0tkv9u0BKvNYsV4NsQx` (PredictLeads -> Audiences company) over segment `audseg_0tkv9vq4SZBjZdJuiYi` on Dallas's go. Queue was every SF Account Type = Prospect with no read: 1,810, trimmed to **1,763** after excluding 47 blank-domain rows (Default Intradiem Account, TEST Account41, old Norwegian records). Composition: 344 already on the DWO roster, 16 back-office, 1,391 unworked remainder. aol.com, yahoo.com and intradiem.com sit in SF as Prospect and were read; the Intradiem row is a CRM data bug.

**Results (1,880 companies now carry a read):** 822 with an ACD vendor (44%), 281 WFM, and only **581 with an ACD vendor AND a 2025+ last-seen**, which is the number the 12-month freshness gate allows copy to name. Avaya 225, Genesys 224, Amazon Connect 115, Five9 111, NICE 81, Talkdesk 31, RingCentral 25; WFM Calabrio 155, Aspect 57, Verint 55. DWO-roster companies hit **59%** (214 of 359) versus 44% overall, so DWO wave 2 is where the spend pays back. Output: `tam-outbound-engine/data/cc_platform_reads_full_sep5.csv` (893 rows).

**Cost 1,875 credits** (64,543 -> 62,668), against 1,763 quoted. The 112 overrun was duplicate reads from the first loop version.

**How to apply:** never project a hit rate from a sample of household enterprises (the 9/10 test and 37/46 in-motion run were Centene/Humana/Aetna scale); the broad prospect universe came in at roughly half that. Open item: the workflow fails closed on `ERROR_INVALID_INPUT - This domain is invalid` (node 1 fails, node 3 never stamps read status, row can never leave the queue) - fix the failure path before publishing, because published it reads every new SF Prospect account at ~1 credit each forever. Related: [[clay-backfill-loop-pattern-sep5]], [[feedback-warn-before-large-credit-spend]], [[feedback-audiences-is-not-salesforce-sep5]].
