---
name: league-deal-desk
version: 1.0.0
description: Weekly deal desk orchestrator. Generates Slack updates, ghostwrites champion-to-EB emails, and extracts MEDDPICC fields from transcripts. Output is account-specific deal briefing with structured sections ready for internal alignment.
---

## When this skill applies

- Run weekly during deal cycles
- Trigger after significant prospect calls or email exchanges
- Run after deal status changes (moved stage, new stakeholder involved, timeline shift)

## Background

The Deal Desk skill centralizes deal activity into a single formatted output. It processes call transcripts, email chains, and deal notes to extract MEDDPICC intelligence, draft internal champion communications, and surface Slack updates for the sales ops channel. This ensures the entire team stays synchronized on account momentum.

## Workflow Steps

1. **Gather Deal Inputs**
   - Collect call transcript(s) from the period
   - Pull email chain with champion and stakeholders
   - Note any deal status changes, new contacts, or timeline shifts
   - Identify the current deal stage (Discovery, Technical Eval, Business Case, Procurement, etc.)

2. **Extract MEDDPICC Fields**
   - Metrics: Quantify the customer's stated KPIs (member count, cost per claim, NPS, engagement %)
   - Economic Buyer: Name, title, reporting line, approval authority
   - Decision Criteria: Stated selection criteria, RFP requirements, internal must-haves
   - Decision Process: Timeline, approval steps, committee structure
   - Paper Process: Legal/Procurement/InfoSec gates, contract review cycles
   - Identified Pain: Clinical pain points, operational gaps, patient/member friction
   - Champion: Primary contact name, title, credibility, motivation
   - Competition: Named competitors or build-in-house threat; their positioning

3. **Draft Slack Update**
   - 2-3 sentences summarizing deal progress
   - Flag any red lights (delay, new objection, stakeholder absence)
   - Include next milestone and expected decision date

4. **Ghostwrite Champion Email**
   - Draft 1:1 email FROM champion TO Economic Buyer
   - Language: Internal memo style, peer-to-peer, focuses on Operational Relief
   - Include 1-2 key metrics from Metrics section
   - Soft CTA: "Let's set 30 mins with the team to walk through the plan"
   - Apply Tenbit++ (Observation → Insight → Value → Next Step)

5. **Populate MEDDPICC Table**
   - Create structured table with 8 fields
   - Add confidence rating (Strong/Moderate/Gap) for each field
   - Flag any empty or weak fields in "MEDDPICC Gaps" section

6. **Generate Gap Questions**
   - For each Moderate or Gap field, create 1-2 discovery questions
   - Assign to Dallas or champion to ask on next call

## Canon Constraints

All communications follow these rules:

- **Tenbit++ Framework**: All external communications follow Observation → Insight → Value → Next Step
- **Pincer Rule**: Communications to VPs and Directors focus strictly on Operational Relief, never Brand Vision
- **Brand-Light Execution**: Do NOT mention League by name in early outreach (Days 1-5). Frame solution as category.
- **FORBIDDEN WORDS**: Never use leverage, synergy, cutting-edge, best-in-class, empower, seamless, robust, transform, transformation, catalyst, paradigm, innovative, or comprehensive
- **Strict Punctuation**: Periods and commas only inside narrative paragraphs. No hyphens or em dashes.
- **Named Outputs**: Every deliverable gets saved as a file. Nothing lives only in chat.
- **MEDDPICC Discipline**: After every call transcript, flag empty or weak MEDDPICC fields.

## Output

Save as: `[Account]_Deal_Desk_Update.md`

Format:

```
# [Account Name] Deal Desk Update
Date: [Date]
Stage: [Current Deal Stage]

## Slack Update
[2-3 sentence update]

## Champion Email (Ghostwritten)
[Email draft ready to share with champion for minor edits]

## MEDDPICC Summary Table
| Field | Status | Confidence | Notes |
|-------|--------|------------|-------|
| Metrics | [Value] | [Strong/Moderate/Gap] | [Notes] |
| Economic Buyer | [Name, Title] | [Confidence] | [Notes] |
| Decision Criteria | [Criteria] | [Confidence] | [Notes] |
| Decision Process | [Timeline/Steps] | [Confidence] | [Notes] |
| Paper Process | [Gates] | [Confidence] | [Notes] |
| Identified Pain | [Pains] | [Confidence] | [Notes] |
| Champion | [Name, Title] | [Confidence] | [Notes] |
| Competition | [Competitors] | [Confidence] | [Notes] |

## MEDDPICC Gaps & Follow-Up Questions
[List any gaps and 1-2 questions per gap to close it]

## Red Lights
[Any timeline slips, stakeholder absences, or objections]

## Next Milestones
[Expected next steps and dates]
```

## Examples

### Compliant Slack Update
"Account XYZ's VP of Benefits confirmed member engagement is down 23%. Their timeline moved left to June 1 go-live. Economic buyer (CFO) confirmed budget allocation. Champion flagged procurement as 4-week gate. Next: Technical scoping call Thursday."

### Non-Compliant Slack Update
"Great momentum with Account XYZ. We can offer them a seamless, cutting-edge platform that will transform their engagement strategy. Let's sync on next steps."
Issue: Uses FORBIDDEN WORDS, vague, no metrics, no timeline clarity.

### Compliant Champion Email
"Hi [Name], Based on our conversation with your team, the member engagement gap is costing roughly $2.4M annually. If we can move 8 points on your engagement metric, that's meaningful relief from a cost and operations perspective. I'd like 30 mins with you and [Economic Buyer] to walk through the 90-day implementation plan and address any legal or procurement questions. Available [2 times]. Let me know."

### Non-Compliant Champion Email
"Hi [Name], We're excited about the potential to transform your health plan through our innovative platform. Our best-in-class technology will empower your team to achieve seamless member engagement. We'd love to sync up and discuss a partnership. Let me know your availability."
Issue: Brand-centric, uses FORBIDDEN WORDS, no metrics, no operational focus.
