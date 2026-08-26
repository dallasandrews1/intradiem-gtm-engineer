# Golden Scaffold Promotion — Run Sheet: Cost-Mandate → `__GOLDEN New-Logo Scaffold` v1
**Executable companion to `Golden_Scaffold_Promotion_Checklist_v1.md` and `Clay_Motion_Scaffold_SOP_v1.md`. Do this ONCE. After it, every new-logo motion is duplicate-and-re-point.**

Generated 2026-07-17 after the Cost-Mandate Send-Readiness workflow (`wf_0tiane7qgXQ6PH9UdBA`) went complete + running end-to-end. This is the moment to promote: the donor's logic is proven live.

---

## What this produces
The **New-Logo golden** (`__GOLDEN New-Logo Scaffold`), donor = Cost-Mandate. Standard kill switch (`customer_flag==TRUE → exclude`). Feeds WFM-Adjacency and any future new-logo/cost motion. The Install-Base golden (donor = Back Office, inverted gate) is a **separate, later** promotion — do not use this one for Install-Base/BOO.

## Where this runs
Clay UI (Chrome), by you. Clay has **no create-table API** — `Duplicate table` is a manual UI action; no agent, MCP, or CLI can do it. This sheet is the click-by-click. Nothing here sends, launches, or flips a gate — it's structure only.

---

## STEP 0 — Certify the Cost-Mandate donor is live-complete
Live Clay is ground truth. A half-built donor stamps a half-built golden into every future motion.

**Already verified from here (2026-07-17, via Clay MCP) — no action needed:**
- [x] All 7 shared Functions live and resolving: `fn_eligible`, `fn_persona_key`, `fn_email_verified`, `fn_tokens_ready`, `fn_draft_clean`, `fn_draft_critic`, `fn_send_ready`.
- [x] `fn_send_ready` ANDs the full gate (Msg1 Critic Status, Human Approved, Bdr Claimed, Customer Exclude, Draft Clean, Email Status).
- [x] Workflow `wf_0tiane7qgXQ6PH9UdBA` runs end-to-end (nodes 1→9), which proves every L1–L4 column the pipeline reads exists and resolves live.

**You confirm in the UI (eyes-on the Cost-Mandate Motion workbook) — the table structure the workflow doesn't directly exercise:**
- [ ] **L1 Accounts/Universe:** `fit_score`/grade present; `customer_flag` exclusion wired into `intent_score`/`intent_status`; tier column present.
- [ ] **L2 Signals:** the 4 cost-signal columns (efficiency_mandate / RIF / margin / hiring-freeze) present, run-conditioned on eligibility.
- [ ] **L3 Contacts:** persona_match; email waterfall (A → B if-empty → pattern+verify → `email_status`); attribution tags (`gtm_engine_sourced`, `source_motion`, `sourced_date`); `wave_number`/`wave_status`.
- [ ] **L4:** `draft_subject`/`draft_body` (MessageGen), `msg1_critic`, `tokens_ready` gate — all present as live columns.
- [ ] If ANY L0–L4 piece is missing/blank-config live → fix it in the Cost-Mandate donor FIRST. Do not promote around a gap.

---

## STEP 1 — Create the golden workbook
- [ ] New workbook: **`__GOLDEN New-Logo Scaffold`** (underscore prefix sorts it to top and marks it never-launch).

## STEP 2 — Duplicate L1–L3 from Cost-Mandate, in dependency order
For each: click the table title (top-left) → **Duplicate table** → then table Actions → **Move table** (verify current UI label) into `__GOLDEN New-Logo Scaffold`.
1. [ ] **L1 Accounts/Universe** (identity → fit → grade → `customer_flag` → intent). Signal columns that live *on* this table come with it.
2. [ ] **L2 Signals helper table** — only if signals are a separate table rather than columns on L1.
3. [ ] **L3 Contacts (Buying Committee)** — carries the L4 MessageGen/critic/`tokens_ready` columns with it (they live on Contacts).
- [ ] **Do NOT duplicate** L5 Send Queue, L6 Outreach Sync, L7 Reply/Attribution, L8 Worklist, or the reference tables (Verified Metrics, Product-Angle Map, ICP Rubric, Variant Library). Those are shared, joined by `source_motion` + Lookup — never duplicated per motion.

## STEP 3 — Neutralize the copies into a reusable golden
Strip everything motion-specific to a placeholder; leave every column, formula, enrichment, and run-condition intact.
- [ ] Confirm duplicated tables are **empty of data rows** (expected — Duplicate copies structure/sources, not rows).
- [ ] **Unbind the universe source** — the golden has no universe; each motion loads its own at stamp time.
- [ ] **MessageGen node** → replace prompt body with `<<MOTION MESSAGEGEN PROMPT — paste per motion>>`.
- [ ] **`source_motion` default** → `<<motion>>` (read-only once a real motion is stamped).
- [ ] **Number rule / H1 window** → strict default with a `<<number rule per motion>>` marker.
- [ ] **Persona routing formula** → leave intact; the allowed rubric-key set is re-pointed per motion.
- [ ] **Confirm kill switch = New-Logo archetype:** `customer_flag==TRUE → exclude`, wired inside `intent_score`/`intent_status` AND as a run-condition on every paid column. (From a Cost-Mandate donor this is already correct — confirm it carried.)

## STEP 4 — First-Duplicate Verification (run ONCE now, on the golden)
Do this once so the stamp is trusted forever after.
- [ ] Every enrichment column present, config intact (not reverted to blank/agent template).
- [ ] **No Claygent binding** — no "Agent template being used" banner on any AI column. If present, click the x to detach.
- [ ] **No stray campaign/sync column** with Auto-run ON and no run-condition — delete if present.
- [ ] Every **run-condition** carried (eligibility / `customer_flag` / only-run-if-empty).
- [ ] **Optional inputs' "Required to run" = OFF** (esp. `li_recent_post_hook`, `disclosed_figure`/`_source`). ← this is the exact class of bug that blocked node 4 and node 6 in the workflow build; don't let it re-enter via the golden.
- [ ] **Lookups resolve** to the shared reference + L5–L8 tables, NOT to Cost-Mandate's copies (the #1 silent breakage). Spot-check one value returns.
- [ ] **Sender webhook / sync = OFF.**

---

## Done → you're stampable
Per-motion loop from here: `Duplicate table` the golden's L1–L3 into a new `<Motion> Motion` workbook → re-point the 5 motion-specific things → fill 5 blanks in the workflow prompt and run it in local Claude Code → runbook gates. Structure in seconds, no Chrome at scale.

**First stamp: WFM-Adjacency** — see `WFM_Adjacency_Clone_Pack_v1.md` (has a confirmed hard pre-req: `fn_persona_key` needs a `wfm` branch before the clone will route anyone).
