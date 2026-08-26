---
name: wfm-adjacency-leak-escalated-aug3
description: "RESOLVED 2026-08-17 — WFM-Adjacency customer-exclusion leak (Elevance/Molina) closed after 21 days; Dallas applied Gate_Fix_UISheet_Aug3.md and both fixes were verified on real rows same day"
metadata: 
  node_type: memory
  type: project
  originSessionId: 8e07e6fd-18f2-4ad0-8b15-44900b30f7c6
  modified: 2026-08-17T16:55:17.523Z
---

**RESOLVED 2026-08-17:** Dallas applied both fixes from `Gate_Fix_UISheet_Aug3.md` on the morning of Aug 17 and they were verified live on real rows the same hour (Clay MCP table reads, interactive session): L1 `customer_flag` now TRUE for Elevance Health and Molina Healthcare (28 rows read), and L3 Send Ready reads HOLD = 524 / READY = 0, so the six exposed customer contacts are out of READY. Closure recorded in `gate-integrity-2026-08-17.md` addendum, evt: gate-2026-08-17#wfm-leak-closed. Wave holds tied to this finding are released. Still open from this thread: wiring the shared `fn_send_ready` so motions stop hand-rolling gate formulas (structural advisory, not a leak), and headless row access for the scheduled audit (it ran UNVERIFIED on Aug 17). History below kept for the record.

---

**UPDATE 2026-08-04:** Dallas confirmed (in a live session, Aug 3 ~09:00 CDT) he wanted this fixed and was given a full click-by-click UI sheet (`Gate_Fix_UISheet_Aug3.md`, Fix 1a/1b — customer_flag reconciliation for Elevance/Molina in L1, `!customer_exclude` added to the L3 Send Ready formula). Whether Dallas actually ran it in Clay is **unconfirmed** — the last thread-listener pass (Aug 3, 21:23 CDT) still read the leak as open (518 HOLD / 6 READY, 5 Elevance rows READY), and no gate-integrity audit has run since (next scheduled is Aug 10). The related Apollo Push gate fix is half-done: the node-edit part landed and is `validate_workflow`-clean, but wiring `customer_exclude_bool` into its Manual trigger is still a separate UI-only step in the same sheet. **Do not assume either fix is live without a fresh check** — this is exactly the kind of "confirmed-in-a-thread but never re-verified" gap the 2026-08-04 rundown proposed a `fix-confirmation-audit-trigger` for (see `proposal_ledger.md`, unbuilt).

---

The WFM-Adjacency motion's customer-exclusion leak, first flagged as an active stop-the-line breach on 2026-07-27 (four real Elevance Health contacts at Send Ready = READY), was re-checked on live rows during the 2026-08-03 scheduled gate-integrity-auditor run and found **unfixed and worse**: a fifth Elevance Health contact (Donisha Jones) has since reached READY, and 292 total Elevance Health + Molina Healthcare contacts (159 + 133) sit under a Send Ready gate (`t_0tic8arWbZp8bSx87Ad`, field `f_0ti9ygfsJv3y8g6Nkcz`) that still has zero reference to customer status. Root cause unchanged: WFM's own L1 table (`t_0tict25TSXgTgdJgtZZ`) still stores `customer_flag = "FALSE"` for both companies even though Star Ratings' Accounts (Master) correctly flags them as customers.

A second instance of the identical design gap was also found this run: a new workflow `Stars Post-Approval Apollo Push (Pilot)` (`wf_0titsor23E4P75KaM8t`, created 2026-07-27, the same day as the last audit) gates only on `human_approved`, never `customer_exclude`. Dormant today (all 16 real customer rows are human_approved=false) but structurally the same bug class.

Full verdict: `automation/logs/gate-integrity-2026-08-03.md` in the repo.

**Why:** two consecutive weekly audits (Jul 27, Aug 3) confirmed this leak with zero sign of remediation attempted in between, and the exposure count went up, not down. This is no longer a "flag it and wait" situation — it has now failed to self-correct across a full week with the audit result presumably reaching the daily rundown.

**How to apply:** Any future session touching WFM-Adjacency, the gate-integrity-auditor cadence, or Dallas's priority list should treat this as the top standing blocker until (a) WFM L1's `customer_flag` is reconciled against Star Ratings' denylist/Nate's SF exclusion list, and (b) WFM's `Send Ready` formula gets a `!customer_exclude` term — ideally by finally wiring `fn_send_ready` (which is correct and unused) instead of each motion's hand-rolled local formula. Do not treat a "PASS last week" as still true without a live re-check; this exact leak proves silent drift happens fast. See [[gate-integrity-auditor-agent]] if that memory exists, and flag this loudly in the next daily rundown / Naveen readout if it's still open.
