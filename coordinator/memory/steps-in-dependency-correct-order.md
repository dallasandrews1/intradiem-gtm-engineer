---
name: steps-in-dependency-correct-order
description: Always sequence Dallas's steps in dependency-correct order and flag ordering traps so he can't make avoidable mistakes.
metadata:
  type: feedback
---

**Standing preference (Dallas, 2026-07-19):** always give steps in the most effective, dependency-correct ORDER so Dallas can't fall into a trap or make a silly mistake.

**How to apply:**
- Never hand him a step before its prerequisite is done.
- When the clean order needs Claude to go first, or a background job to finish, tell him "do nothing yet / hold" rather than handing a step that would regress or conflict.
- Call out ordering traps explicitly. Real examples from this work: pasting the fn_draft_critic prompt BEFORE Claude wires source_motion into the Records (would make Cost-Mandate/WFM critics give wrong verdicts); editing a workflow node while a smoke-test run of that same workflow is in progress (two-sessions-on-one-asset trap); running a wave before the send gate is fixed.
- Order for safety and correctness first, then completeness.

In both CLAUDE.md working conventions. Complements the click-by-click UI sheet ([[click-by-click-ui-sheet-standard]]) and the in-chat copy-paste-prompt convention.
