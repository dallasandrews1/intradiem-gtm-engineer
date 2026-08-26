# Reply System Build Sheet — Star Ratings (reusable across motions)
Date: 2026-07-18 · Table: Contacts (Buying Committee) `t_0thtm73HHxyiupTuepK` · Sender: Smartlead campaign "Stars QBP Wave 1 - Persona 1"

## Why now
Wave 1 (23 sent) is drawing replies (an OOO and an info request on day 1) and there is no reply-handling infrastructure, only a bare `reply_status` select field. This builds the triage + draft layer so no reply is dropped. Structure is motion-invariant; only the objection reframes are motion-specific (they live in intradiem-objection-handler). Fold this into the motion-stamp library once proven here.

## Architecture (the split)
Replies land in Smartlead, not Clay. Clay generates from row data, so the reply BODY must be synced into a Clay column first. Then:
- **Clay does triage** (classify + route + urgency) as an AI column, row-data friendly.
- **Clay drafts the reply** as a second AI column carrying the objection-handler reframe framework, gated to HOLD; a human sends. High-stakes or ambiguous categories escalate to the `intradiem-objection-handler` skill instead of auto-drafting.
- Nothing sends automatically. Ever.

## Prerequisite: get the reply text into Clay
Add/confirm a `reply_body` column populated from Smartlead (reply webhook or the reply sync that already feeds `reply_status`). Without the inbound text in the row, the AI columns have nothing to read. Confirm whether Smartlead's Clay integration pushes reply body, or whether it needs a webhook/Zapier bridge.

## Column 1 — Reply Triage (AI column)
Input: `reply_body` + row context (first_name, company, persona_key, the contract/why_now).
System prompt:
> You classify one inbound reply to a cold outbound email (Intradiem Star Ratings motion). Judge ONLY the literal reply text. Return JSON: category, urgency (high/med/low), one-line reason, suggested_action.
> Categories (pick exactly one):
> - POSITIVE_MEETING — wants to talk, book, or asks for time. urgency high.
> - POSITIVE_INFO — asks for more info, a one-pager, the math, "send me detail." urgency high.
> - REFERRAL — redirects to another person/team. urgency med. Capture the named person in reason.
> - OBJECTION — pushback: bad timing, "we have WFM," built in-house, evaluating a competitor, no budget, wait for ratings. urgency med.
> - NOT_INTERESTED — clear pass/no. urgency low.
> - OOO_AUTO — out-of-office or auto-reply. urgency low. If a return date is present, put it in suggested_action.
> - UNSUBSCRIBE — opt-out / do-not-contact / remove me. urgency high (compliance).
> - NEUTRAL_UNCLEAR — anything else / can't tell. urgency med.
> suggested_action: one short imperative (e.g. "schedule follow-up 7/20", "draft info reply + one-pager", "route to named referral", "suppress + mark opted out", "human review").
> Never draft the reply here; classify only.

## Column 2 — Reply Draft (AI column, gated to HOLD)
Runs ONLY for categories POSITIVE_MEETING, POSITIVE_INFO, REFERRAL, and OBJECTION (skip OOO_AUTO, NOT_INTERESTED, UNSUBSCRIBE, NEUTRAL_UNCLEAR — those route to a human/action, not a draft).
Input: `reply_body` + triage category + row context + the sender's Email 1 thread.
System prompt = [objection-handler reframe framework] + [voice_core subset]:
> You draft one reply in the sending rep's voice to an inbound response, in the same thread. Peer-level, 3-4 sentences. Framework: Acknowledge (their point, genuinely) → Insight Pivot (reframe toward the one idea) → Soft CTA (their-payoff, one question, ends on it).
> Per category:
> - POSITIVE_MEETING: confirm enthusiasm briefly, propose the concrete 15 minutes, name what you'll walk (the contract-level Stars math). One scheduling question.
> - POSITIVE_INFO: give a tight, useful answer or the one-pager offer, then a soft CTA to walk it live. Do not dump; earn the meeting.
> - REFERRAL: thank them, ask for the intro or confirm you can reach out to the named person, keep the door open.
> - OBJECTION: run the matching reframe from intradiem-objection-handler (Bad Timing, Have WFM, Built In-House, Evaluating Competitor, No Budget, Wait for Ratings). Acknowledge → insight pivot → soft CTA. Never argue.
> Hard rules (inherit voice_core): no em dashes; contractions; no banned words; verified-claims gate (no Intradiem number unless from the approved repository); the UHC $190M line is the only pre-cleared third-party proof and only as historical context. Prospect is the hero. Output JSON: reply_subject (keep the thread subject), reply_body, and a confidence (high/med/low). Gated to HOLD; a human reviews and sends.

## Column 3 — Reply Route (formula)
From triage category, set a routing label the rep works from:
- POSITIVE_* → "HOT: review draft + send" · REFERRAL → "re-route" · OBJECTION → "review reframe" · OOO_AUTO → "schedule follow-up <date>" · NOT_INTERESTED → "suppress" · UNSUBSCRIBE → "suppress NOW (compliance)" · NEUTRAL → "human review".

## Escalation rule (human, not a column)
Any OBJECTION with confidence < high, any NEUTRAL_UNCLEAR, and anything naming a competitor or legal/compliance concern goes to `intradiem-objection-handler` run by a human, not the auto-draft. The column handles the clean cases; the skill handles the hard ones.

## Build steps (Clay UI; AI columns are UI-only)
1. Confirm/add `reply_body` synced from Smartlead.
2. Create `Reply Triage` (Use AI, claude-sonnet-5), paste Column 1 prompt, bind `reply_body` + context via the / picker.
3. Create `Reply Draft` (Use AI, claude-sonnet-5), run-condition on the four draftable categories, paste Column 2 prompt.
4. Create `Reply Route` formula (Column 3).
5. Test on the two live replies (Kim OOO → should route "schedule follow-up 7/20"; Latonya info-request → should draft a POSITIVE_INFO reply to HOLD).

## Guardrails
Nothing auto-sends. Every draft is HOLD → human. Verified-claims gate on every drafted line. UNSUBSCRIBE routes to immediate suppression. Do not run two sessions editing this table at once.

## Reusability
Columns 1 and 3 (triage + route) are fully motion-invariant. Column 2 inherits voice_core + the per-motion objection reframes. Promote triage + route into the motion-stamp library as a `reply_handling` template after this proves out on Stars.
