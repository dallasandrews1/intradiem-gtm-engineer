---
name: intradiem-cold-call-playbook
version: 1.0.0
description: >
  Intradiem live-call playbook and dial script generator. Produces persona-calibrated
  openers, 30-second expansions, motion-specific objection handles, voicemails and voice
  notes for Nathan (US) and Jack (UK) across every Intradiem motion. Trigger on any request
  involving: cold call, cold calling, call script, phone script, dial script, live call,
  call opener, what to say when they pick up, how to open a call, objection handling on the
  phone, what to say if they push back, voicemail script, voice note, call prep, call block,
  "give me a script", "what do I say". Also load before editing the Daily Action Brief call
  contract. Runs after intradiem-first-draft-engine, before intradiem-copy-sharpener.
---

# Intradiem Cold Call Playbook

## When this skill applies

Any spoken prospect-facing output: dial scripts, openers, objection handles, voicemails, voice notes, call blocks in the Daily Action Brief, or call prep for a named account. Also load before changing `motions/shared/Cold_Call_Playbook_Aug2.md`, `automation/config/action_brief_format.md`, or the call contract in `automation/run_daily_action_brief.sh`.

Do not load for written-only copy. That is `intradiem-first-draft-engine` plus `intradiem-copy-sharpener`.

## Source of truth, and the drift rule

**`motions/shared/Cold_Call_Playbook_Aug2.md` is canonical for call STRUCTURE.** The unattended Daily Action Brief composer reads that file directly, listed under every brief's `playbook_sources` in `automation/config/action_brief.json`. This skill is the method layer on top: persona calibration, motion handles, the claim gate and the output shape.

**The drift rule:** where this skill and the canon disagree about the opener skeleton, the branch handles, the branch cap or the opener fact check, the canon wins and this skill gets corrected. Never restate the canon's wording here in a way that can silently diverge. If a change belongs to structure, make it in the canon so the composer inherits it; if it belongs to judgment, make it here.

Motion-specific handles live in each motion's own playbook doc, which is what that motion's `playbook_sources` list points at. Check that list is current before writing handles for a motion; a stale entry ships a retired claim into a live dial.

## Who calls

Dallas engineers the script, a rep dials it. US default Nathan Belfield, UK Jack O'Hagan. Write in that person's voice and register, sign nothing (this is spoken). Confirm the sender before writing. When a rep has shared call language that booked meetings, that is the voice reference and it beats anything in this file.

Register: UK asks "Have you got 30 seconds, and you can tell me if it's not relevant?" US asks "Can I take 30 seconds, and you tell me if it's not for you?"

## Scope reminder

Intradiem sells Dynamic Workforce Orchestration across contact centres AND back offices, six verticals (Healthcare, Financial Services, Insurance, Retail, Telecom, Utilities). Never say call-centre tool. WFM (Verint, NICE, Calabrio) and CCaaS are the layer we sit on top of and act through, never rivals to attack on a call. "On top of the WFM you already run" is the house phrasing and it defuses the most common objection before it arrives.


## Why these rules, so you know which are load-bearing

Internal direction only, research-sourced, never quoted to a prospect. From large call corpora (Gong Labs and 2025 dial-level studies):

- Availability yes/no openers book roughly **40% below** baseline. Asking for about 30 seconds with the prospect in control books near **11% against a ~2% average**. This is why the banned opener family is a hard rule and not a style note.
- Proactively stating the reason for the call roughly **doubles** success. Beat three is the whole call.
- Booked calls run nearly **twice as long** as failed ones and contain real back-and-forth. This is why the expansion must end on a check question. A monologue that lands on a meeting ask is the single most common way our scripts fail.

Everything else in this skill is craft. These four are the spine.


## Pre-call research inventory, required before any script

Beat three of the opener IS the research. A script written from the account narrative instead of the person's specifics produces a deletable call. Before writing, list what you actually have for THIS person:

