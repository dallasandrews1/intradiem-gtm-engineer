# Daily War Room — 2026-07-06

First run of this skill (no prior log to diff against). Window swept: last 72-96 hours to cover the Jul 4 holiday gap, plus the active Clover Health Stars-litigation thread that is still moving as of this morning.

Universes scanned: the 32 Tier A+B Star Ratings parents in `StarRatings_Targets_2026_Tiered.csv` (98 contracts). Back-office motion: no Clay export or named target list exists yet in the project folder (ICP is still a straw-man per `intradiem-backoffice-icp`, pending the Scott Kemme conversation), so there is no back-office universe to scan against today. Named accounts: Devoted Health (per `Devoted_WholeParent_StrikePlan.md`).

## Priority 1, Act Today

**Account:** Elevance Health, Inc. (parent of Anthem Blue Cross, Anthem HealthKeepers, Anthem Blue Cross Partnership Plan; contracts H3447, H4161, H0544 in the universe)
**Signal:** Elevance sued the U.S. government on July 2, 2026 in the Southern District of Georgia, alleging CMS's recalculation of its Medicare Advantage Star Ratings did not follow a recent court ruling and cost the company $115 million.
**Date / Source:** July 2, 2026. Bob Herman, STAT News, "Elevance sues government over $115 million tied to Medicare Advantage star ratings."
**Classified:** DEFENSIVE. Lead with the fact that Elevance itself is now on record, in a federal filing, saying Stars math is costing it nine figures. That is their language, not ours.
**Persona:** Persona 1, Stars/Quality (VP/Head of Stars, Quality, or Medicare Quality) and Persona 2, Finance (Medicare segment finance lead or actuary). Both are named in `tam-outbound-engine/config/personas.json` and `config/triggers.json` under the `qbp_earnings_pressure` route.
**Play:** Star Ratings motion. `qbp_earnings_pressure` trigger (weight 22, routes finance + cc_ops). One-idea candidate: the company has just quantified, in a court filing, exactly how much money sits on the Stars line. Localize to Elevance's own sub-4.0 contracts in the universe file (H3447 CS 3.3, H4161 CS 2.8, H0544 CS 2.9) and the customer-service measures specifically, since litigation over ratings math does not fix the underlying CS scores.
**Proof available:** Y, the standing third-party CS-addressability proof point (UHC's own $190M secret-shopper Stars case, per `StarRatings_Targeting_Flags_2026.md` rule 3) pairs directly with this signal. Cite it as UHC's stated figure, not an Intradiem claim, and keep the CY2027 time-stamp caveat (that specific Call Center measure is retired for 2028 Stars).
**Next step + owner:** Route to `intradiem-first-draft-engine` then `intradiem-copy-sharpener` today. Sender is Nathan Belfield, not Dallas. Send window tomorrow 7 to 9am ET per the standard cadence.

**Account:** Clover Health Holdings, Inc. (contract H5141 in the universe, Tier A, CS 3.1 / Clin 3.5 / overall 3.5, addressable $49.1M gross)
**Signal:** Following Clover's May 27, 2026 court win (Southern District of Georgia ruled CMS improperly included 20 measures in Clover's 2026 rating), CMS voluntarily recalculated 2027 Quality Bonus Payment ratings across the industry starting June 17, 2026, removing all Part D measures and several disputed Part C measures. Becker's is reporting (within the last several hours as of this morning) that Clover's primary PPO, which covers 97% of its members, has been bumped again following the recalculation, on top of an earlier move from 3.5 to 4.5 stars overall.
**Date / Source:** May 27 to July 6, 2026 (active, developing). Becker's Payer Issues, Healthcare Dive, Seyfarth Shaw, MedCity News.
**Classified:** HOLD, not a send signal yet. This is a data-integrity flag, not a forcing function to message on.
**Why this is Priority 1 without a play attached:** the recalculation removed disputed measures from the overall composite, not necessarily the CS-specific star. Our addressable math for H5141 in `StarRatings_Targets_2026_Tiered.csv` is built on the Oct 8 2025 CMS release and does not yet reflect this recalculation. Messaging Clover on a sub-4.0 CS thesis while their overall rating is mid-recalculation risks a factual error landing in an exec's inbox.
**Next step + owner:** Dallas to manually verify H5141's post-recalculation CS star before any Clover contract enters a sequence. Do not log this as a demand trigger in the TAM engine yet; flag it as a suppression-review item instead. Broader note: any other Tier A/B contract with disputed Part C measures in this universe could be affected by the same June 17 recalculation; a targeted re-verification pass (not a full re-pull, that is the October cycle's job) is worth scoping before the next batch of outreach goes out on marginal contracts.

