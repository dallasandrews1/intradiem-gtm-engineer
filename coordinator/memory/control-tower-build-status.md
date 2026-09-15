---
name: control-tower-build-status
description: Jul 18 2026 parser fixes for the control tower assembler; the manual-refresh note is superseded, the launchd job has been loaded and deploying daily since the Sep 15 2026 rebuild.
metadata:
  type: project
  date: 2026-07-18
  source: workspace
---

The control-tower assembler (`build_control_tower.py`) runs and writes `control_tower_state.json`; `Control_Tower.html` fetches that JSON at runtime (no HTML regen needed).

**2026-07-18 — both parser bugs fixed:**
1. **Motion status** — statuses were keyed `cost-mandate_motion`/`back_office_motion` but looked up by canonical `cost_mandate`/`back_office`, so every motion fell to the PLANNED default (WFM row didn't match at all: backtick + `(wb_...)` decoration). Now matches motions by keyword against the asset name and normalizes `**BUILT / NEUTRALIZED**`-style cells. All four motions read BUILT (Stars via an honest fallback since the registry doesn't tabulate it as a table row).
2. **Blockers** — all three ⚠️ markers live inside table cells; the old parser skipped every `|` line (zero collected) and the per-motion filter was always-true. Now extracts from the specific cell, picks the sentence carrying the open signal, drops "found and fixed" resolved notes and "see Functions table" cross-references, and attributes each blocker to the right motion. `fn_email_verified` Send-data-back bug lands on both cost_mandate + wfm_adjacency; golden Duplicate-table blanking hazard surfaces globally; both flagged OPEN. Added an OPEN marker to the HTML Blockers card.

**Cadence (superseded Sep 15 2026):** the launchd job `com.dallasandrews.gtm.controltower` is LOADED and runs `automation/run_control_tower.sh` at 7:30 daily, building, staging and deploying; see [[control-tower-animated-rebuild-sep15]]. Earlier note kept for history: it was a manual refresh until then. Next-session trigger: after Dallas re-stamps the registry post his live WFM-Adjacency Sculptor fix, re-run the tower, do the read-only live Clay verify (safe once he's out of the table), then load the daily job. Snapshot still carries seeded funnel values, a stale/UNKNOWN deliverability gate, and a live credit ledger; zero sends by design. See [[control-tower-contract-jul18]].
