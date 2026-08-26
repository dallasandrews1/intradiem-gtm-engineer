---
name: stars-live-table-dollar-wiring-jul20
description: "Live Stars table (Contacts Buying Committee) feeds MessageGen and its critic a GROSS dollar mislabeled as addressable; fix sheet written. Live critic is a forked copy, not fn_draft_critic."
metadata: 
  node_type: memory
  type: project
  originSessionId: 7c09b570-5dad-4007-8754-8157e967649b
  modified: 2026-07-20T04:30:35.661Z
---

Jul 20 2026, from a deep read of live table `t_0thtm73HHxyiupTuepK` "Contacts (Buying Committee)" (143 rows, workspace 1180800):

1. **Live critic is FORKED, not shared.** The Email-1 critic is a hand-written `Draft Audit` AI column (`f_0ti6ehbktFZ6uMkz8dT`), NOT a call to `fn_draft_critic` (`t_0tiabaamPvDuEyTxSaF`). So fixes to the shared `fn_draft_critic` (or the workflow's critic) do NOT reach wave 2's actual gate. See [[stars-5touch-concurrency-fix-jul20]].

2. **Gross-as-addressable bug.** Both the `MessageGen Email 1 (v2.2)` column (`f_0ti6c7jcHFffy94Qmqv`, prompt line) and `Draft Audit` read the token `{{Account Forgone QBP ($M, 2026-cycle)}}` (`f_0thuvdcX5bCtUh8tzRX`), which is a hardcoded GROSS map (Centene 165.8, Humana 1776.3) but is LABELED "CS-attributable slice." The true CS-slice (Centene 52.5, Humana 568.9, Cambia 0.6) already lives inside the `Why Now (2026-cycle)` formula (`f_0thuvhooGA2y8idyaZQ`) second map. The only 2 live critic FAILs are both Cambia, caught correctly (gross 4.8 vs real 0.6). Pre-existing; Wave 1 shipped with it.

3. **Fix sheet written**: `motions/star_ratings/Stars_Wave2_Dollar_Wiring_Fix_Sheet.md`. 3 steps: create `Addressable CS-slice ($M, 2026-cycle)` formula field (CS-slice map)[parent_key], repoint MessageGen token + Draft Audit token to it. UI-only (table columns not editable via MCP). Reversible, no send-gate impact.

Still-open smaller items (flagged in sheet, not wave-2 blockers): (a) `addr_2028_musd` from the account-row lookup is CONTRACT-grain but framed account-wide for multi-contract payers (Centene x21, Medica x3); (b) `parent_key` renders "cvs" but the dollar maps key on "aetna"/"cvshealth" → CVS/Aetna dollars blank.
