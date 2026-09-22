---
name: bo-lemlist-empty-branches-sep22
description: "Sep 22 2026: all four BO Expansion lemlist campaigns have EMPTY accepted/fallback branches with steps stranded on the root after the condition; Net-New has no branching; Nathan has no call number set up in lemlist"
metadata:
  node_type: memory
  type: project
  originSessionId: b37fd0f6-84a0-4d6b-86e3-38bb0786240b
  modified: 2026-09-22T23:13:21.865Z
---

Found Sep 22 2026 when Dallas asked why BO campaigns are so thin and why Nathan's number isn't a caller option on call steps.

**BO structure defect:** BO Expansion Healthcare Payer (cam_N92Tgg29ncHWnYAD9), Financial Services (cam_x8ehMHnWSjBr2CLQe), Insurance (cam_HCu4jiFB8oinz2s3F), BPO (cam_Fy287YF9X5fjPYBSo) are 7 steps each: E1, visit, invite, condition, then DM, E2, one call gated to owner_cleared names. Both condition branches have zero steps; the DM, E2 and call sit on the root after the condition (API build Sep 2, see [[bo-lemlist-shells-built-sep2]]). Net-New (cam_DNErdZPANvC2sqRCK) is 6 steps, no branching. Comparison: Stars, Blitz and DWO campaigns run 20 to 33 steps, 5 sequences, 5 to 8 calls. Insurance activity to Sep 22: 33 E1 sent, 31 visits, 25 invites queued, nothing past the condition.

**Fix route:** fill the two empty branch sequences by API (email, phone, linkedinSend, manual steps are accepted in a child branch; voice notes are not, UI only), add a has-phone sub-branch like the Stars Finance skeleton, and skip_step_for_everyone the stranded root steps (can't delete: leads reviewed). Copy through first-draft engine, sharpener, gtm-copy-reviewer.

**Nathan's number:** lemlist exposes no phone-number API. Caller numbers are per user: a connected personal number must be verified by Nathan under his own login (Settings > Call settings > + Add a number > Connect phone numbers); a purchased number needs Dallas (admin) to add Nathan under "Used by". Call button also needs a phone on the lead.

Related: [[lemlist-nathan-invite-steps-manual-sep22]], [[nathan-lemlist-phone-backfill-sep22]]
