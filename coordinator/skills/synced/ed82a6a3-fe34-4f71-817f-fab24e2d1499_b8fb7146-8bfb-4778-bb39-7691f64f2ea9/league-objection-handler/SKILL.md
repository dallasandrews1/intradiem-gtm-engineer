---
name: league-objection-handler
version: 1.0.0
description: Objection Handler. Triggers when prospect replies with pushback. Diagnoses objection category (Bad Timing, Build In-House, Competitor Eval, No Budget, Send Info). Applies Reframe Framework (Acknowledge → Insight Pivot → Soft CTA). Drafts 3-4 sentence response with calm, peer-to-peer, consultative tone.
---

## When this skill applies

- Trigger immediately when prospect sends pushback or objection email
- Trigger when prospect declines initial meeting request
- Trigger when prospect says "not now," "building in-house," "evaluating competitor," "no budget," "just send info"
- Trigger on any mid-funnel objection or deal stall

## Background

The Objection Handler prevents common objection responses that kill deals. Instead of over-explaining or defending, it diagnoses the objection category and applies the Reframe Framework, which acknowledges the concern, pivots with an insight, and creates a soft next step. This maintains momentum without being pushy.

## Workflow Steps

1. **Capture Prospect Objection**
   - Extract the exact objection text from prospect's email or message
   - Note the source (email subject line, specific paragraph, verbal objection from call)
   - Record date and who said it (title, if known)

2. **Diagnose Objection Category**
   - Map objection to one of 5 categories:

     **Category 1: Bad Timing**
     - Prospect says: "Not now," "Too busy this quarter," "Let's revisit in Q3," "Bad timing," "Not a priority right now"
     - Root cause: Initiative is real, but internal bandwidth is constrained or priorities shifted
     - Dallas strategy: Honor the timing, establish re-engagement cadence

     **Category 2: Build In-House**
     - Prospect says: "We're building this ourselves," "We have an internal solution in dev," "We don't need a vendor," "Our tech team wants to own this"
     - Root cause: Tech team has capacity/budget, fears vendor dependency, previous bad vendor experience
     - Dallas strategy: Acknowledge technical capability, reframe as trade-off between speed and FTE cost

     **Category 3: Evaluating Competitor**
     - Prospect says: "We're evaluating [Accolade/Castlight/Wellframe]," "We're in pilot with another vendor," "Competitor is further along," "Already committed to someone else"
     - Root cause: Competitive deal is active, your timing is late, or competitor has stronger relationship
     - Dallas strategy: Don't badmouth competitor, position League as either alternative or complement

     **Category 4: No Budget**
     - Prospect says: "No budget this year," "Budget allocated elsewhere," "Can't fund new initiatives," "CFO said no"
     - Root cause: Budget was never allocated, financial constraints, wrong timing, or CFO not convinced of ROI
     - Dallas strategy: Focus on cost avoidance or operational relief vs. new spend

     **Category 5: Send Info**
     - Prospect says: "Just send me info," "Put me on your list," "No time to talk now, just email details," "Send a deck"
     - Root cause: Low priority, trying to get you off their calendar, or genuinely interested but busy
     - Dallas strategy: Send something, but make next step easy and specific

3. **Apply Reframe Framework**

   **Step 1: Acknowledge**
   - Validate the concern without being defensive
   - Short, 1 sentence: "I get that Q2 is crunch time with your engagement launch."
   - Avoid: "I understand" (generic), "I hear you" (patronizing)

   **Step 2: Insight Pivot**
   - Introduce one new insight that reframes the objection
   - Connect it to operational relief, not to overcoming the objection
   - 1-2 sentences maximum
   - Example: "Most plans in your category deprioritize member engagement until post-launch. By then, the engagement gap compounds. Plans that address it during launch see 2-3x faster ROI."
   - This isn't pushback. It's a peer-level insight.

   **Step 3: Soft CTA**
   - Make it easy to say yes without committing
   - Avoid: "Let's set up a call," "Are you interested?" (yes/no questions are rejectable)
   - Use: "No pressure timeline," "Just want to keep this on your radar," "Worth 10 mins in [3 weeks]?"
   - Example: "No rush on timing. When your launch settles down (late May?), worth 15 mins to walk through how other plans in your space are approaching post-launch engagement?"

4. **Draft Response Email**
   - 3-4 sentences maximum (shorter than the original objection)
   - Apply Tenbit++ (Observation → Insight → Value → Next Step)
   - Calm, peer-level tone
   - No FORBIDDEN WORDS
   - No defensive language
   - No over-explanation
   - Sign with Dallas's name, short title ("Dallas Andrews" not "Dallas Andrews, VP Sales")

