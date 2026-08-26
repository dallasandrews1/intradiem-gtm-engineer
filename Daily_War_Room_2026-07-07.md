# Daily War Room, 2026-07-07

Window swept: last 24-72 hours (Jul 4 to Jul 7), plus follow-through on the two active threads carried from the Jul 6 run (Elevance suit, Clover recalculation). Sender for all angle notes: Nathan Belfield.

Universes scanned: the 32 Tier A+B Star Ratings parents in `StarRatings_Targets_2026_Tiered.csv` (98 contracts). Back-office motion: still no Clay export or named target list in the project folder (ICP remains a straw-man pending the Scott Kemme conversation per `intradiem-backoffice-icp`), so there is no back-office universe to scan against today. Named accounts: Devoted Health (per `Devoted_WholeParent_StrikePlan.md`), no fresh news this cycle.

## Priority 1, Act Today

**Account:** Centene Corporation (parent of Wellcare; sub-4.0 A/B contracts in the universe include H2775, H5599, H4868, H1416)
**Signal:** Centene opened a voluntary separation program to most of its ~61,000 employees on June 15; at least some recipients were told to decide by July 2, which just closed inside this window. Company guidance ties the move to membership loss (Q1 total down 6% year over year to 26.3M, ACA down ~2M) and it has signaled that involuntary layoffs could follow if voluntary exits miss target. Trade coverage explicitly links payer workforce cuts this cycle to Medicare Advantage pay pressure and Star Ratings. This converges with the April 6 Centene executive reorg already on standing watch (Michael Carson now Group President, Medicare and Specialty).
**Date / Source:** June 15 to July 2, 2026 (buyout decision window just closed; layoff decisions being made now). Bloomberg, Healthcare Dive, Becker's Payer Issues, Modern Healthcare ("Centene, UnitedHealth layoffs stem from Medicare Advantage pay cuts").
**Classified:** DEFENSIVE. Lead with the situation Centene has already put on the public record, that it is being forced to take cost out of the workforce, not with any downgrade language. The angle is about protecting throughput and service levels through a headcount reduction, not about their ratings.
**Persona:** Persona 2, Finance/Ops cost owner (Medicare segment finance or VP/SVP Operations) as the primary, with the Stars/Quality owner as the secondary thread. The buyout is a cost-and-capacity story first, a quality story second.
**Play:** Star Ratings motion with a workforce-cost wedge. Trigger `cost_mandate` (weight 24). One-idea candidate: when the team gets smaller but the volume does not, the gap gets absorbed as longer waits, deferred work, and quiet service erosion; the question worth putting in front of them is how they hold service and Stars-relevant CS measures flat while carrying fewer people. This is squarely a Dynamic Workforce Orchestration conversation across both the contact center and the back office, which fits a payer taking cost out of both.
**Proof available:** Y for the standing third-party CS-addressability proof point (UHC's own $190M secret-shopper Stars case, per `StarRatings_Targeting_Flags_2026.md` rule 3), cited as UHC's stated figure with the CY2027 time-stamp caveat kept intact (that specific Call Center measure is retired for 2028 Stars). N for any Intradiem ROI or peer-savings figure; none goes in the angle until it clears the verified-metrics gate. Centene's own public numbers (61,000 employees, 26.3M members, $20-24M severance guide) are Centene-stated, not Intradiem claims.
**Next step + owner:** Route to `intradiem-first-draft-engine` then `intradiem-copy-sharpener`, sender Nathan Belfield, Finance/Ops primary. Confirm the specific Wellcare sub-4.0 contracts stay in the sequence after the July 2 dedup check. Send window tomorrow 7 to 9am ET.

**Suppression update (no outreach), closes yesterday's Clover review item:** Clover Health H5141 has been confirmed at 4.5 Stars for payment year 2027 (up from 3.5), and its HMO contract H8010 moved from 4.0 to 4.5, both following the post-Clover CMS recalculation. Both Clover contracts have now graduated above 4.0, so Clover comes out of the sub-4.0 CS motion. Yesterday's action item to hand-verify H5141 before any Clover send is resolved: do not sequence Clover on a sub-4.0 CS thesis. Source: Clover 8-K, Healthcare Dive, Healthcare Finance News. Note the structural point: the June 17 recalculation only moves stars up, never down, so it cannot have worsened any other target's addressable math, but it can have quietly graduated marginal contracts. The targeted re-verification pass on other Tier A/B contracts with disputed Part C measures (yesterday's action item 3) is still worth scoping before the next marginal-contract batch ships.

**Carried from yesterday (no re-fire):** Elevance Health's July 2 suit against the government over the $115M Stars recalculation is still live; new detail is that CMS denied Elevance's request to re-rate under the Clover methodology on June 26, which is what triggered the filing. Already logged and actioned yesterday (routed to first-draft-engine, Nathan, Stars/Quality plus Finance). No new action beyond letting that sequence run.

## Priority 2, Prepare This Week

