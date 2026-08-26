# Daily War Room — 2026-07-17

Window swept: last 24-72 hours (Jul 14-17), with a look-back to Jul 1-10 to confirm the carried Stars-litigation thread has not moved. Today is a Friday and the first day *after* the Q2 earnings stretch opened.

Universes scanned: the 32 Tier A+B Star Ratings parents in `StarRatings_Targets_2026_Tiered.csv` (98 contracts). Back-office motion: a target universe now exists (`BackOffice_Target_Universe_v1.csv`), so it is scanned this cycle for the first time — but the top-priority rows in it are `install_base=TRUE` (Capita, Foundever, Ameriprise, CIBC, etc.), and per this skill's canon, install-base accounts are never messaged from the war room; any signal on them routes to the signal engine (AE/CSM), not outbound. Named accounts: Devoted Health (per `Devoted_WholeParent_StrikePlan.md`), no fresh news this cycle. Note: the "back-office motion is blocked on the Scott Kemme ICP conversation" caveat carried in prior logs is retired — Scott is out and the back-office ICP is now Dallas-owned/TBD, not gated on him.

## Priority 1, Act Today

**No fresh Priority 1 fired in this window.** This is the ninth consecutive cycle with zero fresh outbound Priority 1 (07-13 through 07-16 all logged the same). Both live Priority 1 threads are carried, not re-fired:

- **Stars-litigation wave (market-wide, DEFENSIVE).** Held flat at three plaintiffs and ~$290M publicly priced: Elevance (~$115M, filed Jul 1, S.D. Ga.), SCAN (~$125M, Jul 7, D.D.C.), Alignment (~$50M, Jul 10, D.D.C.), all seeking the same Clover recalculation logic CMS withheld from the industry. No new entrant and no new ruling Jul 14-17. The pre-staged `qbp_earnings_pressure` reframe ("the courtroom does not fix a single CS measure") is unchanged and ready; nothing new to send on today.
- **Humana `qbp_earnings_pressure`** (logged Jul 16): carried. Humana reports Jul 29, which is the forcing moment for that thread. No fresh Humana development this window.

## Priority 2, Prepare This Week

**Account:** UnitedHealth Group, Inc. (Tier A parent; universe contracts incl. H3805 CS 3.4, H8768 CS 3.3, H3418 CS 3.0, H0755 CS 3.8)
**Signal:** UnitedHealth reported Q2 2026 earnings on Jul 16 (yesterday, in-window) and *beat*: adjusted EPS $6.38 vs $4.08 a year earlier, medical care ratio 86.7% (down from 89.4%), operating earnings up 55% to $8B, and it *raised* full-year 2026 adjusted-EPS guidance to $19.50-$20.00 from a prior floor of $18.25. Management said Medicare cost trends, while still above historical levels, are running *below* the company's own expectations, and attributed the better Medicare trend to "benefit design, care management models and network curation."
**Date / Source:** Reported Jul 16, 2026. CNBC "UnitedHealth Group (UNH) earnings Q2 2026"; Yahoo Finance "UnitedHealth Group Q2 Earnings Call Highlights"; Investing.com earnings-call transcript.
**Classified:** PROUD, and that is the point for us — this is a parent *outperforming* on MA cost, not one bleeding on it. It is the wrong account to lead a DEFENSIVE Stars angle on right now.
**Why this is P2 not P1:** UNH's print does not hit the Tier 1 triggers (no earnings miss on MA margins, no Stars/quality-pressure language on the call). What it does is *tune the whole stretch*: the first Q2 print of the season came in positive and softened the "every MA plan is collapsing on cost" macro framing that the litigation wave had been amplifying. The pre-staged `qbp_earnings_pressure` variants should not lead with a market-wide "MA margins are cratering" premise into the back half of the earnings stretch, because the tape's opening data point contradicts it. The durable, defensible premise stays account-specific: a given contract's own sub-4.0 CS star and the QBP dollars sitting on it, not a macro bleed narrative.
**Persona:** Persona 1, Stars/Quality; Persona 2, Finance — unchanged, per `tam-outbound-engine/config/personas.json` under `qbp_earnings_pressure`.
**Play:** Star Ratings motion. Sharper single-account DEFENSIVE candidate is **Elevance (reports Jul 22)** — it is the parent that has itself put $115M on the Stars line in a federal filing, which is a cleaner forcing function than any UNH angle. Stage Elevance as the lead earnings-reaction touch when its print lands, not UNH.
**Proof available:** Y, third-party only — the standing UHC $190M secret-shopper CS proof point (`StarRatings_Targeting_Flags_2026.md` rule 3), cited as UHC's own figure, never Intradiem's, keeping the CY2027 time-stamp caveat (that Call Center measure phases out for 2028 Stars). No Intradiem stat in Days 1-5.
**Next step + owner:** No send today. Tune the pre-staged earnings-reaction variants PROUD-aware (drop any macro "MA collapse" premise); hold the sharpest DEFENSIVE application for Elevance on/after Jul 22, sender Nathan Belfield, standard 7-9am ET window once copy clears the sharpener. Remaining stretch: Elevance Jul 22, Molina Jul 22-23, Centene Jul 28, Humana Jul 29, CVS Aug 5.

