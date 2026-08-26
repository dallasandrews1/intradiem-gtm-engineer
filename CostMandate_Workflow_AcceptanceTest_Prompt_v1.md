# Cost-Mandate Send-Readiness Workflow — Acceptance Test Prompt v1

**Paste this into your LOCAL Claude Code / Cursor** (the one with the Clay agent-plugin OAuth-signed into workspace 1180800). This cloud session cannot run it — Clay CLI auth is browser OAuth only.

**Date:** 2026-07-17
**Target:** `wf_0tiane7qgXQ6PH9UdBA` — "Cost-Mandate Send-Readiness (Alpha)". **Already built (22 nodes, validates clean, ends at `send_ready=HOLD`, no send node). DO NOT rebuild it. Read it, then test it.**

---

## Why this test exists (read first — it defines "valid")

The last test was **invalid**. It fed the critic a thin 3-key Record `{Cost Signal Research, top_signal, vertical}`. Clay's **Required-to-run** chips hard-failed the row with **"Some inputs missing"**, so `fn_draft_critic`'s AI node **never ran** — the FAIL/FAIL result was a plumbing error, not a critic judgment. No verdict was ever generated.

So the one rule of a valid test: **every input record must be COMPLETE** — it must populate every field any node in the graph declares as an input. A missing key ≠ a critic FAIL; it's an invalid run. This prompt makes you enumerate the required keys first, then build records that cover all of them.

Do NOT chase verbatim critic reasoning through Enterprise observability / row-read APIs — that path is `auth_forbidden` on this plan and is a dead end. Read the verdict off the workflow test output only.

---

## Step 1 — Enumerate the required-key set (do this before building any input)

1. Read the live workflow: `clay workflows get wf_0tiane7qgXQ6PH9UdBA` (or the read/describe verb the CLI exposes). List its nodes in order and, for each, the Function it calls.
2. For each of the 7 Functions below, read its **declared inputs** (`clay functions list`, then read each). These are the fields that, if absent, trigger "Some inputs missing":
   - `fn_eligible` — t_0tial9rYKzWKU2y9MTC
   - `fn_persona_key` — t_0tiahksb4jmyFfMSQYd
   - `fn_email_verified` — t_0tiajxdwq8Z4zM6hwXw
   - `fn_tokens_ready` — t_0tiako9CBV2yiGnA5r7
   - `fn_draft_clean` — t_0tial35xhuRurytCduv
   - `fn_draft_critic` — t_0tiabaamPvDuEyTxSaF
   - `fn_send_ready` — t_0tiahe2mzsH9CCaC4Sx
