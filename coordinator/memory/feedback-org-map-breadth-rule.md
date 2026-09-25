---
name: feedback-org-map-breadth-rule
description: Sep 25 2026 - an org map row never runs wider than six non-leaf siblings; large leaf sets sit under a titled sub-lead and render as a grid; Rachel's 28 to 35-card maps broke on the renderer Keegan's 17-card maps used
metadata:
  type: feedback
---

Dallas, Sep 25 2026, on Rachel's Wells Fargo map: "The org chart under andrew freymann is very oddly put together it shouldn't be one long line like that", "same with jeff Combs", then "you actually messed up and reverted to an odd layout ... let's fix all of that".

**What it was:** the renderer (build_bo_map_artifact.py) was unchanged; it stacks a leader's all-leaf reports in one column when there are more than four, and centers wide rows so they spill off the left edge. Keegan's maps (17 cards, rows of seven at most, six top cards by hand, Sep 17) never hit it. Rachel's maps (28 to 35 cards, rows of 9 to 15) did.

**Rule:** hand-place every map so no non-leaf row exceeds six siblings; the most senior title in a function becomes the sub-lead for the rest (an SVP Customer Service Executive takes the site and division leaders, a Head of WFM takes the planners); leaf sets under a sub-lead render as a 3-column grid; wide trees scroll from their left edge, never clipped. Check every map by render before hand-over, not only the room. Related: [[keegan-three-account-package-sep17]], [[ae-package-review-rules-sep25]], [[feedback-render-before-calling-it-live]].
