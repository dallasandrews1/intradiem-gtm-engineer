# One-Time Golden Scaffold Promotion Checklist v1
**Companion to `Clay_Motion_Scaffold_SOP_v1.md`. Do this ONCE to make motions stampable. After this, every new motion is duplicate-and-re-point.**

## The donor decision (a correction — don't promote from Back Office alone)
Back Office is your "one workbook per motion" structural precedent, but it is the **wrong donor for a general golden**, for two concrete reasons from your own build logs:
- **BO inverts the kill switch.** In BO, `customer_flag` is NOT an exclusion (the customer's back office IS the target); `fo_risk_flag` suppresses and `owner_cleared` is the send gate. A new-logo motion (WFM-Adjacency, and anything cite-their-cost) stamped from BO would ship with the *inverted* exclusion logic and leak customers into outreach. That is the exact failure the kill switch exists to prevent.
- **BO's L4 may not be live yet.** Per the Jul 16 L4 build log, BO's MessageGen + `Draft Audit (BO)` critic were authored files-first and "nothing transcribed to Clay yet." A golden with a missing critic column stamps a missing critic into every motion.

So: **two gate archetypes → two goldens.**

| Golden | Donor | Kill switch | Feeds |
|---|---|---|---|
| `__GOLDEN New-Logo Scaffold` | **Cost-Mandate Motion** | standard: `customer_flag==TRUE → exclude` | WFM-Adjacency, any new-logo/cost motion |
| `__GOLDEN Install-Base Scaffold` | **Back Office Motion** | inverted: `fo_risk_flag` suppresses, `owner_cleared` gates | Install-Base expansion, BOO |

**Build the New-Logo golden first** (donor = Cost-Mandate) — WFM-Adjacency is your next motion and needs it. Do the Install-Base golden later, when Install-Base comes up.

Why Cost-Mandate is the right new-logo donor: its L4a MessageGen + L4b critic are built and run live (per the s3 build log), it carries the standard customer-exclusion kill switch, and it is hardened. The universe not fitting is a *sourcing* problem — the *structure* is house-standard, which is all a scaffold needs.

---

## STEP 0 — Confirm live completeness before you duplicate (this decides everything)
Live Clay is ground truth; build logs are not proof (Golden Standard §8, and your own live-state-check law). Sweep the donor workbook (Chrome, or eyes-on) and confirm each L0–L4 piece exists live and house-standard **before** promoting it. A half-built donor makes a half-built golden.

Cost-Mandate Motion — confirm live:
- [ ] **L1 Accounts/Universe:** fit_score/grade, `customer_flag` exclusion wired into `intent_score`/`intent_status`, tier.
- [ ] **L2 Signals:** the Tier-1/Tier-2 signal columns, run-conditioned on eligibility.
- [ ] **L3 Contacts:** persona_match, email waterfall (A → B if-empty → pattern+verify → `email_status`), attribution tags (`gtm_engine_sourced`, `source_motion`, `sourced_date`), `wave_number`/`wave_status`.
- [ ] **L4:** MessageGen (`draft_subject`/`draft_body`) + `msg1_critic` + `tokens_ready` gate, all live columns.
- If any L0–L4 piece is missing live, fix it in the donor first — do not promote around a gap.

> This is the one place a live sweep is worth the time even given the Chrome slowness: you do it once, and it protects every future stamp. Everything downstream is duplication, which never touches the browser at scale.

---

## STEP 1 — Create the golden workbook
- [ ] New workbook: `__GOLDEN New-Logo Scaffold`. (Underscore prefix sorts it to the top and marks it never-launch.)

## STEP 2 — Duplicate the L0–L4 tables from Cost-Mandate, in build order
Order follows the dependency chain (Golden Standard §16) so Lookups resolve as you go. For each: click the table title → **Duplicate table** → then table Actions → **Move table** (verify the current UI label; it has moved before) into `__GOLDEN New-Logo Scaffold`.
1. [ ] **L1 Accounts/Universe** (identity → fit → grade → customer_flag → intent). Signal columns that live *on* this table (the BO pattern puts signal inputs on the universe table) come with it; a separate parent/signals helper table gets duplicated next.
2. [ ] **L2 Signals helper table** — only if signals are a separate table rather than columns on L1.
3. [ ] **L3 Contacts (Buying Committee)** — carries the L4 MessageGen/critic/tokens_ready columns with it, since those live on Contacts.
- [ ] Do NOT duplicate L5 Send Queue, L6 Outreach Sync, L7 Reply/Attribution, L8 Worklist, or the reference tables (Verified Metrics, Product-Angle Map, ICP Rubric, Variant Library). Those are shared, joined by `source_motion` tag + Lookup — never duplicated per motion.

## STEP 3 — Neutralize the copies into a reusable golden
Strip everything motion-specific to a placeholder; leave every column, formula, enrichment, and run-condition intact.
- [ ] Confirm the duplicated tables are **empty of data rows** (Duplicate table copies structure/sources, not rows — this is expected and correct).
- [ ] **Unbind the universe source** — the golden has no universe; each motion loads its own at stamp time.
- [ ] **MessageGen node** → replace the prompt body with `<<MOTION MESSAGEGEN PROMPT — paste per motion>>`.
- [ ] **`source_motion` default** → `<<motion>>` (it stays set-at-creation/read-only once a real motion is stamped).
- [ ] **Number rule / H1 window** → set to the strict default with a `<<number rule per motion>>` marker.
- [ ] **Persona routing formula** → leave it; note the allowed rubric-key set is re-pointed per motion.
- [ ] **Verify the kill switch is the New-Logo archetype:** `customer_flag==TRUE → exclude`, wired inside `intent_score`/`intent_status` AND as a run-condition on every paid column. (From a Cost-Mandate donor this is already correct — confirm it carried.)

## STEP 4 — Run the First-Duplicate Verification once against the golden
From the Scaffold SOP (keyed to the §15 gotchas). Do this once now, on the golden, so the stamp is trusted forever after:
- [ ] Every enrichment column present, config intact (not reverted to blank/agent template).
- [ ] **No Claygent binding** (no "Agent template being used" banner) on any AI column.
- [ ] **No stray campaign/sync column** with Auto-run ON and no run-condition — delete if present.
- [ ] Every **run-condition** carried (eligibility / `customer_flag` / only-run-if-empty).
- [ ] **Optional inputs' "Required to run" = OFF** (esp. `li_recent_post_hook`, disclosed_figure/_source).
- [ ] **Lookups resolve** to the shared reference + L5–L8 tables, not to Cost-Mandate's copies. Spot-check one value returns.
- [ ] **Sender webhook / sync = OFF.**

## STEP 5 — (Later) Repeat once for the Install-Base golden
When Install-Base comes up: same steps, donor = **Back Office Motion**, but first transcribe BO's L4 (MessageGen + `Draft Audit (BO)` critic + `tokens_ready`) to Clay live (the open item from the Jul 16 L4 pack) so the donor is complete. Keep the kill switch **inverted** (`fo_risk_flag` suppresses, `customer_flag` NOT an exclusion, `owner_cleared` send gate).

---

## After this: you're stampable
Per-motion loop (Scaffold SOP): decide the motion → **Duplicate table** the right golden's L0–L4 into a new `<Motion> Motion` workbook → re-point the 5 motion-specific things → fill 5 blanks in the workflow prompt and run it in local Claude Code → runbook gates (10-row slice, credit ledger, Draft + critic PASS + approval, nothing sends). Structure in seconds, no Chrome at scale.