3. Produce the **UNION** of every declared input across nodes 1–9 (contact fields + the workflow-owned fields: `signal_source_url`, `signal_source_date`, `signal_evidence`, `number_allowed`, etc.). Print this union as `REQUIRED_KEYS`. Every test record below must set every key in `REQUIRED_KEYS` (empty string only where the scenario explicitly demands a blank, e.g. the known-bad's `signal_source_url`).

If the CLI can't read a Function's inputs, fall back to the blueprint's node table (`CostMandate_Workflow_Alpha_Blueprint_v1.md` §2) as the key list, but say so in the report.

---

## Step 2 — Build 5 COMPLETE real-account records

Use real, in-window right-fit accounts, not synthetic fixtures. Row 1 is fully specified below (locked). For rows 2–5, pull from `CostMandate_RightFit_Batch_v1.md` "NEXT — candidates to verify" (Lumen + screened cost-program accounts) — but only rows whose figure you can tie to a primary source URL dated on/after 2026-04-17. If you can't verify 4 more, run with however many you can (minimum: row 1) and state the count.

Every record sets **all** `REQUIRED_KEYS`. Constants for all 5: `customer_flag=false`, `source_motion="cost_mandate"`, `human_approved=false`, `bdr_claimed=false`.

**Row 1 — Acrisure (LOCKED, Insurance):**
```json
{
  "first_name": "Mark", "last_name": "Wassersug",
  "company": "Acrisure", "company_domain": "acrisure.com",
  "job_title": "Chief Operating Officer",
  "customer_flag": false,
  "disclosed_figure": "2,250 roles (~11%)",
  "disclosed_figure_source": "Insurance Journal",
  "signal_source_url": "https://www.insurancejournal.com/news/national/2026/05/22/871138.htm",
  "signal_source_date": "2026-05-21",
  "signal_evidence": "Acrisure commenced ~2,250 role reductions (~11% of ~19,000), CEO Greg Williams tied it to AI changing how clients expect to be served; phasing into 2027.",
  "top_signal": "public service-workforce cost mandate",
  "product_angle": "",
  "vertical": "insurance",
  "source_motion": "cost_mandate",
  "human_approved": false, "bdr_claimed": false
}
```
Fill any remaining `REQUIRED_KEYS` from Step 1 that aren't shown here (e.g. `persona_key` is computed by node 2, not supplied; do NOT pre-set computed outputs).

---

## Step 3 — Build 1 KNOWN-BAD discriminator record

Same account shape as row 1, **all `REQUIRED_KEYS` populated** (so it clears Required-to-run and actually reaches the critic), EXCEPT:
- `disclosed_figure`: a fabricated, attributed number — `"the 5,000 roles you cut last quarter"`
- `signal_source_url`: `""` (blank)
- `signal_source_date`: `""` (blank)

This must reach node 8 and be **caught there** (sourceless attributed number). If it hard-fails earlier on "Some inputs missing," it's testing the wrong thing — fix its keys and rerun.

---

## Step 4 — Run

```bash
# per record (stdin):
echo '<record-json>' | clay workflows runs test wf_0tiane7qgXQ6PH9UdBA --input -
```
Run all 5 real rows + the 1 known-bad. Capture each run's full node-by-node trace.

---

## Step 5 — Assertions (this is the pass/fail gate)

Print a table: row → last node reached → node-8 `msg1_critic_status` → node-9 `send_ready` → PASS/FAIL.

**A test is VALID only if, for every real row, node 8 returned a real verdict.** Concretely:

1. **No "Some inputs missing" anywhere.** If ANY row (real or bad) reports "Some inputs missing" / "Draft Audit = Some inputs missing" / a Required-to-run error at any node → the run is **INVALID**. Report exactly which node and which declared input was absent from the record, add it to `REQUIRED_KEYS`, and rerun. Do not interpret it as a critic result.
2. **5 real rows — healthy end state:** each reaches node 8 with `msg1_critic_status` = a genuine `PASS` (or a genuine, reasoned `FAIL` — reasoning text present), then node 9 `send_ready = HOLD`. `HOLD` is correct and required (human_approved=false). If any real row ends `READY`, STOP — the human gate leaked.
3. **Known-bad — critic discriminates:** exits at **node 8 with `msg1_critic_status = FAIL`**, never reaching node 9. If it PASSES or reaches send_ready → the critic is rubber-stamping. STOP, report, and tighten `fn_draft_critic` §4 before trusting any PASS.
4. **Dry-run law intact:** confirm no send/sync/campaign node ran and nothing left Clay.

## Step 6 — Report back
- `REQUIRED_KEYS` (the union you enumerated).
- Per-row node-by-node trace + the assertion table.
- One-line verdict: **GREEN** (5 real → HOLD, bad → FAIL at critic, no missing-input errors) or **RED** with the exact failing assertion.
- **Do not** load any campaign, flip any approval, or source the 150–200 universe wave. Those are separate human/credit GOs.

---

### If GREEN, the next moves (do NOT do these in this run)
- Promote the cleanest motion to `__GOLDEN` (Back Office = ratified precedent) via `Golden_Scaffold_Promotion_Checklist_v1.md`.
- Clone-per-motion: swap node 6 (MessageGen prompt) + node 4 number rule; the 7 Function nodes carry over.
- Before cloning to **WFM-Adjacency**: add the `wfm` branch to `fn_persona_key` (declared-not-implemented today → every contact would fall to out_of_icp and HOLD). Before any **install-base** motion: build the inverted `fn_eligible` variant.