5. **Provide Follow-Up Sequence (If Objection Was "Send Info")**
   - If prospect asks to send info, provide 2 options:
     - **Option A**: Send 1-pager (not full deck), follow up in 5 days with "Did this land?"
     - **Option B**: Suggest 20-min call instead ("I can talk way faster than I can email")
   - Do NOT send 20-page deck (low engagement, no conversation)

6. **Anticipate Deeper Objection**
   - Often, surface objection ("no budget") masks real objection ("I don't see the problem you're solving")
   - In response email, reference one additional insight that addresses the likely deeper objection
   - Example: If "no budget" → "I know budget is tight. Most plans find engagement improvement actually reduces operational cost 20-25%, which funds the investment."

## Canon Constraints

- **Tenbit++ Framework**: All external communications follow Observation → Insight → Value → Next Step
- **Pincer Rule**: Communications to VPs and Directors focus strictly on Operational Relief, never Brand Vision
- **Brand-Light Execution**: Do NOT mention League by name in early outreach (Days 1-5). Frame solution as category.
- **FORBIDDEN WORDS**: Never use leverage, synergy, cutting-edge, best-in-class, empower, seamless, robust, transform, transformation, catalyst, paradigm, innovative, or comprehensive
- **Strict Punctuation**: Periods and commas only inside narrative paragraphs. No hyphens or em dashes.
- **Named Outputs**: Every deliverable gets saved as a file. Nothing lives only in chat.
- **MEDDPICC Discipline**: After every call transcript, flag empty or weak MEDDPICC fields.

## Output

Save as: `[Account]_Objection_Response.md`

Format:

```
# [Account Name] Objection Response
Date: [Date objection received]
Source: [Email / Call / Slack]
Prospect: [Name, Title]

## Objection Captured
[Exact quote from prospect]

## Objection Category
- **Category**: [Bad Timing / Build In-House / Evaluating Competitor / No Budget / Send Info]
- **Root Cause**: [Analysis of why they said this]
- **Risk Level**: [High = deal at risk / Medium = stalled but recoverable / Low = expected objection]

## Reframe Analysis

**Acknowledge** (1 sentence):
[Dallas acknowledges the concern]

**Insight Pivot** (1-2 sentences):
[New insight that reframes the situation, focused on operational relief]

**Deeper Objection** (If applicable):
[What might they be thinking beneath surface objection]

## Draft Response Email

[3-4 sentence response, applying Acknowledge → Insight → Soft CTA framework]

---

**Subject**: [Suggested subject line that references their concern, not a generic "Re:"]

[Email body]

Thanks,
Dallas

---

## Follow-Up Strategy

**If prospect replied "Send Info"**:
- [ ] Send 1-page summary (not full deck), not 20-slide presentation
- [ ] Follow up in 5 days: "Did that summary land? Worth a quick call to walk through?"
- [ ] If no response in 5 more days: Move to weekly cadence, low touch

**If prospect replied "No Budget"**:
- [ ] Focus next conversation on cost avoidance, not new spend
- [ ] Example: "Your engagement improvement typically funds the investment through operational cost reduction"
- [ ] Timeline: Re-approach in 60 days when budget cycle reopens

**If prospect replied "Building In-House"**:
- [ ] Acknowledge tech team capability
- [ ] Reframe as trade-off: "Speed vs. FTE cost. When are you live?"
- [ ] Offer to revisit if build takes longer than expected
- [ ] Timeline: Light touch, re-approach in 90 days

**If prospect replied "Bad Timing"**:
- [ ] Honor the timing, acknowledge priorities
- [ ] Schedule explicit re-engagement date: "Let's talk again [specific date in 3-4 weeks]"
- [ ] Add to calendar, send reminder email one week before
- [ ] Timeline: Follow up on promised date, not sooner

**If prospect replied "Evaluating Competitor"**:
- [ ] Ask permission to understand their eval criteria
- [ ] Trigger league-competitive-intel to build counter-narrative
- [ ] Position League as either alternative or complement
- [ ] Timeline: Light touch, let eval play out, re-engage in 30 days

## Deal Health Assessment
[1-2 sentence assessment of deal momentum and next steps]
```

## Examples

### Compliant Objection Response (Bad Timing)
**Prospect Objection**: "Not now. We're in the middle of our engagement launch. Let's revisit in Q3."

