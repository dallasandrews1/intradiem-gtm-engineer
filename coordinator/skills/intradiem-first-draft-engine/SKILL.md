---
name: intradiem-first-draft-engine
description: "Pre-production thinking framework for Intradiem outreach messaging. Forces prospect-first cognition, single-idea message construction, and voice-matched drafting BEFORE any rules or checklists are applied. Produces a first draft that sounds like a real person wrote it in one sitting. Runs before intradiem-copy-sharpener, not after. Also the thinking layer for any edit to the Clay MessageGen system prompt. Trigger on any request to write, draft, or create Intradiem outreach messaging of any kind: emails, LinkedIn InMails, DMs, voice notes, follow-ups, Clay message variants, or any prospect-facing copy. Load proactively whenever messaging output is expected."
---

## When this skill applies

- BEFORE writing any prospect-facing outreach copy (emails, LinkedIn, DMs, voice notes + TL;DL summaries, follow-ups)
- BEFORE intradiem-copy-sharpener runs (this produces the draft; the Sharpener verifies it)
- When designing or editing message variants for the Clay Message Gen table (this skill governs the thinking; `Clay_MessageGen_SystemPrompt_v2.md` is the deployed expression of it)
- When any roadmap, strike plan, or sequence step requires written messaging
- Load proactively whenever messaging output is expected

## Who sends the message (Intradiem-specific)

Dallas engineers the messaging; a rep usually sends it. Default sender for the Star Ratings motion is Nathan Belfield (Sales, Pipeline Generation). Always confirm the sender before drafting, write in THAT person's voice, and sign with THAT person's name. Never default to "Dallas" as the signature. Gate 1 must include: who is the sender, and what can this sender truthfully say they have seen or done?

## Scope reminder

Intradiem sells Dynamic Workforce Orchestration across contact centers AND back offices, six verticals (Healthcare, Financial Services, Insurance, Retail, Telecom, Utilities). Never write copy that frames it as a call-center tool. WFM players (Verint, NICE, Calabrio) are the layer we sit on, never competitors to attack.

## Background

This skill exists because of a specific, recurring failure: outreach copy that passes every rule in the Copy Sharpener but does not read like a real person with a clear thought wrote it. The failure happens when drafting starts with rules and builds sentence-by-sentence against a checklist, producing technically compliant but lifeless copy. The best-performing messages start with one clear idea and flow from that idea as a single thought. The rules come second.

The correct process:

1. Ask one question: what does this prospect need to hear that they do not already know?
2. Write the entire message from that one idea as a flowing thought
3. Read it back as the prospect and ask: would I say yes?
4. THEN check it against the framework and fix anything actually broken

## The Five-Gate Thinking Sequence

Every piece of outreach copy passes through these gates IN ORDER. Do not skip or reorder. Do not start writing until Gate 2 is answered.

### Gate 1: The Prospect's Chair

Before writing a single word, answer silently:

- Who is this person? What is their day-to-day world?
- What are they worried about RIGHT NOW?
- What do they already know about their own situation? (You cannot open with this.)
- What DON'T they know that would make them stop and think?
- If they got this while scanning 200 emails on a Tuesday morning, what makes them pause?
- Who is the sender, and what can the sender truthfully claim?

**The research inventory rule.** Before writing, enumerate every specific, named detail from research: contract IDs, weighted-average scores, measure names, earnings-call quotes, dollar figures, leadership changes, hiring clusters, regulatory dates (the October CMS release, CMS-4208-F3 measure removals), tech-stack facts. Write FROM those details, not from the account-level narrative that summarizes them. "Plans under quality pressure" is narrative; "your weighted average sits right around 3.91, just under the 4.0 line" is the detail. If the detail exists and you did not use it, the message is weaker than it should be.

**Star Ratings humility clause (mandatory for Stars copy).** Public CMS math is an outside estimate. Every Stars message that cites a computed number carries a version of "you will know the exact picture far better than I do." Confidence about the mechanism, humility about their internal numbers. This is the tone of the motion's gold-standard sample (the Point32 message on Naveen's onboarding site).

**The prospect knows their own world.** Never open by narrating their situation back to them. "Your contract is below 4 stars" is narration. "The call center measures are the first to come out under the 2028 window, which makes them the cleanest lever left" is a connection they may not have made.

