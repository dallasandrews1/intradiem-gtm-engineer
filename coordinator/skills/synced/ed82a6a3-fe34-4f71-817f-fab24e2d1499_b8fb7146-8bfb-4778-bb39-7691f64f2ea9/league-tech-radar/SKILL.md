---
name: league-tech-radar
version: 1.0.0
description: Weekly tech infrastructure signal sweep across all Tier-1 accounts. Filters for Microsoft Azure/Fabric, Facets, QNXT, HealthEdge, Epic, cloud migration, digital transformation partnerships in last 7 days. Maps signals to League plays and drafts CDO/CTO outreach angles.
---

## When this skill applies

- Run weekly (every Monday or at start of week)
- Run on each Tier-1 account in parallel
- Run when monitoring tech stack signals for strategic partnership plays
- Trigger immediately when Azure/Fabric, Epic, or QNXT signals appear

## Background

The Tech Radar skill provides infrastructure intelligence that unlocks new selling angles. When a payer announces a Microsoft Azure migration or Epic integration initiative, that's a forcing function to engage CTO/CDO with a "technical partnership" narrative. Tech Radar discovers these signals early and maps them to League's technical plays (Microsoft Pivot, Wrapper Moat).

## Workflow Steps

1. **Define Tech Signal Categories**
   - **Cloud Migration**: Azure, AWS, Google Cloud adoption, cloud-first architecture
   - **Data Platform**: Fabric, Databricks, Snowflake, modern data stack
   - **EHR Integration**: Epic, integration partnerships, claims/EHR bridges
   - **Digital Transformation**: CMS overhauls, member portal redesigns, digital partnerships
   - **Staff Hiring**: CDO/CTO hires, digital health director hires, engineering team expansion
   - **Vendor Partnerships**: Strategic technology partnerships, M&A in digital health space
   - **Regulatory/Compliance**: New CMS initiatives, STAR ratings, quality score announcements

2. **Set Search Parameters**
   - Time window: Last 7 days
   - Sources: Press releases, earnings call transcripts, board filings, news, LinkedIn announcements
   - Accounts: All Tier-1 assigned to Dallas Andrews
   - Keywords: Azure, Fabric, cloud, Epic, QNXT, HealthEdge, Facets, CDO, CTO, digital transformation, data platform, modernization

3. **Scan for Each Account**
   - Search news, earnings, and company announcements for each account
   - Flag any mention of infrastructure initiatives, tech hires, partnerships
   - Record date, source, and exact quote if available

4. **Filter for High-Signal Items**
   - Priority 1: Azure adoption or Fabric migration announcement (Microsoft play)
   - Priority 1: Epic integration or EHR modernization initiative (claims/EHR bridge play)
   - Priority 2: CTO or CDO hire announcement (new technical buyer)
   - Priority 2: Digital transformation partnership or vendor selection
   - Priority 3: Data platform (Fabric, Snowflake, Databricks) adoption
   - Priority 4: QNXT or HealthEdge billing system update or migration

5. **Map Signal to League Play**
   - **Microsoft Azure/Fabric Signal** → **Microsoft Pivot Play**: Position League as the "native Azure application" that fits Microsoft's data platform roadmap. Align on Fabric integration, real-time analytics, and modern data warehouse. CDO/CTO engagement angle: "Your Fabric adoption unlocks real-time member signals. Here's how we integrate."
   - **Epic/QNXT Signal** → **Claims-EHR Bridge Play**: Position League as the bridge between claims data and clinical data. Engagement angle: "Your Epic integration is data access. We're the member activation layer on top of that data."
   - **CTO/CDO Hire Signal** → **New Buyer Play**: Fresh technical buyer, no legacy vendor relationships. Engagement angle: "Welcome to [Account]. We help modern health plans activate member data in 6 weeks, not 6 months."
   - **HealthEdge/Facets Signal** → **Billing Integration Play**: Position League as the consumer-facing layer on top of complex billing systems. Engagement angle: "HealthEdge powers your billing, but member-facing activation is still manual. Here's the fix."

6. **Draft CDO/CTO Outreach Angles**
   - Create 1-2 sentence outreach angle per signal per account
   - Language: Peer-level, technical, assume they know their systems
   - Apply Tenbit++ (Observation → Insight → Value → Next Step)
   - Never mention League brand at this stage. Frame as "our approach to modern member data."
   - Example for Azure: "We saw your Fabric roadmap announcement. Real-time member signals in Fabric unlock things like dynamic intervention routing, predictive churn, and real-time engagement. Let's align on how that works."

