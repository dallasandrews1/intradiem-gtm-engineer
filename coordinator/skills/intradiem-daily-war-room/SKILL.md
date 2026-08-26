---
name: intradiem-daily-war-room
description: "Daily signal scan across Intradiem's outbound universes: the 32 Tier A+B Star Ratings parents, the back-office target list, and named strategic accounts. Sweeps last 24-72 hours for market events (earnings mentions, Stars language in filings, CMS releases), plan-level signals (quality leadership changes, hiring clusters), operational signals (outages, backlog news, cost mandates, BPO changes), and tech-stack signals (WFM/ACD/CCaaS moves: Verint, NICE, Calabrio, Genesys, Amazon Connect). Ranks Priority 1-4, maps each to an Intradiem play, logs fresh triggers for the TAM engine, and hands triggered accounts to the copy skills. Trigger on: run the war room, daily scan, morning sweep, what fired overnight, any breaking news on a target account. Run every business morning."
---

## When this skill applies

- **Automated as of Jul 17 2026:** this runs unattended weekdays at 7:15am via a local launchd job (`automation/run_war_room.sh` in the Intradiem GTM Engineer project), logging to `automation/logs/war-room-<date>.md`. It writes the log only; the gtm-daily-rundown reads it and carries the signal (single-morning-brief rule, no independent DM). Dallas dropped his prior manual habit of running this by hand in Cowork each morning, so don't proactively suggest or run a duplicate manual pass just because it's morning; the automated run already covers it. Still fine to trigger manually for a genuinely fresh reason (breaking news, pre-meeting check), just not as a default daily ritual.
- Immediately when major news breaks on any target account
- Weekly deep pass on tech-stack signals (Monday)
- When a fresh signal needs to become same-day outreach

## Background

Time-sensitive forcing functions have a 48-72 hour window while leadership is actively deciding. This skill catches those moments across BOTH motions (Star Ratings and back office), turns them into ranked, play-mapped actions, and keeps the trigger data flowing into the TAM engine so account scores stay current. It mirrors the signal-tier structure on the onboarding site: the engine's product thesis applied to our own pipeline.

## The universes

1. **Star Ratings motion:** the 32 Tier A+B parent orgs in `StarRatings_Targets_2026_Tiered.csv` (98 contracts). Suppression and routing rules in `StarRatings_Targeting_Flags_2026.md` apply BEFORE any outreach recommendation (Molina MAPD rule, Cigna-to-HCSC, market exits).
2. **Back-office motion:** the back-office / BPO target list as it stands in Clay (post ICP definition with Scott Kemme).
3. **Named accounts:** anything Naveen or Sales flags for standing watch.

Never scan or message on install-base accounts here; that is the signal engine's job and it routes to AEs/CSMs, not outbound.

## Signal taxonomy (tiered like the onboarding site)

**Tier 1, act immediately (Priority 1):**
- The October CMS Stars release (annual, re-tier the whole universe; see universe-vintage rule)
- Stars or quality language in SEC filings and earnings calls of a target parent
- Earnings miss attributed to MA margins, QBP revenue, or service costs
- CEO/COO/CFO change, or a new SVP/VP Stars, Quality, Medicare, or Customer Care
- Public outage, service failure, or complaint spike in the news
- M&A involving a target parent (integration = operational burden = our conversation)

**Tier 2, prioritize this week (Priority 2):**
- Quality/ops hiring clusters (multiple postings in Stars, quality, WFM, back-office ops)
- Contracts sitting just under 4.0 entering a new measurement window
- Cost-reduction or efficiency mandates in guidance
- BPO contract awards, renewals, or repatriations (back-office motion)

**Tier 3, supporting context (Priority 3):**
- WFM/ACD/CCaaS stack news: Verint, NICE, Calabrio expansions, Genesys or Amazon Connect migrations, ServiceNow back-office rollouts. Play mapping: we are the real-time action layer that sits ON the stack they just bought; a fresh WFM investment is a reason to talk, never a blocker. New CIO/CTO = new technical buyer with no legacy commitments.
- Analyst coverage, industry consolidation affecting a target's competitive posture

**Tier 4, track only:** everything contextual that raises priority later but never fires outreach alone.

## Workflow

1. **Scan** news, filings, earnings transcripts, press releases, LinkedIn moves, and job boards for each universe, last 24-72 hours.
2. **Apply suppression rules** from the targeting flags before anything becomes a recommendation.
3. **Rank** every hit Priority 1-4 per the taxonomy. Escalation rule: a Tier 2/3 signal on an account that already holds a live Tier 1 window escalates one level.
4. **Map each Priority 1-2 signal to a play:** which motion, which persona (per the copy skills' persona notes), which one-idea candidate, which verified proof point could support it (check intradiem-verified-metrics; never assume).
5. **Log triggers:** append fresh triggers to the TAM engine's `data/triggers.csv` shape (domain, trigger type, date, source, strength) so fit scores decay-refresh correctly.
6. **Hand off for copy:** any same-day outreach goes through intradiem-first-draft-engine then intradiem-copy-sharpener. The war room writes angles, never final copy.
7. **Competitor mention** in any signal → load intradiem-competitive-intel for the wedge brief.
8. **Route:** Slack-ready alert per Priority 1 signal (signal-to-play format), action list for the day.

## Canon constraints

- Tenbit++ as diagnostic; prospect is the hero; operational relief for VPs/Directors, never brand vision
- Brand-light: no Intradiem naming in Days 1-5 angles
- Forbidden words and no em dashes anywhere
- Every stat in an angle passes the verified-claims gate or ships [UNVERIFIED]
- Sender is the rep (Star Ratings default: Nathan), never Dallas by default
- Contact centers AND back offices; six verticals; never "call center tool"
- Named outputs: every run saves a file

## Output

Save as: `Daily_War_Room_[Date].md`

Sections: Priority 1, Act Today (per signal: account, type, description, date, source quote, forcing function classified PROUD or DEFENSIVE, target persona, play, one-idea candidate, verified proof available Y/N, next step + owner) → Priority 2, Prepare This Week → Priority 3, Context → Accounts with no new signals (one line) → Triggers logged to TAM engine (table) → Executive summary (2-3 sentences) → Today's action list.

**Causal chain (per `automation/LOG_CONVENTION.md`):** every Priority 1-2 item and anything staged ends with an `evt:` anchor (`evt: war-room-<YYYY-MM-DD>#<slug>`), minted at FIRST surfacing only. A signal carried forward from a prior day keeps its original id, cited via `chain:`, never re-minted. Put the evt id in the source/notes field of any staged CSV row; never add a CSV column for it.

## Example (compliant Priority 1)

**Account:** [Tier A parent] · **Signal:** Q2 earnings call, CFO: "Star Ratings pressure on our MA book is a headwind we are actively managing." · **Classified:** DEFENSIVE (lead with the response: the quality investment they announced, not the downgrade) · **Persona:** SVP Stars / VP Medicare · **Play:** Star Ratings motion, 2028-window one idea · **Proof:** check Repository before citing any peer outcome · **Next step:** first-draft-engine today, Nathan sends tomorrow 7-9am ET.

## Example (non-compliant, reject)

"Their CEO mentioned AI on the earnings call, we should send our innovative platform deck." No forcing function, forbidden word, brand-heavy, no persona, no play mapping. Does not enter the report.
