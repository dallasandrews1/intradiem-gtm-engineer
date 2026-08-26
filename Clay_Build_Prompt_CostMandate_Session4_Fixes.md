Cost-Mandate build, session 4 — HARDEN to career-bettable, then fix + regenerate + campaigns + template + close-out
Paste this into a FRESH thread in the Intradiem GTM Engineer project. Live-verified as of 2026-07-16 (session 3). DO NOT re-sweep the session-3 build — this prompt carries the state. Dry-run law holds: nothing sends, nothing launches, no Stars sync touched. This motion's whole hook is "I saw the number YOU disclosed," so the bar is not "does it run" — it is "would you bet your career that every send is true and lands." Build to that bar. Do the HARDENING block first; do not regenerate or send anything until every hardening gate is green.

## Read first (only these)
* `Clay_MessageGen_SystemPrompt_CostMandate_v1.md` (root) — you will EDIT §2 (OPTIONAL PROOF BEAT) + add the source-gate rule.
* `CostMandate_Persona_Sequences_v1.md` (root) — the two campaign lanes.
* Skills to load before touching copy: `intradiem-first-draft-engine`, `intradiem-copy-sharpener`, `intradiem-verified-metrics`, `clay-credit-steward`. Memory `cost-mandate-build-jul16-session3` only if something below seems off.

## Live state — VERIFIED session 3 (trust; don't re-verify)
Workbook `Cost-Mandate Motion` (wb_0ti8rq156Pp8oNNXcEH). Contacts `t_0ti8tdqQAXiWMkx76Jj` = 7 rows (5 clean cost_finance: Selva/Citi, Shanahan/Walmart, Schneider/Abbott, Alagirisamy/Nike, White/J&J; Smits(6) no email + Osborne(7) wrong-company = HOLD). Columns built: `MessageGen Email 1 (Cost-Mandate)` (Sonnet 5, §2 verbatim, 9 chips, subject+body, ran rows 1-5), `Draft Audit` (GPT-4o, §4 verbatim, ran 1-5, ALL FAIL), `msg1_critic Status` formula, `send_ready` formula. All 7 = HOLD (fail-closed WORKS). Credits Usage-authoritative: Cost-Mandate Motion = 51 cr / 52 actions MTD. Kill switch (install-base lookup) correctly zeroes the 4 customers + AmEx.

Why all 5 failed s3: critic OVER-STRICT (false-failed the qualitative frame, workforce count, and non-banned words like "lever"/"walk through"); ONE real catch = unlabeled Humana proof on the 2 healthcare rows.

## ============ BET-YOUR-CAREER HARDENING — do this FIRST, gate everything on it ============

### H1 — Primary-source verification for every number (NON-NEGOTIABLE, the whole ballgame)
The disclosed figures (Citi 300 NY roles, Walmart 306, Nike 1,400, J&J 56) came from the `Cost Signal Research (AI)` Claygent column — LLM prose, never checked against a primary source. The critic can't catch a bad number because it reads the SAME prose. A wrong number about a C-suite prospect's own company kills the motion and reaches Naveen. Before any regen:
1. Add two columns to Contacts: `signal_source_url` and `signal_source_date`.
2. For EACH of the 5 rows, verify the disclosed figure against a real primary source (company press release, 8-K/10-Q, earnings-call transcript, or a named reputable outlet) that states THAT EXACT figure and date. Use Chrome to fetch/search and confirm. Populate url + date. If you cannot confirm the exact number and date from a primary source, mark it UNVERIFIED (leave url blank).
3. Edit the MessageGen §2 system prompt: add a hard rule — "Use a specific dollar/percent/count ONLY if signal_source_url is present AND signal_source_date is within 90 days of today. Otherwise use NO number at all and take the qualitative path (recover idle capacity already on the payroll, no new headcount, no transformation project)."
4. Edit the critic §4: the number gate keys on `signal_source_url` (a real citation), not on Claygent prose. FAIL any number whose row has a blank signal_source_url.
Do NOT send a single numbered draft until this is wired and the 5 sources verified. Any row that can't be sourced ships the qualitative no-number email — still a strong message, zero risk.

### H2 — Prove the critic before you trust it (kills the rubber-stamp)
After Fix 2 the danger is the critic passes everything. Before trusting any real PASS: on a scratch/test row, plant TWO drafts — (a) KNOWN-GOOD (real cited figure, clean copy) and (b) KNOWN-BAD (a fabricated number with an attribution phrase, e.g. "the 5,000 roles you cut last quarter" with NO source_url). Run the critic on both. It MUST return PASS on (a) and FAIL on (b). If it passes (b), it's theater — tighten §4 until it discriminates. Only then run the real 5. Delete the scratch row after.

### H3 — Double-encode guard (nothing malformed can ever sync)
Sonnet double-encoded 2 of 5 rows in s3 (whole JSON dumped into `body`); at 150 rows some corrupt silently. Add formula `draft_clean` = TRUE only if body is non-empty AND does not start with "{" AND does not contain the text `"subject"`. Add `&& {{draft_clean}}` to the `send_ready` formula. Malformed drafts can never reach READY.

