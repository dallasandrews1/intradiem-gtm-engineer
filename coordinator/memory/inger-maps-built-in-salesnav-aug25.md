---
name: inger-maps-built-in-salesnav-aug25
description: "As of Aug 25 2026 evening Dallas has BUILT the back-office Sales Nav maps for Assurant, Cleveland Clinic, Cox, DIRECTV; any rebuild must report ADD/REMOVE/MOVE deltas for those four (diff_built_maps.py -> BO_Map_Changes_Built.md, baseline _built_snapshot.csv) so he can go back and edit them"
metadata:
  type: project
---

Dallas: "I've already completed Assurant, Cleveland Clinic, Cox, and Directv... so please specify if you do indeed make updates or edits to those as I'll need to go back and edit them."

Mechanism: `motions/back_office_expansion/diff_built_maps.py` diffs the current `BO_Map_Build_Sheets_Inger.csv` against `_built_snapshot.csv` (taken from the Desktop copy he built from) for the BUILT set and writes `BO_Map_Changes_Built.md`; run after every rebuild and surface any change in chat explicitly. Page index shows "built in Sales Nav" for those four. Add accounts to BUILT (in both `diff_built_maps.py` and `build_bo_map_artifact.py`) as he finishes them and re-snapshot.

**How to apply:** never silently alter a built map; when a change is warranted (stale contact, missing manager, new lane), list it as an edit for Dallas's hands. Related: [[inger-account-maps-build-aug25]], [[backoffice-four-lanes-standard]].

**Aug 25 late:** built people are protected from every trim (cap, sibling cap, generic filter) and count toward the sibling cap; lane additions only fill remaining room, overflow goes to the bench (Assurant is full at 30, its six ops-technology/workforce-planning adds sit on the bench for a second map). Lane sweep deltas delivered as ADD lists: Cleveland Clinic 1, Cox 5, DIRECTV 2, Assurant 0.

**Aug 27 2026:** Dallas finished building all twelve maps in Sales Navigator. BUILT set in `diff_built_maps.py` and `build_bo_map_artifact.py` now covers all 12; snapshot retaken from the current build sheet (`_built_snapshot.csv`, 280 rows) so every future rebuild reports ADD/REMOVE/MOVE deltas for all twelve. The maps site (backoffice-maps.pages.dev) shows 12 accounts, 280 people, 31 senior executives, 12 maps built; the operating map roster reads "Twelve maps built, names to clear." Next step in the motion is clearance, not building.

**Aug 27 2026, sent:** Dallas emailed Mary Ann (cc Inger, Naveen) with the update: twelve accounts from Inger, all twelve maps live in Sales Navigator and shared with Inger, companion page https://backoffice-maps.pages.dev, offer to continue with other members of her team if she finds value. Wording rules that landed: no build-time claims, no "nothing needed from you," an offer framed on her judgment ("if you find value in this"), the SVP addressed and the AM on cc. Watch for Mary Ann's reply; the next gate is Inger marking who is fair game, then sequences for Nate ahead of all-hands (week of Sep 14).
