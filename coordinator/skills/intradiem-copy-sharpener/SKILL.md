---
name: intradiem-copy-sharpener
description: "Intradiem outreach copy quality gate. Takes drafted messaging and sharpens every word to send-ready C-suite quality. Applies CTA Philosophy (prospect is hero, feel not tell, meeting is their idea) plus 9 rules (So What Chain, Tenbit++ Framework, Length/Front-Loading, Brand-Light, Forcing Function Specificity, CTA Construction/Escalation, Persona/Tone, Linguistic Guardrails, Send-Ready Test) and a hard verified-claims gate against the Intradiem Value Repository. Runs AFTER intradiem-first-draft-engine. Trigger on any request to sharpen, review, or finalize Intradiem outreach copy: emails, LinkedIn, voice scripts, call scripts, Clay message variants. Returns sharpened copy plus CHANGES LOG."
---

## When this skill applies

- Run AFTER intradiem-first-draft-engine has produced the draft. That skill is the pre-production thinking framework; this one is the post-production quality gate. Never use the Sharpener as the starting point for writing. If the First Draft Engine has not loaded, load it first.
- Run on every piece of outreach copy before it is sent, loaded into a sequencer, or seeded into the Clay Message Gen table
- Run on Clay-generated message variants before any batch send is approved
- Run before anything enters the conductor's approval queue

## Critical context

This skill is a VERIFICATION layer, not a CONSTRUCTION tool. If the Sharpener flags a rule violation but the message reads naturally and passes the Prospect Test, the message wins. If it flags something that genuinely breaks the spell (forbidden word, wrong sign-off, Intradiem named in Days 1-5, an unverified stat), fix it without disrupting the flow. Fluidity of the whole message beats any single rule.

## Who signs (Intradiem-specific)

Dallas engineers the copy; a rep sends it. Confirm the sender per motion (Star Ratings default: Nathan Belfield). Sign-off is the SENDER's first name Days 1-5 and full name Day 6+. Never "Dallas Andrews, Intradiem" or "Nathan Belfield | Intradiem" in any email signature.

## Scope reminder

Dynamic Workforce Orchestration across contact centers AND back offices, six verticals. Copy that reads "call-center tool" fails the gate. Verint, NICE, and Calabrio are the layer we act within, never rivals to trash.

## CTA Philosophy (North Star)

Every piece of outreach exists to make the prospect reflect on THEIR problem and want to solve it badly enough to talk to someone. These principles override every other CTA rule on conflict.

- **Prospect is the hero.** Never the sender, never Intradiem, never the solution.
- **Feel, not tell.** Describe the situation so vividly they self-select into it. Never declare their responsibilities to them ("you own the gap...").
- **Self-selection pattern.** WRONG: "You own the last few Stars points." RIGHT: "For plans sitting this close to the line, the call center measures are often where the last few points come from."
- **Meeting is their idea.** The message creates the tension; the prospect resolves it by wanting to talk.
- **CTA connects the dots.** If the CTA does not make the meeting feel like it solves THEIR problem, the message failed regardless of the body.

## The 9 Rules

### Rule 1: So What Chain
Read each sentence. Ask: so what, does the reader care? Delete anything that does not answer "why should I care?" ("We're excited to connect", "Our platform is innovative", "We help companies optimize their workforce" all die here.)

### Rule 2: Tenbit++ Framework Check
Observation (specific to them) → Insight (what it means) → Value (why it matters to them) → Next Step (the ask). A diagnostic for completeness, not a template; a good message weaves these without labeled boxes. Strengthen missing elements, delete sentences that map to none.

### Rule 3: Length and Front-Loading
- Cold Email 1: 80-120 words max
- Cold Email 2+: 120-150 words max
- LinkedIn InMail: 50-80 words
- LinkedIn DM: 50-100 words
- Voice note: under 45 seconds (~100-125 words) + mandatory 2-3 sentence TL;DL text
- Voicemail: under 25 seconds (~50-60 words)
- Cold call opening: under 45 seconds (~100 words)

Front-load: the first 1-2 sentences carry the most compelling insight. Count words. Cut ruthlessly.

### Rule 4: Brand-Light Execution (Days 1-5)
Days 1-5: do NOT name Intradiem anywhere: subject lines, bodies, LinkedIn notes, scripts, signatures. Frame around the problem, never the product category (see product-tell rule). Intradiem can appear from Day 6, sparingly, only where it adds credibility. Sign-off: sender's first name Days 1-5, full name Day 6+.

