# Polar sheet: WFM L3 customer lookup re-bind

> Task slug `wfm-l3-lookup-rebind`. Closes the gate that has read inert since Aug 20 2026: the `L1 Customer Lookup` action on WFM-Adjacency L3 has its Row value bound to the literal text `"{{Company Domain}}"` instead of the Company Domain column, so every lookup returns No Record Found and `customer_exclude` reads false on all 293 customer rows. One input to re-bind, one run, one read to prove it.

## Ground truth (read Sep 13 2026 via the Clay CLI, `clay tables columns get`)

| Item | Value |
|---|---|
| Table | WFM-Adjacency L3, `t_0tic8arWbZp8bSx87Ad`, 524 rows |
| Column to fix | `L1 Customer Lookup` (action, Lookup single row in other table), `f_0tjxaitimfHdnYmh4dN` |
| Table to search | `t_0tict25TSXgTgdJgtZZ` (WFM_Adjacency_L1_Seed_Enriched_28) |
| Target column | `f_0tict26nU7DQakETTrR` (`domain` on L1) |
| Filter operator | `EQUAL` |
| Row value today | `"{{Company Domain}}"` as quoted literal text. This is the defect. |
| Row value wanted | the Company Domain column, `f_0ti8tdrnCsHVcUNjmh8`, inserted as a column chip |
| Working twin on the same table | `Universe Lookup` `f_0ti8uifTiAtoDgVYQTh`: identical table, target and operator, Row value correctly bound to `{{f_0ti8tdrnCsHVcUNjmh8}}`. Copy its Row value setting exactly. |
| Downstream | `customer_exclude` `f_0tjxal4qnNvPxP2jZwN` reads `{{L1 Customer Lookup}}?.record?.customer_flag`; `Send Ready` `f_0ti9ygfsJv3y8g6Nkcz` already carries `!{{customer_exclude}}`. Both self-correct once the lookup returns records. |
| Expected end state | `customer_exclude` TRUE on Elevance Health (143), Molina Healthcare (122), Carelon (4) = 293 rows; Send Ready HOLD on all 293; no row flips to READY. |
| Credits | Internal lookups have run at 0 on this table (Universe Lookup, Jul 18). Stop before Run if Clay shows any estimate above 0. |

Labels marked *(confirm)* are not in Clay's docs (university.clay.com/docs/lookup-rows names only the four inputs: Table to search, Target column, Filter operator, Row value). Read the live screen; where it differs, stop and hand back.

## Paste into Polar (the task)

```
TASK wfm-l3-lookup-rebind. Clay, workbook "WFM-Adjacency Motion", table "WFM-Adjacency L3" (table id t_0tic8arWbZp8bSx87Ad). Follow the numbered steps only. Do not improvise. You have no access to this Mac's files: keep screenshots in your own workspace and give their download links; end your final message with the REPORT block in step 10, then stop. Never run any column other than the one named in step 7, and never on more rows than step 7 states.

1. Open the table. Confirm the page title reads "WFM-Adjacency L3" and the URL contains t_0tic8arWbZp8bSx87Ad. If not, STOP and hand back.
2. Find the column named exactly "L1 Customer Lookup". Take a screenshot of its current settings panel and keep it as before.png in your workspace.
3. Open the column's settings (the column header menu, then the edit/settings entry; the label is not documented, read the screen). You should see four inputs: Table to search, Target column, Filter operator, Row value.
4. Do not change Table to search, Target column or Filter operator. If they are not (WFM_Adjacency_L1_Seed_Enriched_28, domain, Equals) STOP and hand back with a screenshot.
5. In Row value, delete the existing text "{{Company Domain}}". Insert the column reference to "Company Domain" the way Clay inserts a column chip (type / and pick "Company Domain" from the column list, or use the column picker the input shows). The input must show a chip labelled Company Domain, not typed text in braces. If the input still shows typed braces, STOP and hand back.
6. Save the column settings. STOP-AND-HAND-BACK: before anything runs, show Dallas the saved Row value.
7. Run "L1 Customer Lookup" on all rows of this table (524 rows). If Clay shows a credit estimate greater than 0, STOP and hand back before confirming. Do not run any other column.
8. Wait until the column has finished on every row (no cells still in progress).
9. Filter or sort so you can see rows where Company Name is "Elevance Health". Screenshot one such row showing L1 Customer Lookup, customer_exclude and Send Ready, keep it as after.png in your workspace.
10. End your final message with a block that starts with the line REPORT wfm-l3-lookup-rebind and lists: the Row value as it now reads, the number of rows the run covered, the credit estimate Clay showed (or "none"), the values of L1 Customer Lookup, customer_exclude and Send Ready on the Elevance Health row you screenshotted, anything that did not match this sheet, and the download links for before.png and after.png.
11. Stop. Do not message anyone. Do not open any other tab.
```

## Stop-and-hand-back lines

- Table title or id does not match (step 1).
- Any of the three untouched inputs differs from the recorded values (step 4).
- Row value still shows typed braces after the insert (step 5).
- Before Run, always (step 6).
- Any credit estimate above 0 (step 7).

## Report-back

Polar has no access to this Mac (probe, Sep 13 2026: it runs in a cloud sandbox). The report is the REPORT block at the end of its final message. Dallas pastes that block back to Claude Code; the intake logs it as a claim with `python3 automation/polar_intake.py --paste wfm-l3-lookup-rebind` (text on stdin). Screenshots stay in Polar's workspace behind download links; download them to `~/Downloads/polar/wfm-l3-lookup-rebind/` only if the picture matters, the intake scans that folder too.

## Verification that closes the task (Claude Code, not Polar)

1. `clay tables columns get t_0tic8arWbZp8bSx87Ad` shows `L1 Customer Lookup` with `fields|rowValue` formulaText `{{f_0ti8tdrnCsHVcUNjmh8}}` (no quotes).
2. gate-integrity-auditor reads real rows: `customer_exclude` TRUE on all Elevance Health, Molina Healthcare and Carelon rows (293), Send Ready HOLD on every one, READY count unchanged or lower.
3. Log line under `evt: polar-intake-<date>#wfm-l3-lookup-rebind`, chain `gate-integrity-2026-08-20#wfm-l3-customer-lookup-inert`. Registry status to `verified`, memory `wfm-l3-customer-lookup-inert-aug20` marked RESOLVED.

Alternative if the chip will not bind: change the `customer_exclude` formula to read `{{Universe Lookup}}?.record?.customer_flag?.toString()?.toUpperCase() === "TRUE"` and re-run Universe Lookup on all rows instead (its cached records predate the Aug 17 customer_flag fix). Same stop lines, same verification.
