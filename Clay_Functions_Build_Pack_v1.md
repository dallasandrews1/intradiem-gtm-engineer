# Clay Functions Build Pack (v1.0, Jul 16 2026)

**What to extract into Clay Functions, why, and how to build each — grounded in the live column layouts of Stars, Cost-Mandate, and Back Office.** Companion to `Clay_Golden_Standard.md` (Functions are the mechanism that turns its "L5–L8 = SHARED infra, reuse... a copy-paste pattern" into actual centralized logic).

---

## 0. What a Function is, and the one thing to keep straight

A Function is a reusable workflow you build once, that takes defined **inputs**, runs a sequence of steps (formula / enrichment / AI), and returns **outputs** as a single column callable from any table in any workbook. Edit it in an Edit-Mode sandbox, hit **Publish Changes**, and every table referencing it updates at once.

- **Availability:** all paid plans, no extra cost. Build via **Save as function** (multi-select the columns → right-click → Save as function) or **Functions** in the left sidebar → **+ New Function**.
- **Credits:** a Function costs nothing itself; the enrichment/AI actions *inside* it bill exactly as they do today. **So the win is consistency + fix-once maintenance, not credit savings.** Nothing here reduces burn.
- **The doctrine fit:** this is the fix for the "critic/gate/campaign wiring is a copy-paste pattern, not shared infrastructure" line in §1. Functions make it shared infrastructure without violating one-motion-one-workbook.

**Source-of-truth rule for this build:** extract from the **Cost-Mandate** columns, because after session-4 hardening (H1 source-gate, H2 critic discrimination, H3 draft_clean, Fix-1 Humana, Fix-2 critic recalibration) they are the most correct version of the logic you own. Do not extract from the older Stars columns.

---

## 1. Extraction map — what repeats, across which motions

| Logic (live column) | Stars | Cost-Mandate | Back Office | Identical? | Verdict |
|---|---|---|---|---|---|
| Draft critic audit + `msg1_critic Status` | ✔ | ✔ (`Draft Audit`) | ✔ (`Draft Audit (BO)`) | Logic identical; §4 text near-identical | **Function (F1)** |
| `send_ready` gate formula | ✔ | ✔ | ✔ (sync condition) | Identical | **Function (F2)** |
| `draft_clean` malformed-JSON guard (H3) | – | ✔ | (should have) | Identical | **Function (F3)** |
| Email waterfall → ZeroBounce → `email_status` | ✔ (`email_final`) | ✔ | ✔ | Identical chain | **Function (F4)** |
| `persona_key` title→rubric map | ✔ | ✔ | ✔ (+`function`) | Rubric shared; small per-motion tail | **Function (F5), rubric-only** |
| Customer / install-base kill switch | ✔ | ✔ (Install Base Lookup) | ✔ (gates) | Belt-and-suspenders identical | **Function (F6)** |
| `tokens_ready` anti-blank gate | – | (partial) | ✔ | BO-invented, all should adopt | **Function (F7)** |
| MessageGen Email 1 (the prompt itself) | ✔ | ✔ | ✔ | **Prompt text differs by motion** (core position, persona leads, number tokens — §6) | **Do NOT functionalize** — see §4 |
| `fit_score` weights | ✔ | ✔ | ✔ | Weights per-motion | Leave per-motion |

---

## 2. Tier 1 — build now (byte-identical logic, single fix propagates)

### F1 · `fn_draft_critic` — the figure-integrity critic  ★ highest ROI
The one that bit you twice (s3 all-FAIL over-strict, s4 recalibration). As a function you fix §4 **once** and run the H2 discrimination test **once**, and every motion inherits it.

- **Inputs:** `draft_subject`, `draft_body`, `disclosed_figure`, `disclosed_figure_source`, `signal_source_url`, `signal_source_date`, `signal_evidence`, `top_signal`, `product_angle`, `vertical`
- **Internal steps:** (1) AI column, strong reasoning model (not GPT-4o — the s4 swap), §4 verbatim including the Fix-2 "NEVER FAIL FOR" block and the H1 rule that the number gate keys on a populated `signal_source_url`, not Claygent prose. (2) formula parsing the AI verdict → `PASS`/`FAIL`.
- **Outputs:** `msg1_critic_status` (PASS/FAIL), `critic_reason`
- **Bake in H2 permanently:** keep a 2-row test fixture (one known-good cited figure, one fabricated number with an attribution phrase and blank `signal_source_url`) as the function's saved test inputs. Any edit must still PASS good / FAIL bad before Publish. That is the anti-rubber-stamp, enforced structurally.

### F2 · `fn_send_ready` — the single definition of "safe to send"
- **Inputs:** `msg1_critic_status`, `human_approved`, `bdr_claimed`, `customer_exclude`, `draft_clean`, `email_status`, `owner_cleared` (optional, BO only — default TRUE when absent)
- **Output:** `send_ready` (READY/HOLD)
- **Logic:** `critic==PASS AND human_approved AND NOT bdr_claimed AND NOT customer_exclude AND draft_clean AND email_status=="valid" AND owner_cleared`
- **Why one place:** today "send_ready" means slightly different things across motions (BO folds in `owner_cleared`, Cost-Mandate folds in `draft_clean`). One function = one auditable gate definition. Fail-closed stays intact; all rows read HOLD until a rep approves.

### F3 · `fn_draft_clean` — malformed-output guard (H3)
- **Input:** `draft_body`
- **Output:** `draft_clean` (bool) — TRUE only if body non-empty AND does not start with `{` AND does not contain the text `"subject"`
- **Why separate from F2:** it's the guard that catches Sonnet double-encoding (2 of 5 rows in s3; silent corruption at 150 rows). Keeping it its own function makes it independently testable and reusable, then F2 consumes its output.

