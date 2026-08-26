# Golden Scaffold — Neutralize + Re-point Checklist (LIVE-grounded v1)

**Built from a live column-by-column read of the golden workbook `Golden New-Logo Scaffold` (`wb_0tib7v5msZ2qYbGc4AC`) on 2026-07-17 — not the run sheet.** Supersedes `Golden_Scaffold_Promotion_RunSheet_CostMandate_v1.md` STEP 3–4, which was written before the send-readiness pipeline moved onto the L3 table and is stale about where things live. Where they disagree, this file wins.

Tables in the golden:
- **L1 Accounts/Universe** — Company table, 30 cols, 0 rows (dup of Cost-Mandate Universe x-vert).
- **L3** = `CFO, SVP & VP Operations, VP Finance, COO` — Person table, 51 cols, 0 rows.

Key correction to earlier guidance: **the full send-readiness pipeline is L3 table columns**, not just a workflow. MessageGen, both critics, the gate formulas — all live as columns on L3.

---

## 🔴 A. The one confirmed breakage — fix first
**`Universe Lookup` (L3) still points to the Cost-Mandate workbook.** Live: its referenced table is `wb_0ti8rq156Pp8oNNXcEH / t_0ti7w1ctktQfvRPz3tF` = **Cost-Mandate's** Universe, not the golden's own L1 (`wb_0tib7v5msZ2qYbGc4AC`). This is the run sheet's "#1 silent breakage." Every duplicated lookup does this.

Fix: open `Universe Lookup` → Edit column → re-point the referenced table to **this workbook's L1 Accounts/Universe**. (And every time you stamp a motion off the golden, re-point the new copy's `Universe Lookup` to that motion's own L1.)

---

## B. L3 column inventory (live) and what to do with each

**Motion-specific — must neutralize (golden) / re-point (per stamp):**
| Column | Type (live) | Action |
|---|---|---|
| `MessageGen Email 1 (Cost-Mandate)` | **Use AI column** (Claude Sonnet 5, "Create or modify content" — NOT a Claygent; there's a "Create Claygent" button, so nothing bound to detach). Two parts: a **Prompt** field = per-row token binding (first_name/job_title/company/vertical/workforce_size/persona_key/top_signal/signal_evidence/source_motion), and a **"Provide context for task (System Prompt)"** field = the Cost-Mandate §2 body. | Neutralize: replace the **System Prompt** field with `<<MOTION MESSAGEGEN PROMPT — paste per motion>>`. Leave the token-binding Prompt field alone (generic). Rename the column to drop "(Cost-Mandate)". |
| `Draft Audit` | **Use AI column** (the figure-integrity critic; CM-specific SOURCE FIGURE LAW in its system prompt). | Neutralize: placeholder its system prompt; re-point per motion (paste the motion's §4 critic). Motion-specific. |
| `Source Motion` | Text/formula holding `cost_mandate`. | Neutralize → `<<motion>>`; per stamp → the motion key (`wfm_adjacency`). Read-only once a real motion is stamped. |
| `Universe Lookup` | Lookup (see §A). | Re-point to this workbook's L1. |

**Leave as-is — motion-agnostic / generic (carry over untouched):**
- `Email Voice Audit` — Use AI column, cadence-only critic. Motion-agnostic, do not touch.
- `persona_key` — rubric-key column (its logic is `fn_persona_key`, already carrying the live `wfm` branch). Leave; targeting per motion happens by which keys you source, not by editing this.
- Gate inputs/formulas: `customer_exclude`, `bdr_claimed`, `human_approved`, `msg1_critic Status`, `send_ready`, `draft_clean`, `fn_draft_critic` (shared function col → `t_0tiabaamPvDuEyTxSaF`).
- Email verify: `Work Email`, `Validate Email`, `Status`.
- Identity/attribution: `Company Name`, `First Name`, `Last Name`, `Full Name`, `Job Title`, `Location`, `Company Domain`, `LinkedIn Profile`, `gtm_engine_sourced`, `sourced_date`.

**The ~24 hidden columns (not shown in the default 27/51 view):** these are the enrichment/token data layer — email-waterfall provider steps, `disclosed_figure` / `disclosed_figure_source`, `signal_source_url` / `signal_source_date`, `product_angle`, `vertical`, `top_signal`, `workforce_size`, `draft_subject` / `draft_body`, and the `wave_number` / `wave_status` attribution fields. All generic; they carry over untouched. The **only** action on them: confirm the optional inputs (`li_recent_post_hook`, `disclosed_figure`, `disclosed_figure_source`) have **Required-to-run = OFF** (this is the exact class of setting that blocked nodes in the workflow build). Say the word and I'll enumerate all 24 by exact name and type.

---

## C. L1 Accounts/Universe — neutralize
- **Unbind the universe source** (`US Large Industry Leaders`): the golden holds no universe; each motion loads its own at stamp time.
- Confirm the kill switch carried: `customer_flag == TRUE → exclude`, wired into intent scoring AND as a run-condition on paid columns (correct from a Cost-Mandate donor — confirm it's present).

---

## D. STEP 4 verification (run once on the golden)
- [ ] `Universe Lookup` re-pointed to the golden's L1 (§A) — spot-check it resolves.
- [ ] No AI column shows an "Agent template being used" banner (MessageGen is a plain Use-AI col — clean; check `Draft Audit` / `Email Voice Audit` too).
- [ ] No stray campaign/sync column with Auto-run ON and no run-condition.
- [ ] Optional inputs Required-to-run = OFF (`li_recent_post_hook`, `disclosed_figure`, `disclosed_figure_source`).
- [ ] Sender webhook / sync = OFF.
- [ ] Both tables still 0 rows (structure only).

---

## E. WFM-Adjacency stamp — the re-points (after the golden is clean)
Duplicate the golden's L1 + L3 into a new `WFM-Adjacency Motion` workbook, then re-point exactly these:
1. `Universe Lookup` → the WFM copy's own L1.
2. `MessageGen Email 1` System Prompt → paste **`Clay_MessageGen_SystemPrompt_WFMAdjacency_v1.md` §2** (already written). Rename column to `(WFM-Adjacency)`.
3. `Draft Audit` System Prompt → paste the WFM **§4 critic** (motion-specific FAILs: competitor results, WFM-replaced framing, idle-% stats).
4. `Source Motion` → `wfm_adjacency`.
5. Universe source → the WFM technographic/signal source (Verint/NICE/Calabrio/Genesys/Amazon Connect + RTA/intraday postings).
6. Confirm `persona_key` returns `wfm` for a WFM title (already fixed live).

Leave everything in §B "leave as-is" untouched — that's the reuse payoff.
