# Star Ratings — Longer Horizon 5-touch Stage Prompts
Date: 2026-07-19 · Base: live "MessageGen Email 1 - Longer Horizon" (field `f_0ti7aa1XuAP4jZaQkqi`) · Gate: `parent_key` in {caloptima, lacare, iehp, myzinghealth, chpw, atriohp, baystatehealth}

## Why this is a separate line (not a delta over the standard E2-5)
The LH cohort is NOT at the cliff. The LH prompt has a hard rule, **"NEVER FABRICATE A CLIFF"**, that bans "only through December," "closing," "window," "last chance this cycle," "so close," "near the line." The standard E2-5 I authored lean on exactly that December-window urgency (E4/E5). So LH needs its own E2-5. Urgency here comes from COMPOUNDING (the forgone bonus recurs every year under 4.0) + the 2029 CAHPS concentration, never a deadline.

## Inherited from the LH E1 base (hold in every LH stage)
- **NEVER FABRICATE A CLIFF** (the ban list above). This is the rule most likely to drift in later touches; enforce it hardest in E4/E5.
- Dollar is **recurring annual** ("about $Xm a year, and it repeats every year the contract stays under 4.0"), read from `why_now`, CMS-estimate label + humility clause. Account-scoped, never per-contract.
- **LONGER-HORIZON BEAT** (2029 CAHPS concentration = reason to start the climb on service measures now, not a closing window). Vary the wording per touch.
- CS/CAHPS measures only, never clinical/HEDIS. Proportion honesty (service side is the part the team can move, not the whole climb). Brand-light (Intradiem at most once). No UHC $190M proof (excluded for this cohort, per decision). Persona routing on persona_key OR job_title.
- **Output alignment for the workflow:** the live LH E1 emits old "Line 1: Subject:" text. In the workflow, LH E1 must emit the SAME structured JSON (msg1_subject / msg1_body) as the default line so the shared audit chain reads it. Align the OUTPUT FORMAT block when injecting.

## Routing (workflow)
After the shared compose-inputs node, a `parent_key`-in-list conditional routes each stage to EITHER the default MessageGen Ei OR the LH MessageGen Ei; both converge into that stage's existing audit chain (malformed guard → critic → send-ready → voice → HOLD). One audit chain per stage, two prompt variants feeding it.

## LH E2 — Day 3 · New angle on the multi-year climb, soft
STAGE HEADER: Email 2 of a 5-touch LH sequence; reply in thread; open on a NEW facet of the multi-year service-measure climb, never "following up," never a deadline. Soft CTA, one question, end on it. 70-95 words.
Gold standard:
> Subject: where the multi-year climb starts
> Body: "Dana, one more angle on CalOptima OneCare's path back over 4.0. Because the gap is structural, the fastest-moving ground is the customer-service and complaints measures, the ones CMS keeps weighting heavier through 2029. So the service side is where a multi-year climb actually gets traction first, and every year the contract sits under 4.0 is another year of forgone bonus, so starting there compounds. You'll have a far sharper read than I will. Worth 15 minutes to look at which service measures move the rating soonest?"

## LH E3 — Day 6 · Value/proof lane (compounding), Intradiem once
STAGE HEADER: Email 3; no reply to 1-2; reply in thread. Value touch: the mechanism (teams move several service/CAHPS measures at once in real time; Intradiem named once) framed as how you START a multi-year climb, not a deadline play. No UHC proof. One question, end on it. 80-110 words.
Gold standard:
> Subject: how the climb actually compounds
> Body: "Dana, here's what the teams making real multi-year progress do. They stop treating the service measures as a once-a-year push and move several of them at once, in real time, which is what Intradiem does across the contact center and back office. For a plan sitting where OneCare is, that service side is the part the team can actually move, and the addressable bonus, roughly $9.6M a year from public CMS data, recurs every year it stays under 4.0, so the sooner the climb starts the more of it you keep. Worth 15 minutes on how you'd sequence it?"

## LH E4 — Day 9 · Direct, with the deliverable (no deadline)
STAGE HEADER: Email 4; no reply to 1-3; reply in thread. Lead with the concrete artifact (the contract-level math one-pager, which service measures move the rating soonest, account-scoped recurring dollar). Confident, their-payoff. NO December/window language. One question, end on it. 75-100 words.
Gold standard:
> Subject: the OneCare contract-level math
> Body: "Dana, let me make this concrete. I can put the contract-level math for CalOptima OneCare on a page: which of the customer-service and CAHPS measures move the rating soonest, how much of the recurring addressable bonus each one carries, and a realistic order to climb them over the next couple of cycles. That's the whole conversation, 15 minutes to walk it and you decide if there's anything there. Worth putting time on the calendar in the next couple weeks?"

## LH E5 — Day 12 · Confident close (compounding, not a deadline)
STAGE HEADER: Email 5, final; no reply to 1-4; reply in thread. Confident close: short, low-pressure, no guilt, no "last try," NO deadline/window. Close on compounding (every year under 4.0 is another year of forgone bonus). Door open. 45-70 words. May end on a statement.
Gold standard:
> Subject: leaving this with you
> Body: "Dana, I'll leave it here so I'm not crowding your inbox. The short version: the gap holding CalOptima OneCare under 4.0 sits in the service measures, they're the part the team can move, and the bonus it's forgoing recurs every year it stays under the line, so the climb pays back sooner the earlier it starts. If it's worth a look, just reply here and I'll send the contract-level math. Either way, appreciate you reading."

## Defaults chosen (Dallas can override)
- UHC $190M: EXCLUDED across LH (deadline-flavored). 
- Account list: hardcoded 7 (matches live gate); make registry-driven later.
- Run-mode: the workflow has its own manual trigger; the LH column's button-run flag does not carry in.
Run through intradiem-copy-sharpener before go-live; the NEVER-FABRICATE-A-CLIFF ban is the hard gate to verify.
