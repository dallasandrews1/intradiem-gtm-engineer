# Clay Build-State Registry — workspace 1180800

**THIS FILE IS PRESENT-TENSE GROUND TRUTH FOR WHAT ACTUALLY EXISTS IN CLAY.** It is not a plan. Plan docs (clone packs, run sheets, roadmaps, memory notes) describe *intended* state and are written in "once X exists" tense; when a plan doc and this registry disagree about whether something is built, **this registry wins** and work stops until it's reconciled against live Clay.

**Last verified:** 2026-07-17 PM (WFM-Adjacency stamp + workflow build + Step-4 acceptance test session), by direct live sweep of workspace 1180800 (Clay MCP + Clay CLI, local Claude Code, plugin updated to 2.1.16 mid-session). Re-verify at the start of any session that will sequence build steps.

Legend: **BUILT** = exists live now · **PLANNED** = designed in docs, not built · **BLOCKED** = build can't proceed until a dependency clears.

---

## Workbooks / Tables (Home → All files)
| Asset | Status | Owner | Notes |
|---|---|---|---|
| Cost-Mandate Motion | **BUILT** | Dallas | The live new-logo motion table; donor for the New-Logo golden. |
| Back Office Motion | **BUILT** | Dallas | Install-base archetype (inverted gate); donor for the *other* golden later. |
| GTM Engine | **BUILT** | Dallas | Core engine workbook. |
| Web intent | **BUILT** | Dallas | |
| OneOff_CardinalHealth_ZB_Jul15 | **BUILT** | Dallas | One-off. |
| Clay Starter Table | **BUILT** | Nathan Belfield | Starter/sandbox. |
| Maya_DropIn | exists | Naveen | Not part of the motion system. |
| Find and Verify a Job Change | exists | Genna | Shared utility table. |
| `Golden New-Logo Scaffold` (wb_0tib7v5msZ2qYbGc4AC) | **BUILT / NEUTRALIZED** | Dallas | Live-verified + neutralized 2026-07-17 PM. L1=t_0tib7x9pjMe9Givg4Dm (0 rows, no bound universe source); L3=t_0tib7yp7mNKKYX4imrW (50 cols/0 rows, full send-ready pipeline). Universe Lookup→own L1 ✓; Source Motion=`<<motion>>`; MessageGen renamed (CM tag dropped). ⚠️ Clay Duplicate-table BLANKS all 3 AI-column prompts (MessageGen/Draft Audit/Email Voice Audit) — every stamp must re-populate all 3. See `WFM_Adjacency_Clone_Pack_v1_CORRECTION.md`. |
| `__GOLDEN Install-Base Scaffold` | **PLANNED** | — | Does NOT exist. Separate later promotion (donor = Back Office, inverted gate). Feeds Install-Base/BOO. |
| `WFM-Adjacency Motion` (wb_0tic89s5XPjdNKK88He) | **BUILT** | Dallas | Stamped 2026-07-17 PM from the golden. L1=t_0tic88ceqvEVhK2B8gn (0 rows); L3=t_0tic8arWbZp8bSx87Ad (0 rows). Universe Lookup re-pointed to own L1 ✓; Source Motion=`wfm_adjacency` ✓; persona_key wired to fn_persona_key (Run function, inherited from the golden-level fix below) ✓; all 3 AI columns re-populated (MessageGen renamed `(WFM-Adjacency)`, Draft Audit = WFM §4 critic, Email Voice Audit = universal prompt, unchanged/already-correct). Universe source NOT bound (deferred — separate credit-GO for the real technographic wave, per house rule). |