**The prospect knows their own expertise.** A 25-year operations executive can diagram how idle time, shrinkage, and adherence interact in her sleep. Never explain a mechanism to someone whose career proves they already understand it. Gate 1 must answer: what does this person already understand because of who they are, that I must NOT explain? Replace mechanism explanations with the human-level consequence they are watching play out.

**Verify attribution before you reference it.** Confirm any initiative, program, or public statement actually belongs to the prospect's scope before weaving it in. Referencing someone else's initiative as theirs shows sloppy research and destroys the credibility the specificity was supposed to build. When in doubt, reference the underlying problem (which IS theirs) rather than the named program.

**Evidence versus relationship evaluators.** Clinician-executives, actuaries, engineers, and career operators evaluate evidence: SHOW the finding in the body and let the meeting offer the operational details. Sales, marketing, and BD leaders can be drawn by curiosity: a tease can work. When in doubt, show. Showing always works.

**Classify the forcing function: proud or defensive.** PROUD (new leadership role, expansion, a modernization investment, a product launch) is safe to lead with. DEFENSIVE (a ratings downgrade, public complaint data, layoffs, a failed vendor rollout, an outage in the news, earnings misses) is a wound; leading with it reads as an attack dressed as insight. Every defensive forcing function has a proud response behind it: the downgrade produced a quality investment, the outage produced a resilience program, the miss produced an efficiency mandate. Lead with the response, never the wound. For Stars: a plan under 4.0 is a defensive fact. Frame around the lever still available and the window still open, not around the failure.

**The prospect is skeptical by default.** They receive hundreds of cold messages. Yours earns attention by demonstrating you understand their world well enough to say something their own team has not already told them.

### Gate 2: The One Idea

Every message has exactly one idea, stated in a single sentence before writing. Examples of the shape:

- "The call center measures come out of the ratings first, which makes the 2026-2027 measurement years the cleanest attribution window a quality leader will get."
- "There is a cutoff point where adding back-office headcount stops absorbing backlog and becomes the expensive option, and finding it makes every downstream decision easier."
- "The idle time already inside her schedule adherence data is the training budget she thinks she does not have."

If you cannot state the one idea in one sentence, you do not have a message yet. Test it: does this give the prospect something they do not already have? If two prospects in the same account end up with the same one idea, one of them is wrong.

### Gate 3: Write It Like You Said It

Write the entire message in one pass as if saying it aloud to a peer.

- **The first sentence does exactly one thing.** One complete thought, landed fully. If describing what it does requires "and", it is doing too much.
- **Every sentence flows from the one before it.** Forced transitions mean the sentences do not belong together.
- **Do not stop to check rules mid-draft.** Rules come at Gate 5.
- **Vary sentence length naturally.** Rhythm of speech, not a checklist executing.
- **Merge consecutive short sentences in body paragraphs** with commas, "and", "but", "because". Staccato chains read like bullet points disguised as prose. (The Day 1 three-beat close is the intentional exception.)
- **Use connective tissue.** "The reason that matters," "Here's the thing," "That's usually where."
- **Do not over-explain.** If Gate 1 mapped their expertise, cut every sentence explaining what they already own.
- **Never make the sender the subject of a sentence.** No credential lines ("I work with operations teams navigating..."). Establish authority through the insight, not the resume. Show the finding; do not tease it or credential past it.
- **Purge rep-language.** "Plans your size," "companies like yours," "leaders in your space," "I help organizations" read like a template with placeholders. Replace with peer language: "the part I keep thinking about," "the pattern I keep seeing."
- **Never describe the solution category.** "Real-time workforce automation," "intraday management platform," "orchestration layer" are product tells; the prospect reads them and knows the pitch. Describe the human reality instead: "the twenty minutes between calls that nobody can schedule," "the backlog that grows back every Monday," "agents who have not had a coaching conversation since onboarding." If a prospect could guess what your company sells from the sentence, rewrite it.
- **The CTA must be the natural conclusion of the one idea.** It should feel inevitable, not bolted on.

### Gate 4: The Prospect Test

Read the entire message back as the prospect, on their phone, between meetings.

1. Would I keep reading after the first sentence?
2. Do I know why this person is contacting me: why ME, why NOW, about WHAT?
3. Do I know what I would get from a meeting, useful whether or not I ever buy?
4. Can I say yes without feeling like I am agreeing to a sales pitch?
5. Is there one clear thought, or multiple ideas stitched together?
6. Does any sentence make the sender the subject instead of me?
7. Can I guess what this person sells? (If yes, a product tell survived. Rewrite.)
8. Does any sentence explain something I already know because of who I am?
9. Does it open by reminding me of something painful? (Lead with the response I am proud of, not the wound.)

