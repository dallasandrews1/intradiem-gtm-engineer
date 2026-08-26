---
name: swarm-workflow-motion-build
description: First Claude Code Workflow (multi-agent swarm) built for the Intradiem GTM Engineer project — automates the motion send-readiness build/test/critique loop
metadata: 
  node_type: memory
  type: project
  originSessionId: 08009f8b-0bbd-468e-99fe-6cc4be094b66
---

Built `.claude/workflows/motion-workflow-build.js` in the Intradiem GTM Engineer repo (2026-07-16) — a multi-agent Workflow script that scopes a new motion from the runbook docs, drafts its MessageGen prompt, builds the Clay Workflow (Alpha) send-readiness logic via the Clay MCP/CLI, and runs an independent critic panel (structure re-check, verified-claims, copy-quality, known-bad-fixture re-verification) before handing Dallas a go/no-go packet. Loops up to 3 rounds if any critic fails. Invoke with `Workflow({name: 'motion-workflow-build', args: {motion: 'WFM-Adjacency'}})` from within that project directory.

**Why:** Dallas asked for a set of reusable subagent swarms to call on for Clay work. Chose this over a portfolio-health-audit swarm or a bulk-message-QA swarm because it's the highest-leverage recurring cost — every remaining motion (WFM-Adjacency, Install-Base, Back Office) repeats this exact build. Clay has no create-table API, so table structure stays manual (golden-scaffold `Duplicate table`, see [[clay-motion-scaffold-sop]]), but the logic layer (Workflow Alpha + MessageGen prompt) is fully agent-buildable and was previously a single unstructured prompt paste (`Motion_Workflow_Build_Prompt_TEMPLATE_v1.md`, proven once on Cost-Mandate as workflow `wf_0tiane7qgXQ6PH9UdBA`).

**How to apply:** When Dallas is about to start a new motion build — after the golden-scaffold table duplication and the runbook's two decisions (universe source, persona key) are resolved — point him to this workflow instead of the manual template paste. It never creates Clay tables, never sends/syncs, never touches the sender webhook, never spends live-wave credits; those stay human-gated per `New_Motion_Build_Runbook.md`. Next candidates he mentioned wanting eventually: a portfolio-health swarm (parallel error-sweep/capacity/credit audit across all active motions) and a bulk message QA swarm — hold off on those until more motions are actually live to audit.
