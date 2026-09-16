---
name: league-first-draft-engine
description: "Pre-production thinking framework for outreach messaging. Forces prospect-first cognition, single-idea message construction, and voice-matched drafting BEFORE any rules or checklists are applied. Produces a first draft that sounds like a real person wrote it in one sitting. Runs before the Copy Sharpener, not after. Trigger on any request to write, draft, or create outreach messaging of any kind: emails, LinkedIn InMails, DMs, voice notes, follow-ups, or any prospect-facing copy. Also trigger when the execution roadmap or full pipeline reaches a step that requires written copy. Load proactively whenever the user asks for messaging output."
---

## When this skill applies

- BEFORE writing any prospect-facing outreach copy (emails, LinkedIn, DMs, voice notes + TL;DL summaries, follow-ups)
- BEFORE the Copy Sharpener runs (this produces the draft; the Sharpener verifies it)
- When the execution roadmap or full pipeline reaches any step requiring written messaging
- When the user asks to draft, write, create, rework, or sharpen any outreach copy
- Load proactively whenever messaging output is expected

## Background

This skill exists because of a specific, recurring failure: outreach copy that passes every rule in the Copy Sharpener but doesn't read like a real person with a clear thought wrote it. The failure happens because the drafting process starts with rules and builds sentence-by-sentence against a checklist, producing technically compliant but lifeless copy. The best-performing finalized messages consistently start with one clear idea and flow from that idea as a single thought. The rules come second.

This skill encodes the actual cognitive process for arriving at the right first draft. It is not a set of rules. It is a thinking sequence. The Copy Sharpener is the post-production quality gate. This skill is the pre-production creative engine.

## The Core Problem This Skill Solves

When Claude writes outreach, it defaults to:
1. Loading rules from the Copy Sharpener
2. Constructing each sentence to satisfy a specific rule
3. Assembling sentences into a message
4. Checking the assembled message against the 20-point checklist

This produces copy that is mechanically correct but reads like a framework being executed. Each sentence serves a rule instead of serving the message. The result is fragmented, over-optimized, and lifeless.

The correct process is the reverse:
1. Ask one question: what does this prospect need to hear that they don't already know?
2. Write the entire message from that one idea as a flowing thought
3. Read it back as the prospect and ask: would I say yes?
4. THEN check it against the framework and fix anything that's actually broken

This skill enforces that sequence. No exceptions.

## The Five-Gate Thinking Sequence

Every piece of outreach copy must pass through these five gates IN ORDER before the user sees it. Do not skip gates. Do not reorder them. Do not start writing until Gate 2 is answered.

### Gate 1: The Prospect's Chair

Before writing a single word, answer these questions silently (do not output them to the user):

- Who is this person? What is their actual day-to-day world like?
- What are they worried about RIGHT NOW that keeps them up at night?
- What do they already know about their own situation? (This is what you CANNOT open with.)
- What DON'T they know that would make them stop and think?
- If they got this message while scanning 200 emails on a Tuesday morning, what would make them pause?

The answers to these questions are not the message. They are the lens through which you write the message.

**The research inventory rule.** Before writing a single word of copy, enumerate every specific, named detail from your research about this person and their situation: bill numbers, hearing dates, dollar figures, organizational changes, specific people they interact with, technology names, competitive pressures, regulatory deadlines. List them silently. Then write FROM those details, not from the account-level narrative that summarizes them. The account narrative is an abstraction built for internal planning. The specific details are the prospect's lived reality. "The regulatory process and the member experience question" is writing from the narrative. "SB 3175 and the Senate hearings on member impact" is writing from the details. Every time you reach for a general phrase, stop and check whether a specific detail exists that would make the prospect think "this person is actually paying attention to my world." If the detail exists in your research and you didn't use it, the message is weaker than it should be. The Mark Mugiishi HMSA DM (April 2026) is the canonical example: all the details were available (SB 3175, Senate hearings, DOJ April 9 filing, his shift to external stakeholder management, Jenny Smith taking internal ops), but the first draft wrote from the narrative spine ("the member experience question during the regulatory process") instead of from the details. The revision landed because it named the Senate bill, referenced how another CEO structured a specific regulatory argument, and spoke to the political fight Mark is actually in. The details were the difference between a message a CEO deletes and one he responds to.

