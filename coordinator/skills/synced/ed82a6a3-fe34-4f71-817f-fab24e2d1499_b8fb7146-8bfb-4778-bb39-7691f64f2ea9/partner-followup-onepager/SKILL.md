---
name: partner-followup-onepager
description: Build the "what if they say yes" follow-up one-pager from a finished partner account brief, on the approved locked template. Trigger on "build the one-pager for [account]", "follow-up for [account]", "what do we send next", "one-pager based on this brief", or right after a partner-account-brief run. Fills the slots in template.html; never redesigns.
---

# Partner follow-up one-pager

The partner seller just had, or is about to have, the first conversation. This page is what lands next: Intradiem's story told through THAT account's specific, sourced situation. It is prospect-facing through a partner, so every line must survive scrutiny.

## How this works (non-negotiable)
This skill ships `template.html`, the approved design, and `example_mercury.html`, the approved worked example. You FILL THE SLOTS and change NOTHING else: no CSS, no structure, no section text outside the slots. The Proof section, the Alongside callout, and the What happens next steps are hard-coded in the template because they are the approved claims and the approved ask; they are not yours to edit. Output one complete HTML file named `<Account>_Followup_OnePager.html`.

## Inputs
A finished account brief in the conversation (run partner-account-brief first if there is none). One question if unanswered: which pains did the prospect validate, or is this pre-meeting? Pre-meeting, use the brief's two or three strongest sourced findings.

## The slots and how to write each one
Study `example_mercury.html` before writing; match its register exactly.

- `{{ACCOUNT}}`: the account name (page title only).
- `{{SUBHEAD}}`: one sentence starting "For a ..." that names the reader's world in their own terms: what they are, what operations are in scope, what is growing or under pressure. No company name needed; they know who they are.
- `{{OP_BULLET_1..3}}`: three findings about THEIR operation, each shaped as: `<strong>Plain-language claim in seven words or fewer.</strong> One or two sentences of sourced evidence with the specific figures. <span class="src">(source, date)</span>`. The account's own public figures are welcome here (their ratios, their headcount, their charges); they are the account's numbers, sourced. Never an Intradiem number, never an estimate presented as fact.
- `{{GAP_HEADLINE}}`: one two-part sentence naming the watch-versus-act gap in their world. The pattern: "Your systems can tell you what happened. None of them change what happens next." Adapt the nouns to their operation; keep the shape.
- `{{GAP_BODY}}`: two or three sentences making the gap concrete for their operation: what is scheduled in advance, what reports after the fact, and what the correction depends on today.
- `{{SOLVE_BULLET_1..3}}`: three bullets mirroring the OP bullets ONE TO ONE, same order. Each: `<strong>What changes, in their terms.</strong> One sentence of how, in the moment, automatically.` If OP bullet 2 is about the expense line, SOLVE bullet 2 answers the expense line. No feature names, no product SKUs.
- `{{PARTNER_LINE}}`: "Brought to you with [partner name]" only when the partner agreed to be named; otherwise "Brought to you by Intradiem" and the seller fills contact.
- `{{CONTACT_LINE}}`: leave the bracketed fill-ins as they are in the example unless real details were provided.

## Claims rules
- Everything in the three OP bullets carries a real source and date, taken from the brief.
- No dollar savings, ROI multiples, or customer stories anywhere. The Proof section already holds the only approved Intradiem claims and is locked.
- Never reference Intradiem's internal knowledge of the account's vendor contracts. Public evidence only.
- A stronger claim goes on the page only if it is confirmed in the Intradiem Value Repository (check the copy in this project's knowledge); otherwise it stays off.

## Voice
Calm, specific, peer-level. The prospect is the hero; the page reads like it was written by someone who studied their operation, because it was. Contractions. No superlatives, no exclamation points, no em dashes anywhere.
