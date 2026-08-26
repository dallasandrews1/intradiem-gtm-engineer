---
name: feedback-org-chart-density
description: "Dallas's Aug 25 2026 rule for back-office org charts: don't pad a map with many interchangeable same-title directors (DIRECTV had nine 'Director, Business Operations'); show the structure with two or three per manager, bench the rest"
metadata:
  type: feedback
---

Aug 25 2026, on the DIRECTV map: "is it really necessary to have that many director of business operations included?" No. The map's job is to show who runs the back office and how it's structured; a wall of identical director cards adds nothing for the AM and crowds the 30-lead cap.

**How to apply:** `build_map_build_sheets.py` caps same-level, same-function siblings at three per manager (senior/executive directors first), overflow goes to `BO_Map_Bench_Inger.csv`. Prefer breadth of functions and the management layer over depth in one function. Related: [[inger-account-maps-build-aug25]], [[feedback-no-showy-deliverable-copy]].
