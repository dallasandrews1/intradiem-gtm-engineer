---
name: bo-lemlist-shells-built-sep2
description: "Sep 2 2026 five BO lemlist campaign shells built by API (4 customer verticals + net-new), draft/no leads; sender+label are UI steps; step API mechanics learned"
metadata: 
  node_type: memory
  type: project
  originSessionId: b49928c9-4101-489e-9464-72fa64b9d39c
  modified: 2026-09-02T22:55:50.692Z
---

Sep 2 2026: the five back-office lemlist campaign shells from BO_Expansion_Strategy_Aug24
item B7 are BUILT by API, prompted by Nathan Belfield's Aug 31 DM ("whenever the back
office campaign is ready for lemlist, I'll start dumping in the contacts"). Four
existing-customer campaigns by vertical plus one net-new campaign for Nate's six
prospects (kept separate so pipeline-council reporting stays new-logo-clean):
Healthcare Payer cam_N92Tgg29ncHWnYAD9, Financial Services cam_x8ehMHnWSjBr2CLQe,
Insurance cam_HCu4jiFB8oinz2s3F, BPO cam_Fy287YF9X5fjPYBSo, Net-New
cam_DNErdZPANvC2sqRCK. All draft, zero leads, nothing activated. Copy v1 is
mechanism-only (no stats, no peer outcomes, empty claims ledger by design); customer
lanes carry the relationship only via an always-populated {{enterprise_line}} variable
(AM-cleared sentence when brand_safe, neutral vertical line otherwise, never empty or
lemlist holds the lead). Files: BO_Lemlist_Campaign_Copy_Sep2.md,
BO_Lemlist_UISheet_Sep2.md, BO_Lemlist_Campaign_IDs_Sep2.json in
motions/back_office_expansion/.

lemlist API mechanics (verified live): plan upgrade active, /activities returns 200 (the
Aug 14 402 block is gone, supersedes [[lemlist-activities-plan-gate-aug14]]). Campaign
create = POST /api/campaigns (labels param accepted but NOT persisted). Step create =
POST /api/sequences/{sid}/steps (NOT under /campaigns, that path 405s). Call/voicemail
tasks = type "phone" with title+message ("call"/"task" rejected; extra manual/priority
fields on phone/manual cause 400). Step DELETE works while a draft campaign has zero
leads. Senders and labels are UI-only.

Still open: Dallas assigns Nathan as sender + applies gtm-engineering-bo label + sequence
review per the UI sheet; lead load waits on the gated wave process (owner_cleared, both
integrity audits on real rows, warmup green, sign-off). Related:
[[bo-expansion-council-aug24]], [[nate-six-accounts-bo-maps-aug31]].
