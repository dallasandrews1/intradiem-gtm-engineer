# Cost-Mandate Wave 1 — Persona Sequences (Draft-ready)

**Motion:** `cost_mandate_xvert` · **Sender:** the assigned rep (not Dallas) · **Status:** campaign-step templates, Draft only; launch gated on warm mailbox + rep review + `msg1_critic` PASS. Sender webhook OFF.

Two lanes, mirroring the Stars Wave 1 standard: **Lane 1 cost_finance** (CFO / VP Finance / COO / SVP Ops, the cost owner) and **Lane 2 cost_ops** (contact-center / back-office / shared-services operations). Five-touch multi-channel cadence over ~9 business days, merge-field driven so MessageGen personalizes Touch 1 per lead. Staggered committee entry: **cost_finance enters Day 1; cost_ops enters 1-2 days behind.** Never both lanes at one account on the same day.

**Merge fields:** `{{first_name}}`, `{{company}}`, `{{their_figure}}` (the prospect's OWN disclosed figure + attribution — from disclosed_figure/signal_evidence; if empty, the no-number lines below), `{{mandate_event}}` (plain-language fired signal: "the cost program you announced in June" / "the June restructuring" / "the hiring freeze"), `{{workforce_size}}`, `{{sender}}`.

**Claims discipline (hard):** every number is the prospect's own, attributed and dated. No Intradiem ROI, savings, recovered-capacity, or idle-% figure in any touch. Humana proof only in the objection handle / 1:1 replies, healthcare rows, labeled public. Intradiem stays out of Touch 1-3 bodies (brand-light window); named once from Touch 4. Signature: first name Touches 1-3, full name Touches 4-5.

**Cadence (both lanes):** T1 Day 1 Email 1 (MessageGen, 2-3 signal-assigned variants) · T2 Day 2 LinkedIn connect · T3 Day 4 Voicemail + LinkedIn message same day · T4 Day 6 Email 2 (new angle, never recycled) · T5 Day 9 Breakup.

---

## LANE 1 — cost_finance (the cost owner)

**The one idea:** their own mandate names the number; the fastest recoverable line against it is idle labor already on the payroll, bookable this fiscal period, no new headcount and no transformation project.

### Touch 1 (Day 1) — Email 1 (MessageGen output; three assigned variants)
- **1A — their-number opener (default when a disclosed figure exists):** leads with `{{their_figure}}` as stakes (see MessageGen Example A).
- **1B — post-RIF service floor (fires on `rif`):** they cut heads to hit a number; the remaining team's idle minutes are how service holds without rehiring what was just cut.
- **1C — no-number qualitative (block-on-empty fallback):** the mandate is public, no figure disclosed; leads with "the fastest recoverable cost under `{{mandate_event}}` is capacity you already pay for" — no dollar anywhere.

### Touch 2 (Day 2) — LinkedIn connection request
> {{first_name}}, I work the recoverable-capacity side of cost programs, the idle minutes inside large service workforces that a mandate like {{company}}'s can book against without another headcount decision. Seemed worth connecting.

### Touch 3 (Day 4) — Voicemail
> {{first_name}}, this is {{sender}} with Intradiem. I sent you a note on {{mandate_event}} and the piece of it that never makes the program plan: the paid idle capacity inside the workforce that remains. It books against the same target, this fiscal period, without a new headcount decision. I'm at [number], or just reply to the email. Thanks {{first_name}}.

### Touch 3 (Day 4) — LinkedIn message (same day)
> {{first_name}}, left you a voicemail too. Short version: {{mandate_event}} sets the target, and the fastest recoverable line against it is capacity already on the payroll, recovered in real time rather than through another round of cuts. Worth 15 minutes on where it sits at {{company}}?

### Touch 4 (Day 6) — Email 2 (the this-fiscal-period angle)
> Subject: bookable before the period closes
>
> Hi {{first_name}}, one thing about timing. Most levers under {{mandate_event}} are structural: they need a project, a vendor cycle, or a re-org before a dollar moves. Recovered idle capacity is the exception, because the minutes are already paid for and already inside the schedule; turning them into completed work starts showing up in the same fiscal period the decision is made. That's the piece Intradiem works: real-time recovery across the contact center and back office, on top of the stack you already run. Fifteen minutes and I'll walk the read on {{company}}'s workforce, floor by floor.
>
> {{sender_full_name}}

### Touch 5 (Day 9) — Breakup
> Subject: leaving it here
>
> Hi {{first_name}}, I'll stop here. One parting thought: every quarter a cost program runs, the workforce that remains carries paid idle minutes that never make the program math, and they're the cheapest dollars in the building because nobody has to be hired or cut to book them. When that line item becomes worth a look, that's the seam I work. Glad to help whenever the timing's right.
>
> {{sender_full_name}}

---

## LANE 2 — cost_ops (the floor owner)

**The one idea:** the mandate lands on their floor as do-more-with-less; the only headcount-free way to absorb it is the idle minutes already inside their team's day, the gaps WFM schedules around but never touches.

### Touch 1 (Day 1) — Email 1 (MessageGen output; three assigned variants)
- **2A — mechanism opener (default):** leads with the floor reality (see MessageGen Example B); the mandate appears late as the why-now; no figure unless disclosed.
- **2B — post-RIF burnout guard (fires on `rif`):** after a cut, SLAs slip and the remaining team burns out; recovered idle capacity is how service holds without rehiring.
- **2C — freeze-absorption (fires on `hiring_freeze`):** volume isn't frozen; recovered capacity absorbs the growth the freeze would otherwise break.

### Touch 2 (Day 2) — LinkedIn connection request
> {{first_name}}, I work the gap between what WFM schedules and what actually happens on the floor, the idle minutes that pile up when a cost mandate freezes the headcount but not the volume. Given you own that floor at {{company}}, seemed worth connecting.

### Touch 3 (Day 4) — Voicemail
> {{first_name}}, this is {{sender}} with Intradiem. I emailed you about absorbing what {{mandate_event}} puts on your team: the idle minutes already inside their day, recovered in real time for work, training, or coaching, without a req and without touching the stack you run. I'm at [number], or reply to the email. Thanks {{first_name}}.

### Touch 3 (Day 4) — LinkedIn message (same day)
> {{first_name}}, left a voicemail too. The heart of it: your WFM plans the day, but nothing acts in the gaps between scheduled work, and under {{mandate_event}} those minutes are the only capacity you'll get without a hire. Worth 15 minutes on which queues carry the most?

### Touch 4 (Day 6) — Email 2 (the team-protection angle)
> Subject: what the mandate does to your floor
>
> Hi {{first_name}}, the part of a cost program that never makes the announcement: it lands on the floor as more volume per person, and the first things sacrificed are training and coaching, which is how service erodes two quarters later. Recovering the idle minutes already inside the day flips that: the same capacity funds the coaching instead of disappearing into shrinkage. That's what Intradiem does in real time, on top of the WFM you already run. Fifteen minutes and I'll show which of your queues carry the most recoverable time.
>
> {{sender_full_name}}

### Touch 5 (Day 9) — Breakup
> Subject: leaving it here
>
> Hi {{first_name}}, I'll leave it here. One thought worth keeping: mandates end, but the idle minutes don't; they're on the payroll every day, and the floors that recover them ride out the next mandate instead of being reshaped by it. When that becomes worth a look, that's the seam I work. Glad to help whenever the timing fits.
>
> {{sender_full_name}}

---

## Objection quick-handles (both lanes, from intradiem-objection-handler)

**"We already have WFM."** Right, and keep it. WFM plans the day; it does nothing in the gaps between scheduled activities, and it stops at the contact center while the back office runs uncovered. This is the layer that acts in those gaps, on top of the WFM you just described.

**"No budget — we're cutting, not buying."** That's exactly the moment. The mandate created the target and the scrutiny; recovered idle capacity books against that target without a headcount decision, and the spend case is written in your own program's language. If it can't pay for itself inside the program, that's worth knowing in 15 minutes.

**"We built automation in-house / have RPA."** Good, that usually covers the transactions. The gap is the workforce layer: acting on the people-minutes between work in real time. RPA does the task; this recovers the humans' idle time around the tasks. They stack.

**"Send me information."** Will do. The one thing a deck can't answer is where your recoverable capacity actually sits, which floors and how much of it is bookable this period; that's a 15-minute conversation. I'll send the overview and we can find time if it's worth it.
> *Optional verified proof (1:1 replies, healthcare rows only, labeled):* Humana, on the record: first-year in-year return, 7X ROI five years in, 2 hours of capacity per agent per month (public SWPP/Intradiem webinar).

**"Bad timing — the program's just starting."** Program scoping is the cheapest moment to look: the recoverable-capacity line either makes the plan now or gets found two quarters in. Fifteen minutes now beats a re-plan later.

---

## Launch checklist (unchanged from the Golden Standard)
1. Mailbox warm to green first (2-3 weeks). Sender = the assigned rep.
2. Paste each lane as its own campaign ("Cost-Mandate (Finance/COO)" and "Cost-Mandate (Ops)") so per-persona analytics split free. Leads land via the sync column, Draft only.
3. Sync run-condition carries: send_ready AND NOT bdr_claimed AND customer_exclude != true AND Source Motion == "cost_mandate" AND msg1_critic Status == "PASS".
4. Approve a small first batch only; ~20 sends/day to start, 2-3 accounts/day, staggered lanes; bounce under 2-3%.
5. Read every rendered email in the Leads tab before launch. Track to qualified reply, never opens.
