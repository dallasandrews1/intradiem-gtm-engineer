---
name: league-verified-metrics
description: >
  League's source of truth for verified metrics, proof points, and customer value stories.
  Enforces citation discipline and 1:1/1:many approval-tier compliance. Primary source:
  League Value Repository Q1 2026 (updated quarterly). Trigger when citing League stats,
  ROI numbers, proof points, engagement metrics, clinical outcomes, financial impact, or
  customer results. Also trigger when building outreach, pitch prep, webinar content,
  marketing collateral, QBR materials, or any customer-facing content with League data.
  Trigger on "what are our numbers," "where did that stat come from," "is that verified,"
  "what can I say about [customer]," "update proof points," or "add case study data." Load
  proactively when generating content that includes a League number or when a new case
  study or pitch deck is uploaded. Never skip because you "remember" a number — always check.
---

# League Verified Metrics & Proof Points

## When to Load This Skill

**TRIGGER when ANY of these conditions are true:**
- Generating, citing, or calculating with League-specific statistics, engagement metrics, clinical outcomes, financial impact claims, or customer results
- Building outreach copy, pitch prep, webinar slides, marketing collateral, QBR decks, blog posts, analyst materials, or any customer-facing content that references League data
- Answering questions like "what are our numbers," "where did that stat come from," "is that metric verified," "what can I say about [customer]," or "what's our latest on [metric]"
- Ingesting new source material (case studies, press releases, value stories, pitch decks) that may contain proof points to add to the repository
- Running any scoring model, ROI calculator, or business case that uses League stats

**LOAD PROACTIVELY (without being asked) when:**
- Any other skill or workflow is generating content that will include a League number
- The user uploads or references a new case study, value story, or pitch deck
- A draft email, LinkedIn message, call script, webinar slide, or marketing asset contains a quantified League claim

**DO NOT SKIP** this skill just because you "remember" a number from a previous conversation. Numbers change quarterly. Always check.

## Purpose

This skill is the citation-discipline layer for every League stat that appears
in any output. It prevents number drift, enforces source traceability, and
governs which metrics can be used in which contexts (1:1 prospecting vs.
1:many distribution). If a League number leaves this system without a source
and an approval tier, it is non-compliant.

## Background

League's go-to-market teams reference 140+ statistics across outreach,
pitch decks, value stories, webinars, marketing collateral, and internal
models. Without a single verified source of truth, numbers drift — formulas
use "$400 member acquisition cost" when the pitch deck actually says "$400K
monthly cost of inaction per 1M members" (a 100x difference in per-member
terms). Stats that can't be defended in a prospect meeting or on a webinar
stage erode credibility. This skill exists to prevent that.

The repository integrates the **League Value Repository Q1 2026** as the
primary source. The Value Repository is maintained by the Platform Growth
team, updated quarterly with governance standards — traceable sources,
blinding rules, and presenter notes that specify approval status per slide.

## Data Sources

### Embedded Quick Reference (always available)
This skill contains the most commonly referenced 140+ metrics directly in
the body below. For most tasks — writing an email, checking a stat, prepping
for a call, building a slide — this is sufficient.

### Canonical Source: League Value Repository (Google Drive)
The authoritative upstream source is the **League Value Repository** Google
Slides deck, maintained by the Platform Growth team in the "Client Specific
Content" folder on Google Drive.

- **Google Drive file ID:** `12e6jGWD_nbb06gxuUnJc--zo-pvq9PBc2uFOUZAvK6E`
- **URL:** https://docs.google.com/presentation/d/12e6jGWD_nbb06gxuUnJc--zo-pvq9PBc2uFOUZAvK6E/edit
- **Update cadence:** Quarterly
- **Contains:** Customer spotlights, value stories, proof points with presenter notes specifying approval status per slide

If Google Drive is connected, you can fetch the latest version to verify
stats or ingest new data. If Drive is not connected, use the embedded quick
reference below — it reflects the Q1 2026 version of the Value Repository.

