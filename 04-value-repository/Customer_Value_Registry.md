# Customer Value Registry (Zuar / Greenlight-sourced)
**Owner: Dallas Andrews. Created Jul 17 2026. Governed by `Intradiem_Value_Repository.md` (same folder).**
Source: Intradiem Greenlight/Zuar portal (portal.intradiem.com). Data pull dated **Jul 17 2026**. Refresh by re-exporting from Greenlight; stamp the new pull date here.

This registry holds **per-account CTO figures**. CTO = **"Cost Taken Out"** (cost savings attributable to Intradiem automation), verified against the Zuar export dated Jul 17 2026. This supersedes any earlier "Capacity/Time Optimized" wording. It is the numeric layer behind the Install-Base and Back-Office motions. The Value Repository governs *how* these numbers may be used; this file *holds* them.

## CTO measure definition (read before reading any number below)
CTO = "Cost Taken Out," the cost savings attributable to Intradiem automation. In Product's enhancement-prioritization formula it is the numerator term (estimated cost savings if an enhancement were implemented), alongside customer demand and effort reduction. Three portal forms:
- **TOTAL CTO** (`total_cto_v2_sum`) = a raw magnitude of cost taken out (the "CTO" magnitude column below; e.g. UnitedHealth 24.5M, CVS 15.1M over the period). It is NOT an "x" multiple, and it is NOT the sum of the per-source CTO rows (TOTAL runs materially larger than the broken-out sources).
- **CTO Multiple** (`cto_over_ab_fixed_ratio`) = TOTAL CTO / AB Fixed, the derived "x" (the "CTO Multiple" column below). Verified: CVS 17.5x, Aetna 12.8x, Humana 5.81x; portfolio mean ~4.5x, median ~4.2x; 45/63 accounts at or above 2.1x, 25/63 at or above 5x; 8/63 stalled at 0x.
- **CTO5** = a 0-to-5 prioritization score, bucketed 0 -> 0, 1 -> 0.1-0.5x, 2 -> 0.6-1.0x, 3 -> 1.1-1.5x, 4 -> 1.6-2.0x, 5 -> 2.1x and up. Raw `cto5_calc_daily_bi` is stored uncapped; the strict 0-to-5 bucket is applied in the prioritization layer.

Source decomposition of CTO: Coaching, Efficiency, Handle Time, UPT Alerts, UPT Reports, Burnout, Staffing, Adherence, Break/Lunch, TM.

**Guardrails (do NOT let these get miswritten):**
- Never define "Total CTO = sum of individual CTO multiples (units = x)." That is an enhancement-prioritization abstraction, not the portal measure. Never sum the portal per-account multiples into a portfolio "x."
- The CTO Multiple's denominator is AB Fixed, not the licensed-agent count.
- CTO means cost taken out, but the raw magnitude's exact unit (true dollars vs. an internal cost index) is NOT confirmed. Do not publish a hard "$X saved" from a per-account CTO figure until confirmed. TOTAL CTO does NOT reconcile to the $529.6M all-time company savings figure (different measure). Humana's 5.81x reconciles to its public "~2 hours of capacity per agent per month," the only cleared external framing.

## Non-negotiable usage rules (read before citing anything here)
1. **Every figure below defaults to tier `CV-INTERNAL`** — usable to rank, prioritize, and decide who to approach. **It does not go into any prospect-facing copy in this state.**
2. **Raw-magnitude unit is UNCONFIRMED.** CTO = Cost Taken Out (cost savings), but the TOTAL CTO magnitude's exact unit (true dollars vs. an internal cost index) is not confirmed in Greenlight, and the all-time Zuar rollup does **not** reconcile to the $529.6M company savings figure (different measure). **No unit-bearing phrasing** ("$X saved," "Y hours returned," "Z% efficiency") may ship until the unit is confirmed. Until then these are relative-magnitude signals only.
3. **1:1 LOCK.** Once a figure is promoted to `CV-1:1` (see repo), it may be referenced **only in outreach/materials directed back to that same customer's own buyers.** Never to a third party, never blended across accounts, never public.
4. **Promotion to `CV-1:many`** (public/other-logo/deck use) requires named-reference or logo approval + marketing sign-off, at which point the claim moves into the Value Repository VERIFIED 1:many table. Today only Humana qualifies.
5. **STALLED accounts are not proof accounts.** Zero-CTO-with-a-live-agent-base rows are a CS save / re-onboard signal, not a value story. Never frame them as outcomes.

