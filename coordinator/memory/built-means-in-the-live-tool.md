---
name: built-means-in-the-live-tool
description: "FEEDBACK: \"built\" means built in the live tool (Clay), not just the repo engine/spec"
metadata:
  node_type: memory
  type: feedback
  originSessionId: d2d0c444-41ee-442e-a010-f7d16111c9e2
---

Jul 13 2026: Dallas pushed back — "you didn't actually create the new motion? I don't see it in Clay." Claude had described the back-office motion as "built/wired/waiting" when only the repo-side engine (Python scorer, config, universe CSV, specs) existed; nothing was in Clay yet.

**Why:** Dallas measures "built" by what exists in the live operating tool his team actually uses (Clay tables/campaigns), not by what's modeled in the repo. The repo engine is the spec/brain; it is NOT the deliverable on its own. Saying "wired into the engine" blurred a Python model with a live Clay table.

**How to apply:** When a motion/table/campaign is the goal, build it in the live tool (drive Clay via Claude-in-Chrome — the Clay MCP is read/enrich only and can't create tables; Audiences disabled). Don't describe repo-side work as "built/live/waiting to be used" when the thing that actually runs the motion (the Clay table + columns + campaign) doesn't exist yet. State plainly what's in the repo vs what's in Clay. Ties to [[no-finished-product-framing]] and [[backoffice-motion-forked-jul13]].
