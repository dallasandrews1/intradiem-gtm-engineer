---
name: league-meddpicc
version: 1.0.0
description: MEDDPICC Hygiene Pass. Runs after every Discovery Call and significant mid-funnel calls. Populates all 8 MEDDPICC fields with Salesforce text and confidence ratings (Strong/Moderate/Gap). Generates Gap Report with specific follow-up questions.
---

## When this skill applies

- Run after every discovery call
- Run after any multi-stakeholder call or significant prospect meeting
- Run after RFP response or formal demo
- Run weekly during active deals to track MEDDPICC evolution
- Run when deal stalls to diagnose which MEDDPICC field is weak

## Background

The MEDDPICC Hygiene skill enforces rigor in deal diagnosis. By systematically documenting all 8 MEDDPICC fields after every call, Dallas maintains a clear map of deal health and identifies which conversations unlock stuck opportunities. Weak fields become targeted discovery questions for the next call.

## Workflow Steps

1. **Gather Call Inputs**
   - Extract full call transcript (or detailed call notes if transcript unavailable)
   - Identify all participants (name, title, role archetype)
   - Note key statements and quantified metrics mentioned
   - Flag any objections, concerns, or decision criteria mentioned

2. **Populate Metrics Field**
   - Extract every quantified metric prospect mentioned
   - Include: member count, member engagement rate, cost per member, PMPM, call center volume, churn rate, Net Promoter Score, Star Ratings, Any% engagement, etc.
   - Pull direct quote from transcript: "Our engagement rate is 22% and we're targeting 25%"
   - Confidence rating: Strong (multiple metrics confirmed by different stakeholders), Moderate (one or two metrics mentioned), Gap (no metrics discussed)
   - Add context: "What metrics matter most to them?" and "Which metrics does League move?"

3. **Populate Economic Buyer Field**
   - Identify the person with approval authority and budget control
   - Include name, title, department, reporting line if mentioned
   - Note if Economic Buyer participated in call (Strong) or was referenced but not present (Moderate) or unknown (Gap)
   - If not yet identified, note: "Gap: Economic Buyer not yet identified"
   - Add context: "Who controls the budget?" and "When can we access CFO/VP Finance?"

4. **Populate Decision Criteria Field**
   - Extract every selection criterion mentioned
   - Examples: "Must integrate with Epic," "Must support [specific workflow]," "Must have single sign-on," "Must reduce cost," "Must improve NPS"
   - Direct quote from transcript: "We won't move forward unless the platform integrates real-time with Epic"
   - Confidence rating: Strong (multiple criteria confirmed, prioritized), Moderate (some criteria mentioned), Gap (no criteria stated)
   - Add context: "Are there hidden criteria?" and "Which criteria does League meet?"

5. **Populate Decision Process Field**
   - Map the path to approval
   - Answer: How many approval layers? Which stakeholders must sign off? What's the timeline? Are there gates (Procurement, Legal, InfoSec)?
   - Example: "VP Member Experience decides. VP IT must validate integration. CFO approves budget. Timeline: 120 days target go-live."
   - Confidence rating: Strong (full process documented), Moderate (partial process known), Gap (process unclear)
   - Add context: "Who controls the timeline?" and "What's the longest gate?"

6. **Populate Paper Process Field**
   - Identify legal and procurement gates
   - Answer: Will they use MSA or require standard contract? RFP required? InfoSec questionnaire? Procurement SLA? Legal review timeline?
   - Example: "Standard RFP process. Legal will review contract for 4 weeks. InfoSec questionnaire required. Procurement typically 3-4 weeks."
   - Confidence rating: Strong (gates documented with timelines), Moderate (some gates identified), Gap (paper process unknown)
   - Add context: "Who owns Legal?" and "What's the InfoSec risk?"