## Priority 3, Context

- **Molina reaffirmed 2026 guidance (reports Jul 22-23).** Unlike UNH and Elevance, Molina has *reaffirmed* (not raised) its FY2026 outlook — at least $5 adjusted EPS, ~$42B premium revenue — calling it "prudent" given a still-challenging cost environment and a 6% expected Medicaid membership decline (CA, IL, NY, TX). No fresh event this window; this is preview context for its Jul 22-23 print. Molina's MAPD-exit suppression rule in `StarRatings_Targeting_Flags_2026.md` still applies before any Molina contract enters a sequence. Source: Fierce Healthcare, Healthcare Dive.
- **Capita redundancy consultation (back-office universe, INSTALL-BASE — do not message from here).** CWU reports ~265 Capita workers entered a 45-day redundancy consultation. Capita is `bo_priority 1` in `BackOffice_Target_Universe_v1.csv` but flagged `install_base=TRUE`, so this is not a war-room outbound signal — it routes to the signal engine (AE/CSM), which owns install-base motion. Logged here only so it is not mistaken for a net-new outbound opening. Source: CWU union notice.
- **Contact-center WEM / CCaaS consolidation — no fresh account move.** No July 2026 stack change at any universe parent this window. Standing wedge unchanged: we are the real-time action layer on top of whatever WEM/CCaaS stack a plan just bought; a fresh WFM purchase is a reason to talk, never a blocker; a new CIO/CTO is a fresh technical buyer with no legacy commitment.

## Accounts with No New Signals

Humana Inc. (carried P1 thread, reports Jul 29, no fresh development), Elevance Health (carried litigation P1, reports Jul 22), Centene Corporation (voluntary-separation program carried from prior logs, involuntary number still unconfirmed pending Jul 28 print), CVS Health Corporation (Aetna 313-role cut carried, reports Aug 5), Molina Healthcare (see P3), Health Care Service Corporation, California Physicians' Service, Cambia Health Solutions, CareFirst, Point32Health, Lifetime Healthcare, Athena Healthcare Holdings, Baystate Health, Mass General Brigham, New York City Health and Hospitals Corporation, Visiting Nurse Service of New York, Imperial Health Plan of California, Medica Holding Company, Hawaii Medical Service Association, Community Health Plan of Washington, Guidewell Mutual Holding Corporation, Local Initiative Health Authority for LA County (LA Care), Inland Empire Health Plan, Orange County Health Authority, Presbyterian Healthcare Services, Lumeris Group Holdings Corporation, ATRIO Health Plans, Clever Care Health Plan, Zing Health Consolidator, Devoted Health.

## Triggers Logged to TAM Engine

| domain (best available) | trigger_type | detail | date |
|---|---|---|---|
| (none this cycle) | — | UnitedHealth's Jul 16 Q2 beat is not a demand trigger — it is the opposite (a parent outperforming on MA cost), so it is intentionally NOT logged. No fresh demand trigger fired Jul 14-17. | — |

Carried triggers stand: `elevancehealth.com / qbp_earnings_pressure` (Jul 2) and `humana.com / qbp_earnings_pressure` (Jul 16), neither re-logged. SCAN and Alignment remain market-context only (not in the Tier A+B universe).

## Executive Summary

Ninth straight cycle with zero fresh outbound Priority 1. The one genuinely new, dated fact this window is UnitedHealth's Jul 16 Q2 earnings beat: MA cost trend running below the company's own plan and raised full-year guidance. That is a PROUD print, and its real effect on this motion is a tuning one — the opening data point of the Q2 stretch contradicts a market-wide "MA margins are collapsing" premise, so the pre-staged earnings-reaction angles should stay account-specific (a contract's own sub-4.0 CS star and its QBP dollars) rather than lean on a macro bleed narrative. The sharpest DEFENSIVE application is not UNH but Elevance, which reports Jul 22 and has itself put $115M on the Stars line in a federal filing. Everything else is carried: the litigation wave held flat at three plaintiffs / ~$290M, Molina reaffirmed ahead of its Jul 22-23 print, and a Capita redundancy consultation is install-base (routes to the signal engine, not outbound).

## Today's Action List

1. Tune the pre-staged `qbp_earnings_pressure` earnings-reaction variants PROUD-aware in light of UNH's Jul 16 beat: drop any market-wide "MA collapse" premise; keep the premise account-specific (own CS star + QBP dollars). No send today.
2. Stage **Elevance** as the sharpest DEFENSIVE earnings-reaction touch for on/after its Jul 22 print (its own $115M filing is the forcing function); Nathan Belfield sends, standard 7-9am ET window once copy clears the sharpener.
3. Hold the balance of the stretch on the calendar: Elevance Jul 22, Molina Jul 22-23 (apply MAPD-exit suppression), Centene Jul 28, Humana Jul 29, CVS Aug 5.
4. Do not treat the Capita redundancy consultation as an outbound opening — it is install-base; note for the signal engine only.
5. No new demand trigger to log this cycle.
