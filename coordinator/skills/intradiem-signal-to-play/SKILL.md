---
name: intradiem-signal-to-play
description: Closed-loop GTM engine that turns a single account signal into three synchronized outputs — a Marketing triggered-campaign brief, a Slack-ready Sales alert, and a send-ready personalized outreach draft — so Marketing and Sales act on the SAME trigger at the same time. Trigger on "run the signal play for [account]", "signal to play", "turn this signal into outreach", "[account] just had [event], what do we do", or any moment a real-world account signal (intent spike, leadership change, earnings/M&A, hiring surge, tech-stack shift, outage/disruption, regulatory deadline) needs to become coordinated GTM action. Mirrors Intradiem's own product thesis — real-time signals trigger automated action across the workforce — and doubles as an internal "we run GTM the way our product runs operations" proof point. Load proactively whenever a fresh account signal is surfaced.
---

# Intradiem Signal-to-Play Engine

## Scope reminder (read first)
Intradiem sells **Dynamic Workforce Orchestration** for large, structured workforces
in high-demand environments — across **contact centers AND back offices** (claims
processors, lending/underwriting, billing ops, field dispatch, fulfillment, care
teams). It serves six verticals: **Healthcare, Financial Services, Insurance, Retail,
Telecom, Utilities.** Do not frame this as a "call center" tool. The core mechanic is
real-time: reallocate idle/downtime to backlogs and training, auto-trigger task
reallocation to protect SLAs, deliver just-in-time coaching, and monitor burnout
before quality drops.

## Why this exists
Intradiem's product turns real-time operational signals into automated action across
the workforce. This skill does the same thing to GTM itself: one real-world account
signal fires, and Marketing and Sales act on it in lockstep instead of discovering it
days apart. Use the dog-fooding framing in any internal demo — "we run GTM the way our
product runs operations."

## Inputs (ask for anything missing before running)
- **Target account** (required) — and its vertical (Healthcare / Financial Services /
  Insurance / Retail / Telecom / Utilities), which shapes the use case
- **Signal** — the signal type + raw detail, OR an instruction to pull it live
- **Persona(s) in play** — front-office (VP Customer Care, Director Contact Center
  Ops, CX/CCO), back-office/ops (VP Operations, VP Claims, VP Shared Services,
  Director Back-Office Ops), WFM (VP/Dir Workforce Management), or economic buyer
  (CFO, COO)
- **Context (optional)** — open opp vs. net-new, deal stage, prior touches

## Pipeline

### 1. Signal intake & scoring
If a live pull is requested, use `intradiem-signals` and `intradiem-tam` to fetch and
score the signal on urgency / fit / timing. Otherwise score the provided signal.
Produce a single **"Why now" thesis** (one sentence) that everything downstream
anchors to.

### 2. Map signal → play
Translate the signal into the specific Intradiem pain it implies and the play that
addresses it. Match the play to the account's vertical and whether the pain sits in
the contact center, the back office, or both:
- Leadership change (new COO / VP Ops / VP Care) → efficiency mandate → real-time
  idle-time reallocation play
- Earnings miss / cost pressure → margin scrutiny → capacity-recovery + backlog-
  clearance play
- Hiring surge / seasonal ramp → onboarding & adherence pain → just-in-time
  training & coaching play
- New WFM / CCaaS / back-office system → integration moment → augment-not-replace
  orchestration play
- Outage / disruption (Utilities, Telecom) → surge response → dynamic reallocation play
- Regulatory deadline (Healthcare, Insurance, Financial Services) → compliance-
  training-completion play (deliver training without pulling staff off queues/cases)

### 3. Pull proof
Invoke the `intradiem-verified-metrics` skill for **every** stat. Never invent a
number. Match the proof point to the account's vertical where possible. Respect 1:1
vs. 1:many approval tiers. If a stat can't be verified, flag it explicitly rather than
guessing.

## Outputs — produce all three, clearly separated

### A) Marketing Triggered-Campaign Brief
- Audience segment + suppression notes
- Campaign angle tied to the signal and the vertical use case
- Recommended channels + 3 subject/hook options
- One 3-touch nurture outline and the single verified proof point that anchors it

### B) Sales Alert (Slack-ready, copy-paste, **under 120 words**)
- BLUF: what fired, why it matters, what to do in the next 24 hours
- The "Why now" thesis + the one metric to lead with

### C) Personalized Outreach Draft (send-ready)
- One cold email — persona-calibrated, signal-anchored, prospect-as-hero, soft CTA
- One LinkedIn touch (**under 300 characters**)
- Brand-light, no fabricated stats

## Constraints
- Never reduce Intradiem to "call center." Frame by workforce + vertical use case.
- Every metric traces to a verified source; flag gaps explicitly.
- Apply Dallas's brand voice and Intradiem brand guidance where those skills exist.
- Tone: peer-level, clinical, no hype.

## Verification step (run before finishing)
Self-check and report what you checked:
1. All three outputs present and clearly separated.
2. Use case matched to the account's vertical and front/back-office reality.
3. Every stat verified or explicitly flagged.
4. Outreach passes a "would a real person actually send this" read.
5. Sales alert under 120 words; LinkedIn touch under 300 characters.

## Trigger phrases
"run the signal play for [account]", "signal to play", "turn this signal into
outreach", "[account] just had [event] — what do we do", "make a play out of this
signal".
