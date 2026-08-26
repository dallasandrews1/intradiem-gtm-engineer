---
name: claygent-builder-verified-jul26
description: Verified (via clay.com docs + blog, Jul 26) what Claygent Builder/Sculptor actually is, how it deploys, and how it bills, after a separate Claude Chat session recommended it
metadata:
  type: reference
---

Claygent Builder + Sculptor (Clay's conversational agent builder) is real, launched May 2026. Confirmed mechanics:

- **Deploys as a Saved-Claygent AI column on a Table** (Tools -> AI column -> Claygent options -> Saved Claygents), NOT confirmed as a node type invocable directly inside a Workflow. Docs and blog only describe table deployment.
- **Testing is free**: up to 10 inputs per session against real or synthetic data, refreshable, no credit cost. Production runs bill "one action per run plus data credits" (not a flat number).
- **Versioning**: every edit auto-saved, full diff history, one-click rollback to any prior version. Build once in Builder, every deployed table location updates together.
- **UI-only**: no CLI/API access found for Claygent Builder itself (consistent with the existing AI-columns-are-UI-only wall, see [[clay-motion-selfserve-path]]).

**RESOLVED Jul 26:** Claygents and workflow-native agent nodes are two separate mechanisms in Clay, confirmed via clay.com/claygent + the plugin's own workflows-vs-tables framing. A Claygent's only documented homes are a Table column or an Audience (bulk, no row-limit variant) — nothing shows it as an invocable Workflow node. So the other Claude Chat's #1 recommendation, "migrate MessageGen v2.1 into Builder," is NOT a version-history upgrade to the same thing — it would mean pulling MessageGen back OUT of the live Stars workflow (wf_0tiegzuo3PzJ4UtUGFA) onto a table, reversing the Jul20 fix that moved it in-workflow specifically to stop the clay_function-tool-node stalling bug (see [[clay-workflow-execution-gotchas-jul20]]). Verdict: don't migrate MessageGen, ever, unless the workflow architecture itself changes. Claygent Builder's real fit is row/Audience-level judgment calls on table data (qualification, persona classification, change-detection) — not generation logic that has to run in lockstep inside a live send sequence.

**What IS solid to build now, no workflow interaction:** company-level judgment agents that live standalone on a table — back-office qualification (gates Mandate 3), persona classification behind a title prefilter, change-detection on the Tier A+B parents. These don't touch the fragile Stars/WFM workflow architecture at all.

See [[clay-credit-belief-repeatedly-stale]] for the credit-math correction that came with the same advice.
