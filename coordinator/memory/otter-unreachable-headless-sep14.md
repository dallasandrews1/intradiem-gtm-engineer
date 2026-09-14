---
name: otter-unreachable-headless-sep14
description: Scheduled meeting-capture run Sep 14 2026 found zero Otter MCP tools available headless; job correctly flagged the gap instead of a false all-clear
metadata: 
  node_type: memory
  type: project
  originSessionId: 208a508f-550d-4918-bd75-990adf610efe
  modified: 2026-09-14T12:07:33.859Z
---

On 2026-09-14 the scheduled `meeting-capture` agent ran unattended and found no Otter MCP tools (`mcp__claude_ai_Otter_ai__*`) present in its toolset at all, not an auth error mid-call. It could not search or fetch any transcripts, so it logged "ran, 0 new meetings" with the blocker stated plainly (per its guardrail to never produce a silent/false all-clear) rather than pretending nothing was new. `.meeting-capture-state` was correctly left untouched at `2026-09-10T10:01:10-07:00` so the next successful run re-covers the gap instead of skipping it. The Norton CRO no-record gap (2026-07-16) is still open with no new information.

**Why:** claude.ai-connector MCP servers (Otter, Slack, Gmail, etc.) are interactively authenticated and can be absent in headless/cron/scheduled runs even when they work fine in an interactive session — this is a known class of gap, not unique to Otter (see [[outlook-read-paths-vscode-sep9]] for the same pattern with the M365 connector).

**How to apply:** if a scheduled agent that depends on a claude.ai connector (Otter, Slack, M365, Gmail) comes back with an unexpectedly clean/empty result, check whether the connector tools were even present before trusting the "all clear" — the meeting-capture agent's self-report is the model to copy (state the blocker, leave state files untouched so nothing is silently skipped). If this keeps recurring on the meeting-capture cron specifically, worth flagging to Dallas that scheduled Otter runs may need a different auth path than interactive sessions.
