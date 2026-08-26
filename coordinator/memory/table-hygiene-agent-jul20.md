---
name: table-hygiene-agent-jul20
description: table-hygiene agent (Jul 20) — daily Clay column-redundancy/rot auditor that flags removals and hands Dallas the safe-delete re-point plan; never deletes
metadata:
  type: project
---

Built Jul 20 2026 on Dallas's request for a daily agent that checks tables for column redundancies and tells him where to re-point connected columns after he deletes.

**What it is:** `table-hygiene` subagent (~/.claude/agents + coordinator mirror) + scheduled job `com.dallasandrews.gtm.tablehygiene` (weekdays 6:50). Read-only. Sweeps a maintained table-ID list, finds REDUNDANT / ORPHANED / ID-ROTTED columns, and for each removal candidate produces the SAFE-DELETE plan: every dependent that references the target column's field ID + the exact re-point target + the order (re-point dependents FIRST, then delete). Writes `automation/logs/table-hygiene-<date>.md`; rundown reads it; never DMs.

**Two hard design realities (built around, not pretended away):**
1. Clay has NO API to delete a column, and destructive actions are Dallas's hand — so the agent FLAGS + PLANS, never deletes. The value is the re-point map that prevents the ID-rot a blind delete causes (the L1 rebuild-from-rot pain).
2. Clay's table-list endpoint is Enterprise-gated (can't enumerate all tables), so it sweeps `automation/config/table_hygiene_targets.md` — a hand-maintained list. Seeded with WFM L3 (t_0tic8arWbZp8bSx87Ad), WFM L1 clean (t_0tict25TSXgTgdJgtZZ), Stars MessageGen (t_0thtm73HHxyiupTuepK), and the rotted-abandoned WFM L1 (t_0tic88ceqvEVhK2B8gn, flagged for full deletion). Dallas adds Stars L1/L2/L3, Contacts, Back Office, Cost-Mandate table IDs (placeholders in the config).

Distinct from gate-integrity-auditor (that checks customer-leak/gate SEMANTICS; this checks schema HEALTH). Wired into the swarm-heartbeat watch list + rundown. Validated (plutil + zsh -n). LOAD PENDING — Dallas runs chmod+cp+load in his own terminal. See [[agent-registry-and-architect]], [[swarm-default-autonomous]], [[wfm-adjacency-and-belfield-continuation]].
