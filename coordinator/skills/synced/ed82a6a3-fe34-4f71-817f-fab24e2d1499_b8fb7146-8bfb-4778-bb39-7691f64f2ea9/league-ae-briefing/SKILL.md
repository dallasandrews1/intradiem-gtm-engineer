---
name: league-ae-briefing
version: 1.0.0
description: AE Briefing / Account Strike Packet. Generates 1-page forensic briefing with Primary Forcing Function, Playbook Hypothesis, Hidden Fear, Internal Enemy, and Strategic Intervention. Clinical tone, peer-level, output directly into chat for Slack channel copy.
---

## When this skill applies

- Run before initial outreach to any new Tier-1 account
- Run when opening a new deal or account within Tier-1 list
- Run when preparing for first call with new prospect
- Run when strategy needs recalibration mid-deal

## Background

The AE Briefing skill creates a one-page account diagnosis that Dallas can reference before every call. It identifies the operational pain that drives the deal (Forcing Function), the account's likely solution playbook (which competitor/build approach they'll evaluate), their unstated fear (what goes wrong if they pick wrong), the internal blocker (political resistance), and the specific intervention Dallas should use to unlock the deal.

## Workflow Steps

1. **Diagnose Primary Forcing Function**
   - From public research, analyst reports, earnings calls, and industry trends, identify the #1 operational pressure facing this account
   - Forcing functions are typically: cost reduction, regulatory pressure, market consolidation, technology obsolescence, talent crisis, engagement/retention gap, compliance violation, Star Rating decline
   - Be specific: "Member engagement is down 3 points YoY and driving churn" is better than "engagement gap"
   - This is NOT a sales problem. This is the account's real business problem.
   - Example: "Medicaid rate cuts in 3 states create $2M annual margin pressure. Engagement/retention is the highest-leverage cost lever."

