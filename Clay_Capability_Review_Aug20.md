# Clay Capability Review and Build Plan (Aug 20 2026)

Written while the lemlist PO clears. Scope: what Clay can do for us right now (CLI, MCP, Audiences, workflows, Claygents), what is live in workspace 1180800 today, and where to build next for net-new pipeline. Every fact below was pulled live on Aug 20 2026 (CLI 0.5.0 via plugin 2.6.0, workspace sweep, calendar, email, Slack). Opinions are marked as such.

Related: `Clay_Build_State_Registry.md` (ground truth per asset), `Clay_Golden_Standard.md` (rules), `New_Motion_Build_Runbook.md` (loop), `automation/logs/proposal_ledger.md` (open proposals).

---

## 1. Straight answers on the CLI / MCP question

**Can the CLI or MCP create tables or workbooks for you? No.** Confirmed four ways today:
- `clay tables --help` (CLI 0.5.0): list, get, columns, rows, query, query-live, query-usage, update. No create, no import, no write.
- `clay workbooks --help`: list, get only.
- Plugin 2.6.0 skill `tables-cli`: "The CLI cannot insert rows, update cells, or trigger enrichments." Skill `workflows-vs-tables`: "Users cannot build tables via the CLI/API... table creation only happens in the Clay app."
- Public Tables API (developers.clay.com/tables): Enterprise, read-only query endpoint, no create/import/columns.
- `clay update --check`: latest standalone CLI is 0.8.1; the plugin pins 0.5.0. Nothing in the public docs or changelog says 0.8.x added table creation. Worth re-checking the moment the plugin bumps, but do not plan on it.

**What the CLI can do now that the Jul 17 registry did not know about:**
| Surface | New since Jul 17 | Why it matters |
|---|---|---|
| `clay audiences` | `create` (segment with filter AST), `fields create/update/delete`, `records search-ids/get/search-count`, `list/get/update/archive` | Agent-built "tables" in all but name: a segment is a saved, filterable, live-synced record set that a workflow can run against. |
| `clay workflows runs test --audience-segment <seg> --limit N` | Run a workflow over segment members | Removes the duplicate-table step from the stamp loop for anything that lives in Audiences. |
| `clay workflows triggers create/update/delete` | Webhook and other triggers, read shape first | Lets Clay receive events (lemlist webhooks, SF changes) and fire a workflow. |
| `clay workflows publish`, `snapshots`, `diagram` | Publish drafts, roll back, render Mermaid | Workflow lifecycle without the UI. |
| `clay folders create/update/move` | Workspace folders, move tables/workbooks | Housekeeping at CLI speed. |
| `clay claygents list`, `clay workbooks list/get`, `clay functions get` | Inventory and schema reads | Audits and registry refresh without screenshots. |
| `clay webhooks create/test` | Outbound signed webhooks | Clay can push to our automation layer. |
| `clay routines create <function|workflow>` | Promote a workflow/function to a routine | Reps and MCP can run it by name. |

**Clay MCP (claude.ai connector):** still enrich/query/subroutine only. `query-objects` is blocked by workspace settings per the Aug 20 rundown. No structural write.

**Real-row reads work from the CLI.** `clay tables rows list t_0tic8arWbZp8bSx87Ad --limit 2` returned cells today. The gate-integrity, table-hygiene, credit-strategist and pipeline-receipts agents fail headless because they reference `mcp__plugin_clay_clay__table/read` tools that plugin 2.6.0 does not ship. The fix is a re-point to the CLI, not a new access path (section 4, item 6).

---

## 2. The new lever: Audiences is live and Salesforce-synced

The Jul 17 registry says "Audiences disabled." That is no longer true. Live counts today:

| Entity | Records | Notable fields | Source |
|---|---|---|---|
| People | **140,805** | name, title, email, linkedin_url, seniority, department, Lead Source (e.g. "WebHelp Registration"), Lead Status, Owner ID, Account ID | Salesforce sync |
| Companies | **2,283** | org_name, domain, industry, employee_count, technographics, Salesforce Owner ID, **Account Type (Customer / Prospect)**, Ownership | Salesforce sync (Molina = Customer, for example) |
| Deals | **7,841** | opportunity_name, stage, close_date, amount, is_closed, is_won, opportunity_type | Salesforce sync, `origin_source_type: SALESFORCE` |
| Segments | 1: "Star Ratings Accounts" (`audseg_0timvdny29EfhAJKtHw`), **filter is empty**, so it matches all 2,283 companies. Last touched Aug 20 17:27 UTC. | | |

