---
name: league-cold-call-playbook
version: 1.0.0
description: >
  Tier 1 payer executive cold call script generator and live-call playbook.
  Produces persona-calibrated openers, 30-second expansions, objection handles,
  and memorizable 20/45-second script variants for every cold call touchpoint.
  Trigger on any request involving: cold call, cold calling, call script, phone
  script, live call, dial script, what to say when they pick up, how to open a
  call, call opener, call framework, objection handling on the phone, what to
  say if they push back, voicemail script, hail mary call, Day 9 call, Day 10
  call, "what do I say," "how do I open," "give me a script," call prep for
  cold outreach, or any request to generate or sharpen spoken-word outreach
  for payer executives. Also trigger when league-execution-roadmap or
  league-full-pipeline reaches a step that requires a cold call script, voice
  note script, or voicemail script. Load proactively when Dallas is working on
  any Tier 1 account outreach that includes phone-based touchpoints, even if
  not explicitly asked.
---

# Tier 1 Payer Executive Cold Call Playbook

## When this skill applies

Activate whenever a cold call script, phone opener, objection handle, voicemail,
or voice note script is needed for a Tier 1 payer executive. This includes
standalone requests ("give me a call script for Centene's CFO") and embedded
steps inside the execution roadmap or full pipeline (Day 2 call, Day 9 hail
mary, Day 10 execution call). If the task involves words spoken live on the
phone to a payer executive, this skill governs the output.

## Background

Cold calling Tier 1 payer executives is the highest-stakes touchpoint in the
outbound sequence. The call has to do three things fast: prove you belong on
their line, name a risk they already recognize, and make replying easier than
dismissing you. Generic scripts, feature language, and permission-seeking
openers fail immediately at the C-suite level. This skill enforces a specific
philosophy: your first line should sound like a peer noticing operational risk,
not a rep trying to create interest. The goal is not to pitch, not even to
book the meeting immediately. The goal is to get a micro-yes: curiosity,
acknowledgment, or willingness to take a look.

## Core Philosophy (Non-Negotiable)

For payer executives, do not open with League, AI, features, or a long setup.
The strongest structure is:

**Who you are → Why now → One specific friction pattern → One diagnostic question**

This is consistent with the BDR Architect Canon persona rules: CEOs want
consequence and direction, CTOs want risk reduction and architectural safety,
VPs want operational relief. It is also consistent with the Tenbit++ framework:
Observation → Insight → Value → Next Step, compressed into spoken delivery.

The best opener shape for earning the next 30-45 seconds:

"Hi [Name], Dallas at League — quick question. With [forcing function], what's
the bigger risk right now: [friction A] or [friction B]?"

Why this works: it is brief, it proves relevance, it uses one forcing function,
it creates diagnostic tension, and it asks a question that an executive can
answer without committing to a meeting.

## Rules

### Must

1. Every cold call script must open with one forcing function and one two-choice friction prompt within the first 10 seconds.
2. Every script must include a persona-calibrated opener, a 30-second expansion, and a soft-conversion CTA.
3. The CTA must be interest-based ("would you be opposed to a quick compare-of-notes to pressure-test whether...") not meeting-first ("can I get 30 minutes on your calendar?").
4. Every script must include objection handles for at minimum: "I'm in the middle of something," "Send me something," "We already have something in place," and "Not a priority."
5. Every script must be generated in three versions: universal (45-second), persona-calibrated (persona-specific opener + expansion + CTA), and memorizable (20-second).
6. The forcing function must be account-specific and data-backed, never generic.
7. Before any script is finalized, read it aloud mentally and verify: does it sound like a real person talking, or does it sound like a framework being executed? If the latter, rewrite.
8. Apply the Copy Sharpener 9-rule quality gate inline before output: So What Chain, Tenbit++, length limits, brand-light (no League in Days 1-5 scripts), forcing function specificity, CTA escalation match, persona tone match, linguistic guardrails (no forbidden words, no hyphens/em dashes), and send-ready test.
9. Chunk up for senior personas: CEOs hear consequence and direction, not workflow detail. CTOs hear constraint safety and risk reduction, not feature lists. VPs hear operational relief, not brand vision.
10. Name the problem in a way that feels lived-in, not generic. "Service friction showing up as volume" is lived-in. "Challenges with member engagement" is generic.

