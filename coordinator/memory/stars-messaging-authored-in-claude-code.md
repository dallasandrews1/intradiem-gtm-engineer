---
name: stars-messaging-authored-in-claude-code
description: Stars messaging is authored in Claude Code, not the Clay E1 prompt; the post-Clover measure thesis is encoded in all three messaging skills with a hard expiry at the CMS October 2026 release
metadata:
  type: project
---

Sep 22 2026. Dallas decided Stars messaging is written here in Claude Code, calling it the most powerful tool available for it, rather than through the Clay E1 MessageGen prompt. That retires the Clay prompt as a build target and closes the Polar Part A look-only task that existed to find its live home.

**Why:** the Clay prompt path had an unfindable live home and carried the pre-Clover thesis, and messaging drafted here already passes the skill chain (cognitive-calibration, first-draft-engine, copy-sharpener, verified-metrics) which the Clay path did not.

**How to apply:** the post-Clover measure thesis is now encoded in all three messaging skills in `~/.claude/skills` (single copy each, no coordinator mirror): `intradiem-verified-metrics` holds the full measure set under Data sources, `intradiem-first-draft-engine` tells the drafter to read `StarRatings_Measure_Reconciliation_Clover_Sep21.md` before drafting and never to use a Stars file dated before Sep 21 2026, and `intradiem-copy-sharpener` carries the measure check in QC line 8. All three carry the same hard expiry: the CMS October 2026 release, after which the snapshot is unverified until the reconciliation doc is re-cut. Only Customer Service, and indirectly Rating of Health Plan, are measures our service operation reaches. Related: [[clover-ruling-stars-measure-thesis-sep21]], [[stars-recut-staged-sep21]], [[feedback-skills-are-the-method-not-reference]].
