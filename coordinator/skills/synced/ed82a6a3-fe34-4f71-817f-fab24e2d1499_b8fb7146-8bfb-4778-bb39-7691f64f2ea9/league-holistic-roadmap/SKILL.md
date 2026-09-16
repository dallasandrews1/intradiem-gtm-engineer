---
name: league-holistic-roadmap
description: "NHPRI-standard holistic 10-Day Execution Roadmap with full 5-tier buying committee coverage. Supersedes league-execution-roadmap by expanding from High-Propensity Trio to ALL identified committee members (minimum 8, target 10-16 contacts across Champion, Economic Buyer, Technical/Legal, Executive Sponsor, and Operational/Pain layers). Produces a single send-ready .md file with buying committee summary table, staggered entry schedule, and complete outreach copy for every contact organized by tier. Trigger on: roadmap, 10-day plan, execution roadmap, outreach plan, daily cadence, holistic roadmap, full committee roadmap, NHPRI-standard roadmap, run the full roadmap for [account]. Also trigger when league-full-pipeline reaches Phase 5. Load this skill instead of league-execution-roadmap for any new roadmap request — it is the current gold standard."
---

## When This Skill Applies

- Any request for a 10-day execution roadmap, outreach plan, or daily cadence
- When league-full-pipeline reaches Phase 5
- When an account has completed research (Strike Packet, Multi-Threading Matrix, App Audit) and is ready for active outreach
- When the user says "run the full roadmap for [account]"
- This skill REPLACES league-execution-roadmap as the default. If both would trigger, use this one.

## Background

This skill exists because the original league-execution-roadmap focused outreach on a "High-Propensity Trio" of 3 stakeholders. In enterprise payer sales, limiting outreach to 3 contacts leaves the operational and pain layer untouched. These are the people who FEEL the forcing function daily, whose validation accelerates C-suite decisions, and whose buy-in prevents deals from stalling in committee. The NHPRI pipeline (April 2026) proved that covering all 5 tiers with staggered entry produces stronger pipeline velocity than concentrating on 3.

The High-Propensity Trio still determines who gets the MOST outreach and the earliest entry. But every identified committee member gets touchpoints in the roadmap.

## Mandatory Skill Chain

These skills fire in this exact order. Do not skip any. Do not reorder.

1. **cognitive-calibration** — Fires first, before any output. Runs its 5-gate sequence silently. Mode is Build for the roadmap structure, then Execution for the copy.
2. **league-full-pipeline** (Phase 2 logic) — For committee mapping and research. Use the 5-tier buying committee structure (not the 4-tier model in the org skill). Pull fresh research via Clay MCP tools and/or web search to identify ALL committee members.
3. **league-first-draft-engine** — Before writing ANY outreach copy. Every email, LinkedIn message, and voice note TL;DL goes through the five-gate thinking sequence individually per prospect. No batch-writing.

After copy is drafted, league-copy-sharpener verifies. For cold call, voice note, and voicemail scripts, league-cold-call-playbook generates the actual scripts.

## The 5-Tier Buying Committee

This is the committee model. Every identified member across all 5 tiers gets full touchpoints in the roadmap.

### Tier 1: Champion Layer
- **Typical Roles**: VP Digital Health, Director of Member Experience, Senior Manager of Engagement
- **Why they matter**: Recommends solution internally, influences peers, owns member-facing initiatives
- **Outreach focus**: Engagement uplift, NPS, digital experience, app audit findings

### Tier 2: Economic Buyer
- **Typical Roles**: CFO, VP Finance, VP Operations
- **Why they matter**: Controls budget allocation, final financial sign-off
- **Outreach focus**: ROI, payback period, cost avoidance, margin expansion

### Tier 3: Technical/Legal
- **Typical Roles**: CTO, VP IT, General Counsel, Chief Security Officer
- **Why they matter**: Validates feasibility, controls integration and InfoSec gates
- **Outreach focus**: Integration simplicity, API architecture, data security, compliance certs

### Tier 4: Executive Sponsor
- **Typical Roles**: Chief Medical Officer, Chief Member Experience Officer, CEO
- **Why they matter**: Final organizational validation, board-level reporting
- **Outreach focus**: Member outcomes, clinical safety, mission alignment

