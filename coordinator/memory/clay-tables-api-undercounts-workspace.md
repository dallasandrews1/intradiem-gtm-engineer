---
name: clay-tables-api-undercounts-workspace
description: "`clay tables list` returns only 20 tables and silently omits live ones (both WFM-Adjacency tables, 552 rows) - never treat it as the workspace inventory"
metadata: 
  node_type: memory
  type: reference
  originSessionId: a6fa178f-5397-4e80-bd71-df855f3566a2
  modified: 2026-08-07T05:44:53.192Z
---

Verified 2026-08-07. `clay tables list` returns **20 tables** across 5 workbooks (Star Ratings 14, Back Office Motion 2, Cost-Mandate Motion 2, Golden New-Logo Scaffold 2).

**Both WFM-Adjacency tables are live and absent from that list:** L1 `t_0tict25TSXgTgdJgtZZ` (28 rows) and L3 `t_0tic8arWbZp8bSx87Ad` (524 rows). Both respond fine to `clay tables get`, `clay tables columns list`, and `clay tables rows list --filter`. They are just not enumerated.

**How to actually read a table you know the id of:**
```
clay tables get <tableId>                                    # metadata + rowCount
clay tables columns list <tableId>                           # field ids and names
clay tables rows list <tableId> --filter '<fieldId>=<value>' --limit 100 [--cursor <tok>]
```
`rows list` defaults to limit 20, pages via `cursor`, and `--filter` conditions are ANDed. Cells come back as `{status, value, fields}` under `cells`, keyed by field id, not name.

**Why this is load-bearing:** any sweep, audit, or hygiene job that iterates the API inventory will never see those tables, and they are exactly where the open customer-exclusion leak lives ([[wfm-adjacency-customer-leak-open]]). Same failure shape as the ICP-site trap where code iterating a fixed key list never saw a nested branch. Keep a maintained list of table ids rather than trusting the enumeration.
