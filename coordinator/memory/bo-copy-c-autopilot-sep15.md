---
name: bo-copy-c-autopilot-sep15
description: "Sep 15 2026: back-office Version C restructured to the autopilot order (Email 1, call task d1, Email 2 thread d3, LinkedIn after), Nate's read page live at bo-copy-read.pages.dev, load plan with step ids written and STOPPED before any lemlist write; lead read found five wrong-company leads and 8 UHC/Optum rows"
metadata: 
  node_type: memory
  type: project
  originSessionId: 1cc96141-e5aa-4bc9-8ae4-2f2c4b818224
  modified: 2026-09-15T14:32:24.080Z
---

**State Sep 15 2026.** Version C (Sierra's V04 proof on the Sep 4 pressure standard) now runs on the Sep 14 autopilot order on all five BO campaigns: day 0 Email 1, day 1 call task with voicemail (cleared names only on customer lanes), day 3 Email 2 in thread, day 4 LinkedIn visit + connect note, day 7 DM 1, day 10 Email 3 new subject, day 11 Call 2, day 13 DM 2, day 17 breakup. Net-new keeps the Sep 4 pressure tree (three calls, two threads, colleague line) in the same order over 19 days. Record: `motions/back_office_expansion/BO_Copy_v2_Sep9.md` (Sep 15 note on top); Nate's page https://bo-copy-read.pages.dev (project `bo-copy-read`, builder `build_c_nate_read.py`, single source is the v2 md). Plan: `BO_C_Load_Plan_Sep15.md` (nine writes per customer lane, fifteen on net-new, every step id from the Sep 15 sequence read). Variables: `build_c_variable_fill.py` (CSV reference) and `push_c_vars.py` (population = live export, dry run default). Drafts: `BO_Drafts_Sep15.md`.

**Lead read (334 leads, all five campaigns):** five wrong-company leads loaded outside the staged CSVs (53.com in a Regions row and a Molina customer in a Centene row on Net-New, blueshieldca.com and sofi.org on FS, humana.com in a Molina row on HC), one held Truist row mislabeled JPMorgan; eight HC leads are UHC/Optum (alternate proof line). Customer lanes carry only enterprise_line + parent_account; net-new carries opener_line (one dated line per account) + function. Launched: HC 33/67, Insurance 33/33, BPO 25/25 past Email 1; FS 0/79, Net-New 0/130.

**Naveen's Sep 11 launch structure (Otter):** messaging group (Nate, Cheryl, Melissa, Tom) signs off, post-all-hands review of email + ad copy, ads and sequences start together, "automate everything apart from the calls."

**Why:** the Sep 13 review found every sequence stalled at a LinkedIn task after one email; DWO proved the fix Sep 14; BO is the second lane to carry it.
**How to apply:** nothing in lemlist has changed; the swap waits for Dallas's go, then lead deletes first, variable push second, sequence edits third, QC and preview fourth. Leads inserted-behind never receive the new earlier steps. Related: [[dwo-autopilot-lane-sep14]], [[bo-copy-three-versions-sep9]], [[gtm-engine-review-sep13]], [[sixsense-kw-segments-absent-sep15]].
