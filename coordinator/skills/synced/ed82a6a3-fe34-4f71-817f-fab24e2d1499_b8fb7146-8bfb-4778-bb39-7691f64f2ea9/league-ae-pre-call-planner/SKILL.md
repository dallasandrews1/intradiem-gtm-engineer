---
name: league-ae-pre-call-planner
version: 1.0.0
description: >
  Pre-call discovery planner for AEs. Takes a prospect, call type, and available
  research — then produces a call-ready "Disco Prep Sheet" the AE can open 10 minutes
  before a call and execute from. Includes account snapshot, hypotheses, persona-specific
  L1/L2/L3 pain maps for 8+ C-suite personas, Waterfall & Pivot question framework,
  MEDDIC pre-call status, AI readiness discovery threads, buying/governance committee
  mapping, and a timed 30-minute call flow. Trigger when the user says "prep me for a
  call," "discovery prep," "disco prep," "pre-call planner," "call prep for [account],"
  "get me ready for my call with [name]," or "pull a prep sheet." Also trigger when a
  meeting is mentioned with a prospect name and the user wants to prepare. Load
  proactively when a calendar meeting with a prospect is referenced and preparation
  has not been discussed.
---

# Pre-Call Discovery Planner

**Part of the League Seller 3-Part Motion: Research → Call Prep → Debrief**

## When this skill applies

- Before any scheduled discovery, intro, follow-up, event-concierge, or advisory call with a prospect
- When the user provides an account name, prospect name, and call type
- When the user says "prep me," "disco prep," "pre-call planner," or "get me ready for my call"

## Background

This skill produces a call-ready "Disco Prep Sheet" that synthesizes research, hypotheses, persona-specific pain maps, and question frameworks into a single document an AE can execute from. It combines Waterfall & Pivot mechanics (Sandler), Challenger Teach/Reframe, MEDDIC qualification, and Tenbit++ messaging into a unified pre-call playbook scoped to all League Tier 1 accounts and ad hoc discovery calls.

---

## Framework Stack

- **The Waterfall & Pivot:** Ask → Stop → Count 10 → Negative Discovery if fluffy (core mechanic for every question)
- **Discovery Sequence:** Conversational Opening → L1 Pain → L2 Quantify → Why Now (natural MEDDIC chain)
- **Sandler:** Conversational Opening → L1/L2/L3 Pain Funnel → Decision
- **Challenger:** Teach / Reframe / Rational Drowning
- **MEDDIC:** Surface what we know, name what we need, assign a closing question to each gap
- **Tenbit++:** Observation → Insight/Tension → Value → Next Step (for follow-on messaging)

---

## Required Inputs

The user provides the following at trigger time. If any are missing, ask once — then proceed with assumptions stated explicitly in the output.

```
Account: [account name + industry segment]
Prospect: [name]
Title: [title / role]
Call type: [discovery | intro | follow-up | event-concierge | advisory]
Deal stage: [Stage 1–7 — default Stage 2 Discovery if unknown]
Meeting length: [minutes — default 30]
My goal (1–3 outcomes): [bullets]
Research brief: [paste War Room output OR describe what you know OR "pull from War Room"]
```

If "pull from War Room" is specified, read `Daily_War_Room_Reports/` for the most recent report referencing this account.

---

## The Core Mechanic — Waterfall & Pivot (Apply to Every Question)

This is the discipline that separates real qualification from comfortable conversation. It applies at every stage, every question, every meeting.

```
1. 🌊 THE WATERFALL — Ask the question clearly and concisely. No setup. No softening.
2. 🛑 THE STOP — Do not explain the question. Do not fill the silence. Stop talking.
3. ⏱️ THE COUNT — Count to 10 mentally. Let the silence do the work.
4. 🔥 THE PIVOT — If the answer is vague, fluffy, or non-committal:
   use the Negative Discovery question to test the reality of the deal.
```

> **Rule of thumb:** If you feel comfortable asking the question, it probably isn't Negative Discovery. Ask the question that makes you slightly sweaty — then count to 10.

