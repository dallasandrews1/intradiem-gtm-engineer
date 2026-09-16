---
name: league-post-discovery
description: Post-Discovery Follow-Up orchestrator. Runs immediately after multi-stakeholder Discovery Calls. Produces a Forwardable Recap email (BLUF + Assigned Next Steps + Top Problems/Solutions) for the full room, then individual 1:1 follow-up emails per stakeholder, plus Salesforce Activity summary. The recap anchors the deal narrative; the 1:1s deepen individual threads. Trigger on any post-disco follow-up, recap email, discovery debrief, "send the follow-ups," "write the recap," or any request to summarize and follow up after a multi-stakeholder call.
---

## When this skill applies

- Run immediately after multi-stakeholder discovery calls (same day)
- Run after any group call involving 3+ prospect stakeholders
- Run after RFP or formal discovery kickoff
- Use for first deep technical or financial evaluation calls

## Background

The Post-Discovery Follow-Up skill runs a two-layer follow-up sequence after every multi-stakeholder discovery call.

**Layer 1: Forwardable Recap (group email, sent first).** A single email to the full room that anchors the deal narrative. Three sections: a one-sentence BLUF painting the buyer's future state in their own words, assigned next steps with the buyer's action listed first, and the top 2-3 problems surfaced on the call with a quick nod to what a solution looks like. The entire email must pass the "forward to your boss" test. A VP should be able to send it to their CFO or CEO without editing a word. This is the artifact that lives in the prospect's inbox and gets referenced in every internal meeting from here forward.

**Layer 2: Individual 1:1 Follow-Ups (sent 1-2 hours after the recap).** Personalized emails to each stakeholder that reference their specific concern, metric interest, and something they personally said on the call. This multi-threading approach builds peer-level credibility across the buying committee and accelerates deal velocity. The 1:1s are NOT recaps. They deliver value specific to that person.

The recap anchors. The 1:1s deepen. Together they pincer the follow-up.

## Workflow Steps

1. **Extract Stakeholder List**
   - From call transcript or notes, identify every participant
   - For each, capture: Full name, title, department, reporting line (if mentioned)
   - Note if they spoke frequently (engaged) or minimally (less engaged)

2. **Categorize by Role Archetype**
   - **CFO/VP Finance**: Focused on ROI, payback period, cost avoidance, vendor costs
   - **VP Operations**: Focused on workflow efficiency, FTE reduction, timeline, implementation complexity
   - **VP Digital Health/Member Experience**: Focused on engagement metrics, NPS, retention, member feedback
   - **CTO/VP IT**: Focused on integration complexity, API capabilities, data security, scalability, tech stack alignment
   - **General Counsel**: Focused on contract terms, indemnification, compliance, liability
   - **Chief Medical Officer**: Focused on clinical outcomes, evidence base, member safety, clinical workflows
   - **Champion**: Mid-level advocate, usually VP or Director, advocates internally, primary point of contact

3. **Extract Primary Concern per Stakeholder**
   - From call transcript, identify what each stakeholder asked about, challenged, or expressed concern about
   - Examples: "CTO asked 3 questions about API latency and data security" = CTO's primary concern is technical risk
   - "CFO asked about payback period and ROI" = CFO's primary concern is financial justification
   - "VP Operations asked about implementation timeline" = VP Ops' primary concern is disruption and speed

4. **Identify Metric Interest per Stakeholder**
   - Which metrics did each stakeholder ask about or care about?
   - CFO cares about: ROI, payback period, cost avoidance, vendor cost
   - VP Ops cares about: FTE reduction, process automation, member services cost
   - VP Digital Health cares about: Engagement rate, NPS, retention, member satisfaction
   - CTO cares about: Integration timeline, API availability, security certifications
   - CMO cares about: Clinical outcomes, evidence base, member safety metrics

