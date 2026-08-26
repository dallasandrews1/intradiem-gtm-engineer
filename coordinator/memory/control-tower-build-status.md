---
name: control-tower-build-status
description: Verified status of the GTM control tower build; parser bugs fixed 2026-07-18, refresh stays manual until registry re-stamp.
metadata:
  type: project
  date: 2026-07-18
  source: workspace
---

The control-tower assembler (`build_control_tower.py`) runs and writes `control_tower_state.json`; `Control_Tower.html` fetches that JSON at runtime (no HTML regen needed).

**2026-07-18 — both parser bugs fixed:**
1. **Motion status** — statuses were keyed `cost-mandate_motion`/`back_office_motion` but looked up by canonical `cost_mandate`/`back_office`, so every motion fell to the PLANNED default (WFM row didn't match at all: backtick + `(wb_...)` decoration). Now matches motions by keyword against the asset name and normalizes `**BUILT / NEUTRALIZED**`-style cells. All four motions read BUILT (Stars via an honest fallback since the registry doesn't tabulate it as a table row).
2. **Blockers** — all three ⚠️ markers live inside table cells; the old parser skipped every `|` line (zero collected) and the per-motion filter was always-true. Now extracts from the specific cell, picks the sentence carrying the open signal, drops "found and fixed" resolved notes and "see Functions table" cross-references, and attributes each blocker to the right motion. `fn_email_verified` Send-data-back bug lands on both cost_mandate + wfm_adjacency; golden Duplicate-table blanking hazard surfaces globally; both flagged OPEN. Added an OPEN marker to the HTML Blockers card.

**Cadence:** manual refresh (`automation/run_control_tower.sh`) for now. The launchd job (`automation/com.dallasandrews.gtm.controltower.plist`, 7:30 AM daily) exists but is NOT loaded. Next-session trigger: after Dallas re-stamps the registry post his live WFM-Adjacency Sculptor fix, re-run the tower, do the read-only live Clay verify (safe once he's out of the table), then load the daily job. Snapshot still carries seeded funnel values, a stale/UNKNOWN deliverability gate, and a live credit ledger; zero sends by design. See [[control-tower-contract-jul18]].
