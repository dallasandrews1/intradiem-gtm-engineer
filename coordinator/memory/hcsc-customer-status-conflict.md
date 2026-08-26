---
name: hcsc-customer-status-conflict
description: RESOLVED 2026-08-03 — HCSC customer-status leak in the TAM engine was fixed via a customer-denylist cross-check; verified gone as of the 2026-08-04 rundown
metadata: 
  node_type: memory
  type: project
  originSessionId: b5286e82-0af3-4cff-ad51-fb54b9774499
  modified: 2026-08-04T13:00:05.989Z
---

**RESOLVED 2026-08-03, verified 2026-08-04.** The `tam-account-customer-filter` fix (proposed 2026-07-29) landed: `tam-outbound-engine/config/customer_denylist.json` added, `account_engine.py` now cross-checks every account against it, HCSC is in `excluded_customers`, 27/27 tests pass, and `account_plays.json`/`control_tower_state.json` were regenerated. Confirmed on 2026-08-04: HCSC no longer appears in `control_tower_state.json`'s signal list. Treat this specific leak as closed — the history below is kept for the pattern, not as an open item.

---

Health Care Service Corporation (HCSC / BCBS IL-NM-OK-TX / HealthSpring, the rebranded ex-Cigna Medicare book) is a confirmed existing Intradiem customer. The 2026-07-27 gate-integrity audit flagged it `customer_exclude = TRUE` (one of 16 real customer-status rows caught in that audit). Despite that, the same day's war-room log staged HCSC as a Priority-1 cold-outreach candidate (new CFO/Treasurer + Stars-cliff window + Medicare reorg), and separately `tam-outbound-engine/account_plays.json` / `impact/impact.json` present HCSC as a live $11.9M Tier-1 net-new TAM target with a fully drafted 4-persona cold sequence.

On 2026-07-30, follow-up research also found the underlying "new CFO/Treasurer Sarah Soong" claim itself was wrong — a misdated 2021 appointment, not a 2026 event — so that staged row is refuted on the facts as well as blocked on customer status.

Health Care Service Corporation (HCSC / BCBS IL-NM-OK-TX / HealthSpring, the rebranded ex-Cigna Medicare book) is a confirmed existing Intradiem customer. The 2026-07-27 gate-integrity audit flagged it `customer_exclude = TRUE` (one of 16 real customer-status rows caught in that audit). Despite that, the same day's war-room log staged HCSC as a Priority-1 cold-outreach candidate (new CFO/Treasurer + Stars-cliff window + Medicare reorg), and separately `tam-outbound-engine/account_plays.json` / `impact/impact.json` present HCSC as a live $11.9M Tier-1 net-new TAM target with a fully drafted 4-persona cold sequence.

On 2026-07-30, follow-up research also found the underlying "new CFO/Treasurer Sarah Soong" claim itself was wrong — a misdated 2021 appointment, not a 2026 event — so that staged row is refuted on the facts as well as blocked on customer status.

**Why:** the Star Ratings motion's own denylist/gate knows HCSC is a customer, but neither the war-room signal sweep nor the TAM engine's account scoring/seed data currently cross-checks against that same denylist before staging or scoring an account. Two independent surfaces (war room, TAM engine) both nearly routed a current customer into cold outbound.

**How to apply:** Before treating HCSC (or any parent org) as a net-new outbound candidate in any war-room log, first-draft, or TAM strike plan, check current customer status first — don't assume a prior log's framing was correct. The proposed fix (per `proposal_ledger.md`, Idea 3 from the 2026-07-29 daily rundown) is to run the same customer denylist Star Ratings' Accounts (Master) uses against `tam-outbound-engine/data/tam_accounts.csv` and strip/flag customer-tagged domains before they can generate a strike plan — check whether Dallas has approved/built this before assuming it's fixed. See [[gate-integrity-fn-send-ready-not-shared]] and [[wfm-adjacency-active-leak-jul27]] for the same root pattern (hand-rolled gates drifting out of sync) showing up on a third surface.
