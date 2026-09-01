---
name: findings-become-exec-deliverables
description: FEEDBACK (Jul 22) — every substantive finding/result must ship as a real exec deliverable in the John Norton briefing format on the official Intradiem brand, not left in chat
metadata:
  type: feedback
---

Dallas directive, 2026-07-22 (said while heading into a Naveen meeting about the ACD validation result): "you need to be making these deliverables like we made for John." A validated finding delivered only as a chat message is not enough.

**Why:** Dallas is judged on showable artifacts for Naveen and leadership. A finding that lives in chat doesn't travel, can't be forwarded, and doesn't read as the output of a GTM Engineer. The Norton briefing set is the quality bar he's already established.

**How to apply:** After ANY validated finding, test result, or motion milestone, produce a polished exec deliverable, don't stop at the chat summary. Match the John Norton format: self-contained HTML exec summary + one-page engine briefing (the norton-briefing/ files are the template), print-clean so it exports to PDF. Use the OFFICIAL Intradiem brand for anything Naveen/leadership-facing (green-forward, Playfair Display + DM Sans), per the brand two-mode rule, not dallas-brand blurple. Mark internal when it carries customer names/data. Reference living examples: GTM_Engine_for_Naveen_Review.html, StarRatings_CSuite_OnePager.html, norton-briefing/Norton_Exec_Summary.html.

**WHERE deliverables live (the standard, confirmed Jul 22):**
- Editable HTML source + working PDF go in the project folder `Intradiem GTM Engineer/exec-updates/`, dated naming `Topic_Type_YYYY-MM-DD.{html,pdf}` (matches StarRatings_Beta_Update_2026-07-21).
- The FINAL sendable PDF is copied to the Desktop folder **`/Users/IntradiemDA/Desktop/Intradiem Deliverables/`** — this is Dallas's canonical deliverables folder, the new standard. Do NOT leave exec deliverables in the project root.
- ACCESS CAVEAT: the Desktop folder is behind macOS privacy protection (TCC); reaching it from Bash requires `dangerouslyDisableSandbox: true`, a normal listing returns "Operation not permitted."

First application: ACD_Detection_Validation_2026-07-22 (see [[acd-detection-validation-jul21]]). Complements [[exec-deliverables-present-state]] and [[norton-presentation-ownership]].
