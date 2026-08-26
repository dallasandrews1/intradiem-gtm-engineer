---
name: invoke-workflow-trigger-inputschema-jul20
description: "Invoke Workflow column inputs = a SINGLE Inputs JSON box whose keys pass to the trigger VERBATIM (snake_case, case-sensitive). NOT driven by trigger inputSchema. Pass SCALARS (dot-paths), objects don't pass reliably."
metadata:
  node_type: memory
  type: reference
  originSessionId: 7c09b570-5dad-4007-8754-8157e967649b
  modified: 2026-07-20T16:40:03.762Z
---

Jul 20 2026: Wiring the Stars 5-touch workflow `wf_0tiegzuo3PzJ4UtUGFA` to the Contacts table `t_0thtm73HHxyiupTuepK` via its `Invoke Workflow` action column (`f_0tigv5kewgcXkv9eJRp`). Hard-won mechanics (same as the WFM runbook [[wfm-sendready-runbook-jul20]]):

**CONFIRMED MECHANISM (Jul 20, verified by experiment):** The Invoke Workflow action column builds its per-input mapping list from the workflow GRAPH — specifically the trigger inputs CONSUMED BY THE FIRST NODE AFTER THE TRIGGER (the entry node). It does NOT read the manual trigger's declared inputSchema (setting that via surfaces_edit_trigger was a wrong lever — harmless but the column never reads it). Proof: a brand-NEW column on the current workflow version still showed only `customer_exclude` — which killed the "column cached the schema" theory. `customer_exclude` was the ONLY trigger input consumed by the entry node (1g. Customer-exclude gate). So the column surfaced only that one.

**THE FIX that worked:** make the entry node declare ALL the trigger inputs. For Stars, edited the entry conditional gate 1g (`wfn_0tiehaekZA9kfDpjpRf`) to list all 19 trigger inputs as `conditionalConfig.variables` (each inputRef path `$.<key>` sourceNodeId = trigger `wfn_0tiegzuTFCfeSZXx32R`) AND in its inputSchema. The gate's RULE still tests only `customer_exclude` (Equal "TRUE"), so routing is byte-identical; the extra variables are unused but make the column surface all 19. edit_node persists conditional variables + inputSchema (validated clean). Then hard-refresh the Clay tab (Cmd+Shift+R) + pick the newest Version in the column → all 19 input rows appear. (For a code/agent entry node you'd instead declare all inputs in its inputSchema.)

**Column maps by COLUMN only** (no typing/JSON/paths in the Stars UI): each of the 19 inputs points to a real table column. Existing columns cover most; 4 helper Formula columns needed for the Lookup sub-fields (cs_star/clin_star/members/contract_id). addr_2028_musd left unmapped (no contract-grain data). customer_exclude -> raw text col f_0thzalcNJ5VDtBRUcri (gate does Equal "TRUE"). See mapping table below.

(Earlier note, still true for OTHER workspaces/older UI: WFM's Invoke Workflow column used a single JSON Inputs box whose keys pass to the trigger verbatim — a different/older UI mode. Stars' current UI is per-field column-mapping, driven by the graph as above.)

**Enumerate the keys** the workflow reads from the trigger by grepping the workflow dump for sourcePath near the trigger node id. Stars needs 15: first_name, job_title, company, seniority_tier, persona_key, why_now, addressable_forgone_qbp_musd, cliff_edge_contract_count, cs_star, clin_star, addr_2028_musd, members, contract_id, customer_exclude, email_status (+ literals source_motion, bdr_claimed, human_approved, li_recent_post_hook).

**Pass SCALARS via dot-paths, NOT whole objects.** WFM proved a scalar leaf dot-path works in the box (`"{{f_col}}?.record?.field"`); passing a whole JSON object is unproven/likely stringifies. So the star fields go in as scalars from the Lookup; node 5a (`wfn_0tiehcioJrFRnJc9Riq`) ASSEMBLES account_row from those scalars for MessageGen (its original design — do NOT refactor it to take an account_row object; that bet on object-passing and was reverted).

**Lookup key path (verified, not guessed):** the `Lookup Single Row in Other Table` action wraps the matched row under `.record` keyed by column NAME (confirmed on this table: `{{Lookup Single Row in Other Table (2)}}?.record?.Email`). Accounts (Master) = `t_0thuumoUcu6wAAhovti`, columns (from canonical CSV) are snake: contract_id, parent_org, marketing_name, members, overall_star_2026, cs_star, clin_star, gross_forgone_qbp_musd, addressable_forgone_qbp_musd, addressable_pct. So `{{f_0thuwo4xcvzA4i3Egiq}}?.record?.cs_star` etc. **There is NO addr_2028_musd column** — pass it "" (empty); the compose omits the 2028 sentence rather than fabricating (verified-claims gate).

**customer_exclude gate hardened:** gate 1g (`wfn_0tiehaekZA9kfDpjpRf`) changed from operator "True" (truthiness — text "FALSE" is truthy, ambiguous) to exact `Equal "TRUE"` (BinOp value:"TRUE"). Map customer_exclude to the RAW text column `f_0thzalcNJ5VDtBRUcri` (formula guarantees exactly "TRUE"/"FALSE"). The Checkbox helper `customer_exclude_bool` (f_0tigv0bPYTxSt3Zdh7s) is now UNUSED — a column value interpolated through the Inputs box stringifies, so a real boolean can't survive it anyway; the gate must string-match.

**Contacts field IDs for the Inputs JSON:** first_name f_0thtm73zrsrnkq9cqxG, job_title f_0thtm74WsoQtAf6vg6m, company f_0thtm74JvDBs8jimWYf, seniority_tier f_0thtm77QKTuaPahmAhD, persona_key f_0thv1b3dWVzfK4BKNAK, why_now f_0thuvhooGA2y8idyaZQ, addressable_forgone_qbp_musd->Addressable CS-slice f_0tigi0jRvx7xNjMUszG, cliff_edge_contract_count f_0thuvf8EotuTDBXNyQr, Lookup f_0thuwo4xcvzA4i3Egiq, customer_exclude f_0thzalcNJ5VDtBRUcri, email_status->Status f_0thvwirStgd9SBpP4qY. Literals: source_motion="star_ratings", bdr_claimed=false, human_approved=false (dry-run -> ends HOLD), li_recent_post_hook="". See [[stars-live-table-dollar-wiring-jul20]], [[voicefix-two-pass-architecture-jul20]].
