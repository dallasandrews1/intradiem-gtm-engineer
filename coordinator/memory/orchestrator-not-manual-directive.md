---
name: orchestrator-not-manual-directive
description: Dallas's core GTM-Engineering mandate — Claude builds the agent-buildable parts live in Clay; Dallas orchestrates, not manually in things.
metadata:
  type: feedback
---

**Standing directive (Dallas, 2026-07-18):** The dream/end state for his GTM Engineering function is that Dallas ORCHESTRATES after building, not that he sits manually inside tools. So Claude must actually BUILD the agent-buildable parts live in his real Clay account, not just hand him specs to execute.

**Why:** the whole point of the function is leverage. A spec Dallas still has to build by hand is only half the value; the goal is the engine builds itself and Dallas directs it.

**How to apply:**
- Agent-buildable in Clay = **workflows** (CLI `clay workflows create` + `edit_node` + `validate_workflow`; write path CONFIRMED live in workspace 1180800, 2026-07-18) and **enrichment/data ops**. BUILD these live, don't just spec them.
- NOT agent-buildable (always Dallas's UI hands, no API exists): **AI columns, Functions, table structure**. For these, prefer moving the logic INTO a workflow (agent-buildable) rather than a table AI column, so Claude can build it. When something truly must be a Function/AI-column/table edit, hand Dallas the exact paste, but default to the workflow path.
- Safety unchanged: every built workflow ends at HOLD, never a send node, never flip a send gate; for the FIRST build of a new type show the design; don't run two sessions on the same live asset; validate + test one real row before calling it done.
- Sends and Function/AI-column edits stay human. Everything workflow-shaped, Claude builds live.

This reframes the motion factory and every "build sheet" going forward: build sheets are the fallback for UI-only surfaces; the default is Claude builds the workflow. See [[clay-motion-selfserve-path]].