What this unlocks, in priority order:
1. **Customer exclusion gets a Salesforce input, not a Salesforce source of truth.** Reconciled the same afternoon: 9 of the 101 install-base accounts are Prospect, blank, or absent in the synced SF set (Elevance Health and TD Bank absent; Cigna, Assurant, Farmers, McKesson, Citi, British Gas tagged Prospect). So `Account Type = Customer` under-counts and would have leaked Elevance again on its own. The rule: cold-outbound exclusion = SF (Customer or Partner) segment UNION the install-base table UNION motion denylists, until Sales Ops cleans Account Type. The SF segment still helps: it adds 7 customers the install-base table lacks (BT Group, Comcast, CPS Testing, HealthEquity, Luxottica, PillPack, Wayfair) and 41 Partners.
2. **Install-base and BO-leader lists without a new table.** The Aug 24 Back-Office Marketing meeting asks for "prepared lists" of existing and newly identified BO leaders. Both are segments: customers x BO titles, prospects x BO titles.
3. **Pipeline receipts from deals, not a stale markdown file.** 7,841 deals with stage/amount/won. A zero-credit join of deals to motion account lists gives "opportunity surfaced at a targeted account after first touch" and "realized", kept separate, refreshed by a script.
4. **Webinar and inbound enrichment (Carter's lane).** People with Lead Source like "WebHelp Registration" are already in Audiences. A segment plus a workflow run on it is the enrichment pipeline, no table build.
5. **Stars 5-Touch and Reply workflows can run on a segment** instead of a duplicated L3 table once Stars contacts are pushed to Audiences.

One ordering trap: the CLI help says filter ASTs must copy `key`/`dataPath` from an existing audience rather than guess them, and our only existing audience has an empty filter. So the first filtered segment gets built once in the UI (Account Type = Customer), then every other segment is stamped from that AST by CLI.

---

## 3. What is live today (inventory, Aug 20)

- **Credits:** 71,037.3 (consumed 12,798.7 of ~83,836 ever available, ~15%). Action-execution balance is effectively unlimited. Sourcing via CLI search and MCP list-enrich costs 0 credits (verified Aug 17).
- **Workbooks (8):** Star Ratings, Back Office Motion, Cost-Mandate Motion, WFM-Adjacency Motion, Golden New-Logo Scaffold, Contact Role Test, Contact Role Intelligence, OneOff_ZB_Sweep_Jul29. No folders in use.
- **Tables (43):** the motion L1/L3 pairs, the Stars QBP wave and messaging tables (9), Back Office set (Back Office Contacts - Master List 313 rows = all current customers, Savannah's Existing BO Contacts 214, Back-Office Product Owners, Claims IT, Ops Leaders, COO/SVP), Salesforce import table (137), Full Opp Contact Role List (882), three committee ZB tables (Bell, BMO, TELUS), Contact Intake (134), LI Accounts/Universe, etc.
- **Workflows (9):** Cost-Mandate Send-Readiness, WFM-Adjacency Send-Readiness (proven end-to-end Jul 17), WFM 5-Touch, Stars 5-Touch (last runs Jul 27), Reply Triage + Draft (Jul 18), ACD Detection Validation Test, Stars Post-Approval Apollo Push (Pilot, Jul 27, mixed completed/failed runs), Profile Photo Fetch, Profile URL Repair (Aug 7, the ICP committee site maintenance). None have triggers wired; all are manual/test-run.
- **Claygents (37):** 25 are per-touch clones (Stars MessageGen E1-E5, Stars Voice Audit E1-E5, Voice Fix E1-E5, Stars Figure Critic inline+E2-E5, WFM MessageGen E1-E5 and Voice Audit E1-E5) plus Cost-Mandate and WFM Email1 pairs, Stars LinkedIn Msg, Reply Triage/Draft (Stars, Alpha). Consolidation candidate once lemlist is live, not before.
- **Functions (7 custom):** fn_eligible, fn_persona_key, fn_email_verified (Send-data-back bug still open), fn_tokens_ready, fn_draft_clean, fn_draft_critic, fn_send_ready (documented as shared, not actually called by any live table). Plus the managed functions (Enrich Person, Find Contact Details, Company Domain, etc.).
- **Action catalog (workflow building blocks) includes:** `lemlist-add-lead-to-campaign-v2`, `zoominfo-oauth-enrich-contact/company/search-contacts`, `salesforce-lookup-via-soql/lookup-record/convert-lead`, `slack-send-for-approval-to-channel`, plus Apollo, HubSpot, Outreach, Salesloft, Smartlead, Instantly, Gong packages. No 6sense, no Sales Navigator action.

---

## 4. Where I would build next (ranked for pipeline, tied to the calendar)

Ranking rule: earliest real reply or meeting first, then gate safety, then leverage. Agent = Claude builds it via CLI/MCP. Hands = needs Dallas in the Clay UI.

| # | Build | Serves | Who | Credits | Notes |
|---|---|---|---|---|---|
| 1 | **Segment layer in Audiences** (BUILT 2026-08-20 by CLI, 0 credits; ids in the registry): `Current Customers (SF)` 92, `Prospects (SF)` 1,848, `Cold-Outbound Exclusion (SF: Customer or Partner)` 133, `Account Type Missing (SF hygiene)` 300, `BO Leaders (customers, Dir+)` 337, `BO Leaders (prospects, Dir+)` 1,541, `Webinar Registrants (WebHelp Registration)` 2,831. Open Opps cannot be a saved audience (deals are read-only via records). "Star Ratings Accounts" left untouched (empty filter) pending Dallas's definition. | Every motion's exclusion gate (as one input, see section 2), Aug 24 BO meeting, Carter, gate-integrity | Done | 0 | Next: gate-integrity diffs motion tables against SF segment UNION install-base table. |
| 2 | **Back-Office leaders list pack for Aug 24** (Savannah/Mary Ann/Ellen/Naveen meeting, "Prep: Prepared lists"): two lists from #1 plus the existing 313/214 tables reconciled, delivered as the standard branded HTML page with the why (install-base vs net-new, who to market to vs who BDRs call) | Aug 24 13:30 CT Back-Office Marketing Strategy Alignment | Agent | 0 (list), credits only if we decide to email-waterfall net-new BO contacts | Mandate 3 persona map lives in the backoffice-icp skill. |
| 3 | **6sense burn plan before Aug 28-30**: (a) hand Sierra/Genna the exact SF filters for 6sense data workflows (target accounts x BO and ops titles, Stars Tier A+B parents, open-opp accounts) so the 183K SI credits enrich contacts that land back in Audiences via the SF sync; (b) cut the agency's LinkedIn partner-marketing list (email + name + company + title) straight from Audiences at 0 Clay credits | Aug 24 13:00 CT 6sense touchbase | Agent drafts both; Sierra/Genna run 6sense | 0 | Bulk CSV into 6sense was unclear per Sierra's Aug 5 thread; SF-filtered workflows are the path 6sense already confirmed. |
| 4 | **Carter crossover (Aug 21 10:00 CT)**: agree the carve-up (Carter: inbound/webinar/marketing enrichment and HubSpot-side; Dallas: outbound motions, gates, sending; shared: Audiences field naming, one credit ledger line for marketing, folders). Build him a first workflow: `Webinar Registrant Enrich + Route` on a `Lead Source = WebHelp Registration` segment (enrich, persona_key, Slack/SF route) | Aug 21 Carter meeting, then Aug 25 GTM cadence | Agent builds the workflow; Carter owns it after | low (Enrich Person 0.5/row) | Gives Carter a Clay win he runs himself, matches the self-serve framing. |
| 5 | **Pipeline receipts from Audiences deals** (zero-credit script): join deals to motion account lists, output "surfaced at targeted account after first touch" vs "realized (won)", write candidate rows for `impact/outcomes.csv` with human confirm; feed the Friday readout and the stale `credit_pipeline_receipts.md` | Aug 24 16:00 CT Pipeline Council preview (September wants results), Friday readout | Agent | 0 | Respects attribution ratification still pending with Naveen: candidates, not claims. Closes the `receipts-ledger-refresher` proposal. |
| 6 | **Headless access fix**: re-point gate-integrity, table-hygiene, credit-strategist, pipeline-receipts agents to `clay tables rows list` / `columns get` (verified today) | Restores the daily real-row audits that failed Aug 17-20 | Agent | 0 | Closes `gate-integrity-headless-access-fix` (Aug 18 ledger). |
| 7 | **lemlist landing prep (no regret while the PO clears)**: build `Post-Approval lemlist Push (Pilot)` by CLI mirroring the Apollo pilot with `lemlist-add-lead-to-campaign-v2`; put `slack-send-for-approval-to-channel` inside the workflow as the judgment checkpoint; test in Sandbox Mode at 0 cost; wire a Clay webhook trigger for lemlist reply events | First live wave the week lemlist turns on | Agent builds, Hands connects the lemlist account in Clay | 0 until a real push | Automation-first framing: checkpoint inside the flow, not a wall. |
| 8 | **State Farm + Centene ABM buying-committee test** (Naveen, Aug 18): free sourcing path for ~10 personas each, committee page via `icp-committee-page-builder`, two messaging variants per persona via motion-stamp | Aug 25 GTM engineering cadence | Agent sources and drafts; Dallas calls the wave | 0 to source; ~13/row only if we waterfall emails | Put on the Aug 25 agenda as the next motion after Star Ratings. |
| 9 | **ZoomInfo (Aug 26 11:00 CT)**: Clay already carries ZoomInfo OAuth enrich/search actions, so a ZoomInfo contract becomes a waterfall provider inside Clay workflows (ZI credits, not Clay credits). Ask for OAuth/API access in the seat bundle, SalesNav integration (Nathan's ask), seat count for Nate/Keegan/Jack | Aug 26 ZoomInfo; Naveen's tools list alongside Gong | Dallas | n/a | Position as complementary to Clay, not a replacement. |
| 10 | **Workspace folders**: Motions / Shared Data / One-offs / Archive, move the 8 workbooks and loose tables | Carter, Genna, Jack finding things | Agent | 0 | Reversible. Stage the move list, run on a nod. |
| 11 | **Claygent consolidation** (37 to ~9 stage-parameterized, prompts from motion-stamp's library) | Drift control | Hands | 0 | After lemlist go-live, not before. |
| 12 | **fn_send_ready wiring + fn_email_verified Send-data-back fix** | Cost-Mandate and WFM can resolve | Hands | 0 | Standing items, unchanged. |

Not proposed: anything that adds spend before the first lemlist wave sends. The receipts story needs replies, not more sourcing.

---

## 5. Calendar map (next three weeks, Central time)

| When | Meeting | Clay artifact to bring |
|---|---|---|
| Thu Aug 20 12:30 | ZoomInfo (Connor MacRae) | Questions in #9. |
| Fri Aug 21 10:00 | Dallas/Carter Clay strategy | Carve-up (#4), Audiences walk-through, webinar workflow offer, folders (#10). |
| Mon Aug 24 13:00 | 6sense contact enrichment touchbase | Filter definitions + agency CSV (#3). |
| Mon Aug 24 13:30 | Back-Office Marketing Strategy Alignment | BO leaders list pack (#2), segments (#1). |
| Mon Aug 24 16:00 | Pipeline Council (August preview) | Listen; note what September wants; receipts script (#5) ready by the next one. |
| Tue Aug 25 10:00 | GTM engineering cadence (Naveen, bi-weekly) | Audiences as the new layer, State Farm/Centene ABM (#8), lemlist landing prep (#7). |
| Wed Aug 26 11:00 | ZoomInfo (updated) | #9. |
| Aug 28-30 | 6sense credits expire | #3 must be running by Aug 26. |
| Tue Sep 8 10:00 | GTM engineering cadence | First lemlist wave receipts if the PO lands this week. |

---

## 6. Registry deltas to apply

- Capability boundary row "Table / workbook STRUCTURE": still NO (re-verified Aug 20, CLI 0.5.0 and latest 0.8.1, Tables API read-only).
- New row: **Audiences**: ENABLED and Salesforce-synced (people 140,805 / companies 2,283 / deals 7,841), one segment with an empty filter; CLI can create segments and fields and run workflows on segments.
- New row: **Folders**: CLI create/move available; none in use.
- Workflows: add Stars Post-Approval Apollo Push (Pilot), Stars 5-Touch, WFM 5-Touch, Reply Triage + Draft, ACD Detection Validation Test, Profile Photo Fetch, Profile URL Repair (all exist; none triggered).
- Claygents: 37 live (was 2 tracked).
- Headless real-row read path: `clay tables rows list` works; agent defs must stop referencing `mcp__plugin_clay_clay__*`.