7. **Populate Identified Pain Field**
   - Extract every pain point mentioned (clinical, operational, member experience, financial)
   - Examples: "Member engagement is down 3 points," "Call center cost is unsustainable," "Digital member portal is fragmented," "We can't track member behavior post-visit"
   - Direct quote from transcript: "Our member services team is overwhelmed. We have 10 FTE managing 200K members."
   - Confidence rating: Strong (pain is quantified and confirmed by multiple stakeholders), Moderate (pain mentioned but not quantified), Gap (no pain stated)
   - Add context: "Is this pain bad enough to buy?" and "Who feels this pain most?"

8. **Populate Champion Field**
   - Identify the primary internal advocate (usually mid-level operator, director, or VP without final authority)
   - Include name, title, department, motivation (what's their personal win)
   - Note if champion is truly committed to League or just evaluating options (Strong vs. Moderate)
   - Example: "VP Digital Health Sarah Martinez. Her goal: reduce call center cost 20%. She benefits from engagement uplift and NPS improvement."
   - Confidence rating: Strong (champion is committed, has influenced peers), Moderate (champion is interested but untested), Gap (no champion yet)
   - Add context: "Is this person credible with Economic Buyer?" and "Does champion need help with peer influence?"

9. **Populate Competition Field**
   - Identify named competitors or competitive dynamics
   - Examples: "Evaluating Accolade and Wellframe," "Building in-house," "Status quo (staying with Castlight)," "No active competition (sole vendor)"
   - Note competitor's positioning and strengths as mentioned by prospect
   - Confidence rating: Strong (competitor named and positioned), Moderate (competitor category mentioned), Gap (no competition mentioned)
   - Trigger: If competitor named, run league-competitive-intel immediately
   - Add context: "How do we differentiate?" and "What's competitor's weakness?"

10. **Create Confidence Matrix**
    - For each of 8 MEDDPICC fields, rate confidence: Strong / Moderate / Gap
    - Strong = Multiple sources, direct quotes, quantified, confirmed by multiple stakeholders
    - Moderate = Mentioned once or twice, partially quantified, from single source
    - Gap = Not discussed, unknown, or contradictory information

11. **Generate Gap Report & Next Questions**
    - For each Moderate or Gap field, create 1-2 discovery questions for next call
    - Assign ownership: Dallas asks CEO, Champion asks CFO, BDR asks IT, etc.
    - Prioritize: Which gaps must be closed before moving to next stage?
    - Example Gap: "Economic Buyer not yet engaged. Next step: Ask Champion to loop in CFO for budgeting and approval discussion. Dallas to send Economic Buyer context email on 90-day ROI."

## Canon Constraints

- **Tenbit++ Framework**: All external communications follow Observation → Insight → Value → Next Step
- **Pincer Rule**: Communications to VPs and Directors focus strictly on Operational Relief, never Brand Vision
- **Brand-Light Execution**: Do NOT mention League by name in early outreach (Days 1-5). Frame solution as category.
- **FORBIDDEN WORDS**: Never use leverage, synergy, cutting-edge, best-in-class, empower, seamless, robust, transform, transformation, catalyst, paradigm, innovative, or comprehensive
- **Strict Punctuation**: Periods and commas only inside narrative paragraphs. No hyphens or em dashes.
- **Named Outputs**: Every deliverable gets saved as a file. Nothing lives only in chat.
- **MEDDPICC Discipline**: After every call transcript, flag empty or weak MEDDPICC fields.

## Output

Save as: `[Account]_MEDDPICC_Update.md`

Format:

```
# [Account Name] MEDDPICC Update
Date: [Call date]
Participants: [Names, titles]
Call Duration: [Minutes]

## MEDDPICC Confidence Matrix

| Field | Status | Confidence | Key Evidence | Notes |
|-------|--------|------------|--------------|-------|
| **Metrics** | [Value] | Strong/Moderate/Gap | [Direct quote] | [Context] |
| **Economic Buyer** | [Name, Title] | Strong/Moderate/Gap | [Evidence] | [Context] |
| **Decision Criteria** | [Criteria list] | Strong/Moderate/Gap | [Evidence] | [Context] |
| **Decision Process** | [Timeline/Steps] | Strong/Moderate/Gap | [Evidence] | [Context] |
| **Paper Process** | [Gates] | Strong/Moderate/Gap | [Evidence] | [Context] |
| **Identified Pain** | [Pains] | Strong/Moderate/Gap | [Evidence] | [Context] |
| **Champion** | [Name, Title] | Strong/Moderate/Gap | [Evidence] | [Context] |
| **Competition** | [Competitors] | Strong/Moderate/Gap | [Evidence] | [Context] |

## Gap Report & Next Steps

### High Priority Gaps (Close Before Next Stage)
1. **Gap**: [Field name]. **Question**: [Specific question to answer]. **Owner**: [Dallas/Champion/BDR]. **Timing**: [Next call/email].
2. [Repeat for each high-priority gap]

### Moderate Priority Gaps (Close During Sales Cycle)
1. **Gap**: [Field name]. **Question**: [Question]. **Owner**: [Owner]. **Timing**: [Timing].
2. [Repeat]

### Confidence Summary
- Strong fields: [List]
- Moderate fields: [List]
- Gap fields: [List]

## Deal Health Assessment
[1-2 sentence evaluation of deal momentum and risk factors]

## Next Call Agenda
Based on gaps identified:
1. [Topic 1 with MEDDPICC field]
2. [Topic 2 with MEDDPICC field]
3. [Topic 3 with MEDDPICC field]
```

## Examples

### Compliant MEDDPICC Entry (Metrics Field)
**Status**: 250K covered lives, 18% engagement rate, $2.1M annual member services cost
**Confidence**: Strong
**Evidence**: "Our engagement rate is currently 18%. We have 250,000 covered members. Member services cost us $2.1M annually." — VP Operations, call transcript
**Notes**: Multiple metrics confirmed. These are the key operational metrics. Need to understand which metrics drive her KPIs.

### Compliant MEDDPICC Entry (Economic Buyer Field)
**Status**: CFO John Smith, reporting to CEO, controls $50M annual discretionary budget
**Confidence**: Moderate
**Evidence**: VP Operations mentioned CFO must approve vendor decisions. CFO has not participated yet.
**Notes**: Champion confident CFO will engage after technical demo. Next step: Have champion set up CFO meeting for business case walkthrough.

### Compliant MEDDPICC Entry (Competition Field)
**Status**: Actively evaluating Accolade. Status quo (Castlight platform). Discussed internal build option.
**Confidence**: Strong
**Evidence**: "We're in pilot with Accolade. Castlight is our current platform. And we're exploring if we can build this internally." — SVP Member Experience
**Notes**: Three competitive paths. Accolade is furthest along (pilot). TRIGGER: Run league-competitive-intel for Accolade wedge analysis. Build in-house is legitimate risk (internal champion is tech team).

### Non-Compliant MEDDPICC Entry
**Status**: They need member engagement.
**Confidence**: Gap
**Evidence**: None
**Notes**: Vague, not quantified, no direct quote, no source credibility.
Issue: Not specific enough, no metrics, confidence rating doesn't match lack of evidence.

### Compliant Gap Report Entry
**Gap**: Economic Buyer not yet engaged. CFO approval required for final sign-off.
**Question for Next Call**: "When can we present the 90-day financial impact to your CFO? What's his timeline for this decision?"
**Owner**: Champion (VP Ops) to schedule CFO meeting. Dallas to prepare 1-page business case before meeting.
**Timing**: Next week. Get on CFO calendar within 5 business days.
**Priority**: High. Can't move to procurement without Economic Buyer buy-in.

### Non-Compliant Gap Report Entry
**Gap**: We need to understand their business better.
**Question**: General inquiry about their situation.
**Owner**: Dallas will figure it out.
**Timing**: Eventually.
Issue: Vague gap, no specific question, no clear owner, no deadline.
