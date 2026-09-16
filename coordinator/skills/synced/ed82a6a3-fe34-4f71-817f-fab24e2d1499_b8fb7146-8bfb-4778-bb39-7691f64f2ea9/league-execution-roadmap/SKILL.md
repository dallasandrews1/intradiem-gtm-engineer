---
name: league-execution-roadmap
description: "Use this skill to map out a day-by-day outreach sequence for a payer account over 10 business days. Trigger for any request involving daily touchpoint scheduling, outreach cadence planning, or sequencing cold emails, LinkedIn, voice notes, and calls across numbered days. Also trigger when someone has completed account research and is ready to start prospecting or execute on outreach. Recognizable phrases: execution roadmap, day-by-day plan, 10-day plan, outreach plan, daily cadence, pincer, High-Propensity Trio, map out days 1 through 10, book a meeting. Produces Week 1 foundation touches, Week 2 pincer escalation, Day 10 hail mary, with send-ready scripts for every touchpoint. Do NOT trigger for strike packets, call prep, transcript processing, competitive intel, or objection handling alone. For all cold call, voice note, and voicemail scripts, this skill automatically invokes league-cold-call-playbook to ensure gold-standard output quality."
---

## When this skill applies

- Run after Phase 2, 3, and 4 are complete (Strike Packet, Multi-Threading Matrix, App Audit done)
- Run when ready to execute outreach on a new account
- Run as the transition from research to active engagement
- Run before sending first cold email or LinkedIn InMail

## Background

The Execution Roadmap turns research into a 10-day tactical calendar. It identifies the "High-Propensity Trio" (the 3 stakeholders most likely to respond positively), then schedules specific outreach to each per day. Week 1 focuses on getting on their radar (emails, LinkedIn, voice notes). Week 2 focuses on the Pincer Move (simultaneous push from multiple angles: technical deep-dive, economic impact, hail mary call). Every task includes the Why, so Dallas knows what's driving each action.

## Workflow Steps

1. **Identify High-Propensity Trio**
   - From the Multi-Threading Matrix, identify the 3 stakeholders MOST LIKELY to respond positively to initial outreach
   - Typically: Champion (VP Digital Health) + CFO + CTO
   - Alternative trio: Champion + VP Ops + CMO (if clinical angle is stronger)
   - Criteria for selection:
     - Has stated pain point that League solves
     - Has decision-making authority or strong influence
     - Likely to be responsive to outreach (active on LinkedIn, public engagement)
     - Not in "bad timing" mode
   - Why these 3: If you can get meetings with these 3 stakeholders in 10 days, you've launched the deal momentum.

2. **Analyze Each Trio Member**
   - For each of the 3, note:
     - Current role and title
     - Primary pain point (from research)
     - Best contact method (email, LinkedIn, phone)
     - Optimal messaging angle (from Multi-Threading Matrix)
     - Likelihood of response (High/Medium/Low based on LinkedIn activity, seniority)

3. **Map Week 1: Foundation (Days 1-5)**
   - Goal: Get on their radar without expecting a response
   - Activities per person:
     - Day 1: LinkedIn connection request (with note referencing specific insight)
     - Day 2: Cold email #1 (forcing function or app audit angle, brand-light)
     - Day 3: LinkedIn InMail (if not yet connected) OR voice note (if connected)
     - Day 4: App audit email (if applicable and person is VP Digital Health)
     - Day 5: Second email #2 (follow-up with additional insight)
   - Volume: Low touch, multiple touchpoints, different channels
   - Tone: Peer-level, consultative, not pushy

4. **Map Week 2: Pincer (Days 6-10)**
   - Goal: Create momentum by hitting from multiple angles simultaneously
   - Activities per stakeholder type:
     - **Champion (VP Digital Health)**:
       - Day 6: Call request with specific time options
       - Day 7: If no response, voice note or LinkedIn voice message
       - Day 8: Final email with "Let's align briefly" CTA
       - Day 9-10: If scheduled, prep for call
     - **CFO/VP Finance**:
       - Day 6: Economic Impact email (1-page business case summary)
       - Day 7: CFO-specific call script (focus on ROI)
       - Day 8: Follow-up emphasizing cost avoidance
       - Day 9-10: If call scheduled, prep business case presentation
     - **CTO/VP IT**:
       - Day 6: Technical deep-dive email (integration, architecture, data security)
       - Day 7: Offer technical webinar or architect call with League CTO
       - Day 8: Follow-up with third-party tech validation (SOC 2, security certifications)
       - Day 9-10: If call scheduled, prep technical specs

