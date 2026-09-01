# BMO Committee — ZeroBounce UI Sheet (Jul 29 2026)

**Why this runs before drafting ships:** enrichment law. Every committee email is ZeroBounce-validated before the strike-room copy is sent. The draft is built in parallel, but nothing sends until these come back valid. One address (`gallagher@bmo.com`) is a weak lastname-only pattern from Clay and is the specific reason this sweep matters.

**Where:** Chrome → app.clay.com → workbook **`OneOff_ZB_Sweep_Jul29`**. Add a **new blank table** in that workbook named **`BMO_Committee_ZB`** (one table per account; do not make a new workbook).
- If `OneOff_ZB_Sweep_Jul29` does not exist in the workspace yet, create it: **+ New → Workbook → Blank table**, name the workbook `OneOff_ZB_Sweep_Jul29` and the table `BMO_Committee_ZB`.

## The 6 addresses to sweep (email-led seats only)

The three enterprise anchors (Nalgirkar, Haward-Laird, Tennyson) are **not** in this sweep — they run LinkedIn-led with no email, so there is nothing to validate for them.

| # | Name | Seat | Email | Watch |
|---|---|---|---|---|
| 1 | Paul Malik | SVP, Customer Loyalty / Operational Excellence | `paul.malik@bmo.com` | — |
| 2 | Joseph McNellis | Sr Mgr, CX & Complaint Resolution | `joseph.mcnellis@bmo.com` | — |
| 3 | Caroline Dufaux | CFO, BMO US | `caroline.dufaux@bmo.com` | — |
| 4 | Christie Bauer | Contact Center Manager | `christie.bauer@bmo.com` | — |
| 5 | Shane Hansen | Sr Mgr, PM Technology Operations | `shane.hansen@bmo.com` | reserve (Tier 3) |
| 6 | Bill Gallagher | Head, Customer Experience | `gallagher@bmo.com` | **WEAK — lastname-only. If ZB returns invalid/unknown, re-run `bill.gallagher@bmo.com` then `william.gallagher@bmo.com`** |

## Steps (the sequence that works)

1. In `OneOff_ZB_Sweep_Jul29`, add a blank table, name it `BMO_Committee_ZB`.
2. Set the row-count box next to **+ Add** to **5** (that is seats − 1, since row 1 already exists), click **+ Add**. You now have 6 rows.
3. Type each email **cell by cell** into the email column. Critical: after the double-click to open the cell editor, **wait 1 second** before typing (the editor has to mount, or the text silently goes nowhere). Rhythm per cell: double-click → wait 1s → type → wait 1s → Return. **Never paste all six with newlines — it merges cells.**
4. **Add column → Add enrichment → search `zerobounce` → Validate Email (ZeroBounce, 0.1/row).** The email column auto-maps.
5. **Continue to add fields → toggle on `Status` and `Sub Status` → Save chevron → "Save and run 6 rows in this view."**
6. On the page, confirm **"100% of table completed"**, then read the **Status** column verbatim for all 6 before reporting.

## After the run — report back to me, verbatim

Paste the Status (and Sub Status) column for all 6 rows. I need it before the sequence leaves HOLD. Specifically:
- Any `invalid` / `unknown` / `catch-all` sub-status.
- **Gallagher's result.** If it is not clean, I will swap the address in the sequence to whichever of `bill.gallagher@` / `william.gallagher@` validates, and you re-sweep just that one.

## Cost
0.1 credits/row × 6 = **~0.6 credits.** Log the actual to `Clay_Credit_Ledger.md` (the row is already staged there under Jul 29, marked "not run").