2. **Hypothesize the Playbook (Solution They'll Evaluate)**
   - Based on forcing function and account size, predict which solution playbook they'll pursue
   - Common playbooks:
     - **TSA Exit**: Leaving Traditional Service Area (Medicaid) for Medicare. Need consumer-first engagement and retention.
     - **Microsoft Pivot**: Migrating to Azure/Fabric. Need cloud-native data applications that integrate with Microsoft stack.
     - **Wrapper Moat**: Building moat around legacy systems (Epic, HealthEdge) with consumer layer. Need to wrap legacy with modern UX.
     - **Labor Substitution**: Reducing FTE in member services/call center. Need automation and self-service that actually works.
     - **Care Redesign**: Shifting to value-based care or specialized verticals. Need engagement/activation for new care model.
   - Example: "Centene will likely pursue Labor Substitution + Care Redesign. They're moving into specialized verticals (oncology, behavioral) where member engagement and navigation are critical but staffing is expensive."

3. **Identify Hidden Fear (Unstated Anxiety)**
   - Hidden fear is what keeps the buying committee up at night that they won't say in discovery calls
   - Usually: wrong vendor pick creates expensive rip-and-replace, new CEO will inherit failed project, board will question ROI, integration will delay critical timeline
   - Be clinical. These are legitimate risks.
   - Example: "Hidden fear: Engaging with a consumer-first vendor is new. What if our IT team can't integrate it? What if we pick wrong and CEO 2.0 kills it?"

4. **Identify Internal Enemy (Political Resistance)**
   - Diagnose which internal stakeholder or group will resist change
   - Resistance usually comes from: incumbent vendor sponsor (IT leader defending HealthEdge), labor union (worried about job cuts), incumbent vendor champion (marketing director defending Castlight), data/analytics team (worried about new integration)
   - Example: "Internal Enemy: VP IT has deep relationship with HealthEdge integrator. Will recommend "build it ourselves" to avoid vendor dependency and protect integrator relationship."

5. **Build Strategic Intervention**
   - Design the specific intervention Dallas uses to unlock the deal
   - Interventions target the forcing function, overcome the hidden fear, and neutralize the internal enemy
   - Example intervention: "Our strategic intervention: Bypass IT/HealthEdge integrator by positioning League as 'consumer layer, not platform layer.' This removes integration risk. Target CFO + VP Member Experience. Frame as operational cost relief (Labor Substitution) with zero platform risk. Internal Enemy (VP IT/integrator) is excluded from decision because this isn't a platform play."

6. **Document Deal Playbook & Pacing**
   - Outline the likely deal progression and buying committee motion
   - Predict timing: When will each Tier become engaged? Which gate takes longest (usually Procurement/Legal)?
   - Identify wildcard risks that could stall deal

## Canon Constraints

- **Tenbit++ Framework**: All external communications follow Observation → Insight → Value → Next Step
- **Pincer Rule**: Communications to VPs and Directors focus strictly on Operational Relief, never Brand Vision
- **Brand-Light Execution**: Do NOT mention League by name in early outreach (Days 1-5). Frame solution as category.
- **FORBIDDEN WORDS**: Never use leverage, synergy, cutting-edge, best-in-class, empower, seamless, robust, transform, transformation, catalyst, paradigm, innovative, or comprehensive
- **Strict Punctuation**: Periods and commas only inside narrative paragraphs. No hyphens or em dashes.
- **Named Outputs**: Every deliverable gets saved as a file. Nothing lives only in chat.
- **MEDDPICC Discipline**: After every call transcript, flag empty or weak MEDDPICC fields.

## Output

Output directly into chat. Copy entire briefing into Slack channel for team alignment. Format:

```
# [Account Name] Strike Packet
Date: [Date]
AE: Dallas Andrews

## Primary Forcing Function
[1 paragraph describing the #1 operational pain driving this account]

## Playbook Hypothesis
The account will likely pursue: [TSA Exit / Microsoft Pivot / Wrapper Moat / Labor Substitution / Care Redesign]
Rationale: [1-2 sentences explaining why this playbook fits their situation]

## Hidden Fear
[1 paragraph describing the unstated anxiety of the buying committee]

## Internal Enemy
[Name/Title/Department] resists this solution because [1-2 sentence explanation]
Their leverage: [What gives them political power]
Our intervention: [How we neutralize this resistance]

## Strategic Intervention
To unlock this deal, Dallas should:
1. [Specific action 1]
2. [Specific action 2]
3. [Specific action 3]

Target: [Which Tier of buying committee to target first]
Angle: [The operational narrative to lead with]
Timeline: [Expected sales cycle length]

## Deal Playbook
Phase 1 [Week X]: [First call, discovery, who engaged]
Phase 2 [Week X]: [Technical eval, second Tier engagement]
Phase 3 [Week X]: [Business case presentation, Economic Buyer engagement]
Phase 4 [Week X]: [Procurement/Legal gates]
Phase 5 [Week X]: [Go-live decision]

## Wildcard Risks
1. [Risk 1 and mitigation]
2. [Risk 2 and mitigation]
3. [Risk 3 and mitigation]
```

## Examples

### Compliant Strike Packet (Medicaid Plan)
**Forcing Function**: Medicaid rate cuts in 4 states (14% reduction). Margin pressure forces cost reduction across member services. Current member engagement is 16% and declining, driving unnecessary churn.

**Playbook Hypothesis**: Labor Substitution + Wrapper Moat. They'll invest in automation and consumer-first UX to reduce member services FTE and improve engagement with legacy Epic data.

**Hidden Fear**: New CEO doesn't understand digital health. Selecting a vendor without IT validation risks "he'll kill the project if it doesn't hit ROI in first 90 days."

**Internal Enemy**: VP IT and Epic integrator. They'll recommend "build it ourselves" to avoid vendor risk. They've underestimated integration timelines on past projects.

**Strategic Intervention**: Position League as consumer layer, not platform. Removes integration risk and IT validation burden. Lead with CFO (margin relief) + VP Member Experience (engagement uplift). Frame as labor cost reduction with zero platform architecture risk. Timeline: 90-120 days.

### Compliant Strike Packet (Medicare Advantage)
**Forcing Function**: Star Ratings down 0.5 points YoY. Engagement metric (HOS coverage) is below 50th percentile. CMS rate cut announced for 2027. Board is questioning competitive strategy.

**Playbook Hypothesis**: Care Redesign + Engagement. Pivoting to carve-out model for high-cost conditions (COPD, CHF, diabetes). Engagement and personalized care navigation are critical to success.

**Hidden Fear**: CMO is skeptical that consumer engagement can move clinical outcomes. Worried that "engagement startup" will overpromise and underdeliver on clinical impact.

**Internal Enemy**: Chief Medical Officer and care management team. They see engagement as marketing gimmick, not clinical lever. Will resist vendor solution, prefer internal build.

**Strategic Intervention**: Establish credibility with CMO first. Get clinical data showing engagement-to-outcome correlation (NCQA, publicly available). Position League as clinical data activation tool, not marketing platform. Lead with CMO, not member experience. Timeline: 60-90 days.

### Non-Compliant Strike Packet
"Account XYZ needs our innovative, cutting-edge platform to transform their member engagement. We should tell them about our best-in-class technology. This is a great opportunity to discuss our comprehensive solution."
Issue: Uses FORBIDDEN WORDS, brand-centric, no forcing function, no internal politics, no strategic intervention, no specific account context.

### Compliant Hidden Fear Language
"Hidden fear: New leadership team doesn't know if they picked the right vendor. If engagement metrics don't improve in 90 days, the new CEO will blame the vendor and start a competitor evaluation. We need to lock in early wins and baseline metrics."

### Non-Compliant Fear Language
"They're worried that we won't deliver. Let's tell them how great we are."
Issue: Generic fear, no political/organizational context, no specificity.