5. **Schedule Touchpoints Across Week 2**
   - Don't send all economic emails on same day (looks coordinated)
   - Spread them: CFO email Day 6, CTO email Day 7, Champion call request Day 8
   - This creates the "pincer" effect: they all feel like independent outreach, but they're strategically timed

6. **Define "Hail Mary" Play (Day 10)**
   - If no responses from any of the trio by Day 9, execute the "hail mary"
   - Hail Mary options:
     - Call the Champion directly (10-second hook: "Hi [Name], Dallas Andrews. Something came up in your app reviews I think you'd want to see. Got 2 minutes?")
     - Call the CFO (focus on cost discovery: "Hi [Name], Dallas Andrews. I've been mapping member services cost structures for plans your size. Got 5 minutes for a quick sanity check?")
     - LinkedIn video message to highest-probability person with app audit observation
   - Hail Mary is NOT pushy. It's a last-ditch consultative reach.

7. **Document Task List with Why**
   - For each day's action item, include the Why:
     - Why this person? Because they're [pain point] and have budget authority
     - Why this channel? Because they're [active on LinkedIn / prefer email / not checking email]
     - Why this angle? Because [forcing function / app audit / competitive insight] resonates with their role
     - Why this timing? Because [week 1 builds awareness, week 2 creates urgency]
     - What's the next step if they respond? [Call invitation, business case, technical deep-dive]

8. **Identify Success Metrics**
   - Success = at least 1 of the 3 agrees to a call within 10 days
   - Measure by: LinkedIn connection acceptance rate, email open rate (if trackable), call confirmations
   - If 0 of 3 respond by Day 10: Escalate to weekly cadence, consider adding 4th stakeholder, re-evaluate messaging angle

## Mandatory Copy Quality Standards

**IMPORTANT: Before writing ANY outreach copy in this roadmap, invoke league-first-draft-engine.** That skill governs the thinking process for how copy is drafted: prospect-first cognition, single-idea construction, voice-matched writing, and the Prospect Test. The Copy Sharpener verifies the draft afterward. The First Draft Engine produces it. Do not skip this step. Do not start with the Copy Sharpener's rules and build sentences against a checklist. Start with the First Draft Engine's five-gate sequence, then verify with the Sharpener.

All outreach copy generated by the Execution Roadmap MUST meet these standards. These are non-negotiable and apply to every touchpoint in the 10-day plan.

### Cold Call Scripts

**IMPORTANT: For all cold call scripts, invoke league-cold-call-playbook.** That skill contains the gold-standard persona-calibrated openers, 30-second expansions, objection handles, and memorizable 20/45-second script variants. The guidelines below provide structural parameters; the cold call playbook skill provides the actual script patterns and voice.

- **Maximum 45 seconds spoken** (~100 words). The prospect decides in 8 seconds whether to keep listening.
- **Opening (8-10 sec)**: Name, one credible sentence about what you do. No company pitch. Example: "Hi [Name], Dallas Andrews. I work with digital strategy teams at the big plans on front door architecture."
- **Hook (15-20 sec)**: One specific, data-backed observation about THEIR business. Not a generic pain point. Reference their app ratings, earnings data, member count, or a specific initiative they've announced.
- **Bridge (10-15 sec)**: Connect the observation to a result someone else achieved. "One plan your size solved this by..." Keep it vague enough to create curiosity, specific enough to be credible.
- **CTA (5-10 sec)**: Assumptive, not permission-seeking. "I think it'd be worth 10 minutes to dig into this" or "If that resonates, let's find 15 minutes this week."
- **Tone**: Conversational, peer-level, never rushed. Mixed sentence lengths. Sounds like someone explaining something interesting at a dinner party, not reading a script.
- **NEVER**: Start with "I know you're busy." Never use "Does that make sense?" Never ask yes/no questions as CTAs.