- **Q2 2026 earnings season opens July 16 with UnitedHealth Group** (Thursday July 16, 8am ET, confirmed via UHG IR). This is the setup shot for the whole Tier A universe: Humana, Elevance, Centene, and CVS/Aetna calls follow across late July, and given the Elevance and Clover litigation backdrop, Stars and MA-margin language is very likely on these calls. Prepare to run each target parent's call through the war room in real time the morning after it reports, and pre-stage the `qbp_earnings_pressure` angle so a fresh CFO or CEO Stars quote can become same-day outreach. No send today; this is a calendar-stage item.
- **Centene cost pressure feeds the earnings read.** Centene's buyout outcome and any layoff decision will surface on or around its Q2 call. Treat the Priority 1 Centene sequence and the earnings watch as one connected thread, not two.

## Priority 3, Context

- **CMS 2027 QBP recalculation mechanics confirmed one-directional.** Only plans whose stars increase get their 2027 ratings updated and can resubmit bids; no plan is downgraded by the recalculation. Useful framing: our addressable math can only be stale-high (a marginal contract may have quietly graduated), never stale-low, which is why the targeted re-verification pass matters before marginal-contract outreach. Source: Healthcare Finance News, Seyfarth Shaw, Avalere.
- **WFM/CCaaS market, no account-specific news this cycle.** The Verint-Calabrio combined entity and the Genesys / NICE / Amazon Connect field remain in integration-and-coexistence posture, no target-account stack move surfaced. Standing wedge unchanged: a WFM or CCaaS purchase is a reason to talk, never a blocker, and a new CIO/CTO is a fresh technical buyer.
- **Change Healthcare claims-backlog coverage resurfaced** in search but traces to the February 2024 cyberattack aftermath, not a fresh event. Context only, no account fired.

## Accounts with No New Signals

Humana Inc., CVS Health Corporation, UnitedHealth Group (earnings-date item is a calendar stage, not a signal), Molina Healthcare (MAPD-exit context unchanged; April Long Beach layoffs stale), Health Care Service Corporation, Elevance Health (carried, no re-fire), Clover Health Holdings (suppression update, graduated out), California Physicians' Service, Cambia Health Solutions, CareFirst, Point32Health, Lifetime Healthcare, Athena Healthcare Holdings, Baystate Health, Mass General Brigham, New York City Health and Hospitals Corporation, Visiting Nurse Service of New York, Imperial Health Plan of California, Medica Holding Company, Hawaii Medical Service Association, Community Health Plan of Washington, Guidewell Mutual Holding Corporation, Local Initiative Health Authority for LA County (LA Care), Inland Empire Health Plan, Orange County Health Authority, Presbyterian Healthcare Services, Lumeris Group Holdings, ATRIO Health Plans, Clever Care Health Plan, Zing Health Consolidator, Devoted Health.

## Triggers Logged to TAM Engine

| domain | trigger_type | detail | date |
|---|---|---|---|
| centene.com | cost_mandate | Voluntary separation program opened to most of ~61,000 employees (Jun 15), decision deadline Jul 2 just closed, involuntary layoffs signaled if targets missed; tied to MA pay pressure and membership loss | 2026-07-02 |

Clover Health (H5141, H8010) NOT logged as a demand trigger; logged instead as a suppression event (both contracts graduated to 4.5, out of the sub-4.0 CS motion). Elevance not re-logged; its `qbp_earnings_pressure` trigger was recorded on the Jul 6 cycle.

## Executive Summary

One fresh Priority 1 fired: Centene's voluntary-separation window closed July 2 and involuntary layoff decisions are being made now, a clean DEFENSIVE cost-and-capacity forcing function on a target parent that already carries several sub-4.0 Wellcare contracts and a three-month-old Medicare reorg. Yesterday's Clover review item is resolved and turns into a suppression: both Clover contracts graduated to 4.5 Stars on the recalculation, so Clover leaves the sub-4.0 motion. The near-term calendar item is the July 16 UnitedHealth Q2 call opening an earnings season that, against the Elevance and Clover litigation backdrop, is likely to hand us live Stars quotes across the Tier A parents. Back-office motion still has no universe to scan; that gap sits with the Scott Kemme ICP conversation.

## Today's Action List

1. Run Centene through `intradiem-first-draft-engine` then `intradiem-copy-sharpener`, sender Nathan Belfield, Finance/Ops primary and Stars/Quality secondary, after confirming the Wellcare sub-4.0 contracts survive the July 2 dedup check. Send window tomorrow 7 to 9am ET.
2. Mark Clover Health suppressed in the sub-4.0 CS motion (H5141 and H8010 both at 4.5 for PY2027); close the hand-verify item from July 6.
3. Log the Centene `cost_mandate` trigger to `tam-outbound-engine/data/triggers.csv` (row above) so its fit score decay-refreshes.
4. Stage the earnings-season watch: put UnitedHealth July 16 on the calendar and pre-load the `qbp_earnings_pressure` angle so any fresh Stars quote from a Tier A call becomes same-day outreach.
5. Scope the targeted re-verification pass on other Tier A/B contracts with disputed Part C measures that the June 17 recalculation may have quietly graduated, before the next marginal-contract batch ships.
6. No back-office action today; universe remains blocked on the Scott Kemme ICP conversation.
