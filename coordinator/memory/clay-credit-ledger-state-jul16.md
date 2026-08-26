---
name: clay-credit-ledger-state-jul16
description: "Reconciled Clay credit total: 864/5,000 confirmed (Jul 14) / ~985-990 bridged estimate (Jul 17); canonical ledger lives in Intradiem GTM Engineer, not any per-motion project folder"
metadata:
  node_type: memory
  type: project
  originSessionId: catchup-jul17-2026
---

Last Usage-page-confirmed reconciliation was Jul 14: **864/5,000 monthly credits (17.3%)**, by workbook — GTM Engine 702, Back Office Motion 119, Find-and-Verify-a-Job-Change 44. The automated Thursday creditcheck job's first unattended run (Jul 17) bridged this forward to **~985-990/5,000 (~19.7%)** by folding in the Jul 15-16 runs still logged "pending meter-confirm" (Cost-Mandate slices, Blue Shield of CA + Aflac one-offs) — that bridge is not a fresh Usage-page read, so those rows stay unconfirmed until Dallas reads the Usage page by hand. 60%-burn alert never in play. Both figures are now recorded in the ledger's running header (updated Jul 17).

**Canonical ledger location (settled Jul 17):** `Intradiem GTM Engineer/Clay_Credit_Ledger.md` is the ONE source of truth — meter-verified history since 2026-07-07, wired into the Thursday creditcheck automation and the `clay-credit-steward` skill. A same-day WFM-Adjacency session created a second, parallel `Clay_Credit_Ledger.md` inside the separate `Clay Builds and Strategy` project folder (sibling to `Intradiem GTM Engineer`, not inside it) instead of appending to the canonical one. Merged and the duplicate now redirects to canonical — see [[clay-builds-strategy-duplicate-ledger-jul17]].

**Open item:** the ledger's Budget-by-motion table originally summed to exactly 5,000 across 4 lines; Cost-Mandate and WFM-Adjacency have both opened since without a formal reallocation pass, and WFM-Adjacency's proposed 3,500 alone doesn't fit what's left of Reserve once Cost-Mandate is counted. Needs one explicit call from Dallas on how the 5,000 splits across five motions now — flagged in the ledger, not resolved.

**How to apply:** before quoting a credit total in the Friday readout or any exec deck, use the ledger's own confirmed/bridged split rather than treating the bridged estimate as authoritative. Any new motion's credit activity — regardless of which project folder that motion's build docs live in — appends to the canonical ledger path above, never a new file. Ties to [[clay-credit-steward]] skill.
