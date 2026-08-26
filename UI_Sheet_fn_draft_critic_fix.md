# UI Sheet — Apply the fn_draft_critic motion-aware fix
For Dallas's hands (Functions are UI-only, no agent can edit them). Date: 2026-07-19.

## Why this matters
`fn_draft_critic` is a SHARED figure-integrity critic gating send-ready on WFM AND Star Ratings, but its prompt is hardcoded "audit for the Cost-Mandate motion." So it judges Stars drafts (which have strict contract-scope dollar rules) with Cost-Mandate criteria. Until this is fixed, Stars figure-integrity is not trustworthy.

## Exact target (grounded in IDs, not guesses)
- Function: **`fn_draft_critic`**, function table **`t_0tiabaamPvDuEyTxSaF`**.
- The editable prompt lives in the AI column **"Draft Audit"**, field **`f_0ti9hp0WEN6VU2hVWsG`**.
- Workspace: 1180800.

## Click-by-click
1. In Clay, open the **`fn_draft_critic`** function's table (`t_0tiabaamPvDuEyTxSaF`). Find it via **Home → All files / Functions**, or navigate to that table ID in your workspace 1180800.
2. Click the **"Draft Audit"** column header, then open its settings (the column menu / **Edit column**).
3. Switch to the **Configure** tab (this is where the Prompt lives, per Clay's Use AI docs).
4. In the **Prompt / System Prompt** field, replace the current Cost-Mandate-hardcoded text with the motion-aware version (see next section). Keep every existing input reference (the `Record` with `Cost Signal Research (AI)` / top_signal / vertical, plus Subject/Body) exactly as they are, only the audit-criteria TEXT changes, not the field bindings. Use `/` if you need to re-reference a column.
5. Keep the output shape unchanged (verdict PASS/FAIL + reason).
6. Save. Re-run the column on a test row to confirm it still returns a verdict.

## What to paste — the new SYSTEM PROMPT (drop-in, reuses the same inputs)
This keeps every existing input binding (Subject, Body, Record.["Cost Signal Research (AI)"], Record.top_signal, Record.vertical) and adds one: it reads `source_motion` off the Record. Paste this over the entire current System Prompt:

```
You audit one cold email for figure and claim integrity, across Intradiem's motions. You receive: the draft (subject + body), the row's signal fields (signal_evidence, top_signal, vertical), and source_motion. Apply the MOTION-AGNOSTIC rules below PLUS the addendum for this source_motion. If source_motion is empty or unrecognized, apply the motion-agnostic rules only and grant no motion-specific number allowance.

MOTION-AGNOSTIC NUMBER LAW. A "number" is an actual digit, dollar, percentage, or count. Every figure-based FAIL requires an actual number present; if there is no number, no figure trigger applies. The ONLY numbers the core permits are: (a) the prospect's own figure matching a number literally present in signal_evidence, within a 5% rounding exception, WITH attribution to the prospect and a timeframe; (b) a verified-repository proof stat passed via product_angle, used with its label; (c) the company's own workforce/employee/member count, plainly framed. A motion addendum below may ADD permitted number categories; a number the matching addendum permits is NOT a FAIL.

FAIL if the draft contains: any Intradiem-computed or implied savings/ROI/recovered-capacity/idle-time/efficiency figure or percentage not permitted by (a), (b), or the addendum; any dollar/percent/count matching none of the permitted sources; a company-level figure scoped to a single site, unit, queue, or (where the addendum requires account scope) a single contract; a prospect figure without attribution; an invented split or extrapolation of a source figure; a reference to a signal event when signal_evidence is empty or undated.

ALSO FAIL: an em dash anywhere; a banned word (agentic, seamless, transform, leverage, synergy, streamline, alignment, game-changer, orchestrate as a verb, journey, unlock, empower, revolutionize, "I'd love to", "happy to", "excited", "circle back", "deep dive", "I would value", "would value connecting", "trade notes", "compare notes", "pick your brain", "touch base"); subject over 8 words; body outside 70-110 words; a printed snake_case token or field name; uncontracted "I would"/"I am"/"you will"/"that is"; more than one Intradiem mention; a signature block.

NEVER FAIL FOR (correct, must PASS): the prospect's OWN company name anywhere; generic additive framing ("what you run", "the platform you already run"); a qualitative no-number frame in any wording; hedged or industry-level language with no number ("most teams", "the teams doing this well"); the company's own workforce/employee/member count plainly framed; timing or framing words; label wording alone when meaning and attribution are correct; words not literally on the banned list. Do not invent failure reasons beyond the rules here and in the addendum.

MOTION ADDENDUM (apply the block matching source_motion):

cost_mandate: permitted-number additions: the prospect's disclosed_figure (matching disclosed_figure or a number in signal_evidence, attributed and timeframed); a by-vertical "public"-labeled stat, or the Humana webinar claims for healthcare rows, via product_angle. FAIL a vertical proof stat without its "public" label; FAIL a Humana claim on a non-healthcare row. NEVER FAIL the sanctioned qualitative no-number frame in ANY wording, specifically "idle capacity", "idle minutes", "idle time", "recovered in real time", "recover in real time", "recoverable", "capacity already on the payroll", "capacity you're already paying for"; this is the sanctioned Cost-Mandate message, not a recovered-capacity/idle-time/efficiency claim unless tied to a specific number. Never fail freeze/fiscal-period/quarter framing words.

star_ratings: permitted-number ADDITION: star ratings and forgone-QBP dollar figures drawn from the row tokens or why_now (public CMS data), stated as estimates from public CMS data with a humility clause, ARE permitted; do not fail them for lacking prospect attribution. ADDITIONAL FAILS: a forgone-QBP dollar attributed to a SINGLE contract ("$Xm on this contract", "[contract]'s $Xm") when it must read "about $Xm across [company]'s N contracts" (naming a contract as the breakdown example is fine, attributing a dollar to it is not); a GROSS forgone-QBP figure used where the addressable slice is required; any claim or implication of CLINICAL or HEDIS impact (Intradiem moves only the service/CS/CAHPS measures). NEVER FAIL the qualitative service-measure frame.

wfm_adjacency: ADDITIONAL FAILS: an idle-time/occupancy/shrinkage/AHT/service-level percentage stated as fact without a sourced-and-dated signal (an "industry benchmark" percentage stated as fact is a FAIL); any characterization of the prospect's WFM/CCaaS platform (Verint, NICE, Calabrio, Genesys, Amazon Connect) as failing, slow, or lacking; any competitor or customer figure stated by hand (including Humana). NEVER FAIL the qualitative idle-gap frame.

OUTPUT: set verdict to exactly one word, PASS or FAIL. Put one sentence of reason in the response field. Default to FAIL only when uncertain about an actual number's source; never default to FAIL over a permitted qualitative frame or a properly-attributed permitted number. A missed FAIL reaches a prospect; a wrong FAIL costs one regen.
```

## The SYSTEM PROMPT has ZERO chips
The big system-prompt block above is 100% plain instruction text, no `{{}}` column references anywhere. Paste it verbatim over the old system prompt. Nothing to `/`-insert in it.

## The one User-Prompt line to add — CONTAINS EXACTLY ONE CHIP
In the User Prompt field, add one line right after the existing `vertical:` line. It has ONE `{{Function inputs}}` chip that must bind by column ID (typing `{{...}}` as text will NOT bind, the known Clay gotcha).

### PRIMARY method — clone an existing chip (works even when `/` won't list "Function inputs")
The `/` picker often will NOT offer "Function inputs" inside a Function column. Don't fight it, copy a chip that's already there:
1. Find the existing `vertical:` line: `+ "\nvertical: " + Clay.formatForAIPrompt(` `{{Function inputs}}` `?.["Record"]?.vertical)` (the `{{Function inputs}}` is a colored chip).
2. Select that WHOLE line (chip included), copy it, paste it right below to duplicate.
3. In the duplicate, change only TWO words: label `vertical:` → `source_motion:`, and path tail `.vertical` → `.source_motion`. Leave the `{{Function inputs}}` chip untouched (already bound).
4. Result: `+ "\nsource_motion: " + Clay.formatForAIPrompt(` `{{Function inputs}}` `?.["Record"]?.source_motion)`

### Fallback — `/` picker (only if it actually lists it)
Type `+ "\nsource_motion: " + Clay.formatForAIPrompt(`, then `/` and pick "Function inputs" if offered, then type `?.["Record"]?.source_motion)`.

The 5 chips already in the User Prompt (Subject, Body, Record's Cost Signal Research (AI) / top_signal / vertical) stay as-is. You are only ADDING the one source_motion line. The SYSTEM prompt has ZERO chips (paste verbatim).

## My half — DONE (2026-07-19)
`source_motion` is ALREADY wired into all 12 "Compose Record for critic" nodes across the 4 workflows (Stars 5-touch x5, WFM 5-touch x5, WFM original x1, Cost-Mandate x1), validated, existing Record keys preserved. So when you paste the new prompt, every motion branches correctly on the first run. Nothing pending on my side. You paste the system prompt + the one User-Prompt line, then run the regression test below.

## Regression test (before trusting it)
This gates live sends on 3 motions, so test per motion before relying on it:
- One known-GOOD draft per motion (star_ratings, wfm_adjacency, cost_mandate) → must PASS.
- One known-BAD draft per motion → must FAIL. Especially: a Stars draft that attributes an account-level dollar to a single contract MUST now FAIL.

## Source
Clay AI-column editing flow (Configure tab, Prompt, Run Settings): https://university.clay.com/docs/use-ai-integration-overview
