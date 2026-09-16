---
name: league-daily-war-room
version: 1.0.0
description: Daily signal scan for all Tier-1 accounts. Filters for M&A, leadership changes, earnings, regulatory shifts in last 24-72 hours. Ranks by urgency (Priority 1-4). Generates Tenbit++ outreach sequences for triggered accounts.
---

## When this skill applies

- Run daily (morning of every business day)
- Run after market open (check for earnings/M&A announcements)
- Run immediately when major news breaks (CEO departure, acquisition, regulatory change)
- Trigger when prospect is involved in M&A or leadership change

## Background

The Daily War Room skill catches time-sensitive forcing functions that unlock immediate outreach. When an account's CEO departs, announces a major acquisition, or faces new regulatory pressure, there's a 48-72 hour window where leadership is making strategic decisions and open to new vendor conversations. This skill identifies those moments and generates outreach ready to send within hours.

## Workflow Steps

1. **Set Daily Scan Parameters**
   - Time window: Last 24-72 hours (for morning scan)
   - Accounts: All Tier-1 assigned to Dallas Andrews
   - Signal sources: News, SEC filings, earnings announcements, press releases, regulatory bulletins
   - Keywords: M&A, acquisition, merger, divestiture, CEO, CFO, leadership change, restructuring, earnings, regulatory, CMS, rate increase, penalty

2. **Scan for M&A and Ownership Changes**
   - Flag any announcement of acquisition, merger, or divestiture involving Tier-1 account
   - Note date, buyer/seller, deal rationale (cost reduction, technology acquisition, market consolidation)
   - Urgency: **Priority 1** (immediate outreach needed)
   - Forcing function: New leadership team evaluating vendor strategy, integration complexity creates operational relief opportunity

3. **Scan for Leadership Changes**
   - Flag CEO, CFO, COO, or CIO departures or promotions
   - Flag new C-suite hires (especially CFO or CDO hires from competitor)
   - Note date and incoming executive's background
   - Urgency: **Priority 1** (new executives have no legacy vendor commitments)
   - Forcing function: "Welcome to account. Here's how modern health plans solve member engagement."

4. **Scan for Earnings and Financial Events**
   - Pull recent earnings announcements and earnings call transcripts
   - Flag any language about cost reduction, operational efficiency, technology investment, margin pressure
   - Note specific guidance changes (earnings miss, revised guidance down)
   - Urgency: **Priority 2** (context-dependent; if earnings miss due to engagement/churn, move to Priority 1)
   - Forcing function: "We saw your earnings guidance. Engagement and retention are your highest-leverage cost levers. Let's talk."

5. **Scan for Regulatory and Market Changes**
   - Flag CMS rate announcements, Star Rating changes, regulatory penalties, compliance violations
   - Flag market consolidation announcements (industry M&A activity affecting competitive posture)
   - Note date and potential impact on account's business
   - Urgency: **Priority 2-3** (context-dependent)
   - Forcing function: "Your Star Ratings are under pressure. Engagement metrics drive 35% of Star Score. Here's how we improve those in 90 days."

6. **Rank by Urgency**
   - **Priority 1**: Active M&A (acquired or acquiring), CEO/CFO departure or new hire, regulatory penalty or CMS rate cut
   - **Priority 2**: Earnings miss, Star Rating decline, guidance revision down, competitive loss announced
   - **Priority 3**: Leadership hire outside C-suite, strategic partnership announcement, technology investment signal
   - **Priority 4**: Industry consolidation, regulatory shift (not directly impacting account yet)

7. **Generate Tenbit++ Outreach Sequences**
   - For each Priority 1 signal, create opening email/call script
   - Structure: Observation → Insight → Value → Next Step
   - Never mention League by name
   - If M&A: Frame as integration and operational efficiency angle
   - If leadership change: Frame as welcome angle without legacy baggage
   - If earnings miss: Frame as specific metric (engagement, retention, Star Score) that drives profitability
   - If regulatory pressure: Frame as operational relief through metric improvement

8. **Assign to Dallas**
   - Create action items: "Call [Contact] at [Account] within 24 hours with [Angle]"
   - Provide email draft and call script
   - Flag any contact information gaps

## Canon Constraints

- **Tenbit++ Framework**: All external communications follow Observation → Insight → Value → Next Step
- **Pincer Rule**: Communications to VPs and Directors focus strictly on Operational Relief, never Brand Vision
- **Brand-Light Execution**: Do NOT mention League by name in early outreach (Days 1-5). Frame solution as category.
- **FORBIDDEN WORDS**: Never use leverage, synergy, cutting-edge, best-in-class, empower, seamless, robust, transform, transformation, catalyst, paradigm, innovative, or comprehensive
- **Strict Punctuation**: Periods and commas only inside narrative paragraphs. No hyphens or em dashes.
- **Named Outputs**: Every deliverable gets saved as a file. Nothing lives only in chat.
- **MEDDPICC Discipline**: After every call transcript, flag empty or weak MEDDPICC fields.