**The prospect knows their own world.** Never open by narrating their situation back to them. "Your app is 3.2 stars" is narration. "CCN next-gen is about to put cost-per-transaction under a microscope" is an insight they might not have connected yet. The first tells them what they already know. The second gives them something to think about.

**The prospect knows their own expertise.** This is different from knowing their own situation. Situation is "we launched D-SNP last October." Expertise is "I've spent 25 years in payer operations and I can diagram how unabsorbed complexity becomes call volume in my sleep." Never explain a mechanism to someone whose career proves they already understand it. The prospect's career arc (years of experience, previous organizations, functional depth) determines what you can IMPLY versus what you need to SPELL OUT. A 25-year COO who came from L.A. Care and Molina does not need to be told that two benefit sets without digital self-service create calls and grievances. She lived it. A newer director in a specialized function might need more of the mechanism made explicit. Gate 1 must produce a clear answer to: "What does this person already understand because of who they are, that I must NOT explain?" Every sentence that explains something the prospect already understands is a sentence that makes the message longer without making it smarter. The Suma GCHP InMail (April 2026) is the canonical example: the original draft walked a 25-year COO through the mechanism behind "unabsorbed complexity becomes calls." The revision replaced that with "the person who doesn't know which plan covers what," which is the human reality she's watching play out, not the operational abstraction she already owns.

**Verify attribution before you reference it.** If your research surfaced a specific initiative, campaign, program, or public statement, confirm it actually belongs to the prospect's scope of responsibility before weaving it into the message. A campaign launched by a county supervisor is not the same as a campaign launched by the health plan CEO, even if they're in the same department. Referencing someone else's initiative as if it's the prospect's shows sloppy research, not deep research. The specificity that was supposed to build credibility will destroy it. The Irene Lo / Contra Costa InMail (April 2026) is the canonical example: the "Right Care, Right Way" ER diversion campaign was initially referenced as if it were the health plan CEO's initiative. It was actually launched by a county supervisor in collaboration with the fire district and Kaiser. Attributing it to Irene would have told her the sender didn't understand her org structure. The fix was to reference the underlying problem (non-emergency ambulance dispatches among her members) rather than the campaign name, because the problem IS hers even though the campaign isn't.

**The prospect's professional background determines how you deliver insight.** Not all executives evaluate the same way. A clinician-executive (physician, nurse, actuary, engineer) who built their career on evidence wants to see the finding, then decide if the details are worth their time. A relationship-oriented executive (sales leader, marketing VP, BD) can be drawn in by curiosity and pattern teases. Gate 1 must produce a clear answer to: "Does this person evaluate evidence or evaluate relationships?" This determines whether you SHOW the insight in the message body (evidence-oriented) or TEASE it and let curiosity earn the meeting (relationship-oriented). When in doubt, show. Showing always works. Teasing only works for certain personas. The Irene Lo InMail (April 2026) is the canonical example: the first draft teased a pattern ("a few county plans found a surprisingly consistent pattern in what held quality scores"). Irene is a surgeon-turned-CEO, a clinician who evaluates evidence. She would have thought "just tell me the pattern or don't contact me." The revision gave her the finding (outreach moved awareness but didn't change behavior; it dropped when members had somewhere to turn in real time). She gets value from reading. The meeting earns its place because she wants the operational details, not because information is being withheld.

**Classify the forcing function before you write.** Every account has a forcing function that creates urgency. But forcing functions split into two categories, and the category determines whether you can lead with it or must approach it indirectly.

**PROUD forcing functions** are things the prospect would bring up at a conference, mention on LinkedIn, or reference in a board presentation as progress: a new CEO appointment, market expansion, NCQA accreditation, a new product launch, a strategic partnership, a growth milestone, a digital transformation initiative. These are safe to lead with because the prospect is energized by them. "When a health plan creates a Chief Member Experience Officer for the first time" works because Marlen Torres is proud of her new role and the organizational commitment it represents.

