# WFM-Adjacency Email 2-5 Stage Prompt Build Sheet
Date: 2026-07-18 · Table: L3 `t_0tic8arWbZp8bSx87Ad` · Motion: wfm_adjacency

## Purpose
Stand up four new MessageGen columns (Email 2-5) so Clay generates a personalized 5-touch sequence per contact, each touch gated to READY by the same critic chain as Email 1. This is a v1 spec. Run each stage through `intradiem-copy-sharpener` before flipping it live; every stage inherits the verified-claims gate.

## Architecture (single responsibility, do not violate)
- **Each column = one email.** Email 1 (`P2P Outreach Email`) is cold, Day 1. Email 2-5 are the follow-up touches.
- **The sequencer schedules and threads; it never writes copy.** Static boilerplate follow-ups would live as fixed sequencer steps and need no MessageGen. These are personalized, so they are MessageGen columns.
- **Replies are a fourth job** (`intradiem-objection-handler`, human-gated, needs the inbound message as input). Never a Clay column.

## The shared block (single source of truth)
Your live `P2P Outreach Email` prompt IS the shared house-style block. Every stage prompt below = **[STAGE HEADER] + [the full shared block, pasted verbatim]**. Inherit these from the shared block unchanged in all five, never re-derive or reword them:
- THE CORE POSITION (additive execution layer on top of the WFM/CCaaS stack they keep)
- The number gate / Top Signal Rule (a specific figure only with a populated Signal Source URL AND a date within 90 days; unsourced or "industry benchmark" numbers are an automatic FAIL)
- PROOF BEAT (specific+named only from the verified-repository feed, which is not wired yet; industry-level qualitative pattern is the only proof allowed today; never invent a customer, outcome, or number; never name Humana or any customer by hand)
- PERSONA ROUTING (wfm / cc_ops / coo_finance) — the two lanes are handled here, inherited by every stage
- COPY RULES, BANNED WORDS, OPENER discipline, SENTENCE FLOW, PLAIN-SPOKEN rules, TOKEN USE, no em dashes, contractions always
- OUTPUT: valid JSON, `subject` (8 words max) + `body` (70-110 words), salutation is first name + comma, no signature block

## The one idea (constant across all 5, never restated, approached from a new angle each touch)
WFM schedules the day but can't act in the idle minutes between scheduled activities; that idle capacity is recoverable in real time on top of the stack they already run. Each touch advances ONE new facet of this. No touch repeats the full pitch.

