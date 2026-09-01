# WFM Send-Ready Customer-Exclusion Leak — UI Fix Sheet (Aug 6 2026)

Regenerated Aug 6 2026 against the LIVE WFM schema (read-only gate-integrity audit). Supersedes `Gate_Fix_UISheet_Aug3.md`, which is no longer on disk. All IDs below are confirmed from the live workspace, not remembered.

## Status: STOP-THE-LINE, still open
5 Elevance Health contacts (Elevance = active customer since 12/21/2016) sit at `Send Ready = READY` right now. A 6th READY row (VNS Health, not a customer) is exposed by the same gap but is a legitimate target. Do not run any WFM send wave until this sheet is complete and validated on real rows.

## The leaking rows (live, as of Aug 6)
| Full Name | Company (L3) | Domain | Status | Send Ready | Customer? |
|---|---|---|---|---|---|
| Noemi G. | Elevance Health | elevancehealth.com | valid | READY | Customer |
| Carlos Doroteo | Elevance Health | elevancehealth.com | do_not_mail | READY | Customer |
| Donisha Jones | BioPlus Specialty Pharmacy | elevancehealth.com | valid | READY | Customer (domain -> Elevance) |
| Jessica Sisneros | Elevance Health | elevancehealth.com | valid | READY | Customer |
| Melissa Zam | Elevance Health | elevancehealth.com | valid | READY | Customer |
| Linda Reid | VNS Health | vnshealth.org | invalid | READY | Not a customer (leave; legit) |

Three Elevance rows (Noemi, Jessica, Melissa) are `Status: valid` + READY with nothing between them and a cold send. The other two would likely fail email-verify, but that is luck, not a gate.

## Root cause (confirmed on live schema)
- L3 `Send Ready` (`f_0ti9ygfsJv3y8g6Nkcz`) formula is:
  ```
  {{Final Audit Verdict}}?.verdict?.toLowerCase()==="pass" && {{Final Voice Audit}}?.verdict?.toLowerCase()==="pass" ? "READY" : "HOLD"
  ```
  It references no customer field at all. Pure audit-quality gate, not a send-eligibility gate.
- L1 `customer_flag` (`f_0tict27m8jMKrMoFjFE`, static text) stores `"FALSE"` for Elevance Health and for Molina Healthcare, both of which are on Nate's SF customer list. So even a customer-aware formula would miss Elevance until the flag is corrected.

## Exact IDs
- Workbook: `wb_0tic89s5XPjdNKK88He` (WFM-Adjacency Motion)
- L1 table: `t_0tict25TSXgTgdJgtZZ` (WFM_Adjacency_L1_Seed_Enriched_28, 28 rows)
  - `customer_flag`: `f_0tict27m8jMKrMoFjFE` (static text)
- L3 table: `t_0tic8arWbZp8bSx87Ad` (L3, 524 rows)
  - `Send Ready`: `f_0ti9ygfsJv3y8g6Nkcz` (formula)
  - `Universe Lookup`: `f_0ti8uifTiAtoDgVYQTh` (json action; carries `?.record?.customer_flag` from L1)
  - `Final Audit Verdict`: `f_0ti9hp0WEN6VU2hVWsG` | `Final Voice Audit`: `f_0tidtseMQ33YDojtMEd`
  - `Company Domain`: `f_0ti8tdrnCsHVcUNjmh8`

---

## Do this in ORDER. Do not reorder — each step depends on the one before it.

### Step 0 — do not touch the L3 `Send Ready` formula yet
Fixing the formula first would change nothing (the flag it needs to read is still wrong), and could give a false "it's gated now" read. Flag first, formula last.

### Step 1 (Fix 1a) — correct the L1 `customer_flag` values
On L1 (`t_0tict25TSXgTgdJgtZZ`), in the `customer_flag` column (`f_0tict27m8jMKrMoFjFE`):
- Find the **Elevance Health** row -> set the cell to `TRUE`.
- Find the **Molina Healthcare** row -> set the cell to `TRUE`.
This is a static text column, so you edit the cell value directly (double-click the cell, type `TRUE`). [Confirm the exact cell-edit gesture in the current Clay UI.]

### Step 2 — re-run the L3 `Universe Lookup` column so the flag change propagates
L3 reads the flag through the cached `Universe Lookup` blob (`f_0ti8uifTiAtoDgVYQTh`), not from L1 live. After Step 1, re-run that column for the affected rows (or all rows) so the mirrored `customer_flag` updates from `FALSE` to `TRUE`. Use the column header menu -> the run/refresh action. [Confirm the exact menu label ("Run column" / "Run all rows" vary by Clay version) before clicking.]
- Trap: if you skip this, the formula in Step 3 will still read the stale `FALSE` and the leak stays open even though every step "looks" done.
- Verify after re-run: open one Elevance L3 row and confirm `Universe Lookup` now shows `customer_flag` = `TRUE`. If it still shows `FALSE`, stop — the lookup keys on something stale and needs a closer look before proceeding.

### Step 3 (Fix 1b) — add the customer-exclusion term to L3 `Send Ready`
Edit the `Send Ready` formula (`f_0ti9ygfsJv3y8g6Nkcz`) to:
```
{{Final Audit Verdict}}?.verdict?.toLowerCase()==="pass" && {{Final Voice Audit}}?.verdict?.toLowerCase()==="pass" && !({{Universe Lookup}}?.record?.customer_flag?.toLowerCase()?.includes("true")) ? "READY" : "HOLD"
```
- Why `?.toLowerCase()?.includes("true")` and not a boolean check: `customer_flag` is stored as TEXT (`"TRUE"`/`"FALSE"`), so it must be compared as text, case-insensitively. A boolean cast would misfire. This is the exact gotcha that caused the original leak class.
- When you insert `{{Universe Lookup}}`, let the field picker autocomplete the path and confirm it resolves to `...record.customer_flag`. If the picker shows a different nesting, use what it shows, not what is typed here.

### Step 4 — validate on REAL rows before any send (required)
Do NOT treat a synthetic/`--input` pass as proof here; this gate depends on real null-vs-text semantics.
- The 5 Elevance rows must flip `READY` -> `HOLD`.
- VNS Health (Linda Reid) stays `READY` (non-customer, correct).
- Total `READY` across L3 should be at most 1. If any Elevance row is still `READY`, the gate did not take — recheck Step 2's re-run and the formula path in Step 3.

---

## Out of scope for this fix (noted, not folded in)
- L3 has no `human_approved` / `bdr_claimed` / `customer_exclude` field at all — the golden-parity gap flagged Jul 20 / Aug 3. Deliberately not addressed here; this sheet closes the customer leak only.
- Fallback if the `Universe Lookup` mirror proves unreliable: gate `Send Ready` on a direct domain denylist against `Company Domain` (`f_0ti8tdrnCsHVcUNjmh8`) instead of the lookup blob. More robust but heavier to maintain; only reach for it if Step 2 verification fails.