When the prospect finally answers, do not accept the first response. Drill down: "Help me understand why..." / "What's behind that?" Repeat until you reach the root business driver.

---

## Skill Execution — Step by Step

### Step 1 — Load Reference Files (Required Before Every Run)

Before generating any output, read:
- `AE_Deal_Accelerator_OS/AE_Deal_Accelerator_Canon.md`
- `SKILLS/League_Verified_Metrics_Repository.docx`

These are the source of truth. Do not fabricate proof points, customer claims, or product capabilities beyond what is confirmed in these files.

---

### Step 2 — Extract Signals and Build Hypotheses

From the research brief, extract **5–8 signals** (initiatives, leadership moves, org structure clues, tech stack indicators, pain signals, competitive context, regulatory pressures).

Convert signals into **3–5 hypotheses:**
> *Hypothesis:* "[What you think is true]" → *Why it matters:* "[What it means for the conversation]"

---

### Step 3 — Produce the Disco Prep Sheet

Output the following sections exactly in this order.

---

#### A. ACCOUNT SNAPSHOT
- 5–8 signal bullets from research
- Flag each: **[Pain]**, **[Trigger]**, **[Tech]**, **[Person]**, **[Risk]**

---

#### B. TOP HYPOTHESES
- 3–5 bullets: *"We think [X] because [Y] — which means [Z] if confirmed"*
- Include one hypothesis specifically about where the buying committee or governance committee might have concerns

---

#### C. LEAGUE-TO-ORG CONTEXTUALIZATION

*Auto-generated for each call. Gives the AE a ready-made framing that ties League to this specific account's world — not a pitch, but a way to orient what gets said and how.*

**Their World (2–3 sentences):**
[What this org is focused on right now, the pressures they're under, and what the person in the chair is personally accountable for — drawn from the research signals. Written from their perspective, not League's.]

**The League Fit (1 sentence):**
[Which specific League capability maps to their most likely primary pain, and why — framed as a capability or outcome, not a product name.]

**Best Proof Point for This Context:**
[The ONE proof point from the Canon that resonates most for this persona and account. Include the exact sentence to use — pulled from Canon approved assets only.]

**Framing Hypothesis (use naturally in conversation — not as an opener):**
[2–3 sentences the AE can drop at a natural moment: "The pattern I've been seeing with plans in your position is..." or "What's interesting about where [Account] sits right now is..." — connects their world to the category of problem League addresses without naming League explicitly.]

**What NOT to say in this conversation:**
[1–2 specific things that would land wrong for this persona or account context.]

---

#### D. CONVERSATIONAL OPENING

The opening is not a script — it is a direction. Start with genuine curiosity about their work. Let them describe their own world in their own words.

**The opening sequence:**
1. Brief, specific acknowledgement of who they are and what they're working on — drawn from research.
2. Let them talk without interruption. Listen for: what they're prioritizing, what's frustrating them, what they're behind on.
3. Use what they surface to choose the right L1 entry question.
4. Set light intent at a natural pause: "I want to make sure by the end of this we've both figured out whether there's something worth going deeper on — and if it isn't the right fit, I'd rather be honest about that too."

**Opening question bank (choose one based on title and context):**
- "What's your world focused on solving right now — where's the pressure coming from?"
- "Tell me about your current setup — what's working, and where's the friction?"
- "I saw [specific public signal from research]. How has that landed internally?"
- "You've been [at this org / in this role] for [X time]. What's the one thing you wish was working better than it is right now?"

---

#### D. THREE-PHASE DISCOVERY FRAMEWORK

##### PHASE 1: VALIDATING THE PAIN — "Why Change?"
*Goal: Confirm that the pain is real, personal, and urgent enough to justify action.*

**1. TOP PRIORITIES & TRIGGER**
> 🌊 "What specific internal trigger or event caused you to take this meeting now — versus six months ago?"
> 🔥 Pivot: "You've been operating with your current setup for years. Why is the status quo no longer acceptable?"

