# Daily War Room — 2026-07-16

Window swept: last 24-72 hours (Jul 13-16), with a look back to Jul 7-10 to capture the two new Stars-litigation filings that landed after the last log ran on Jul 6.

Universes scanned: the 32 Tier A+B Star Ratings parents in `StarRatings_Targets_2026_Tiered.csv` (98 contracts). Back-office motion: still no Clay export or named target list in the project folder (ICP remains a straw-man pending the Scott Kemme conversation), so there is no back-office universe to scan against today. Named accounts: Devoted Health (per `Devoted_WholeParent_StrikePlan.md`), no fresh news this cycle.

## Priority 1, Act Today

**Account:** Market-wide (Star Ratings motion), with direct application to universe parents Elevance Health, Humana, UnitedHealth Group, and Centene
**Signal:** The Clover-driven Stars-litigation wave has gone industry-wide in the last week. After Elevance sued CMS on July 1, SCAN Health Plan filed July 7 and Alignment Healthcare filed July 10 (both in federal court in Washington, D.C.), each asking to be moved from 4 to 4.5 stars on the same recalculation logic CMS applied to Clover but withheld from everyone else. SCAN put the figure at ~$125M, Alignment at ~$50M. Coverage crested Jul 13-14 ("'The system is undeniably broken': More insurers sue CMS," Healthcare Dive; Becker's Payer Issues).
**Date / Source:** Filings Jul 1 / Jul 7 / Jul 10, 2026; coverage Jul 13-14, 2026. Healthcare Dive, Becker's Payer Issues, Healthcare Finance News, The Healthcare Labyrinth.
**Classified:** DEFENSIVE. Lead with the industry's own words, not ours: multiple payers are now on record in federal filings calling the Stars system "broken" and quantifying the money at stake. That is their language.
**Why this is Priority 1:** the reframe it hands the copy skills is the strongest one this motion has had. The lawsuits are fights over *ratings math* — which measures CMS may count — not over whether the underlying customer-service scores are good. Per the same coverage, UnitedHealthcare and Centene have won court fights on call-center-related metrics while Humana lost its challenge in that arena. The takeaway to carry into copy: even a plan that wins the math fight still has to actually move its CS measures, and litigation does nothing for that. That is exactly the operational gap this motion sells into.
**Persona:** Persona 1, Stars/Quality (VP/Head of Stars, Quality, or Medicare Quality) and Persona 2, Finance (Medicare segment finance lead or actuary), per `tam-outbound-engine/config/personas.json` under the `qbp_earnings_pressure` route.
**Play:** Star Ratings motion. One-idea candidate: the money everyone is suing over is the same money that sits on the CS line, and the courtroom does not fix a single call-center measure. Localize to each parent's own sub-4.0 CS contracts in the universe file.
**Proof available:** Y, third-party only. The standing UHC $190M secret-shopper CS proof point (per `StarRatings_Targeting_Flags_2026.md` rule 3) pairs with this, cited as UHC's own figure, never as an Intradiem claim, and keep the CY2027 time-stamp caveat (that specific Call Center measure phases out for 2028 Stars). No Intradiem stat goes in Days 1-5 copy.
**Next step + owner:** Hand the reframe to `intradiem-first-draft-engine` then `intradiem-copy-sharpener`. Sharpest single-account application is Humana (below). Sender is Nathan Belfield, not Dallas. Nothing sends today; this is angle-writing, not final copy.

**Account:** Humana Inc. (largest universe parent; sub-4.0 CS contracts incl. H5619 CS 3.1, H5970 CS 3.1, H3533 CS 3.1, H8908 CS 3.3)
**Signal:** Inside the same July litigation coverage, Humana is the named parent that *lost* its legal challenge on call-center-related Stars metrics, while UnitedHealthcare and Centene won theirs. Humana has publicly called its 2026 results "disappointing" (only ~20% of members in 4-star-plus plans, down from 25%) and is banking on "material improvements" in 2027 Stars.
**Date / Source:** July 2026 litigation coverage (Healthcare Dive, "CMS recalculates MA stars"); prior Humana Stars-slip coverage (Healthcare Dive, Modern Healthcare). NOTE on vintage: the Humana court loss itself is established legal posture, not a fresh July event; what is fresh is its role in this week's industry framing.
**Classified:** DEFENSIVE. Lead with the 2027-improvement commitment Humana has already made publicly, not the downgrade.
**Persona:** Persona 1, Stars/Quality (VP Medicare Quality / Stars) primary; Persona 2, Finance secondary.
**Play:** Star Ratings motion, 2028-window one idea. Humana is the cleanest single-account expression of the P1 reframe: the one big parent that cannot litigate its way out of the CS measures and has staked its guidance on actually moving them next cycle. That gap is the wedge.
**Proof available:** Y, same third-party UHC CS proof point, same caveats. Verify anything else against `intradiem-verified-metrics` before it enters copy.
**Next step + owner:** Log the `qbp_earnings_pressure` trigger to the TAM engine (below). Route to first-draft-engine, Nathan sends on the standard 7-9am ET window once copy clears the sharpener. Apply the Molina/market-exit and Cigna-to-HCSC suppression checks in `StarRatings_Targeting_Flags_2026.md` before any Humana contract enters a sequence.

## Priority 2, Prepare This Week

- **Elevance contract-level math is now public (enrichment of the Jul 6 trigger, not a new one).** The July filing detail has surfaced in coverage: one contract covering GA/KY/OH/WI would rise 4→4.5 stars (~$65.8M QBP differential), a Texas contract 3.5→4 (~$36.5M), and three more in CA, IA, and AZ from 3→3.5. This sharpens the existing `elevancehealth.com / qbp_earnings_pressure` trigger already logged Jul 6; it does not create a second one. Worth handing the specific contract geographies to whoever drafts the Elevance touch so the localization is exact (H3447 Anthem HealthKeepers, H4161 Anthem Blue Cross Partnership, H0544 Anthem Blue Cross all sit sub-4.0 CS in the universe file).

## Priority 3, Context

- **Cost/efficiency signals at two universe parents.** Aetna (CVS Health, a Tier A parent) is cutting 313 positions in its small-group business before the end of July; PacificSource (Tier C parent, H3864) is laying off 97 following its Montana and individual-market exit. Neither cut is contact-center or back-office specific, so neither fires outreach alone, but both are cost-mandate context worth a standing watch as the Cost-Mandate motion matures. Source: Becker's Payer Issues, "15 payers cutting jobs 2026."
- **Contact-center WEM consolidation continues, no fresh account move.** Verint has unified its brand post-Calabrio merger (positioning Calabrio WFM as midmarket, Verint as enterprise); AWS acquired NLX (April 2026) to add a no-code layer on Amazon Connect; NICE holds Cognigy (July 2025). No July 2026 account-specific stack change in the universe. Reinforces the standing wedge only: we are the real-time action layer on top of whatever WEM/CCaaS stack a plan just bought, and a fresh WFM purchase is a reason to talk, never a blocker. A new CIO/CTO is a fresh technical buyer with no legacy commitment.
- **Back-office / BPO macro.** Insurance BPO market ~$68.4B in 2026 (claims processing ~38.75% of it), with human-in-the-loop claims models cited as cutting backlogs and costs up to ~50%. No named account or contract signal attached; macro framing for the back-office motion once a target list exists. Source: Mordor Intelligence via BPO trade coverage.

## Accounts with No New Signals

UnitedHealth Group (context only, court wins on CS metrics), Centene Corporation (context only, court wins on CS metrics; April group-president reorg unchanged), CVS Health Corporation (see P3 Aetna cuts), Molina Healthcare (MAPD-exit context unchanged), Health Care Service Corporation, California Physicians' Service, Cambia Health Solutions, CareFirst, Point32Health, Lifetime Healthcare, Athena Healthcare Holdings, Baystate Health, Mass General Brigham, New York City Health and Hospitals Corporation, Visiting Nurse Service of New York, Imperial Health Plan of California, Medica Holding Company, Hawaii Medical Service Association, Community Health Plan of Washington, Guidewell Mutual Holding Corporation, Local Initiative Health Authority for LA County (LA Care), Inland Empire Health Plan, Orange County Health Authority, Presbyterian Healthcare Services, Lumeris Group Holdings Corporation, ATRIO Health Plans, Clever Care Health Plan, Zing Health Consolidator, Devoted Health.

## Triggers Logged to TAM Engine

| domain (best available) | trigger_type | detail | date |
|---|---|---|---|
| humana.com | qbp_earnings_pressure | Named in Jul 2026 Stars-litigation coverage as the parent that lost its call-center-metric court challenge (UHC/Centene won theirs); publicly staked 2027 guidance on "material" Stars improvement it cannot litigate its way to | 2026-07-16 |

Elevance (elevancehealth.com) intentionally NOT re-logged; the Jul 2 `qbp_earnings_pressure` trigger stands and this cycle only enriches it with public contract-level detail. SCAN and Alignment are not in the Tier A+B universe and are not logged as targets; they are market-context only.

## Executive Summary

The one Priority 1 that fired this cycle is the Stars-litigation wave going industry-wide: SCAN sued July 7 and Alignment July 10, joining Elevance, and the trade press is now quoting payers calling the Stars system "broken." The reframe it hands this motion is clean and defensible, because every one of these suits is a fight over ratings math, not over customer-service performance, and even the winners still have to actually move their CS measures. Humana is the sharpest single-account expression of that gap: the largest universe parent, on record having lost its call-center-metric challenge, with 2027 guidance riding on improvement it can only get operationally. Everything else is context: enriched Elevance contract detail, two cost-driven layoff notices at CVS/Aetna and PacificSource, ongoing WEM consolidation with no account move, and BPO macro with no target attached. Back-office motion still has no universe to scan, gated on the Scott Kemme ICP conversation.

## Today's Action List

1. Hand the industry-wide "the courtroom does not fix a CS measure" reframe to `intradiem-first-draft-engine` then `intradiem-copy-sharpener`; sharpest single-account application is Humana, sender Nathan Belfield, standard 7-9am ET window once copy clears.
2. Log the Humana `qbp_earnings_pressure` trigger to the TAM engine's `data/triggers.csv`.
3. Pass the specific Elevance contract geographies (GA/KY/OH/WI, TX, CA/IA/AZ) to whoever drafts the Elevance touch so localization is exact; do not double-log the trigger.
4. Apply `StarRatings_Targeting_Flags_2026.md` suppression checks before any Humana or Elevance contract enters a sequence.
5. No back-office action today; universe remains blocked on the Scott Kemme ICP conversation.
