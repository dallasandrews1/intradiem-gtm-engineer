---
name: genna-icp-titles-package-sep21
description: "Sep 21 2026: Genna asked the GTM group DM for ICPs and titles behind every motion; PDF plus filter-ready spreadsheet built from one data block in motions/marketing/genna_icp_titles_sep21/build.py, staged in Deliverables, not yet sent"
metadata:
  type: project
---

Genna Barrett-Moeller asked in the group DM C0C3F93JU1F (Naveen, Cheryl, Nathan, Sierra, Carter, David; Sep 21 2026 2:07pm CT) for "a list of ICPs/Titles you're using for your various GTM motions". This is the wider version of [[sierra-lists-package-aug26]], which covered only the webinar lists, back office and the persona rubric.

Built: `motions/marketing/genna_icp_titles_sep21/build.py` holds every motion's accounts, title strings, removals and seniority once and emits the branded HTML (printed to a 7-page PDF with headless Chrome) and an xlsx with one row per motion and seat (37 rows) plus a shared-rules tab. Copies in `~/Desktop/Intradiem Deliverables/ICPs and Titles for Genna (Sep 21)/`. Eleven motions: Star Ratings, Healthcare QO (October, in preparation), back office, front office new logo, DWO executives, WFM Present and Genesys Present, competitive displacement, cost mandate, WFM adjacency, UK and Ireland, named accounts. Source file and line for each block sits in SOURCES at the bottom of build.py.

Dallas's layout call: free to leave the Aug 26 PDF format when a better delivery exists. Marketing ops works in filters, so a scan-first matrix plus a paste-ready spreadsheet beats a PDF alone.

**Why:** the group DM is leadership-visible, so the package carries no campaign status, counts, dollar estimates or customer names, only criteria.

**How to apply:** for the next title or ICP ask, edit the data in build.py and re-run; do not rebuild from the motion files. Left out on purpose: the alumni lane (no roster), the actuary addition (bo_gates.py now excludes actuarial titles), Engagement Hub (covered by the icp-committees link).
