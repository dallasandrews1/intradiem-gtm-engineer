# Stars QBP Wave 2 — Work-Laptop Handoff README

Pick up the Stars wave-2 5-touch engine where the personal-laptop session left off and finish the launch. Read this top to bottom before touching anything.

## 0. WHERE TO RUN THIS

**Run in VS Code Claude Code (the extension), authed with your Intradiem Claude Enterprise account. NOT Cowork.**

**Model: Opus 4.8 (1M context).** This is Clay workflow surgery with send-gate stakes. `/fast` is fine (still Opus). Don't run the workflow reasoning on Sonnet/Haiku; Sonnet is fine only for the `clay-operator` subagent doing mechanical node edits.

Why not Cowork: this uses the local Clay MCP plugin (`plugin:clay:clay`), the `clay` CLI, and the file-based memory + CLAUDE.md. Cowork has none of those. Do AI work in VS Code Claude Code; do table/sequencer clicks in the Clay web app.

### Prereqs on the work laptop (see also `~/coordinator/WORK_MACBOOK_SETUP.md`)
1. Copy the **coordinator** folder (memory/ + CLAUDE.md + .claude/skills/) and mirror CLAUDE.md + skills globally.
2. Copy this **Intradiem GTM Engineer** project folder (need `04-value-repository/Intradiem_Value_Repository.md`).
3. `clay login` → pick **Intradiem workspace 1180800**. Verify `clay whoami`.
4. Auth Claude Code with the **Intradiem Enterprise** account. Skip Mem0 (compliance hold).
5. Note: tables/columns API is Enterprise-observability-gated and is OFF on this login (`clay tables rows/columns` returns empty/forbidden). `clay workflows` (get/runs/snapshots), `edit_node`, `read`, `validate_workflow`, `surfaces_read/edit_trigger`, and the `table` query tool all WORK. So row/column checks happen in the Clay UI, not via CLI.

## 1. WHAT THIS IS
A full 5-touch (E1–E5) cold email engine for the Star Ratings motion. A contact goes into the Contacts table, the **Invoke Workflow** column runs the workflow per row and writes all 5 emails into WF Msg1–5, a table **Wave 2 Audit** column gates them, and a sequence sends them through Nathan's inbox in Draft.

- **Workflow:** `wf_0tiegzuo3PzJ4UtUGFA` — "Star Ratings 5-Touch Send-Readiness (Alpha)"
- **Contacts table:** `t_0thtm73HHxyiupTuepK`
- **Accounts (Master):** `t_0thuumoUcu6wAAhovti`
- **Value Repository:** `04-value-repository/Intradiem_Value_Repository.md`
- Wave-2 universe = **24 rows**: 15 `stars_quality` (P1) + 9 `coo_finance` (P2), all `wave_number=2`, all non-customers.

## 2. CURRENT STATE (Jul 20 PM)

**Engine CONFIRMED working end-to-end** — a full run assembles all 5 emails (`bodies=5/5`). The blank-WF-Msg problem is solved.

**Architecture = purely LINEAR single-incoming spine** (this shape is load-bearing, do NOT reintroduce joins):
`MsgGen E1 → Voice Fix E1 → Capture E1 → MsgGen E2 → Voice Fix E2 → Capture E2 → … → Voice Fix E5 → Capture E5 → Assemble`.
Each `Capture En` code node reads its Voice Fix immediately (`get_input("structuredOutputs")["revised_body"]`) and emits `msgN_subject/body`; `Assemble` (`wfn_0tihrbzCRBsMN9U26KF`) is single-incoming off Capture E5 and gathers all 5 by distant `sourceNodeId` ref. Three Clay quirks forced this (all in `coordinator/memory/clay-workflow-execution-gotchas-jul20.md` rules 7–9): distant agent-`structuredOutputs` reads return empty; code nodes read RAW upstream keys not renamed schema keys; and multi-incoming JOIN nodes never fire.

**Content fixes applied Jul 20 PM:**
- E1 got a "WHY THIS CONTRACT" rule (names the example contract with a defensible reason, no invented ranking).
- **Proof-line variety fix** (the reason the audit was HOLDing): each touch now hard-assigns a DISTINCT proof so the prospect never sees the same one twice — E1 = Humana "first-year in-year return", E3 = **UHC $190M** (its designed proof, no Humana line), E4 = Humana "two hours capacity/agent", E5 = Humana "table stakes". E2 = none (light).

**The audit works.** The `Wave 2 Audit` table column caught the proof-line repetition correctly (not a false alarm). It needs the tightened prompt in §4 so it stops HOLDing on *borderline* cases while keeping every real catch.

