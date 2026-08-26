---
name: clay-motion-factory-scaffold-system
description: "\"Stamp, don't rebuild\" system: future motions clone structure from a golden scaffold workbook (Clay's native Duplicate table) and logic from a Clay Workflow template, built on top of the Golden Standard"
metadata:
  node_type: memory
  type: project
  originSessionId: catchup-jul17-2026
---

Because Clay has no create-table API (verified against developer docs, per [[clay-mcp-audiences-disabled]]), hand-building a new motion's L0-L4 tables in Chrome every time was the real time cost. Two-layer fix built mid-July: **structure** (tables/columns) clones via Clay's native "Duplicate table" from a designated golden workbook; **logic** (the send-readiness brain) builds as a Clay Workflow (Alpha) via local Claude Code, using a fill-in-5-blanks template (`Motion_Workflow_Build_Prompt_TEMPLATE_v1.md`).

"Promote to golden scaffold" means: take a hardened, live-verified motion's L1-L3 tables, strip motion-specific values to placeholders, store as `__GOLDEN New-Logo Scaffold`. **Cost-Mandate was chosen as the New-Logo donor over Back Office** — an explicit correction, since Back Office uses an inverted kill switch and its L4 critic wasn't live yet, which would have stamped a wrong exclusion and a missing critic into every future motion. Two golden archetypes exist by design: New-Logo (standard `customer_flag` exclusion, donor = Cost-Mandate) and Install-Base (inverted gate, donor = Back Office, built later).

Clay's native AI copilot **Sculptor** was scoped separately (`Clay_Sculptor_Operating_SOP_v1.md`): it drafts new structure and does read-only analysis, but never authors gates, message copy, or verified-claims logic — "Sculptor drafts and analyzes; your system decides and sends."

**Status Jul 17:** WFM-Adjacency (the first real stamp off this scaffold) had been blocked on a missing `wfm` branch in `fn_persona_key` — that fix landed and was verified live same day (job_title "Director of Workforce Management" now correctly routes `in_icp`). Clone execution is now underway in the live `WFM-Adjacency Motion` workbook (L1 table `t_0tic88ceqvEVhK2B8gn`, L3 table `t_0tic8arWbZp8bSx87Ad`): of Step 1b's five listed re-points, two required table edits (Universe Lookup column Table ID repointed to the workbook's own L1 ID; Source Motion column formula set to literal `wfm_adjacency`), both made same-session — the other three were already satisfied. MessageGen prompt for WFM-Adjacency does exist (`Clay_MessageGen_SystemPrompt_WFMAdjacency_v1.md`). Next: Step 1c, the three AI columns. See [[wfm-adjacency-and-belfield-continuation]], [[clay-functions-build-status]].