1. **Their number or their seam.** The one dated, specific fact: a filing, a posting cluster, a measure read, a contract id, a leadership change, a service event. Not "the member experience question", but the thing itself.
2. **Their stored variables.** `vm_hook`, `voice_script`, `measure_read`, `contract_id`, `plan_name`, platform reads. These are the only facts a composed opener may use.
3. **The seat.** What this title owns, and therefore which one idea is theirs. Not the account's idea, theirs.
4. **A true anchor, or none.** A LinkedIn connect this week, a note actually sent. If there is no anchor, there is no anchor; never manufacture familiarity.
5. **The colleague fact.** Who else at the account has the same note, stated as a fact from the account map. Never "I can't tell whose desk this is".
6. **The platform read**, only if `CC Platform last seen` is inside 12 months or a rep confirmed it. Otherwise say nothing about platforms.

If items 1 and 2 are empty, do not write a script. Point at the lemlist task and say the research is missing. A confident script built on nothing is worse than no script.

## The call, in order

Per the canon, so only the judgment notes are here.

**Opener, four beats, 10 to 12 seconds, then stop talking.** Name and a real pause; who you are; the reason for the call carrying this lead's specific hook; then the 30-second contract with the prospect in control. The pause after the name is the pattern interrupt, not a stumble.

**The banned opener family is a hard rule.** Any availability yes/no before the reason lands ("did I catch you at a bad time", "is now a good time", "did I catch you with 30 seconds"). It hands them an exit before they know why you called. The contract in beat four is the opposite: it comes after the reason, asks for a slice, and makes ending the call their explicit right.

**If they engage:** 20 to 30 seconds expanding one idea, then a check question that hands them the floor. Never expansion straight into the meeting ask. Give the insight away in full whether or not you get the meeting; the value is the point and the meeting is the consequence.

**The ask names the payoff.** What they get in the 15 minutes, in their terms. "Fifteen minutes and I'll walk you through which contracts sit closest to the line." A meeting ask with no named payoff is the most common failure in our drafts. Do NOT append an honest-exit clause; see the standards conflict below.

**On a yes, lock the slot on the call.** Two concrete options. Never "I'll send some times over."


## The standards conflict, and which one wins

`Cold_Call_Playbook_Aug2.md` and the Sep 4 pressure standard disagree, and Sep 4 is later and is the one Dallas called "the new standard of quality for messaging". **Sep 4 governs.**

Aug 2 wrote brush-off and opener language that Sep 4 now fails: "Fair enough, I won't push", "appreciate you being straight with me, I'll leave you be", "We haven't spoken before, so I'll be quick", and any honest-exit clause on the ask. Sep 4 bans apology and exit phrases everywhere except the single breakup, and requires every touch to end on an ask.

**The reconciliation, and it keeps what each was protecting.** Aug 2's HARD STOP exists so nobody second-pitches a person who said no; that survives untouched. What changes is the wording around it. On a brush-off: accept it, ask one calibrated either/or question, and let the call end on their answer. No apology, no release line, no "I'll leave you be". Their answer is logged as intel, never worked.

Fails Sep 4, do not speak: "fair enough", "I'll be quick", "I'll stop", "I'll leave you be", "I'll leave you alone", "sorry to bother", "no need to reply", "either answer helps me stop guessing", "if this is the wrong desk", "I'll close the file".

**This means the canon is out of date on wording.** Until `Cold_Call_Playbook_Aug2.md` is corrected, a composed brush-off block may render a failing line. Flag it when you see it rather than reproducing it, and raise the canon fix; the composer reads that file, not this one.


## The three calls have three different jobs

Per the Sep 4 pressure standard: three calls across the sequence, every one leaves a voicemail, EA route when there is no direct number. They are not the same script dialled three times.

**Call 1, early.** The insight call. Full four-beat opener, the one idea, the check question. Voicemail 1 carries `{{vm_hook}}` and points at the email. No number in the voicemail yet.

**Call 2, mid.** The evidence call. Opener drops the LinkedIn reference and leads with the reason. Voicemail 2 is the one that carries the number: one verified figure, the callback line. "One number for context: Humana has handle time down 45 seconds with this, on the record."

**Call 3, late.** The decision call, and the shortest. One question that is easy to answer either way and tells you where this goes: "Is this a this-year question for your team, or a next-year one?" Both answers are useful. If next year, ask permission to come back on a named date. If this year, lock a slot with two concrete options. Voicemail 3 is about 20 seconds and states it is the third note, names the colleague, and closes on the ask.

