# Fix Spec — make fn_draft_critic motion-aware
Date: 2026-07-18 · Function table `t_0tiabaamPvDuEyTxSaF` · Shared across Cost-Mandate, WFM-Adjacency, Star Ratings

## The problem (found 2026-07-18)
`fn_draft_critic`'s system prompt is hardcoded "You audit one cold email drafted for Intradiem's Cost-Mandate motion," with Cost-Mandate-specific rules (idle-capacity phrasing, a Cost-Mandate SOURCE FIGURE LAW). It's a SHARED function now gating send-ready for WFM and Stars too. So the figure-integrity critic judges WFM and Stars drafts with Cost-Mandate criteria. The data plumbing is fine (node 8b's key matches); the AUDIT CRITERIA are mis-scoped. This gates the 6 live WFM send-ready contacts and the live Stars campaign.

## The fix: motion-agnostic core + motion-keyed addendum
Keep it ONE shared function (preserves "fix once everywhere"), but make the prompt read the motion and apply the right rules. It already has motion context available (`source_motion` in the row / trigger).

### Core (motion-INVARIANT — this is the whole job for most drafts)
Use the WFM "Final Audit Verdict" prompt as the clean base (it's already near motion-agnostic: the WHAT-IS-NEVER-A-VIOLATION / WHAT-TO-FAIL / THE-TEST structure). Core rules:
- FAIL only on: (a) a specific NUMBER/metric presented as fact about the prospect's operations without a populated Signal Source URL AND a Signal Source Date within 90 days, including "industry benchmark" numbers stated as fact; (b) a specific DATED or NAMED real incident asserted as verified fact with no signal backing; (c) a prohibited/misleading claim (deceptive guarantee, unverifiable superlative as fact).
- NEVER fail: the prospect's own company name; generic additive framing ("what you run"); the universal operational moment; hedged/industry-level language; the company's own employee/member count plainly framed.
- On FAIL, quote the exact offending phrase; if you can't quote a specific unsourced number or dated/named incident, verdict is PASS.

### Motion-keyed addendum (append the block matching source_motion)
- **star_ratings**: ALSO FAIL if a forgone-QBP dollar is attributed to a single contract (dollars are account-level, must read "$Xm across N contracts"); FAIL if a gross figure is used where the addressable slice is required; FAIL any implied clinical or HEDIS impact (Intradiem moves only the service/CAHPS measures). Naming one contract_id as the breakdown example is fine; attributing a dollar to it is not.
- **wfm_adjacency**: ALSO FAIL an idle-time/occupancy/shrinkage percentage stated as fact without a sourced+dated signal; FAIL any characterization of their WFM/CCaaS platform (Verint, NICE, Calabrio, Genesys, Amazon Connect) as failing/slow/lacking; FAIL any competitor or customer figure stated by hand (incl. Humana).
- **cost_mandate**: keep the existing Cost-Mandate SOURCE FIGURE LAW rules (pull them verbatim from the current prompt so nothing is lost).

## Build steps (Clay UI; Functions are UI-edit only)
1. First READ the full current `fn_draft_critic` prompt and preserve any Cost-Mandate guard still needed (move it into the cost_mandate addendum).
2. Replace the prompt: motion-agnostic core (WFM Final Audit Verdict base) + a switch on `source_motion` that appends the matching addendum.
3. Confirm the function receives `source_motion` (add it to the function inputs / Record if missing).
4. Regression test per motion BEFORE trusting: one known-good draft (must PASS) and one known-bad draft (must FAIL) for each of star_ratings, wfm_adjacency, cost_mandate. Especially: a Stars draft that attributes an account dollar to one contract MUST now FAIL.

## Guardrails
This gates live sends on three motions. Do not deploy without the per-motion regression test. Do not run two sessions editing this function at once.
