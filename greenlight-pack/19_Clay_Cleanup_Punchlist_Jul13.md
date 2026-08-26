# Clay Cleanup Punch-List — GTM Engine workbook (Jul 13 2026)

Read live from workspace 1180800, workbook **GTM Engine** (wb_0thtlocqNeb46szQtAf) through the browser, plus the workspace file list and the Campaigns view. Nothing was deleted — deletion is a data-removal action and stays your call. This is the classified list you asked for.

Scope note: the workspace is shared. Seven of the eight workbooks belong to Nathan, Naveen, and Genna — those are not yours to delete (see bottom). Your entire build is the **GTM Engine** workbook: 16 tables/campaigns.

---

## KEEP — core engine (do not touch)

- **Accounts (Master)** — 98 rows, 42 cols. The L2 intent layer. Auto-run paused (correct).
- **Contacts (Buying Committee)** — 137 rows, 64 cols. The finalized Wave 1 committee list.
- **CMS_Star_Movement_25v26** — 98 rows. Feeds the live `sig_measure_slippage` signal.
- **Parent_Signals_L2_seed** — 29 rows. The parent-grain helper (audit R8). Live component, not cruft.
- **Verified Metrics / Claims** — 6 rows. Verified-claims source for MessageGen.
- **ICP / Persona Rubric** — 10 rows. Grading rubric.
- **Product-Angle Map** — 8 rows. Message-angle reference.
- **Stars QBP Wave 1 - Tier A Committee (GATED)** — campaign. Current gated send path off Contacts (137). 0 rows synced by design (sync saved, not run).

## KEEP or ARCHIVE — raw source

- **CMS Star Ratings Import** — 307 rows. The raw universe Accounts (Master) was cut from and your October re-pull anchor. Don't delete; archive/hide if you want it out of the working view.

---

## DELETE — Tier 1, clean cruft (nothing live downstream)

Superseded Jul 10 per-persona load lists, replaced by the consolidated 137-row Contacts (Buying Committee):

1. **15_Eligible_Load_List_Persona1_Jul10** (custom table, 16 rows) + its CSV import.
2. **15_Eligible_Load_List_Persona2_Jul10** (custom table, 23 rows) + its CSV import.

Their only downstream is the two persona campaigns below.

## DELETE — Tier 2, superseded send artifacts (confirm first — send path)

Both are Draft, both consolidated into Tier A Committee off the finalized Contacts list:

3. **QBP Wave 1 - Persona 1 (Stars/Quality)** — campaign, 16 leads.
4. **Stars QBP Wave 1 - Persona 2 (Finance)** — campaign, 23 leads.

Caveat: Persona 2 is a distinct **Finance** segment. If you still want a separate Finance send, keep the campaign but re-point it at Contacts filtered to Finance and still delete the old load-list table (#2).

## COLLAPSE — Tier 3, intermediate staging (verify no live lookups, then delete/archive)

These are scaffolding that fed Contacts. Safe to remove only once Contacts holds the rows natively rather than via a live lookup — check each column's source in Contacts first.

5. **SalesNav Staging (Persona Pull)** — 128 rows. Dashed lookup into Contacts; sever before deleting.
6. **Healthcare Quality Leadership, Medic…** (Person table, 128 rows) — the raw SalesNav source pull feeding #5.
7. **Stars_Wave1_NewContacts_Import** — 10 rows. Gap-fill import. Delete only if the rows are already merged into Contacts; if the 7 queued emails are still pending, keep until merged.

---

## Cosmetic (for the "clean OS" look)

- Naming drift on your campaigns: `QBP Wave 1 - Persona 1` vs `Stars QBP Wave 1 - Persona 2` vs `Stars QBP Wave 1 - Tier A Committee`. Standardize the prefix.

## Not yours — workspace clutter you can't/shouldn't delete

Belong to other people; ask the owner or ignore. They affect the shared file-list impression but not your workbook:

- Clay Starter Table (Nathan), Maya_DropIn (Naveen), 4× Untitled workbook (Nathan/Naveen), Find and Verify a Job Change (Genna — 221 rows, actively running).
- Two `2026-06-10 New campaign` drafts (Naveen).
- The audit-era stray `2026-07-12 New campaign` is already gone.

---

## Net

Deleting Tier 1 (#1–2) plus their two CSV imports is unambiguous and takes the workbook from 16 to a tighter core. Tier 2 (#3–4) and Tier 3 (#5–7) need a 30-second confirm each. After that the workbook reads as: one master account table, one contacts table, one live signal table, one parent helper, three small reference tables, one raw source, one gated campaign — a clean operating system.
