# Clay workbook execution matrix

Use this whenever a Clay build is moving from planning into execution.

## Purpose

This matrix makes the handoff explicit so the work is split cleanly between:
- Claude Code CLI
- Cowork MCP
- manual Clay UI work
- blocked steps caused by missing enterprise access

## Decision rule

Before acting, classify the task into one of these lanes.

### 1. Claude Code CLI
Use this when the work is primarily:
- repo prep
- workflow drafting
- local logic
- scaffold planning
- handoff notes
- build-order sequencing

### 2. Cowork MCP
Use this when the work is primarily:
- context retrieval
- coordination
- structured planning
- summarizing existing state
- helping move from docs into a next-step brief

Do not treat Cowork MCP as a full enterprise Clay execution surface.

### 3. Manual Clay UI
Use this when the work requires:
- live workbook edits in Clay
- duplicate or re-point a workbook
- workflow node wiring in the Clay UI
- shared Function or Claygent changes
- any action that must happen inside the Clay product itself

### 4. Blocked by current environment
Use this when the task requires:
- enterprise-only Clay access
- higher-access tenant permissions
- features not available in the current account setup

In that case, mark the step as:
- manual follow-up required
- blocked by environment
- requires an enterprise-enabled account

## Recommended response structure

For each build handoff, answer these five questions:

1. What is already known from the repo?
2. What can be done in Claude Code CLI right now?
3. What can be done in Cowork MCP right now?
4. What must be done manually in Clay UI?
5. What is blocked by the current environment?

## Example handoff template

Use this wording:

> This is a workbook-build handoff. Claude Code can prepare the plan and local workflow logic, Cowork MCP can support context and coordination, and the remaining Clay-specific actions are either manual UI steps or blocked by current access limits.

## Practical usage

When a new workbook build starts, do this in order:

1. Read the build state and runbook from the repo.
2. Classify the next action into CLI, MCP, UI, or blocked.
3. Give the user the next action only.
4. Do not overclaim Clay execution capability.

## Guardrails

- Do not assume full Clay execution capability without enterprise access.
- Do not treat MCP as a substitute for the live Clay UI.
- Keep the handoff specific and action-oriented.
- If a step is ambiguous, label it as a manual or blocked follow-up rather than pretending it is complete.