## 3. ⚠️ CRITICAL: RE-PIN THE TRIGGER AFTER EVERY WORKFLOW EDIT

The Invoke Workflow column fires a **`clay_table` trigger** that runs a **pinned workflow SNAPSHOT**, NOT the live draft. `clay workflows runs test` runs the draft; the COLUMN runs the pinned snapshot. So after ANY `edit_node` change, the column keeps running the OLD graph until you re-pin. (This is what caused the "failed to run" / "HOLD on a deleted node" errors.)

**Also: a `clay_table` trigger will NOT dispatch with `snapshotId:"latest"` — the cell shows "failed to run" with no reason. You MUST pin a CONCRETE snapshot id.**

**Re-pin procedure (do this as the LAST step after any workflow edit, before running the column):**
1. `clay workflows snapshots list wf_0tiegzuo3PzJ4UtUGFA` → grab the newest `id` (top of the list).
2. `surfaces_edit_trigger` with `resourceId: 6c999a95-8ec4-4c5f-8b01-677425d551dc`, `trigger.snapshotId: <that newest snapshot id>`.
3. Verify with `surfaces_read` (trigger) → `snapshotId` = the id you set, `status` = `live`.

Trigger id: `6c999a95-8ec4-4c5f-8b01-677425d551dc` · table `t_0thtm73HHxyiupTuepK` · field `f_0tihfhlVMZAjmcWgejt`.

## 4. THE WAVE 2 AUDIT COLUMN (the send gate, on the table)

One AI column, `Wave 2 Audit`, reads WF Msg1–5 and returns `READY` / `HOLD: <reason>`. It replaces the figure+voice critics that were pulled out of the workflow (removing them is what made runs finish). Build: AI/"Use AI" text column, Claude model, single plain-text output, insert each `WF Msg…` via the `/` picker so it binds by ID.

**TIGHTENED PROMPT (re-paste this over the current one — it stops the all-HOLD by defaulting to PASS and dropping mechanical comma-counting, while keeping the figure gate and the repetition catch):**