### H4 — Deliverability gate
A great email to a dead address is a reputation-damaging bounce. Resolve flags: Shanahan @jet.com (Walmart-legacy — verify it routes or find current address); confirm each of the 5 is ZeroBounce "valid". Make it explicit: only ZB-valid, non-flagged emails go READY. Osborne (wrong company) + Smits (no email) stay HOLD.

### H5 — Filtering-at-scale check (the GTM-Engine bar)
The 10-row slice has Fit=100 for every account, so the Fit/Grade/intent layers have never rejected an in-play account — the filtering you're betting on is unproven. (1) Slice: confirm the layers CAN produce non-max values — they do on the excluded customers/AmEx, so the kill switch works; good. (2) When the real ~150-200 signal-first universe wave runs (separate credit GO — do NOT source it in this session without explicit go), the FIRST job before any send is to verify Fit/Grade/intent actually discriminate: spot-check that borderline accounts get rejected and that each "rif/cost-mandate" signal is REAL (not Claygent dressing a stale layoff — apply H1 to every wave row). Calibrate thresholds on the hard cases. The slice proves the plumbing; the wave proves the filter.

## ============ FIXES (after hardening is wired) ============

### FIX 1 — Humana / product_angle conflict (edit MessageGen §2)
Replace the OPTIONAL PROOF BEAT paragraph with: "Include a proof stat ONLY if product_angle supplies one, used as a one-sentence beat with its 'public' label exactly as passed. If product_angle is empty, make NO proof claim. Never introduce Humana, ROI, capacity-per-agent, or any vertical stat on your own. Never appears in the subject; skip it if the email already has a number." Re-paste edited §2 into the live column via clipboard (navigator.clipboard.writeText + cmd-V; typed newlines get eaten).

### FIX 2 — critic recalibration (edit Draft Audit §4)
(a) Swap Draft Audit off GPT-4o to a stronger reasoning model. (b) Add to the TOP of §4, verbatim: "NEVER FAIL FOR (these are correct): words not literally on the banned list (only exact listed tokens are banned; 'leverage' being banned does NOT ban 'lever'); the qualitative frame 'idle capacity / idle minutes / recovered in real time / recoverable / capacity already on the payroll' (frame, not numbers); the company's own workforce count plainly framed; a number attributed to the company or its disclosure with a timeframe word AND backed by a populated signal_source_url. Only FAIL a number if it lacks a signal_source_url OR appears in neither the sourced figure nor a labeled product_angle stat." Then run H2 to prove it discriminates.

## REGEN
Re-run MessageGen rows 1-5 (right-click → Run 1 cell; watch for double-encode, re-run if body starts with "{"). Re-run Draft Audit 1-5. READ every rendered draft yourself against the "would you send this to this exact COO" bar (not just "does it pass rules"). Confirm `msg1_critic Status` → PASS, `draft_clean` → TRUE, `send_ready` → HOLD (human_approved unchecked = correct; a rep approves later). Any residual FAIL: fix per-row via Run 1 cell; never full re-roll.

## CAMPAIGNS (Dallas already deleted the 2 broken drafts; Clay "New campaign" was erroring — retry; if it still errors, pause and flag, don't loop)
Build TWO native Draft-only campaigns from `CostMandate_Persona_Sequences_v1.md`: "Cost-Mandate (Finance/COO)" (Lane 1) and "Cost-Mandate (Ops)" (Lane 2), 5 touches each. BEFORE pasting any touch, run it through intradiem-first-draft-engine → intradiem-copy-sharpener → intradiem-verified-metrics — do NOT raw-paste the doc; each touch must be send-ready C-suite quality with zero unverified Intradiem claims and the Humana line only if labeled + product_angle-supplied. Sender webhook OFF. Never "Save" a Contacts-sourced campaign. Sync run-condition VERBATIM: `send_ready AND NOT bdr_claimed AND customer_exclude != true AND Source Motion == "cost_mandate" AND &&{{msg1_critic Status}}?.toString()?.toUpperCase()==="PASS"`. Verify 0 leads loaded (all HOLD) = correct end state.

## TEMPLATE STAMP
Duplicate the workbook (menu → Duplicate; fallback = Duplicate table + Move). Strip motion-specific values to placeholders, name `Motion Template (do not edit)`. Save-as-function on the intent rollup formulas. Append the template step to `New_Motion_Build_Runbook.md`.

## CLOSE-OUT
Reconcile `Clay_Credit_Ledger.md` 2026-07-16 rows to the Usage actual (Cost-Mandate = 51 cr / 52 actions MTD; pending→actual, drift note if >25%). Mirror the H1 source-gate, Fix-1 Humana, and Fix-2 critic wording into `config/proof.json` + triggers/registry, or flag as its own task. Memory-checkpoint the session-4 outcome.

## Ratified — do not re-ask
persona_key coo_finance canonical (Clay labels cost_finance/cost_ops). One motion = one workbook. Usage page = only authoritative credit number; no monthly allocation except Stars. Wave discipline per Golden Standard §16. Fail-closed gate is the design — HOLD is correct until a rep approves. The real 150-200 universe wave is a SEPARATE credit GO — do not source it without explicit approval.
