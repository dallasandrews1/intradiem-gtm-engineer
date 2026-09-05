---
name: clay-messagegen-retired-sep5
description: "Sep 5 2026 decision: Clay does not write messaging; MessageGen columns, per-touch Claygents, draft critic columns and Sync Leads are retired (hide now, delete after the Sep 8 recording); copy is Claude-side per contact via first-draft engine + copy sharpener and loaded by the lemlist bridge"
metadata:
  type: project
---

Dallas, Sep 5 2026: having Clay draft copy that Claude already drafts is double work and burns credits per row, so the Clay drafting layer is obsolete and is to be eliminated. Clay keeps research, enrichment and Audiences. The Clay gate Functions and send-ready columns are retired too (Dallas, same night): nothing live calls them; the real gates are Claude-side (exclusion union in build_us_lists.py/push_us_lists.py, denylist re-check in the bridge node, ZeroBounce status from enrichment, the skills' claims gate, Dallas's approval). The July Alpha send-readiness workflows are retired with them. Line: Clay finds, enriches, stores; Claude decides, writes, gates; lemlist sends.

**How to apply:** never run or reference a MessageGen column as the source of copy; never build one into a new motion (motion-stamp step 4 retired); demo and narration show drafting in the Claude layer (act 1 strike plan, act 3 lemlist variables), Clay clip is research only. The removal list and keep/kill rule are in motions/shared/Clay_MessageGen_Retirement_Sep5.md; the Clay deletions are Dallas's hand after the recording, with the table-hygiene agent's safe-delete plan. Related: [[lemlist-variable-generation-is-claude-side]], [[feedback-check-memory-before-describing-pipeline]], [[allhands-demo-v3-narrated-sep4]].