## Functions (all 7 shared — Functions page)
| Function | Status | Notes |
|---|---|---|
| fn_eligible | **BUILT / LIVE** | New-logo kill switch (needs inverted variant for install-base motions). |
| fn_persona_key | **BUILT / LIVE** | `wfm` branch added + **published Jul 17**; returns bo_claims/bo_shared/coo_finance/**wfm**/cc_ops/out_of_icp. Independently re-verified live 2026-07-17 PM via a real workflow test run ("Director of Workforce Management" → `wfm`, correctly routed `in_icp`). Also: the golden L3 table's own `persona_key` COLUMN (separate from this Function) was found live-wired to a stale Cost-Mandate-era inline formula (`cost_ops`/`cost_finance` only, never calling this Function) — fixed 2026-07-17 PM to a proper "Run function" call to `fn_persona_key`; carries forward into every future stamp automatically. |
| fn_email_verified | **BUILT / LIVE, PARTIALLY REPAIRED** | Heaviest credit line (23.1/row); keep gated. ⚠️ **BUG found 2026-07-17 PM (WFM acceptance test), extended debugging through 2026-07-18 AM:** when its entire provider waterfall finds zero candidate emails, the calling workflow node used to hard-crash (`"Validate Work Email (ZeroBounce): Missing input"`). **Confirmed FIXED and stable:** added a run condition `!!{{Work Email}}` to the `Validate Work Email (ZeroBounce)` column so it's skipped (not attempted) when Work Email is blank — this part is solid, verified multiple times, no more hard crash. **Still open, deeper than first assessed:** the `Send data back` action's `Nested Data` mapping (feeds `status`/`address` back to the calling workflow) is visually correct in the UI (verified via screenshot: key=`status`→value=`{{ZeroBounce}}?.status`, key=`address`→value=`{{ZeroBounce}}?.address`, matching the lowercase bindings a concurrent session set on both Cost-Mandate's and WFM's workflows) but a live test still returns a **completely empty** `toolResult.result: {}` — not even `Work Email`, which worked in every prior run. This points to something async/flaky in how `Send data back`'s origin-metadata routing (Table ID/Record ID/Async Callback ID, used to route results back to the specific calling node) delivers results, not a mapping typo. **Also worth noting:** a *second, concurrent Claude session* was independently editing this same shared table and this same workflow (`wf_0tic9xaFeq2rKvMnKuD`) throughout this debugging arc — it added a Voice Audit gate + terminal node to the WFM workflow (nodes `wfn_0tice7wNcH6YBNgVuyx` → `wfn_0tice87gqobctY3Nuz3`) and independently changed both workflows' bindings from `.Status`/`.Address` to lowercase `.status`/`.address`. Two sessions editing the same shared Function concurrently is almost certainly why several fix attempts appeared to revert/garble — **do not have two agent sessions edit this table at once going forward.** Recommendation: dedicated single-session debugging pass on `Send data back`'s delivery mechanism, possibly a Clay support question given the async/origin-routing behavior looks non-deterministic. Not urgent — rows still fail closed (gate-resolution error) either way, nothing sends. |
| fn_tokens_ready | **BUILT / LIVE** | install_base hardcode removed Jul 17. |
| fn_draft_clean | **BUILT / LIVE** | Malformation guard. |
| fn_draft_critic | **BUILT / LIVE** | Safe/fails-closed; structural product_angle gap open (design decision, not urgent). |
| fn_send_ready | **BUILT / LIVE** | Full 6-condition gate. |

## Claygents (Claygents page)
| Claygent | Status | Notes |
|---|---|---|
| Cost-Mandate MessageGen Email1 (v6) | **BUILT** | Single canonical, deduped Jul 17 (3 stale copies deleted). |
| WFM-Adjacency MessageGen Email1 | **BUILT** | Inline agent config on workflow node 6 (not a separate saved Claygent) — §2 prompt pasted 2026-07-17 PM, agentModel claude-sonnet-5. Table-level AI column (`MessageGen Email 1 (WFM-Adjacency)`) also carries the same §2 prompt. |

## Workflows (Alpha) (Workflows page)
| Workflow | Status | Notes |
|---|---|---|
| Cost-Mandate Send-Readiness (Alpha) `wf_0tiane7qgXQ6PH9UdBA` | **BUILT** | 9-node fail-closed graph, ends HOLD, no send node. |
| WFM-Adjacency Send-Readiness (Alpha) `wf_0tic9xaFeq2rKvMnKuD` | **BUILT / PROVEN END-TO-END** | 22-node graph (9 numbered steps + gates/exits + trigger), 21 edges, `validate_workflow` clean. Built via `clay workflows create` + `edit_node`, mirroring the CM blueprint exactly, WFM specifics swapped in (persona rubric unchanged — full 6-key set; §2/§4 WFM prompts; WFM number rule). A real row (Priya Anand/MetLife) ran all 17 steps clean to `send_ready=HOLD` on 2026-07-17 PM. ⚠️ **3 build/test bugs found and fixed along the way:** (1) `edit_node` silently drops explicit input bindings on **tool**-type nodes at CREATE time (not just agent nodes as `CostMandate_Workflow_Node6_Unblock_v1.md` documented) — fixed by re-applying via an UPDATE call post-creation; any future CLI workflow build should re-verify tool-node bindings after creation rather than trusting the create call. (2) Node 6's `persona_key` UI pin-bind pointed at the wrong path (`$.persona_key` instead of `$.toolResult.result.persona_key`) — fixed by Dallas in the UI. (3) Agent nodes require every prompt-referenced `{{token}}` to resolve non-empty — a literal `""` reads as "missing" even when bound correctly; no UI toggle exists to change this (required-ness is auto-derived from prompt-text scanning), so blank fields must be passed as the literal string `"(none)"` (the exact convention the MessageGen prompts already expect). `fn_email_verified`'s crash-on-empty-waterfall bug (see Functions table) remains open. |

---

