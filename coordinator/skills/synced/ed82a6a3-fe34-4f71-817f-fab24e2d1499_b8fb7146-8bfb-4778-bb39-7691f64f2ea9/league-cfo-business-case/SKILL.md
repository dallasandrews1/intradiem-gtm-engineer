---
name: league-cfo-business-case
version: 1.0.0
description: CFO Economic Impact Statement builder. Triggers once Economic Buyer identified. Extracts economic data from transcripts (members, costs, churn, vendors, budgets) and generates 1-page business case with Current State, Projected Impact, Cost of Inaction, and Implementation Timeline.
---

## When this skill applies

- Trigger immediately upon identification of Economic Buyer (CFO, VP Finance, VP Operations)
- Run after first conversation with Economic Buyer where financial metrics are discussed
- Run when prospect shares budget constraints or financial targets
- Run before any business case presentation or formal proposal stage

## Background

The CFO Business Case skill converts operational insights into financial language. It extracts numbers from call transcripts, contextualizes them against League's value drivers, and builds a 1-page document that speaks to the CFO's primary incentive: cost relief and operational efficiency. This is the bridge between clinical/operational discovery and financial justification.

## Workflow Steps

1. **Extract Economic Data from Transcripts**
   - Pull all quantified metrics mentioned:
     - Total covered members or lives
     - Annual total cost of care (PMPM or total)
     - Current member engagement or activation rate
     - Projected churn rate or member attrition
     - Current staffing (call center, member services, digital operations)
     - Vendor costs (current engagement platform, care management, etc.)
     - Budget allocation for member experience or digital initiatives
     - Any stated cost reduction targets
   - Flag missing data as "Ask on Next Call"

2. **Identify Pain-Driven ROI Lever**
   - From discovery conversations, identify which operational cost is largest pain point:
     - FTE staffing costs (member services, call center)
     - Call center volume and cost per call
     - Vendor redundancy (paying for multiple tools doing same thing)
     - Engagement gap costing churn or medical waste
   - This becomes the primary ROI lever in the business case

3. **Build Current State Section**
   - Create 3-5 line summary of prospect's baseline metrics
   - Format: "250K covered members. 18% engagement rate. Annual member services cost: $2.1M (call center + digital). Current engagement platform: Castlight ($150K annual)."
   - Use only numbers extracted directly from prospect conversation or their website

4. **Calculate Projected Impact (Use League Value Prop Data)**
   - From League_Payer_Value_Prop.pdf, extract League's typical impact metrics:
     - Engagement uplift (e.g., "3-8 point engagement increase")
     - FTE cost reduction (e.g., "15-25% reduction in member services cost through automation")
     - Vendor cost consolidation (e.g., "replace 2-3 point solutions with League, reduce annual vendor spend 20-30%")
     - Churn reduction (if engagement-driven)
   - Calculate prospect-specific impact by applying League's ranges to their baseline numbers
   - Example: "Your 250K members at current 18% engagement. If League drives 5-point uplift to 23%, that's 12.5K additional engaged members. If engagement prevents 0.5 point annual churn, that's 1.25K members retained. At $12K PMPM, that's $15M retained medical value. Member services cost reduction: At 20% reduction on $2.1M, that's $420K annual savings."

5. **Calculate Cost of Inaction (Monthly Dollar Impact)**
   - Project what the engagement gap costs them monthly
   - Example: "Disengaged members have 40% higher medical cost. Your 205K disengaged members (82% at current 18% engagement) represent $82M in avoidable medical cost annually. That's $6.8M monthly cost of inaction."
   - Frame this as "monthly bleed" rather than annual, to trigger urgency

6. **Build Implementation Timeline**
   - Create realistic timeline with key gates and effort:
     - Implementation: 4-6 weeks (data integration, member communications, system configuration)
     - Procurement/Legal: 3-4 weeks (contract negotiation, InfoSec review, indemnification)
     - InfoSec: 2-3 weeks (data security, breach liability, compliance audit)
     - Technical Scoping: 2 weeks (API design, data model, integration validation)
     - Executive Sign-Off: 1-2 weeks
     - Buffers: 1 week
     - Total: 14-20 weeks from kickoff to go-live
   - Highlight what triggers the longest gate (usually Procurement or InfoSec)

