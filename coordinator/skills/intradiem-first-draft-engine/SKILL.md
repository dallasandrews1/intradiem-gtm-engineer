---
name: intradiem-first-draft-engine
description: "Pre-production thinking framework for Intradiem outreach messaging. Forces prospect-first cognition, single-idea message construction, a persona-to-angle library, situational plays, and voice-matched drafting BEFORE any checklist is applied. Produces a first draft that sounds like a real person wrote it in one sitting. Runs before intradiem-copy-sharpener, not after. Also the thinking layer for any edit to the Clay MessageGen system prompt. Implements motions/shared/Messaging_Doctrine_Sep3.md. Trigger on any request to write, draft, or create Intradiem outreach messaging of any kind: emails, LinkedIn InMails, DMs, connect notes, voice notes, follow-ups, breakups, Clay message variants, or any prospect-facing copy. Load proactively whenever messaging output is expected."
---

## Source of truth

This skill implements `motions/shared/Messaging_Doctrine_Sep3.md` in the Intradiem GTM Engineer repo. If this file and the doctrine disagree, the doctrine wins. The doctrine adopts the practice of the two BDRs, Jack O'Hagan (UK) and Nathan Belfield (US), who are the experts on what gets a reply. On Sep 3 2026 it retired the brand-light rule, the three-beat close, the five-email ladder and the 22-point test; none of those apply any more.

## When this skill applies

- BEFORE writing any prospect-facing outreach copy (emails, LinkedIn connect notes and messages, voice notes with TL;DL, breakups, exec air cover)
- BEFORE intradiem-copy-sharpener runs (this produces the draft; the Sharpener checks it)
- When designing or editing Clay MessageGen prompts or lemlist per-lead variables
- When any strike plan, sequence, or account pack needs written messaging

## Who sends

Dallas engineers the messaging; a rep sends it. US default is Nathan Belfield. UK is Jack O'Hagan. Always confirm the sender, write in that person's voice, sign with that person's first name only. Never "Dallas" unless Dallas is genuinely the sender. Gate 1 must answer: who is the sender, and what can this sender truthfully say they have seen or done? When the rep has shared copy that booked meetings, that copy is the voice reference; match it before applying anything in this file.

## Scope reminder

Intradiem sells Dynamic Workforce Orchestration across contact centers AND back offices, six verticals (Healthcare, Financial Services, Insurance, Retail, Telecom, Utilities). Never write it as a call-center tool. WFM players (Verint, NICE, Calabrio) and CCaaS platforms are the layer we act on, never rivals to attack.

## The message shape (from the doctrine)

Cadence: Email 1, LinkedIn connect (day 2), Email 2 (day 4), LinkedIn message (day 7), Email 3 breakup (day 11). Phone between touches for planning, WFM and performance personas. A blitz may compress to ten days; it never adds emails.

- **Email 1**: their world and a dated signal in sentence one. What we do in one concrete sentence by sentence two or three, Intradiem named once. One idea. One question at the end that names the topic, with no calendar, no minutes, no demo. Under 110 words.
- **Email 2** (in thread): one new angle or one new verified number from the library. Shorter than Email 1. One question. Never "bumping this".
- **Email 3** (breakup): shortest, under 60 words. Names the re-entry condition and wishes them well specifically.
- **LinkedIn connect**: under 300 characters, counted, references the email.
- **LinkedIn message** (day 7): short version of the email plus the conversation offer.
- **Exec air cover**: one email under 80 words, only after an operational thread is live, naming the engaged colleagues.

## The Five-Gate Thinking Sequence

Every message passes these gates in order. Do not start writing until Gate 2 is answered.

### Gate 1: The Prospect's Chair

Answer silently before writing:

- Who is this person and what is their day-to-day world? What are they worried about right now?
- What do they already know about their own situation? (You cannot open with this.)
- What do they NOT know that would make them stop and think?
- Who is the sender, and what can the sender truthfully claim?
- Which persona row in the angle library is this person, and what is their worldview sentence?
- Which situational play applies (new in role, win-back, prior no, gatekeeper, air cover, build-in-house)?

**Research inventory rule.** Enumerate every specific, dated detail from research: contract IDs, weighted scores, earnings-call lines, leadership changes, hiring clusters, platform migrations, regulatory dates, site openings. Write FROM those details. A signal without a date cannot support a why-now email.

**The prospect knows their own world and their own expertise.** Never narrate their situation back to them, never explain a mechanism a career operator already owns. Name the consequence they are watching play out.