**DEFENSIVE forcing functions** are things the prospect would rather not discuss with a stranger: data breaches, lawsuits, settlements, financial losses, DOJ investigations, leadership departures under pressure, failed implementations, bad app ratings publicly visible, member complaints in the news, closed-lost vendor decisions. These are the prospect's wounds. Leading with them makes the message read like an attack dressed up as insight. The prospect's instinct is to delete because you just reminded them of the worst thing that happened to their organization in order to sell them something.

The rule: if the forcing function involves organizational failure, embarrassment, legal exposure, or reputational damage, NEVER lead with the event itself. Instead, lead with the INVESTMENT they made in response, which they ARE proud of. Every defensive forcing function has a proud response behind it. A data breach leads to a security modernization investment. A DOJ settlement leads to a compliance overhaul. A closed-lost deal leads to a strategic re-evaluation. A financial loss leads to an operational efficiency mandate. Lead with the response, not the wound. The prospect will connect the dots without you pouring salt in it.

The Nancy Jenkins McLaren email (April 2026) is the canonical example. The original draft opened with "Two breaches, 2.9 million people affected, and a $14M settlement." Nancy lived it. She doesn't need a stranger recounting her worst year back to her to sell her something. The revision opened with "When a plan invests heavily on the clinical and infrastructure side, there is usually a lag before members notice. Epic, Cerner, HCL, a rebuilt security posture — that is real investment." Same forcing function (the breach created the modernization mandate), but framed through what she's proud of (the investment in response) rather than what she's ashamed of (the breach itself). She's proud of Epic, Cerner, HCL, the rebuilt security. She's not proud of 2.9 million affected people. Start with what she's proud of.

This filter applies at Gate 1 and must produce a clear answer to: "Is the forcing function I'm about to lead with something this prospect would bring up proudly, or something they'd rather not discuss with a stranger?" If it's defensive, identify the proud investment behind it and lead with that instead. The forcing function still powers the urgency of the deal. It just can't power the opening line of the email.

**The prospect is skeptical by default.** They receive hundreds of cold messages. Every one of them claims to have something valuable. Your message earns attention by demonstrating that you understand their world well enough to say something they haven't already heard from their own team.

### Gate 2: The One Idea

Every message has exactly one idea running through it. Not two ideas. Not a setup idea and a payoff idea. One idea, expressed as a flowing thought.

Before writing, state the one idea to yourself in a single sentence. Examples from finalized copy:

- "Commercial payers have already been grinding on the exact numbers the VA is about to get evaluated on, and Chris has been on that side of it." (Ed HES email)
- "Where does the front door still reflect yesterday's assumptions, even after the business has moved on?" (Denise InMail)
- "There's a cutoff point where manual outreach stops driving closure and becomes the expensive option, and finding it makes every downstream decision easier." (Elizabeth email)

If you cannot state the one idea in a single sentence, you don't have a message yet. Stop and think until you do.

**Test the idea:** Does this idea give the prospect something they don't already have? Does it make them reflect on their own situation differently? If not, find a better idea.

### Gate 3: Write It Like You Said It

Write the entire message in one pass as if you're saying it out loud to a peer. Not constructing it. Not assembling it. Saying it.

Rules for this gate:

- **The first sentence does exactly one thing.** It accomplishes one complete thought. Not two things connected by "and." Not a fact followed by a qualifier. One idea, landed fully, in one sentence. Test: describe what the first sentence does. If you need the word "and" to describe it ("it names the data point AND connects it to her members"), the sentence is trying to do too much and will do neither well. The Irene Lo InMail (April 2026) is the canonical example: the first draft opened with "23,000 non-emergency ambulance dispatches last year across Contra Costa, and a good chunk of those are CCHP members." That sentence tries to establish a data point AND connect it to her members, and the second half ("a good chunk of those") is vague and deflating. The revision opened with "Your members accounted for a significant share of the 23,000 non-emergency ambulance dispatches across Contra Costa last year." One sentence, one thought: her members are driving a quantified problem. It starts with "Your members" so she's in the story from the first two words.
- **Write the whole message from the one idea.** Every sentence should feel like it flows naturally from the one before it. If you have to force a transition, the sentences don't belong together.
- **Do not stop to check rules mid-draft.** Write the complete thought first. The rules come at Gate 5.
- **Vary sentence length naturally.** Some short. Some longer and more layered. The rhythm should feel like speech, not like a checklist being executed.
- **Merge consecutive short sentences in the body.** When the draft produces two or three short declarative sentences in a row (e.g., "The DOJ filing went in. One Health is moving. The timeline is real."), merge them with commas, "and", "but", or "because" to create the rhythm of someone actually talking ("The DOJ filing went in April 9, and One Health is moving from theoretical to real."). Staccato chains of short sentences read like bullet points disguised as prose. Real people connect their thoughts when they speak. This rule applies to body paragraphs only — the CTA close intentionally uses short punchy elements (see CTA Discipline below).
- **Use connective tissue.** "The reason that matters," "Here's the thing," "That's usually where," "Once that's clear." These are the phrases that make a message feel like one flowing thought instead of five disconnected observations.
- **Do not over-explain.** If the one idea is clear, the prospect will connect the dots. Trust them. The best copy leaves space for the prospect to fill in their own context. The Elizabeth email doesn't spell out what "the expensive option" costs. It doesn't need to. She knows. The specific test: for every explanatory sentence, ask "does this person already understand this because of who they are?" If Gate 1 mapped their expertise and the answer is yes, cut the sentence. Replace it with the human-level consequence they're watching play out, not the operational abstraction they already own. Writing long because you're explaining a mechanism to an expert is the most common form of over-explanation, and it makes the message feel like a briefing document instead of a peer observation.
- **Never make the sender the subject of a sentence.** The entire message, opening to CTA, keeps the prospect as the central figure. The most common failure mode is the "credential line": a sentence like "I work with payer CX teams navigating that transition" inserted to establish the sender's authority mid-message. This line pattern-matches to every vendor InMail the prospect has ever deleted. It breaks the prospect-first spell because it shifts the story from THEIR world to the sender's resume. If the message needs to establish that the sender has something valuable to offer, do it through the INSIGHT, not through a credential. But there are two levels of insight: showing and teasing. Teasing says "a pattern exists" and withholds it. Showing gives the finding and lets the details earn the meeting. Showing is almost always stronger because the prospect gets value from reading whether or not they reply, and the meeting becomes their idea because they want the operational specifics. A credential tells the prospect WHO you are. A tease tells them you KNOW something. Showing tells them WHAT you know. Prospects respond to what you know. The Irene Lo InMail (April 2026) is the canonical example of showing beating teasing: "I've watched other county plans run similar campaigns and hit the same wall: the outreach moved awareness but didn't actually change behavior. It dropped when members had somewhere to turn in real time, before they dialed 911." landed where the earlier tease version ("A few county plans found a surprisingly consistent pattern in what held quality scores through the contraction") would have been recognized as an information-withholding play and ignored. The first gives the finding. The second holds it hostage. Default to showing. Only tease when Gate 1 identifies the prospect as relationship-oriented (see persona calibration above).
- **Purge rep-language.** Certain words and phrases reveal you're running a sales motion instead of sharing a genuine observation. Common offenders: "plans your size," "companies like yours," "leaders in your space," "I help organizations," "I've been working with," "teams I partner with." These are the phrases that could appear in a BDR playbook template with [COMPANY] or [INDUSTRY] placeholders, and that's exactly how they read to a prospect. Replace with language a peer would use when genuinely thinking about a problem: "the part I keep thinking about," "a handful of," "the pattern I keep seeing," "what I keep coming back to." The test: read the sentence and ask whether it sounds like one person talking to another person about something that interests them, or like a rep categorizing an account. If it's the second, rewrite.
- **Never describe the solution category.** A credential line reveals WHO the sender is. Rep-language reveals the sales MOTION. A product tell reveals WHAT the sender sells. All three break the spell, but the product tell is the subtlest because it hides inside an otherwise insight-driven message. "Digital self-service absorbing the complexity" is a product tell. A COO reads that phrase and immediately knows she's being pitched a digital platform. "The person who doesn't know which plan covers what" is the human reality. It describes the PROBLEM at the human level without describing the solution category. The test: if a prospect could read the sentence and accurately guess what your company sells, it's a product tell. Rewrite using the human consequence instead of the functional description. Never use language that reads like a product capability framed as an observation: "digital self-service," "member engagement platform," "unified benefit navigation," "real-time eligibility layer." These are feature descriptions wearing insight clothing. The Suma GCHP InMail (April 2026) is the canonical example: "if there's no digital self-service absorbing the complexity, it all flows back as calls and grievances" was replaced with "that's where two benefit sets collide with the person who doesn't know which plan covers what." The first tells the prospect what you sell. The second tells the prospect what their members experience. Only one of those earns a meeting.
- **The CTA must be the natural conclusion of the one idea.** If the message is about a cutoff point that makes downstream decisions easier, the CTA is about finding that cutoff point together. If the message is about two people working on the same problem from different systems, the CTA is about whether a conversation is worth it while they're in the same building. The CTA should feel inevitable, not bolted on.