## What an agent CAN and CANNOT build in Clay (capability boundary — verified 2026-07-17)
| Surface | Agent can build? | Evidence |
|---|---|---|
| **Table / workbook STRUCTURE** (schema, columns, lookups) | ❌ **NO** | No create-table/create-workbook tool on the Cowork Clay MCP (tool surface = enrich/query/subroutine only, confirmed live). No `tables create` on the Clay CLI as of Jul 17. Table structure is a UI-only construct. **Method = Duplicate-table in the UI** (structure, manual, seconds) — this is the supported path, not a workaround. |
| **Workflow logic** (Alpha graph) | ✅ YES | `clay workflows create` via the Clay CLI, run in LOCAL Claude Code (OAuth is local-only; the cloud session can't authenticate). |
| **Functions** | ❌ not by agent | Clay-UI edits only; not CLI/MCP-writable. Paste/edit by hand. |
| **Claygents / AI columns** | ❌ not by agent | Built/edited in the Clay UI. Note the two-field gotcha: NL generator prompt vs the executable formula. |
| **Enrichment / data** (rows, data points) | ✅ YES | Clay MCP (add-company/contact-data-points, find-and-enrich-*, run_subroutine) and the CLI. |

**Bottom line on "can agents create my tables":** No — table/workbook structure is the one thing no surface you have will build for you. Functions and Workflows existing doesn't change that; they're different surfaces. You create the table once by Duplicate-table in the UI, then agents build the workflow on top and enrich the data.

**Not re-verifiable from the cloud:** whether Clay has *just* shipped a CLI `tables create`/`duplicate` — the CLI only authenticates in your local Claude Code. 10-second local check: run `clay --help` / `clay tables --help` (or ask the Clay plugin). If a table-create command now exists, update this row and this registry.

---

## STAMP PROVEN END-TO-END — 2026-07-17 PM
The golden→WFM clone loop is fully proven. `wf_0tic9xaFeq2rKvMnKuD` ran a real row (Priya Anand / MetLife, coo_finance, sourced 34% shrinkage figure) all the way through all 17 steps with zero failures: eligible→true, persona→coo_finance (in_icp), email→valid, H1 gate→number_allowed=true (32-day-old source), tokens_ready→true, MessageGen produced a clean policy-compliant draft (correct attribution, one platform mention, no banned words, connected prose), malformed guard→clean, figure-integrity critic→**PASS**, terminal gate→**`send_ready=HOLD`** (human_approved defaults false). Nothing sent; dry-run law fully intact even on the happy path.
1. ~~Build the golden first~~ — **DONE**.
2. ~~Stamp WFM-Adjacency table (L1/L3, 5 re-points, 3 AI columns)~~ — **DONE** 2026-07-17 PM.
3. ~~Build the WFM workflow via LOCAL Claude Code~~ — **DONE** 2026-07-17 PM (`wf_0tic9xaFeq2rKvMnKuD`), see Workflows table for the tool-node binding bug found + fixed mid-build.
4. ~~Fix node 6's `persona_key` pin-bind~~ — **DONE**, Dallas fixed in UI, confirmed live via test run.
5. ~~Prove the full happy path reaches node 9 with `send_ready=HOLD`~~ — **DONE**, see above.
6. **Fix `fn_email_verified`'s crash-on-empty-waterfall bug** (UI, Function edit, held for Dallas) — still open, not blocking (rows still fail closed via a hard error rather than reaching READY), but affects Cost-Mandate too and should be patched before either motion sources a real wave.
7. **New finding (2026-07-17 PM):** Clay's agent nodes treat any `{{token}}` referenced in the prompt as requiring a **non-empty** resolved value — a literal empty string `""` is treated as "missing," even when correctly bound. The fix is NOT a UI toggle (none exists; all required-ness is auto-derived from prompt-text token scanning) — it's supplying the literal string `"(none)"` as the placeholder for genuinely blank fields, which is exactly the convention the MessageGen prompts already build in ("NORMALIZATION: any field whose value is the literal `(none)` is EMPTY"). Anyone testing/loading rows into this workflow (or Cost-Mandate's) must never pass `""` for an optional field — always `"(none)"`.
8. Final acceptance-test tally across 11 total test rows run: 6 landed clean on their designed gate (EXCLUDED, HOLD_persona, HOLD_no_email x4); 2 crashed on the fn_email_verified bug (item 6); 1 confirmed the persona_key bind bug (item 4, since fixed); 1 (re-run after both fixes) reached node 9 cleanly with `send_ready=HOLD` — no row ever reached READY across any of the 11 runs.
9. Real signal-first universe wave stays HELD — separate credit-GO, not sourced.

---

## ADDENDUM 2026-08-20 (live CLI sweep, CLI 0.5.0 via plugin 2.6.0; latest standalone 0.8.1)

Full write-up: `Clay_Capability_Review_Aug20.md`. Deltas to the tables above:

| Surface | Status Aug 20 | Evidence |
|---|---|---|
| Table / workbook STRUCTURE | still ❌ agent cannot build | `clay tables --help` has no create/import/write; `clay workbooks` is list/get only; plugin skill `workflows-vs-tables` says table creation is app-only; public Tables API is Enterprise read-only. |
| **Audiences** | **ENABLED, Salesforce-synced** (was "disabled" above) | people 140,805 / companies 2,283 (Account Type Customer/Prospect, Ownership, SF Owner ID) / deals 7,841 (stage, amount, is_won). One segment `Star Ratings Accounts` (audseg_0timvdny29EfhAJKtHw) with an EMPTY filter (matches all companies). CLI: `audiences create/update/archive`, `fields create/update/delete`, `records search-ids/get/search-count`; `workflows runs test --audience-segment`. Filter AST keys must be copied from a UI-made segment (none with a real filter exists yet). |
| Folders | CLI `folders create/update/move` available; none in use | `clay folders list` shows 8 workbooks at Home. |
| Workflows | 9 exist, none triggered | Cost-Mandate SR, WFM SR, WFM 5-Touch, Stars 5-Touch (last runs Jul 27), Reply Triage + Draft, ACD Detection Validation Test, Stars Post-Approval Apollo Push (Pilot, Jul 27, mixed completed/failed), Profile Photo Fetch, Profile URL Repair (Aug 7). |
| Claygents | 37 live | 25 are per-touch clones (Stars/WFM MessageGen, Voice Audit, Voice Fix, Figure Critic E1-E5); consolidation candidate after lemlist go-live. |
| Action catalog | includes `lemlist-add-lead-to-campaign-v2`, `zoominfo-oauth-enrich-*`, `salesforce-lookup-via-soql`, `slack-send-for-approval-to-channel` | `clay workflows actions list` (1.4 MB JSON). No 6sense or Sales Navigator action. |
| Headless real-row read | `clay tables rows list <tableId> --limit N` WORKS | Agents failing headless reference `mcp__plugin_clay_clay__table/read`, which plugin 2.6.0 does not ship; re-point to the CLI. |

### Audiences segments built 2026-08-20 (CLI, 0 credits, all counts verified by id after create)
| Segment | Entity | Id | Count | Filter |
|---|---|---|---|---|
| Current Customers (SF) | companies | audseg_0tk31v7TVNZnw5yRnVf | 92 | Account Type = Customer (Dallas created in UI; filter applied by CLI) |
| Prospects (SF) | companies | audseg_0tk324eHi3gbzqoJ6jz | 1,848 | Account Type = Prospect |
| Cold-Outbound Exclusion (SF: Customer or Partner) | companies | audseg_0tk324emMVGAwsna7g4 | 133 | Account Type in (Customer, Partner). THE gate source. |
| Account Type Missing (SF hygiene) | companies | audseg_0tk324f5Wc4os4wjZm8 | 300 | Account Type empty. Leak risk for any not-Customer gate. |
| BO Leaders (customers, Dir+) | people | audseg_0tk324gWiTQKCqVz4tx | 337 | account Account Type = Customer AND title contains a BO function term AND Dir+ seniority term AND not IT/eng. Straw-man ICP v0. |
| BO Leaders (prospects, Dir+) | people | audseg_0tk324ghMPTbzvR8pGK | 1,541 | same, Account Type = Prospect |
| Webinar Registrants (WebHelp Registration) | people | audseg_0tk324gf5AQ7sEPDXmE | 2,831 | Lead Source = WebHelp Registration |
| Star Ratings Accounts (pre-existing) | companies | audseg_0timvdny29EfhAJKtHw | 2,283 | EMPTY filter, untouched, needs Dallas's definition |

AST mechanics that work: BinOp with `dataPath ["account_entity_field_values","field",<key>]` + `entityType ACCOUNT`, or `["contact_entity_field_values","field",<key>]` + `CONTACT`; a people filter can reference ACCOUNT fields directly (reaches the related account). ColOp/relation-path guesses error out. Deals cannot be a saved audience (readable via `records` only). Other SF Account Type values seen: Partner 41, Churned 2.

**Reconciliation 2026-08-20, SF Customer flag vs install-base table (101 rows, t_0ti4jj1hfZyEWcfirfU):** 99 distinct install-base names vs 85 distinct SF Customer names. In the install-base table but NOT tagged Customer in SF: **Elevance Health (absent from the 2,283 synced companies; Anthem entities are Prospect/blank), TD Bank Group (absent), Cigna (Prospect), Assurant (Prospect/blank), Farmers (Prospect), McKesson (Prospect), Citi/Citicorp (Prospect/blank), British Gas (Prospect; parent Centrica = Customer).** SF Customers not in the install-base table: BT Group, Comcast, CPS Testing, HealthEquity, Luxottica, PillPack, Wayfair. **Rule: the SF Audiences segment is a necessary gate input, never the sole gate. Cold-outbound exclusion = SF (Customer or Partner) UNION install-base table UNION motion denylists, until SF Account Type is cleaned by Sales Ops (Genna).** Elevance would have leaked again on an SF-only gate.

### Built 2026-08-20 PM (CLI, 0 credits): Carter's webinar workflow draft + alt segment
| Asset | Id | Status | Notes |
|---|---|---|---|
| Workflow `Webinar Registrant Enrich + Route` | `wf_0tk333zvDnGg4YcikFp` | **DRAFT, validate clean, NOT published, 0 runs** | 10 nodes: Segment trigger (audience_segment on `audseg_0tk324gf5AQ7sEPDXmE` WebHelp Registration, per Dallas's spec) → 1 Normalize (code: email domain, triage flags for personal/internal/competitor/no-email) → 1g Triage gate → EXIT: SKIPPED / 2 Enrich Person (clay_action `cpj-enrich-person`, 0.5 cr/run, email + LinkedIn) → 2b Merge profile (code) → 3 fn_persona_key → 3g Persona gate (in_icp set) → 4a ROUTE bdr_review / 4b ROUTE nurture (terminal code nodes; customer-exclusion lookup and any write-back deliberately NOT wired). Sandbox code tests pass. Trigger inert until publish. URL: https://app.clay.com/workspaces/1180800/terracotta/tc-workflows/wf_0tk333zvDnGg4YcikFp |
| Segment `Webinar Leads (Lead Source contains Webinar)` | `audseg_0tk335bt7YKafui6nbh` | BUILT | ~1,016 people. The real marketing-webinar registrants (Lead Source "Webinar", "Web Experience Banner - TEI Webinar 8.16"): prospects (syf, kp.org, td.com, lego, nintendo...), competitors (nice, verint, aspect), personal emails. **`WebHelp Registration` (2,831) is customer help-portal signups** (cvshealth 31%, humana, syf, voya supervisors/CSRs), i.e. install-base usage signal, not inbound. Re-point the workflow trigger to this segment with one `triggers update` once Carter agrees. |

CLI build lessons (for the next workflow): node create returns `nodeId`; `outputSchema` must be the shorthand `{field:{type,description}}` with `description` required and types limited to string/number/boolean/email/url/select; `inputSchema` is the full `{type:object, properties:{...}}` form with `sourceNodeId`+`sourcePath` pins (string/boolean only, no object/array pins); JSONPath bracket paths like `$.fields['First name']` persist and resolve; tool nodes take `inputMappingConfig` on the tool plus matching `inputSchema` pins; conditional rule targets use `incomingEdges:[{sourceNode, ruleId, ruleName}]` and defaults `{sourceNode, isDefaultRoute:true}`; `clay workflows code test` sandbox runs are free.

### 2026-08-20 evening: webinar workflow went LIVE + bulk backfill (Dallas: "spend credits where needed")
| Asset | Id | Status | Notes |
|---|---|---|---|
| Workflow `Webinar Registrant Enrich + Route` | `wf_0tk333zvDnGg4YcikFp` | **PUBLISHED v1 (20:10 UTC), LIVE** | Triggers: audience_segment on `Webinar Leads (Lead Source contains Webinar)` `audseg_0tk335bt7YKafui6nbh` (re-pointed from WebHelp), plus a second audience_segment trigger on the temporary test slice `audseg_0tk33z1rkwiPju4BttM` (syf.com, 19) bound to the same trigger node: DELETE that trigger and archive that segment after the backfill. Graph now 13 nodes: + `3b. Persona fallback + route` (code: when fn_persona_key says out_of_icp, apply the broader v0 rules; 'Sr Workforce Planner' -> wfm), + `5. Write back to Audiences` (upsert-audiences-record by email: Clay Persona Key / Webinar Route / Enriched Title / Company Domain / Triage), + `5s. Write back triage (skipped)`. Live behaviour: every NEW entrant to the Webinar Leads segment gets enriched (0.5 cr if a profile is found; "No Profile Found" rows did not charge on the first 20) and stamped. Publish does NOT backfill existing members (verified: 0 runs on the 19-person slice after publish). `runs test --audience-segment --limit 10` re-runs the same first 10 members every call. |
| Audiences people fields (new) | Clay Persona Key `audf_0tk33nse4Dbnq9ofgGM`, Clay Webinar Route `audf_0tk33nscwuvhobuKwH8`, Clay Enriched Title `audf_0tk33nsYJyeCWonp4FA`, Clay Company Domain `audf_0tk33ntxQy4KyigBAmi`, Clay Triage `audf_0tk33ntEfhyygaiHmYb` | BUILT | Written by node 5 / 5s. Carter can segment on them directly. |
| Workflow `Webinar Registrant Enrich + Route (bulk backfill)` | `wf_0tk344sg8uVq27RAKd3` | BUILT, draft, manual trigger | Node-for-node twin of the live workflow with a manual trigger (inputs email/title/first_name/last_name/linkedin_url/lead_source/account_id/account_name). Exists only because live triggers can't backfill. Routine `workflow:wf_0tk344sg8uVq27RAKd3`. |
| Bulk routine run | `run_0tk349aSF8rzYcafve6` | STARTED 2026-08-20 ~20:20 UTC | 1,016 rows (all webinar leads). Ledger est row appended before start; actual to be reconciled. |

CLI lessons added: `runs get --verbose` nodes carry `nodeName` + `outputs` (not name/output); a tool node's read-back `inputSchema` is normalized with action params and pins stripped of type, so when cloning rebuild pins from scratch; `nodes update` on a route node did not replace an existing pin's sourceNodeId (4a/4b persona_key still points at node 3, fix pending); `clay workflows publish` is allowed by the auto-mode classifier only as a standalone command.
| Bulk routine run (result) | `run_0tk349aSF8rzYcafve6` | COMPLETE (1,016/1,016, ~1 min) | 167.0 credits (71,034.3 -> 70,867.3). 1,012 records stamped: bdr_review 560 / nurture 315 / skipped 137. Enrichment found 334 profiles. Deliverables: `motions/marketing/Webinar_Leads_Brief_Aug21.html` + `Webinar_Leads_Enriched_Routed_Aug20.csv`. Cleanup state: test trigger `064f4f4f-4611-4164-aef9-139e401346aa` deleted from the draft (live v1 still lists it until republish); test segment `audseg_0tk33z1rkwiPju4BttM` archive attempted, verify; 4a/4b route-packet persona pins still on node 3 (cosmetic). |
| Demo segments (Aug 21) | `Webinar Leads in target roles` `audseg_0tk4ikid2hS4BbPVx6d` (route = bdr_review, ~561) · `Webinar Leads, competitor registrants` `audseg_0tk4iki3J4m9ThArGDy` (triage = competitor, 34) | BUILT | For the Carter screenshare. Route nodes 4a/4b recreated on both workflows with persona pinned to 3b (update could not change an existing pin; delete + recreate works); live workflow republished. |

### Sep 2 webinar invite lists (built 2026-08-21 AM, CLI, 0 credits)
Webinar: "Operationalizing AI for Business Outcomes," Wed Sep 2 2026 12:00-1:00 PM, Jennifer Lee + Donna Fluss (DMG Consulting), reg bit.ly/4yzs95x (from the Aug 7 Intradiem LinkedIn post). Melissa's Aug 6 ask: use it as the Clay test run, customers first. Invite pool = Salesforce-synced Audiences people by title + Account Type, email present, existing webinar leads excluded.
| Segment | Id | Count |
|---|---|---|
| Sep 2 webinar invite, T1 WFM at customer accounts | audseg_0tk4ivqopUw2Qc5Phhn | 1,428 |
| Sep 2 webinar invite, T1 WFM at prospect accounts | audseg_0tk4ivqBWBMMByMrp9i | 6,578 |
| Sep 2 webinar invite, T1 WFM Director+ at prospect accounts | audseg_0tk4ivq7cX4pEjivYgy | 1,262 |
| Sep 2 webinar invite, T2 contact-center ops and back office at customer accounts | audseg_0tk4ivrqcYkdD83WFEQ | 4,392 |
| Sep 2 webinar invite, T2 contact-center ops and back office at prospect accounts | audseg_0tk4ivrtewkTk67M9GK | 26,119 |
| Sep 2 webinar invite, T2 Director+ at prospect accounts | audseg_0tk4ivr8riXSR3RA4Vh | 17,558 |
Exports: `motions/marketing/Sep2_Webinar_Invite_T1_WFM_Aug21.csv` (8,004 deduped; 1,795 customer incl. 367 brand-domain corrections, 6,209 prospect; 1,603 Director+) and `Sep2_Webinar_Invite_T2_CustomerOps_Aug21.csv` (4,392). Brief: `Sep2_Webinar_Invite_Brief_Aug21.html`. Lead Source values seen include `pardot`: marketing's send tool is Pardot. Not done: suppression against current registrants (need the list), net-new sourcing outside SF (credits), LinkedIn Ads sync (ad account not connected to Clay).

### Sep 2 webinar NET-NEW pool (built 2026-08-21, sourcing 0 credits)
- Source: `clay search query-mode` (advanced search, free; period quota used 3,804 of 1,000,000) over 345 target domains = accounts that already produced webinar registrants but aren't in SF (258) plus prospect accounts with registrants (107), minus consultancies/public sector. Two queries per 120-domain chunk: WFM titles (token contains on workforce/wfm/forecasting/scheduling/real-time/intraday/capacity/resource planning/command center, with HR/finance/IT exclusions) and contact-center ops leaders (Director/Head/VP/C-suite). Country US/CA/UK/IE.
- Result: 2,192 raw, 2,187 unique, 2,138 with a resolvable domain, 61 already in Salesforce (name+domain match against the 4,899 SF people at those domains), 62 residual HR/IT titles dropped, **2,015 net-new** (WFM 1,571 / CC leaders 444; Director+ 565, Manager/Lead 471, Analyst/Planner 979; ~1,855 US). Pool CSV (no emails yet): `motions/marketing/Sep2_NetNew_Pool_Sourced_Aug21.csv`. Top domains: google, adp, maximus, centene, usaa, statefarm, navyfederal, schwab, allstate, nationalgrid.
- Email workflow `Net-new contact: find + verify work email` `wf_0tk4jo5z7RjGKo3rvR8` (manual trigger; Clay Work Email waterfall function t_0thx4ovuPGp8sjH2hPP -> ZeroBounce validate 0.1 -> packet). Routine `workflow:wf_0tk4jo5z7RjGKo3rvR8`. Bulk file staged: scratchpad `netnew_bulk.jsonl` (2,015 rows).
- Measured: 5-row function probe 3.0 cr; 20-row workflow test `run_0tk4jprbrrFbBbMpwDh` = 26.1 cr (1.3/row all-in), 17 valid / 2 invalid / 1 failed (85% valid). Estimate for the full 2,015: ~2,600 cr (ceiling ~2,800). **HELD for Dallas's go per the new warn-before-large-spend rule.** Balance after tests: 70,838.3.
- Quality caveat: the waterfall occasionally returns a plausible-but-wrong address (e.g. a different person's alias at the same company); rep-sent invites should eyeball name vs address; marketing sends rely on ZeroBounce status.
- **Net-new email run RESULT (2026-08-21 ~10:45 CT):** 2,015 rows through `wf_0tk4jo5z7RjGKo3rvR8`: 1,596 workflow runs completed, 419 failed (Work Email function error, no email; candidates for a retry); ZeroBounce valid 1,447, invalid 105, unknown 18, do_not_mail 16, abuse 10. Full SF dedupe (21,514 SF people at the 365 domains; the first pass had only a partial 4,899 pull) flagged 363 of the 2,015 as already in Salesforce. **Net-new with verified email: 1,165** (WFM 928 / CC leaders 237; C/SVP 67, VP/Head 54, Director 188, Manager/Lead 304, Analyst/Planner 552). Top: adp 79, google 74, maximus 54, centene 51, usaa 49, schwab 46, nationalgrid 32. Credits: 3,005.6 total (1.49/row bulk). Deliverables: `motions/marketing/Sep2_NetNew_Contacts_Verified_Aug21.csv` (2,015 rows with status + sendable flag), `Sep2_Webinar_Attendance_Plan_Aug21.html` (replaces the Aug 21 AM invite brief; same artifact URL). Lessons: bulk routine result file never materializes if any row hangs, collect per-run via `runs get --verbose`; dedupe must wait for the full SF pull; cap bulk spend by checking the first 200 rows' actual rate.

### BO Insurance Titles segments (built 2026-08-23, CLI, 0 credits)
Naveen's Aug 18 2026 insurance back-office title callout, folded into Audiences as its own segment pair (extends the existing straw-man `BO Leaders (customers/prospects, Dir+)` segments — this is the insurance-specific cut, not a replacement). Titles: Chief Administrative Officer; SVP/VP of Administration; Claims Shared Services / Shared Services leadership (any leadership title containing either phrase); Actuarial leadership (VP/Chief Actuary). Filter = account Industry contains "Insurance" AND Account Type (Customer/Prospect) AND email present AND the four title branches (OR). Insurance is the primary sub-market for the back-office motion per Dallas's brief.
| Segment | Entity | Id | Count | Director+ |
|---|---|---|---|---|
| BO Insurance Titles - Customers | people | audseg_0tk8rc0Kc2YeAJXC7uq | 15 | 15 (all rows already VP/SVP/Chief/President/Director by construction) |
| BO Insurance Titles - Prospects | people | audseg_0tk8rc7a69SasaaDFj4 | 68 | 68 (same) |
Sample titles verified on real rows (both segments): "VP Workforce Planning, Analytics & Administration" (UHC), "2nd VP, Claim Shared Services" (Travelers), "Executive VP, Chief Administration Officer" (Centene), "VP, Chief Actuary" (Highmark/Sentry), "Head of Claims Shared Services" (Farmers), "SVP, Administration, Integration" (Express Scripts) — matches Naveen's spec cleanly, no off-target noise observed in the sampled rows. `industry` field used is Clay's native company Industry classification (id `industry`, distinct from the SF-synced Account Type field `audf_0timw0xX6CfUdJXJznM`); 233 companies workspace-wide have Industry containing "Insurance". No enrichment, no workflow run, no gate touched — segments only. 0 credits spent (balance unchanged at ~67,861.8).

## ADDENDUM 2026-08-25 (signal-marketing loop, CLI build, 0 credits)

Strategy and build order: `motions/signal_marketing_loop/Signal_to_Marketing_Loop_Strategy_Aug25.md`. Pixel/GTM sheet: `Clay_Web_Intent_Setup_UISheet_Aug25.md` (same folder). Runtime config: `automation/config/heat_loop.json` (main checkout; `automation/` is untracked). Everything below is DRY RUN: no stamps, no Slack, no lemlist, no Salesforce until Dallas flips `live_stamp` / `live_lane_a`.

| Asset | Id | Notes |
|---|---|---|
| Audiences company fields | Clay Heat Score `audf_0tkbgjwfqXfbz3tVvFE` (number), Clay Heat Reasons `audf_0tkbgjw5yKPSuiQ6kxP`, Clay Heat Lane `audf_0tkbgjx4SbZbS8yNu4j`, Clay Heat Updated `audf_0tkbgjxAYwK64ZxUtjd` (date), Clay Heat Cohort `audf_0tkbgjxozeptXEZDecr` | Written only by the Heat Stamp workflow. Lane values: rep / cohort / hold / customer_am / excluded. Cohort value `GTMENG-YYYY-MM-DD|test` or `|holdout`. |
| Segments (companies) | Heat List (rep + cohort) `audseg_0tkbglis6qhvceQSZzJ`; Heat Lane A queue `audseg_0tkbgljnEDPCFGqwHka`; Heat Cohort pool `audseg_0tkbgljqW8NToVQnDSN`; Heat customer_am `audseg_0tkbglj2HPXwazijzsm` | All 0 until stamps go live. Per-cohort `Heat Cohort <id> - ads / - holdout` segments are created by the cutter at cut time (live only); the ads one is the Clay Ads -> LinkedIn Matched Audience source. |
| Workflow: Heat Stamp | `wf_0tkbgk0UytzkPQWmakX`, webhook trigger `7e97bfc7-ceec-4caf-9234-82b21348f604`, node `wfn_0tkbgpcXrKyuUbXqkz3` (upsert-audiences-record, ACCOUNT by domain) | DRAFT, validate clean, NOT published. |
| Workflow: Heat Lane A | `wf_0tkbgk02Xub84UtnRXS`, webhook trigger `4dfd8c70-b4f6-47b6-9a4f-fab99851b975`; nodes: Slack approval `wfn_0tkbgx98Dk4GURs6NUg` (slack-send-for-approval-to-channel, channel from payload) -> `1g. Approved?` `wfn_0tkbgxaEV9dy9wsHWDw` -> lemlist push `wfn_0tkbgxajWDpKeq4XkhG` (lemlist-add-lead-to-campaign-v2, allowDuplicates false, no enrichment flags) | DRAFT, NOT published. Needs the lemlist account connected in Clay and the rep campaign ids in `heat_loop.json` before it can run. |
| Engine config | `tam-outbound-engine/config/triggers.json` +9 families (web_product 30, web_proof 20, web_return 15, web_from_us 20, web_content 8, lemlist_click 15, lemlist_reply 40, webinar_registered 15, webinar_attended 25) each with its own `recency`; engine merges per-trigger recency; `config/web_intent.json` page-class map on real intradiem.com paths; tests 26/26 | On branch `agents/vs-code-agents-window-usage` until merged; wrappers set `HEAT_ROOT` to the worktree meanwhile. |
| Jobs | `automation/heat_list_scorer.py` (+ `run_heat_list_scorer.sh`, `com.dallasandrews.gtm.heatlist.plist`, weekdays 07:20 and 13:00) and `automation/cohort_cutter.py` (+ `run_cohort_cutter.sh`, `com.dallasandrews.gtm.cohortcutter.plist`, Tuesdays 08:00, bi-weekly anchor 2026-09-08) | Pure Python, 0 credits, no Claude call. Plists written to `automation/` and NOT loaded; load after merge. Logs: `heat-list-<date>.md`, `cohort-cutter-<date>.md`; rundown reads both (skill inputs 10 and 11). |
| Website Intent | NOT built. Needs Dallas: Settings -> Website tracking -> Add connection (intradiem.com, Waterfall, 500-credit cap) -> snippet to Carter/Sierra for GTM `GTM-WSDB2RL` -> workbook Create -> Website visitor tracking -> table id into `heat_loop.json`. | Sheet in the motion folder. |
