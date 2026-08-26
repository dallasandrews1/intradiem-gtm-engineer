---
name: wfm-race-fix-and-new-blockers-jul27
description: WFM Workflow's MessageGen E2-E5 re-parented to mirror Stars's fan-out race fix; structurally validated but two unrelated pre-existing bugs block full end-to-end proof
metadata:
  type: project
---

2026-07-27: re-parented `wf_0tie30io3hiPqSzVRU2` (WFM-Adjacency 5-Touch Send-Readiness) so MessageGen E2-E5 each trigger off the prior touch's terminal "9. Send-ready gate" node instead of the shared "6a. Compose MessageGen E1 inputs" node — mirroring `wf_0tiegzuo3PzJ4UtUGFA` (Stars, fixed Jul 20) node-for-node. `validate_workflow` clean, post-edit graph read confirms a serialized spine with no leftover direct edges from compose to E2-E5. Node 1 (eligibility gate) and the table's `Send Ready` column formula (the separate STOP-THE-LINE leak, see [[gate-integrity-fanout-first-run-jul27]]) were both left untouched as scoped — this was a Workflow-graph edit only, via Clay MCP `edit_node`, no table/trigger/snapshot touched.

**Could not get a full known-good/known-bad run through the actual re-wired chain.** Two separate, pre-existing, out-of-scope bugs block every row (real or synthetic) before it ever reaches MessageGen:

1. **`fn_email_verified` output-schema bug** (node 3, `wfn_0tie38uu3TAUDAq8mi8`) — its output schema never actually populates `status`/`address`, so every row hard-fails at "3g. Email verify gate" regardless of input. Already flagged Jul 18 in [[wfm-workflow-blockers-and-park]], confirmed still live today. Also affects `wf_0tic9xaFeq2rKvMnKuD`.
2. **NEW: `fn_eligible` formula bug** (shared function, table `t_0tial9rYKzWKU2y9MTC`, field `eligible`): formula is `!{{Install Base Lookup BO Universe}} && {{Customer Flag}} != true` — any non-empty string (even literal text `"FALSE"`) is truthy, so a text-typed "FALSE" incorrectly excludes an otherwise-eligible row. Same bug CLASS as the known `customer_exclude` text-vs-boolean trap (see [[wfm-eligibility-gate-defect-jul20]] and the live_example in [[CLAUDE.md]]'s customer_exclude note), but a DIFFERENT function, and shared across motions, not just WFM.

**Net state:** the race-condition fix is structurally sound and matches Stars's shipped pattern exactly (confirmed via live read, not assumed), but is NOT behaviorally proven end-to-end. Dallas's call whether to fix either blocker now (WFM is still on strategic freeze per [[motion-focus-jul20]]) or leave the structural fix unproven until WFM comes off freeze.

Related: [[graph-engineering-audit-jul27]], [[stars-5touch-concurrency-fix-jul20]], [[wfm-workflow-blockers-and-park]], [[wfm-eligibility-gate-defect-jul20]].