### Tier 5: Operational/Pain Layer
- **Typical Roles**: Directors, VPs, and mid-level leaders whose teams absorb consequences of the forcing function daily (Dir. of Member Services, Clinical Operations Manager, Contact Center Director, Dir. of Quality/HEDIS, Care Management leads)
- **Why they matter**: They live the pain. Their validation is as valuable as C-suite engagement. They often become internal champions because the problem is their daily reality.
- **Outreach focus**: Operational relief, workflow efficiency, staff burden reduction, specific pain points they experience firsthand

## Workflow

### Step 1: Research-First Committee Expansion

Before building the roadmap, expand the buying committee to minimum 8 contacts, target 10-16.

1. Use Clay MCP tools (`find-and-enrich-contacts-at-company`) to pull current contacts at the account across all 5 tiers
2. Supplement with web search for leadership team, LinkedIn research for operational leaders
3. For each contact identified, capture: Name, Title, LinkedIn URL (if found), Tier assignment, Role Archetype, Pain Domain, likely response probability
4. If fewer than 8 contacts are identified, research harder. Check org charts, recent hires, conference speakers, published authors from that organization.
5. Map each contact to a tier. If unsure, ask Dallas.

### Step 2: Build the Buying Committee Summary Table

Create a table with every identified contact. This is the first section of the output file.

| Name | Title | Role Archetype | Pain Domain | Entry Tier | Entry Day | Status/Probability |
|------|-------|---------------|-------------|------------|-----------|-------------------|
| [Name] | [Title] | Champion / EB / Tech / Exec / Ops | [Their specific pain] | Tier [1-5] | Day [1-10] | [High/Med/Low] |

Sort by Entry Day, then by Tier. The High-Propensity Trio (highest probability contacts) enter Day 1. Remaining contacts stagger across Days 1-5 based on tier and probability.

### Step 3: Build the Staggered Entry Schedule (Strategic, Not Arbitrary)

Map all contacts with strategic entry days. Each contact gets their OWN 10-step sequence starting from their entry day. The calendar span of the roadmap extends as far as needed to give every contact their full 10 steps. A roadmap with Day 9 entrants will extend to calendar Day 18.

**Strategic entry logic (determined by buying committee role and account context, not arbitrary tier rules):**

- **Day 1**: High-Propensity Trio + Tier 5 operational/pain contacts who feel the forcing function daily. These are the people most likely to engage AND whose early signals inform later messaging. Also any contact where there is prior warm outreach context.
- **Days 2-3**: Remaining technical contacts (CTO, VP IT, data leads) and additional operational contacts. Entering after Day 1 avoids the "coordinated spray" appearance when the CIO and CTO both get identical-day outreach.
- **Days 3-5**: Tier 4 Executive Sponsors (CEO, CMO). They enter after champion-layer contacts have had time to mention the outreach internally. A CEO who hears "I got an interesting note about our redetermination numbers" from their VP before receiving their own email evaluates it with social proof already in the room.
- **Days 5-6**: Procurement and vendor management gatekeepers. Approaching them before any champion traction risks getting routed into a procurement process that kills deal velocity.
- **Day 7-9**: Contacts where strategic delay creates maximum impact (e.g., a CEO as a hail mary play only after champion engagement has been attempted).

**The coordinated spray problem:** If 12 people all get cold emails from the same person on the same morning, and any two compare notes, every carefully crafted insight becomes "we're getting mass-prospected." Strategic staggering creates the illusion that each person is being contacted individually because something specific triggered the outreach to them. That illusion is what makes the copy work.

**Early signals sharpen later messaging:** If the CIO opens your Day 1 email twice and accepts the LinkedIn connect, that tells you something about angle resonance before you write the CFO's Day 3 entry email.

**Per-contact sequence extends beyond Day 10 as needed:** A contact entering Day 5 gets their full 10-step sequence across calendar Days 5-14. The document header must reflect the actual calendar span (e.g., "Kickoff April 21, Final touches May 12"). The CRM handles variable-length sequences.

**Stagger within each day**: Do not send all emails at the same time. Spread across morning/afternoon. Different channels for different tiers on the same day create the pincer effect without looking coordinated.

### Step 4: Write Full Copy for Every Contact — ALL 10 DAYS