## Field notes
- **CTO** column = TOTAL CTO (`total_cto_v2_sum`), the raw magnitude of cost taken out (per parents-only export, Jul 17 2026). Raw-magnitude unit UNCONFIRMED (dollars vs. internal cost index). NOT the sum of the per-source CTO rows.
- **CTO Multiple** column = `cto_over_ab_fixed_ratio` = TOTAL CTO / AB Fixed, the derived "x." NOT CTO divided by the licensed-agent count. A low multiple on a real agent base = under-realization / expansion or save signal. (Values below are rounded to one decimal; raw ratios drive the portfolio counts in the definition section above.)
- `maturity` / `platform_score` = Greenlight Maturity model (Beginning→Modern; score 0–10).
- Success Manager = the internal owner to route a warm intro / reference request through.

## Registry
| Account | Success Mgr | TOTAL CTO (raw magnitude, unit UNCONFIRMED) | CTO Multiple (x) | Maturity | Platform Score | Industry | Tier / Status |
|---|---|---|---|---|---|---|---|
| UnitedHealth Group (UHG) | Julia LaGrange | 24,495,658 | 6.8× | Beginning | 4.4 | Health Insurance | CV-INTERNAL |
| CVS Health | Kira Guzman | 15,133,640 | 17.5× | Modern | 7.4 | Health Insurance | CV-INTERNAL |
| JPMorgan Chase | Kira Guzman | 14,370,894 | 7.4× | Modern | 7.6 | Financial Services | CV-INTERNAL |
| Aetna Inc | Kira Guzman | 10,451,945 | 12.8× | Modern | 8.1 | Health Insurance | CV-INTERNAL |
| Kaiser Permanente (KPIT) | Nate Jones | 8,971,355 | 7.2× | Evolving | 9.2 | Healthcare | CV-INTERNAL |
| Charter Communications | Amanda Shupe | 7,358,689 | 8.7× | Modern | 8.1 | Technology & Communications | CV-INTERNAL |
| AT&T Enterprise Group | DeAndra Scheidt | 5,989,525 | 7.8× | Evolving | 5.8 | Technology & Communications | CV-INTERNAL |
| Cigna Corporation | Christine Gotleib | 4,774,160 | 3.1× | Modern | 7.0 | Health Insurance | CV-INTERNAL |
| Elevance Health | DeAndra Scheidt | 3,903,735 | 10.1× | Evolving | 6.5 | Health Insurance | CV-INTERNAL |
| Health Care Service Corporation | Amy Johnson | 3,540,170 | 6.6× | Modern | 7.4 | Health Insurance | CV-INTERNAL |
| Synchrony Financial | Lisa Vidal | 3,034,460 | 5.9× | Modern | 7.1 | Financial Services | CV-INTERNAL |
| Citicorp Credit Services | Amanda Shupe | 2,279,054 | 3.2× | Beginning | 3.1 | Financial Services | CV-INTERNAL |
| CENTRICA PLC | Scott McHaffie | 1,876,064 | 5.0× | Modern | 5.8 | Utilities | CV-INTERNAL |
| American Express Global Business Travel | DeAndra Scheidt | 1,824,720 | 5.8× | Modern | 7.5 | Travel | CV-INTERNAL |
| Wells Fargo | Amanda Shupe | 1,752,100 | 5.0× | Maturing | 3.9 | Financial Services | CV-INTERNAL |
| Rogers Communications Canada | Christine Gotleib | 1,699,255 | 3.9× | Maturing | 5.0 | Technology & Communications | CV-INTERNAL |
| Cox Enterprises Inc | Chris McCoy | 1,691,308 | 6.0× | Modern | 7.7 | Technology & Communications | CV-INTERNAL |
| Canadian Imperial Bank Of Commerce (CIBC) | Lisa Vidal | 1,478,583 | 5.3× | Maturing | 4.4 | Financial Services | CV-INTERNAL |
| Humana | Christine Gotleib | 1,403,278 | 5.8× | Modern | 8.1 | Health Insurance | CV-INTERNAL |
| Assurant | DeAndra Scheidt | 1,303,269 | 10.9× | Beginning | 5.0 | Home & Auto Insurance | CV-INTERNAL |
| Liberty Global | Scott McHaffie | 1,239,458 | 2.9× | Beginning | 5.2 | Technology & Communications | CV-INTERNAL |
| MetLife | Kelsey Ruml | 1,125,946 | 7.6× | Modern | 8.2 | Financial Services | CV-INTERNAL |
| Goldman Sachs | Kira Guzman | 1,112,333 | 7.4× | Maturing | 5.2 | Financial Services | CV-INTERNAL |
| Exelon Corporation | Chris McCoy | 925,381 | 7.4× | Beginning | 4.7 | Utilities | CV-INTERNAL |
| PNC Financial | Lisa Vidal | 873,902 | 4.1× | Maturing | 4.3 | Financial Services | CV-INTERNAL |
| Royal Bank of Canada (RBC) | Kelsey Ruml | 847,005 | 2.6× | Beginning | 6.9 | Financial Services | CV-INTERNAL |
| The Northwestern Mutual Life Insurance Company | Amy Johnson | 806,186 | 6.0× | Modern | 8.1 | Financial Services | CV-INTERNAL |
| Anthology | Nate Jones | 711,925 | 9.7× | Evolving | 6.0 | Other | CV-INTERNAL |
| Capital Group | Amy Johnson | 708,035 | 5.0× | — | — | — | CV-INTERNAL |
| Edward Jones | Lisa Vidal | 508,498 | 4.0× | Beginning | 10.0 | Financial Services | CV-INTERNAL |
| McKesson Inc | Amy Johnson | 427,858 | 3.3× | Modern | 8.4 | Healthcare | CV-INTERNAL |
| Auto & General Insurance Company | Scott McHaffie | 331,472 | 4.5× | Beginning | 5.0 | Home & Auto Insurance | CV-INTERNAL |
| AXA (UK) | Scott McHaffie | 274,517 | 3.4× | Maturing | 5.6 | Home & Auto Insurance | CV-INTERNAL |
| Progressive Leasing | Amy Johnson | 231,617 | 7.5× | Beginning | 4.2 | Financial Services | CV-INTERNAL |
| Ameriprise Financial | Chris McCoy | 227,009 | 4.2× | Maturing | 5.1 | Financial Services | CV-INTERNAL |
| DIRECTV | DeAndra Scheidt | 222,759 | 4.8× | — | — | — | CV-INTERNAL |
| TD Bank Group | Lisa Vidal | 216,028 | 2.8× | — | — | — | CV-INTERNAL |
| Molina Healthcare | Nate Jones | 195,510 | 1.1× | — | — | — | CV-INTERNAL |
| The Home Depot | DeAndra Scheidt | 173,078 | 1.7× | Beginning | 6.4 | Consumer-Focused Industries | CV-INTERNAL |
| Cleveland Clinic | Amy Johnson | 171,314 | 1.9× | Evolving | 5.4 | Healthcare | CV-INTERNAL |
| Prudential Financial | Amy Johnson | 168,691 | 2.0× | Beginning | 4.0 | Financial Services | CV-INTERNAL |
| Zurich Insurance Group | Amanda Shupe | 159,518 | 4.3× | Beginning | 5.5 | Home & Auto Insurance | CV-INTERNAL |
| Vibrant Emotional Health | Amy Johnson | 159,433 | 5.1× | Modern | 8.0 | Healthcare | CV-INTERNAL |
| Dominion Energy | Chris McCoy | 158,006 | 8.1× | — | — | — | CV-INTERNAL |
| AAA - National HQ | Lisa Vidal | 149,791 | 6.9× | Evolving | 7.7 | Home & Auto Insurance | CV-INTERNAL |
| The Travelers Companies | Kelsey Ruml | 148,408 | 1.6× | Beginning | 3.9 | Home & Auto Insurance | CV-INTERNAL |
| Social Finance (SoFi) | Amanda Shupe | 137,678 | 1.8× | Beginning | 2.7 | Financial Services | CV-INTERNAL |
| VitalityHealth | Scott McHaffie | 137,674 | 1.5× | Maturing | 2.7 | Health Insurance | CV-INTERNAL |
| Snap Finance LLC | Amanda Shupe | 135,169 | 2.0× | Beginning | 3.2 | Financial Services | CV-INTERNAL |
| Edison International | Chris McCoy | 134,167 | 4.1× | Modern | 6.9 | Utilities | CV-INTERNAL |
| Guardian Life | Amy Johnson | 110,300 | 3.1× | Modern | 7.3 | Financial Services | CV-INTERNAL |
| AccorHotels | DeAndra Scheidt | 66,039 | 2.8× | Beginning | 4.7 | Travel | CV-INTERNAL |
| Foundever (Sitel) | Amanda Shupe | 15,007 | 1.0× | Beginning | 2.3 | Professional Services | CV-INTERNAL |
| Amica Mutual | Kelsey Ruml | 10,695 | 1.0× | — | — | — | CV-INTERNAL |
| SCAN Health Plan | Kelsey Ruml | 151 | 0.0× | — | — | — | CV-INTERNAL |
| Baylor Scott & White Health | Kelsey Ruml | 0 | 0.0× | — | — | — | STALLED — no realized value; save/re-onboard signal, NOT a proof account |
| PG&E Corporation | Chris McCoy | 0 | 0.0× | Modern | 7.7 | Utilities | STALLED — no realized value; save/re-onboard signal, NOT a proof account |
| Royal Automobile Club Victoria (RACV) | DeAndra Scheidt | 0 | 0.0× | — | — | — | STALLED — no realized value; save/re-onboard signal, NOT a proof account |
| Capita | Scott McHaffie | 0 | 0.0× | — | — | — | STALLED — no realized value; save/re-onboard signal, NOT a proof account |
| ADT | Christine Gotleib | 0 | 0.0× | Beginning | 4.6 | Other | STALLED — no realized value; save/re-onboard signal, NOT a proof account |
| US Bancorp | — | 0 | 0.0× | — | — | — | STALLED — no realized value; save/re-onboard signal, NOT a proof account |
| Duke Energy | Chris McCoy | 0 | 0.0× | — | — | — | STALLED — no realized value; save/re-onboard signal, NOT a proof account |
| Illumifin | — | 0 | 0.0× | — | — | — | STALLED — no realized value; save/re-onboard signal, NOT a proof account |

**OPEN DATA FLAG (Aetna TOTAL CTO):** a Jul 17 2026 correction note cited Aetna TOTAL CTO at 15.5M, but this registry holds 10,451,945 (10.5M). UnitedHealth (24.5M) and CVS (15.1M) matched the correction note exactly, and Aetna's 12.8x multiple matches; only the Aetna magnitude conflicts. Left at 10,451,945 pending a direct re-check against the Zuar export. Do NOT cite Aetna's TOTAL CTO magnitude until reconciled. Also confirm whether the magnitude column is a trailing-90-day sum or a full-period `total_cto_v2_sum`; the two labels appeared inconsistently in prior notes.

_63 accounts. 55 with realized value (CV-INTERNAL), 8 STALLED. Regenerate from the Greenlight parents-only + maturity exports on each refresh._