> 🌊 "What is the core problem you're looking to solve with your digital member experience?"
> 🔥 Pivot: "You have a digital experience today and the lights are still on. What specifically is the risk to the business if this doesn't change?"

**2. CURRENT STATE & TECHNICAL PAIN (L1)**
> 🌊 "How long has this been a focus? What investments have you already made to address it?"
> 🔥 Pivot: "It sounds like you have smart people working on this internally. Why haven't they been able to solve it yet?"

**3. BUSINESS IMPACT (L2)**
> 🌊 "Have you quantified the impact of suboptimal member CX on the bottom line?"
> 🔥 Pivot: "If this project fails, does it materially impact revenue, Stars, or retention — or is it just an annoyance?"

**L3 Personal Check:**
> 🌊 "As the person responsible for [their function] — how does this sit with you personally?"
> 🔥 Pivot: "What happens to you personally if this doesn't change by end of year?"

---

##### PHASE 2: WHY NOW — Natural MEDDIC Chain

"Why Now" is not its own phase — it is the natural next question after L2 pain has been quantified.

**The sequence:**
1. L1 pain is surfaced (what's broken)
2. L2 is quantified (what does that cost)
3. "Why Now" emerges naturally: *"So given that this is costing you [X] and you've known about it for [Y] — what makes this the year to address it?"*

**If they have a real answer** (Open Enrollment window, Stars measurement, board mandate): the deal is real. Map to timeline.
**If "nothing specific":** The deal is exploratory. Either create urgency through cost-of-inaction framing, or re-qualify priority level.

**Follow-on questions:**
> 🌊 "Has funding been allocated for this, or is it still in the request stage?"
> 🔥 Pivot: "Is the budget a real line item, or 'approved in principle'?"

> 🌊 "Who else needs to weigh in before this moves forward?"
> 🔥 Pivot: "Who is most likely to say no internally — and do you have the authority to move forward anyway?"

---

##### PHASE 3: VALIDATING THE WIN — "Why Us?"
*Goal: Force the prospect to sell League back to you.*

**7. COMPETITION & ALTERNATIVES**
> 🌊 "What other approaches or partners are you considering?"
> 🔥 Pivot: "Be honest with me — why wouldn't you just go with [Competitor]? They are the [incumbent / cheaper / already in your stack] option."

**8. THE PRE-MORTEM**
> 🌊 "What would make this effort stall or lose momentum?"
> 🔥 Pivot: "Fast forward six months. We signed the deal, but the implementation failed. What went wrong?"

**THE BOARD MEETING CHECK (Late Stage Only — Stage 6/7):**
> 🌊 "Is this project on the agenda for the upcoming Board or Strategy meeting?"
> 🔥 Pivot: "If you walk into that meeting without a solution selected, what is the consequence to you personally?"

---

#### D.1 STAKEHOLDER PAIN MAP — Healthcare Payer Personas

Use this table to choose the right L1 entry question and predict the L2/L3 chain before the call.

---

**VP of Member Services / Chief Experience Officer**

| Level | Likely Pain |
|-------|------------|
| L1 | "Our member portal has low adoption." "Reps toggle through seven screens to answer one question." "Our CAHPS scores are flat." |
| L2 | Negative impact on Star Ratings (CMS bonus revenue). High member churn. Excess call center cost from avoidable contacts. |
| L3 | Personal stress from constant member complaint escalations. Fear of falling behind peers. Bonus tied to CAHPS/NPS. |

**Best L1 opener:** "When your reps are on a live call with a member — how many places do they check to find a benefits or eligibility answer?"
**Negative Discovery:** "Your team has been dealing with this for years. Why is this year different?"

---

**CIO / VP of Technology or Digital**

| Level | Likely Pain |
|-------|------------|
| L1 | "Too many disconnected legacy systems." "Our platform is expensive to maintain." "Data security and interoperability are concerns." |
| L2 | High IT OpEx/CapEx with no strategic return. Increased HIPAA breach risk. Inability to support AI roadmap due to inflexible architecture. |
| L3 | Personal anxiety about a cybersecurity incident. Frustration at being seen as a cost center. |

**Best L1 opener:** "What percentage of engineering capacity is going toward keeping existing systems running versus building new capabilities?"
**Negative Discovery:** "You've made significant investments in your current stack. Why isn't your internal team able to close the last-mile gap?"

---

**Chief Financial Officer (CFO)**

| Level | Likely Pain |
|-------|------------|
| L1 | "Administrative costs are too high." "Call center overhead is a growing line item." "I don't see clear ROI on the tech stack." |
| L2 | MLR pressure. Inaccurate forecasting from unpredictable operational costs. Missed revenue from lower Stars ratings. |
| L3 | Pressure from board to improve margins. Personal credibility at stake with every budget cycle. |

**Best L1 opener:** "If you had to quantify the cost of avoidable member contacts — calls that could have been resolved digitally — what's your current estimate per year?"
**Negative Discovery:** "If this project fails to deliver ROI in Year 1, what is the consequence to the budget?"

---

**Chief Operating Officer (COO)**

| Level | Likely Pain |
|-------|------------|
| L1 | "Claims appeals are slow and manual." "Call center morale is low." "Workflows require too many steps." |
| L2 | High cost per interaction. Missed SLAs and regulatory timelines. High employee turnover driving training cost. |
| L3 | Constant stress from operational breakdowns. Reputation as an effective operator personally on the line. |

**Best L1 opener:** "When you look at call center cost per interaction — how much is driven by rep inefficiency versus raw call volume?"
**Negative Discovery:** "Your operations team has been working on this for a while. Why is this the year it gets fixed?"

---

**Chief Digital Officer (CDO)**

| Level | Likely Pain |
|-------|------------|
| L1 | "We have a digital strategy but execution is fragmented." "Engagement programs aren't scaling." |
| L2 | Digital adoption stagnant. New AI/digital initiatives blocked by legacy architecture. |
| L3 | Frustration at being unable to ship the digital roadmap at the pace leadership expects. Personally accountable for digital maturity. |

**Best L1 opener:** "Of the digital investments you've made in the last 18 months — where are you seeing real adoption and where is it stalling?"

---

**Chief Strategy Officer / Growth / Innovation (CSO)**

| Level | Likely Pain |
|-------|------------|
| L1 | "Point solutions aren't enough to bridge care gaps." "We need to differentiate on member experience." |
| L2 | Consumer acquisition and retention cost rising. Inability to demonstrate strategic value of digital investments to the board. |
| L3 | Balancing near-term revenue pressure against long-term transformation goals. |

**Best L1 opener:** "When your leadership team talks about where AI can move the needle on member outcomes — what's the first use case they keep coming back to?"
**Negative Discovery:** "You've been investing in digital for years and still describe it as fragmented. At what point does the board decide this is a leadership execution problem, not a technology problem?"

---

**Chief Marketing Officer (CMO / Marketing)**

| Level | Likely Pain |
|-------|------------|
| L1 | "Content and outreach are segment-level, not personalized." "We're not retaining members post-acquisition." |
| L2 | Member acquisition cost rising. Brand perception flat. Limited ability to demonstrate engagement ROI. |
| L3 | Balancing commercial messaging with mission-driven healthcare brand. |

**Best L1 opener:** "When a new member joins — what does their first 90 days of digital experience look like? How is it personalized?"

---

**Chief Medical Officer (CMO / Medical)**

| Level | Likely Pain |
|-------|------------|
| L1 | "Clinical AI is hard to get physicians to trust." "We're not performing in value-based contracts." |
| L2 | HCAHPS/CAHPS scores not improving. Poor performance in quality and value-based care metrics. |
| L3 | Managing trade-off between physician satisfaction and financial viability. Personally responsible for quality outcomes. |

**Best L1 opener:** "Where is the biggest disconnect between what your data shows and what actually gets acted on at the point of care?"
**Negative Discovery:** "Physician adoption of new digital tools has historically been low. Why would this be different?"

---

**Fractional Advisor / Influencer (non-buyer)**

| Level | Likely Pain |
|-------|------------|
| L1 | "My clients have lots of AI pilots but nothing operational." "They can't staff a big implementation." |
| L2 | Clients' rep efficiency and call handle time cost. No governance framework for AI. |
| L3 | Personal credibility as an advisor is on the line — recommending the wrong vendor damages client relationships. |

**Best L1 opener:** "When you're advising a plan on AI for member services — what's been the hardest question to answer?"
**Champion-building question:** "If you were to recommend League to one of your Blue plan clients — what would you need to have seen?"

---

#### E. AI READINESS DISCOVERY THREAD

Use when the prospect is evaluating AI specifically, or when AI adoption readiness is unknown.

**Market and AI Adoption:**
- "Have you already invested in any AI solutions, or are you currently exploring?"
- "Are you piloting or in production with any AI-driven solutions?"
- "What's been the biggest challenge in moving AI initiatives forward internally?"
- "How are you managing hallucinations and accuracy risks in member-facing AI products?"
- "How are you thinking about a future where members interact with multiple agents? Who owns the orchestration layer?"

**AI Purchasing Decision Criteria:**
- "How is new technology — especially AI — typically evaluated and approved at [Account]?"
- "How do you evaluate AI tools for HIPAA compliance and data privacy?"
- "What proof points or metrics are most important when assessing AI vendors?"
- "How are you thinking about the relationship between AI agents and human support staff?"

**Agent Teams "This Is Cool" → "Let's Build Something" Pivot:**

When a prospect responds positively to the Agent Teams demo or story:
1. "What specifically stood out? Was it the rep-assist piece, the member-facing piece, or the governance layer?"
2. "Where do you see this fitting into a specific use case you're working on internally?"
3. "When you think about evaluating something like this — what does that process look like at [Account]?"
4. "Let me give you a POV on how we'd move forward. Based on what you've told me, I'd suggest we start with [specific use case] and here's why — [Challenger insight]. Does that map to how you're thinking?"
5. "The next logical step is a bespoke demo built around [their confirmed use case]. Can we get that on the calendar?"

---

#### E.1 AI BUYING COMMITTEE — Who's in the Room

| Role | What They're Evaluating | What Closes Them |
|------|------------------------|-----------------|
| CIO / VP Technology | Integration risk, security, vendor viability | Composability, HIPAA/SOC 2/HITRUST, reference architecture, time to deploy |
| CDO / VP Digital | Strategic fit, digital roadmap alignment | Evidence of digital adoption lift, omnichannel deployment, product roadmap |
| CMO / CXO / VP Member Services | Member experience outcomes, CAHPS/NPS | Proof points (Highmark, Manulife), rep-assist framing, first-call resolution |
| COO / VP Operations | OpEx reduction, call volume, headcount efficiency | Cost-per-interaction reduction, handle time data, scale without headcount adds |
| CFO | ROI timeline, TCO vs. build, budget justification | Cost-of-inaction model, 6-month launch timeline, build vs. buy |
| Chief Compliance / Legal | HIPAA, data privacy, AI governance, audit trail | Trust Layer, governed responses, hallucination rate, HITRUST certification |
| VP Member Services (champion) | Daily operational relief, rep productivity | Demo built on their use case, rep-assist framing |

**Questions to map the buying committee:**
- "When an initiative like this gets evaluated internally — who typically owns the process?"
- "Who would need to sign off on the budget, the technical review, and the compliance review?"
- "If I needed to present this to three different stakeholders — who would be the most skeptical, and why?"

---

#### E.2 AI GOVERNANCE COMMITTEE — Who Controls What Gets Deployed

| Role | Primary Concern | Key Question to Unlock |
|------|----------------|------------------------|
| Chief Privacy Officer / DPO | PHI handling, data minimization, member consent | "How does the system handle PHI? Who sees what, and when?" |
| Chief Compliance Officer | Regulatory alignment (CMS, HIPAA), audit readiness | "Is there a compliance review process for deploying AI in member-facing workflows?" |
| CISO | Security architecture, data residency, breach risk | "What does the security review process look like?" |
| Clinical / Medical Officer | Clinical accuracy, liability for AI recommendations | "If the AI surfaces a care recommendation, who is liable?" |
| Legal / General Counsel | Contract terms, indemnification, IP ownership | "Does your legal team have standard AI vendor addenda?" |
| IT Architecture / Enterprise Architect | Integration approach, data flows, API design | "What does your integration review process look like?" |

**Key governance questions to ask the champion:**
- "Does your organization have a formal AI governance process — who runs it?"
- "Have you deployed AI in a member-facing context before? What did that approval process look like?"
- "What's the typical timeline from 'business decision made' to 'compliance and legal cleared'?"

---

#### F. LEAGUE AI STORY (Verbatim)

Always deliver after L1 is surfaced — never before. Match version to audience sophistication.

**10-second:**
"League gives health orgs an AI concierge front door — personalized to each member — able to complete tasks like benefits help, provider navigation, and support across fragmented systems."

**25-second:**
"League is an AI-native experience layer for healthcare. Our concierge uses a secure Health Story — a member context record — to personalize answers and route requests to the right agent or workflow for things like benefits explanations, navigation, and service. One consistent branded experience across products and backends — without a rip-and-replace."

**60-second (when asked "how is it different?"):**
"Most healthcare AI chat is a thin bot bolted onto a single dataset or one workflow, so it breaks when members cross vendors, systems, or lines of business. League is built for real-world complexity. The member interacts with one concierge front door. Behind it, the concierge uses a secure Health Story to understand context and intent, then routes to the best-fit agent — benefits, care navigation, care gaps, coaching, or even your own third-party agents — while keeping a consistent brand voice. And because this is healthcare, we add guardrails: privacy controls, governed responses, and escalation so unresolved situations move to a live team with full context. Net: more trustworthy automation and measurable digital containment — without rebuilding your core systems."

**Mapping question (required):**
"Which matters most first for your team: reducing inbound call volume, improving how reps answer benefits questions on the call, or closing gaps in care navigation?"

---

#### G. MEDDIC PRE-CALL STATUS

State what is CONFIRMED, PARTIAL, or UNKNOWN for each element going into the call. Assign the one question the AE should prioritize to surface each gap.

| Element | Pre-Call Status | Priority Question to Surface |
|---------|-----------------|------------------------------|
| M — Metrics | [Confirmed / Partial / Unknown] | [Question] |
| E — Economic Buyer | [Confirmed / Partial / Unknown] | [Question] |
| D — Decision Criteria | [Confirmed / Partial / Unknown] | [Question] |
| D — Decision Process | [Confirmed / Partial / Unknown] | [Question] |
| I — Identified Pain | [Confirmed / Partial / Unknown] | [Question] |
| C — Champion | [Confirmed / Partial / Unknown] | [Question] |

**Hatch-close rule:** Do not move to a proposal or SE demo unless Pain (I) and Economic Buyer (E) are at minimum Partial.

---

#### H. THREAD-PULLS (4–6 Research-Grounded Hooks)

Each pull = one signal from research + one exact follow-up question.

Format:
> **Thread:** [signal or observation]
> **Pull:** "[Exact question — Waterfall style]"
> **Pivot:** "[Negative Discovery version if answer is fluffy]"

Default thread themes (customize to account):
- Service pressure / contact center volume growth
- Benefits and eligibility friction (reps hunting through multiple portals)
- Provider navigation gaps
- Platform fragmentation / legacy core with AI bolted on
- AI pilot abundance with no operational wins (the Pilot Gap)
- Governance / data ownership / compliance readiness for AI
- Seasonal headcount cycles (ACA vs. Medicare enrollment pressure)
- Microsoft / Azure investment with no last-mile activation (the Microsoft Pivot)

---

#### I. STAGE-BASED QUESTION BANK

Select the right pressure-test questions based on where this deal sits. Every question follows Waterfall → Stop → Count 10 → Pivot.

**Stage 1 — Interested:**
> 🌊 "What specific phrase in my outreach made you decide this meeting was worth your time?"
> 🔥 "Most people just delete these. Why didn't you? Is this a real priority or are you just curious?"

**Stage 2 — Discovery:**
> 🌊 "What specific internal trigger caused you to look for a solution now versus six months ago?"
> 🔥 "You've been operating this way for years. Why is the status quo no longer acceptable?"

**Stage 3 — Qualification & Validation:**
> 🌊 "Which specific capability maps directly to the biggest gap in your current member strategy?"
> 🔥 "If we delivered this exactly as shown, does it actually move the needle on your corporate KPIs — or is it a nice-to-have?"

**Stage 4 — Solution Alignment:**
> 🌊 "Walk me through the decision-making process. Who besides yourself needs to weigh in?"
> 🔥 (if "just me"): "So if you say yes today, we can bypass the CFO and Procurement and go straight to contract?"
> 🔥 (if vague): "What direction do you go if [Stakeholder X] says no? Do you have the authority to overrule them?"

**Stage 5 — Scoping & Planning:**
> 🌊 "We're targeting a [Month] launch. What needs to be true internally for your team to be ready?"
> 🔥 "Is there a compelling event driving that, or is it just a target? If we slip a quarter, what's the impact?"

**Stage 6 — Commercials:**
> 🌊 "What specific ROI metrics does your committee need to approve this spend immediately?"
> 🔥 "If the board pushes back on price, what is your Plan B — competitor, build internally, or do nothing?"

**Stage 7 — Contracting:**
> 🌊 "Walk me through the signature path. Whose desk does this land on, and in what order?"
> 🔥 "Why would your legal team prioritize this contract over everything else they have?"
> 🦈 Shark Close: "If Legal approves by Friday, is there any reason that prevents you from signing on Monday?"

---

#### J. DECISION, COST OF INACTION & NEXT-STEP CONTRACT

**2–3 Sandler decision questions (only after Pain is confirmed):**
1. "If today's conversation makes sense — what does the evaluation process look like at [Account]?"
2. "What would success look like in the first 90 days — and how would you measure it?"
3. "Is there a compelling event this year — Stars measurement, Open Enrollment, a board review — that this needs to land before?"

**Cost-of-inaction framing (when L2 pain has been quantified):**
> "Based on what you've shared — the excess handle time, the rep turnover, the avoidable call volume — the cost of keeping the current setup sounds like it's in the range of [rough figure] per year. Is that a fair characterization?"

**Next-step contract (close verbatim):**
> "Based on what we've covered, here's what I'd suggest as a logical next step: [specific: SE demo / working session / Forrester Wave + reconnect / pilot scoping]. Does that make sense? And if timing shifts or this isn't the priority, I'd rather know that now so we don't waste each other's time."

---

#### K. RISKS & LANDMINES (3 bullets, account-specific)

- **Avoid:** [Account-specific risk — what NOT to say or assume]
- **Likely objection:** [Most probable pushback for this persona]
- **AI trust / compliance default response:** "We built League specifically for healthcare compliance — HIPAA, SOC 2, and HITRUST are foundational, not retrofitted. We also have a Trust Layer that grounds every AI response in verified benefits and clinical data. In production, our hallucination rate is 4% or lower."

---

#### L. NOTES CAPTURE (Fill In During the Call)

```
L1 pain stated (their words, not paraphrased):
L2 impact confirmed (with number if possible):
L3 personal stake (what they said, not what we assumed):
Why Now — compelling event or stated urgency:
AI maturity (pilot / production / evaluating / none):
Buying committee members mentioned:
Governance / compliance process described:
Economic Buyer (named or implied):
Other stakeholders mentioned:
Decision process described:
Compelling event or deadline stated:
Constraints (data, budget, timeline, IT, compliance):
Confirmed next step + date:
Open questions to close in follow-up:
```

---

#### M. DEFAULT 30-MINUTE FLOW

| Time | Segment | What to Listen For |
|------|---------|----------------|
| 0:00–3:00 | Conversational opening — let them describe their world | L1 signals, priorities, frustrations |
| 3:00–10:00 | Pull on L1 pain → quantify to L2 → surface L3 | Pain confirmed, impact quantified, personal stake named |
| 10:00–12:00 | Why Now — natural follow-through from L2 | Compelling event or lack of one |
| 12:00–18:00 | League contextualization + AI story (25s or 60s) + mapping question | Story lands; prospect engages on specific use case |
| 18:00–24:00 | Thread-pulls, AI readiness thread, buying committee mapping | Additional pain threads; governance and buying process surface |
| 24:00–28:00 | Cost-of-inaction framing + decision + next-step contract | Urgency confirmed; specific next step agreed |
| 28:00–30:00 | Close verbally, state follow-up timing | Next step locked; any open items named |

**Multi-presenter call:** Open with 2–3 minutes of conversational opening. Insert 1–2 thread-pulls during natural pauses. Reserve decision + next-step contract for the final 3 minutes. Do not let the call end without a named next step.

---

### Step 4 — Optional Add-Ons (Only Generate If Asked)

- **Full objections + responses:** "We can build this," "Our data isn't ready," "We're already evaluating another vendor," "AI accuracy concerns," "HIPAA risk"
- **Pre-call confirmation email:** Under 80 words, executive tone, confirms agenda
- **Cost-of-inaction worksheet:** Rough financial model from public data
- **Post-call CRM note template:** Pre-populated with known fields

---

### Step 5 — Save Output

```
AE_Wing/Disco_Prep/[AccountName]_[YYYY-MM-DD]_DiscPrep.md
```

---

## Rules

### Must
1. Read the Canon and Verified Metrics Repository before generating any output.
2. Use only approved proof points — never fabricate or extrapolate.
3. Apply the Waterfall & Pivot mechanic to every question generated.
4. Include a MEDDIC pre-call status with priority closing questions for every gap.
5. Generate all sections A through M in order for every prep sheet.
6. State assumptions explicitly when inputs are incomplete.

### Should
1. Customize thread-pulls and pain maps to the specific account and persona.
2. Include the League AI Story version that matches audience sophistication.
3. Map both the buying committee and governance committee when AI is part of the conversation.
4. Save output to `AE_Wing/Disco_Prep/` with the standard naming convention.

### Never
1. Never fabricate proof points, customer claims, or product capabilities not confirmed in the Canon or Verified Metrics Repository.
2. Never cold-pitch the CEO unless a VP-level champion is confirmed.
3. Never use forbidden words: leverage, synergy, cutting-edge, best-in-class, empower, seamless, robust, transform, transformation, catalyst, paradigm, innovative, comprehensive, game-changer, disruptive.
4. Never pitch the roadmap as GA. Benefits Navigation Agent Team and Health Coach Agent Team are GA. Care Navigation and Care Gap Agent Teams are expansion context only.
5. Never skip discovery stages — if Pain is not confirmed, the next step is more discovery, not a demo or proposal.

## Examples

### ✅ Compliant
**Hypothesis:** "We think Avera is under CMS Stars pressure because their 2025 CAHPS scores dropped 0.3 points — which means the VP of Member Services is personally accountable for a recovery plan and will be receptive to a rep-assist framing that reduces avoidable contacts."

This is compliant because it connects a specific, verifiable signal to a persona-level implication and suggests a specific framing approach.

### ❌ Non-compliant
**Hypothesis:** "Avera probably needs League because their member experience isn't great and they could use some help with digital transformation."

This fails because it is vague, uses no specific signals, assumes the conclusion ("needs League"), and uses the forbidden word "transformation."

## Exceptions
No exceptions. All sections are required for every prep sheet. Optional add-ons in Step 4 are generated only when explicitly requested.
