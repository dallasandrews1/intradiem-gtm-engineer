---
name: intradiem-objection-handler
description: "Objection handler for Intradiem outbound and mid-funnel replies. Triggers when a prospect replies with pushback. Diagnoses the category (Bad Timing, We Have WFM, Built In-House RPA, Evaluating Competitor, No Budget, Send Info, Wait for October Ratings) and applies the Reframe Framework (Acknowledge → Insight Pivot → Soft CTA) in a calm, peer-level 3-4 sentence response drafted in the sending rep's voice. Trigger on: prospect pushed back, they said no, objection reply, they're evaluating someone else, they said send info, they have Verint or NICE already, they built it in-house, how do I respond to this reply. Load proactively whenever a prospect reply lands from any motion."
---

## When this skill applies

- Any prospect pushback or declined meeting from the Star Ratings or back-office motions
- Any mid-funnel stall
- When Nate or another rep forwards a reply asking how to respond
- Every response drafts in the SENDING rep's voice and signs with their name

## Background

Replies are where the meetings mandate actually lives. The engine sources conversations; the reframe keeps them alive. Never defend, never over-explain. Acknowledge, pivot with one insight, close soft. Response is always shorter than the objection.

## Objection categories

**1. Bad Timing** ("not now," "revisit in Q4," "peak season")
Root cause: real interest, constrained bandwidth. Strategy: honor the timing, set an explicit re-engagement date, note that the forcing-function window (Stars measurement year, launch date) keeps moving regardless.

**2. We Already Have WFM** ("we have Verint/NICE/Calabrio," "our WFM covers this")
Root cause: category confusion; they think we compete with their scheduler. Strategy: the sits-on-top reframe. Their WFM plans the day; the gap is what happens inside the day when reality diverges from the plan. A strong WFM investment makes the conversation MORE relevant, not less. Never disparage the WFM vendor; it is the layer we act within.

**3. Built In-House RPA / Scripts** ("our team automated this," "we have bots")
Root cause: capable ops/IT team, vendor fatigue. Strategy: acknowledge the capability sincerely. Reframe: rules that fire off real-time ACD/WFM state across the whole intraday surface are a different animal from scheduled scripts; the question is maintenance load and coverage, not whether their team is smart. Offer the trade-off conversation, not a takedown.

**4. Evaluating Competitor** ("we're looking at [vendor]," "already in a pilot")
Root cause: active eval, late timing. Strategy: never badmouth. Position as alternative or complement, ask about their success criteria, and load intradiem-competitive-intel for the wedge brief. Light touch, re-engage in 30 days.

**5. No Budget** ("budget's allocated," "CFO said no")
Root cause: unallocated budget or unconvinced economic buyer. Strategy: pivot from new spend to found capacity: the value comes out of time already paid for (idle time, shrinkage, backlog overtime), which is cost avoidance, not a new line item. Ask about the reforecast cycle. Only cite specific figures that pass the verified-claims gate; otherwise speak in mechanisms.

**6. Send Info** ("just send me something")
Root cause: low priority or genuinely busy. Strategy: send the one-pager (never the deck), name the 5-day follow-up, offer the 15 minutes as the faster path. If the motion has an interactive artifact (calculator, walkthrough page), send that instead of a PDF; it performs the demo without a meeting.

**7. Wait for October** (Stars-specific: "let's see the new ratings first")
Root cause: reasonable-sounding delay that costs a measurement year. Strategy: acknowledge the logic, then the window insight: the measures that move ratings are being lived RIGHT NOW, in this measurement year; October only reports what already happened. Waiting to see the score means booking this year's performance as-is. Humility clause applies to any computed number.

## Reframe Framework

1. **Acknowledge** (1 sentence): validate without defending. Never "I understand" or "I hear you."
2. **Insight Pivot** (1-2 sentences): one new insight that reframes, aimed at operational relief. Peer observation, never rebuttal.
3. **Soft CTA** (1 sentence): easy to accept, names the topic, no yes/no rejectable framing, calibrated to seniority.

## Response rules

- 3-4 sentences maximum, always shorter than the objection
- Sending rep's voice and name; brand-light rules still apply if within Days 1-5
- No forbidden words, no em dashes, no defensiveness, no over-explanation
- Anticipate the deeper objection beneath the surface one and address it with the insight, not with more words
- Every claim passes the verified-claims gate or ships as mechanism language
- Competitor named → also produce the intradiem-competitive-intel wedge brief for the rep's back pocket
- Route final copy through intradiem-copy-sharpener before send

## Output

Save as: `[Account]_Objection_Response.md`

Sections: objection captured (exact quote, source, who) → category + root cause + risk level → reframe analysis (acknowledge / insight pivot / deeper objection) → draft response email (subject that references their concern, body, rep sign-off) → follow-up strategy (category-specific cadence with dates) → deal health note (1-2 sentences).

## Example (We Already Have WFM)

**Objection:** "We just rolled out NICE WFM last year, we're covered."
**Response (rep's voice):** "That rollout is exactly why this is worth a look now rather than later. WFM builds the plan for the day; the expensive part is what happens inside the day when volume, absence, and handle times drift off that plan, and that drift is invisible in the schedule itself. Worth 15 minutes to hear how teams running NICE handle the intraday gap?"

## Example (Wait for October, Stars)

**Objection:** "Let's reconnect after the October release drops."
**Response:** "That's the natural checkpoint, and I'd want to see the new numbers too. The catch is that October reports a measurement year that's already being lived right now, so the score you'll see is largely booked by the time it publishes. If the call center measures are where your last points are, the window to move them is the current year, not the release. Worth 15 minutes before peak season planning locks?"