**Verify attribution.** Confirm an initiative belongs to the prospect's scope before referencing it. When in doubt reference the underlying problem, which is theirs.

**Proud, not wound.** A downgrade, outage, miss or layoff is never the opener. Every defensive fact has a proud response behind it; lead with the response.

**Star Ratings humility clause (mandatory).** Every computed Stars number carries "you will know the exact picture far better than I do."

### Gate 2: The One Idea

One sentence before writing. If you cannot state it in one sentence you do not have a message. If two people in the same account end up with the same one idea, one of them is wrong; pick a different angle from the library.

### Gate 3: Write It Like You Said It

Write the whole message in one pass as if saying it to a peer.

- The first sentence does exactly one thing: their world plus the dated signal.
- The product sentence says what Intradiem does in concrete actions ("spots idle windows as they open, routes aging cases into them, pushes training into the quiet hours, on top of the WFM you already run"). Never a category label ("real-time workforce automation platform", "intraday management solution", "orchestration layer").
- Every sentence flows from the one before. Merge short declaratives with commas, "and", "but", "because". Vary rhythm.
- Never make the sender the subject of a sentence. No credential lines. Authority comes from the insight and the product sentence, not the resume.
- Purge rep language: "plans your size", "companies like yours", "leaders in your space", "I help organizations".
- The closing question is the natural conclusion of the one idea and names the topic.

### Gate 4: The Prospect Test

Read it back as the prospect, on their phone, between meetings.

1. Would I keep reading after sentence one?
2. Do I know why me, why now, about what?
3. Do I know what this company does, in one sentence, without guessing?
4. Can I say yes without agreeing to a sales pitch?
5. Is there one thought, or several stitched together?
6. Does any sentence make the sender the subject instead of me?
7. Does any sentence explain what I already know because of who I am?
8. Does it open with something painful?

If any answer fails, back to Gate 3.

**Batch honesty.** After drafting a whole account, rerun Gate 4 on every message as if it were the only one. Clay and lemlist multiply any laziness by every row.

### Gate 5: Doctrine QC (light touch)

Run the eight-line QC from the doctrine as a reader, not an auditor:

1. Email 1 opens on their world with a dated signal and says what we do by sentence three.
2. Every Intradiem number traces to a VERIFIED Repository row (intradiem-verified-metrics). Every prospect number has a source under 90 days old. Nothing else carries a number. Unconfirmed claims ship as [UNVERIFIED] or not at all. Figures from roi_model.json, proof.json, or engine output never ship.
3. Email 1 ends on one question, no calendar, no demo, no minutes.
4. E1 under 110 words, E2 shorter, E3 under 60. Connect note under 300 characters, counted.
5. No two people in one account share the same angle.
6. No em dashes, no banned words, no "hope you're well", first-name sign-off.
7. Coordination note present, account rules encoded in the header.
8. Customer-exclusion gate passed, opt-out line where required.

If the message passes Gates 1 to 4 and reads like a real person, do not rewrite sentences to satisfy a rule. Fluidity of the whole beats compliance of any line.

## Persona to angle library

Pick by what the title owns. Same verified numbers across an account, different framing per person.

**Front office**

| Persona | Angle | Worldview sentence |
|---|---|---|
| Head of Resource Planning / WFM | The intraday layer WFM never finished. Practical, sits on top of what they run. | "The plan is right at 8am and wrong by 10, and your team absorbs the drift by hand." |
| Contact centre / Ops Director | Scale and timing. Tie to the live event. Productivity while hiring, never redundancy. | "Growth becomes contact volume." |
| Performance / Op Ex | The last unmeasured variance. | "The biggest number never makes your dashboards." |
| Customer / Service Director | One lever moving cost and service the same direction. | "Coaching happens when we're quiet, which is never." |
| Complaints / Quality owner | Upstream lever. | "The rushed call becomes the repeat contact becomes the complaint." |
| Transformation / Automation lead | Highest-certainty item on the roadmap, nothing new to govern. | "A known number in a portfolio of modelled benefits." |
| VP/SVP Stars, Quality, Medicare | Measure math, cut points, the 2028 window. Evidence evaluator. | "The call centre measures are the cleanest lever left." |
| Group / C-level | Air cover only, after a thread is live. | |
| New in role (six months or less) | A visible first-year win with no restructure. | "The listening tour ends and the agenda gets written." |

