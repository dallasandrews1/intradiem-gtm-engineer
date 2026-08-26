---
name: gate-integrity-fn-send-ready-not-shared
description: fn_send_ready is documented as the shared send-ready gate across Clay motions but no live table actually calls it — each motion hand-rolled its own local formula and drifted
metadata: 
  node_type: memory
  type: project
  originSessionId: 7cdec17f-b7cf-4470-8073-fe210baf0f37
  modified: 2026-07-27T12:53:58.193Z
---

As of the 2026-07-27 gate-integrity audit, `fn_send_ready` (Clay Function `t_0tiahe2mzsH9CCaC4Sx`) is documented as "the single send-ready gate, shared across motions," but none of the three live contact tables (Cost-Mandate, Star Ratings Contacts, WFM-Adjacency L3) actually call it via a Run-function action. Each has an independently hand-rolled local send-ready formula: Cost-Mandate kept `customer_exclude` + `human_approved`; Star Ratings dropped both (structural gap, not yet an active leak, saved only by approval-timing); WFM-Adjacency dropped everything except the two AI-audit verdicts and has no `customer_exclude` field at all — this is the direct mechanism behind [[wfm-adjacency-active-leak-jul27]].

**Why:** each motion's L3 table was stamped from the golden scaffold and then hand-edited independently rather than actually wiring the shared Function, so the three formulas silently diverged over time with nothing checking they stayed in sync.

**How to apply:** Any new motion stamp or gate edit should verify the table's `Send Ready` formula actually calls `fn_send_ready` (or is audited to match it), not just that the Function itself is correct. The 2026-07-27 agent-architect run proposed `send-ready-function-parity-check` (extend the weekly gate-integrity run to diff every live table's actual formula against the canonical Function) — check `proposal_ledger.md` for whether Dallas has approved it before assuming it's built.
