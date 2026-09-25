---
name: intradiem-copy-sharpener
description: "Intradiem outreach copy quality check. Takes drafted messaging and runs the eight-line QC from motions/shared/Messaging_Doctrine_Sep3.md plus the hard verified-claims gate against the Intradiem Value Repository, then returns send-ready copy with a short changes log. Runs AFTER intradiem-first-draft-engine. Trigger on any request to sharpen, review, check, or finalize Intradiem outreach copy: emails, LinkedIn notes and messages, voice scripts, call scripts, breakups, Clay message variants, lemlist per-lead variables."
---

## Source of truth

This skill implements `motions/shared/Messaging_Doctrine_Sep3.md`. If they disagree, the doctrine wins. The Sep 3 doctrine retired the brand-light rule, the three-beat close, the five-email escalation ladder, the full-name-from-day-6 sign-off and the 22-point send-ready test. Do not reintroduce them. Copy a BDR has shared as having booked meetings is the reference, not the thing to correct.

## When this skill applies

- After intradiem-first-draft-engine has produced the draft. Never use this skill as the starting point for writing. If the First Draft Engine has not loaded, load it first.
- On every piece of outreach copy before it is loaded into lemlist, seeded into a Clay MessageGen table, or entered into the conductor's approval queue.

## Posture

This is a check, not a construction tool. If a line breaks a rule but the message reads like a real person with a clear thought and passes the prospect test, the message wins. Fix only what genuinely breaks the spell: an unverified number, a calendar ask in Email 1, a category label instead of a product sentence, an em dash, a banned word, a wrong sender, a missing dated signal. Fluidity of the whole beats compliance of any line.

## Who signs

