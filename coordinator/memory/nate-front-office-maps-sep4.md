---
name: nate-front-office-maps-sep4
description: Sep 4 2026: front-office maps for Nate's six built (87 people, 69 credits) as a "mode": "front_office" set on the same map pipeline; Centene two-map page for Rachel DiBello; the Aug 24 back-office Strike Room ask is still an open decision
metadata:
  type: project
---

Sep 4 2026. Audit of Nathan's asks from Aug 24-31 found two never delivered: the front-office maps for Centene, Fidelity, National Grid, Truist, Paychex and Regions (Dallas promised them Aug 31) and anything for Rachel DiBello on Centene ("Centene for Rachel", Aug 27). Both built today.

Front-office maps = set `sets/nate_front.json` with `"mode": "front_office"`; `fo_vocab.py` supplies lanes (customer operations executives, contact center and service leaders, workforce management and planning, service technology), topics, functions and an EXCLUDE list; bo_titles.configure swaps them in place, bo_gates skips the front-line gate in that mode. Back-office regens for nate and inger stay byte-identical. Sourcing: `fo_sweep.py` (Clay query-mode per lane + Audiences SF-known layer, 0 credits); Regions only resolves by company_name in Clay search. URL bridge = Clay MCP find-and-enrich-list-of-contacts, 20 names a call, transcribed into bridge_results CSVs. Live verify 69.0 credits. Result 87 people (Centene 19, Fidelity 30, National Grid 12, Paychex 4, Regions 7, Truist 15). Rachel's page = set centene_rachel (group_by map_name).

DEPLOYED Sep 4 on the house standard (Dallas: anything going to a rep is a deployed page, never a Desktop file or artifact link). backoffice-maps.pages.dev is now four pages from `motions/back_office_expansion/deploy-backoffice-maps/`: `/` Inger's twelve byte-identical and untouched, `/nate/` back office 150, `/nate/front-office/` 87, `/centene/` Rachel's two maps. Redeploy with `npx wrangler pages deploy deploy-backoffice-maps --project-name=backoffice-maps --branch=main --commit-dirty=true`. Builder gained optional `sibling_links`/`sibling_label` (hero companion row, CSS emitted only when present so old pages rebuild byte-identical). Nothing sent to Nathan or Rachel yet.

Still open: Sales Nav build of all twelve Nate maps (Dallas's hands), whether to build a back-office-only Strike Room (Aug 24 ask, Enterprise-owned artifact), Nathan's Financial Services copy verdict.

**How to apply:** any rep's front-office map request = copy sets/nate_front.json, set accounts, run fo_sweep -> filter_sweep -> bridge (MCP) -> apply_bridge -> build -> verify_live -> sf_check --only-map -> build -> check_all -> build_bo_map_artifact. Related: [[nate-six-accounts-bo-maps-aug31]], [[bo-map-pipeline-rep-sets-aug31]], [[nate-bo-review-maximus-sep4]].