### Gate 4: The Prospect Test

Read the entire message back as the prospect. Not sentence by sentence. The whole thing, start to finish, the way they would read it on their phone between meetings.

Answer these questions honestly:

1. **Would I keep reading after the first sentence?** If the opener narrates my situation back to me, I'm deleting it. If it tells me something I haven't thought about, I'll read the next line.
2. **Do I know why this person is contacting me?** Not "they want a meeting." Why ME, why NOW, about WHAT specifically.
3. **Do I know what I'd get from a meeting?** Not a pitch. Not a demo. Something useful to me whether or not I ever buy anything. Pattern data from peers. A diagnostic I can use internally. A question I should be asking that I'm not.
4. **Can I say yes without feeling like I'm agreeing to a sales pitch?** The CTA should feel like a useful decision for me, not a favor I'm doing for the sender.
5. **Does this message have one clear thought, or does it feel like multiple ideas stitched together?** If I have to re-read to figure out what the point is, it's not ready.
6. **Does any sentence make the sender the subject instead of me?** If there's a line about who the sender is, what they do, or who they work with, the spell breaks. I went from reading about MY world to reading someone's LinkedIn headline. That's the moment I pattern-match this to "vendor outreach" and move on. Every sentence should be about my situation, my tension, or an insight I haven't considered. Zero sentences should be about the sender's qualifications.
7. **Can I guess what this person sells?** If any sentence describes a product category, capability, or solution type clearly enough that I can identify what the sender's company does, I know I'm being pitched. "Digital self-service absorbing the complexity" tells me this person sells a digital member platform. "The person who doesn't know which plan covers what" tells me this person understands my members. The first is a product tell. The second is an insight. A message that passes questions 1-6 can still fail here. The credential trap catches when the SENDER becomes visible. The product tell catches when the PRODUCT becomes visible. Both break the spell equally.
8. **Does any sentence explain something I already know because of who I am?** If I'm a 25-year operations executive and a sentence walks me through a mechanism I could diagram from memory, the message just talked down to me. It told me something my own team tells me every week. That's not an insight. That's a briefing I didn't ask for. Every explanatory sentence must earn its place by telling me something my expertise DOESN'T already cover.
9. **Does this message open by reminding me of something painful that happened to my organization?** If the first paragraph recounts a breach, a lawsuit, a settlement, a financial loss, a failed initiative, or any event I'd rather not discuss with a stranger, the message reads like someone building a case against me to sell me something. My guard goes up immediately. The message should open with what my organization DID about the problem (the investment, the response, the rebuilding), not the problem itself. I'm proud of our response. I'm not proud of what happened. Start with what I'm proud of.