**No direct number, the EA route.** Main line, ask for their office, leave one line with the assistant by name: "Nathan Belfield at Intradiem. I sent [first name] a note on the customer service score at [plan]. 937-238-3179." Never pitch the assistant, never leave the insight with them.

## Persona-calibrated call angles

One idea per person, same verified numbers across the account. Full library in `intradiem-first-draft-engine`; these are the spoken cuts.

**Front office**

| Persona | Spoken one-liner |
|---|---|
| Resource Planning / WFM | "The plan's right at eight and wrong by ten, and your team absorbs the drift by hand." |
| Contact centre / Ops Director | "Growth turns into contact volume before it turns into anything else." |
| Performance / Op Ex | "The biggest variance you carry never makes the dashboard." |
| Customer / Service Director | "Coaching happens when it's quiet, and it's never quiet." |
| Complaints / Quality | "The rushed call becomes the repeat contact becomes the complaint." |
| Transformation / Automation | "It's the one item on the roadmap with a known number, and nothing new to govern." |
| VP/SVP Stars, Quality, Medicare | See the Star Ratings section below before speaking any measure. |
| New in role, six months or less | "The listening tour ends and the agenda gets written." |
| Group / C-level | Air cover only, after an operational thread is already live. Never a cold dial. |

**Back office**

| Persona | Spoken one-liner |
|---|---|
| Claims Ops, Appeals, Payment Ops | "The backlog you clear by Friday grows back by Monday." |
| Shared Services | "You can't see idle capacity you don't measure." |
| Document processing / intake | "The weeks that age your cases show up in intake days before the queue feels it." |
| Back-office technology | "It sits on top of the case system and the WFM. Nothing to rip out." |
| COO / SVP Operations | "The backlog gets paid for twice, in overtime and again in rework." |
| CFO / VP Finance | "Capacity without headcount, and a payback you can check." No adjectives, no vision. |

Vertical translation keeps the mechanics and swaps the pressure. Mutuals and public-facing brands hear service up, never heads down.

## Star Ratings calls: which measures may be spoken

Full section in the canon and in `intradiem-verified-metrics`. The short form:

**Say** the CAHPS Customer Service score. It is the one Star measure set in the plan's own service centres, two of its three questions are about the call itself, and it survived CMS's June 2026 recalculation. Rating of Health Plan may be named as the score the call sits inside.

**Never say, as bonus money:** complaints about the plan, appeals, members choosing to leave, call centre interpreter and TTY. CMS pulled all of them out of the 2027 quality bonus determination on Jun 17 2026. They are still real operational pain and may be named as such. The "half-star this cycle" framing is retired.

**Never attach to our service operation:** Getting Appointments and Care Quickly, Getting Needed Care, Care Coordination. Those are answered about the doctor's office, and naming them to a quality leader reads as a mismatch.

A plan's own numbers come from the lead's `measure_read` and `contract_id` variables, never from memory and never from a file dated before Sep 21 2026. `qbp_avg` is retired; do not read it aloud.

**EXPIRY: the CMS October 2026 release.** After it lands, nothing above is speakable until `StarRatings_Measure_Reconciliation_Clover_Sep21.md` is re-cut and the leads re-run.

## Objection handles

