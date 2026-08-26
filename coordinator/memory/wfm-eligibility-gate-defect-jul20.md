---
name: wfm-eligibility-gate-defect-jul20
description: WFM-Adjacency 5-touch workflow blocker (Jul 20) — the L3 Invoke Workflow column's eligibility-gate inputs are mis-wired AND fn_eligible has the text-vs-boolean customer trap; fix both before the 6 committee contacts can run
metadata:
  type: project
---

Diagnosed Jul 20 2026 (clay-operator, read-only) while clearing the WFM-Adjacency Draft-Audit blocker. Goal: run 6 curated Director+ committee contacts (Elevance: Noemi G., Carlos Doroteo, Donisha Jones, Jessica Sisneros, Melissa Zam; VNS: Linda Reid) through send-readiness to get READY drafts.

**Run surface (decided):** the 5-touch workflow `wf_0tie30io3hiPqSzVRU2` (snapshot `wfs_0tie866CaYwbBJwEfBg`), NOT the single-touch `wf_0tic9xaFeq2rKvMnKuD` (that one is not table-attached and its MessageGen inputs are unbound). The 5-touch validates clean (57 nodes), MessageGen tokens incl. source_motion are correctly bound via compose node `wfn_0tie3ah8nB3zDjNrPUb`, and it's wired to L3 `t_0tic8arWbZp8bSx87Ad` via the `Invoke Workflow` action column `f_0tieeexepsCroV9MtBk`. Table-column MessageGen abandoned (pasted chips don't bind). The old Universe-Lookup domain-mismatch is RESOLVED — all 6 now sit on elevancehealth.com/vnshealth.org, matching L1.

**THE BLOCKER — eligibility gate, two defects (both = the customer_exclude trap):**
1. The `Invoke Workflow` column's Inputs are mis-wired: `"Customer Flag"` → contact Full Name (a string), `"Install Base Lookup BO Universe"` → the raw `Universe Lookup` JSON blob. Any non-null object is truthy, so `fn_eligible` (`t_0tial9rYKzWKU2y9MTC`: `!install_base && customer_flag != true`) computes eligible=FALSE for all 6 and routes every one to EXIT:EXCLUDED before MessageGen. Currently fails CLOSED (blocks work), not open.
2. `fn_eligible` compares against boolean `true` but `customer_flag` is stored as TEXT ("FALSE"/"TRUE") on L1 (`t_0tict25TSXgTgdJgtZZ`, field `customer_flag`=`f_0tict27m8jMKrMoFjFE`). So even once inputs are fixed, a real customer stored "TRUE" reads `"TRUE" != true` = passes = leaks into cold. Harden to `?.["Customer Flag"]?.toUpperCase()?.includes("TRUE")` before this table-attached workflow runs on any un-vetted row.

**Fix (Dallas applies; gate-input change, not Claude's to flip):**
- `"Install Base Lookup BO Universe"` → literal `false` (no real install-base source on L3; honest not-applicable for pre-vetted new-logo; both accounts confirmed customer_flag "FALSE" on real L1 rows).
- `"Customer Flag"` → **CONFIRMED (Jul 20 UI eyeball):** `{{Universe Lookup}}?.record?.["Customer Flag"]`. The matched L1 row nests under `record` (22 fields), keyed by DISPLAY NAME; Customer Flag = text "FALSE" for Elevance. Same `?.record?.["..."]` pattern the Draft Audit node already uses. Insert the Universe Lookup chip via picker (binds by ID), then append the path; do NOT paste as text. Do NOT hardcode Customer Flag=false — table-attached workflow would neuter the customer gate for all future rows.
- Install Base input: CLEAR/empty (unmapped), NOT the text "false" (Clay stores "false" as truthy string → re-breaks the gate). Empty is falsy = correct.
- Universe Lookup record also exposes `New Logo Eligible` (=true here), which already encodes BOTH customer-flag AND install-base exclusion per the L1 formula — the durable fix could key eligibility off that single field instead of two inputs.
- fn_eligible input keys are byte-exact: `"Customer Flag"`, `"Install Base Lookup BO Universe"`.

**BIGGER ROOT CAUSE found Jul 20 (runtime error):** running the Invoke Workflow column errored `path "$.customer_flag" resolved to undefined ... Available keys: [fieldId, tableId, recordId, Customer Flag, asyncCallbackId]`. The column's Inputs JSON keys pass through to the trigger (`wfn_0tie30i7zFvBvRzsfvP`) VERBATIM; the workflow nodes read snake_case `$.customer_flag`, `$.install_base_flag`, and (downstream) `$.company`/`$.first_name`/`$.source_motion`/etc. The Inputs JSON currently carries ONLY "Customer Flag" (Title Case) — so the entire trigger→node mapping is incomplete, not just the gate. This is the "standalone 5-touch graph whose trigger isn't wired to the L3 table" gap. FIX = rebuild the column Inputs JSON with the FULL set of snake_case keys every node reads, each mapped to the right L3 column (clay-operator enumerating). A piecemeal gate fix just moves the undefined error to the next node. The two-input fix in the runbook is SUPERSEDED by the full-mapping fix.

Watch Carlos Doroteo (do_not_mail) + Linda Reid (invalid) — likely fail live email re-verify at `3g. Email verify gate`. L3: 524 rows, 6 READY (only 6 with a Work Email). Nothing sends without explicit go. See [[wfm-adjacency-and-belfield-continuation]], [[clay-functions-build-status]].
