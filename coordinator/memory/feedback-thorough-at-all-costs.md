---
name: feedback-thorough-at-all-costs
description: "Dallas's Aug 25 2026 rule after a tie-splitting bug silently moved cards on a map he had already built in Sales Nav: never half-do a check; be thorough at all costs; every rebuild runs the full pre-publish gate (check_all.py) before anything is published or synced"
metadata:
  type: feedback
---

Aug 25 2026: "don't half ass anything like that ever again. you have to be thorough with this at all costs." Trigger: a global tie counter reshuffled Assurant's reporting lines when Goldman changed, on a map Dallas had already built by hand; earlier the same day a hasty Goldman trim removed a legitimate operations leader (Chelsey Jurgielewicz).

**Why:** every card on these maps costs Dallas hand-clicks in Sales Navigator and credibility with the AM; a silent change means rework and lost trust.

**How to apply:** `motions/back_office_expansion/check_all.py` is the gate: URLs and titles present, level parsing sane, no inversions or dangling managers, cap and density, no generic titles, no excluded or AM-map people on a map, built-map diff, audit. Run it after every rebuild; publish only on exit 0 and only after reading the built-map diff. Determinism matters: per-account tie handling, pinned reporting lines on built maps. Related: [[inger-maps-built-in-salesnav-aug25]], [[feedback-guess-and-label-sales-validates]].

**Aug 25 night lesson:** a broad title regex ('controller', 'banking') silently removed Goldman's Transaction Banking operations line and Assurant's CAO from a built map; the gate passed because removals on built maps were only a diff, not a failure. Now any REMOVE or MOVE on a built map is a hard FAIL in check_all.py, and every filter change gets its removal list read name by name before rebuilding.
