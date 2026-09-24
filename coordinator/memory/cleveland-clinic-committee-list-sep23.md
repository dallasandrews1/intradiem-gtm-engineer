---
name: cleveland-clinic-committee-list-sep23
description: "Sep 23 2026: the 61-name Cleveland Clinic buying committee and outreach list built for Sierra's MAC review; 33 campaign targets, Clay-verified, reply draft staged in Outlook; Salesforce stale on Kull, Boissy, DeAngelo"
metadata:
  node_type: memory
  type: project
  originSessionId: 42be9592-5883-44a3-ab0f-46b5bf8aa1f6
  modified: 2026-09-23T23:51:02.471Z
---

**Ask (Sep 23 2026, "Cleveland Clinic Retention Strategy" meeting, then Sierra's 14:38 CT email):** Dallas compiles the Cleveland Clinic contact list for the DWO-for-Stars save campaign, WFM leaders and up, blocker excluded; replies on Sierra's thread so Cheryl can run it by Mary Ann Chandler. Nate curates the final list and names the WFM-team blocker.

**Page LIVE Sep 23 2026:** https://save-rooms.pages.dev/cleveland-clinic/inger/committee/ (builder `motions/churn_risk_save_plan/build_committee_page.py`, in Inger's room tree so the theme pass and the phase-one host move both cover it; Inger's room hero links it; registered in the shared links manifest). Dallas's rule the same evening: a list like this is a showcase, so it ships as a page on the room system plus the CSV, never as an email table. Names, tiers, routes and method on the page; emails and mobiles only in the CSV.

**Revised the same evening (Dallas):** the ten people the save plan routes through Inger and Amy are NOT held out of the campaign and are never described as "already contacted" or as a separate account-team lane, which read as if Inger and Amy weren't doing their jobs. They sit inside the campaign list with an orange "Inger first" or "Amy first" chip naming the planned note and week, plus the line "confirm with Inger before anyone else writes." Campaign is now 43 in five groups (IT and platform added for the RFP evaluators). The group cards carry names, what they run, what they care about, what the note says, the ask and a watch line; headings are plain statements with counts.

**Built:** 61 names in `motions/churn_risk_save_plan/data/cleveland_clinic_committee_sep23.csv` (Desktop copy in Intradiem Deliverables). Tiers: 33 campaign (WFM and contact center management, access ops and transformation, experience and quality, MA risk and value), 10 account-team-only (Rena, the Faini IT four, Goode, Letwin, Hemsoth, Becka, Restaino), 6 held (Kokoruda, Yerian, Laraway, Peacock, Chandra, Hatchett), 4 excluded or gone, 8 WFM users for proof only. 46 mobiles and 53 ccf.org emails from the Enrich Person and Find Contact Details routine, 378 credits. Reply body saved beside the CSV as "Cleveland Clinic - Reply to Sierra - Sep 23" (.html and .txt); the Microsoft 365 connector has no Mail.ReadWrite scope, so Outlook drafts cannot be created from here and Dallas pastes and attaches by hand.

**Findings:** Salesforce still carries Matt Kull as CIO (left Aug 2023; Sarah Hatchett is SVP CIO since May 2024), Adrienne Boissy (now Case Western; Brian Carlson is CXO since Aug 2026) and Mickey DeAngelo (Andgo). Nine Salesforce-only contacts (Nahra, Griffin, Kokochak, Grdina, Fitch, Walton, Foster, Evans, Shantel Adams) have no public profile in Clay by name or email. Blocker name unrecorded; our match is Shantel Adams. Crystal Borders is the WFM manager over the real time analysts. Robert McDaniel (Exec Director Patient Access Support Services, Jun 2026) is a new seat.

**How to apply:** the campaign list and the save plan's personal notes must not hit the same person in the same week; anyone in tier 2 stays out of lemlist. Clay people search on `clay.filter_to_companies(("clevelandclinic.org"))` works; the `title contains "scheduling"` arm floods with clinical schedulers, use "Real Time", "Workforce", "Contact Center", "Call Center", "Access Optimization" tokens instead. See [[cleveland-clinic-cisco-dwo-not-qo-sep23]], [[clay-enrich-person-contact-details-routine]], [[inger-execution-state-rogers-sep20]].
