---
name: backoffice-motion-forked-jul13
description: "Back-office motion (Mandate 3) forked off the L2 Stars spine Jul 13 with an INVERTED kill switch, then built live in Clay as its own workbook; ICP v1 supersedes v0; Scott Kemme is now a 50-contact review, not a build gate"
metadata:
  node_type: memory
  type: project
  originSessionId: d2d0c444-41ee-442e-a010-f7d16111c9e2
---

Jul 13 2026: stood up motion #2 (back-office install-base / Mandate 3) as a FORK of the L2 Stars spine. Dallas said operate without waiting on Scott Kemme, so the whole engine was built on a v0 straw-man ICP, leaving only the paid 200-contact sourcing gated on ICP ratification.

**Key design ("fork not copy"):** the back-office motion INVERTS the Stars kill switch, encoded in `motion_overrides.back_office`. `customer_flag` is NOT an exclusion here (the customer's back office IS the target); `fo_risk_flag` suppresses instead; `install_base` is a warm-base term; `owner_cleared` is a send gate. Proof case: Humana is excluded in Stars but shows grade_lift/45 in back-office.

Repo build (0 credits): 6 back-office signals, scorer `--motion` CLI, tests 37→61 green including a Stars-parity guard.

**Same day, ICP upgraded to v1** (execution-ready, supersedes v0): grounded in the real install base (101 accounts from [[customer-file-landed-jul10]]), the Back Office Optimizer product, and Intradiem's house rubric → personas bo_claims/bo_shared/coo_finance. Built `BackOffice_Target_Universe_v1.csv` (56 T1 / 35 T2 / 10 T3). Scott Kemme's role changed from build-gate to a 50-contact quality review. The one open decision left is the credit go on the sourcing pull.

**Then actually built in Clay** (Dallas caught that nothing existed there yet — repo-only doesn't count, see [[built-means-in-the-live-tool]]): a new isolated workbook "Back Office Motion" (one workbook per motion, deliberately not shared with Stars), imported the 101-account universe, built the inverted intent_score_bo + intent_status_bo formulas live (0 credits), added 6 signal checkbox columns, verified end-to-end with a live test-then-revert. Staged a Sample-50 cohort (15 Tier-1 accounts, ~49 contacts) as the smallest irreversible step before a full 200-contact pull — sourcing 200 blind was flagged as the mistake to avoid. Ties to [[intradiem-q3-mandates]], [[l2-intent-layer-built-jul11]], [[clay-build-audit-jul12]].
