---
name: always-confirm-live-clay
description: "Dallas always wants Clay answers verified against live Clay state, never from docs/memory alone. Never ask whether to sweep."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 60c830b0-538b-4bbe-8a77-65282b3f7d2a
  modified: 2026-07-20T03:28:05.825Z
---

Any question about Clay tables, workbooks, columns, gates, counts, or state must be answered from the LIVE Clay state, not from project docs or memory. Docs/memory are a starting point only.

**Why:** Docs describe the state as of when they were written; Dallas operates on the live workbook and a stale answer can mislead a wave decision. Confirming live is "the entire point."

**How to apply:** When a Clay question comes in, go read the live table/workbook first (Chrome extension get_page_text, Clay MCP, or CLI as available), then answer with page-verbatim state. Never end a Clay answer by asking "want me to confirm against live Clay?" — just do it. This aligns with Gate 2B / BFM-1 (report only page-verbatim state). Related: [[contacts-list-finalized-jul13]].