### F4 · `fn_email_verified` — waterfall + validation
- **Inputs:** `first_name`, `last_name`, `company_domain` (+ full name / LinkedIn optional, Required-to-run OFF)
- **Internal:** provider waterfall with **only-run-if-empty** on each step → `Validate Email · ZeroBounce` → status
- **Outputs:** `email_final`, `email_status`
- **Why:** identical 11-provider chain in every motion and your single biggest credit line — centralizing means the provider order and the only-run-if-empty discipline live in one place. (Still bills per run; the function doesn't change that.)

---

## 3. Tier 2 — build after Tier 1 proves out

### F5 · `fn_persona_key` — title → **rubric** key (rubric-only)
- **Input:** `job_title` → **Output:** `persona_key` ∈ {`coo_finance`,`cc_ops`,`wfm`,`cx`,`bo_claims`,`bo_shared`,`out_of_icp`} (the canonical `ref_ICP_Persona_Rubric.csv`)
- **Hard caveat:** the function returns the **rubric key only**. Keep each motion's label layer (`cost_finance`/`cost_ops`, `stars_quality`, BO's `function`) as a **separate thin formula** in that workbook — do NOT pull motion labels into the function, or you re-introduce the drift the rubric exists to kill.

### F6 · `fn_eligible` — customer / install-base kill switch
- **Inputs:** `company_domain`, `customer_flag` (manual) → **Outputs:** `eligible` (bool), `exclusion_reason`
- **Internal:** Lookup against the install-base universe (Record Found → exclude) **OR** manual `customer_flag` (belt-and-suspenders, per §4).
- **Wire `eligible` into every paid signal run-condition and into `intent_score`/`intent_status`.** Verify cross-workbook reachability of the lookup in the live UI first (§0 warns cross-workbook lookups sometimes need a seeded copy; a Function input can point at the reference table to sidestep it).

### F7 · `fn_tokens_ready` — anti-blank gate (adopt BO's invention everywhere)
- **Inputs:** `first_name`, `job_title`, `company`, `persona_key`, `email_status`, `source_motion`
- **Output:** `tokens_ready` (bool) — TRUE only when all required tokens non-empty, `persona_key≠out_of_icp`, `email_status==valid`, `source_motion` matches expected
- **Why:** makes MessageGen structurally unable to fire on an incomplete row — the fix for the Jul-15 snake_case wipe. Every motion should gate MessageGen on this.

---

## 4. Do NOT functionalize (and what to do instead)

- **MessageGen Email 1.** Golden Standard §6 is explicit: the prompt text, persona lead structures, and number tokens are **per-motion**. A single MessageGen function would freeze one motion's core position across all of them — exactly wrong. Keep the AI column per workbook.
  - *Instead:* manage the **shared** parts (the §8 copy house-style, §6 number discipline, output format) as a reusable **prompt block** you paste into each motion's §2 — a documentation practice, not a Clay Function. If you ever want it enforced structurally, it belongs in `fn_draft_critic` (F1), which already audits every one of those rules post-hoc.
- **`fit_score`.** Weights are per-motion; no shared logic to extract. Leave it.

---

## 5. Build order (step-by-step, current Clay UI)

Verify each screen live before clicking — Clay's UI moves (§0). Dry-run law holds: nothing sends; `send_ready` stays HOLD throughout.

**Phase A — extract F1–F4 from Cost-Mandate (the hardened source):**
1. Open the **Cost-Mandate Motion** contacts table (`t_0ti8tdqQAXiWMkx76Jj`).
2. For F1: Cmd-click the header of `Draft Audit` **and** `msg1_critic Status` → right-click → **Save as function**.
3. In the dialog: name `fn_draft_critic`; set **inputs** = the values that change per table (the draft + source fields in §2 above); set **outputs** = `msg1_critic_status`, `critic_reason`. Leave "Replace columns with function" **unchecked** on the first build (keep the originals until the function is proven). → **Create**.
4. Repeat for F2 (`send_ready` formula), F3 (`draft_clean` formula), F4 (the Work Email waterfall + ZeroBounce columns — multi-select the whole chain).
5. Open **Functions** in the sidebar → for `fn_draft_critic` click **Edit function** → **Add test inputs** → paste the two H2 fixtures (known-good / known-bad) → confirm PASS / FAIL → **Review Changes** → **Publish Changes**.

**Phase B — call them from Back Office and Stars:**
6. Open **BO_Contacts** → **Tools** → under **Functions** pick `fn_draft_critic` → map its inputs to BO's columns (`MessageGen Email 1 (BO)` → draft, BO's disclosed/source fields, etc.) → run on a slice, verify outputs in the background mini-table before wiring anything downstream.
7. Point BO's sync run-condition at the function's `msg1_critic_status` output. Repeat F2–F4. Then do the same on the Stars contacts table.
8. Once a function is proven live in ≥2 motions, go back and re-run its **Save as function** source with "Replace columns with function" if you want the originals collapsed — optional, cosmetic.

**Phase C — Tier 2 (F5–F7):** same pattern; build F6's lookup with cross-workbook reachability verified first (§0).

**Gate before relying on any of this:** prove F1 on a 10-row slice per motion, confirm the H2 fixtures still discriminate after Publish, and confirm `send_ready` still reads HOLD everywhere. A function that silently passes is worse than the copy-paste it replaced.

---

## 6. Definition of done
`fn_draft_critic`, `fn_send_ready`, `fn_draft_clean`, `fn_email_verified` published and called from Cost-Mandate, Back Office, and Stars; the critic's H2 fixtures saved as its test inputs and green; one auditable definition of "send-ready" across all motions; nothing sent. Tier 2 (`fn_persona_key` rubric-only, `fn_eligible`, `fn_tokens_ready`) follows once Tier 1 is proven on a slice.
