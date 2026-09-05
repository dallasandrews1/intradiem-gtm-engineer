---
name: email-final-empty-classes-sep5
description: "Why email_final goes empty in Contacts (Buying Committee) — three distinct causes, one of them structural and permanent"
metadata: 
  node_type: memory
  type: project
  originSessionId: 2b07d59f-caa0-4120-a028-088a631552f9
  modified: 2026-09-05T04:59:26.727Z
---

Sep 5 2026, diagnosed on real rows. In table `Contacts (Buying Committee)`
(t_0thtm73HHxyiupTuepK, Star Ratings workbook), `email_final`
(f_0thx699qdHjGY5zW7fH) is a basic formula column:

`{{f_0thx5pwpHdfnW5smPfa}}?.record?.Email || {{f_0thv1axBVzr9YuGHoPf}}?.["Email"] || ""`

Source 1 is `Lookup Single Row in Other Table (2)`, which matches on **LinkedIn URL**
into `Sales Navigator Import (Staging)` (t_0thv913kpCnJuDEFUQY) and reads that table's
`Email` column, the output of an 11-provider waterfall (Findymail, Hunter, Prospeo,
Kitt, Datagma, Wiza, Icypeas, Enrow, Dropcontact, LeadMagic, SMARTe).

33 of 153 rows were empty, in three classes:

1. **Waterfall genuinely found nothing (19 rows).** Lookup returns `✅ Record Found`
   but the staging row's Email is null. 21 of 128 staging rows are like this.
   Re-running the same waterfall burns credits for nothing; these people need
   LinkedIn/phone routing or a different finder.
2. **Lookup can never match (4 rows: Anthony Portela/UHC, Mark Riddlesworth/Humana,
   Bob Wadsworth/Medica, Corey Taliaferro/Centene).** STRUCTURAL. The source column
   has two feeds: SalesNav Staging (121 records) and `Contacts_Backfill_Originals_Jul8`
   (22 records). Backfill rows never passed through the staging waterfall, so a
   LinkedIn-URL lookup into staging misses by construction. Confirmed none of the four
   exist in staging. Any future backfill import hits this same wall.
3. **Blank stub rows (10 rows, created 2026-09-05 02:59 UTC).** No name, company or
   LinkedIn URL; only `GTM Engine Sourced=TRUE`, `data_source`, `sourced_by=gtm_engine`.
   Clay has no row-delete API, so removal is Dallas's hands.

Load-bearing downstream: the `Validate Email` action column
(f_0thvwiqGFtriBqJMqx6) takes its `email` input from `email_final`, so an empty
`email_final` means Validate Email cannot run on that row at all.

Related: [[clay-free-sourcing-path]], [[feedback-warn-before-large-credit-spend]]