**Response**:
"Makes sense. Q2 is crunch. One thought though: most plans deprioritize member engagement until post-launch. By then, the engagement gap compounds and takes longer to fix. Plans that align engagement with launch see faster ROI. No rush on our end. Let's set a specific date in late May when your launch settles down, maybe the 20th or 27th. Interested?"

**Analysis**: Acknowledges timing. Provides insight (engagement during launch = faster ROI). Soft CTA (specific future date, no pressure).

### Compliant Objection Response (No Budget)
**Prospect Objection**: "Budget was allocated elsewhere for 2026. We don't have room for a new vendor."

**Response**:
"Totally understand. Budget is tight. Here's what we're seeing: most plans improve engagement 5-8 points, which drives member retention and reduces member services cost. At your scale, that's typically 20-25% operational cost reduction, which actually funds the investment. No pressure on timing, but worth understanding your 2026 budget cycle and whether Q3 allocation is possible. When do you reforecast?"

**Analysis**: Acknowledges budget constraint. Pivots to cost avoidance (not new spend). Soft CTA (asking about their budget cycle, not pushing a meeting).

### Compliant Objection Response (Build In-House)
**Prospect Objection**: "We have technical capability in-house. Our dev team is building a solution."

**Response**:
"That's smart. Your tech team is strong. One consideration: build timelines for member-facing applications typically run 9-18 months, and FTE cost on dedicated resources is usually $500K-$1M annually. Most plans find it's faster to launch with a vendor and keep dev team focused on core platform. No opinion either way, but worth the trade-off conversation with your CTO. When would be a good time to align on that?"

**Analysis**: Acknowledges capability. Reframes as trade-off (speed vs. FTE cost). Soft CTA (suggesting alignment conversation with CTO, not pushing demo).

### Compliant Objection Response (Evaluating Competitor)
**Prospect Objection**: "We're in pilot with Accolade. They're further along in our eval."

**Response**:
"Great. Accolade brings real coaching strength at scale, which is valuable. One thing to understand in your eval: coaching alone typically moves engagement 2-3 points. For larger uplift and member retention, you need routing and navigation on top of coaching. Some plans use both vendors. Other plans find a single vendor with routing + coaching works better operationally. Either way, worth understanding your success criteria in the eval. What's most important to you: coaching scale, engagement points, or operational simplicity?"

**Analysis**: Acknowledges competitor. Provides technical insight (coaching vs. routing+coaching). Doesn't badmouth competitor. Soft CTA (asking about their eval criteria, not pitching).

### Compliant Objection Response (Send Info)
**Prospect Objection**: "Busy right now. Just send me some info and I'll take a look."

**Response**:
"Happy to. Rather than a long deck, I'm going to send you a 1-page summary and a demo video (5 mins). That'll give you the gist. I'll follow up in 5 days to see if it landed. If it makes sense, maybe 15 mins to walk through how this works at your scale. Sound good?"

**Analysis**: Honors request (send info). But specifies what you're sending (1-page, not 20-slide deck). Soft CTA (5-day follow-up, no high pressure).

### Non-Compliant Objection Response (Bad Timing)
**Prospect Objection**: "Not now. Too busy Q2."

**Bad Response**: "I totally understand you're busy. But this is really important and won't take long. You should really make time for this. Our solution is innovative and best-in-class. Can we do a quick call Thursday at 2pm?"

**Issues**: Dismisses their concern ("this is important"), uses FORBIDDEN WORDS, pushy CTA, not consultative.

### Non-Compliant Objection Response (No Budget)
**Prospect Objection**: "No budget this year."

**Bad Response**: "That's too bad. Most companies eventually see the value and budget for it. You're probably missing out on a lot of opportunities. When you do get budget, let me know."

**Issues**: Condescending, dismissive, no Insight Pivot, weak close.

### Non-Compliant Objection Response (Build In-House)
**Prospect Objection**: "We're building this in-house."

**Bad Response**: "Building in-house never works. Vendors like us are always better. You'll regret trying to build it yourself. Let's talk about why you should work with us instead."

**Issues**: Dismissive of their decision, ad hominem, defensive, no insight, no respect for their technical capability.

### Compliant Deeper Objection Recognition
**Surface Objection**: "Send me some info."
**Likely Deeper Objection**: "I don't see why I need a vendor. I'm skeptical this is real."
**Response Strategy**: The 1-page you send should lead with the forcing function and app audit data (proof of pain). The follow-up call should be: "Did the app audit insight resonate? That's usually the biggest eye-opener."