**If any answer is no, go back to Gate 3 and rewrite.** Do not show the user a draft that fails the Prospect Test. This is the single most important gate. Every thread where the user had to redirect came from drafts that would have failed this test if it had been applied honestly.

**The batch generation honesty problem.** When this gate runs inside a roadmap or multi-prospect session, there is a documented tendency to apply it with decreasing rigor as volume increases. Contact 1 gets a genuine simulation. By contact 8, the gate becomes a rubber stamp — "yeah, this feels fine" — because the cognitive cost of genuinely inhabiting each new prospect's perspective accumulates. This is the exact moment the gate matters most. The fix is not "try harder." The fix is: after ALL copy is drafted for the full committee, come back and re-run Gate 4 on every piece of copy with fresh eyes. Read each message as if it's the only one you're evaluating. The holistic roadmap skill enforces this as a separate Step 6 (Prospect Response Simulation) that runs after all copy is complete. But even in standalone copy generation, this gate must be applied with the same honesty you would bring if Dallas were about to ask "would they say yes?" — because he will ask, and the answer has never once been "yes, ship it as-is" when the simulation wasn't genuine.

### Gate 5: Rule Check (Light Touch)

NOW — and only now — check the draft against the Copy Sharpener fundamentals. But check it as a READER, not as an auditor. The question is not "does every sentence satisfy a rule?" The question is "does anything in this message break the spell?"

Quick scan for:
- Forbidden words or phrases (leverage, synergy, etc.)
- Em dashes (replace with periods, commas, colons)
- League mentioned in Days 1-5
- Sign-off correct (first name only for Days 1-5, full name for Days 6+)
- Word count within range for the channel
- CTA ends on a question, not a statement
- Vague metaphors and AI-default phrases (see below)

**The AI-ism filter.** AI-generated copy has a tell beyond forbidden words and em dashes: vague metaphorical language that sounds like it means something but actually says nothing. These phrases survive every other gate because they're not technically wrong. They're just empty. Common offenders: "gets heavier," "on the horizon," "looming large," "at the forefront," "navigate the landscape," "in an era of," "the weight of," "carries significant implications," "sends a clear signal," "positions them well," "a critical juncture," "the stakes are high." The test: can you replace the phrase with a specific, concrete statement that says what you actually mean? If yes, always use the specific version. "That cost line gets heavier as the contraction hits" means "that's an expensive problem to carry into a $330M revenue contraction." The second version says the actual thing. The first version uses a metaphor to avoid saying it. Real people in professional contexts say the actual thing. AI defaults to the metaphor. The Irene Lo InMail (April 2026) is the canonical example: "gets heavier" was flagged by Dallas as "wtf does that even mean really" and replaced with the specific financial reality. Every vague metaphor is a missed opportunity to say something concrete that demonstrates you understand the prospect's actual numbers.

If the message passes Gates 1-4 and reads like a real person with a clear thought, do NOT rewrite sentences to better satisfy individual rules. The fluidity of the whole message is more important than any single rule. The Copy Sharpener rules are guardrails, not a construction manual. Use them to catch real problems, not to optimize individual lines.

**What "breaking the spell" means:** If a prospect is reading a message that flows naturally and then hits a word like "synergy" or an em dash that screams AI, the spell breaks. That's what Gate 5 catches. It does NOT mean rewriting a perfectly natural sentence because it doesn't explicitly map to a Tenbit++ component.

### Voice Note TL;DL Rule