5. **Draft the Forwardable Recap Email (Layer 1, send first)**

   This is a group email to all call participants. It is sent BEFORE the 1:1 follow-ups.

   ### Structure (three sections, in this order):

   **Section 1: BLUF (Bottom Line Up Front)**
   - One sentence painting the buyer's future state, in the buyer's own words from the call.
   - This is NOT a summary of the meeting. It is a vision statement of where the prospect is headed.
   - Use language the prospect actually used on the call. Mirror their framing, not yours.
   - Format: "Based on our conversation, [Prospect Org] is working toward [their stated future state]."
   - The prospect is the hero. You are reflecting their ambition back to them.

   **Section 2: Next Steps (Assigned)**
   - Lead with the buyer's action items first, then yours. This signals respect and positions the buyer as driving the process.
   - Every item has: [Owner Name]: [Specific action] by [date or timeframe].
   - If no date was committed on the call, use "by [reasonable date]" and flag it as tentative.
   - Keep to 3-5 items maximum. If more exist, group minor items under a single line.

   **Section 3: What We Heard (Top Problems + Solutions)**
   - Maximum 3 items. These must be actual problems surfaced on the call, not features or "wants."
   - The test: would the prospect's boss read this and say "yes, those are real problems we need to solve"?
   - Format each as: **[Problem in plain language]**: [One sentence describing what a path forward looks like. No product pitch. Category-level framing.]
   - Problems should be ordered by urgency as expressed on the call, not by your sales priority.

   ### Recap Rules:
   - Length: 150-200 words maximum. Skimmable. Every sentence earns its place.
   - Tone: Peer-to-peer, consultative. You are a strategic partner documenting shared understanding, not a vendor confirming requirements.
   - The "forward to your boss" test: Before finalizing, ask — could a VP on this call forward this email to their CEO or CFO without editing a single word? If no, rewrite.
   - Brand-light: League may be mentioned once in the sign-off if the prospect has already engaged with League directly. Otherwise, no company name in the body.
   - No selling in the recap. Zero product language. This is a mirror, not a pitch.
   - Close with: "Anything I missed or got wrong? Want to make sure we're aligned before [next step]."
   - This closing invites correction and positions the prospect as the authority.

6. **Draft Individual 1:1 Follow-Up Emails (Layer 2, send 1-2 hours after recap)**
   - Create separate email for each stakeholder
   - Structure: Thank you for specific contribution → Acknowledge their concern → Address their specific metric interest → Next step
   - Apply Tenbit++ (Observation → Insight → Value → Next Step)
   - Language: Peer-to-peer, professional, reference something they specifically said in the call
   - Length: 80-120 words (short, email 1 of sequence)
   - Never mention League by name (brand-light)
   - Include specific CTA (coffee chat, technical deep-dive, business case preview)
   - These emails must NOT repeat the recap. They go deeper on that person's specific thread.

7. **Draft Champion-Specific Follow-Up**
   - Champion email is slightly different: Acknowledge their champion role, offer support for internal coalition building
   - Structure: Thank you for leading the discussion → We're here to support your internal conversations → Offer flexibility on next steps → Soft CTA
   - Example: "Thanks for leading the discovery. We see an operational fit with your cost reduction goal. As you continue internal conversations, we're happy to support with executive summaries, technical deep-dives, or formal business cases. What would be most helpful as you align your team? Flexible on timing and format."

8. **Generate Salesforce Activity Summary**
   - Create log of call, participants, key outcomes, and next steps
   - Include: Call date/time, participants, key takeaways per stakeholder, MEDDPICC gaps (if applicable), next milestone

## Canon Constraints

- **Tenbit++ Framework**: All external communications follow Observation → Insight → Value → Next Step
- **Pincer Rule**: Communications to VPs and Directors focus strictly on Operational Relief, never Brand Vision
- **Brand-Light Execution**: Do NOT mention League by name in early outreach (Days 1-5). Frame solution as category.
- **FORBIDDEN WORDS**: Never use leverage, synergy, cutting-edge, best-in-class, empower, seamless, robust, transform, transformation, catalyst, paradigm, innovative, or comprehensive
- **Strict Punctuation**: Periods and commas only inside narrative paragraphs. No hyphens or em dashes.
- **Named Outputs**: Every deliverable gets saved as a file. Nothing lives only in chat.
- **MEDDPICC Discipline**: After every call transcript, flag empty or weak MEDDPICC fields.
- **Recap is a mirror, not a pitch**: The Forwardable Recap contains zero product language. It reflects the prospect's problems back in the prospect's words. Selling happens in the 1:1s.

