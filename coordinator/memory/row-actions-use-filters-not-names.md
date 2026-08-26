---
name: row-actions-use-filters-not-names
description: "When asking Dallas to act on specific Clay table rows, always give a filter that isolates them plus a bulk action, never \"find these named rows.\""
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 7c09b570-5dad-4007-8754-8157e967649b
  modified: 2026-07-20T05:26:40.131Z
---

Jul 20 2026: When any Clay-table step needs Dallas to act on a specific subset of rows (tag, run a column on a slice, validate, etc.), NEVER instruct him to "type X into these N rows" or hand him a list of names to find manually. He can't tell which rows those are and won't hunt for them.

**Why:** manual row-hunting is friction and error-prone; Clay is built for filter-then-bulk-act.

**How to apply:** give him a precise FILTER expression that isolates exactly the target rows (field conditions, "is any of" lists, status values), then one bulk action on the filtered view (bulk-fill a value, run the column on filtered rows). The filter does the selection. Only ask for manual per-row clicking when the build genuinely can't express it as a filter, and say so explicitly. Prefer a formula or filter over hand-tagging every time.