## Output

Save as: `Daily_War_Room_[Date].md`

Format:

```
# Daily War Room
Date: [Date]
Scan Period: Last 24-72 hours

## Priority 1: Act Today
[List all Priority 1 signals with forcing function and outreach ready to deploy]

### Account: [Account Name]
- **Signal Type**: M&A / Leadership Change / Regulatory Penalty
- **Description**: [What happened]
- **Date Announced**: [Date]
- **Key Context**: [Why this matters operationally]
- **Forcing Function**: [Operational pain created by this signal]
- **Target Contact**: [Name, title, best contact method]
- **Outreach Angle**: [Tenbit++ observation-insight-value-next step]
- **Email Draft**: [Ready-to-send email 80-120 words]
- **Call Script**: [Opening 3-5 sentences for Dallas to use]
- **Next Step**: [Timeline for Dallas to execute]

[Repeat for each Priority 1 signal]

## Priority 2: Prepare & Monitor
[List all Priority 2 signals with context and prep notes]

### Account: [Account Name]
- **Signal Type**: [Earnings/Star Rating/Competitive Loss]
- **Description**: [What happened]
- **Date Announced**: [Date]
- **Forcing Function**: [Potential opportunity]
- **Timeline**: [When to reach out]

[Repeat for each Priority 2 signal]

## Priority 3: Track
[Brief list of Priority 3 signals]

## Accounts with No New Signals
- [Account Name]
- [Account Name]

## Executive Summary
[1-2 paragraph summary of the day's opportunity landscape]

## Dallas' Action List
1. [Specific action 1]
2. [Specific action 2]
3. [Specific action 3]
```

## Examples

### Compliant Priority 1 M&A Signal
**Account**: Centene
**Signal**: Acquires multi-state Medicaid plan (state government operator)
**Forcing Function**: Integration complexity creates operational burden. Member engagement and retention become critical post-acquisition.
**Outreach Angle**: "We saw your acquisition close. Post-acquisition, member retention and activation are make-or-break. Integration timelines create friction. Let's talk about how modern plans activate members at scale."
**Email Draft**: "Hi [Name], Congratulations on closing the acquisition. Post-acquisition member retention is always operationally complex. Engagement metrics directly impact profitability. We help health plans activate members in 6-8 weeks and reduce member services operational cost 20-25%. Let's talk about how that applies to your integration. Available [2 times] this week. Thanks, Dallas."
**Call Script**: "Hi [Name], Dallas Andrews with [Company]. I saw your acquisition close. Post-acquisition member engagement and retention are your biggest cost levers over the next 90 days. I wanted to see if there's a fit to talk about how modern plans handle that. Do you have 15 minutes Thursday or Friday?"

### Compliant Priority 1 Leadership Change Signal
**Account**: Aetna (now CVS Health)
**Signal**: New Chief Digital Officer appointed from competitor (ex-Humana digital executive)
**Forcing Function**: No legacy vendor relationships, responsible for digital transformation initiatives.
**Outreach Angle**: "Welcome to Aetna. Your digital transformation roadmap is ambitious. Member activation at scale requires both data infrastructure and consumer-first design. Let's align on how modern plans approach that."
**Email Draft**: "Hi [Name], Welcome to Aetna. Your background at Humana gives you insight into what modern member engagement looks like. At Aetna's scale, member activation is the largest lever for engagement and retention. We've helped similar-scale plans activate engaged members 5-8 points within 90 days. Let's talk about your roadmap. Available [2 times]. Thanks, Dallas."

### Non-Compliant War Room Entry
**Account**: Blue Shield
**Signal**: CEO announcement about digital transformation strategy
**Error**: "We should tell them about our cutting-edge, best-in-class platform that will transform their member engagement and empower their team. This is a great opportunity to discuss our innovative solutions."
Issue: Uses FORBIDDEN WORDS, no operational focus, no specific metric connection, no forcing function, brand-centric.

### Compliant Priority 2 Earnings Signal
**Account**: UnitedHealth
**Signal**: Earnings miss on medical loss ratio. Guidance revised down.
**Forcing Function**: Engagement and retention are cost levers that impact margin.
**Preparation Angle**: "Wait for next earnings call or investor day announcement. If they specifically mention engagement or member retention as remediation strategy, move to Priority 1 and outreach immediately."

### Non-Compliant Urgency Misjudgment
Treating a routine leadership hire in IT operations (not digital or member-facing) as Priority 1.
Correct approach: Priority 3. Only escalate to Priority 1 if it's a CDO, CMO, or CFO hire from a competitor.