If any answer is no, return to Gate 3 and rewrite. Never show a draft that fails this test.

**The batch generation honesty problem.** In multi-prospect sessions, rigor decays: contact 1 gets a genuine simulation, contact 8 gets a rubber stamp. After ALL copy is drafted, re-run Gate 4 on every piece with fresh eyes, each message evaluated as if it were the only one. This matters double at Intradiem because Clay generates at scale: any laziness in the thinking layer gets multiplied by every row in the table.

### Gate 5: Rule Check (Light Touch)

Now check against the Copy Sharpener fundamentals, as a READER, not an auditor. The question is "does anything break the spell?", not "does every sentence satisfy a rule?"

Quick scan for:

- Forbidden words and phrases (see Sharpener)
- Em dashes (never in prospect-facing copy; replace with periods, commas, colons)
- Intradiem named in Days 1-5 copy (brand-light window)
- Sign-off correct: sender's first name Days 1-5, full name Day 6+, never "Dallas" unless Dallas is genuinely the sender
- Word count within channel range
- CTA ends on a question
- Vague AI metaphors ("gets heavier," "at a critical juncture," "navigate the landscape"): replace with the specific, concrete statement the metaphor is avoiding
- **Verified-claims gate (hard stop):** every Intradiem stat, customer outcome, or ROI figure must be confirmed against the intradiem-verified-metrics skill / Value Repository. Figures from `roi_model.json`, `proof.json`, or any engine output are placeholders and NEVER appear in prospect copy as fact. Unconfirmed claims ship as [UNVERIFIED] or not at all.

If the message passes Gates 1-4 and reads like a real person with a clear thought, do NOT rewrite sentences to better satisfy individual rules. Fluidity of the whole beats compliance of any line.

## Voice Note TL;DL Rule

Every voice note script gets an accompanying 2-3 sentence written TL;DL that passes the same five gates: the one idea plus the CTA, standing alone even if the audio is never played.

## The CTA Discipline

- **The Vague Ask** ("Worth a conversation?"): the CTA must name the topic the conversation addresses.
- **The Over-Promise** ("with the data behind those numbers"): frame the meeting as a conversation, not a deliverable the sender may not have.
- **The Disconnected CTA:** the CTA is the conclusion of the one idea, nothing else.
- **The Meeting-As-Favor:** frame it so the prospect benefits ("Worth 15 minutes to hear how you're approaching your cliff-edge contracts?"), never so they are granting an audience.
- **The Credential Bridge:** never bridge body to CTA with "I work with...". Give the insight in the body; let the CTA offer the specifics.

**The Three-Beat Day 1 Close** (cold email 1 only): (1) one short peer proof-point sentence [verified source only], (2) one standalone "Might be helpful to walk you through..." sentence, (3) blank line, then "Worth 15 min in the next few weeks?" on its own line, (4) blank line, sender's first name. Senior contacts get "in the next few weeks"; tight time anchors on C-suite cold outreach signal desperation.

## Persona Notes (Intradiem buying world)

- **VP/SVP Stars, Quality, Medicare (Star Ratings motion):** lives in measure math and cut points. Evidence evaluator. Window language lands; humility clause mandatory; never lecture on how Stars works.
- **COO / SVP Operations:** career operator; imply mechanisms, name consequences. Operational relief, never brand vision.
- **VP Customer Care / Contact Center:** owns AHT, adherence, shrinkage, attrition daily. Insight must beat what her own WFM reporting already tells her.
- **VP Back Office / Shared Services / Claims Ops:** the white space. Backlog, cost-per-transaction, overtime. Often has NO real-time visibility today: the "you cannot see idle capacity you do not measure" family of ideas lives here.
- **CFO / VP Finance:** cost per contact, capacity without headcount, payback. Numbers-first, no adjectives.
- **CIO / CTO:** integration surface, security posture, what sits on top of the ACD/WFM stack. Third-party validation over claims.

## What This Skill Does NOT Do

- Replace the Copy Sharpener (post-production gate)
- Contain word-count tables or channel mechanics (Sharpener)
- Handle sequencing and touchpoint scheduling (roadmap skills)
- Conduct research or build strike plans (upstream engines and skills)

## Output

No separate file. This skill governs the PROCESS inside any other skill's output. When asked for copy directly, deliver: the message ready to send, one sentence stating the one idea behind it, nothing else unless asked.
