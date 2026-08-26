---
name: clay-build-audit-jul12
description: "Jul 12 red-team audit of the live Clay L2 build found a live customer-leak in intent_score (R1, critical) — fixed and verified same day; measure_slippage signal built live and free"
metadata:
  node_type: memory
  type: project
  originSessionId: aa8ceb79-626e-4543-8aa3-e0e0309a2e5d
---

Adversarial audit of the live Clay build + L2 intent layer, Jul 12 2026. Full report: `greenlight-pack/17_Clay_Build_Audit_2026-07-12.md`.

**Top finding (R1, critical) — fixed + verified live same day:** `intent_score` originally self-cleaned only on `overall_star_2026 >= 4`, not `customer_flag`, so Humana/UHC/CVS (customers, sub-4.0) sat at intent 15-35/in_motion. Fixed: both `intent_score` and `intent_status` now gate on `(star>=4 || customer_flag=="TRUE")`. Verified: all customer rows now 0/excluded.

All other findings also fixed same day (0 credits): hiring threshold corrected, vestigial signal columns hidden, tests expanded 17→37 (customer-gate assertions), credit cadence corrected to parent grain (~260/sweep, ~520/mo vs ~1176 at contract grain). Specced + held for go: parent-grain helper table, closed-loop attribution, back-office fork.

**Ran live Jul 12** (Dallas: "my gut says run it"): first real signal sweep on 44 eligible-only accounts, produced a live self-cleaning ranked list (customers 0/excluded, eligible in_motion/dormant, named leadership hits). Verified spend via Clay Usage page: 343 of 5,000 monthly credits (~7%).

**measure_slippage signal built + wired live**, free (first-party CMS data, prior-cycle 2025 vs 2026 star movement): overall Star declined AND HD5/HD3 domain <=3.0 = service gap = QO-addressable; 22/98 fire. Refresh each October CMS release.

**Cleanup:** a stray "Create Clay email campaign" click during the audit created a draft campaign that auto-synced ~10 real leads via an unintended second sync column — caught, column disabled, draft deleted, both verified gone. Send gate re-verified intact (all 137 Contacts rows HOLD, human_approved unchecked). Ties to [[l2-intent-layer-built-jul11]], [[customer-file-landed-jul10]], [[built-means-in-the-live-tool]].
