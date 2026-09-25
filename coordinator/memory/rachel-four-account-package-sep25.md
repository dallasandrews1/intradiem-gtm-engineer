---
name: rachel-four-account-package-sep25
description: "Sep 25 2026: Rachel DiBello's Keegan-shape package extended from Wells Fargo to four accounts (Bank of America, Centene, TD Bank added); builders generalized to N accounts; committees enriched through Clay (about 3,400 credits); STAGED, deploy is Dallas's terminal"
metadata:
  type: project
---

**Ask (Sep 25 2026, 07:02 CT call + Slack DM):** Rachel DiBello (Enterprise Sales Director) wants the exact Keegan master page and plan for Wells Fargo, Bank of America, Centene and TD Bank. Her framing: each line of business is its own logo. WF and TD are customers with a small footprint (TD in Wealth only, Coaching and Staffing launched Sep 21 2026, success manager Lisa Vidal); Centene and BofA are net-new in live cycles; she had a Centene call Sep 25. She never needs to see Clay ("nothing you guys need to look at").

**State:** Wells Fargo was already LIVE on backoffice-maps and save-rooms (the intradiem-accounts host 404s for it: the plans deploy was never run). The three new accounts are STAGED under ~/Desktop/Intradiem Deliverables/deploy-backoffice-maps/rachel/<slug>/ and deploy-save-rooms/<slug>/rachel/ (room, brief/, one-pager/, one-pagers/ x11, sequence/); rep index at /rachel/ shows four cards. Deploy = `automation/deploy_rep_pages.sh` maps, rooms, plans from Dallas's terminal (auto mode denies wrangler). Register every sent URL in automation/config/shared_links_manifest.json.

**Builders (now N-account):** every Rachel builder takes accounts from dicts keyed by account name (plans.py PLANS/LANES/ENG_OWNS with kind customer|prospect, tag, signal, read, enriched; people.py SHEET/ENRICHED_DATE/MAPS_PHRASE/WHO/EXEC; build_kit KIT with rules and hero; shelf_rachel MOMENTS_BY_SLUG plus flat MOMENTS; build_rachel_sheets ACCOUNTS with trees and expected count; accounts/write_shelf_manifest.py derives the manifest; map_notes.json). Shared: build_shelf_generic.py reads MOMENTS_BY_SLUG when present; build_rep_index.py renders a signal chip. The data contract checklist is in the plans.py docstring. Regression rule that held: Wells Fargo output byte-identical after every change.

**Sourcing pipeline that worked (reuse for the next AE):** research/search_candidates_sep25.py (lane title searches per account through `clay searches query-mode`, search results cost no lead credits, period quota 1M), a selection agent per account writing <sheet>_committee_selection_sep25.csv on the WF schema plus map_name/reports_up_to/function/level/new_in_seat/in_sf/source/why, then research/enrich_committee_sep25.py (Enrich Person and Find Contact Details, 12.4 credits each, resolves URL-less names by a name plus company search first, re-runnable, home-company check by letters-only company match with aliases). Names with no LinkedIn profile in Clay's data stay off the sheet and go in people.py EXEC with a public source. sf_known_people_sep25.py reads every Salesforce-known person per domain at 0 credits.

**Numbers:** BofA 87 enriched, 70 emails, 86 mobiles, 83 cards; Centene 88, 76, 88, 85 cards (37 already in Nathan's sequences, badged); TD 94, 54, 89. Balance 47,159.6 before, about 43,700 after.

**Findings another job acts on (log automation/logs/rachel-four-accounts-2026-09-25.md):** Centene's COO Susan Smith and COO Medicare Dan Clark got a cold back-office email Sep 24 to 25 while Rachel's cycle is live; TD's North America seat is Mushtak Najarali (EVP NACO since Mar 2025, Open lead, no validated email yet); BofA has no open opportunity on the record; Centene's Salesforce owner id is not Rachel's.

Related: [[wells-fargo-rachel-package-sep24]], [[feedback-keegan-room-is-the-bar]], [[signal-researcher-agents-cannot-write]].
