---
name: bo-lemlist-empty-branches-sep22
description: "Sep 22 2026: BO lemlist campaigns rebuilt to the branch skeleton; Payer/Ins/BPO moved to v2 campaigns because lemlist locks sequences once leads enter; Payer lead copy still owed"
metadata:
  node_type: memory
  type: project
  originSessionId: b37fd0f6-84a0-4d6b-86e3-38bb0786240b
  modified: 2026-09-22T23:38:00.104Z
---

Sep 22 2026. The four BO Expansion campaigns had empty accepted/fallback branches (steps stranded on the root after the condition); Net-New had no branching. Rebuilt from BO_Copy_v2_Sep9.md (Version C) on the Blitz / Stars Finance skeleton. Everything lives in `motions/back_office_expansion/bo_rebuild_sep22/` (spec.py = copy + tree, build.py = REST builder, dry run default, branches.json = every seq id, BO_Rebuild_Copy_Sep22.md = review doc). gtm-copy-reviewer fixes applied.

State: FS (cam_x8ehMHnWSjBr2CLQe) and Net-New (cam_DNErdZPANvC2sqRCK) rebuilt in place, paused. New drafts with root split on lead variable `bo_e1_sent` (TRUE = got Sep 2 Email 1, follow-on path opening "re: <old subject>"): Payer v2 cam_tysjbaAP4vrcCATCJ, Insurance v2 cam_wLsY4xhaBH3tMdgkc (33 leads, tagged), BPO v2 cam_oYTypEKTjbs6TDZrt (24 leads, tagged, unsubscribed Drex Fitzwater removed). Payer lead copy was classifier-denied: 67 leads still in the old Payer campaign, 32 need the tag, 1 bounced. Old Payer/Ins/BPO campaigns are dead; archive after the Payer copy. National Grid opener_line replaced (no wound opener).

lemlist mechanics learned: once any lead enters a campaign, NO sequence in it accepts new steps (pausing doesn't help), so rebuild in a new campaign; never-launched campaigns allow step DELETE and adds. REST calls need a User-Agent header or Cloudflare returns 403/1010. Manual linkedinVoiceNote steps ARE accepted inside a branch (only AI voice is refused). create_campaign_with_sequence reports "running" but the campaign is a draft. Lead variables: POST adds only when the key is new to the campaign; after that use PATCH.

Nathan's number: he had zero call tasks ever and zero dialer calls. Caller numbers are chosen in the dialer by the logged-in user, not on the call step.

Related: [[lemlist-nathan-invite-steps-manual-sep22]], [[nathan-lemlist-phone-backfill-sep22]], [[lemlist-salesforce-sync-overwrites-lead-fixes]]
