---
name: bo-presend-verdict-sep4
description: Sep 4 2026 pre-send pass on the five BO campaigns - customer-exclusion gate PASS on all 332 real rows, AM clearance UNVERIFIED on the four customer lanes (Sep 2 moved it to Nate's post-load review, no record it ran), two wrong-company leads, cold-mailbox warmup lands Sep 21-28
metadata:
  type: project
---

Sep 4 2026, logs `automation/logs/lemlist-integrity-2026-09-04.md` and `gate-integrity-2026-09-04.md`. Real rows, all five campaigns paused, every lead in review, nothing sent.

- Customer-exclusion union: PASS. 0 of 132 net-new leads at a customer or partner domain; 200 of 200 customer-lane leads at genuine current customers. No cross-lane duplicates.
- AM clearance: the Sep 2 loader dropped the pre-load clearance filter in favor of Nate reviewing names in lemlist after load. Clearance_Rollup_Sep2.csv still shows cleared = 0 on all 18 accounts and there is no record Nate's review ran. Customer lanes hold until Nate confirms (Mary Ann's rule).
- Defects: Karoline Kane (Barclays mailbox tagged Wells Fargo, FS) removed Sep 4; Joel Davis (Freedom Mortgage mailbox tagged Truist, Net-New) removal handed to Dallas; Steve Hagerman (Truist, Net-New) has parentAccount JPMorgan / motion bo_customer corruption between staging and load, held.
- Sender: all five send from Nate's main intradiem.com mailbox. Cold mailbox nathan.belfield@intradiemhq.com is 3 days old (created Aug 31), domain health 100; the Aug 31 plan holds cold volume until a 3-4 week warmup (about Sep 21-28). Decision open: net-new lane from the main domain now, or wait for the warm mailbox.

DECISION Sep 4 (Dallas): make all fixes; the net-new lane waits for the warm intradiemhq.com mailbox, goal two weeks (earliest Sep 18, Aug 31 plan says Sep 21 to 28), he may not have the luxury of waiting longer. Fixes applied Sep 4: Joel Davis and the mm@fidelity.com record removed (130 leads left), Hagerman fields restored, five DWO-retagged leads and Amrine restored to bo_netnew / in_sequence. Lesson: motion fields are contact-level and shared across campaigns, so any later push can re-stamp a loaded lead.

Verdict Sep 4: Healthcare Payer, Insurance, BPO = GO on data, HOLD for Nate's clearance confirmation. FS = GO on data after the Kane removal, same hold. Net-New = NO-GO until Joel Davis is pulled, Steve Hagerman's fields are fixed, the five staged and one stale rows are resolved, and the sending-mailbox decision is made. See [[motionstatus-not-a-lemlist-gate-sep4]], [[bo-netnew-package-sep2]].
