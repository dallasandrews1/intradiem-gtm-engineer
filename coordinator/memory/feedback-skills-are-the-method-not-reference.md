---
name: feedback-skills-are-the-method-not-reference
description: "Dallas, Sep 21 2026: reading a doctrine file is not the same as running the skill; run cognitive-calibration then the domain skill BEFORE drafting, not after a reviewer catches it"
metadata:
  type: feedback
---

On the Frank QuickStart call cards Dallas asked "did you use the cold call playbook skill at all?" The honest answer was no: the doctrine files (`Cold_Call_Playbook_Aug2.md`, `Messaging_Doctrine_Sep3.md`) had been READ and applied by hand, and two adversarial reviewers ran afterward. The skills themselves (`cognitive-calibration`, `intradiem-first-draft-engine`) were never invoked.

**What that cost, measured:** 72 cards ran on 14 shared tracks. Four Highmark VPs got word-for-word identical copy with one noun swapped, and all 72 shared a 35-word product sentence that was a category label ("recover productive time, an earlier read on where demand and capacity are out of balance"). The first-draft engine's Gate 2 forbids two people in one account sharing an idea; Gate 3 forbids category labels and demands concrete actions. Both were broken at scale, and a reviewer pass does not catch template creep because each card passes on its own.

**Then calibration caught the second-order failure:** after writing 21 per-person angles, 39 people still shared copy. That is FM-04, point-fix without generalizing: fixing the four names Dallas saw rather than the class. The fix was a title-keyed angle layer, taking 72 cards from 14 to 58 distinct engage blocks, with the only remaining shares being genuinely same-title peers (four Directors of Operational Excellence).

**How to apply:** run `cognitive-calibration` first, then the domain skill, BEFORE drafting. When a repetition or quality defect is found, measure the whole set programmatically (count distinct rendered outputs) instead of fixing the named instance. Related: [[feedback-talking-points-defend-before-delivery]].

**Round two of the same lesson, same night (Dallas: "these call scripts just flat out aren't good... look at the structure and framework and natural energy smoothness inside the description of the skill"):** the skill he meant was `league-cold-call-playbook`, which I had never opened; I had built on `Cold_Call_Playbook_Aug2.md` (the four-beat opener) instead. The playbook's engine is different: one data-backed forcing function, a TWO-CHOICE friction prompt inside ten seconds ("what's the bigger risk right now: A, or B?"), a "reason I ask" expansion about seams not systems, a pressure-test ask ("would you be opposed to a ten-minute pressure-test..."), four mandatory handles, a 25-second voicemail with one data point and one thing of value. Rebuilt all 72 cards on it (talk_tracks.py `card()`, FRICTION + SUBFRICTION). Where the League skill and the Intradiem doctrine disagree, the doctrine wins: "quick question" is banned there, so it was cut. The floor reviewer's rule for A and B: each a risk that operator would actually pick, under ten words, in that seat's nouns; never the consequence of the other. When Dallas names a skill by its shape, open THAT skill file before writing a line.

**The fork rule, worth keeping for every future call card:** A and B are each a risk that operator would actually pick, under ten words, in the seat's nouns, and never one the other's consequence. Half of the first-pass forks failed it; the failures were "A isn't a risk" and "B is the consequence of A". Measure it programmatically (word counts, distinct forks) before any reviewer sees it.