### Voice Note Scripts

**For voice note script generation, also reference league-cold-call-playbook** which contains voice note templates and delivery standards.

- **Under 45 seconds** (~100-125 words when spoken at natural pace).
- **Structure**: Quick intro (name only), one specific credible reference (their earnings call, their app data, a recent hire), one insight that shows pattern recognition, soft next step.
- **Tone**: Like leaving a message for a colleague you respect. Warm, brief, no pitch language.
- **NEVER**: Use "I'd love to" or "I was hoping to." These signal lower status.
- **TL;DL (Too Long; Didn't Listen)**: Every voice note MUST be accompanied by a short written TL;DL summary (2-3 sentences max) sent alongside it. The TL;DL captures the core insight and CTA in text form so the prospect can engage even if they don't play the audio. Sending both the voice note and TL;DL is getting significantly more replies than voice note alone.

### Voicemail Scripts
- **Under 25 seconds** (~50-60 words). Most voicemails get deleted at 15 seconds.
- **Structure**: Name, one sentence of context, callback reason. That's it.
- **Example**: "[Name], Dallas Andrews. Saw your D-SNP expansion across five states. I've got retention data from three plans who did the same thing. If you want it, my number is [number]."

### Email Copy
- **Cold Email 1**: 80-120 words. Observation-led. Soft CTA.
- **Cold Email 2+**: 120-150 words. Can add one proof point or case reference. Moderate CTA.
- **LinkedIn InMail**: 2-3 sentences max (50-80 words). Reference the email topic without repeating it.
- **LinkedIn DM**: 3-5 sentences max (50-100 words). Value deposit or direct ask depending on sequence position.
- **LinkedIn Comments**: Industry insight that adds to the conversation. No mention of League. No CTA. No ask. Pure thought leadership.

### Vidyard Scripts
- **Under 3 minutes**. Structure: Screen share of their actual app reviews or public data, walk through 2-3 specific friction points, reference one peer outcome, soft CTA.
- **Tone**: Like showing a colleague something interesting on your screen. Not a sales demo.

### CTA Escalation Schedule (Mandatory)
- **Days 1-2**: Soft/assumptive. "If any of that resonates, I'd be happy to walk through what I found." or "Let me know if you want to dig in."
- **Days 3-5**: Moderate. "I think it'd be worth 15 minutes to walk through this." or "If you think there's something here, let's find time this week."
- **Days 6-8**: Direct. "Let me send over a couple times that work." or "I've got the data mapped out. Let's set up 15 minutes."
- **Days 9-10**: Confident close. "This is worth your time. I'm here whenever the timing lines up." No desperation. Calm confidence.

### Tone Requirements (All Channels)
- **Sounds human**: Mixed sentence lengths. Some short. Some longer and more conversational. Varies rhythm.
- **Peer-level**: Talks like an expert explaining something to another expert. Not pitching. Not asking permission.
- **Account-specific**: Every script references something specific to THAT account. No generic scripts reused across accounts.
- **Natural openers**: Never start two scripts in the same playbook the same way. Vary: observation-first, question-first, reference-first, data-first.
- **No canned phrases**: Never use "compare notes," "pick your brain," "want 15 minutes to see the path," "touch base," "circle back," or "I know you're busy."

## Canon Constraints

- **Tenbit++ Framework**: All external communications follow Observation → Insight → Value → Next Step
- **Pincer Rule**: Communications to VPs and Directors focus strictly on Operational Relief, never Brand Vision
- **Brand-Light Execution**: Do NOT mention League by name anywhere in Days 1-5 outreach — not in subject lines, email bodies, LinkedIn notes, voice scripts, or email signatures. Sign as "Dallas Andrews" only. Frame solution as category. League can appear starting Day 6, but sparingly.
- **FORBIDDEN WORDS**: Never use leverage, synergy, cutting-edge, best-in-class, empower, seamless, robust, transform, transformation, catalyst, paradigm, innovative, or comprehensive
- **Strict Punctuation**: Periods and commas only inside narrative paragraphs. No hyphens or em dashes.
- **Named Outputs**: Every deliverable gets saved as a file. Nothing lives only in chat.
- **MEDDPICC Discipline**: After every call transcript, flag empty or weak MEDDPICC fields.
- **Cold Call Playbook Integration**: All cold call, voice note, and voicemail scripts MUST be generated using the league-cold-call-playbook skill. Do not generate phone-based scripts from the structural guidelines above alone — use the playbook's gold-standard patterns.
- **Copy Quality Gate**: Before saving the final roadmap file, re-read every piece of outreach copy in the document and verify it against the Mandatory Copy Quality Standards. Specifically check: (1) no forbidden words anywhere in copy, (2) word counts within spec for each format, (3) CTAs match the escalation schedule for that day, (4) no League mentions in Days 1-5 including signatures, (5) no two scripts open the same way, (6) every voice note has an accompanying TL;DL (too long; didn't listen) text summary. If anything fails, rewrite it inline before saving.

## Output

Save as: `[Account]_10_Day_Roadmap.md`

Format:

```
# [Account Name] 10-Day Execution Roadmap
Created: [Date]
Kickoff Date: [Start date of Day 1]
Target: Book Discovery Call by Day 10

## High-Propensity Trio

### Person 1: [Name] | [Title]
- **Account**: [Account Name]
- **Pain Point**: [What they care about]
- **Likely Response**: [High/Medium/Low]
- **Best Channel**: [Email / LinkedIn / Phone]
- **Primary Angle**: [Forcing function / App audit / Competitive]
- **Success Criteria**: Call booked by Day 8

### Person 2: [Name] | [Title]
[Same format]

### Person 3: [Name] | [Title]
[Same format]

---

## Week 1: Foundation (Days 1-5)

### Day 1: LinkedIn Research & Connection Requests
- **Task**: Send LinkedIn connection request to all 3 trio members
- **Specific Actions**:
  - Person 1: Connection request + note: "[Specific insight about their pain]"
  - Person 2: Connection request + note: "[Specific business metric you found]"
  - Person 3: Connection request + note: "[Specific technical challenge you found]"
- **Why**: Get on their radar in their primary professional network. Notes show you've done homework.
- **Success Measure**: 2 of 3 accept connection by Day 3

### Day 2: Cold Email #1 (Forcing Function Lead)
- **Task**: Send cold email #1 to all 3 (personalized version for each)
- **Specific Actions**:
  - Email subject varies per persona
  - Email body: Forcing function lead (80-120 words, brand-light, Tenbit++)
  - Include soft CTA: "Curious your thoughts. Worth 15 mins?"
- **Why**: Email establishes credibility and forcing function connection before you call
- **Success Measure**: 1+ opens (if trackable), no bounces
- **Email Angle**:
  - Person 1 (Champion): "App ratings" angle
  - Person 2 (CFO): "Cost reduction" angle
  - Person 3 (CTO): "Integration simplicity" angle

### Day 3: LinkedIn InMail or Voice Note
- **Task**: Engage on LinkedIn or send voice note
- **Specific Actions**:
  - If person accepted connection: Send LinkedIn InMail (2-3 sentences, different angle from email)
  - If person didn't accept: Comment on one of their recent posts with relevant insight
  - Alternative: Send voice note via email (under 45 seconds) + TL;DL text summary (2-3 sentences capturing core insight and CTA)
- **Why**: Different channel keeps you visible without being repetitive
- **Success Measure**: InMail engagement, comment likes/replies, or voice note reply
- **Persona Variations**:
  - Person 1: InMail about app audit finding
  - Person 2: InMail about ROI comparison
  - Person 3: InMail about technical architecture fit

### Day 4: Persona-Specific Follow-Up Email
- **Task**: Send second email with deeper insight
- **Specific Actions**:
  - If Person 1 (VP Digital Health): App audit insights email with specific complaint data
  - If Person 2 (CFO): Cost avoidance business case email (1-page summary)
  - If Person 3 (CTO): Technical deep-dive email (integration approach, API details)
- **Why**: Shows you understand their specific domain and pain
- **Success Measure**: Email open, reply
- **Content Quality**: Specific to their role, data-backed, peer-level tone

### Day 5: Final Foundation Email
- **Task**: Send warm follow-up email
- **Specific Actions**:
  - "Following up on my emails from earlier this week. I think you'd find this relevant."
  - Keep it short (2 sentences)
  - Include soft CTA: "Worth 15 mins to chat? I'm flexible on timing."
- **Why**: Wraps up Week 1 awareness building, tests receptiveness before Week 2 pincer
- **Success Measure**: Engagement, reply, or silence (silence = go to Week 2 pincer)

---

## Week 2: Pincer (Days 6-10)

### Day 6: Simultaneous Multi-Angle Push Begins

#### Person 1 (Champion - VP Digital Health): Call Request Day
- **Task**: Send call request email with 2-3 specific time options
- **Specific Actions**:
  - Subject: "[Account] - Member Engagement Insights"
  - Body: Reference app audit insight. CTA: "30 mins to walk through? Available [3 times]."
  - Send time: 10am
- **Why**: Champion is most likely to respond. Call request after 5 days of awareness = good timing
- **Follow-Up if No Response by EOD**: Add to calendar for Day 7 call attempt

#### Person 2 (CFO - VP Finance): Economic Impact Email
- **Task**: Send economic impact summary email
- **Specific Actions**:
  - 1-page business case summary (not full deck)
  - Focus on ROI, payback, cost avoidance
  - CTA: "Let me know if you'd like to dig deeper. Happy to walk through."
  - Send time: 2pm
- **Why**: CFO processes business cases slower. Start early with econ impact so they have time to review
- **Follow-Up if No Response by Day 8**: Send ROI comparison email

#### Person 3 (CTO - VP IT): Technical Deep-Dive Email
- **Task**: Send technical architecture email
- **Specific Actions**:
  - Focus on integration simplicity, API details, data security
  - Include third-party validation (SOC 2, HIPAA, security certs)
  - CTA: "Happy to set up a technical call with our engineering team if helpful. Available [times]."
  - Send time: 3pm
- **Why**: CTOs move slow on decisions. Start technical conversation early so they have time to vet
- **Follow-Up if No Response by Day 8**: Offer recorded demo or architecture webinar

### Day 7: Escalation Touchpoints (If No Response from Day 6)

#### Person 1 (Champion): Voice Note or Phone Call
- **Task**: Leave voice note or attempt warm call
- **Specific Actions**:
  - If voice note: "Hi [Name], this is Dallas Andrews. I found something in your app feedback I think you should see. 2-minute voice note attached. Check it out and let me know if it resonates. Thanks."
  - TL;DL to accompany voice note: "Pulled your app ratings. [Specific finding] is the top complaint in 1-star reviews. I mapped how other plans fixed this. Worth 15 mins to walk through?"
  - If call: 10-second hook + soft ask for 15 mins
- **Why**: Voice humanizes outreach, feels less automated. TL;DL gives them a text option to engage even if they skip the audio.
- **Success Measure**: Voice note reply, TL;DL reply, or call acceptance

#### Person 2 (CFO): ROI Comparison Email
- **Task**: Send quick ROI comparison email
- **Specific Actions**:
  - Compare their cost structure to other plans in their category
  - Example: "Your member services cost is $2.1M. Plans in your category using engagement and automation see 20-25% reduction."
  - CTA: "Quick call to validate if this applies to you?"
- **Why**: CFO speaks in comparisons and benchmarks
- **Success Measure**: Email engagement, question, call agreement

#### Person 3 (CTO): Technical Webinar or Call Offer
- **Task**: Offer technical webinar or direct call with League CTO
- **Specific Actions**:
  - "I'd like to get our technical team and yours aligned on integration. We have a 30-min architecture webinar on [date] or I can do a direct call [times]. Which works?"
  - Focus on solving their technical concern
- **Why**: CTO often needs peer-level technical conversation
- **Success Measure**: Webinar registration or call acceptance

### Day 8: Final Momentum Push (If Still No Response)

#### Person 1 (Champion): "Let's Align Briefly" Email
- **Task**: Send final Champion-focused email
- **Specific Actions**:
  - Subject: "Quick Alignment [Account]"
  - Body: "Hey [Name], I've sent a few notes your way on member engagement. I'm going to assume you're swamped. How about we just do a quick 15-minute call to see if there's a fit? I'm flexible on timing. [2 times]."
  - Tone: Low pressure, respectful of their time
- **Why**: Lowers the ask from "learning call" to "quick alignment." More likely to get a yes.
- **Success Measure**: Call confirmation

#### Person 2 (CFO): Cost Avoidance Business Case Email
- **Task**: Send formal business case email
- **Specific Actions**:
  - 1-page formal business case attached
  - Body: "John, I put together a preliminary business case on cost avoidance through member engagement. If you see a potential fit, let's 30 mins to validate the assumptions. Available [times]."
- **Why**: CFOs respond to formal business cases more than soft emails
- **Success Measure**: Call agreement or detailed questions

#### Person 3 (CTO): "Validation Question" Email
- **Task**: Send specific technical validation question email
- **Specific Actions**:
  - "Quick technical question for your team: If we integrated with [their tech stack] via [your standard method], would your team validate that approach? Asking because we're scoping with another health plan in your category and want to make sure our architecture is sound. Appreciate any feedback."
- **Why**: CTOs respond to technical questions better than pitches
- **Success Measure**: Technical engagement, call offer, or detailed response

### Day 9: Confirm Day 10 Calls (If Booked) OR Hail Mary (If Not)

#### If Call(s) Booked:
- **Task**: Prep for calls
- **Specific Actions**:
  - Confirm meeting time and format (Zoom/phone)
  - Prepare talking points for each call
  - Draft one-pager or agenda to share 24 hours before
  - Identify key questions to ask (discovery mode)
- **Why**: Show professionalism and respect their time

#### If No Call Booked by Day 9:
- **Task**: Execute Hail Mary play
- **Specific Actions**:
  - Call the Champion directly: "Hi [Name], Dallas Andrews. Something came up in your app member feedback I think you'd want to see. Got 2 minutes right now?"
  - If can't reach Champion: Call CFO or CTO with specific question (technical for CTO, cost question for CFO)
  - Keep call under 2 mins. Goal: "Can we set up 15 mins next week?"
- **Why**: Hail Mary is low-risk, high-reward. Sometimes people just need to hear a voice.
- **Success Measure**: Call connection, brief engagement, agreement to set meeting

### Day 10: Execution (Calls) OR Cadence Shift

#### If Call(s) Scheduled:
- **Task**: Execute discovery calls
- **Specific Actions**:
  - Run discovery call (20-30 mins)
  - Take notes on MEDDPICC fields
  - Identify next steps (demo, business case, technical deep-dive)
  - Send follow-up email within 24 hours
- **Why**: Discovery call is your goal. Measure success by what you learned, not just by meeting happening.

#### If Still No Call by Day 10:
- **Task**: Shift to weekly cadence
- **Specific Actions**:
  - Move to weekly email (1 per week, different angle each time)
  - Maintain LinkedIn presence (like/comment on their posts)
  - Monitor their company for forcing function signals (layoffs, earnings, strategy change)
  - If forcing function surfaces, escalate back to daily/weekly outreach
  - Re-evaluate in 30 days: Are you missing something about this account? Wrong personas? Wrong angle?
- **Why**: Weekly keeps you on radar without being pushy. Signals + forcing functions = re-engagement opportunity

---

## Success Metrics

- **Week 1 Goal**: Get on their radar (LinkedIn connections, email opens, no bounces)
- **Week 2 Goal**: Book at least 1 discovery call with the trio by Day 10
- **Ultimate Goal**: Discovery call by Day 12, decision process map by Day 20, business case by Day 30

## Risk Flags & Contingencies

- **Risk**: All 3 ignore outreach (Low likelihood, but possible)
  - **Contingency**: Shift to weekly cadence + monitor for forcing function signals (earnings miss, new CTO hire, rating decline)
  - **Re-engage**: If forcing function surfaces, re-trigger daily outreach

- **Risk**: Only 1 person responds, other 2 ghost
  - **Contingency**: Ask respondent to make introductions to the other 2
  - **Next Step**: Have respondent champion internal alignment

- **Risk**: Person 1 responds but Person 2 and 3 don't
  - **Contingency**: Ask Person 1 for CFO and CTO introductions
  - **Next Step**: Person 1 becomes your champion internally

---

## Daily Action Checklist

**Day 1**: [ ] LinkedIn connection requests sent (3)
**Day 2**: [ ] Cold email #1 sent (3 personalized)
**Day 3**: [ ] InMail or voice notes sent (3) — voice notes include TL;DL text summary
**Day 4**: [ ] Persona-specific deep-dive email sent (3)
**Day 5**: [ ] Final foundation email sent (3)
**Day 6**: [ ] Call request to Champion sent, econ email to CFO sent, tech email to CTO sent (3 different channels)
**Day 7**: [ ] Voice notes (with TL;DL) or escalation touchpoints executed (3)
**Day 8**: [ ] Final momentum emails sent (3)
**Day 9**: [ ] Prep for calls OR hail mary executed
**Day 10**: [ ] Call(s) executed OR shift to weekly cadence

---

## Post-10-Day Success Metrics

- **Calls booked**: [X of 3 trio members]
- **Meetings held**: [X of Y scheduled]
- **MEDDPICC fields populated**: [Which fields are strong vs. gaps?]
- **Next milestone identified**: [Demo / Business case / Technical deep-dive / Executive alignment]
- **Re-engagement cadence**: [Weekly / every 2 weeks / monthly]
```

## Examples

### Compliant 10-Day Plan (Centene Example)
**High-Propensity Trio**:
1. Sarah Martinez (SVP Digital Health) - Champion - High response likelihood
2. John Chen (CFO) - Economic Buyer - Medium response likelihood
3. Lisa Patel (CTO) - Technical Gate - Medium response likelihood

**Day 1**: LinkedIn connections to all 3 with personalized notes
**Day 2**: Cold emails: Sarah (app audit angle), John (cost reduction angle), Lisa (integration simplicity angle)
**Day 3**: LinkedIn InMails or voice notes
**Day 4**: App audit email to Sarah, business case to John, tech architecture to Lisa
**Day 5**: Final foundation emails with soft CTAs
**Day 6**: Call request to Sarah (pincer begins), econ impact email to John, technical deep-dive email to Lisa
**Day 7**: If Sarah hasn't responded, voice note + TL;DL. If John hasn't responded, ROI comparison email. If Lisa hasn't responded, webinar offer.
**Day 8**: Final momentum emails to all 3
**Day 9**: Confirm calls or execute hail mary
**Day 10**: Execution (calls) or cadence shift

### Non-Compliant 10-Day Plan
"Send emails to lots of people and hope someone responds. Our solution is innovative and cutting-edge, so people will want to talk to us."
Issue: No specific trio, no strategic pacing, no persona-specific messaging, uses FORBIDDEN WORDS, no Why rationale, no escalation plan.

### Compliant Day 6 Pincer Messaging
**To Champion (Sarah, VP Digital Health)**:
Subject: "Sarah - Member Engagement Opportunity"
Body: "Hi Sarah, I've been analyzing member feedback on your app. Three issues stand out: benefit navigation (34% of complaints), login issues (28%), claims visibility (18%). These are solvable and typically move engagement 5-8 points. I think it'd be worth 30 minutes to walk through what I found. Available Wednesday 2-4pm or Thursday 10am-12pm. — Dallas"

**To CFO (John)**:
Subject: "Cost Impact Analysis - Member Engagement"
Body: "John, I looked at your member services cost structure relative to other plans in your category. Centene is at the higher end on per-member cost, partially due to engagement gap. Plans addressing engagement operationally typically reduce member services cost 20-25%. I put together a preliminary impact if you want to validate. Happy to walk through. Thanks, Dallas."

**To CTO (Lisa)**:
Subject: "Technical Question - QNXT Integration"
Body: "Lisa, I'm scoping with another plan on QNXT integration and want to validate our approach with you. We integrate through EDI and standard API patterns. Your IT team has probably seen different approaches. Would it be helpful to do a 30-min technical call with our engineering team to validate? Available next week. Thanks, Dallas."

---

All three emails sent on **Day 6**, different times, different channels = pincer effect without feeling coordinated.

IMPORTANT: Write this EXACT content to the file. Do not summarize or truncate. Write the complete file.