```
You are the pre-send audit for a 5-touch Star Ratings cold email sequence. You get all 5 emails (subject + body). Default to PASS. Return READY unless you can quote the exact offending words AND name a specific rule written below. Do NOT invent rules that are not written here. A borderline case is a PASS. A blank or missing email is a HOLD. Output nothing but the verdict line.

CHECK 1 - FIGURE INTEGRITY (verified-claims gate)
- Every dollar figure must read as an ESTIMATED forgone Quality Bonus Payment figure from public CMS data, scoped to the PAYER (across its contracts).
- PAYER-scoped dollars PASS. Phrasings like "across [company]'s N contracts", "the N contracts near the bonus line", or "[company]-wide" are PAYER-scoped, NOT a subset, treat them as correct. If you are unsure whether "N contracts" is the payer's full set, PASS.
- ONLY a dollar tied to a SINGLE named contract ID is a HOLD: "$Xm on H2775", "H2775's $Xm", "$Xm for H2775". Naming one contract as the example whose breakdown is offered is fine; attaching a dollar to that one contract is the HOLD.
- It is EXPLICITLY PERMITTED to name one example contract (e.g. H2923, H8889) in the SAME email as a payer-scoped dollar ("across [company]'s N contracts ... $Xm"). This is the intended design, not a violation. Do NOT HOLD, hesitate, or "reconsider" on a named example contract sitting near a payer-scoped dollar.
- Any fabricated, rounded-up, or unsourced number is a HOLD. Snake_case token names (cs_star etc.) in the copy are a HOLD.
- PRODUCT CAPABILITY vs CUSTOMER CLAIM (do NOT confuse these):
  * Describing what Intradiem's PRODUCT does is ALWAYS PERMITTED and is NOT a customer claim. These MUST PASS: "teams use Intradiem to move several service and CAHPS measures at once in real time", "a platform that reads real-time signals across the contact center and acts on them". Never HOLD a product-capability description.
  * A specific named-CUSTOMER RESULT, METRIC, or ROI figure is restricted. The ONLY permitted ones are these six Humana lines, VERBATIM (exact number, keep "working with us"/"bringing us in", say "dynamic workforce orchestration" not "automation"/"products"):
    1. Humana's freed up about two hours of capacity per agent every month working with us.
    2. Five years in, Humana's seen a 7X ROI working with us.
    3. Humana ran 2.7 million automated actions across their contact center last year working with us.
    4. Humana's own team calls our dynamic workforce orchestration system table stakes now, not a nice-to-have.
    5. Humana got a first-year, in-year return after bringing us in back in 2020.
    6. Humana cut average handle time by 45 seconds working with us.
    A Humana line with a changed number/wording, or ANY other named-customer result figure, is a HOLD.
- The UnitedHealthcare $190M line is permitted ONLY as a historical stakes figure (UHC's own stated figure, prior rules), never as an Intradiem-caused result.
- CLINICAL/HEDIS: CAHPS measures are customer-EXPERIENCE / service-side Star measures that Intradiem DOES move; they are NOT clinical or HEDIS. "Intradiem moves service and CAHPS measures" is CORRECT and permitted. ONLY an explicit claim that Intradiem moves a CLINICAL or HEDIS measure (blood-pressure control, diabetes care, medication adherence, a named HEDIS measure) is a HOLD.

CHECK 2 - VOICE (AI tells)
- EXEMPTION: the six permitted Humana lines and the UHC $190M stakes line are pre-approved as written. Do NOT apply any voice rule (false-contrast, banned words, stacking) to those exact sentences, even when a line like "table stakes now, not a nice-to-have" contains an "X, not Y" shape. Apply the voice checks only to the rest of the copy.
- Any em dash is a HOLD. Uncontracted "I would/I am/you will/that is" is a HOLD. False-contrast ("not X, it's Y" / "X, not Y") is a HOLD.
- Stacking (a sentence that crams 3+ distinct facts with no connective words like because/so/which/though) is a HOLD. Do NOT count commas mechanically. A run of 3+ short flat sentences in a row is a HOLD.
- Banned words are a HOLD: agentic, seamless, transform, leverage, synergy, streamline, alignment, game-changer, journey, unlock, empower, revolutionize, "I'd love to", "happy to", "excited", "circle back", "deep dive", "touch base", "pick your brain", "trade notes", "compare notes".

CHECK 3 - PROOF PLACEMENT & VARIETY
- E1: one Humana line. E2: NO proof line. E3: the UHC $190M stakes line (no Humana line). E4: one Humana line. E5: one Humana line.
- The proof line in E1, E4, and E5 must each be a DIFFERENT Humana line. If the same Humana line (or same proof sentence) appears in more than one email, that is a HOLD (repetition tell).
- A missing required proof line, a proof line on E2, or two proof lines in one email is a HOLD.

OUTPUT: Decide silently, then output your ENTIRE response as EXACTLY one of these, first character onward, with no other text:
READY
or
HOLD: <one short sentence naming the email and quoting the offending words>
Never narrate your checks. Never write "checking", "re-examining", or any reasoning in the response. Never self-correct in the output. Verdict only. If your silent check talks you OUT of a HOLD (you find yourself writing "reconsider", "re-evaluating", "permitted", or "no clear HOLD exists"), the answer is READY. Output READY. Never print "HOLD:" followed by reasoning that concludes there is no violation.

THE FIVE EMAILS:
E1 subject: [insert WF Msg1 Subject]
E1 body: [insert WF Msg1 Body]
E2 subject: [insert WF Msg2 Subject]
E2 body: [insert WF Msg2 Body]
E3 subject: [insert WF Msg3 Subject]
E3 body: [insert WF Msg3 Body]
E4 subject: [insert WF Msg4 Subject]
E4 body: [insert WF Msg4 Body]
E5 subject: [insert WF Msg5 Subject]
E5 body: [insert WF Msg5 Body]
```

## 5. EXACT NEXT STEPS (in order)