### Should

1. Default to the pressure-test response trigger ("would you be opposed to a quick pressure-test") as the primary CTA type, since it converts highest with skeptical executives.
2. Use "quick question" as the opening frame since it creates a micro-commitment before the ask.
3. Frame the two-choice friction prompt as operationally specific alternatives, not abstract concepts.
4. Keep the 30-second expansion focused on seams, not systems: "the core usually isn't what breaks first, it's the seams around it."
5. Vary sentence length in every script: some short, some longer, natural rhythm, never monotone.

### Never

1. Never open with League, AI, features, a value proposition, or a company description in the first sentence.
2. Never say: "I know you're busy," "How are you?," "The reason for my call is," "We help health plans with," "Do you have a few minutes so I can tell you about," "We've helped lots of plans," "We're an AI platform," or "Wanted to introduce myself."
3. Never use yes/no CTAs ("Would you be interested in a call?").
4. Never list three pains. One forcing function, one friction frame. That is it.
5. Never explain League before naming the problem.
6. Never use FORBIDDEN WORDS: leverage, synergy, cutting-edge, best-in-class, empower, seamless, robust, transform, transformation, catalyst, paradigm, innovative, comprehensive.
7. Never use hyphens or em dashes in script copy. Periods and commas only.
8. Never use "compare notes," "pick your brain," "touch base," "circle back," "does that make sense," or "would you be interested."
9. Never generate a cold call script without also generating the matching objection handles.
10. Never produce a script that sounds like a script. If it reads like bullet points being recited, rewrite it until it reads like speech.

## Pre-Call Preparation (Required Before Every Script)

Before generating any script, confirm or establish these four inputs. If they
are not available, ask Dallas or pull from the account's Strike Packet and
research files.

1. **One forcing function.** The specific trigger event or operational pressure driving outreach to this account right now. Must be data-backed.
2. **One likely failure pattern.** The most probable friction signal this executive is already seeing or about to see.
3. **Persona lane.** Which lane does this executive live in: consequence and direction (CEO), risk reduction and architectural safety (CTO/CIO), trust and continuity (CXO/Equity/Pop Health), or operational relief (VP/Ops/Director).
4. **Interest-based CTA.** The specific low-commitment ask that matches this persona. Default: pressure-test. Alternatives: architecture sanity-check (CTO), compare-of-notes (CEO), quick walkthrough (VP/Ops).

## Script Architecture

Every cold call script follows this structure. No exceptions.

### The 45-Second Universal Script (Default)

This is the base version. Generate this first, then calibrate per persona.

**Opener (8-10 seconds):**
"Hi [Name], Dallas at League — quick question. With [forcing function], what's
the bigger risk right now: [friction A] or [friction B]?"

**30-Second Expansion (if they engage at all):**
"The reason I ask is that in moments like this, the core systems usually aren't
what break first. It's the seams around them — service spikes, eligibility
confusion, handoffs, disconnected vendor journeys. It stays manageable at first,
then quietly resets the cost baseline."

**Soft Conversion CTA (5-10 seconds):**
"I know I caught you out of the blue, but would you be opposed to a quick
10-15 minute compare-of-notes to pressure-test whether any of that is already
forming?"

**Why this is the best base version:**
One forcing function, one risk frame, operationally credible, soft ask,
pressure-test trigger, no product dump.

### The 20-Second Memorizable Script

This is the version to memorize first. Use when time is extremely short or
the prospect sounds impatient.

"Hi [Name], Dallas at League. Quick question — with [forcing function], what's
the main friction signal you're watching right now: service volume, eligibility
confusion, or fragmented handoffs? We've been helping plans pressure-test
whether those issues are still reversible before they become structural. Open
to a brief 10-minute look next week?"

### When They Answer the Phone

Use these micro-rules every time:

**Ask permission only lightly if needed:** "Did I catch you with 30 seconds?"

**Do not** waste time with "How are you?"

**Do not** explain League first.

**Do not** list three pains.

**Do not** say "I'm calling because we help health plans with digital transformation."

**If they stay on:** Name the problem in a way that feels lived-in, not generic.
For senior personas, chunk up from process pain to business risk. Use one
response trigger only, ideally pressure-test by default.

