---
name: tier1-swarm-agents-built
description: Tier 1 swarm gap agents built Jul 19 — reply-triage, gate-integrity-auditor, pipeline-receipts-tracker; all on-demand read-only subagents in the registry
metadata:
  type: project
---

Built Jul 19 2026 from the swarm gap pass. All three are on-demand subagents (in ~/.claude/agents + coordinator mirror), read-only, registered in [[agent-registry-and-architect]] (AGENT_REGISTRY.md section 2). Need a session restart to be invocable.

- **reply-triage** — classifies an inbound reply and drafts a peer-level reframe in the rep's voice (Nathan default). Registers the built Reply Engine v1 + the intradiem-objection-handler skill as an invocable agent. Drafts, never sends. No input needed; stamped directly.
- **gate-integrity-auditor** — reads REAL rows via Clay MCP `table`/`read` to prove no current customer can reach a cold send and shared Functions still hold (guards the two known leak classes: intent_score customer-leak Jul 12, hardcoded install_base literal; and the customer_exclude text-"TRUE"-vs-boolean trap). Dallas chose LIVE Clay real-row read (not synthetic, not export). Run before any wave. Never edits a gate.
- **pipeline-receipts-tracker** — credits-in vs qualified replies/meetings-out per motion for the renewal case. Dallas chose source = the receipts ledger he maintains (`automation/logs/credit_pipeline_receipts.md`), NOT inbox/CRM inference. Surfaced vs realized never blended. Feeds the Friday readout + rundown.

Built as on-demand (not scheduled) on purpose: the highest-value mode is before-a-wave / before-the-readout, AND the morning-schedule reliability is unresolved (see the wake/sleep correction in the registry). Can be wired scheduled later once the sleep approach is picked. See [[validate-before-handoff]].