## Output

Save as: `[Account]_Discovery_Follow_Ups.md`

Format:

```
# [Account Name] Post-Discovery Follow-Ups
Date of Discovery Call: [Date]
Participants: [List all names and titles]

## Stakeholder Analysis

### [Stakeholder Name] | [Title]
- **Role Archetype**: [CFO/VP Ops/VP Digital Health/CTO/General Counsel/CMO/Champion]
- **Primary Concern**: [What they cared about most in the call]
- **Metric Interest**: [Which KPIs matter to them]
- **Engagement Level**: [High/Moderate/Low based on call participation]

[Repeat for each stakeholder]

---

## Forwardable Recap Email (Send First — To Full Room)

**To:** [All participant emails]
**Subject:** [Account Name] Discovery Recap + Next Steps

Hi [Primary Contact First Name] and team,

[BLUF: One sentence. Buyer's future state, in their words.]

**Next Steps:**
- **[Buyer Name]**: [Action] by [date]
- **[Buyer Name 2]**: [Action] by [date]
- **[Dallas/League]**: [Action] by [date]

**What We Heard:**
- **[Problem 1]**: [One-sentence path forward, category-level]
- **[Problem 2]**: [One-sentence path forward, category-level]
- **[Problem 3]**: [One-sentence path forward, category-level]

Anything I missed or got wrong? Want to make sure we're aligned before [next step].

Dallas

---

## Individual 1:1 Follow-Up Emails (Send 1-2 Hours After Recap)

### To: [Stakeholder Name], [Title]
Subject: [Specific, personalized subject - reference their concern]

[Email body 80-120 words]

---

[Repeat for each stakeholder]

## Champion Follow-Up (If Applicable)

### To: [Champion Name], [Title]
Subject: [Subject acknowledging champion role]

[Champion-specific email body]

---

## Salesforce Activity Summary

**Call Date**: [Date and time]
**Duration**: [Minutes]
**Participants**: [List]
**Organizer**: [Who set it up]

**Key Outcomes by Stakeholder**:
- [Stakeholder name]: [Key takeaway]
- [Stakeholder name]: [Key takeaway]
- [Stakeholder name]: [Key takeaway]

**MEDDPICC Gaps Identified**: [List any gaps from call]

**Next Milestone**: [What's the next step and when]

**Deal Health**: [1-2 sentence assessment]
```

## Examples

### Compliant Forwardable Recap Email
**Account**: Midwest Health Partners
**Call**: Discovery with VP Ops, CTO, CFO, VP Digital Health
**Subject**: Midwest Health Discovery Recap + Next Steps

"Hi Derrick and team,

Based on our conversation, Midwest Health is working toward a single member experience that eliminates the 7-system toggle your service reps deal with today and gives members one front door to navigate benefits, find care, and manage claims.

**Next Steps:**
- **Derrick**: Share the 3-slide overview with Ericka and Shawn and confirm Wednesday availability by Friday
- **Sarah**: Send current integration architecture doc to Dallas by Monday
- **Dallas**: Prepare preliminary cost model scoped to Midwest's 1.2M member base by Wednesday

**What We Heard:**
- **Rep productivity is bleeding margin**: Service reps toggle across 7 systems per call, adding 4-6 minutes of handle time. A unified member platform would collapse those workflows into one screen.
- **Member engagement is flat despite investment**: Portal adoption sits at 12% and digital campaigns aren't moving the needle. The gap is navigation, not content. Members need a single entry point, not more emails.
- **Build vs. buy decision is stuck**: Internal dev estimated 18-24 months and $4M+ to build what's needed, but the team hasn't benchmarked that against external options.

Anything I missed or got wrong? Want to make sure we're aligned before Wednesday.

Dallas"

