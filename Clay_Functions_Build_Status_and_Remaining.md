# Clay Functions — Build Status & Remaining Steps (Jul 16 2026)

Live build session in workspace 1180800. What follows is the honest state and exact steps for what's left.

## Built live and published (3 of 7)

| Function | Source | State | Notes |
|---|---|---|---|
| **fn_draft_critic** | Cost-Mandate `Draft Audit` | LIVE, recalibrated | Model swapped GPT-4o → **Claude Sonnet 5** and published (cost unchanged ~1 cr/row). Prompt left as-is — it was already the hardened §4 with the full "DO NOT FAIL for" calibration block, so the fix was the model, not the rules. Inputs: Subject, Body, Record, Top Signal, Vertical. Output field is cosmetically named "Trim" (Clay auto-name; not click-editable — rename in Edit Mode later). 0 sources wired. |
| **fn_send_ready** | Cost-Mandate `send_ready` | LIVE | Inputs: Msg 1 Critic Status, Human Approved, Bdr Claimed, Customer Exclude. The live formula does NOT include draft_clean or email_status (those were never added to the live column) — add them by editing the function once fn_draft_clean exists. |
| **fn_persona_key** | BO_Sample_People `persona_key` | LIVE | Input: Job Title. Returns rubric keys **bo_claims / bo_shared / coo_finance / out_of_icp** (the back-office + finance subset). Extend the function's formula to cover wfm / cc_ops / cx when those motions need them. Rubric key only — motion labels stay separate, as designed. |

All three: "Replace columns with function" was left OFF, so every original column is intact.

## Not built — why, and exactly how to finish each (4 of 7)

Each of these hit a real blocker (verified live, not assumed). None should be authored blind into production; here are the precise steps.

### fn_email_verified — waterfall has no group-level "Save as function"
**Blocker (verified):** right-clicking the `Waterfall` group header offers only *Edit group* / *Delete*. A waterfall can't be extracted in one action; you must multi-select its columns.
**Steps:** On a table with the live waterfall (Cost-Mandate contacts or BO_Sample_People): Cmd-click every provider column in the waterfall group (`Find Work Email`, `Find Work Email (2)`, `(3)`, `Find work email`, … and the coalesced output) **plus** `Validate Work Email` → right-click → **Save as function** → name `fn_email_verified` → inputs should resolve to First Name, Last Name, Company Domain → outputs: email + email_status → uncheck "Replace columns" → Create. Verify on a 5-row slice before relying on it; waterfalls are the one place a partial extraction silently drops providers.

### fn_eligible — no single source column (logic is embedded)
**Blocker (verified against the build notes):** the customer/install-base kill switch lives *inside* `intent_status` / `Intent Score` / `New Logo Eligible` on the Cost-Mandate Universe, not as a standalone `eligible` column, so there's nothing to extract.
**Steps:** On the Cost-Mandate Universe table, add a formula column `eligible`:
```
{{Customer Flag}} != true && {{Install Base Lookup}} == "No Record Found"
```
(returns TRUE = safe to pursue; adapt the exact column names/values to the live cells). Then right-click `eligible` → Save as function → `fn_eligible` → inputs: Customer Flag, Install Base Lookup (or Company Domain if you want the lookup inside the function) → output: eligible → uncheck Replace → Create. **Cross-workbook caveat:** if you want the install-base lookup to live *inside* the function, verify a cross-workbook Lookup resolves in the function's mini-table before trusting it — the Golden Standard flags cross-workbook lookups as sometimes-broken; the fallback is to pass the lookup result in as an input.

### fn_draft_clean — never built as a live column (was file-only, H3)
**Blocker:** no live `draft_clean` column exists on any table to extract.
**Steps:** On the Cost-Mandate contacts table, add a formula column `draft_clean` reading the MessageGen body:
```
{{body}} != "" && !{{body}}.trim().startsWith("{") && !{{body}}.includes("\"subject\"")
```
(TRUE only when the body is non-empty, doesn't start with `{`, and doesn't contain the literal `"subject"` — the malformed-JSON / double-encode guard). Save as function → `fn_draft_clean` → input: Body → output: draft_clean → uncheck Replace → Create. Then edit **fn_send_ready** to AND-in this output.

### fn_tokens_ready — never built on the live BO table
**Blocker (verified):** BO_Sample_People has `persona_key` but no `tokens_ready` column; it was only ever in the build pack.
**Steps:** On BO_Sample_People, add a formula column `tokens_ready`:
```
{{First Name}} != "" && {{Job Title}} != "" && {{Company Name}} != ""
&& {{persona_key}} != "out_of_icp" && {{email_status}} == "valid"
&& {{source_motion}} == "back_office"
```
Save as function → `fn_tokens_ready` → inputs: First Name, Job Title, Company, persona_key, email_status, source_motion → output: tokens_ready → uncheck Replace → Create. Gate MessageGen on this in every motion.

## Session gotchas worth keeping
- The Clay Support (Intercom) popup pins itself over the bottom-right **Run** and **Review changes** buttons and swallows clicks. Hide it via console (`display:none` on `[class*="intercom"]` + bottom-right fixed iframes) before using those buttons.
- "Save as function" auto-suggests a junk name/description and defaults "Replace columns with function" **ON** — always rename and uncheck.
- The output-field name in the save dialog isn't editable by clicking; rename it later in the function editor if it matters.
- H2 critic discrimination test (known-good PASS / known-bad FAIL) was blocked by the Run-button overlay above; run it once fn_draft_critic is wired to real rows, or via the function's Add-test-inputs after clearing the widget.