### Additional Verified Sources
- League Q1 2026 Reintroduction Pitch Deck — Financial framing, cost-of-inaction data
- Forrester Wave Q1 2026: CX Platforms for Healthcare — Analyst recognition
- League Connect 2026 Executive Summary — Conference-sourced claims
- League Case Studies Q2 2025 — Customer spotlights (check Value Repository for newer data)
- Social Proof Data Points Q2 2025 — Legacy stats (~1 year old, flagged for refresh)
- KFF (2024-2025) — Industry financial benchmarks

## Repository Structure

140+ verified metrics | 27+ cited sources | 10 customer spotlights | 8 sections

1. **Platform Engagement Metrics** — MAU, user growth, program enrollment, AI stats, deployment speed, satisfaction
2. **Health Outcomes & Clinical Impact** — Preventative care, chronic care (diabetes, hypertension, anxiety), screenings, maternal health, medication adherence, seniors
3. **Communication & Marketing Effectiveness** — Open rates, CTR, push notifications, onboarding *(NOTE: all 7 stats in this section flagged NEEDS REFRESH — sourced from Social Proof Q2 2025, ~1 year old)*
4. **Customer-Specific Results** — Medibank, Highmark, Shoppers/PC Health, Manulife, SCAN, Santa Clara, Baptist Health, Quest (pre-launch), Alberta, HCSC, CareSource, enGen
5. **Financial Impact** — Enterprise value unlock (~$40M/1M/5yr), operational savings, clinical/quality impact, growth/retention, cost of inaction framing
6. **Industry Benchmarks (Third-Party)** — Acquisition/retention costs, call center economics, NPS, churn, workforce context, KFF financial benchmarks
7. **Numbers Requiring Internal Validation** — Flagged metrics NOT verified by any official League source
8. **Source Index** — All documents cited with context