**Back office** (marketing's four BOO personas and what each is measured on live in `04-value-repository/BOO_Messaging_Framework_Jun26.md`: WFM Champion, Economic Buyer COO/VP Ops, Technical Buyer IT/CTO, End User Head of Ops. Read them before choosing a row.)

| Persona | Angle | Worldview sentence |
|---|---|---|
| VP/Dir Claims Ops, Appeals, Payment Ops | Backlog is a timing problem, not a staffing problem. | "The backlog cleared by Friday grows back by Monday." |
| VP/Dir Shared Services | Utilisation they cannot prove, no live view across queues. | "You can't see idle capacity you don't measure." |
| Document processing / intake | Peak intake is visible in the data days before the queue feels it. | "The weeks that age cases show up in intake first." |
| Back-office technology / ops systems | Integration surface, sits on top of the case system and WFM. | "Nothing new to govern, nothing to rip out." |
| COO / SVP Operations | Operational relief, never brand vision. | "The backlog is paid for twice: overtime and rework." |
| CFO / VP Finance | Capacity without headcount, payback, cost per transaction. No adjectives. | "Headcount stops absorbing backlog at a point nobody has found yet." |

Vertical translation keeps the mechanics and swaps the pressure: insurance to claims surges and Consumer Duty; utilities to price-cap cost pressure and winter surge; telco to churn and complaints tables; banking to branch-to-contact-centre migration; healthcare to Stars, patient access, appeals timelines; BPO to client SLAs and margin per seat. Mutuals and public-facing brands: service up, never heads down.

## Situational plays

- **New in role**: congratulate, name the moment, position the first-year win. Email 2 names the internal pressure-testers.
- **Win-back / ex-user**: never a stranger, never pleading. "You'll know Intradiem from your [company] days, so I'll skip the intro." Never criticise the tool they switched to.
- **Exec air cover**: one email under 80 words, only after an operational thread is live, naming engaged colleagues.
- **Prior no**: quarantine. One re-approach email that quotes their words and leads with what changed, fired only on a named trigger.
- **Gatekeeper known to kill deals**: one touch positioning them as the expert; ask for their read, never pitch.
- **Build-in-house**: no cadence; one LinkedIn benchmark-participation touch.
- **Policy bounce**: email channel dead, stop, convert to phone and LinkedIn.

Encode every piece of account intel as a rule in the account header so it cannot be forgotten.

## Coordination note (every account)

Contact order by day; who is estate owner, evaluator, sponsor, budget holder in waiting; hit everyone the same week and say so; who pulls whom into a call; "this team compares notes, keep the numbers identical"; account rules (quarantines, dead channels, names still to find).

## Voice Note TL;DL Rule

Every voice note script gets a 2 to 3 sentence written TL;DL that passes the same gates and stands alone if the audio is never played.

## Market rules

- **UK / EU**: opt-out line in Email 1. Email 1 ending is the benchmark question or the offer note (see `motions/shared/Offer_Notes_Aug3.md`), never a calendar ask. Jack's `vertical-strategy-pack` skill governs UK account packs; Jack's UK product facts are CONFIRM tier in the Value Repository and ship only in UK copy on his authority.
- **Netherlands**: written natively, lead with the relevance ask, never localised.
- **US**: same shape. Nate's Email 1 A/B (variant A benchmark question, variant B offer note) keeps running until Nate calls it.

## What This Skill Does NOT Do

- Replace the Copy Sharpener (post-production check)
- Handle load mechanics, variables, or lemlist steps (Variable Seam Contract, motion-stamp)
- Conduct research or build strike plans (upstream engines and skills)

## Output

No separate file. This skill governs the process inside any other skill's output. When asked for copy directly, deliver: the message ready to send, one sentence stating the one idea, the persona row used, nothing else unless asked.

## Sep 4 addendum (the pressure standard)
The cadence line above is the Sep 3 floor. From Sep 4 the standard for net-new sequences is the pressure model in the doctrine's Sep 4 addendum: five emails across two threads, three calls that all leave voicemails (EA route when there is no number), three LinkedIn DMs for accepted connects, a voice note where the persona warrants it, one breakup last, invite withdrawn after it, 16 to 17 touches over 18 business days. C-level seats get calls. Write the colleague line as a fact from the account map, never as a guess. No apology, no exit talk, direct asks after Email 1. Reference copy: `motions/shared/Messaging_Gold_Examples_Sep4.md`.