7. **Flag Competitive Risk**
   - Note if competitor is mentioned in same announcement (e.g., "selecting Epic and Accolade")
   - This triggers competitor intel skill

## Canon Constraints

- **Tenbit++ Framework**: All external communications follow Observation → Insight → Value → Next Step
- **Pincer Rule**: Communications to VPs and Directors focus strictly on Operational Relief, never Brand Vision
- **Brand-Light Execution**: Do NOT mention League by name in early outreach (Days 1-5). Frame solution as category.
- **FORBIDDEN WORDS**: Never use leverage, synergy, cutting-edge, best-in-class, empower, seamless, robust, transform, transformation, catalyst, paradigm, innovative, or comprehensive
- **Strict Punctuation**: Periods and commas only inside narrative paragraphs. No hyphens or em dashes.
- **Named Outputs**: Every deliverable gets saved as a file. Nothing lives only in chat.
- **MEDDPICC Discipline**: After every call transcript, flag empty or weak MEDDPICC fields.

## Output

Save as: `Weekly_Tech_Radar_[Date].md`

Format:

```
# Weekly Tech Radar
Week of: [Date]
Scan Period: [Last 7 days]

## Priority 1 Signals (Act This Week)

### Account: [Account Name]
- **Signal**: [Azure/Epic/CTO Hire/Other]
- **Source**: [Press release/Earnings/News article]
- **Date**: [Date]
- **Details**: [1-2 sentence description]
- **League Play**: [Microsoft Pivot/Claims-EHR Bridge/New Buyer/Billing Integration]
- **CDO/CTO Outreach Angle**: [1-2 sentence angle for Dallas to use]
- **Next Step**: [Schedule call with CTO/CDO/Contact this account]

[Repeat for each Priority 1 signal]

## Priority 2 Signals (Monitor & Prepare)

### Account: [Account Name]
- **Signal**: [CTO Hire/Digital Transformation Partnership/Data Platform]
- **Source**: [Source]
- **Date**: [Date]
- **Details**: [Description]
- **League Play**: [Play name]
- **Timing**: [When to engage]

[Repeat for each Priority 2 signal]

## Priority 3 Signals (Contextual)

### Account: [Account Name]
- **Signal**: [Data platform/Billing system]
- **Source**: [Source]
- **Date**: [Date]
- **Details**: [Description]

[Repeat for each Priority 3 signal]

## Accounts with No New Signals
- [Account Name]
- [Account Name]
- [Account Name]

## Competitive Risk Flags
- [Account with competitor mention in same announcement]

## Week's Actions
1. [Outreach 1 - Send CDO outreach for Account X]
2. [Outreach 2 - Schedule call with CTO of Account Y]
3. [Monitor - Track Article Z for Account Z]
```

## Examples

### Compliant Priority 1 Signal
**Signal**: Microsoft Fabric adoption roadmap
**Account**: Humana
**Source**: Humana Q4 2025 earnings call transcript
**Details**: "We are modernizing our data infrastructure with Microsoft Fabric and Azure. This enables real-time analytics and improved member insights."
**League Play**: Microsoft Pivot (position League as native Fabric application)
**CDO/CTO Outreach Angle**: "Your Fabric adoption is powerful. Real-time member signal routing requires a consumer-first layer. Let's talk about how modern health plans activate Fabric data at scale."

### Compliant Priority 1 Signal
**Signal**: CTO hire
**Account**: Anthem
**Source**: LinkedIn announcement
**Details**: "Announcing Jennifer Park as VP Technology for Digital Health. Leading Anthem's member-facing innovation roadmap."
**League Play**: New Buyer Play
**CDO/CTO Outreach Angle**: "Jennifer, welcome to Anthem. Building modern member experiences at scale requires both data and activation. Let's connect on how we approach that."

### Non-Compliant Signal Analysis
"Anthem announced a new CTO. This is a great opportunity to tell them about our cutting-edge platform. We should tell them about all the innovative features we have."
Issue: Uses FORBIDDEN WORDS, no technical specificity, no operational mapping, generic tone.

### Compliant Competitive Risk Flag
**Account**: CVS Aetna
**Competitor Signal**: "Selecting Epic for EHR integration and Accolade for member engagement."
**League Play Impact**: Competitor is already in the deal. Trigger league-competitive-intel. Accolade = coaching-focused. Wedge = staffing cost at scale. Position League as operational fix to Accolade's FTE bottleneck.
