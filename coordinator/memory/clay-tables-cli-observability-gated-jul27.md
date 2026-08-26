---
name: clay-tables-cli-observability-gated-jul27
description: "clay tables list/get/columns/rows CLI all return auth_forbidden on Dallas's workspace (Enterprise-only observability API) — confirmed Jul 27 2026; there is no table-enumeration or workbook-canvas-read path in this Clay setup today"
metadata:
  type: reference
---

Confirmed directly (clay-operator agent, Jul 27 2026): `clay tables list`, `get`, `columns`, `rows` all return `auth_forbidden` — "the public observability API is not enabled for this workspace (available on Enterprise plans)." This is a hard workspace-tier gate, not a flaky auth issue — retrying or re-authing won't fix it.

Also confirmed: the Terracotta MCP `read`/`edit_node`/`validate_workflow` tools only operate on Clay **Workflows** (Alpha), not native table workbooks/canvases — passing a workbook id (e.g. `wb_...`) to `read` returns "Workflow not found." The MCP `table` tool (schema/query modes) DOES work, but only once you already hold a specific table's id — there is no enumeration or canvas-graph-read path to discover table ids from a workbook.

**Net capability today:** to inspect a specific table live, you need its `t_...` id already (from memory, a prior build doc, or Dallas pulling it from the canvas UI). There is no "list every table in this workbook" tool call that works on this workspace.

**Why:** matches the standing gate in [[clay-mcp-audiences-disabled]] (Audiences/observability are Enterprise-tier features gated per-workspace, not admin-togglable) — this is the CLI/Terracotta-side instance of the same wall. Matthew Quan's Jul 24 commitments ([[matthew-quan-clay-cli-outreach-jul24]]: Audiences opening up, table CRUD API in development, personally ungating Dallas early) may resolve this — check outcome of any post-Jul-24 Clay calls before treating this gate as permanent.

**How to apply:** Before asking an agent to "sweep/audit a Clay workbook" for orphaned or redundant tables, either (a) already have every relevant table's id in hand, or (b) expect the sweep to come back partial with a request for Dallas to supply node ids from the canvas UI for the tables it couldn't reach. Don't re-attempt `clay tables list` expecting a different result — check whether the Enterprise gate has lifted first.