### Forrester Wave Q1 2026
League designated **Leader** in Forrester Wave: CX Platforms for Healthcare.
Strategy Score: 4.20 (#1 of 12). Current Offering: 3.46 (Top 3 of 12).
Perfect 5.00 scores in Vision, Innovation, Roadmap, Adoption, Composability,
and Customer Health Record Access. Known gaps: Partner Ecosystem (1.00),
Search (1.00), Find Care (1.00).

## Two-Tier Approval Model

Every metric carries an **Approval Tier** that governs where and how it
can be used:

**1:1** — Individual outreach: cold emails, DMs, call prep, 1-on-1 prospect
conversations, internal account planning. Standard usage rules apply. Follow
blinding restrictions. Content is unlikely to be redistributed.

**1:many** — Broad distribution: webinars, marketing collateral, website,
press, conference presentations, blog posts, analyst briefings, social media.
Requires heavier scrutiny. Check Value Repository presenter notes for specific
restrictions. May need PM/Marketing sign-off. Content may be scrutinized by
senior leadership or external audiences.

**When generating content, always check the tier.** A metric approved for 1:1
use may NOT be appropriate for a webinar slide, blog post, or marketing
one-pager without additional review.

## Rules

### Must

1. Every League-specific statistic used in any output must include its source document in parentheses — e.g., "3-4x preventative visit increase (Value Repository Q1 2026, Slide 9)."

2. Before using any League metric in customer-facing content, check it against this skill's data. If a stat is not listed here, flag it as **[UNVERIFIED]** in the output.

3. When a number appears in the Flagged/Unverified section, always include a note that it has not been verified by an official League source and state the recommended alternative.

4. When any formula or model references a League stat, pull the exact value from this skill rather than using a hardcoded number from a prior conversation or script.

5. When new case studies, press releases, pitch decks, or value stories are provided, follow the New Proof Point Ingestion workflow (below).

6. Always check and respect the **Approval Tier** (1:1 vs 1:many) before including a metric. If the output is for broad distribution (webinar, marketing, press), only use metrics approved at the 1:many tier. If a 1:1-only metric is needed for 1:many use, flag it for PM/Marketing review.

7. Always check and respect the **Usage Rules** for each metric — blinding requirements, customer attribution restrictions, sample size caveats, and "NEEDS REFRESH" flags all override default behavior.

### Should

1. When citing industry benchmarks, clearly label them as "Industry benchmark" rather than a League-specific claim — e.g., "Member acquisition costs range from $500-$1,500 (AArete, industry benchmark)."

2. When multiple sources confirm the same metric, cite the most recent and most authoritative source first. Prefer Value Repository Q1 2026 over older documents when both exist.

3. When a conversation requires a number that isn't verified, suggest deriving it from verified engagement metrics rather than inventing a figure — e.g., "We can't claim a specific churn reduction %, but we can say 3x engagement lift and 5x program enrollment (both verified), which are leading indicators of retention."

4. When a metric is flagged "NEEDS REFRESH," note the age of the data and check whether the Value Repository has a newer version before citing.

5. For blinded customers (Highmark, Manulife, Shoppers in certain contexts), use the blinding language specified in the Usage Rules — e.g., "a large US payer" instead of naming Highmark directly, depending on context.

### Never

1. Never present a number from the Flagged/Unverified section as a confirmed League proof point in any customer-facing material.

2. Never use the "$400 member acquisition cost" framing — the verified number is "$400K monthly cost of inaction per 1M members" ($4.80/member/year), which is a fundamentally different claim. The $40M enterprise value figure is per 1M member population over 5 years — not a per-member acquisition cost.

3. Never fabricate or extrapolate a League-specific statistic that doesn't appear in this skill or an official League document, even if the calculation seems reasonable.

4. Never cite a third-party industry benchmark as if it were a League result.

5. Never use Quest Diagnostics data externally — Quest is NOT yet live on the League platform (R1 launch targeted early Q4 2026). All Quest value shown is anticipated/forward-looking.

6. Never use a 1:1-tier metric in 1:many content without explicitly flagging it for approval.

## New Proof Point Ingestion Workflow

When new source material is provided (case studies, press releases, pitch
decks, value stories, customer success reports):

1. **Extract** — Read the full document and extract every specific number, percentage, statistic, metric, and quantified outcome.

2. **Categorize** — Sort each metric into the appropriate section. Assign an Approval Tier (1:1 or 1:many) based on the source's distribution context. Note blinding, sample size, approval status, and any caveats.

3. **Cross-reference** — Check if the metric confirms, updates, or contradicts an existing entry. Note any conflicts. Prefer the Value Repository as the authoritative source when there's a conflict with older documents.

4. **Update** — Add new verified metrics with the source document name, date, specific location (e.g., "Slide 4"), Usage Rules, and Approval Tier.

5. **Report** — Present a summary showing: what's new, what's updated, what conflicts were found, and what remains unverified.

## Key Verified Numbers (Quick Reference)

These are the most commonly referenced stats. For the full 140+ metrics
with detailed Usage Rules and Approval Tiers, consult the Value Repository
in Google Drive.

### Platform Scale
- 70M contracted users globally (Value Repository Q1 2026; League PR 2026)
- 271% YoY user growth (League PR, March 2025)
- 180M AI-powered personalized recommendations annually (Value Repository Q1 2026, Slide 8)
- $500M+ platform investment (Value Repository Q1 2026, Slide 8)
- 150PB data processed in 24 months (Value Repository Q1 2026, Slide 8)
- AI hallucination rate ≤4% (League Connect 2026 CTO keynote)
- Forrester Wave Leader — Strategy Score 4.20, #1 of 12 (Forrester Wave Q1 2026)

### Engagement
- 20-45% Monthly Active Users across book of business (Value Repository Q1 2026, Slide 23)
- 3x increase in digital engagement (Value Repository Q1 2026, Slide 23) [1:1 — cite Manulife, blinded]
- 5x increase in program enrollment (Case Studies Q2 2025; Pitch Deck) [1:1]
- 95% increase in daily digital interactions (Value Repository Q1 2026, Slide 11) [1:many — Medibank specific]
- 50% self-enrollment in programs (Value Repository Q1 2026, Slide 24) [1:1]
- 95% program continuation rate (Value Repository Q1 2026, Slide 24) [1:1]
- 2.1 programs completed per member (Value Repository Q1 2026, Slide 24) [1:1]
- 60% recommended health activity completion (League PR, March 2025) [1:many]

### Health Outcomes
- 3-4x more likely to get a preventative visit (Value Repository Q1 2026, Slides 9, 28) [1:many]
- 6x increase in behavioral health services adoption (Value Repository Q1 2026, Slide 12) [1:many — Manulife blinded]
- 3.2x annual wellness visits increase (Social Proof Data Points Q2 2025) [1:1]
- Diabetes: blood sugar in target range 46%→69% in 3 months (Value Repository Q1 2026, Slide 27) [1:1]
- Diabetes: preventative care compliance 79%→93% in 3 months (Value Repository Q1 2026, Slide 27) [1:1]
- Hypertension: 22% BP decrease; 77% of decreasers to normal (Value Repository Q1 2026, Slides 25, 28) [1:1]
- Anxiety: 47% reported decrease (Value Repository Q1 2026, Slide 28) [1:1]
- Medication adherence: 95% during program (Value Repository Q1 2026, Slide 25) [1:1]

### Financial Impact
- ~$40M enterprise-wide value unlock per 1M members over 5 years (Value Repository Q1 2026, Slide 7) [1:1]
- $43M-$74M total 5-year value range per 1M (Value Repository Q1 2026, Slide 7) [1:1]
- $12M-$21M operational savings at engagement scale (Value Repository Q1 2026, Slide 7) [1:1]
- $26M-$45M clinical outcomes & quality impact (Value Repository Q1 2026, Slide 7) [1:1]
- $6M-$8M growth & retention impact (Value Repository Q1 2026, Slide 7) [1:1]
- $400K/month cost of inaction per 1M members (2026 Pitch Deck, Slide 2) [1:1]
- = $4.8M/year per 1M members (derived)
- = $4.80/member/year (derived — label as derived)
- 20-36% admin touchpoint reduction for satisfied members (Value Repository Q1 2026, Slide 7) [1:1]
- Digitally engaged members 3x more likely to renew (Value Repository Q1 2026, Slide 7) [1:many]

### Customer Highlights (check blinding rules per metric)
- Medibank (logo + story approved): 4.2M+ users, 95% daily interactions digitized, 3+ experiences launched [1:many]
- Highmark (blinded): 1.57M activated members (2025), 30% MAU, 60 features launched, 9% YoY call reduction, $2.7M est. annual call deflection savings [1:1]
- Shoppers/PC Health (blinded in some contexts): 1M+ activated users, 4.8 app rating, 140K+ care services, 2x diabetic engagement, 70% GLP-1 completion [1:1]
- Manulife (blinded): 2x mobile activation, 3x engagement, 6x behavioral health, 2.1M licenses, 59% rewards completion [1:1]
- SCAN (logo + story approved): 37% MAU, 54% MAU growth in 2 quarters, 82% user satisfaction (n=2,000) [1:many]
- Santa Clara (logo + story approved): 3x digital activation, 68% CSAT, 20% HRA completion, 5 languages [1:many]
- Baptist Health (logo + story approved): 42% well-baby visit attendance increase, 41% postpartum care completion increase, 11% fewer missed prenatal visits [1:1]
- Quest (pre-launch, blinded): 1 in 3 adult Americans reached, 11.6M eligible — DO NOT use externally [1:1]
- All deployments: ~6 months to first release [1:many]

### Industry Benchmarks (NOT League claims — for contextual framing only)
- Member acquisition cost: $500-$1,500 per member (AArete)
- Cost to retain existing member: $100-$300/year (AArete)
- Acquisition vs. retention cost ratio: 5x more to acquire (AArete; industry standard)
- Healthcare call cost (compliance-heavy): $7-$9 (Nextiva 2026); complex calls $8-$15+ (Nextiva; CloudTalk; KrispCall)
- Average call center cost per call (general): $4.90 (Dialog Health; Call4Health)
- Average annual call center operating cost: $13.9M (Dialog Health)
- Healthcare NPS average: +58 (CustomerGauge); median 61 (Survicate 2025)
- Digital call deflection (early adopters): 20-25% (Luma Health; Fierce Healthcare)
- MA plan average churn: ~10% (Oliver Wyman; Engagys)
- Revenue loss from churn per 100K-member plan: ~$120M (Data Decisions Group)
- Voluntary/preventable churn: 30-50% (Engagys; Press Ganey)
- 75% of adults using health apps; 80% of 65+ using digital health tools (KFF 2024)

### Flagged / Unverified (DO NOT use as League claims)
- "$400/member acquisition cost" — INCORRECT framing of pitch deck data; the verified figure is $400K/month cost of inaction per 1M members
- "15-30% League churn reduction" — no League case study quantifies churn reduction directly; derive from engagement or get from CS
- "40% call center deflection" — NOT in any League doc; industry range is 20-25%; Highmark blinded data shows 9% YoY call reduction
- "0.5 calls/member/year" — industry assumption, no source found; research via AHIP or payer partners
- "$15/call" — high end of industry range; use "$8-$15 range" or "$7-$9 for compliance-heavy" instead
- "90+ NPS" — NOT in any League doc; industry avg is 58-61; remove until verified

## Examples

### Compliant (1:1 outreach — Sales/BD)

**User asks:** "What call center savings can we pitch to a large payer?"

**Correct response:** "Based on verified League data, we can frame call center
impact using a combination of League proof points and industry benchmarks.
Highmark (blinded as 'a large US payer') saw a 9% YoY total call reduction
and 10% ID card call volume reduction after embedding League, with estimated
annual call deflection savings of $2.7M (Value Repository Q1 2026, Slide 22 —
1:1 tier, blinded only). For broader context: healthcare payer compliance
calls cost $7-$9 each (Nextiva 2026, industry benchmark), and early digital
adopters see 20-25% call deflection (Luma Health, industry benchmark). Combined
with League's verified 3x digital engagement increase and 95% daily interaction
digitization, you can build a defensible case. Note: the 40% call deflection
figure used in some older materials is unverified and should not be presented
as a League proof point."

### Compliant (1:many content — Marketing)

**User asks:** "I need a stat for a webinar slide about preventative care."

**Correct response:** "The 3-4x preventative visits increase is approved at the
1:many tier (Value Repository Q1 2026, Slides 9, 28). Safe for webinar use.
If you also want to cite the 6x behavioral health adoption, that's also
1:many-approved but must be blinded (do not attribute to Manulife by name in
broad distribution). The 3.2x annual wellness visits figure is 1:1 only —
don't include it on a webinar slide without PM review."

### Compliant (Customer Success — QBR prep)

**User asks:** "I'm prepping a QBR deck for our SCAN account. What results can I highlight?"

**Correct response:** "SCAN is logo + story approved, so you can use their name
and data freely. Key metrics: 37% MAU, 54% MAU growth over 2 quarters, and
82% user satisfaction with n=2,000 respondents (Value Repository Q1 2026,
Slide 15). All three are approved at the 1:many tier, so they're safe for
a QBR deck that might get forwarded internally at SCAN. If you want to
compare against other customers for context, Medibank (also logo-approved)
has 4.2M+ users and 95% daily interactions digitized — but keep Highmark and
Manulife blinded if referenced."

### Non-compliant

**User asks:** "What call center savings can we pitch?"

**Incorrect response:** "League typically reduces call center volume by 40%,
saving plans approximately $15 per deflected call."

This fails because: (a) 40% is not verified by any League case study or
official source, (b) $15/call is the high end of the industry range presented
as a League-specific number, (c) no source citations are provided, and
(d) no approval tier is considered.

## Exceptions

When the user explicitly asks for a rough internal estimate or back-of-napkin
calculation and labels it as such (e.g., "just give me a ballpark for internal
modeling, not for a prospect"), unverified numbers may be used IF they are
clearly marked with **[INTERNAL ESTIMATE - NOT FOR EXTERNAL USE]** and the
verified alternative is noted alongside.

## Source Hierarchy

When the same metric appears in multiple documents, prefer sources in this order:

1. **League Value Repository Q1 2026** — Primary source, quarterly updated, governance-backed
2. **2026 Reintroduction Pitch Deck** — Financial framing and cost-of-inaction data
3. **Forrester Wave Q1 2026** — Analyst recognition and competitive positioning
4. **League Connect 2026 Executive Summary** — Conference-sourced claims (verify before written collateral)
5. **League Case Studies Q2 2025** — Customer spotlights (check if Value Repository has newer data)
6. **Social Proof Data Points Q2 2025** — Legacy stats (~1 year old, flagged for refresh)
7. **KFF / Third-party sources** — Industry context only, never present as League claims
