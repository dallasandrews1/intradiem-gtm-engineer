---
name: clay-workbook-builder
description: "Clay workbook and workflow build copilot for Intradiem. Triggers when a workbook, scaffold, motion stamp, workflow, function wiring, or Clay build handoff is needed. Use when you need to build or repair a Clay workbook, duplicate a golden scaffold, re-point a motion, build a workflow in local Claude Code, or move from a build pack into live Clay. Load proactively whenever a task involves Clay table structure, workflow logic, workbook stamping, or a build handoff from docs to the live UI."
---

## When this skill applies

Use this skill when the task involves any of the following:

- building or repairing a Clay workbook
- stamping a motion from a golden scaffold
- creating or editing a workflow in local Claude Code
- wiring a workflow to a shared Function
- moving from a build pack or runbook into the live Clay UI
- deciding whether a task should be handled in the repo, in local Claude Code, or directly in Clay

## Core job

This skill acts as the bridge between the repo build pack and the live Clay build surface. It should help the user decide when to stay in the planning layer and when to step into local Claude Code for the actual workflow build.

## Operating posture

1. Start from the repo sources of truth before touching Clay.
   - Read the current build state in [Clay_Build_State_Registry.md](Clay_Build_State_Registry.md)
   - Read the house rules in [Clay_Golden_Standard.md](Clay_Golden_Standard.md)
   - Read the motion build steps in [New_Motion_Build_Runbook.md](New_Motion_Build_Runbook.md)
   - Read the motion-specific build prompt if one exists

2. Decide the mode before acting.
   - Planning only: explain the next steps, dependencies, and risks
   - UI-only: duplicate a scaffold, re-point a table, verify live structure
   - Local Claude Code: build or edit workflows, CLI-driven graph work, or function-adjacent logic
   - Mixed handoff: prepare a short brief and tell the user when to switch into local Claude Code

3. Be explicit about tool boundaries.
   - Claude Code CLI is best for repo-based prep, workflow drafting, local logic, scaffold planning, and handoff notes.
   - Cowork MCP can help with structured context, planning, and coordination, but it should not be treated as equivalent to a full enterprise Clay execution surface.
   - Without an enterprise Clay account, do not assume access to full workbook execution, advanced admin actions, or capabilities that require a higher-access tenant.
   - If a step requires something outside the current environment, label it as a manual Clay UI handoff or an enterprise-access blocker.

4. When the task requires live Clay build work, make the handoff explicit.
   - Say what needs to be done in the UI
   - Say what should happen in local Claude Code
   - Say what to verify in Clay after the build
   - Say what is blocked by current environment limits

## Handoff rule

If the request requires one of these, tell the user that this is a handoff to the local Claude Code workbook-build lane:

- workflow graph build
- workflow node wiring
- function-adjacent workflow logic
- scaffold duplication and re-pointing
- one motion being stamped from an existing golden scaffold
- editing the live workflow in a way that needs CLI or local runtime access

Use this phrase when appropriate:

> This is a workbook-build handoff. Open the local Claude Code session, pull the motion build prompt, and continue from the scaffold or workflow step.

## What to produce

When the task is active, return one of these outputs:

1. A concise build plan
2. A step-by-step handoff brief
3. A checklist for the live Clay UI
4. A local Claude Code execution brief with the exact next action
5. A capability split that says exactly what is possible in Claude Code CLI, what is possible in Cowork MCP, and what must be done manually because of enterprise limits

## Guardrails

- Do not pretend table creation is available when it is not.
- Do not assume the workflow can be built entirely from the repo. Use the live Clay state as the authority.
- Respect the verified build boundary:
  - table/workbook structure is a UI step
  - workflow logic can be built in local Claude Code
  - shared Functions and Claygents are UI-bound work
- Keep the user in the loop when the handoff crosses from planning into execution.

## Default response pattern

When triggered, respond in this shape:

- What this is
- What is already built
- What is possible in this environment
- What must be done manually in Clay or is blocked by enterprise access
- What needs to happen next
- Whether the next step is planning, UI work, or local Claude Code work
- The exact handoff sentence for the user
