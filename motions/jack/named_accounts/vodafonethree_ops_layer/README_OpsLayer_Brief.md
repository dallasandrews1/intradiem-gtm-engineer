# VodafoneThree ops layer, build brief (Aug 17 2026)

Built same-day from Jack's Slack spec (11:56-11:15 CDT thread). The play: reach the operational layer beneath the held senior contacts (Bonnar, Bourke, Dalton, Rubertazzi, Shaw), use those conversations for intelligence and referrals, then re-approach the seniors non-cold.

**Deliverables:** `VodafoneThree_OpsLayer_v1.1.csv` (106 contacts, verified + enriched, supersedes v1), `VodafoneThree_EntryLayer_Brief.html` (the strategy page for Jack, published as the VodafoneThree Entry Layer artifact), `Wave1_Staged_Planning_Platforms_Analytics.csv` (22 rows staged), `UI_Sheet_Import_To_Clay_Table.md` (Dallas's 5-minute table import).

## What was done

1. **Broad net** (Jack's step one): Clay advanced search across VodafoneThree, Three UK, and Vodafone UK entities, analyst-to-manager seniority, semantic title matching across all four buckets. 556 raw results, 341 unique people. A second precision sweep recovered 5 planning analysts hidden under the global Vodafone entity.
2. **Dedupe and gates:** matched against `UK_NamedAccounts_Roster_v1.1` (Bonnar and Bourke auto-dropped as already held). Jon Shaw and Ryan Rubertazzi on a hard avoid list per Jack. No senior directors or heads captured.
3. **Classification** (Jack's step two): against his written definition, not a title list. 230 excluded (retail, field, network, IT, finance, HR, cyber, advisors/ICs).
4. **URL bridge:** 96 LinkedIn URLs resolved (91 via Clay contact match, 5 more via research), fresh current titles pulled, which caught 6 stale entries (leavers/retiree) that were removed.
5. **Research pass** (Jack's highest-value component): 7 parallel research agents, one pass per contact, two for managers. Hard no-fabrication rule: 25 contacts have a real, cited hook; the other 81 carry an honest `NONE FOUND` plus a fallback angle built only from confirmed facts (tenure, merger timing, site). Nothing invented.

**Clay credit cost: 0.0.** The whole build ran on search and contact-match surfaces that bill action executions, not credits. Worth carrying into the UK-credits-vs-Lusha conversation: the sourcing and classification layer is free; Lusha (or Clay waterfalls at ~13 credits/contact) is only needed for emails and phones.

## Counts

| Bucket | Kept | Notes |
|---|---|---|
| Planning and WFM | 13 | The core persona. 4 need URLs (see gaps) |
| Analytics and CI | 15 | Strongest hooks live here |
| Contact Centre Operations | 43 | ~9 flagged possible out-of-scope, see below |
| Frontline Management | 34 | Thin public footprints, as expected |
| Bonus: CC Tooling / Transformation | 5 | Own the Genesys estate and change programmes |

## Priority shortlist (real hook, in scope)

1. **Dan Taylor**, Senior Manager, Service & Contact Centre Platforms. The seat that owns whatever WFM/orchestration layer sits on the Genesys Cloud estate. Confirm current remit name first (a second source shows "Digital Omni-Channel Processes and Tooling").
2. **Karen Findlay**, Senior Programme Manager Contact Centre Transformation, Glasgow. Programme started May 2025, the merger-completion month.
3. **Jed Shields**, Reporting and Data Analyst (Three side). Hand-builds Excel/VBA KPI dashboards and runs a side business doing exactly that. The sharpest single hook in the file.
4. **Simone Golden**, Senior Ops Manager, Specialist Sales & Strategic Ops. UK National Contact Centre Awards 2023 Gold winner, featured on the CCMA CareerTalk podcast.
5. **Sajid Ahmed**, Channels Insight Analyst (Vodafone side). Built an MVP at a Vodafone AI & Innovation hackathon.
6. **Christopher Stewart**, Senior Ops Manager (Three side). Ran the outsourced Three Mobile sales operation at Capita for 12+ years before it came in-house.
7. **Muhammad Safdar**, Specialist Care Process Improvement Ops Manager. BPO career (Webhelp, Konecta) brought in-house, Six Sigma.
8. **Steven McNulty** and **David Watret**, FCA QA Team Managers (Three side, Glasgow). Vendor-side and compliance-route careers respectively.
9. **Michael Suarez**, CX Improvement Lead (Vodafone side). Owns the retail complaints programme turnaround, active in the #cxigang community.
10. ~~**Gareth James**~~ REMOVED Aug 18: the verify pass shows he left for MBNL (the EE/Three network JV). Kept here as the example of why verification runs before outreach; he was the research pass's standout hook.
11. **Jennifer Clarke**, Senior Performance Manager, Customer Care. Came up through Medallia VoC and mystery-shopping measurement.
12. **Paul Campbell**, Senior Manager Demand and Supply Planning (Three side, decade in seat). Seniority flag: likely Bonnar's peer or manager; sequence him relative to Bonnar deliberately.

## Gaps needing Jack (his SalesNav/Lusha can close these fast)

- **4 Vodafone-side planning contacts have no findable LinkedIn URL:** Phil Thornhill (Lead Real Time Analyst), Jill Armitage URL found but thin, Joe Findon (Lead Forecast Analyst), Chris Dunn (Forecast Analyst), Martin Mason (Senior Forecasting Analyst). These are the core Intradiem persona on the Vodafone side; worth a manual SalesNav pull.
- **Ahmed A.** (Service Performance Analyst, Three): surname truncated at source; needs the full name.
- **Bradley Roberts** (Team Supervisor, Cwmbran): no public footprint at all.

## Verify-before-touch list (identity or scope risks the agents caught)

- **Kenneth Fallens**: a same-named profile now shows at Virgin Media O2, a current Intradiem customer. If he moved, he is out of scope twice over. Check first.
- **Julie Bushell**: her listed URL slug is `julievalla` (surname mismatch, possibly a name change); a theorg listing shows her as Head of Service Quality Management. Confirm identity before using any career detail.
- **Akanksha Phadnis**: public LinkedIn shows "Scrum Master, Vodafone Business" vs our "Demand Planning & Capacity Manager". Confirm current role.
- **Mandy Ellis**: URL slug is `mandy-cooke`, likely a name change, unconfirmed.
- **Gary Stewart**: two candidate URLs (`gary-stewart-89ba8b5` vs `garystewart1984`, the latter matched his bio repeatedly). Confirm before connecting.
- **Steve Moores**: two conflicting records (Customer Care Team Leader vs Social Media Manager) that may be different people.
- **Andrea Hutchinson**: profile at her URL displays as "Andrea Mehmood" (likely married name).
- **Katie B.**: best candidate is Katie Brough (Vodafone Sales Team Manager, Cheshire), location exact but not fully confirmed.
- **Tariq Timol, David Bain, Nat Bell**: namesake or duplicate-URL conflicts, single manual check each.
- **Demand-planning cluster caution** (Neha Dave, Fiona McGrath, Daniel Gibbs, Mandy Ellis, Akanksha Phadnis): "demand planning" in telco can mean supply-chain or network capacity, not contact-centre workload. McGrath's history (CTIL mast infrastructure) leans network. Bonnar uses "demand and supply" for contact-centre planning, so these stay in with a verify flag rather than being dropped.

## Probable out-of-scope (kept in the CSV, flagged in division column, Jack decides)

Michael McKeown (wholesale carriers/partners), Brad Chapple (retail stores), Fernando Goncalves (retail stores), Steve Maguire (IT ops), Neil Kingston and Amanda Eales (Technical CX = network/service-performance track, peer-inference), Daniela Di Pasquale (digital self-serve UX, though a strong future digital-deflection contact), Sam W. (CX insights, better as a data ally than a buyer), Kevin Christie (omnichannel design, borderline).

## Notes for the messaging layer, when it gets built

- Estate tags: Three-side contacts confirmed via career history; VodafoneThree-entity contacts marked TBD where history was invisible. Three is the smaller estate absorbing the larger one's operating model, a different angle per Jack's spec.
- Integration phase (duplication assessment, office consolidation) is context explaining resistance, never a buying signal. None of the hooks reference redundancy or headcount.
- No Intradiem figures appear anywhere in this file, so nothing here touches the verified-claims gate yet. The gate applies when outreach copy gets drafted.
- Org mapping byproduct: Laura Halls (Head of Contact Centre Sales, Vodafone Consumer Operations) surfaced above the target layer; useful for the org chart, not a target.