Confirm the sender per motion (US: Nathan Belfield; UK: Jack O'Hagan). First name only in every message. The mailbox signature block carries the rest.

## Scope reminder

Dynamic Workforce Orchestration across contact centers AND back offices, six verticals. Copy that reads "call-center tool" fails. Verint, NICE, Calabrio and the CCaaS platforms are the layer we act on, never rivals to trash.

## The eight-line QC

1. **Opens on their world with a dated signal, and says what we do by sentence three.** The product sentence describes concrete actions on top of what they already run. Category labels ("real-time workforce automation", "intraday management platform", "orchestration layer") fail. Intradiem named once in Email 1 is correct, not a violation.
2. **Numbers.** Every Intradiem number, customer outcome or peer claim traces to a VERIFIED row in the Value Repository (check via intradiem-verified-metrics, never from memory). Every prospect number has a source dated within 90 days. Industry benchmarks stated as fact fail. Figures from roi_model.json, proof.json or engine output never ship. Anything unconfirmed: rewrite without it or mark [UNVERIFIED] and flag. Silent inclusion is the one unforgivable failure. UK copy may carry the CONFIRM-tier UK sales claims on Jack's authority; US copy may not until they are VERIFIED.
3. **Email 1 ends on one question that names the topic.** No calendar, no minutes, no demo, no time slot, no stacked questions. Allowed shapes: the benchmark question ("Worth a conversation on how other [persona] teams run this?") or the offer note ("Is it worth me sending over how other [vertical] teams are approaching this? No meeting attached."). Meeting-with-time asks start at the day-7 LinkedIn message or Email 2.
4. **Length falls through the sequence.** Email 1 under 110 words, Email 2 shorter than Email 1, Email 3 under 60. LinkedIn connect note under 300 characters, counted. LinkedIn message 50 to 100 words. Voice note under 45 seconds with a TL;DL. Voicemail under 25 seconds. Exec air cover under 80 words.
5. **One angle per person.** No two contacts in one account share the same one idea or open the same way. Same verified numbers across the account.
6. **Language.** No em dashes (periods, commas, colons instead). Contractions always. Banned: leverage, synergy, cutting-edge, best-in-class, empower, seamless, robust, transform, transformation, catalyst, paradigm, innovative, comprehensive, unlock, streamline, game-changer, journey, "I hope this finds you well", "quick question", "circle back", "touch base", "reach out", "just following up", "bumping this", "I know you're busy", "I'd love to", "happy to", "excited". No exclamation marks. No qualifiers ("I think", "hopefully"). No engagement-tracking references. No implementation timelines unless verified. No vague AI metaphors ("navigate the landscape", "at a critical juncture"). Subject lines short, lowercase, conversational; Email 2 and 3 as "re:" replies. First-name sign-off.
7. **Account layer.** Coordination note present; account intel encoded as rules in the header (prior no, dead channel, quarantine, names to find); situational play applied where one fits.
8. **Gates.** Customer-exclusion gate passed on every row. Opt-out line on UK and customer-lane Email 1. Stars humility clause wherever a computed number appears. Proud-not-wound opener. **Stars measure check:** if the copy names a Star Ratings measure, only the durable six may appear, and of those only Customer Service and Rating of Health Plan may be tied to what our service operation reaches. Complaints, appeals, members choosing to leave, and call center interpreter and TTY are operational pain only, never bonus-money claims, and Getting Appointments, Getting Needed Care and Care Coordination are about the doctor's office. Verify against `StarRatings_Measure_Reconciliation_Clover_Sep21.md`, which expires at the CMS October 2026 release.

## Persona check

Read every sentence against the persona's row in the angle library (First Draft Engine). Finance reads numbers and payback with no adjectives; operators want implied mechanisms and named consequences; planners want the intraday layer in their own vocabulary; Stars leaders want measure math and humility; back-office leaders want the backlog as a timing problem and a live view they do not have today; technology leaders want integration surface and third-party validation.

## Spoken-word standards

For any spoken output, check it against `intradiem-cold-call-playbook` as well: the banned availability-opener family, the ask naming its payoff, the brush-off hard stop, the branch cap, and the Star Ratings measure rules. A script that passes the eight-line QC can still fail the call contract.


- **Cold call**: under 45 seconds. Name plus one credible sentence, one specific observation about their business, one verified peer result or the product sentence, a soft ask. Never open with "I know you're busy" or "Do you have a minute?". Objection handlers for "Who is this?", "Not a good time", "Send me an email", "We already have WFM", "We built it in-house".
- **Voice note**: under 45 seconds. First and last name, one verifiable reference to their business, one insight, soft next step. Ships with its TL;DL.
- **Voicemail**: under 25 seconds. Name, one sentence of context, callback reason, name again at the end. No pitch.
- **LinkedIn**: pending connection gets an InMail with a DM version underneath; fresh connection gets a short text DM; long-standing connection gets a voice note with TL;DL. Connect note under 300 characters referencing the email, or blank where the rep prefers it.

## Output

Save as `[Account]_Copy_Check_[Channel].md` when a file is wanted; otherwise return inline.

Sections: header (date, channel, recipient, sender, sequence position) → QC results, eight lines, PASS or FIX each → send-ready copy → changes log (original, revised, which line, why) → verified-claims ledger (each claim and its Repository row or [UNVERIFIED]) → one-line recommendation.

## Worked example (back-office healthcare payer, Email 1, sender Nathan)

**Draft that fails lines 1 and 3:**
"Hi {{firstName}}, there's a pattern in claims and appeals operations that rarely makes it into the staffing conversation: the backlog that gets cleared by Friday grows back by Monday, while the week's schedules already hold enough idle minutes to absorb it. Might be helpful to walk through where those windows usually sit. Worth 15 min in the next few weeks?"

**Why:** no dated signal, never says what we do, calendar ask in Email 1, the three-beat template ending.

**Passes:**
"Hi {{firstName}}, [dated signal per lead] puts the Monday backlog on a different footing this year, and most claims teams are still staffing it by guesswork.

Intradiem's Back Office Optimizer shows you exactly how much work is piling up, whether the staff you have can handle it, and which case each worker should tackle next, before you miss an SLA or pay a penalty. It sits alongside the WFM and case system you already run.

Worth a conversation on how other payer claims teams are running the week?

Nathan"

Claims ledger: no Intradiem number used (the BOO framework's only figure is an illustrative model). Product sentence is marketing's own line from `04-value-repository/BOO_Messaging_Framework_Jun26.md`. Signal ships only with its dated source.

## Product sentence sources (Sep 3 2026)

Back office: `04-value-repository/BOO_Messaging_Framework_Jun26.md` (marketing's value proposition, personas, elevator pitch, tone). Front office and DWO: the official value deck claims in the Value Repository (7X ROI with payback in as little as 3 months, 90 to 120 day deployment, 6 to 10 percent productivity savings within weeks) and the 2X contract guarantee. Customer proof: `04-value-repository/Customer_Stories_Registry_Jul21.md`; only Humana and Virgin Media by name; JPMC, AT&T and Liberty Mutual never. Index of every source: `motions/shared/Product_Materials_Index_Sep3.md`.

## Sep 4 addendum (the pressure standard, Dallas: "the new standard of quality for messaging")
Read the Sep 4 addendum at the end of the doctrine and `motions/shared/Messaging_Gold_Examples_Sep4.md` before returning any verdict. Four more QC lines apply on top of the eight: (9) every call step has a voicemail script and an EA route; (10) no admission of not knowing the org, colleague references are stated facts from the account map; (11) no apology or exit phrase anywhere except the single breakup ("sorry", "fair enough", "I'll be quick", "I'll stop", "I'll leave you be", "closing the file", "closing this out", "no need to reply", "either answer helps me stop guessing" all fail), every touch ends on an ask; (12) delays written as relative days before they enter lemlist. Direct asks are fine from Email 2 on.