**Your goal:** Not to pitch. Not even to book the meeting immediately. Your goal
is to get a micro-yes: curiosity, acknowledgment, or willingness to take a
look. That is exactly the interest-based CTA logic from the cold call framework.

## Persona-Calibrated Scripts

Generate all four versions for every Tier 1 account. Each must sound distinctly
different because the executive's world is different.

### 1) CEO / President

Use consequence, not workflow detail. CEOs validate direction and downside.

**Opener:**
"Hi [Name], Dallas at League — quick question. With [forcing function], is the
bigger concern protecting margin through the transition, or making sure
experience noise doesn't obscure whether the new model is actually stabilizing?"

**30-Second Expansion:**
"I ask because in these moments, the issue usually isn't the strategy. It's
that service friction and operational noise make it harder to tell whether the
organization is improving or just absorbing more cost."

**CTA:**
"Would you be opposed to a short 10-minute compare-of-notes to pressure-test
whether that risk is still reversible right now?"

### 2) CTO / CIO

Use constraint safety. Make clear you are not threatening the core.

**Opener:**
"Hi [Name], Dallas at League — quick question. With [forcing function], are you
spending more energy right now on protecting member experience at the edge, or
on avoiding more integration drag against the core stack?"

**30-Second Expansion:**
"The pattern we see is that teams don't want another rebuild. They want a way
to reduce manual queues and stabilize the experience without creating more tech
debt or touching the main transaction engines."

**CTA:**
"Would you be opposed to a quick architecture sanity-check sometime next week
to see whether that's relevant in your environment?"

### 3) Chief Experience / Equity / Population Health

Keep trust and continuity central. Do not collapse into cost-only language.

**Opener:**
"Hi [Name], Dallas at League — quick question. With [forcing function], are you
seeing more risk around trust and continuity right now, or more risk around
members falling through disconnected journeys?"

**30-Second Expansion:**
"What usually happens is the experience doesn't collapse. It just gets less
coherent — more handoffs, more repeated effort, more confusion at moments when
members need clear direction."

**CTA:**
"I know this is out of the blue, but would you be open to a short 10-15 minute
compare-of-notes to see whether that fragmentation risk is already showing up?"

### 4) VP / Ops / Health Services / Transformation

This is where the Pincer Rule matters most: operational relief over brand
vision. Focus on what goes away.

**Opener:**
"Hi [Name], Dallas at League — quick question. With [forcing function], are you
seeing more pressure from extra handoffs, or from member issues that should've
been resolved digitally but are still hitting the team?"

**30-Second Expansion:**
"The reason I'm asking is that these transitions rarely fail all at once. They
usually show up as cleanup work — more follow-up, more calls, more exceptions,
more team lift than expected."

**CTA:**
"Would you be opposed to a quick 10-minute walkthrough to pressure-test whether
that's already becoming structural?"

## Objection Handling (Mandatory in Every Output)

These four handles must accompany every script. Deliver calmly, peer-level,
never defensive.

### "I'm in the middle of something."

"Understood. Let me leave you with the question then: with [forcing function],
is the bigger risk service friction or backend fragmentation? If that's worth
pressure-testing, I'd be glad to keep it to 10 minutes."

### "Send me something."

"Happy to. I'll send a short note. Before I do, which angle is more relevant
so I send the right thing — cost-to-serve, member experience friction, or
technical stabilization?"

**Why this works:** It turns a brush-off into signal. Now you know their lane
before you send the follow-up.

### "We already have something in place."

"That makes sense. Usually the issue isn't whether something exists — it's
whether it's actually absorbing friction at the seams. That's really the only
thing I'd want to pressure-test."

### "Not a priority."

"Totally fair. In accounts like yours, that usually means either the risk is
still theoretical or someone already has it contained. Which is it on your
side?"

**Why this works:** It is a strong pressure-test response when delivered calmly.
It reframes "not a priority" as a diagnostic question rather than accepting it
as a closed door.

## Voice Note Scripts

When the roadmap calls for a voice note (typically Days 3, 7), apply this
standard. Voice notes are spoken, not read. Pacing, breath, and tone matter.

**Structure:** Quick intro (first name and last name only) → one specific
credible reference (their earnings call, app data, a recent hire) → one insight
showing pattern recognition → soft next step.

