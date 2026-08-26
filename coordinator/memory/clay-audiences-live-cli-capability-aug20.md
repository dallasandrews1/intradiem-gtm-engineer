---
name: clay-audiences-live-cli-capability-aug20
description: "Aug 20 2026 live sweep: Clay Audiences is ENABLED and Salesforce-synced (140.8K people / 2.3K companies w/ Account Type / 7.8K deals); CLI still cannot create tables (0.5.0 pinned, 0.8.1 latest) but can create audience segments/fields and run workflows on a segment; real-row reads work via clay tables rows list"
metadata: 
  node_type: memory
  type: project
  originSessionId: 89c2a123-02d8-4510-98d1-b221ec71a34d
  modified: 2026-08-20T18:25:17.224Z
---

Live sweep of workspace 1180800 on 2026-08-20 (plugin 2.6.0 pins CLI 0.5.0; `clay update --check` says 0.8.1 is latest, plugin-managed so it can't self-update):

- **No table/workbook creation from CLI or MCP**, re-confirmed: `clay tables` is read/query only, `clay workbooks` list/get only, plugin skills say table creation is app-only, public Tables API is Enterprise read-only. The Jul 17 registry row stands.
- **Audiences is live and Salesforce-synced** (the Jul 17 registry said "disabled"): people 140,805 (Lead Source/Lead Status/Owner ID/Account ID), companies 2,283 (Account Type = Customer/Prospect, Ownership, SF Owner ID, e.g. Molina = Customer), deals 7,841 (stage, amount, is_won). One segment `Star Ratings Accounts` (audseg_0timvdny29EfhAJKtHw) exists with an EMPTY filter (matches all 2,283 companies).
- CLI can `audiences create` (filter AST), `fields create`, `records search-ids/get/search-count`, and `workflows runs test --audience-segment <seg> --limit N`. Filter AST `key`/`dataPath` must be copied from a UI-made segment; none with a real filter exists yet, so the first filtered segment (Account Type = Customer) is a UI step, then the rest stamp by CLI.
- New CLI surfaces since Jul 17: folders create/move, claygents list, workbooks list/get, workflows triggers/snapshots/publish/diagram, webhooks, routines create.
- `clay tables rows list <tableId> --limit N` returns real cells: this is the headless real-row read path. Agents failing headless (gate-integrity, table-hygiene, credit-strategist, pipeline-receipts) reference `mcp__plugin_clay_clay__table/read` tools the 2.6.0 plugin does not ship.
- Action catalog includes `lemlist-add-lead-to-campaign-v2`, `zoominfo-oauth-enrich-*`, `salesforce-lookup-via-soql`, `slack-send-for-approval-to-channel`; no 6sense or Sales Navigator action.
- Inventory: 8 workbooks, 43 tables, 9 workflows (none triggered), 37 Claygents (25 per-touch clones), 7 custom functions, 71,037.3 credits.

**Why:** Audiences changes the build model: segments are the agent-buildable "table," Salesforce Account Type is the authoritative customer-exclusion source, and deals give zero-credit pipeline receipts.

**How to apply:** plan and build per `Clay_Capability_Review_Aug20.md` (main repo root) and the Aug 20 addendum in `Clay_Build_State_Registry.md`. Before any Audiences-based gate goes live, verify on real rows per [[gate-integrity-fn-send-ready-not-shared]]. Related: [[clay-free-sourcing-path]], [[lemlist-approval-status]].

**Update, same day:** segment layer BUILT by CLI (0 credits): Current Customers (SF) 92 / Prospects 1,848 / Cold-Outbound Exclusion (Customer or Partner) 133 / Account Type Missing 300 / BO Leaders customers Dir+ 337 / BO Leaders prospects Dir+ 1,541 / Webinar Registrants (WebHelp Registration) 2,831. Ids in `Clay_Build_State_Registry.md` (2026-08-20 section). A people filter can reference ACCOUNT fields directly (`entityType: ACCOUNT`); relation/ColOp paths error. Deals can't be a saved audience.

**Correction, same day (important):** SF Account Type is NOT a sufficient customer flag. Reconciled against the 101-row install-base table: Elevance Health and TD Bank are absent from the synced SF companies; Cigna, Assurant, Farmers, McKesson, Citi, British Gas are tagged Prospect. Rule: cold-outbound exclusion = SF (Customer or Partner) segment UNION install-base table UNION motion denylists, never SF alone. Sales Ops (Genna) owns cleaning Account Type; the `Account Type Missing (SF hygiene)` segment (300) is the backlog.

**Aug 20 PM, workflow build by CLI works end-to-end:** `Webinar Registrant Enrich + Route` (`wf_0tk333zvDnGg4YcikFp`) built as a 10-node draft on an audience_segment trigger, validate clean, no publish/runs. Gotchas: `nodes create` returns `nodeId`; outputSchema = shorthand with required `description`, types string/number/boolean/email/url/select only; inputSchema = full form with sourceNodeId/sourcePath pins (no object/array pins); bracket JSONPath for spaced Audiences field names works. `WebHelp Registration` = customer help-portal signups (cvshealth/humana/syf/voya), not marketing; real webinar leads are Lead Source contains "Webinar" (segment `audseg_0tk335bt7YKafui6nbh`, ~1,016).
