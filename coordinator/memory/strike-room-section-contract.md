---
name: strike-room-section-contract
description: "Every strike room uses the same eleven sections in the same order, §0 to §10, because the field guide navigates by number"
metadata:
  type: reference
---

Fixed Sep 22 2026 after a heading rename silently broke it. The field guide at strike-room-guide.pages.dev tells a rep "§6 is the only part you open right before the call" and "if a fact is not in §3 or §7 it does not leave your mouth". That only works if every room numbers the same way.

**The contract, §0 to §10:**

| § | Holds |
|---|---|
| 0 | What holds this account. If nothing does, say so explicitly, that is information |
| 1 | The forcing function |
| 2 | Account rules |
| 3 | Account snapshot, every fact with source and date |
| 4 | The committee |
| 5 | Cadence, or the call track |
| 6 | Per-seat angles, or the written copy. One idea each |
| 7 | What we can say, and what we cannot |
| 8 | Coordination |
| 9 | What happens next |
| 10 | How this was sourced |

A room may name a section for its own motion (§4 "Who Naveen calls" rather than "The committee", §5 "Naveen's call track" rather than "Cadence"), but the **number and the slot never move**. A phone room and an email room differ only in what fills §5 and §6.

**The failure this prevents:** renaming or reordering one room's sections is invisible in that room and breaks the guide for every other room. BCBSM had drifted to 6=what we can say, 7=live-call levers, 8=the copy, with no §0, so a rep following the guide landed in the wrong place twice. Live-call levers became a subsection of §7; coordination was pulled out of §5 into its own §8.

**Check before shipping any room:** diff the `^## ` lines of the new room against an existing one. They should be 0 through 10 with nothing missing.

Related: [[strike-room-guide-deployed-sep22]], [[strikerooms-bcbsm-vanguard-sep22]], [[feedback-no-fluff-scannable-deliverables]]