## Thread handling (Email 2-5)
These send as replies in the same thread, so they open on a new facet, not on the silence. BANNED openers (in addition to the shared block's list): "just following up," "circling back," "bumping this," "checking in," "wanted to resurface," "in case you missed it." Pick the idea back up mid-thought, the way you would if you'd been thinking about their floor since the last note.

---

## EMAIL 2 — Day 3 · New angle, still soft
STAGE HEADER to prepend to the shared block:
> You are composing EMAIL 2 of a 5-touch sequence to a prospect who has not replied to Email 1. This sends as a reply in the same thread. Open on a NEW facet of the one idea (a different place the idle minutes appear), never on the fact they didn't reply and never by re-pitching Email 1. Escalation: still soft, curiosity over ask. Brand window: WFM convention B, Intradiem may appear AT MOST ONCE (same as Email 1), but lead with the operational moment and keep the product late or absent; the soft touch is stronger without it. CTA: low-friction, name what the 15 minutes is about, exactly one question, END on that question. 70-95 words. Generate NO signature (same as Email 1); the sender/signature layer handles the sign-off.

Stage gold-standard (sharpened 2026-07-18; no number, no named customer, industry-level proof, ends on the question):
> Subject: the minutes right after a call wraps
> Body: "Noemi, one more place this shows up. It's not just the coaching pull-offs, it's the stretch right after a call wraps early, before the next one routes. Scheduling works in blocks, so those minutes fall between them and nobody's assigning them. That time's recoverable the same day, on top of what you already run, without asking anyone to move faster. The teams handling this well point it at the small things that used to wait, a quick coaching nudge, a certification. Worth fifteen minutes to see where it sits across your queues?"

## EMAIL 3 — Day 6 · Value/proof lane, brand window opens
STAGE HEADER:
> You are composing EMAIL 3 of a 5-touch sequence; the prospect has not replied to Email 1 or 2. Sends as a reply in the same thread. This is the value/proof touch. Brand window is now OPEN: you may name Intradiem once and lead with the industry-level proof beat (how customers in their space use it), still with NO named customer and NO number unless the row's signal is sourced and dated within 90 days. Escalation: slightly firmer, the ask is more direct than Email 2 but still their-payoff framed. CTA timing for VP+ recipients: "in the next couple weeks," never a tight this-week anchor. 80-110 words. Generate NO signature; the sender/signature layer flips to FULL NAME from Day 6.

Stage gold-standard (sharpened 2026-07-18; Intradiem named once, no customer, no number, VP-appropriate timing):
> Subject: how peers use the idle minutes
> Body: "Noemi, here's what the teams solving this actually do. They stop treating the idle minutes as unavoidable and put them to work in real time, on coaching, training, or handled work, on top of the WFM platform they already run. Intradiem is the layer that does it, no new heads, no change to the scheduling stack. The ones doing it well aren't hiring for coverage, they're using time they already pay for that used to sit empty between scheduled activities. If it's worth a look, I can walk you through where that capacity sits across your floors and queues. Worth fifteen minutes in the next couple weeks?"

## EMAIL 4 — Day 9 · Direct, with a deliverable
STAGE HEADER:
> You are composing EMAIL 4 of a 5-touch sequence; no reply to Emails 1-3. Sends as a reply in the same thread. This is the direct-with-deliverable touch: lead with the concrete artifact you'll bring (the read of where recoverable idle capacity sits across their contact center floors, queues, and back-office teams) and make the ask specific and confident, still their-payoff framed, never seller-want. Brand window open (Intradiem at most once). Exactly one question, end on it, VP-appropriate timing. 75-100 words. Generate NO signature; sender layer signs FULL NAME.

Stage gold-standard (sharpened 2026-07-18; deliverable-led, back-office positioning intact, one question):
> Subject: the read on where your idle capacity sits
> Body: "Noemi, let me make this concrete. I can put together the read of where the recoverable minutes actually sit for you, the gaps after early wraps, the coaching and compliance pull-offs, the back-office queues running uncovered while the floor is scheduled, and what it'd take to fill them in real time on top of your current stack. That's the whole conversation, fifteen minutes to walk it and you decide if there's anything there. Worth putting time on the calendar in the next couple weeks?"

## EMAIL 5 — Day 12 · Confident close
STAGE HEADER:
> You are composing EMAIL 5, the final touch; no reply to Emails 1-4. Sends as a reply in the same thread. This is the confident close: short, low-pressure, no guilt, no "last try" or "final attempt" language. Leave the door open and make it easy to restart later. Brand window open but light (Intradiem not required). 45-70 words. A confident close may end on a clean statement rather than a question (the one intentional exception to end-on-a-question). Generate NO signature; sender layer signs FULL NAME.

Stage gold-standard (sharpened 2026-07-18; confident close, door open, no guilt):
> Subject: leaving this with you
> Body: "Noemi, I'll leave it here so I'm not crowding your inbox. The short version: the minutes your schedule can't fill are recoverable in real time, on top of what you already run, and I'd still be glad to show you where they sit. If the timing's better later, just reply here and I'll pick it back up."

---

## Audit chain reuse (per stage)
Each stage email needs the same gating as Email 1. Reuse, do not rebuild:
1. Point a copy of the `Final Audit Verdict` critic at the stage's draft body (the critic prompt is stage-agnostic; it only checks for unsourced numbers and dated/named incidents).
2. Point a copy of `Email Voice Audit` → `Voice Rewrite (Final)` → `Final Voice Audit` at the stage draft.
3. Extend the `Send Ready` formula (or make a per-stage Send Ready) so a stage is READY only when its own audit verdict AND voice audit both pass.
For 6 contacts this is small. If the per-stage audit sprawl gets heavy at scale, consolidate to one shared critic column that takes the stage draft as input.

## Clay UI build steps (AI columns are UI-only; the API cannot create them)
For each of Email 2-5:
1. In the L3 table, Duplicate the `P2P Outreach Email` column (this carries the AI action type and claude-sonnet-5 model).
2. Rename it `MessageGen Email N (WFM-Adjacency)`.
3. **The Duplicate BLANKS the prompt** (known gotcha). Open Edit column and paste: [STAGE N HEADER] + [full shared block from Email 1]. Pass any genuinely blank field as the literal `(none)`, never `""`.
4. Repeat the Duplicate-and-repaste for that stage's `Final Audit Verdict`, voice audit, rewrite, and final voice audit, repointing each token to the stage N draft.
5. Run one test row end to end and confirm it reaches READY before building the next stage.

## Notes
- Credit: 6 contacts x 4 new emails x (gen + audit calls) is a small spend; run a credit check before applying this pattern to a larger wave.
- The two-lane split (wfm/cc_ops vs coo_finance) is already handled by the inherited persona routing; no separate lane columns needed.
- Sending is downstream: even at READY, no send until deliverability is refreshed (currently UNKNOWN) and mailbox warmup is complete.

---

## Copy-Sharpener Pass — 2026-07-18 (intradiem-copy-sharpener)

Applied to the four stage gold-standards above. Channel: cold email follow-up (WFM-Adjacency). Sender: WFM motion rep (confirm per motion). Examples are templates, not account sends.

### Changes log
| Stage | Original | Sharpened | Rule | Rationale |
|---|---|---|---|---|
| E2 header | (sharpener tried "BRAND-LIGHT, do NOT name Intradiem") | "Intradiem at most once, same as Email 1" (WFM convention B) | Motion override of Rule 4 | Dallas ruled B: WFM allows Intradiem once per touch from Day 1, matching the live/tested Email 1. The generic brand-light Days 1-5 rule does NOT apply to this motion. Reverted. |
| E2 CTA | "...across your queues? Fifteen minutes." | "Worth fifteen minutes to see where it sits across your queues?" | Rule 6 | Never end on a statement; fold the ask into one question that names the topic. |
| E3 CTA | "Fifteen minutes this week?" | "Worth fifteen minutes in the next couple weeks?" | Rule 6 seniority timing | Tight this-week anchors read as desperation to VP+; widen for senior personas. |
| E4 CTA | "Does a short window this week or next work better?" | "Worth putting time on the calendar in the next couple weeks?" | Rule 6 | One clean question, VP-appropriate timing, ends on the ask. |
| E5 close | "...pick it back up. Either way, appreciate you reading." | "...just reply here and I'll pick it back up." | Rule 6 confident-close | Breakup ends clean and low-pressure; trimmed the trailing filler line. |
| All headers | "Sign-off: FIRST/FULL NAME" (in body) | "Generate NO signature; sender/signature layer handles the flip" | Consistency w/ Email 1 | Email 1 generates no signature block; the first-name (D1-5) → full-name (D6+) flip lives in the sender's signature template, not the AI column. |

### Verified-claims ledger (hard gate)
| Claim in copy | Type | Repository status |
|---|---|---|
| (none) | no numbers, no % figures, no dollar amounts across E2-E5 | PASS — nothing to verify |
| "the teams handling this well / the ones doing it well" | industry-level use pattern, no named customer, no outcome figure | PASS — allowed proof beat, carries no verified-claims risk |
| "Intradiem is the layer that does it" (E3) | product position, no metric | PASS — Day 6+, additive framing, no claim to verify |
Result: all four pass the verified-claims gate. No `[UNVERIFIED]` tokens present. The moment the verified_proof feed is wired, a named+numbered proof line may be added to E3/E4 verbatim with its approved label.

### Send-Ready test (template level)
PASS on: opens on a new facet not a greeting; answers "so what"; under word count; one question per CTA (E2-E4); CTA names the topic; prospect is the hero, self-selection holds; persona tone (wfm/cc_ops/coo_finance inherited); zero forbidden words; zero em dashes; zero product tells; **WFM brand convention B applied (Intradiem at most once per touch from Day 1, not the generic brand-light Days 1-5 hold)**; verified-claims clean; bodies flow, no staccato.
Carry-forward (applied at build, not template): sender signature flip D1-5 → D6+; per-row persona routing; the number gate fires only when a row's signal is sourced and dated within 90 days.

### Final recommendation
The four stage examples are send-ready as templates. Before go-live, run ONE generated row per stage through the live column output and re-check the number gate on any row that actually carries a sourced signal (the examples deliberately use the no-number path). WFM runs tighter than the generic playbook's 120-150 word Email 2+ band by design; keep the tight voice.
