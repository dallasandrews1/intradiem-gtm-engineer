---
name: impact-realized-gate-aug7
description: FIXED Aug 7 2026 - impact_engine now refuses pre-role outcomes and control tower must EARN the REALIZED label; supersedes the demo-data contradiction
metadata: 
  node_type: memory
  type: project
  originSessionId: a6fa178f-5397-4e80-bd71-df855f3566a2
  modified: 2026-08-07T06:08:29.955Z
---

**Was:** `impact/outcomes.csv` shipped with two interview-era rows dated 2026-06-10 and 2026-06-11, before the role started (2026-07-06). They produced a standing "1 meeting booked / $180K pipeline" that `build_control_tower.py` rendered under a **hardcoded** `"trust": "REALIZED"`, while `automation/logs/credit_pipeline_receipts.md` independently reported 0 meetings and $0. Two files in one repo disagreed about whether a meeting had happened.

**Fixed 2026-08-07, at the source rather than by editing the output:**

- `impact/impact_engine.py`: added `ROLE_START = "2026-07-06"`. `realized_metrics()` now skips any row dated before it, **and fails closed on undated rows**, reporting `excluded_pre_role_rows` / `excluded_undated_rows` so the exclusion is visible instead of silent. Regression-tested both ways.
- `build_control_tower.py`: new `realized_trust(impact)` replaces the hardcoded label. REALIZED requires the source present, fresh (7 days), `data_complete`, and zero gate-excluded rows. Everything else is `UNVERIFIED`. Unit-checked across 5 cases, including the historical Jun 13 file, which now correctly reads UNVERIFIED.
- `tam-outbound-engine/config/roi_model.json`: added `_verified: false`. `impact_engine` now emits `surfaced_basis` and stamps the surfaced total `[UNVERIFIED]` in the summary, so a placeholder dollar cannot travel without its label.
- Demo rows moved to `impact/outcomes.demo-archive.csv` with a header explaining why. **Archived, not deleted.**

**Result:** realized now reads 0 meetings / $0, matching the receipts ledger. Surfaced still reads $41.6M but always carries `[UNVERIFIED]`.

**Still open and NOT fixed by this:** the credit reconciliation gap (itemized per-motion lines sum to ~1,927 against ~11,649 consumed top-down), and `credit_pipeline_receipts.md` being stale since 2026-07-19. Those need Usage-page confirmation and cannot be derived. See [[engine-room-deliverable-aug7]].

**Durable rule:** never let a trust label be a literal. If a label asserts provenance, it has to be computed from the source's actual state, or it will eventually assert something false and nobody will notice.
