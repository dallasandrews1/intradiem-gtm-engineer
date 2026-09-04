---
name: feedback-checkins-sweep-otter-weekly
description: "Sep 4 2026: any weekly check-in, readout, or recap must be built from a full Otter sweep of that week's calls (otter_search by date range) plus the file record, never the file record alone; Dallas replaces his own 15Five lines with the built ones"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8285eff5-5a56-4d14-ba76-e3d09f30bcb6
  modified: 2026-09-04T15:45:18.015Z
---

Dallas, Sep 4 2026, while building the 15Five backfill: "make sure to check all the transcripts for all my otter calls each week when we're making these so that no context is missed," and "you can replace all the lines I have in there, as mine are nowhere near the level of quality needed here."

**Why:** the file and memory record misses calls that never produced a deliverable (Jul 30 Genna Clay-to-Salesforce sync, Aug 4 Side Quest intro, Aug 4 product-team session, Aug 25 product AI session), and those are exactly the cross-functional touches leadership reads for.

**How to apply:** before writing any week's check-in, readout, or recap, run `otter_search` with `created_after`/`created_before` for the week, read the summaries and action items for every call, and fold them in. Otter had no recordings for Aug 8 to 14 and Aug 17 to 20 in this account, so the memory files stay the source for those days. 15Five backfill page: https://fifteenfive-backfill.pages.dev (deploy folder `~/Desktop/Intradiem Deliverables/deploy-15five-backfill/`). Related: [[jenn-east-exec-elt-knows-players-sep4]], [[feedback-no-failure-talk-leadership]], [[naveen-jul31-call-commitments]].

**Spelling (Sep 4 2026):** Otter transcribes Genna Barrett-Moeller as "Jenna"; it is always Genna. The Jul 30 Clay-to-Salesforce mapping call and the Lemlist-to-Salesforce integration are hers.
