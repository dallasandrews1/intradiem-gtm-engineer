---
name: lemlist-body-format-div-not-p
description: lemlist email bodies must use <div> paragraphs with <div><br></div> spacers; <p> renders bunched in the editor. Fixed across 206 bodies Sep 23 2026.
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2be09a2c-67c6-4445-85c7-dd64d507803c
  modified: 2026-09-24T02:21:03.026Z
---

Every email body written to lemlist (REST PATCH on a step, or the MCP update_sequence_step / set_ab_variant) must be `<div>para</div><div><br></div><div>para</div>`, never `<p>para</p><p>para</p>`. Dallas flagged the whole sequence library as bunched and unprofessional on Sep 23 2026.

**Why:** lemlist's editor and lead preview render `<p>` with no margin, so every paragraph runs into the next. The div-plus-spacer form is what lemlist's own editor writes, and it renders correctly everywhere. The 162 bunched bodies all came from build scripts that emitted `<p>` (BO rebuild, Stars re-cut, bridge fix, E1 opener).

**How to apply:** route every body through `motions/shared/lemlist_body_format.py` (`lemlist_body()` for new copy, `p_to_div()` for a legacy body). Verify by reading the step back, not by trusting the PATCH response: REST sometimes answers "Upgrade your plan to use this feature" and stores the body anyway. REST PATCH edits a running campaign without pausing; the MCP set_ab_variant refuses on a running campaign. One retired variant B on Stars - Resurrection (winner already A) still holds `<p>`. Related: [[bo-lemlist-empty-branches-sep22]], [[stars-recut-staged-sep21]].
