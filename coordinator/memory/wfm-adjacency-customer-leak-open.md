---
name: wfm-adjacency-customer-leak-open
description: "OPEN as of Aug 7 2026 - 5 Elevance directors at Send Ready READY in WFM-Adjacency; THREE stacked defects, not one, and fixing any single one changes nothing"
metadata: 
  node_type: memory
  type: project
  originSessionId: a6fa178f-5397-4e80-bd71-df855f3566a2
  modified: 2026-08-07T06:08:03.623Z
---

Verified live 2026-08-07 by direct Clay read, not carried from the Aug 3 gate-integrity log.
**Fix sheet: `motions/wfm_adjacency/Gate_Leak_Fix_UISheet_Aug7.md`** (exact IDs, formulas, order).

**Exposure.** L3 `t_0tic8arWbZp8bSx87Ad` (524 rows) has 6 rows at `Send Ready = READY`: 5 Elevance Health directors (Noemi G., Melissa Zam, Jessica Sisneros, Carlos Doroteo, Donisha Jones) + Linda Reid at vnshealth.org (she is legitimately eligible, not a leak). Behind them: 159 elevancehealth.com + 133 molinahealthcare.com = 292 contacts. Elevance and Molina are customers per `Accounts (Master)` (54 customer rows across 6 parents). Nothing sent; all 8 lemlist campaigns are draft.

**It is THREE defects stacked, which is why two prior passes closed nothing:**

1. **L1's `customer_flag` was never populated.** `t_0tict25TSXgTgdJgtZZ` field `f_0tict27m8jMKrMoFjFE` is a plain TEXT column with **no formula**, and **all 28 rows read literal `"FALSE"`**. Not a two-account misclassification, an unwired column. No account in this motion has ever been customer-checked.
2. **L3's `Send Ready` (`f_0ti9ygfsJv3y8g6Nkcz`) never mentions customer status.** Two AI critic verdicts only. All 63 columns checked: no `customer_exclude`, `human_approved`, `bdr_claimed`, or `customer_flag` exists on the table.
3. **The workflow kill switch FAILS OPEN, and this was in no prior log.** `wf_0tie30io3hiPqSzVRU2` node `1. Eligibility kill switch` runs `fn_eligible`, so it looks protected. Its `Customer Flag` input is wired to `$.customer_flag` on the L3 table trigger, **a column L3 does not have**. And gate `wfn_0tie37dgbfKmaoxhjV4` routes `eligible == False` to EXIT with the **default route continuing**, so an empty/unmatched value proceeds.

**ORDERING TRAP:** fix L1's data BEFORE L3's formula. The new L3 formula reads `customer_flag` through `Universe Lookup` into L1; with L1 still saying FALSE, the fix looks green and changes nothing.

**Coercion trap (the live example for the house rule):** `customer_flag` is TEXT `"TRUE"`, and in JS the string `"FALSE"` is truthy. `!{{customer_flag}}` is wrong in both directions. Use `String(...).trim().toUpperCase() !== "TRUE"`, and `?? "TRUE"` so a missed lookup fails closed.

**Not fixable by API.** Clay table columns have no CLI/MCP edit surface (`tables` = list/get/columns/rows/query only; `edit_node` is workflows only). Function tables are not even readable (`clay tables columns get t_0tial9rYKzWKU2y9MTC` returns `not supported by this API`), so `fn_eligible`'s return semantics cannot be verified without running it. That is why step 3 was left to the UI rather than blind-edited.

**Root cause is convergence:** `fn_send_ready` `t_0tiahe2mzsH9CCaC4Sx` exists and no live send table calls it; three motions run drifted hand-rolled copies. Related: [[clay-tables-api-undercounts-workspace]], [[engine-room-deliverable-aug7]].
