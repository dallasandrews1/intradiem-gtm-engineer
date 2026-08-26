---
name: wfm-sendready-runbook-jul20
description: RUNBOOK (Jul 20) — exact click-by-click to unblock the WFM-Adjacency 6 committee contacts: fix the eligibility-gate inputs, run the 5-touch workflow, census. Self-contained with all IDs.
metadata:
  type: project
---

# WFM-Adjacency — get the 6 committee contacts to send-ready

Goal: the 6 curated Director+ contacts on L3 produce READY drafts through the 5-touch workflow. Blocker was the eligibility gate mis-wiring (see [[wfm-eligibility-gate-defect-jul20]]). Nothing sends without explicit go.

## IDs (Clay workspace 1180800)
- L3 contacts table: `t_0tic8arWbZp8bSx87Ad`
- Run column: `Invoke Workflow` (`f_0tieeexepsCroV9MtBk`) — calls the 5-touch workflow `wf_0tie30io3hiPqSzVRU2` (snapshot `wfs_0tie866CaYwbBJwEfBg`)
- Eligibility function: `fn_eligible` (`t_0tial9rYKzWKU2y9MTC`)
- L1 accounts table: `t_0tict25TSXgTgdJgtZZ`
- The 6: Noemi G., Carlos Doroteo, Donisha Jones, Jessica Sisneros, Melissa Zam (Elevance); Linda Reid (VNS) — the only 6 rows with `Send Ready = READY` / a Work Email out of 524.

## STEP 1 — Rebuild the FULL trigger Inputs on the `Invoke Workflow` column — FINAL Jul 20
Root cause (proven by runtime error): the column's `Inputs` is a SINGLE JSON box whose keys pass to the trigger VERBATIM (case-sensitive). The 5-touch workflow reads 16 snake_case fields off the Triggers node; the column was passing only "Customer Flag" (Title Case) → `$.customer_flag resolved to undefined`. A piecemeal gate fix just moves the error to the next node. Fix = replace the whole Inputs JSON with all 16 keys in snake_case (field-ID refs = the proven-parsing form in this box):

```json
{
  "company": "{{f_0ti8tdqbxQo5dNucJjc}}",
  "first_name": "{{f_0ti8tdqKabRw8T5JFpv}}",
  "last_name": "{{f_0ti8tdqTvG5rzPcjy83}}",
  "job_title": "{{f_0ti8tdqMAWD2Nmo2ErE}}",
  "company_domain": "{{f_0ti8tdrnCsHVcUNjmh8}}",
  "vertical": "{{f_0tidmindeicfTd44EQY}}",
  "source_motion": "{{f_0ti8tva3CyGc7jD6mzv}}",
  "top_signal": "{{f_0tidsd0oNTfFAC4xjJH}}",
  "signal_evidence": "{{f_0tidmnhjmF66yehE694}}",
  "signal_source_url": "{{f_0tidscy4zfT4AfHBTig}}",
  "signal_source_date": "{{f_0tidscvoqKQNVzfus5i}}",
  "universe": "",
  "customer_flag": "{{f_0ti8uifTiAtoDgVYQTh}}?.record?.customer_flag",
  "install_base_flag": false,
  "bdr_claimed": false,
  "human_approved": false
}
```
System keys fieldId/tableId/recordId/asyncCallbackId are auto-provided (don't add). `install_base_flag`/`bdr_claimed`/`human_approved` are literal `false` (human_approved=false is the built-in dry-run → every row ends HOLD, no send node exists). Flagged: `universe`="" is a safe no-op (formula never reads it); `customer_flag` path best-guess, non-blocking (all 6 are non-customers, pass eligibility regardless) — verify + harden fn_eligible before un-vetted rows.
APPLY: replace the whole box, then TEST ONE ROW (Jessica Sisneros, clean email) — confirm no undefined error + MessageGen personalizes to her — before running the other 5. Concurrency: column was being live-edited Jul 20; confirm no one else is mid-edit.

## STEP 2 — Run the 6
- Filter L3 to `Send Ready = READY` (the 6) or select them by name.
- Run the `Invoke Workflow` column on those rows (per-cell run icon or the column's run-selected control — confirm the label in the current UI).
- Fires the 5-touch workflow per contact: eligibility → persona → email verify → MessageGen E1-E5 → figure-integrity critic → voice audit → send-ready.

## STEP 3 — Census
- Read each draft (E1-E5). The figure/voice critics gate; fix FAILs per-lead.
- Expect **Carlos Doroteo** (stale `do_not_mail`) and **Linda Reid** (stale `invalid`) to hold at the live email-verify gate `3g`; recover Linda's email manually + ZeroBounce if needed.
- Nothing sends. Sender defaults to `{{sender_first_name}}` = Nathan Belfield; confirm before any send.

## FOLLOW-UP (before this table-attached workflow runs on any un-vetted row, not today's blocker)
Harden `fn_eligible` (`t_0tial9rYKzWKU2y9MTC`) for the text flag: change `{{Function inputs}}?.["Customer Flag"] != true` to `!({{Function inputs}}?.["Customer Flag"]?.toString()?.toUpperCase()?.includes("TRUE"))`. Otherwise a future customer stored as text "TRUE" reads `"TRUE" != true` = passes = leaks into cold. Same text-safe pattern L1 Intent Score uses. Alternative durable fix: key eligibility off the L1 `New Logo Eligible` field (via Universe Lookup), which already encodes both customer-flag AND install-base exclusion in one boolean.
