---
name: cto-definition-cost-taken-out
description: "CTO = Cost Taken Out (cost savings), the corrected Greenlight/Zuar metric definition; supersedes the old Capacity/Time Optimized reading"
metadata:
  type: reference
---

**CTO = "Cost Taken Out"** per customer: the cost savings attributable to Intradiem automation. Verified against the Zuar export dated Jul 17 2026. This SUPERSEDES the earlier (wrong) reading that had CTO as "Capacity/Time Optimized" / "minutes of optimized agent time" (that inference lived in the verified-metrics skill until Jul 18 2026 and is now corrected). In Product's enhancement-prioritization formula CTO is the numerator term (estimated cost savings if an enhancement were built), alongside customer demand and effort reduction.

Three portal forms:
- **TOTAL CTO** (`total_cto_v2_sum`): raw magnitude of cost taken out (e.g. UnitedHealth 24.5M, CVS 15.1M). NOT an "x" multiple; NOT the sum of the per-source rows (TOTAL runs materially larger).
- **CTO Multiple** (`cto_over_ab_fixed_ratio`): TOTAL CTO / AB Fixed = the derived "x." CVS 17.5x, Aetna 12.8x, Humana 5.81x; portfolio mean ~4.5x, median ~4.2x; 45/63 >= 2.1x, 25/63 >= 5x, 8/63 stalled at 0x. Denominator is AB Fixed, NOT the licensed-agent count.
- **CTO5**: 0-5 prioritization score, bucketed (5 = 2.1x+). Raw `cto5_calc_daily_bi` stored uncapped; strict 0-5 bucket applied in the prioritization layer.

Source decomposition: Coaching, Efficiency, Handle Time, UPT Alerts, UPT Reports, Burnout, Staffing, Adherence, Break/Lunch, TM.

**Guardrails:** Never define "Total CTO = sum of individual CTO multiples (units=x)" (that is an enhancement-prioritization abstraction, not the portal measure); never sum portal per-account multiples into a portfolio "x." Unit caution: CTO is cost, but the raw magnitude's exact unit (true dollars vs internal cost index) is NOT confirmed in Greenlight, so no hard "$X saved" from a per-account CTO until confirmed. TOTAL CTO does NOT reconcile to the $529.6M all-time company savings figure. Humana's 5.81x reconciles to its public "~2 hours of capacity per agent per month," the only cleared external framing.

Applied and kept in sync Jul 18 2026 across FOUR copies of `intradiem-verified-metrics/SKILL.md` (repo canonical, `~/.claude/skills` global mirror, `coordinator/.claude/skills`, `greenlight-pack/skills-wave1`) plus `04-value-repository/Intradiem_Value_Repository.md` and `04-value-repository/Customer_Value_Registry.md`. All four SKILL.md copies are byte-identical (131 lines); the repo copy is canonical and the other three must be re-synced from it after any edit. The `coordinator/.claude/skills` copy had been a stale Jul 9 pre-CTO version (103 lines) until this sync. The registry Ratio column was renamed CTO Multiple and its definition corrected (was wrongly "CTO / agent-base"). See [[surface-split-rule]].

**Window question RESOLVED:** the registry CTO column is full-period `total_cto_v2_sum` (parents-only export, Jul 17 2026), the same measure as the definition examples — NOT a trailing-90-day sum.

**OPEN FLAG (Aetna magnitude) — still unreconciled:** a Jul 17 correction note / ground-truth cited Aetna TOTAL CTO at 15.5M, but the registry export cell holds 10,451,945 (10.5M); both claim the same Jul 17 Zuar export. UHG (24,495,658→24.5M) and CVS (15,133,640→15.1M) match their definition examples exactly; Aetna is the only mismatch, and the multiple-consistency check leans toward 10.5M (12.8x on 10.45M implies ~817K AB Fixed, next to CVS's ~865K; on 15.5M it would imply ~1.21M, unexplained). Jul 18: Dallas deferred the call to me; I HELD — Aetna is kept OUT of the definition example lists (examples now carry only UHG 24.5M + CVS 15.1M), the registry row stays at 10,451,945, and the registry DO-NOT-CITE flag on Aetna's magnitude stands. Reconcile 15.5M vs 10.45M against the export before Aetna's TOTAL CTO magnitude is cited anywhere. Aetna's 12.8x multiple is unaffected.