When drafting a voice note script, also draft the accompanying TL;DL (too long; didn't listen) — a 2-3 sentence written summary sent alongside the audio. The TL;DL goes through the same five-gate sequence as any other written copy. It should capture the one idea and the CTA in text form. Think of it as a standalone micro-message that works even if the prospect never plays the voice note. Sending both is getting significantly more replies than voice note alone.

## The CTA Discipline

CTAs have been the single biggest failure point across all threads. Here is what keeps going wrong and how to prevent it.

### Failure Pattern 1: The Vague Ask
"Worth a conversation at Dana Point?" — About what? Why would I block 20 minutes for a topic I can't identify?

**Fix:** The CTA must tell the prospect what the meeting is ABOUT. Not by promising specific deliverables (which pins the presenter to something they may not be able to deliver), but by naming the topic or question the conversation would address.

### Failure Pattern 2: The Over-Promise
"With the data behind those three numbers" — Now Chris is committed to showing up with specific data he may not have. If the meeting doesn't deliver exactly that, trust is broken on the first interaction.

**Fix:** Frame what the meeting offers in terms of the CONVERSATION, not deliverables. "He's been on the commercial payer side of those numbers" is what Chris can truthfully say. "With the data behind those numbers" is a promise.

### Failure Pattern 3: The Disconnected CTA
The email body earns the right to ask. Then the CTA asks about something different, or asks so generically that the body's work is wasted.

**Fix:** The CTA must be the natural conclusion of the one idea from Gate 2. If the body is about a structural ceiling in outreach models, the CTA is about finding whether that ceiling exists in their world. If the body is about two systems grinding on the same numbers, the CTA is about whether a conversation between those two sides is worth having. The CTA should feel inevitable after reading the body.

### Failure Pattern 4: The Meeting-As-Favor
"Open to scheduling a brief chat with him?" — I'm being asked to do something for the sender. The meeting should feel like something I'M getting, not something I'm giving.

**Fix:** Frame the CTA so the prospect is the one who benefits. "Worth finding 20 minutes onsite to see whether that question is relevant on your side?" puts the value on HER side. She's finding out something useful, not granting an audience.

### Failure Pattern 5: The Credential Bridge
"I work with [type] teams navigating [problem]." The message was about MY world until this sentence, and now it's about the sender. I know I'm being prospected. The sender needed to bridge from the body to the CTA and defaulted to a credential instead of an insight.

This is the most insidious failure pattern because it feels necessary. The logic goes: "I've described the prospect's tension, now I need to establish why they should talk to ME specifically." That logic is correct. The execution is wrong. A credential establishes authority by telling. An insight establishes authority by showing.

**Fix:** If the CTA needs a bridge between the body and the ask, give the insight in the body and let the CTA offer the operational details. Do not tease. Do not withhold. The prospect should get genuine value from reading the message whether or not they reply. The meeting earns its place because they want the specifics, not because you're holding information hostage. Compare these three approaches for the same message:

- Credential: "I work with payer CX teams navigating that exact inflection point. Worth a quick conversation about what they did differently?"
- Tease: "A handful of community-based plans have navigated that without losing the human feel. The pattern is surprisingly consistent. Worth a quick conversation about what they actually did differently?"
- Show: "I've watched other county plans run similar campaigns and hit the same wall: the outreach moved awareness but didn't actually change behavior. It dropped when members had somewhere to turn in real time, before they dialed 911. Worth 15 minutes to walk through what two similar plans did differently?"

The credential makes the sender the subject. The tease keeps the story about the prospect's problem but withholds the actual finding, which smart executives recognize as an information-asymmetry sales tactic ("just tell me or don't"). The show gives the finding (education alone doesn't change behavior; real-time access does) and lets the CTA offer the implementation details. The prospect got value from reading. Now they want to know HOW those plans did it. That curiosity earns the meeting honestly.

Default to showing. The only time a tease is appropriate is when Gate 1 identifies the prospect as relationship-oriented (see persona calibration in Gate 1). Evidence-oriented prospects (clinicians, actuaries, engineers, operations executives) will recognize withholding and resent it.

### The Three-Beat Day 1 Close

Day 1 cold emails use a specific CTA structure that is intentionally punchy and separate from the flowing body prose. This is NOT a contradiction of the body fluidity rule — the CTA close earns its punch by contrasting with the smooth body above it.

**Structure:**
1. **Proof point sentence**: One short sentence about a peer or comparable plan. "A COO at a comparable plan used the review period to get ahead of exactly this."
2. **Value statement**: One standalone sentence starting with "Might be helpful/useful/valuable to walk you through..." that bridges to a meeting. "Might be helpful to walk you through how she structured the operational readiness timeline."
3. **Time ask** (separated by a blank line): "Worth 15 min in the next few weeks?" as its own line.
4. **Sign-off** (separated by a blank line): "Dallas"

The Rick Hopfer HMSA Day 1 email is the gold standard for this structure. The three beats create a descending rhythm: context → offer → ask. Merging these into one flowing sentence kills the punch. Each element earns its own breath.

**Time anchor calibration:** "in the next few weeks" or "in the next couple weeks" for VPs, SVPs, and C-suite. "this week or next" only for directors and mid-level contacts. Cold outreach to senior executives with tight time anchors signals desperation.

## What This Skill Does NOT Do

- It does not replace the Copy Sharpener. The Sharpener is still the post-production quality gate. This skill produces the draft that the Sharpener then verifies.
- It does not contain formatting rules, word count limits, or channel-specific mechanics. Those live in the Copy Sharpener.
- It does not handle sequencing, day-by-day scheduling, or touchpoint planning. That's the Execution Roadmap.
- It does not generate cold call scripts or voicemail scripts. That's the Cold Call Playbook. (It DOES generate voice note TL;DL summaries, since those are written copy.)
- It does not conduct research or build strike packets. Those are upstream skills.

This skill does ONE thing: it ensures that the first draft of any written outreach (emails, LinkedIn, DMs, follow-ups) sounds like a real person wrote it in one sitting with one clear idea, and that it would survive being read by a skeptical executive scanning their inbox on a Tuesday morning.

## Process for Multi-Message Output

When generating copy for multiple prospects in one session (e.g., an execution roadmap with 5+ personas):

1. Run Gates 1-2 for EACH prospect individually before writing anything. Each person gets their own one idea. If two prospects end up with the same one idea, one of them is wrong.
2. Write each message independently through Gates 3-5. Do not batch-write by applying the same template across prospects.
3. After all messages are written, read them back-to-back and verify they sound like different messages written to different people, not the same structure with nouns swapped.

## Interaction with Copy Sharpener

The intended workflow when both skills are active:

1. **First Draft Engine (this skill):** Gates 1-4 produce a draft. Gate 5 does a light rule check.
2. **Copy Sharpener:** Runs the full 20-point send-ready test and flags anything that needs fixing.
3. **Resolution:** If the Sharpener flags a rule violation but the message reads naturally and passes the Prospect Test, the message wins. If the Sharpener flags something that genuinely breaks the spell (forbidden word, wrong sign-off, League mentioned in Days 1-5), fix it without disrupting the flow.

The Sharpener should NEVER be used as the starting point for writing. It is a verification layer, not a construction tool.

## Canon Constraints (Inherited)

- Tenbit++ (Observation, Insight, Value, Next Step) is a useful diagnostic for whether a message has all its pieces, but it is NOT a template. A good message may weave these elements together in a way that doesn't map cleanly to four labeled boxes. Check for completeness, not structure.
- Pincer Rule: VPs and Directors hear Operational Relief, never Brand Vision. This affects the one idea at Gate 2.
- Brand-Light Days 1-5: No League mentions. This is a Gate 5 catch.
- All linguistic guardrails from the Copy Sharpener apply at Gate 5.

## Output

This skill does not produce a separate file. It governs the PROCESS by which outreach copy is drafted inside any other skill's output (execution roadmaps, pipeline phases, one-off email requests). The output is the draft itself, delivered in whatever format the requesting skill or the user expects.

When the user asks for copy directly (not as part of a roadmap), deliver:
- The message, ready to send
- One sentence explaining the one idea behind it (so the user can evaluate whether the idea is right before evaluating the words)
- Nothing else unless the user asks for it

Do not deliver changelogs, Tenbit++ breakdowns, or rule-by-rule analysis unless the user specifically requests them. The message should speak for itself.
