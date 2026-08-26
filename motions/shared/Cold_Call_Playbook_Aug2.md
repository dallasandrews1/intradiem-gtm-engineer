# Cold Call Playbook (shared, Aug 2 2026)

Canonical live-call direction for every motion's Daily Action Brief. Listed in `automation/config/action_brief.json` under every brief's `playbook_sources`. The brief composer reads this file for call STRUCTURE and for the universal branch handles below; motion-specific objection handles stay in each motion's own playbook doc. This doc adds ZERO new prospect-facing claims: every fact in a rendered script still comes only from the lead's variables or the motion's playbook sources.

**Evidence base (internal direction only, research-sourced, not Intradiem-verified, never quoted to a prospect):** analysis of large call corpora (Gong Labs and 2025 dial-level studies) finds availability yes/no openers ("did I catch you at a bad time", "is now an OK moment") book roughly 40% BELOW baseline, while asking for about 30 seconds with the prospect explicitly in control books at ~11% against a ~2% average; proactively stating the reason for the call roughly doubles success; booked cold calls run nearly twice as long as failed ones and contain real back-and-forth, not a monologue that ends in a meeting ask. Those four findings are the spine of everything below.

---

## The opener skeleton (every dial, both reps)

Four beats, in order, 10 to 12 seconds total, then stop talking:

1. **Their name, then a beat of silence.** "John." Pause. The pause is the pattern interrupt; don't rush past it.
2. **Who you are.** "It's Jack Ohagan at Intradiem." First and last name, company named once. Never "This is X speaking."
3. **The reason for the call, one sentence, carrying the lead's specific hook.** Built from the lead's `vm_hook` material: their number, their seam, their morning after. "I'm calling about the morning after a disrupted day, and what it costs a service team once a delay crosses the three hour mark." If a true familiarity anchor exists, it goes here in half a sentence first ("we connected on LinkedIn this week", "I sent you a note on X"), but the reason still lands in the same breath; the email reference alone is never the reason, most prospects never saw the email.
4. **The 30-second contract, prospect in control.** UK register (Jack): "Have you got 30 seconds, and you can tell me if it's not relevant?" US register (Nate): "Can I take 30 seconds, and you tell me if it's not for you?"

**Banned opener family (hard rule, named defect class):** any availability yes/no that hands the prospect an exit before the reason lands. "Did I catch you at a bad time?", "Did I catch you at an OK moment?", "Is now a good time?", and "Did I catch you with 30 seconds?" all belong to it. The difference between the banned form and beat 4 is order and control: the contract comes AFTER the reason, asks FOR a slice of time, and makes ending the call the prospect's explicit right. That's what earns the trust the yes/no version begs for.

Honesty is allowed and works: "We haven't spoken before, so I'll be quick" is a legitimate beat-3 lead-in when there's no anchor.

## The flow after the opener

- **If they engage:** the 20 to 30 second expansion of the one insight, then it MUST end on a check question that hands them the floor: "Does that match what you see on your side?", "Is that anywhere near how it plays out at {{company}}?" Never expansion straight into the meeting ask; let them talk, then respond to what they actually said. The insight is given away in full on the call, meeting or not; the value is the point, the meeting is the consequence.
- **The ask:** house natural CTA form, and it names what they get in the 15 minutes ("I'll walk you through which contracts sit closest to the line", "what those days actually cost at {{company}}"). An honest-exit clause is encouraged where it fits the moment: "if it turns out that's already handled, I'll say so and leave you alone."
- **On a yes: lock the slot on the call.** Offer two concrete options ("tomorrow morning or Thursday, what suits?"). Never end a yes with "I'll send some times over."

## Universal branch handles (both reps, spoken form; motion facts filled from the lead's variables, never invented)

**"I'm busy / in the middle of something."**
Shape: full respect, a ten-second version of the reason so the call wasn't noise, then trade up to a real slot. "Completely get it. Ten seconds so you know what this was: [one-line reason from the lead's hook]. When's better this week for a proper 15 minutes?"

**Brush-off ("not interested", "we're fine").**
Shape: accept it immediately, no second pitch. One calibrated either/or question, then release warmly. "Fair enough, I won't push. One thing before I go, is that because [the specific problem] is already handled, or just not the priority right now?" Whatever they answer: "Either way, appreciate you being straight with me. I'll leave you be." HARD STOP: after their answer, the release line is the end of the call. Never a second pitch, never "the reason I ask", no matter what they say. Their answer goes into the DONE/SKIP thread reply as intel; it gets logged, not worked.

**"Just send me an email."**
Shape: agree, then one qualifying question so the email can actually be useful, then a conditional ask. "Will do, and I'll keep it short. So I send the one page that's useful and not a brochure: [one qualifying question about their situation]. I'll get it to you today, and if it lands, worth 15 minutes to walk it through?"

**"What's this about?" (guarded or gatekept).**
Shape: the plain reason, one sentence, zero seller-speak, then re-offer the 30-second contract. Never a feature pitch, never "just following up".

## Delivery cues (rendered once per Calls block, not per call)

Slower than feels natural. Pause a beat after their name. Let the ask sit in silence; the first one to speak after the ask should be them. Know the shapes, don't read the words; the script is a map, not a teleprompter.

## Voicemail (unchanged, restated)

Voicemail is an email amplifier, not a callback play. Under 30 seconds, rep's name up front, the note's hook restated in one sentence, both doors left open ("I'm on [your number], or just reply to the email"), warm sign-off with their name. No asks beyond that.

## Composition constraints (for the unattended brief composer)

- Openers are ASSEMBLED from the skeleton plus the lead's real variables (vm_hook material, true anchors). Never add a number, name, or fact that isn't in the lead's variables or the motion's playbook sources.
- Branch handles render from this doc's shapes with the motion slot filled from the lead's variables; motion-specific objections (October ratings, WFM, claims providers) come only from that motion's own playbook doc.
- Segment labels and order per the format spec: Opener / If they engage / The ask / If they're busy / If they brush you off / If pushback: "<objection>" / No answer: voicemail. Busy and brush-off render on dial tasks; omit on voicemail-only tasks.
- BRANCH CAP (the map stays glanceable): a dial task renders at most seven labeled blocks and at most two If-pushback blocks, chosen by relevance to this lead. The motion doc always carries the full handle set; a rep mid-call reads a map, not a manual. This cap is a relevance rule, not a size rule; it never trims the wording of any block that renders.
- OPENER FACT CHECK (live runs, where openers are composed rather than staged): before a composed dial script ships, every number, name, and fact in its opener must trace to the lead's stored variables or this brief's playbook sources. Anything untraceable means recompose without it, or fall back to "copy is loaded in the Lemlist task". The run writes one OPENER-CHECK line per composed dial script to the log (lead, facts used, which variable each came from) so the first-live-brief eyeball takes one minute.
- Everything passes the SPOKEN VOICE bar in the format spec. Contractions always, no em dashes, warm never curt.
