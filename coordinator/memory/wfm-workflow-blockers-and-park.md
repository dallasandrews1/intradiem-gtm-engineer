---
name: wfm-workflow-blockers-and-park
description: Smoke test confirmed 2 WFM workflow bugs; strategic call = park WFM, put credits on Stars (the live pipeline motion).
metadata:
  type: project
  date: 2026-07-18
---

Smoke test of the WFM 5-touch (`wf_0tie30io3hiPqSzVRU2`, real Elevance contact via labeled --input, 2026-07-18) FAILED usefully at node 3g and surfaced two bugs:

1. **`fn_email_verified` output schema is broken (confirms the registry's open blocker).** Its `status`/`address` fields are stored as un-interpolated strings `"{{f_0ti58f5i6hTUbNaQudU}}?.status"` instead of real fields; at runtime it returns only `{"Work Email": "..."}`, no `status`. So node `3g. Email verify gate` (reads `$.toolResult.result.status`) HARD-FAILS on EVERY row, deterministically. Breaks BOTH the 5-touch AND the original `wf_0tic9xaFeq2rKvMnKuD` (same gate wiring), likely Cost-Mandate too. Shared Function = UI fix, Dallas's call (fix the outputSchema mapping or repoint the gate). NOTE: Stars is NOT blocked by this (Stars uses its own table Validate Email/ZeroBounce columns, not this workflow function).

2. **Trigger field mapping when run as an L3 column.** Dallas attached the workflow to L3 and got `path "$.customer_flag" resolved to undefined... Available keys: [... "Customer Flag", ... "Install Base Lookup BO Universe"]`. The node input refs use snake_case (`customer_flag`) but a real L3-column run supplies the COLUMN display names ("Customer Flag" etc.). The trigger-fed node bindings must be remapped to the real L3 column names for the column-run path. Agent-buildable (edit_node). (The --input smoke test passed eligibility because --input provided snake_case keys directly; the column path does not.)

**STRATEGIC CALL (Dallas's credit reframe → 2026-07-18):** 72K is a MONTHLY budget, precious; spending it without pipeline is a bad first-90-days look. WFM is a fully-built engine but: 2 plumbing bugs open, universe source NOT bound, no live signal wave. Running it now would burn monthly budget with no near-term pipeline. **So PARK WFM** (fix the plumbing only when it's greenlit to run on a real signal universe). **The pipeline bet is STAR RATINGS**: live campaign, replies landing day 1, a warm referral to Nancy Guzman (Stars & CAHPS Manager) sitting unanswered. Put credits + focus there. Prove Stars converts before spending a budget slice on WFM. This is the [[credit-strategist]]'s verdict applied. See [[star-ratings-upgrade-backlog]], [[credit-budget-correction-jul18]].