**Why this is compliant:** BLUF uses the prospect's own language ("single member experience," "one front door"). Buyer's actions listed first. Problems are real operational pain, not feature requests. Each solution nod is category-level, zero product pitch. A VP could forward this to their CEO without editing. Closes by inviting correction.

---

### Non-Compliant Forwardable Recap Email
"Hi everyone,

Great meeting today! We're really excited about the opportunity to work together. League's platform is a perfect fit for your needs and we think we can deliver incredible value.

**Next Steps:**
- We'll send over a proposal
- Let us know when you're free to chat again

**Key Takeaways:**
- You need better member engagement
- You want to reduce costs
- You're interested in our AI capabilities

Looking forward to the next conversation!

Dallas"

**Issues:** BLUF is seller-centric ("we're excited"), not buyer's future state. Next steps are vague with no owners or dates, and seller's actions are listed first. "Key Takeaways" are generic wants, not specific problems with solution paths. Mentions League by name. "Perfect fit" and "incredible value" are pitch language. Fails the forward-to-your-boss test.

---

### Compliant Post-Discovery Follow-Up (To CFO)
**Stakeholder**: John Chen, CFO
**Concern**: Payback period and ROI
**Subject**: CFO follow-up on cost impact

"Hi John, Thanks for walking through your financial targets. Your comment about member services cost being 18% of budget really resonates. That's where the leverage is operationally. A 20-25% reduction in member services cost, paired with engagement uplift, typically delivers payback within 12 months at your scale. We've built a preliminary business case for your review. Available this Friday or next week for a 20-min deep-dive on the financial model. Thanks, Dallas."

### Compliant Post-Discovery Follow-Up (To CTO)
**Stakeholder**: Sarah Martinez, CTO
**Concern**: Integration complexity and API reliability
**Subject**: Technical deep-dive on integration

"Hi Sarah, Loved your questions on data integration and API latency. You're right that real-time data sync is non-negotiable. We handle member activation data through EDI and SFTP refresh cycles, plus real-time webhooks for urgent signals. Zero custom development required. I'd like to set up 30 mins with your tech team to walk through the architecture and validate against your HealthEdge instance. Available [2 times]. Thanks, Dallas."

### Compliant Post-Discovery Follow-Up (To Champion)
**Stakeholder**: Lisa Thompson, VP Digital Health
**Role**: Champion
**Subject**: Supporting your internal alignment

"Hi Lisa, Thanks for leading the discovery call. Really impressed by how you framed the engagement and member experience challenges. As you continue conversations with your team, we're here to support in whatever way is most useful. We can provide executive summaries for your CFO, technical deep-dives for your CTO, or clinical evidence summaries for your CMO. Happy to adjust scope and timing based on your internal motion. Let me know what's most helpful. Thanks, Dallas."

### Non-Compliant Post-Discovery Follow-Up
"Thanks everyone for the great meeting. We're excited about the opportunity and think our innovative, cutting-edge platform is a perfect fit for your team. Let's set up a follow-up to discuss our best-in-class solution."
Issue: Group email (not 1:1), uses FORBIDDEN WORDS, no personalization, no specific concern acknowledgment, generic CTA, brand-centric.

### Compliant Post-Discovery Follow-Up (To VP Ops)
**Stakeholder**: Mike Rodriguez, VP Operations
**Concern**: Implementation complexity and member services workflow disruption
**Subject**: Implementation timeline and team support

"Hi Mike, You asked great questions on implementation timeline and member services disruption. Typical rollout is 4-6 weeks from kickoff to first member activation. We work closely with your ops team to stage rollout in phases, so zero disruption to call center operations. We'll doc all member services workflows upfront, then phase implementation by member segment. I'd like to schedule a 20-min call with your ops lead to walk through the rollout plan. When works best next week? Thanks, Dallas."

### Non-Compliant Post-Discovery Follow-Up (To VP Ops)
"Hi Mike, We're excited about the partnership. Our platform will transform your operations and empower your team to be more efficient."
Issue: Generic language, uses FORBIDDEN WORDS, no specific concern from call, no metric-based value prop, no peer-level credibility.
