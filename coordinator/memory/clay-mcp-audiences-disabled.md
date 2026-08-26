---
name: clay-mcp-audiences-disabled
description: "The connected Clay MCP cannot read Dallas's built tables; Audiences is disabled for the workspace"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 8b3b4535-2af4-4064-b1d6-02433f0b1779
---

As of Jul 9 2026, the connected Clay MCP returns a hard error on `query-objects` and `ask-question-about-accounts`: "Clay Audiences is not enabled for this workspace, so no accounts are accessible through MCP. Only a Clay workspace admin enabling Audiences will resolve this." `list_subroutines` is empty. So the Clay connector here exposes only prospecting tools (search-contacts, enrich, find-and-enrich-company, add-data-points) plus Audiences-based account queries that are switched off. It CANNOT read Dallas's custom tables (e.g. the Star Ratings contract table, the [[contacts-table-finalized-jul9]] buying-committee table).

**How to apply:** To use Dallas's Clay data (contract star ratings, counts, enrichment values), ask Dallas to export/paste the rows (CSV) and parse locally. Do not claim the pull is impossible without naming this specific error, and do not invent numbers from his tables. This is why the Centene 3.5-contract count stayed count-safe in [[star-ratings-addressability-cut]] outreach.

CORRECTION (Jul 24): Audiences is an Enterprise-tier feature, not a per-workspace toggle a workspace admin can flip. Confirmed by Dallas ahead of the [[matthew-quan-clay-cli-outreach-jul24]] call — dropped from the ask list to Matthew Quan since it's not solvable there. Dallas's actual play: get Clay's CLI/API opened up further to build faster and prove ROI, which is the argument he'll bring to his ELT to justify the Enterprise-tier spend (which would include Audiences).

UPDATE (Jul 24, later same thread): Matthew Quan confirmed via email Audiences is "opening up to all," will likely hit Enterprise first for load testing, and he personally committed to getting Dallas ungated early. Also confirmed a table CRUD API is in active development ("similar to table API"), directly validating the #1 ask in [[matthew-quan-clay-cli-outreach-jul24]]. Both blockers are moving, not dead ends — don't treat this file's "Enterprise-only, no path" framing as current without checking the Jul 29 call outcome first.
