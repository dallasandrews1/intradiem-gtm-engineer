---
name: l2-intent-layer-built-jul11
description: "L2 intent layer built Jul 11: config + runnable scorer + ledger + spec, then built live in Clay same day; L2 is a Clay table layer, NOT a Claude cron; 5,000 credits is MONTHLY"
metadata:
  node_type: memory
  type: project
  originSessionId: 9a0d7e1b-8571-48bc-b373-5cff3cda3f2c
---

L2 (signal→intent) layer built Jul 11 2026 as the head start for the Clay column stand-up. Files in `intradiem-signal-engine/`: `config/l2_intent_signals.json` (5 signals — sec_filing_stars 30/T1, earnings_stars_mention 25/T1, quality_leadership_change 20/T1, quality_hiring_cluster 15/T2, claims_backlog_news 10/T2; recency decay 30-120d floor 0.4; self-clean at overall_star_2026>=4.0 forces intent 0 + drops account), `l2_intent_scorer.py` + tests (17/17 green). Spec: `greenlight-pack/16_L2_Signal_Monitoring_Spec_Jul11.md`. Ledger created: `Clay_Credit_Ledger.md`.

Two corrections this session: (1) the 5,000 Clay credits is a **MONTHLY** budget, not quarterly. (2) **L2 is the Clay table layer** (signal enrichment columns + intent_score + self-clean formula, refreshed by Clay's native column auto-update schedule), NOT a Claude scheduled task — Dallas caught this; the two Claude L2 cron tasks were deleted. Ratified cadence: monthly full 5-signal sweep ~400cr, weekly delta on fast movers ~100/wk, event-triggered sweeps around earnings + October CMS. Steady state ~800/mo.

**Update same day:** L2 columns built LIVE in Clay via Chrome extension on Accounts (Master), auto-run OFF (zero credits). 5 checkbox signal columns + intent_score formula (self-clean baked in) + intent_status formula. Verified live: firing a signal moved intent 0→30 and status dormant→in_motion, then cleared. Real exclusion fields on Accounts = customer_flag + new_logo_eligible (NOT customer_exclude). Held paid step: wire each signal to its native Clay Signal enrichment and run the first sweep — needs explicit go. Ties to [[clay-tables-not-live-yet]], [[clay-mcp-audiences-disabled]], [[clay-build-audit-jul12]].
