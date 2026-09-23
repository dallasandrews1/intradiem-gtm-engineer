---
name: feedback-next-moves-must-read-alone
description: Sep 23 2026 - next-move lines on rep pages must make sense by themselves - a verb, the person and role, one short reason; plain_moves.json holds them
metadata:
  type: feedback
---

Dallas, Sep 23 2026: the next-move statements at the front of every master link "need to be easier to understand. I don't know what they mean by themselves", so they don't give AEs and AMs immediate value.

**Why:** plan shorthand ("The claims door: X", "Confirm the record", "gates everything after it", "known layer", "wave two", "Salesforce next action date: ...") is written for the builder, not the rep. A rep reading only the hero line has to know what to do, with whom, and why.

**How to apply:** every move shown on a rep page starts with a verb the rep does (or names who does it for them), gives the person with their role or team, and adds at most one short reason. Banned on rep-facing lines: door, layer, lane, gate, record (say "Salesforce account"), wave, sponsor line, alias. The overlay lives in motions/shared/plain_moves.json, keyed slug|text. The index build prints any live move with no plain version, so write one whenever a plan gets a new move. Related: [[feedback-seller-pages-no-fluff]], [[rep-index-pages-sep20]], [[feedback-keegan-room-is-the-bar]].