**Tone:** Like leaving a message for a colleague you respect. Warm, brief, no
pitch language.

**Length:** Under 45 seconds (~100-125 words spoken at natural pace).

**Template:**
"Hi [Name], Dallas Andrews. I pulled [specific data point about their business].
[One sentence interpreting what it means operationally]. The pattern I keep
seeing in plans going through [forcing function] is [one-sentence friction
pattern]. If that's relevant on your end, I think it'd be worth a quick
10-minute pressure-test. Let me know."

**TL;DL (Too Long; Didn't Listen):** Every voice note MUST be accompanied by a
short written TL;DL summary (2-3 sentences max) sent alongside the audio. The
TL;DL captures the core insight and CTA in text form so the prospect can engage
even if they don't play the voice note. Sending both is getting significantly
more replies than voice note alone.

**TL;DL Template:**
"Pulled [specific data point]. [One sentence on what it means]. Worth [X]
minutes to pressure-test whether [friction pattern] is forming on your end?"

**Never use in voice notes:** "I'd love to," "I was hoping to," "I wanted to
reach out," "I think you'd be a great fit." These signal lower status.

## Voicemail Scripts

When the call goes to voicemail. Under 25 seconds (~50-60 words). Most
voicemails get deleted at 15 seconds.

**Structure:** Name, one sentence of context, callback reason. That is it.

**Template:**
"[Name], Dallas Andrews. Saw your [one specific data point]. I've got [specific
thing of value] from [number] plans who [did what they're doing]. If you want
it, my number is [number]."

**Example:**
"[Name], Dallas Andrews. Saw your D-SNP expansion across five states. I've got
retention data from three plans who did the same thing. If you want it, my
number is [number]."

## The Live-Call Formula (Summary)

Use this as the default formula for every cold call:

**Quick question + forcing function + two-choice friction prompt + 20-second
consequence frame + pressure-test CTA**

That gives you the best chance of sounding brief, credible, relevant, and
worth continuing.

## What Not To Say (Blacklist)

Do not say any of these on a cold call. They weaken Tier 1 credibility because
they either sound generic, introduce feature language too early, or break
persona guardrails:

- "We're an AI platform..."
- "We help health plans improve engagement..."
- "Wanted to introduce myself..."
- "The reason for my call is..."
- "Do you have a few minutes so I can tell you about..."
- "We've helped lots of plans..."
- "I know you're busy..."
- "How are you?"
- "We're a company that specializes in..."
- "Our platform does..."
- "I think we could really help you with..."

## Canon Constraints (Inherited)

All scripts generated by this skill must also comply with:

- **Tenbit++ Framework**: Observation → Insight → Value → Next Step (compressed for spoken delivery)
- **Pincer Rule**: VPs and Directors hear Operational Relief, never Brand Vision
- **Brand-Light Execution**: No League mention in Days 1-5 scripts (including sign-offs). Starting Day 6, League may appear sparingly.
- **FORBIDDEN WORDS**: leverage, synergy, cutting-edge, best-in-class, empower, seamless, robust, transform, transformation, catalyst, paradigm, innovative, comprehensive
- **Strict Punctuation**: Periods and commas only. No hyphens or em dashes.
- **So What Chain**: Every sentence earns the next one. If a listener could think "so what?" without the next sentence answering it, rewrite.
- **Recipient Perspective Gate**: Before finalizing, read the script as the executive receiving it. Would you stay on the line? Would you answer the question? If not, revise.

## Output Format

Save as: `[Account]_Cold_Call_Playbook.md`

Every output must include ALL of these sections:

```
# [Account Name] Cold Call Playbook
Created: [Date]
Forcing Function: [Specific trigger]
Account Context: [1-2 sentence summary]

## Pre-Call Inputs
- Forcing Function: [specific, data-backed]
- Failure Pattern: [most likely friction signal]
- Persona Lane: [consequence / risk reduction / trust / operational relief]
- Interest-Based CTA: [pressure-test / sanity-check / compare-of-notes / walkthrough]

## Universal Script (45-Second Version)
[Opener + Expansion + CTA — the version that works for any executive]

## Memorizable Script (20-Second Version)
[The one to memorize first — shortest, tightest]

## Persona-Calibrated Scripts

### CEO / President
- Opener:
- 30-Second Expansion:
- CTA:

### CTO / CIO
- Opener:
- 30-Second Expansion:
- CTA:

### Chief Experience / Equity / Population Health
- Opener:
- 30-Second Expansion:
- CTA:

### VP / Ops / Health Services / Transformation
- Opener:
- 30-Second Expansion:
- CTA:

## Objection Handles
### "I'm in the middle of something."
[Handle]

### "Send me something."
[Handle]

### "We already have something in place."
[Handle]

### "Not a priority."
[Handle]

## Voice Note Script
[If applicable to this touchpoint]

## Voice Note TL;DL
[Written summary to accompany voice note — 2-3 sentences, core insight + CTA]

## Voicemail Script
[If applicable to this touchpoint]

## Quality Gate Verification
- [ ] One forcing function, data-backed
- [ ] Two-choice friction prompt in opener
- [ ] Persona-calibrated language
- [ ] Interest-based CTA (not meeting-first)
- [ ] No forbidden words
- [ ] No League mention (if Days 1-5)
- [ ] No hyphens or em dashes
- [ ] Sounds like speech, not a script
- [ ] Objection handles included
- [ ] All four persona versions generated
- [ ] 20-second and 45-second versions included
- [ ] Recipient Perspective Gate passed
- [ ] Voice note TL;DL included (if voice note generated)
```

## Examples

### Compliant Script (BCBS NC, Day 2 Call to VP Digital Health)

**Pre-Call Inputs:**
- Forcing Function: CuraCor launch and ongoing platform modernization
- Failure Pattern: Integration looks clean but measurement is the hard part
- Persona Lane: Operational relief
- CTA: Pressure-test

**Opener:**
"Hi [Name], Dallas at League — quick question. With the CuraCor rollout, are
you seeing more pressure from members struggling to navigate the new experience,
or from your team spending more time on issues that should have been resolved
digitally?"

**30-Second Expansion:**
"The reason I ask is that launches like this rarely break all at once. They
usually show up as extra cleanup — more follow-up calls, more eligibility
confusion, more manual work than anyone expected. It's manageable early on, but
expensive to unwind once it sets in."

**CTA:**
"Would you be opposed to a quick 10-minute pressure-test to see whether any of
that is already forming on your side?"

**Why this is compliant:**
One forcing function (CuraCor). Two-choice friction prompt. Operationally
specific. Persona lane (VP = operational relief). Pressure-test CTA. No
product dump. No League pitch. Sounds like a peer, not a rep.

### Non-Compliant Script (Shows What to Avoid)

"Hi [Name], this is Dallas from League. We're an AI-powered digital health
platform that helps health plans improve member engagement through innovative
technology. We've worked with lots of plans your size and I'd love to tell you
about how our cutting-edge solution can transform your member experience. Do
you have 30 minutes this week so I can walk you through a demo?"

**Why this fails:**
- Opens with League and company description (Never rule 1)
- Uses FORBIDDEN WORDS: innovative, cutting-edge, transform (Never rule 6)
- "I'd love to" signals lower status
- Feature dump before naming a problem
- 30-minute ask on a cold call (too aggressive, not interest-based)
- Yes/no CTA (Never rule 3)
- No forcing function
- No persona calibration
- Sounds like a script, not a peer

## Integration with Other Skills

This skill is designed to work alongside:

- **league-execution-roadmap**: When the roadmap reaches a day requiring a cold
  call, voice note, or voicemail, this skill governs the script quality.
- **league-copy-sharpener**: The 9-rule quality gate from the sharpener is
  applied inline within this skill. There is no separate sharpening step needed.
- **league-ae-briefing**: The Strike Packet's forcing function, hidden fear,
  and failure pattern feed directly into the pre-call inputs.
- **league-objection-handler**: For objections that arise during the call beyond
  the standard four handles above, escalate to the full objection handler skill.
- **league-full-pipeline**: Phase 6 (Omnichannel Swipe File) should invoke this
  skill for all phone-based touchpoints rather than generating call scripts
  from generic guidelines.

## Exceptions

No exceptions. Every cold call, voice note, and voicemail script for Tier 1
payer executives must follow this playbook. If an edge case arises (e.g.,
warm introduction, inbound callback, referral), adapt the opener but maintain
the structure: forcing function + friction prompt + interest-based CTA.
