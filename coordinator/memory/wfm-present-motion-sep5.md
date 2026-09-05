---
name: wfm-present-motion-sep5
description: "Sep 5 2026: platform-keyed motions load in FULL, no waves (Dallas's call); WFM Present cam_K6dGjBt6WukSo3jvB 362 leads and Genesys Present cam_b7TS4fCDCnt2f8S84 296 leads, both DRAFT, 0 credits; cap 10 per account, customer gate, US only"
metadata: 
  node_type: memory
  type: project
  originSessionId: 32356113-80bc-4c67-becf-7d26485dac27
  modified: 2026-09-05T06:55:51.656Z
---

Built Sep 5 2026 on the PredictLeads platform backfill ([[tech-stack-verified-read-sep5]], [[cc-platform-backfill-sep5]]).

**Dallas's rule (Sep 5, late):** "stop the waves and upload all the contacts into these campaigns, these are very specific motions." Platform-keyed motions load in full. What replaces the wave: US only; person-level dedupe (our index of every campaign plus lemlist's own cross-campaign check); cap 10 per account (VP+ first, then WFM titles, then LinkedIn on file); customer gate on every account (SF exclusion segment audseg_0tk324emMVGAwsna7g4 plus parent-level holds: Optum, Aetna, Assurant, TTEC, Maximus, AT&T U-verse). Held names carry a reason and are the next names per account.

- WFM Present: companies audseg_0tkvnqxJPhevjxbg4hJ (81), people audseg_0tkvnsrRpKkpm2FBk9q (1,822). lemlist cam_K6dGjBt6WukSo3jvB, 33 steps, 362 leads at 54 accounts (39 hand-written, the rest generated from the account read on the same frame, every E1 at or under 110 words). Name still says "Wave 1", rename in the UI. Nate read page live at wfm-present-read.pages.dev.
- Genesys Present: companies audseg_0tkvp4cWjaRzEpkwzCH (111), people audseg_0tkvp3gkKr94ubHuURa (1,932). lemlist cam_b7TS4fCDCnt2f8S84, 34 steps with the ACD as the platform, 296 leads at 52 accounts. Accounts with a WFM read belong to WFM Present, not here.
- Tooling: motions/wfm_present/build_full_load.py (plan, --go load, --reconcile), scratch map_people_to_cos.py (people to account by account-domain filter, 0 credits), build_nate_read_page.py. Ids in each motion's *_Lemlist_Campaign_Sep5.json.
- Customer side: 59 customer accounts with a named platform stay a read for the back-office lane (backoffice-maps.pages.dev/platforms/); no customer contacts loaded, AM-clearance rule stands ([[bo-expansion-council-aug24]]).

**Why:** the platform read makes the platform-keyed story specific enough to run at full width; a 40-lead wave under-used it.

**How to apply:** new platform-keyed motions (Five9, Amazon Connect, NICE next) follow the same planner and rules. Sender and labels are Nate's UI steps; never launch from a session ([[bo-lemlist-shells-built-sep2]]). Lift the cap per account only on Nate's word.