**A. Re-pin the trigger** to the newest snapshot (§3). ✅ DONE: trigger is pinned to `wfs_0tii2yiXHW8QyaN4yoT` — the fully-fixed version: distinct proof lines, no dollar-repetition, EMAIL SPACING (paragraph breaks), MANDATORY proof line, payer-scoped dollars, and NO STAT REPETITION (E2–E5 reference the gap conceptually instead of restating E1's exact "X.X under 4.0" star stat). Verified on a live row: E1 owns the star/dollar setup, E2–E5 drop the repeated stat but stay substantive (still name the contract, keep proofs + spacing). Only redo the pin if you make further workflow edits. Verify with `surfaces_read` trigger → snapshotId should be `wfs_0tii2yiXHW8QyaN4yoT` (or newer).

**B. Confirm one row.** Re-run the Invoke Workflow cell on one Centene/Devoted row (~10 min). Read E1–E5 and confirm 4 DISTINCT proofs (E1 Humana in-year-return, E3 UHC $190M, E4 Humana capacity, E5 Humana table-stakes; E2 none). Re-paste the tightened audit prompt (§4) and confirm that row now returns READY (or a legitimate, quotable HOLD).

**C. Batch the 24.** Run the Invoke Workflow column on all 24 wave-2 rows. ~40% of runs hit Clay's random agent hang; re-run those cells (Clay redoes only the failed cell). Done when every row has all 10 WF Msg fields and a Wave 2 Audit verdict. Read the HOLD reasons; spot-check a few READYs against the actual emails to confirm the audit is calibrated.

**D. Fix the sync condition (safety).** The Wave 2 Audit is ADVISORY (an LLM audit rambles and can't be a reliable machine gate), so the audit clause is DROPPED from the sync. The deterministic gates carry the machine safety; the figure gate is enforced by reading the audit flags in Draft. Corrected P1 (fail-closed on customer):
```
{{customer_exclude}}?.toString()?.toUpperCase()=="FALSE" && {{Persona Key}}=="stars_quality" && {{wave_number}}?.toString()=="2"
```
P2 = same with `{{Persona Key}}=="coo_finance"` → the P2 sequence.

**E. Build P1 + P2 sequences.** 5 steps each, step N pulls `WF MsgN Subject/Body`, sender Nathan, campaign stays **Draft**. P1 = 15 `stars_quality`, P2 = 9 `coo_finance`. Don't guess the sequencer UI — show the step editor to Claude and get exact clicks.

**F. Validate the customer gate on REAL rows.** Before enabling either sync, confirm on the actual 24 rows that every non-customer passes and no customer leaks (`customer_exclude` is text; null-vs-"FALSE" is where a leak hides; never validate on synthetic input). The `gate-integrity-auditor` agent does this.

**G. Review in Draft → launch.** You read the batch in Draft and launch. Nothing auto-sends before that.

**Hard ordering rule:** the audit gate (§4) and the customer-gate validation (F) must both clear before you enable a sync or launch. Sequence-building (E) can run in parallel since it stays in Draft.

## 6. KEY IDS
- Workflow `wf_0tiegzuo3PzJ4UtUGFA` · Trigger `6c999a95-8ec4-4c5f-8b01-677425d551dc` · Contacts `t_0thtm73HHxyiupTuepK` · Invoke-field `f_0tihfhlVMZAjmcWgejt`
- Assemble (terminal) `wfn_0tihrbzCRBsMN9U26KF` · Captures E1–E5 `wfn_0tihrlsaRcYsJDeGfb4` / `wfn_0tihrlvUSbZMkd49tEm` / `wfn_0tihrm0zGXAb62FUrFe` / `wfn_0tihrm4CeF3kb5z6BZK` / `wfn_0tihrm8sdQSYyZGfhFU`
- MessageGen E1–E5 `wfn_0tiehe8J6zEXqoGKnGV` / `wfn_0tiehwcEeQthi2Yt2yy` / `wfn_0tiei0jyJuTqKPtrjzT` / `wfn_0tiei41w6ds8kKjs74S` / `wfn_0tiei7eTKfUdXe76BVJ`
- Voice Fix E1–E5 `wfn_0tigswnfnCnyxXAXKow` / `wfn_0tigt20dkAoEw6sdDF6` / `wfn_0tigt2ayVRBMpsgz5xz` / `wfn_0tigt2kgHEsiVCnt2ui` / `wfn_0tigt2uRrgzgkQSn7sA`
- fn_draft_critic `t_0tiabaamPvDuEyTxSaF` · fn_tokens_ready `t_0tiako9CBV2yiGnA5r7`

## 7. READ THESE MEMORY FILES FIRST
In `coordinator/memory/`:
- `clay-workflow-execution-gotchas-jul20.md` — rules 1–9. Rules 7/8/9 (distant-read, join-never-fires, trigger-snapshot-pin) are the ones that cost the most time. **Read before touching the graph.**
- `stars-5touch-engine-live-state-jul20.md` — engine live state.
- `proof-lines-attribute-to-intradiem.md` — proof lines attribute results to us; DWO not "automation"/"products"; UHC $190M is stakes, not an us-win.
- `verify-dont-theorize.md` — get ground truth from the tool before proposing a fix.

## 8. COPY-PASTE RESUME PROMPT (paste to Claude Code on the work laptop)
> Read `STARS_WAVE2_HANDOFF_README.md` and `coordinator/memory/MEMORY.md`. Confirm `wf_0tiegzuo3PzJ4UtUGFA` validates, and check whether the trigger `6c999a95-8ec4-4c5f-8b01-677425d551dc` is pinned to the newest snapshot (re-pin per §3 if not). Then walk me through Steps A–G for the Stars QBP Wave 2 launch, starting with a one-row confirm of the four distinct proof lines and the tightened Wave 2 Audit. Do the AI-buildable parts; give me click-by-click UI sheets for anything needing my hands in Clay. Re-pin the trigger after any workflow edit. Never flip a send gate.
