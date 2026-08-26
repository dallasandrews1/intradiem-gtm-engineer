---
name: wfm-adjacency-active-leak-jul27
description: WFM-Adjacency Clay motion had an active customer-exclusion leak as of 2026-07-27 — 4 Elevance Health contacts at Send Ready READY with generated drafts
metadata: 
  node_type: memory
  type: project
  originSessionId: 7cdec17f-b7cf-4470-8073-fe210baf0f37
  modified: 2026-07-27T12:53:49.175Z
---

On 2026-07-27, `gate-integrity-2026-07-27.md` found WFM-Adjacency (Clay table `t_0tic8arWbZp8bSx87Ad`, "L3") had gone live (0 to 524 rows since Jul 20) with a customer-exclusion gate that never checked customer status. Four real Elevance Health contacts (Director-level Customer Care) were sitting at `Send Ready = READY` with fully generated cold-outreach drafts. Elevance is a confirmed Intradiem customer. Root cause: WFM-Adjacency's L1 table still stores `customer_flag = FALSE` for Elevance/Molina (same misclassification flagged as latent on Jul 20), and the `Send Ready` formula only checked the two AI-audit verdicts, never `customer_exclude`. Molina (100+ contacts, all HOLD) is one AI-critic pass from the identical failure.

**Why:** WFM-Adjacency's send-ready gate was hand-rolled independently of Cost-Mandate's (which correctly includes `customer_exclude` + `human_approved`). The Function meant to be the shared gate, `fn_send_ready`, is documented as "the single send-ready gate, shared across motions" but no live table actually calls it — each motion drifted its own local formula.

**How to apply:** Before any WFM-Adjacency sourcing or send-readiness work resumes, confirm with Dallas that (1) the 4 Elevance rows were manually pulled off READY, and (2) `Send Ready` has been rewired to include a real `customer_exclude` check. Until confirmed, treat WFM-Adjacency as blocked, not just "parked." See [[gate-integrity-fn-send-ready-not-shared]] for the broader pattern this incident exposed.
