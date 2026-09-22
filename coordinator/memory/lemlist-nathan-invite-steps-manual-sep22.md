---
name: lemlist-nathan-invite-steps-manual-sep22
description: "Nathan's lemlist LinkedIn invite steps were set manual (\"approve before sending\"), piling 118 invite tasks; switch to automatic half done Sep 22 2026"
metadata:
  node_type: memory
  type: project
  originSessionId: 7fcc8343-d604-4d8d-9244-d83189a75ab4
  modified: 2026-09-22T22:36:53.059Z
---

Sep 22 2026: Nathan's campaigns had the linkedinInvite step set manual (title "LinkedIn connect for {{firstName}}, no note (approve before sending)"), so invites became tasks, not sends. 118 pending invite tasks across 7 campaigns. LinkedIn account connected is Nathan's.

Switched to automatic via connector: BO Expansion - Insurance (cam_HCu4jiFB8oinz2s3F), BO Expansion - BPO (cam_Fy287YF9X5fjPYBSo).
Still manual: Stars - Fresh Pool / Quality (cam_viEbB6HkYsCPtxKbi) and Stars - Resurrection (cam_sh3JCJoxtEHyjGrsw) are RUNNING, so the API refuses edits while they run; cam_N92Tgg29ncHWnYAD9 (BO Healthcare Payer) and cam_2gy9hmEvMjYEuPZ8A were denied by the auto mode classifier. cam_yWefPqaDhNNv4RyQK was already automatic.

**Why:** existing tasks don't convert when a step flips; send_task can't action linkedinInvite, so the backlog clears only in the Tasks UI bulk bar.
**How to apply:** check which of these steps are still manual before debugging LinkedIn sends; the linkedinSend follow-up steps are still manual too (not asked to change). Related: [[stars-recut-staged-sep21]]
