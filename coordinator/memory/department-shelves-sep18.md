---
name: department-shelves-sep18
description: "Sep 18 2026 night: one-pager shelves built and deployed for all three departments (AE Keegan 25, AM Alex 30 + Inger 11, partners Frank 15 incl. three partner-seller pages); shared builder, how each department's objective changes the pages, Frank's self-serve skills updated, and the white-glove vs self-serve recommendation"
metadata:
  type: project
---

**Live at save-rooms.pages.dev (81 one-pagers total, 134 new URLs 200 on Sep 18 2026):** `/<slug>/<rep>/one-pagers/` is a shelf page with a what-to-send-when selector; each page sits beneath it as HTML + PDF. Rooms for Alex (6), Inger (Cleveland Clinic) and Frank (Assurant) link to their shelf. PDFs in Desktop folders `Alex Execution Kit - Sep 18`, `Inger Execution Kit - Sep 18`, `Frank Partner Kit - Sep 18`.

**Shared tooling:** `motions/shared/execution_kit/build_shelf_generic.py` (data module in), `SHELF_BUILD_BRIEF.md` (hand to a builder agent with the department objective), `link_shelf.py` (room header link; rerun after any room rebuild). Data modules: `back_office_expansion/kit/shelf_alex.py`, `churn_risk_save_plan/kit/shelf_inger.py`, `partner_channel/kit/shelf_frank.py`, each with a CLAIMS_LEDGER.

**Objective changes the pages, not the method:** AE net-new = public situation and why now. AM expansion (Alex) = back-office readers, relationship-neutral, the AM supplies the relationship line. AM save (Inger, Cleveland Clinic) = newly introduced stakeholders, NOTHING commercial or internal, no finance page, no dollar or return tile. Partners (Frank) = end-customer pages with the partner never named, plus partner-seller pages (workforce management partner, cloud contact center partner, systems integrator) quoting the partner's own public words.

**Own-story guard:** a blinded tile never goes on that customer's own page: training hours = Synchrony, 5.9% = McKesson, $6.1M and 26,624 = RBC, $50M+ = Wells Fargo, 8,700+ and 1,800 = Cigna, 15.4X = Optum, 21,000 = BT/EE, 7 pts = CVS/Aetna.

**Frank's self-serve skills updated Sep 18** (backup `frank_selfserve/_bak_sep18/`): `template_with_proof.html` + `proof_tiles.md`, proud-not-wound, default partner line "Brought to you by Intradiem", partner-type page mode; knowledge examples cleaned (Maximus call was Aug 6 2026, not Aug 13; Ally 30% figure was not in the primary release). Frank's Claude project needs the new files re-uploaded by hand.

**Recommendation given to Dallas (white glove vs self-serve):** both, split by risk. White glove stays for research, maps, contact data, gates, sequences and anything that sends; self-serve skills sit on top of gated material only (page picker and builder, reply and objection handler, call prep) and can recombine approved pairs and tiles but never invent a fact. Roll out one department project at a time, AEs first, watch usage two weeks. Not yet built.

**Lessons:** agents that spawn their own research workers can hand back early with nothing written; resume them with SendMessage and tell them to research inline. Most repo facts on customer accounts are internal and unusable on a page, so AM shelves need fresh primary-source research. Upstream fixes DONE Sep 18: Citi $5B date corrected in alex plans.py and the room redeployed; Frank's live Assurant one-pager (on gtm-partner-pilot, NOT save-rooms) lost its restructuring bullet. `rooms/alex_accounts/build_rooms.py` rebuilds all five rooms and wipes the shelf links every time, so `link_shelf.py` always follows it. Python urllib gets 403 from Cloudflare Pages; diff live pages with curl.

Related: [[keegan-execution-kit-sep18]], [[feedback-social-proof-ships-sep18]], [[feedback-no-draft-copy-to-ams]], [[feedback-no-claims-guidance-to-partners]].
