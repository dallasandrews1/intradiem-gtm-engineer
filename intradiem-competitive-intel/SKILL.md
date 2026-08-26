---
name: intradiem-competitive-intel
description: Competitive displacement orchestrator for Intradiem. Identifies competitor mentions (Verint, NICE, Calabrio, Assembled, Playvox, in-house RPA/scripts, status quo) and generates counter-narrative briefs with wedge analysis, reframe positioning, and trap-setting talking points. Trigger immediately when a competitor is named in any call, email, or note; when an RFP mentions competing solutions; or when a prospect says they're "evaluating options." Built for the GTM Engineer to turn competitor mentions into operational wedges for Sales.
---

# Intradiem Competitive Intel Engine

## When this skill applies
- Trigger immediately when a competitor is named in any call, email, or meeting note
- Run after an RFP review mentions competing solutions
- Run when a prospect indicates they are "evaluating options"
- Run during competitive deal situations (pilot vs. competitor's pilot)

## Background
This skill turns competitor mentions into strategic advantage. It diagnoses what the
competitor will say, where they are genuinely strong, and critically where they
break — then generates a wedge narrative and trap-setting questions that plant doubt
while positioning Intradiem as the operational fix. The wedge is always operational,
never feature-trivia.

## Competitor map
Map any mention to one of:
- **Verint** — WFM / WEM suite incumbent
- **NICE** — CXone / WFM platform incumbent
- **Calabrio** — WFM + analytics
- **Assembled** — modern WFM (support teams)
- **Playvox** — WFM / QA (now Verint)
- **In-house RPA / scripts** — they built automation themselves
- **Status Quo** — no automation; manual supervisor intervention

If the competitor is unnamed ("we're looking at vendors"), apply Status Quo framing.

## Pipeline

### 1. Identify competitor & extract positioning
Parse the transcript/email/note for the explicit mention. Pull the prospect's own
language describing the competitor and any claims or features they referenced.

### 2. Build "What They Will Say"
Write the competitor's likely pitch (2-3 talking points they lead with). Stay
clinical and peer-level. No mockery.
- Verint / NICE: "single suite, we already own your WFM"
- Calabrio: "WFM plus analytics in one"
- Assembled: "modern, fast to deploy for support teams"
- In-house: "we can script this ourselves / we own it"

### 3. Where they are strong (be honest)
List 2-3 genuine strengths. Credibility requires acknowledging real advantages —
e.g., incumbency, existing data, single-vendor convenience.

### 4. The wedge (where they break) — operational, not feature
Find the gap between claimed strength and reality. Examples:
- "Your WFM suite forecasts and schedules, but it doesn't *act* in real time when
  the day goes sideways. Who closes the gap between the forecast and the live floor?"
- "In-house scripts work until the person who wrote them leaves. Who owns that
  automation when your dev team is split across three priorities?"
- "A single suite is convenient, but 'we already own it' often means 'the automation
  module is on a roadmap we don't control.' What's actually live today?"
- "Most WFM tools stop at the contact center. Your idle time, backlog, and training
  pain in the back office (claims, lending, billing, fulfillment) sit outside their
  scope. Who orchestrates the whole workforce, not just the phones?"

### 5. Questions to plant
3-4 innocent-sounding questions for the prospect to ask the competitor that expose
the wedge without revealing strategy. E.g.:
- "When intraday reality diverges from forecast, what does the platform do
  automatically vs. what still needs a supervisor?"
- "Is the real-time automation live today, or roadmap? Can we see it on our stack?"
- "If we build in-house, what's the maintenance owner when staffing changes?"

### 6. The reframe (Intradiem positioning)
2-3 sentences positioning Intradiem against this competitor's specific weakness —
real-time, automated action across the whole workforce (contact center AND back
office: claims, lending, billing, underwriting, fulfillment), guaranteed measurable
results, augmenting the WFM they already own rather than replacing it. The platform
frame (Naveen's words): a suite of products moving various metrics that delivers
what pure human investments and pure AI investments have both failed to deliver on
these goals; DWO is the third path, not a bigger version of either. The structural
wedge against contact-center-only WFM tools (Verint, NICE, Calabrio, Assembled,
Playvox) is scope: Intradiem orchestrates front and back office; they don't. Route any
stat through `intradiem-verified-metrics`.

### 7. Trap-setting talking points
4-5 peer-level, observational statements Dallas/the rep can make in discovery to
prime doubt without sounding sales-y.

## Output

Save as: `[Account]_Competitive_Brief.md`

```
# [Account Name] Competitive Brief
Date: [Date]
Competitor: [Verint / NICE / Calabrio / Assembled / Playvox / In-House / Status Quo]
Deal Stage: [Current Stage]

## What They Will Say
[2-3 expected talking points]

## Where They Are Strong
1. [Genuine strength]
2. [Genuine strength]
3. [Genuine strength]

## The Wedge (Where They Break)
[Operational-gap narrative]

## Questions to Plant
- [Question 1]
- [Question 2]
- [Question 3]

## The Reframe (Intradiem Positioning)
[2-3 sentences; verified stats only]

## Trap-Setting Talking Points (Internal Use)
- [Observation 1]
- [Observation 2]
- [Observation 3]
- [Observation 4]

## Next Steps
[How to deploy this brief in the next call or email]
```

## Constraints
- Wedge is operational, never feature-trivia or ad hominem.
- **The module, never the layer.** When Verint/NICE/Calabrio appear in a deal, the wedge targets their automation add-on module or their contact-center-only scope, never the WFM layer itself. Intradiem sits on and acts within that layer; disparaging it undermines our own integration story and the DWO positioning (we orchestrate the whole workforce on top of the stack they already own).
- Acknowledge real competitor strengths — credibility first.
- Every stat verified via `intradiem-verified-metrics` or flagged `[VERIFY]`.
- Apply Intradiem brand voice. Tone: clinical, peer-level, no mockery.
- Named output — save as a file.
