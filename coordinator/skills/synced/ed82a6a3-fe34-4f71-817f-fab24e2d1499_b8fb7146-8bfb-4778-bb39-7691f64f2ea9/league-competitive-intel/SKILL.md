---
name: league-competitive-intel
version: 1.0.0
description: Competitive displacement orchestrator. Identifies competitor mentions (Epic, Accolade, Included Health, Wellframe, Castlight, build in-house, status quo) and generates counter-narrative briefs with wedge analysis, reframe positioning, and trap-setting talking points.
---

## When this skill applies

- Trigger immediately when a competitor is named in any call, email, or meeting notes
- Run after RFP review mentions competing solutions
- Run when prospect indicates they are "evaluating options"
- Run during competitive deal situations (pilot vs. competitor's pilot)

## Background

The Competitive Intel skill turns competitor mentions into strategic advantages. It diagnoses what the competitor will say, where they are strong, and critically, where they break. The skill then generates a wedge narrative (the gap) and trap-setting questions to plant doubt while positioning League as the operational fix.

## Workflow Steps

1. **Identify Competitor**
   - Parse call transcript, email, or deal note for explicit competitor mention
   - Map competitor to one of: Epic, Accolade, Included Health, Wellframe, Castlight, Internal Build, Status Quo
   - If competitor is unnamed ("we're looking at vendors"), apply Status Quo framing

2. **Extract Competitor Positioning**
   - Pull any language the prospect used to describe the competitor
   - Note what the competitor claimed or promised (from prospect's paraphrase)
   - Flag any product features or claims mentioned

3. **Build "What They Will Say" Section**
   - Based on competitor identity and prospect's language, write the competitor's likely value pitch
   - Include 2-3 talking points they typically lead with (e.g., Epic = "integrated EHR data," Accolade = "health coaching," Castlight = "plan navigation")
   - Stay clinical, peer-level. No mockery.

4. **Identify Where They Are Strong**
   - List 2-3 genuine strengths of the competitor
   - Be honest. Credibility requires acknowledging competitor's real advantages.
   - Example: "Epic has deep claims data integration; we match that through NCQA feeds, but integration takes 6-8 weeks."

5. **Identify The Wedge (Where They Break)**
   - Find the gap between competitor's claimed strength and reality
   - Examples of wedges:
     - "Accolade says coaching is their strength, but they have 2 FTE coaches per 50K members. At your scale (200K), that's 8 FTE coaches. Does that feel operationally realistic?"
     - "Castlight says they're integrated, but their integration is read-only navigation. They don't close the loop on conversion."
     - "Building in-house means you own the tech debt and the hiring risk. Who owns member engagement if your dev team is split between 3 projects?"
   - The wedge is always operational, not feature-based.

6. **Draft Questions to Plant**
   - Create 3-4 innocent-sounding questions for the prospect to ask the competitor
   - Questions should expose the wedge without revealing your strategy
   - Examples:
     - "How many FTE coaches do you allocate per member population at our scale?"
     - "Walk us through what integration with QNXT looks like in your platform. Real-time or batch?"
     - "If we go in-house, what's your typical engineering timeline for a member engagement MVP? And how many heads?"

7. **Build The Reframe (League Positioning)**
   - Write 2-3 sentences positioning League against this specific competitor's weakness
   - Apply Tenbit++ (Observation → Insight → Value → Next Step)
   - Example: "We know Accolade is strong at coaching, but at your member scale, staffing becomes the limit. We route members to the right intervention (coaching, navigation, clinical) based on NCQA data and claim patterns. You get coaching scale without the FTE bottleneck."
   - Never name League in the reframe. Use "we" and "our approach."

8. **Generate Trap-Setting Talking Points**
   - Create 4-5 peer-level statements Dallas can make in discovery calls that prime doubt
   - Statements should feel observational, not sales-y
   - Examples:
     - "Most vendors pitch coaching as their primary lever, but engagement drives 70% of impact. Coaching is secondary."
     - "Integration complexity is usually underestimated in build scenarios. Typical in-house timelines are 9-18 months before you see member adoption."
     - "Real-time integration requires EDI and SFTP refresh cycles. Most vendors can't deliver actual real-time."

## Canon Constraints

- **Tenbit++ Framework**: All external communications follow Observation → Insight → Value → Next Step
- **Pincer Rule**: Communications to VPs and Directors focus strictly on Operational Relief, never Brand Vision
- **Brand-Light Execution**: Do NOT mention League by name in early outreach (Days 1-5). Frame solution as category.
- **FORBIDDEN WORDS**: Never use leverage, synergy, cutting-edge, best-in-class, empower, seamless, robust, transform, transformation, catalyst, paradigm, innovative, or comprehensive
- **Strict Punctuation**: Periods and commas only inside narrative paragraphs. No hyphens or em dashes.
- **Named Outputs**: Every deliverable gets saved as a file. Nothing lives only in chat.
- **MEDDPICC Discipline**: After every call transcript, flag empty or weak MEDDPICC fields.

## Output

Save as: `[Account]_Competitive_Brief.md`

Format:

```
# [Account Name] Competitive Brief
Date: [Date]
Competitor: [Epic/Accolade/Included Health/Wellframe/Castlight/Build In-House/Status Quo]
Deal Stage: [Current Stage]

## What They Will Say
[2-3 expected talking points from the competitor]

## Where They Are Strong
1. [Genuine strength 1]
2. [Genuine strength 2]
3. [Genuine strength 3]

## The Wedge (Where They Break)
[Narrative paragraph identifying the operational gap]

## Questions to Plant
- [Question 1 for prospect to ask competitor]
- [Question 2 for prospect to ask competitor]
- [Question 3 for prospect to ask competitor]
- [Question 4 for prospect to ask competitor]

## The Reframe (League Positioning)
[2-3 sentences positioning League's operational advantage without naming League]

## Trap-Setting Talking Points (Dallas Use Only)
- [Observation 1 to plant doubt]
- [Observation 2 to plant doubt]
- [Observation 3 to plant doubt]
- [Observation 4 to plant doubt]
- [Observation 5 to plant doubt]

## Next Steps
[How Dallas should deploy this brief in next call or email]
```

## Examples

### Compliant Competitive Brief (Accolade)
**The Wedge**: "Accolade staffs 1 coach per 25K members. At a 200K population, that's 8 FTE coaches. Health plan coaching is expensive relative to scale. As you grow, coaching becomes a cost center, not a margin driver."

**Trap-Setting Talking Point**: "We've noticed that coaching works best for 5-7% of engaged members. Scaling coaching FTE to reach 30% of your population typically requires hiring 3-4x more coaches. How do you balance that economics?"

### Non-Compliant Competitive Brief
"Accolade is inferior to us. Their coaching is limited and they'll never match our innovative platform. We're the best-in-class solution for member engagement."
Issue: Ad hominem attack, uses FORBIDDEN WORDS, no operational wedge, no trap-setting.

### Compliant Questions to Plant
- "Walk us through your coaching model. How many members does each coach actively engage per month?"
- "What percentage of your member base actually receives coaching at scale?"
- "If we wanted to expand coaching to 30% of our population, how many additional coaches would we need to hire?"

### Non-Compliant Questions
- "Isn't your coaching outdated?"
- "Don't you think your platform is inferior?"
Issue: Leading questions, no operational clarity, antagonistic tone.