7. **Flag Data Gaps**
   - List any metrics you couldn't extract
   - Create "Ask on Next Call" list with specific questions to fill gaps

## Canon Constraints

- **Tenbit++ Framework**: All external communications follow Observation → Insight → Value → Next Step
- **Pincer Rule**: Communications to VPs and Directors focus strictly on Operational Relief, never Brand Vision
- **Brand-Light Execution**: Do NOT mention League by name in early outreach (Days 1-5). Frame solution as category.
- **FORBIDDEN WORDS**: Never use leverage, synergy, cutting-edge, best-in-class, empower, seamless, robust, transform, transformation, catalyst, paradigm, innovative, or comprehensive
- **Strict Punctuation**: Periods and commas only inside narrative paragraphs. No hyphens or em dashes.
- **Named Outputs**: Every deliverable gets saved as a file. Nothing lives only in chat.
- **MEDDPICC Discipline**: After every call transcript, flag empty or weak MEDDPICC fields.

## Output

Save as: `[Account]_Business_Case.md`

Format:

```
# [Account Name] Economic Impact Statement
Date: [Date]
Economic Buyer: [Name, Title]

## Current State
[3-5 line summary of baseline metrics]
- Members: [X]
- Current Engagement Rate: [X%]
- Annual Member Services Cost: [X]
- Current Vendor Stack: [List]
- Total Annual Vendor Cost: [X]

## Projected Impact (12-Month Horizon)
- Engagement Uplift: [X to Y points] = [X additional engaged members]
- Member Services Cost Reduction: [X%] = [$X savings]
- Vendor Cost Consolidation: [X%] = [$X savings]
- Churn Reduction (if applicable): [X%] = [$X medical value retained]
- Total Annual Impact: [$X to $Y]

## Cost of Inaction
Monthly member services operational cost: [$X]
Monthly avoidable medical cost (disengaged members): [$X]
Total monthly impact: [$X]

## Implementation Timeline
- Technical Scoping: 2 weeks
- Data Integration and Setup: 4-6 weeks
- Procurement and Legal: 3-4 weeks
- InfoSec Review: 2-3 weeks
- Executive Sign-Off: 1-2 weeks
- Go-Live: [Estimated date]
- Total: 14-20 weeks from kickoff

## Data Gaps & Next Steps
- [Gap 1] - Ask: [Specific question]
- [Gap 2] - Ask: [Specific question]
- [Gap 3] - Ask: [Specific question]
```

## Examples

### Compliant Business Case
**Current State**: 180K covered members. 16% engagement rate. $1.8M annual member services cost. Current platform: Castlight ($120K annual).

**Projected Impact**: Engagement uplift 5-8 points to 21-24%. At 5-point uplift, 9K additional engaged members. Member services cost reduction 20% = $360K savings. Vendor consolidation (replace Castlight) = $120K savings. Total year 1 impact: $480K.

**Cost of Inaction**: 151K disengaged members. At 35% higher medical cost differential, that's $5.2M in avoidable annual medical cost. Monthly cost of inaction: $433K.

### Non-Compliant Business Case
"Account ABC will benefit from our cutting-edge, best-in-class platform that seamlessly transforms member engagement. We will empower your team to achieve innovative results. The business case speaks for itself."
Issue: Uses FORBIDDEN WORDS, no numbers, no operational metrics, no timeline, no cost structure.

### Compliant Cost of Inaction Language
"Your 151K disengaged members (at 16% current engagement) represent a medical cost premium. If disengaged members have 35% higher annual medical cost, that's approximately $5.2M in avoidable annual medical expenditure. Recovering even 2-3 points of engagement prevents $700K-$1M in annual medical waste."

### Non-Compliant Cost of Inaction
"Your engagement problem is urgent and you need to act now."
Issue: No quantification, vague, no mathematical support.