### Rule 5: Forcing Function Specificity
The opening references a specific, data-backed forcing function. VAGUE: "I saw you run a large contact center." SPECIFIC: "Your weighted average looks to be right around 3.91, just under the 4.0 line." For every computed Stars number, the humility clause rides along ("you will know the exact picture far better than I do"). Defensive forcing functions (downgrades, outages, misses) are never the opening; lead with the proud response behind them.

### Rule 6: CTA Construction and Escalation
- **Connector sentence required** before every CTA: one line linking their role/pain to why THIS meeting matters to THEM.
- **Every CTA specifies WHAT the meeting is about.** WRONG: "Worth 15 minutes?" RIGHT: "Worth 15 minutes to hear how you're approaching your cliff-edge contracts?"
- **One question, one ask.** Never stack questions.
- Emails specify what the 15 minutes is for; short DMs may close with "Worth a quick conversation?" since context sits directly above.
- **Seniority timing:** Directors: "early next week" is fine. VP and above: "in the next couple weeks." Tight anchors on senior cold outreach signal desperation.
- **Escalation:** Email 1 soft → Email 2 stronger → Email 3 direct with deliverable → Email 4 formal → Email 5 confident close ("This is worth your time. I'm here whenever the timing lines up."). Week 2 moves to phone/voice.
- **Day 1 Three-Beat Close (required on first cold emails):** (1) short peer proof-point sentence [verified claims only], (2) standalone "Might be helpful to walk you through..." sentence, (3) blank line + "Worth 15 min in the next few weeks?" on its own line, (4) blank line + sender first name. Do not merge the beats.
- NEVER end on a statement. NEVER command ("Let me send over times"). NEVER hedge ("if at all," "I can walk through what I found").

### Rule 7: Persona and Tone Matching
- **CFO / VP Finance:** metrics, payback, cost per contact, capacity without headcount. No adjectives.
- **COO / SVP Operations:** operational relief, never brand vision. Imply mechanisms; a career operator already owns them.
- **VP Customer Care / Contact Center:** AHT, adherence, shrinkage, attrition, coaching time. Must beat what her own WFM reporting tells her.
- **VP Back Office / Shared Services / Claims Ops:** backlog, cost-per-transaction, overtime, zero real-time visibility today.
- **VP/SVP Stars / Quality / Medicare:** measure math, cut points, the 2028 window, payment-year consequences. Evidence evaluator; never lecture on how Stars works.
- **CIO / CTO:** integration surface, security posture, sits-on-top-of-the-stack. Third-party validation over claims.

Check every sentence against the persona's values and vocabulary.

### Rule 8: Linguistic Guardrails
- FORBIDDEN WORDS: leverage, synergy, cutting-edge, best-in-class, empower, seamless, robust, transform, transformation, catalyst, paradigm, innovative, comprehensive
- No vague language: "exciting," "great," "amazing," "powerful"
- No qualifiers: "I think," "hopefully," "I believe"
- No defensive openers: "I know you're busy"
- No clichés: "circle back," "touch base," "reach out," "at the end of the day"
- NO EM DASHES in prospect-facing copy (AI giveaway). Periods, commas, colons, semicolons.
- No engagement-tracking references (opens, clicks) in prospect copy, ever.
- No specific implementation timelines unless verified. "Weeks, not quarters."
- No product tells: "real-time workforce automation," "intraday management," "orchestration platform" and kin reveal the pitch. Describe the human reality instead.
- No robotic, staccato bodies: merge consecutive short declaratives with commas, "and", "but", "because". (The three-beat close is the intentional exception.)
- No "Result:" transitions or formulaic scaffolding.
- Subject lines: short, lowercase, conversational.

### Rule 9: Send-Ready Test (22 points)
- [ ] Starts with a specific observation, not a greeting
- [ ] Forcing function is data-backed
- [ ] Answers "so what"
- [ ] Tenbit++ complete (woven, not boxed)
- [ ] Under word count for the channel
- [ ] First sentence hooks
- [ ] CTA matches sequence position
- [ ] CTA has a connector sentence
- [ ] CTA specifies what the meeting is about
- [ ] Exactly one question in the CTA
- [ ] Prospect is the hero (never told what their job is)
- [ ] Feel-not-tell / self-selection holds
- [ ] Persona tone matched
- [ ] Zero forbidden words, zero vague language
- [ ] Brand-light: Intradiem absent from Days 1-5 copy including signature
- [ ] Sign-off is sender first name (D1-5) or full name (D6+)
- [ ] Zero em dashes
- [ ] Zero product tells
- [ ] Stars copy carries the humility clause where a computed number appears
- [ ] **Every stat/outcome verified against the Value Repository (intradiem-verified-metrics), or marked [UNVERIFIED] and pulled**
- [ ] Sounds like a peer, not a salesperson
- [ ] Body flows; no staccato chains

