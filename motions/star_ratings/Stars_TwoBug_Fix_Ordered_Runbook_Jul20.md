# Stars Table — Two-Bug Fix, Ordered Runbook
Date: 2026-07-20 · Table: Contacts (Buying Committee) `t_0thtm73HHxyiupTuepK` · workspace 1180800
Both fixes are UI-only (Dallas's hands), reversible, and do NOT touch any send gate.

## Do them in THIS order (dependency)
Concat bug FIRST, dollar wiring SECOND, then ONE combined 2-row verify.
Reason: the dollar fix's verify regenerates MessageGen on 2 rows. If Company/Title still
double, those drafts come out corrupted and the dress rehearsal is worthless.

## Guardrails (both fixes)
- Verify ONLY on uncontacted rows. Never regenerate the 23 already-sent or the cohort prepped
  for manual Email 2/3.
- Do NOT re-run sync over any wave holding per-lead overrides.
- Confirm every formula/label on your screen before saving; flagged labels below need a look.

---

## FIX 1 — Company + Job Title doubling ("CenteneCentene", doubled title)
Symptom (from the 2026-07-19 smoke test): the Company and Job Title values render doubled,
which would corrupt real-row MessageGen copy. Cause is a concat formula. Exact field IDs and
formula are NOT in any file, so this is locate-then-fix. [CONFIRM the formula on screen.]

1. Open table `t_0thtm73HHxyiupTuepK`. Find the columns feeding MessageGen's company/title
   tokens (the ones whose cells show "CenteneCentene" / a doubled title on a Centene row).
2. Click each column header to open it. Note whether it is a **Formula** column or a plain
   data/enrichment column:
   - If **Formula**: read the formula. The doubling is almost always a self-concat
     (`{{Company}} + {{Company}}`) or two identical sources joined (an enriched Company field
     concatenated with a mapped Company field). Replace the whole expression with a single
     clean reference to the ONE correct source (e.g. just `{{Company}}`), so it emits the value
     once. Same for Job Title.
   - If **plain/enrichment** showing doubled text: the doubling is upstream in whatever formula
     or mapping populates it. Trace to that source column and apply the single-reference fix
     there.
3. Save. Confirm a Centene row now shows "Centene" once and a single clean title.
4. [FLAG] If the doubled column is a token MessageGen reads directly (not a separate display
   column), the fix must land on the exact column MessageGen references, or the copy stays
   corrupted. Confirm which column the MessageGen prompt actually pulls.

---

## FIX 2 — Gross-as-addressable dollar wiring
Source of truth: Stars_Wave2_Dollar_Wiring_Fix_Sheet.md (same folder). 3 steps, all IDs below.

### Step 1 — Create the CS-slice field
Add a new **Formula** column named exactly: `Addressable CS-slice ($M, 2026-cycle)`
Paste (values verbatim from the Why Now formula so the number matches the email hook):
```
({humana:568.9,uhc:248.7,aetna:72.4,cvshealth:72.4,centene:52.5,hcsc:23.5,cloverhealth:49.1,medica:23.7,excellusbcbs:15.1,guidewell:5.8,blueshieldca:11.5,vnshealth:26.1,devoted:31.0,imperialhealthplan:25.4,clevercarehealthplan:21.2,carefirst:5.9,massgeneralbrigham:5.5,point32health:8.3,cambiahealth:0.6,nychealthandhospitals:5.4,caloptima:9.6,lacare:13.4,lumeris:8.1,iehp:14.8,phs:19.1,myzinghealth:24.9,chpw:4.9,atriohp:10.4,baystatehealth:10.3})[{{parent_key}}]
```

### Step 2 — Repoint the MessageGen token
Open **MessageGen Email 1 (v2.2)** (`f_0ti6c7jcHFffy94Qmqv`) → Prompt. Find:
```
addressable_forgone_qbp_musd (CS-attributable slice, $M): " + Clay.formatForAIPrompt({{Account Forgone QBP ($M, 2026-cycle)}})
```
Change ONLY the token to `{{Addressable CS-slice ($M, 2026-cycle)}}`. Everything else byte-identical.

### Step 3 — Repoint the critic's token (must match Step 2 or it false-fails)
Open **Draft Audit** (`f_0ti6ehbktFZ6uMkz8dT`) → Prompt. Find:
```
SOURCE addressable dollars ($M): " + Clay.formatForAIPrompt({{Account Forgone QBP ($M, 2026-cycle)}})
```
Change the same token to `{{Addressable CS-slice ($M, 2026-cycle)}}`.

---

## COMBINED VERIFY (validates both fixes at once)
1. Pick 2 real UNCONTACTED rows on a multi-contract payer (Centene ideal): one Persona 1
   (Stars/Quality/Member Experience title) and one Persona 2 (CFO/Finance title).
2. Re-run MessageGen Email 1 on just those 2 rows, then re-run Draft Audit on them.
3. Confirm ALL of:
   - Company reads "Centene" once; title is clean (Fix 1).
   - Lead dollar reads the account CS-slice (Centene ~$52.5M, not $165.8M, not one contract) (Fix 2).
   - Draft Audit / msg1_critic Status = PASS.

## Still open after this (flag, not blocking)
- `addr_2028_musd` is contract-grain, framed account-wide for multi-contract payers.
- CVS/Aetna key mismatch: parent_key "cvs" vs map keys "aetna"/"cvshealth" → blank dollar.
- Draft Audit is a hand-forked critic, not shared `fn_draft_critic`; shared fixes miss this table.
