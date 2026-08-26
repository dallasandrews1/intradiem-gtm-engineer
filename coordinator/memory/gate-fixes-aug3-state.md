---
name: gate-fixes-aug3-state
description: "Aug 3 gate-fix state: TAM HCSC filter live+tested, Apollo Push gate node hardened but inert until trigger wiring, WFM leak STILL OPEN pending Dallas's UI sheet (Gate_Fix_UISheet_Aug3.md)"
metadata:
  type: project
---

Aug 3 2026, Dallas confirmed all three gate fixes from the gate-integrity STOP-THE-LINE audit via the new rundown thread loop, executed in a live session.

State after execution:
- `tam-hcsc-filter` DONE: tam-outbound-engine now has config/customer_denylist.json (source of truth = greenlight-pack/Active_Customers_SF_Jul10.csv + alias patterns). build_plays returns (plays, excluded); HCSC is out of cold output into excluded_customers, MCP get_strike_plan refuses customer domains, 27/27 tests pass.
- `apollo-push-gate-fix` HALF-LIVE: gate node wfn_0titspxijvd45DBu6Q6 in wf_0titsor23E4P75KaM8t now requires human_approved AND NOT customer_exclude_bool (validated), BUT the Manual trigger doesn't declare customer_exclude_bool, so at runtime the check is inert until Dallas adds the trigger field. validate_workflow passing does NOT mean the gate is live. Workflow dormant (all 16 customer rows human_approved=false).
- `wfm-sendready-fix` NOT DONE, leak open: WFM L1 customer_flag is a STATIC text column (no formula, no workflow node) and L3 Send Ready is a table formula; the tables API on this plan has no write path, so both are Clay-UI-only. Ordered click-by-click sheet saved at project root: `Gate_Fix_UISheet_Aug3.md` (Fix 1a before 1b; expected end state 523 HOLD / 1 READY max). Until Dallas runs it, WFM L3 still shows 5 Elevance Health contacts at READY.

Standing lesson confirmed again: [[clay-tables-cli-observability-gated-jul27]]: table columns/formulas are never agent-editable in this workspace; only workflow nodes are. Scope note: WFM L3 has no human_approved/bdr_claimed at all (golden-parity gap), deliberately NOT folded into this fix.