## Verified-Claims Gate (hard stop, Intradiem-specific)

Before returning ANY sharpened copy:

1. List every number, customer outcome, and peer claim in the draft.
2. Check each against the intradiem-verified-metrics skill / Intradiem Value Repository. Never trust memory; always check.
3. Figures originating from `roi_model.json`, `proof.json`, engine outputs, or seeded dashboards are placeholders. They NEVER appear in prospect copy as fact.
4. Anything unconfirmed: rewrite without it, or mark [UNVERIFIED] and flag for approval. Silent inclusion is the one unforgivable failure; regulated buyers and one bad stat kill the whole engine's credibility.

## Spoken-Word Standards

**Cold call scripts:** max 45 seconds. Opening (8-10s, name + one credible sentence), Hook (15-20s, specific observation about THEIR business), Bridge (10-15s, verified peer result), assumptive CTA (5-10s). Never open with "I know you're busy," the company name, or "Do you have a minute?" Include objection handlers for "Who is this?", "Not a good time," "Send me an email," "We already have WFM / we built RPA in-house."

**Voice notes:** under 45 seconds. First and last name, no title, no company. One verifiable reference to their business, one pattern insight, soft next step. Always ship with the TL;DL text.

**Voicemail:** under 25 seconds. Name, one sentence of context, callback reason. No pitch.

**Video (Vidyard-style):** under 3 minutes, their public data on screen, 2-3 specific friction points, one anonymous verified peer outcome, soft CTA. Never a product demo.

**Multi-persona batches:** every script in the same account references a DIFFERENT forcing function, uses that persona's vocabulary, opens differently, and varies CTA framing. No two scripts in a playbook open the same way.

**LinkedIn touch logic:** pending connection = InMail (include a DM version underneath). Fresh connection (24-48h) = short text DM, voice note saved for Day 4+ escalation. Long-standing connection = voice note DM + TL;DL. Connection requests always go blank. LinkedIn disabled = voicemail instead.

**Default timeline:** Day 1 blitz (all first emails same day), follow-ups cascade Day 2+, pincer starts Day 4-5, compress to ~7 days.

## Copy Quality Gate (before saving any output)

Re-read every piece and verify: no forbidden words or canned phrases; word counts in spec; CTAs match escalation position; no Intradiem mentions in Days 1-5 including signatures; no two scripts open the same way; every CTA has a connector and names the topic; prospect is the hero; zero em dashes; correct sender sign-off; no stacked questions; every voice note has a TL;DL; bodies flow; Day 1 emails use the three-beat close; every claim passed the verified-claims gate. Anything failing gets rewritten inline before saving.

## Output

Save as: `[Account]_Copy_Sharpener_[Channel].md`

Sections: session header (date, channel, recipient, sender, sequence position, goal) → Original Draft → Send-Ready Test results (PASS/FAIL) → Sharpened Copy → Changes Log (original / sharpened / rule / rationale per change) → Word Count Analysis → Persona Tone Check → Tenbit++ Verification → Verified-Claims Ledger (each claim + Repository status) → Final Recommendation (1-2 sentences).

## Worked example (Star Ratings, cold email 1)

**Original draft:**
"Hi Kristen, I hope this finds you well. I'm reaching out from Intradiem, the leader in real-time workforce automation. We help health plans transform their contact center operations with our innovative platform. Given your Stars challenges, I think we could really help. Would you be interested in a call?"

**Issues:** greeting filler; names Intradiem on Day 1; product tells ("real-time workforce automation," "platform"); forbidden words (transform, innovative); "Stars challenges" is a defensive wound framing with no data; weak yes/no CTA; sender unclear.

**Sharpened (sender: Nathan, Day 1):**
"Kristen, your weighted average looks to be right around 3.91, just under the 4.0 line, though you will know the exact picture far better than I do. For plans sitting this close, the call center measures are often where the last few points come from, and those are the first ones to come out of the ratings under the 2028 window. A quality VP at a comparable plan used exactly that window to get ahead of her cliff-edge contracts.

Might be helpful to walk you through how she sequenced it.

Worth 15 min in the next few weeks?

Nathan"

**Why it passes:** specific computed observation + humility clause; window insight she may not have connected; no company name, no product tell; verified peer reference only if the Repository confirms one (otherwise the proof-point beat is rewritten or dropped); three-beat close; one question; sender first name.