## Priority 2, Prepare This Week

- **CMS CY2027 final rule, Star Ratings structural overhaul.** Confirmed this week in coverage of the final rule: ten measures removed from Stars, including the call center accessibility measures (foreign language interpreter availability, TTY access), phased out starting with the 2028 Star Ratings. This reinforces, and time-bounds, the existing standing note in `StarRatings_Targeting_Flags_2026.md` rule 3: the UHC $190M proof point must keep citing that specific measure as historical proof under the prior rules, never as still-live money. No new action, but worth a one-line reminder to Nathan and anyone drafting Stars copy this week: don't let the $190M citation drift into present tense.
- **Centene Corporation executive reorg (April 6, 2026, resurfaced in this sweep).** Centene created two new group president roles under CEO Sarah London; Michael Carson now holds Group President, Medicare and Specialty, with expanded oversight of MA, Part D, Duals, and Specialty. Not fresh news, but Centene carries several sub-4.0 Wellcare contracts in the universe (H2775, H5599, H4868, H1416). A reorg at this level often cascades into a Stars/Quality VP change over the following quarter; worth a standing watch rather than action today.

## Priority 3, Context

- **Verint-Calabrio integration continues.** The combined company (post Thoma Bravo acquisition, Dave Rhodes as CEO since February 2026) now holds over 40% of the global WEM market and explicitly markets integration with Genesys, NICE CXone, Five9, and Amazon Connect rather than displacement. No account-specific news this cycle, but it reinforces the standing wedge: a WFM or CCaaS purchase is never a blocker, we sit on top of the stack, and a new CIO/CTO is a fresh technical buyer with no legacy commitment to the old platform.
- **Healthcare BPO market sizing.** General market coverage puts the 2026 healthcare BPO market at roughly $423 to $510 billion, growing toward $700B plus by 2031, with claims processing and revenue cycle as the largest categories. No named account or contract signal attached; useful only as macro framing for the back-office motion once a target list exists.

## Accounts with No New Signals

Humana Inc., CVS Health Corporation, UnitedHealth Group, Molina Healthcare (MAPD-exit context unchanged since the June 30 flags-file update, no new development this week), Health Care Service Corporation, California Physicians' Service, Cambia Health Solutions, CareFirst, Point32Health, Lifetime Healthcare, Athena Healthcare Holdings, Baystate Health, Mass General Brigham, New York City Health and Hospitals Corporation, Visiting Nurse Service of New York, Imperial Health Plan of California, Medica Holding Company, Hawaii Medical Service Association, Community Health Plan of Washington, Guidewell Mutual Holding Corporation, Local Initiative Health Authority for LA County (LA Care), Inland Empire Health Plan, Orange County Health Authority, Presbyterian Healthcare Services, Lumeris Group Holdings Corporation, ATRIO Health Plans, Clever Care Health Plan, Zing Health Consolidator, Devoted Health (per `Devoted_WholeParent_StrikePlan.md`, no fresh news this cycle beyond what that strike plan already carries).

## Triggers Logged to TAM Engine

| domain (best available) | trigger_type | detail | date |
|---|---|---|---|
| elevancehealth.com | qbp_earnings_pressure | Elevance sued CMS Jul 2 2026 alleging Stars-ratings recalculation math cost it $115M, Southern District of Georgia | 2026-07-02 |

Clover Health (H5141) intentionally NOT logged as a trigger this cycle; it is a suppression-review flag, not a demand signal, until the post-recalculation CS star is confirmed.

## Executive Summary

One real Priority 1 fired this cycle: Elevance has now put a $115 million number on Stars-ratings pressure in a federal court filing, which is about as clean a DEFENSIVE forcing function as this motion gets. A second item, Clover Health's ongoing rating recalculation, is Priority 1 for review, not for outreach, since it could change our own addressable math on that contract. Everything else this week is context: a CMS rule confirming the CS-measure time-stamp we already track, a stale-but-relevant Centene reorg, and industry-level WFM and BPO market news with no account attached. Back-office motion has no universe to scan yet, that gap sits with the Scott Kemme ICP conversation, not with this sweep.

## Today's Action List

1. Run Elevance through `intradiem-first-draft-engine` then `intradiem-copy-sharpener`, sender Nathan Belfield, target Stars/Quality and Finance personas, send window tomorrow 7 to 9am ET.
2. Manually verify Clover Health's H5141 post-recalculation CS star before it re-enters any sequence; hold all Clover outreach until confirmed.
3. Scope a targeted (not full) re-verification pass on other Tier A/B contracts with disputed Part C measures affected by the June 17 2026 CMS recalculation.
4. No back-office action today; back-office universe remains blocked on the ICP conversation with Scott Kemme.