This is the core output. **Every contact gets exactly 10 unique, send-ready touchpoints.** No contact gets fewer than 10 steps. The psychology of sustained invisible pressure requires that every person receives distinct, escalating touches every single day until something changes. Assuming early conversion and giving someone only 3-5 touches is a planning failure.

**For each contact, include:**

1. **Pain Summary** (2-3 sentences): What keeps this person up at night. Specific to their role and the account's forcing function.

2. **Pre-Existing Outreach Context**: If any prior outreach exists in the account folder, reference it. If this is net-new, note that.

3. **Day 1: Cold Email + LinkedIn Connection Request**: 80-120 words. Observation-led, brand-light, question CTA, "Dallas" sign-off. Blank LinkedIn connect (no note). Day 1 emails use the **three-beat CTA close**: (1) a short proof point sentence about a peer or comparable plan (e.g., "One plan in [region/size bracket] cut that cycle by 40% in a single enrollment period."), (2) a standalone "Might be helpful/useful/valuable to walk you through how they did it..." sentence, (3) a blank line, then "Worth 15 min in the next few weeks?" as its own line, another blank line, then "Dallas". The Rick Hopfer HMSA Day 1 email is the gold standard for this three-beat structure. Every cold email #1 should mirror its rhythm: forcing function opener, situation description where the prospect self-selects, diagnostic question, then the three-beat CTA close.

4. **Day 2: LinkedIn InMail/DM**: If connection pending, send InMail (2-3 sentences). If accepted within 24-48hrs, send short text DM (save voice note for Day 4+). If long-standing 1st degree, voice note + TL;DL. No League mentions.

5. **Day 3: Deep-Dive Email**: 120-150 words. Deeper insight specific to their pain domain. One proof point or peer reference. Moderate CTA.

6. **Day 4: Foundation Touch**: Channel varies by persona. Voice note + TL;DL for Champions and relationship personas. Technical email for CTOs. Business case snippet for CFOs. Operational relief angle for Tier 5.

7. **Day 5: Pincer Phone Call #1**: First cold call attempt. Full script with 20-second opener, 45-second expansion, and persona-specific objection handles (generated via league-cold-call-playbook). Log outcome.

8. **Day 6: Follow-Up Email**: References the call attempt without being needy. Introduces a SECOND value angle they haven't seen in Days 1-5. Sign-off switches to "Dallas Andrews" (League can be mentioned from Day 6 forward).

9. **Day 7: Second Phone Call**: Different opener than Day 5. Shorter, more direct. Reference that you've sent a few things their way. Brief objection handles. Voicemail script included (20-30 seconds spoken).

10. **Day 8: Pattern Interrupt**: Break the cadence rhythm. Use a DIFFERENT channel or format from recent touches. LinkedIn Voice Note + TL;DL (if not used earlier), or a completely different email angle. The "here's what I keep coming back to" reflection piece. Something that makes the prospect think "this person is approaching me differently than everyone else."

11. **Day 9: Hail Mary Email**: Final value piece. The one thing you'd want them to know even if they never respond. No desperation, no urgency language. Just the sharpest, most distilled version of the thesis for this specific person. The email equivalent of "if you read one thing from me, read this."

12. **Day 10: Final Phone Call + Voicemail**: Calm, confident, "leaving the door open" tone. Reference the thread of prior touches without listing them. One last clear CTA. Voicemail script (20-25 seconds) that acknowledges the outreach without being apologetic about it.

**Contacts who enter later than Day 1** still get all 10 touchpoints. Their sequence starts on their entry day and extends as far as needed. A contact entering Day 5 gets their cold email on Day 5 and their final call on Day 14. The calendar extends; the arc never truncates or compresses.

**CRITICAL: Escalation Arc Order Is Sacred.** Every contact's 10-step sequence MUST follow this exact order, regardless of entry day:

1. Cold Email + LinkedIn Connect (soft)
2. LinkedIn InMail/DM (soft)
3. Deep-Dive Email (moderate)
4. Foundation Touch / Voice Note (moderate)
5. Pincer Phone Call #1 (direct)
6. Follow-Up Email (direct)
7. Second Phone Call (persistent)
8. Pattern Interrupt (persistent)
9. Hail Mary Email (nuclear)
10. Final Phone Call + Voicemail (nuclear)

