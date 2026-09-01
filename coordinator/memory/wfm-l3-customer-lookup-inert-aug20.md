---
name: wfm-l3-customer-lookup-inert-aug20
description: "Aug 20 2026 real-row read: WFM-Adjacency L3's L1 Customer Lookup returns No Record Found on every Elevance/Molina row, so customer_exclude=false on all 524 rows and HOLD is held only by the audit verdicts (GATE INERT, not an active leak); headless-access fix APPLIED same day, UI lookup re-bind STILL OPEN as of re-verification Aug 27 2026"
metadata: 
  node_type: memory
  type: project
  originSessionId: 89c2a123-02d8-4510-98d1-b221ec71a34d
  modified: 2026-08-27T12:00:04.055Z
---

Found 2026-08-20 while smoke-testing the CLI read path for the gate-integrity re-point (log: `automation/logs/gate-integrity-2026-08-20.md`, evt `gate-integrity-2026-08-20#wfm-l3-customer-lookup-inert`):

- WFM L3 `t_0tic8arWbZp8bSx87Ad`: 524 rows, Send Ready HOLD 524 / READY 0. 293 rows are customers per the exclusion union (Elevance 143, Molina 122, Carelon 4). **All 293 have `customer_exclude=false`** because the `L1 Customer Lookup` action (`f_0tjxaitimfHdnYmh4dN`) returns "No Record Found" even though WFM L1 has `elevancehealth.com` / `molinahealthcare.com` at `customer_flag=TRUE` since Aug 17 16:26 UTC and the lookup recomputed after that (16:46). Likely cause: the lookup's `rowValue` binding is the literal text `"{{Company Domain}}"` (name token in quotes) instead of a field-id binding. Send Ready = audits pass AND !customer_exclude, so the gate is inert until fixed; the moment audits pass on an Elevance/Molina draft it goes READY.
- Star Ratings Contacts `t_0thtm73HHxyiupTuepK`: 143 rows, 16 customer rows TRUE and HOLD, 4 READY rows none customers. Exclusion PASS; `send_ready` formula still lacks customer_exclude/human_approved (standing advisory).
- Fix is Dallas's hands in the UI: re-bind the lookup's row-value input to the Company Domain column, run on all rows, confirm `customer_exclude` TRUE on the 293, Send Ready still HOLD.

**APPLIED 2026-08-20 (Dallas ran apply.sh --apply):** `automation/staging/headless-access-fix-2026-08-20/` holds re-pointed defs for gate-integrity-auditor, table-hygiene, credit-strategist, pipeline-receipts-tracker (CLI-only tools, `clay_rows2tsv.py` parser with `strict=False` because Stars rows carry raw control chars that break jq, GATE INERT verdict class, check 7 = SF segment UNION install-base UNION denylist UNION L1 flags), `apply.sh --apply` installs both copies + registry addendum. Backups of the old defs sit in the staging dir (`backup_copy1_*.bak`, `backup_copy2_*.bak`). The UI re-bind of the WFM L3 lookup is still open.

**Why:** "HOLD=524" read as a verified fix on Aug 17, but the hold came from the audit columns, not the customer gate. Real-row verification must check the table's own customer flag against an independent source, not just READY/HOLD.

**How to apply:** never accept READY/HOLD counts as proof of exclusion; read the customer flag column and, for action lookups, the lookup cell value. Related: [[gate-integrity-fn-send-ready-not-shared]], [[clay-audiences-live-cli-capability-aug20]], [[wfm_adjacency_leak_escalated_aug3]].

**RE-VERIFIED STILL OPEN 2026-08-27** (table-hygiene scheduled sweep, `automation/logs/table-hygiene-2026-08-27.md`): the UI re-bind has NOT happened yet, 7 days later. `L1 Customer Lookup`'s `rowValue` is still the literal string `"{{Company Domain}}"`, not a field reference. Spot-checked 100 rows: lookup returns `"❌ No Record Found"` on all 100, `customer_exclude` reads `false` on all 100, including known-customer domains (blueshieldca.com, point32health.org, carefirst.com). This is a standing open item, not a new leak — surfacing again because it's still unresolved and table-hygiene runs read-only (can flag, can't fix). Needs Dallas's hands in the Clay UI: re-bind `rowValue` to the Company Domain column (`f_0ti8tdrnCsHVcUNjmh8`).
