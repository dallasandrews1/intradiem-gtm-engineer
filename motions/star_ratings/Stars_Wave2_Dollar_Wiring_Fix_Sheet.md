# Stars Wave 2 — Dollar-Wiring Fix Sheet
Date: 2026-07-20 · Table: Contacts (Buying Committee) `t_0thtm73HHxyiupTuepK` · workspace 1180800

## The problem (pre-existing, present in Wave 1 too)
The MessageGen Email 1 prompt and the Draft Audit critic both read the dollar token
`{{Account Forgone QBP ($M, 2026-cycle)}}` (field `f_0thuvdcX5bCtUh8tzRX`), which holds the
**GROSS** forgone-QBP total (Centene 165.8, Humana 1776.3), while the prompt LABELS it the
"CS-attributable slice." The true customer-service-addressable slice (Centene 52.5, Humana
568.9, Cambia 0.6) already exists, hardcoded inside the `Why Now (2026-cycle)` formula
(`f_0thuvhooGA2y8idyaZQ`), but was never broken into its own field. Live proof it bites: the
table's only 2 current critic FAILs are both Cambia, where the draft used gross $4.8M as
addressable and the critic correctly caught it against the real $0.6M.

## The fix (3 steps, ~15 min, reversible, does NOT touch the send gate)

### Step 1 — Create the CS-slice field
Add a new **Formula** column named exactly: `Addressable CS-slice ($M, 2026-cycle)`
Paste this formula (same proven pattern as the existing gross field, values pulled verbatim
from the Why Now formula so they stay identical to what the email hook already says):

```
({humana:568.9,uhc:248.7,aetna:72.4,cvshealth:72.4,centene:52.5,hcsc:23.5,cloverhealth:49.1,medica:23.7,excellusbcbs:15.1,guidewell:5.8,blueshieldca:11.5,vnshealth:26.1,devoted:31.0,imperialhealthplan:25.4,clevercarehealthplan:21.2,carefirst:5.9,massgeneralbrigham:5.5,point32health:8.3,cambiahealth:0.6,nychealthandhospitals:5.4,caloptima:9.6,lacare:13.4,lumeris:8.1,iehp:14.8,phs:19.1,myzinghealth:24.9,chpw:4.9,atriohp:10.4,baystatehealth:10.3})[{{parent_key}}]
```

### Step 2 — Repoint the MessageGen token
Open the **MessageGen Email 1 (v2.2)** column (`f_0ti6c7jcHFffy94Qmqv`) → Prompt field.
Find this line:
```
addressable_forgone_qbp_musd (CS-attributable slice, $M): " + Clay.formatForAIPrompt({{Account Forgone QBP ($M, 2026-cycle)}})
```
Change ONLY the token from `{{Account Forgone QBP ($M, 2026-cycle)}}` to
`{{Addressable CS-slice ($M, 2026-cycle)}}`. Leave everything else byte-identical.

### Step 3 — Repoint the critic's source token (must match Step 2 or the critic will false-fail)
Open the **Draft Audit** column (`f_0ti6ehbktFZ6uMkz8dT`) → Prompt field.
Find this line:
```
SOURCE addressable dollars ($M): " + Clay.formatForAIPrompt({{Account Forgone QBP ($M, 2026-cycle)}})
```
Change the same token to `{{Addressable CS-slice ($M, 2026-cycle)}}`.

## Verify (the "regenerate a couple contacts" dress rehearsal)
1. Pick 2 real uncontacted rows: one Persona 1 (Stars/Quality/Member Experience title) and one
   Persona 2 (CFO/Finance title), ideally on a multi-contract payer like Centene.
2. Re-run MessageGen Email 1 on just those 2 rows, then re-run Draft Audit on them.
3. Confirm: the draft's lead dollar now reads the account-level CS-slice (Centene ~$52.5M, not
   $165.8M and not one contract's number), and `msg1_critic Status` = PASS.

## Still open after this fix (flag, not blocking wave 2)
1. **2028-window figure is contract-grain.** `addr_2028_musd` comes from the account-row lookup,
   which returns ONE contract per payer. For multi-contract payers the prompt still frames it as
   account-wide. Fix later: either drop the 2028 dollar (keep December urgency qualitative) or
   build an account-level addr_2028 rollup.
2. **CVS/Aetna key mismatch.** `parent_key` renders "cvs" but the dollar maps use keys "aetna"/
   "cvshealth", so CVS/Aetna rows get a blank dollar (draft falls back to star-only). Cleanup: add
   a "cvs" key to the maps, or fix parent_key.
3. **Structural drift.** This table's Draft Audit is a hand-forked critic, NOT a call to the shared
   `fn_draft_critic`. Fixes to the shared function do not reach this table. Decide if single-source
   is the intent.