The arc progresses: **soft → moderate → direct → persistent → nuclear.** This order is non-negotiable. When building later-entry contacts, map steps 1-10 to sequential calendar days starting from their entry day. Do NOT rearrange steps to fit within a calendar window. Do NOT place nuclear steps (Hail Mary, Final Call) before direct or persistent steps just because the calendar is running out. If a contact enters Day 7, their Hail Mary lands on Day 15 and their Final Call on Day 16. That is correct.

**CRM Header Format:** Every step for every contact must have a `### DAY X:` header where X is the calendar day. This is how the CRM parses the sequence. Steps without proper day headers will not import correctly.

### Step 5: Apply Copy Standards

Every piece of copy must pass these standards. These are hardcoded and non-negotiable.

**Process standards:**
- First Draft Engine 5-gate sequence runs for EACH prospect individually
- Gate 1 (Prospect's Chair) produces a unique lens for each contact
- Gate 2 (One Idea) produces a distinct idea for each contact. If two contacts end up with the same idea, one is wrong.
- Gate 3 (Write It Like You Said It) produces flowing copy, not rule-constructed copy
- Gate 4 (Prospect Test) must pass for every message
- Gate 5 (Rule Check) is the light-touch verification

**Linguistic standards:**
- Question CTAs always (not statement CTAs)
- Sign-off and League mentions are determined by CALENDAR day, not step number: "Dallas" for calendar Days 1-5, "Dallas Andrews" for calendar Day 6+. A contact entering Day 5 gets "Dallas" on their Step 1 but "Dallas Andrews" on their Step 2 (calendar Day 6). "Best, Dallas" for event outreach.
- Blank LinkedIn connects (no note on connection requests)
- Brand-light calendar Days 1-5: zero League mentions in any channel, including signatures. League CAN be mentioned from calendar Day 6 forward regardless of step number.
- No em dashes anywhere. Periods and commas only.
- No forbidden words: leverage, synergy, cutting-edge, best-in-class, empower, seamless, robust, transform, transformation, catalyst, paradigm, innovative, comprehensive
- No tracking refs or UTM parameters
- No product tells: never describe the solution category in a way that reveals what the sender sells
- No rep-language: never use "plans your size," "companies like yours," "leaders in your space," "I help organizations"
- No sender-as-subject: zero sentences where Dallas is the grammatical subject (except sign-off)
- Every voice note has an accompanying TL;DL (2-3 sentences)
- CTA escalation schedule: Days 1-2 soft, Days 3-5 moderate, Days 6-8 direct, Days 9-10 confident close

**FM-09 Template Creep guard:**
After writing all copy, read every message back-to-back. Verify:
- No two emails across the entire committee open the same way
- No two LinkedIn messages use the same structure
- Each contact's copy sounds like it was written specifically for them, not generated from a template with variables swapped
- Openers vary: observation-first, question-first, reference-first, data-first
- If template creep is detected, regenerate the offending messages from scratch through the First Draft Engine

**Copy fluidity principle:**
The framework (Tenbit++, CTA escalation, brand-light rules) provides guardrails, not a construction manual. Each message should read as one flowing thought written by a real person in one sitting. If a message technically satisfies every rule but reads like a checklist was executed, it fails. Fluidity wins over line-level compliance.

**Body prose fluidity:** Consecutive short declarative sentences in the email body (not the CTA close) should be merged with commas, "and", "but", or "because" to create natural speaking rhythm. Two back-to-back sentences under 8 words each almost always read better as one sentence joined by a connector. Read the body aloud. If it sounds like a telegram, merge until it sounds like a person talking across a table.

**Three-beat CTA close exception:** The three-beat CTA close (proof point sentence, "Might be helpful..." sentence, "Worth 15 min..." line) is an intentional exception to the fluidity merge rule. These three elements stay as separate punchy elements. The proof point lands, the value statement bridges, and the time ask closes. Merging them kills the rhythm.

**Time anchor calibration:** Use "in the next few weeks" or "in the next couple weeks" for VPs, SVPs, and C-suite cold outreach. These titles have calendars booked 2-4 weeks out, and a tight time anchor feels presumptuous on a first touch. Use "this week or next" only for directors and mid-level contacts where scheduling windows are shorter and the urgency is appropriate. Event outreach follows its own time anchor rules per the LCDS standard.

**Self-selection pattern:** Describe situations so prospects see themselves in it. Never tell them their reality directly. "That confusion lands on your team" is wrong because it presumes and accuses. "Members don't know which portal to use" is right because it describes a situation the prospect either recognizes or doesn't. The prospect self-selects into the problem. If they don't see themselves in it, the email fails gracefully instead of offending.

### Step 6: Prospect Response Simulation (Mandatory — Do Not Skip)

This gate exists because of a documented, persistent pattern: copy that passes every framework gate (First Draft Engine, Copy Sharpener, Tenbit++, word counts, forbidden words, CTA structure) but would not actually earn a reply from the person it's addressed to. Every time Dallas has asked "would you say yes to this if you were them," the answer has required revisions. This gate eliminates that gap by running the simulation BEFORE delivery, not after.

**For every piece of outreach copy in the roadmap — every email, every InMail, every DM, every voice note TL;DL — do the following:**

1. **Read the message as the specific prospect.** Not as a generic executive. As THIS person: their title, their tenure, their political situation, their inbox volume, their daily reality. A 2.5-year CIO at a Fortune 25 evaluates differently than a newly hired VP in her first 90 days. A COO with 25 years of payer operations experience evaluates differently than a Director of Digital Experience who started 8 months ago. Read as THEM.

2. **Ask one question: would I respond to this?** Not "is this good copy." Not "does this pass the rules." Would I, as this person, on this Tuesday morning, scanning my inbox between meetings, actually stop and reply? If the answer is "maybe if I'm in a good mood" or "it's fine but I'd probably skip it," that is a NO.

3. **If the answer is no, diagnose WHY before rewriting.** Common failure reasons:
   - The message flatters me but gives me no reason to want the conversation (one-way value exchange)
   - A sentence tells me something I already know because of who I am (over-explanation to an expert)
   - A sentence positions the sender as teaching me something, which flips the power dynamic (fortune cookie wisdom, proverbs about leadership, unsolicited advice from a stranger)
   - The CTA is vague — I don't know what the meeting is actually about
   - I can tell this person sells something and the "insight" is just the setup for a pitch
   - The message opens with something painful that happened to my organization
   - The message sounds like every other vendor outreach I received this week (template creep)

4. **Rewrite through Gate 3 of the First Draft Engine with the diagnosis in hand.** Don't patch. Don't swap one sentence. Go back to the one idea (Gate 2) and ask whether the idea itself is strong enough, or whether the idea is right but the execution talked down to the prospect, over-explained, or failed to give them a reason to want the conversation.

5. **Re-run the simulation on the rewrite.** If it still doesn't pass, rewrite again. No piece of copy ships from this roadmap that wouldn't survive a "would you say yes" challenge from Dallas.

**Why this gate exists separately from First Draft Engine Gate 4:** Gate 4 of the First Draft Engine already says "read the message as the prospect." In practice, during batch generation of 10-16 contacts across 10 days each, that gate gets applied with decreasing rigor as the volume increases. By contact 8, the simulation becomes perfunctory — a quick "yeah, this feels right" instead of a genuine read as a skeptical executive. This step forces the simulation to run with FULL rigor after all copy is drafted, when it can be evaluated with fresh eyes across the entire committee. It is the difference between checking your work as you go (which degrades under volume) and reviewing the finished product as the audience (which catches what the in-process checks missed).

**The batch generation trap:** When writing copy for 12 contacts across 10 days, the natural tendency is to get faster and less critical as the volume grows. Contact 1 gets a genuine prospect simulation. Contact 12 gets a rubber stamp. This is the exact moment the simulation matters most, because contacts 8-12 are often the Tier 3-5 contacts whose copy gets the least attention but whose engagement can tip the committee. Run the simulation with equal rigor on the last contact as the first.

### Step 7: Quality Gate

Before saving the final file, run this checklist across the entire document:

1. Every identified committee member has exactly 10 touchpoints (no one left out, no one under-covered)
2. No forbidden words anywhere in the document
3. Word counts within spec for each format (cold email 80-120, follow-up 120-150, InMail 50-80, DM 50-100, voicemail 50-60 words)
4. CTAs match escalation schedule for the day they appear on
5. Zero League mentions in Days 1-5 copy (including signatures)
6. No two messages open the same way across the entire document
7. Every voice note has a TL;DL
8. No em dashes
9. No placeholders anywhere. Every [bracket] is filled with real data. The file is send-ready.
10. Committee summary table is complete and accurate
11. Days 6-10 introduce NEW angles and proof points (not recycled from Days 1-5)
12. Each day's copy for each person is distinct from every other day AND from other people's same-day copy
13. Every contact's 10-step arc follows correct escalation order: soft (Steps 1-2) → moderate (Steps 3-4) → direct (Steps 5-6) → persistent (Steps 7-8) → nuclear (Steps 9-10). No exceptions.
14. Every touchpoint has a `### DAY X:` header with the correct sequential calendar day number. No gaps, no duplicates, no missing headers.
15. Later-entry contacts' sequences extend beyond Day 10 as needed. Verify: a Day 5 entrant's Step 10 should be on Day 14, not crammed into Day 10.
16. Body prose flows naturally with merged sentences and connective tissue (no staccato chains of short declarative sentences in the email body).
17. Day 1 email CTAs follow the three-beat structure: proof point sentence about a peer/comparable plan, then "Might be helpful/useful/valuable to walk you through..." sentence, then "Worth 15 min in the next few weeks?" as a separate line.

If anything fails, fix it inline before saving.

## Output

Save as a single .md file to: `/Accounts/[Account Name]/[Account]_Holistic_10_Day_Roadmap.md`

### Output Structure

```markdown
# [Account Name] Holistic 10-Day Execution Roadmap
Created: [Date]
Kickoff Date: [Start date of Day 1]
Target: Book Discovery Calls by Day 10
Committee Size: [X] contacts across 5 tiers

## Buying Committee Summary

| Name | Title | Role Archetype | Pain Domain | Entry Tier | Entry Day | Status/Probability |
|------|-------|---------------|-------------|------------|-----------|-------------------|
| ... | ... | ... | ... | ... | ... | ... |

## Staggered Entry Schedule

### Day 1
- [Name] (Tier 1, Champion): LinkedIn connect + Cold Email
- [Name] (Tier 2, CFO): LinkedIn connect + Cold Email
- [Name] (Tier 3, CTO): LinkedIn connect + Cold Email
- [Name] (Tier 5, Dir Member Services): Cold Email
- [Name] (Tier 5, Clinical Ops Mgr): Cold Email

### Day 2
[...]

### Day 3-10
[...]

---

## Tier 1: Champion Layer

## FULL NAME -- [Title]
**Pain Summary:** [2-3 sentences]
**Pre-Existing Context:** [Prior outreach or "Net-new contact"]

### DAY 1: Cold Email
Subject: [subject]
[Full email body, 80-120 words]

Dallas

### DAY 2: LinkedIn Connect
[Blank connect — no note]

### DAY 3: Deep-Dive Email
Subject: [subject]
[Full email body, 120-150 words]

Dallas

### DAY 4: Voice Note + TL;DL
**Voice Note Script** (~40 sec):
[Script]

**TL;DL:**
[2-3 sentence summary]

#### Day 5: Pincer Phone Call #1
**Script** (~20 sec opener + 45 sec expansion):
[Full call script with objection handles]

**Voicemail** (~25 sec):
[Script]

#### Day 6: Follow-Up Email
Subject: [subject]
[Second value angle, 100-130 words]

Dallas Andrews

#### Day 7: Second Phone Call
**Script** (shorter, more direct):
[Different opener than Day 5]

**Voicemail** (~20 sec):
[Script]

#### Day 8: Pattern Interrupt
[Different channel/format: LinkedIn Voice Note + TL;DL, or different-angle email]

#### Day 9: Hail Mary Email
Subject: [subject]
[Sharpest distilled thesis, 80-120 words]

Dallas Andrews

#### Day 10: Final Phone Call + Voicemail
**Script** (calm, door-open tone):
[Final CTA, reference thread]

**Voicemail** (~20 sec):
[Script]

---

## Tier 2: Economic Buyer

## FULL NAME -- [Title]
[Same structure as above]

---

## Tier 3: Technical/Legal

## FULL NAME -- [Title]
[Same structure]

---

## Tier 4: Executive Sponsor

### [Name] | [Title]
[Same structure — enters Day 4-5]

---

## Tier 5: Operational/Pain Layer

## FULL NAME -- [Title]
[Same structure]

## FULL NAME -- [Title]
[Same structure]

---

## Success Metrics
- Week 1: LinkedIn connections accepted, email opens, no bounces
- Week 2: At least 2 discovery calls booked across committee
- Day 10: If zero responses, shift to weekly cadence with forcing function monitoring

## Hail Mary Playbook (Day 9-10)
[Cold call scripts for top 3 unresponsive contacts, generated via league-cold-call-playbook]
```

## Canon Constraints

- **Tenbit++ Framework**: Observation, Insight, Value, Next Step. Diagnostic for completeness, not a rigid template.
- **Pincer Rule**: VPs and Directors hear Operational Relief, never Brand Vision.
- **Brand-Light Days 1-5**: No League mentions in any channel.
- **FORBIDDEN WORDS**: leverage, synergy, cutting-edge, best-in-class, empower, seamless, robust, transform, transformation, catalyst, paradigm, innovative, comprehensive.
- **Strict Punctuation**: Periods and commas only. No em dashes.
- **Named Outputs**: Everything saved to /Accounts/[Account Name]/. Nothing lives only in chat.
- **Cold Call Playbook Integration**: All phone scripts generated via league-cold-call-playbook.
- **Full Committee Coverage**: NEVER limit outreach to 3 contacts. Every identified committee member gets touchpoints.
- **Full 10-Step Coverage**: NEVER give a contact fewer than 10 touchpoints. Every person gets all 10 steps from THEIR entry day. Sequences extend beyond calendar Day 10 as needed. Assuming early conversion is a planning failure.
- **Strategic Staggering**: Entry days are determined by buying committee role and account context, not arbitrary tier rules. Staggering prevents the coordinated spray problem and lets early engagement signals sharpen later messaging. Champion momentum before executive entry.
- **Escalation Arc Order**: The 10-step arc (soft → moderate → direct → persistent → nuclear) is sacred and never reordered. Later-entry contacts map steps to sequential calendar days from their entry day, extending the calendar as needed. NEVER cram nuclear steps early to fit a calendar window. NEVER place Hail Mary or Final Call before Follow-Up Email or Second Phone Call.
- **CRM Day Headers**: Every touchpoint must have a `### DAY X:` header with the correct calendar day number. The CRM parses these headers to build sequences. Missing or misnumbered headers break the import.
- **CRM Contact Headers**: Every contact section must start with `## UPPERCASE NAME -- Title` (two hashes, space, ALL CAPS name, space-hyphen-hyphen-space, title). The CRM parses these headers to detect individual contacts in multi-contact blitz files. Using `###` instead of `##`, pipes instead of ` -- `, or mixed-case names will cause the CRM to fail contact detection. Match the HMSA gold standard format exactly: `## RICK HOPFER -- EVP & Chief Information Officer`.
- **Rick Gold Standard**: The Rick Hopfer HMSA Day 1 email is the benchmark for all cold email #1 output. Structure: forcing function opener, then situation description (prospect self-selects into the problem), then diagnostic question, then proof point sentence about a peer/comparable plan, then "Might be helpful to walk you through..." sentence, then "Worth 15 min in the next few weeks?" as its own line, then bare "Dallas" sign-off. Every cold email #1 in every roadmap should mirror this rhythm. If a Day 1 email doesn't read like it came from the same hand that wrote the Rick email, it needs to be rewritten.

## What This Skill Does NOT Do

- It does not conduct Phase 1-4 research from scratch. It assumes Strike Packet, Multi-Threading Matrix, and App Audit exist (or will be created as part of the skill chain). If they don't exist, it will pull research as part of Step 1 but the output quality depends on upstream research.
- It does not generate PDFs. Phase 7 of league-full-pipeline handles that.
- It does not replace league-full-pipeline. It IS Phase 5-6 of that pipeline, elevated to a standalone skill with the gold-standard committee model.
- It does not produce cold call playbooks as separate files. Phone scripts appear inline in the roadmap. For a standalone playbook file, run league-cold-call-playbook separately.
