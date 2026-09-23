---
name: pmo-action-extractor-runs
description: Latest PMO action-extractor run status and accuracy trend (register + validation queue for the AI-enabled PMO goal)
metadata: 
  node_type: memory
  type: project
  originSessionId: 2e161116-739c-4c05-a2c7-b8cc8d8f5137
  modified: 2026-09-23T12:34:16.045Z
---

Sep 23 2026 unattended run: 15 new items from 3 sources (otter 13, email 2), 0 from calendar/Monday, 3 carried against earlier ids. All four sources (Otter, Outlook mail, Outlook calendar, Monday.com AI Initiatives board) were reachable. Accuracy to date: 20 graded, 95% precision (1 wrong_date, otherwise clean) — up from the Aug 31 2026 baseline of 20 graded/19 correct that first surfaced the due-date inference rule (see the agent's own changelog in `/Users/dallasandrews/.claude/agents/pmo-action-extractor.md`).

**Why:** this agent is still in its read-only proving phase — the goal (Monday item 12664120782, champion Dallas) needs measured extraction accuracy before any follow-up gets automated. The validation queue (`automation/pmo/validation_queue.csv`) only grows in accuracy signal as Dallas grades more rows.

**How to apply:** when asked about PMO extraction accuracy or whether the goal is ready to move past read-only, check `automation/pmo/validation_queue.csv` graded-row count and precision directly rather than assuming this snapshot is still current — it decays every run. Two open "needs a human" items from this run: an owner attributed via calendar cross-reference (not a verbatim quote) and a vendor support-ticket reply worth confirming is in scope for extraction.
