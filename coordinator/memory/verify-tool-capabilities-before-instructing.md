---
name: verify-tool-capabilities-before-instructing
description: "FEEDBACK — always verify a third-party tool's CURRENT capabilities/UI (Clay especially) via its docs before giving Dallas click-by-click steps"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: ee52015b-9ac7-4c92-9a8f-4a99545ff075
---

FEEDBACK (Jun 30 2026): Before giving Dallas step-by-step instructions for any third-party tool (Clay first and foremost, also Salesforce, Outreach, etc.), VERIFY the current feature name, location, and behavior against the tool's live docs (web search / fetch) instead of instructing from memory. Do not assert UI labels or menu paths from training data.

**Why:** During the Clay build I told him to use a "Write to Table" column type. It was wrong on two counts — it's not a column type (it's under the Actions menu) and the feature was renamed. The real thing is "Send Table Data" (formerly "Write to Other Table"). He caught it, twice. Tool UIs and feature names drift constantly; confident-but-stale instructions waste his time and burn credibility mid-build.

**How to apply:** When about to give tool steps, do a quick doc check first (Clay: university.clay.com / clay.com/university / support.clay.com). If I can't verify, say so and verify before instructing rather than guessing. Cite the doc. This applies live during hands-on-keyboard sessions, not just planning. Clay specifics learned (re-verified Jul 8 2026 vs university.clay.com/docs/send-table-data): Clay-to-Clay row moves = "Send Table Data", now under **Exports** (was Actions — moved again, proving the rule); methods = Send row / Send row for each item in a list; sends are linear A→B→C (no loops; reverse-direction reads use Lookup Single/Multiple Rows, non-destructive); max 20 connected tables; "Update existing rows on re-run" toggle = dedupe behavior. Pairs with [[intradiem-cohesion-layer]] (Clay Build Pack) and the project's `Clay_Engine_Full_Architecture.md`.