Universal branches (busy, brush-off, send me an email, what's this about) live in the canon and render on every dial. The full diagnostic set is `intradiem-objection-handler`; these are the spoken shapes for the ones that actually come up on Intradiem dials.

**"We already have WFM."** Agree, then separate the layers. "Good, you'd need to. Verint tells you what the day should look like. We act on the gap when the day doesn't. It runs on top of what you've got, so there's nothing to replace." Never a word against the WFM vendor.

**"We built something in-house."** Respect it, then name the maintenance seam. "Most teams who've got this far built something. The question I'd ask is who owns it when the rules change and the person who wrote it has moved on." One question, no teardown.

**"Not a priority right now."** Accept, one calibrated question, release. Never a second pitch.

**"No budget."** Do not sell past it. "Fair enough. Is it that there's no line for it this year, or no case for it yet?" The second answer is workable, the first is a date to come back on.

**"Send me something."** Agree, one qualifying question so the thing you send is useful, then a conditional ask. Per the canon.

**"Aren't those Star measures going away?"** Agree plainly, name what changed, land on what's left. "Some are. CMS pulled complaints, appeals and the call centre measure out of the bonus math in June. What it kept is the member survey, and Customer Service is the one score in it your service centres set." Never argue the ruling, never predict October.

**"We'll wait for the October ratings."** That is a date, not a no. "Makes sense. The thing worth knowing before then is the survey behind the next one is already being lived, through open enrolment. Worth a look at that window rather than the release?"

## Voicemail

Under 25 seconds. It amplifies the email, it does not replace it. Carries `{{vm_hook}}`, one number for context at most, the callback number, and the rep's name twice (start and end). If it runs long, cut the hook, never the callback line. No pitch, no second idea.

## Voice notes

Under 45 seconds, spoken register, and every one carries a written TL;DL of two to three sentences that passes the same gates and stands alone if the audio is never played.

## The claim gate on a live call

Three lanes, same standard as written copy, higher stakes because nothing is reviewable after it leaves the rep's mouth.

- **Lane 1**, any Intradiem or customer outcome: traces to the Value Repository via `intradiem-verified-metrics`. Humana's handle time down 45 seconds and roughly two hours of capacity per agent per month are the workhorses; the first-year return and 7X are cleared. Nothing else ships spoken.
- **Lane 2**, public facts about their world: primary source, as-of date, re-checked before the call block runs. CMS data goes stale between drafting and dialling.
- **Lane 3**, anything we modelled: 1:1 only, labelled as an estimate out loud, never a headline. Most modelled numbers should simply not be spoken.

Under the canon's OPENER FACT CHECK, every number, name and fact in a composed opener traces to the lead's stored variables or the brief's playbook sources. Anything untraceable gets recomposed without it.

## Blacklist

No em dashes in anything spoken or written here. Contractions always. Never: leverage, synergy, best-in-class, empower, seamless, robust, transform, transformation, cutting-edge, unlock, streamline, game-changer, journey, "I hope this finds you well", "quick question", "circle back", "touch base", "just following up", "I know you're busy", "I'd love to", "excited to". No exclamation marks, no qualifiers ("I think", "hopefully"). Never reference tracking ("I saw you opened"). Never name a competitor as an enemy. Never claim an implementation timeline that is not verified. Never a second pitch after a brush-off release line.

## Branch cap

A dial task renders at most seven labelled blocks and at most two pushback blocks, chosen by relevance to this lead. A rep mid-call reads a map, not a manual. The cap is a relevance rule and never trims the wording of a block that does render. The motion doc always carries the full set.

## Output format

Labelled segments, each in its own block, never one merged paragraph and never an objection folded into the opener:

```
Opener
If they engage
The ask
If they're busy
If they brush you off
If pushback: "<objection>"
No answer: voicemail
```

Voicemail-only tasks drop the busy and brush-off blocks. Every variable resolved from the lead's record, or the script points at the lemlist task instead. Never invent copy, never guess a script.


## What good sounds like (worked example)

Live Stars lead, paused campaign, Sep 2026. Nathan calling Marsha, Director of Quality Improvement at CalOptima, a KEEP_STARS lead whose largest under-4 contract reads Customer Service 1, Rating of Health Plan 3. (The Network Operations seat at the same plan is a HOLD_SEAT lead and gets no Stars call at all; picking the wrong seat at a right account is the most expensive mistake on this list.) Variables: `plan_name` CalOptima, `contract_id` H5433, `measure_read` "1 star on Customer Service and 3 on Rating of Health Plan".

**Opener**
> "Marsha." [pause] "It's Nathan Belfield at Intradiem. I'm calling about the member survey CMS kept when it recalculated bonus ratings this summer, and the one score in it that gets set in your own service centres. Can I take 30 seconds, and you tell me if it's not for you?"

**If they engage**
> "Two of the three questions behind the Customer Service score are about the call itself: whether the member got the help they needed, and whether they were treated with courtesy. CMS has H5433 at 1 star on Customer Service. Intradiem sits on top of the WFM those centres already run and holds adherence and handle time steady through the day. Humana has that half on the record, handle time down 45 seconds. The survey half has no number behind it yet." Then hand over the floor: "Does that line up with how the score moves on your side?"

**The ask**
> "Fifteen minutes on which of those three questions your service operation can actually reach on H5433, before the survey goes out in March."

**If they're busy**
> "Completely get it. Ten seconds so you know what this was: the Customer Service score on H5433 is the one survey measure your service centres set. When's better this week for a proper fifteen minutes?"

**If they brush you off**
> "Understood. One thing before I go: is that because the Customer Service score is already someone's project this cycle, or because the attention is on the clinical measures?" Then the call ends on their answer. No release line, no second pitch, log what they said.

**No answer, voicemail**
> "Marsha, Nathan Belfield with Intradiem. I sent you a note on the customer service score at CalOptima, the one survey score that gets made in your service centres, and that's the part I wanted to talk through. There's a short note from me in your inbox with the detail. I'm at 937-238-3179. Thanks Marsha."

Why this passes: the reason lands before the contract; one idea, not three; the measure named is one our service operation actually reaches; the Humana number is Lane 1 verified and the gap is stated out loud rather than implied; the expansion ends on a check question; the ask names its payoff and a date; the brush-off stops without apologising.

## What bad sounds like, and why

Adapted from the Sep 4 before-and-after. Every left-hand line was written by us and cut.

| Wrote this | Should be | Why it fails |
|---|---|---|
| "Did I catch you at an OK moment?" | Reason first, then "Can I take 30 seconds, and you tell me if it's not for you?" | Banned opener family, roughly 40% below baseline |
| "If this is the wrong desk, a name is all I need." | "Worth fifteen minutes to find out what yours is?" | Admits no research. The pool is mapped |
| "...and then I'll leave you be." | Cut it, end on the ask | Exit talk, fails Sep 4 |
| "I asked your colleague the same thing, I honestly can't tell whose desk this lands on." | "Aldemaro owns the transformation side of this, so I've sent the same note there." | Never admit not knowing the org. State the fact from the map |
| Expansion straight into "so can we get fifteen minutes?" | Expansion, then "Does that match what you see?" | A monologue ending in an ask. Booked calls have back-and-forth |
| "The complaints and appeals measures price your bonus this cycle." | "Customer Service is the one score CMS kept that your service centres set." | Retired claim. CMS pulled those out in June 2026 |
| "We help you transform your member experience." | "We hold adherence and handle time steady through the day, on top of the WFM you already run." | Category language and a banned word. Say the concrete action |
| Naming Getting Appointments or Care Coordination to a quality leader | Customer Service, or nothing | Those are answered about the doctor's office. Reads as a mismatch |

## Self-check before the script ships

Run every line. A no is a rewrite, not a note.

1. Does the opener state the reason BEFORE asking for time, with no availability yes/no?
2. Is the reason built only from this lead's stored variables and the brief's playbook sources?
3. Is there exactly one idea, and is it this seat's idea rather than the account's?
4. Does the expansion end on a check question that hands over the floor?
5. Does the ask name what they get, and a date or a window?
6. Is every number Lane 1 verified, or a Lane 2 fact with a source inside its freshness window?
7. Zero apology and zero exit phrases anywhere outside the breakup?
8. Busy and brush-off branches present on dial tasks, brush-off ending without a second pitch?
9. Voicemail under 25 seconds, carrying the hook, with the callback line intact?
10. Seven labelled blocks or fewer, two pushback blocks or fewer?
11. If a Star measure is named, is it Customer Service or Rating of Health Plan, and is the reconciliation doc still inside its expiry?
12. Read it aloud. Does it sound like Nathan on a Tuesday, or like a document?

## Integration

```
cognitive-calibration        (always first)
   -> intradiem-first-draft-engine   (the one idea, the persona angle)
      -> intradiem-cold-call-playbook (this: spoken shape, handles, gate)
         -> intradiem-verified-metrics (every number)
            -> intradiem-copy-sharpener (final QC, spoken-word standards)
```

`intradiem-objection-handler` owns replies to inbound pushback and is the deeper reference when a live call surfaces something these handles do not cover.

## What this skill does NOT do

It does not dial, schedule or log. It does not invent facts about an account; research comes from the account's own files and the lead's variables. It does not override a rep's proven language. It does not restate the canon's structure as its own, and it is not the place to change the opener contract.
