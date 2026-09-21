---
name: stars-refresh-rehearsal-sep21
description: Sep 21 2026 rehearsal wired refresh_oct_release.py end to end; found CMS re-issued the 2026 Summary Ratings (34 universe contracts changed, 21 now at or above 4.0) and that lead variables lack a measure-level read
metadata:
  type: project
---

Sep 21 2026: `october-flywheel/refresh_oct_release.py` went from skeleton to wired. It finds CMS tables by name at any folder depth (CSV or XLSX), decodes UTF-8 first with cp1252 fallback, matches the 19 addressable measures by NAME through `october-flywheel/addressable_measures.json` (CMS renumbers codes every cycle), and emits per-contract `service_measures_down` / `service_measures_up` plus a contract x measure table. Rehearsed with 2026 as new and 2025 as prior; validated 98 of 98 on 2025 overall stars against `CMS_Star_Movement_25v26.csv`. Outputs in `october-flywheel/rehearsal_25v26/`, log in `automation/logs/stars-refresh-rehearsal-2026-09-21.md`.

**Finding that matters now:** cms.gov rebuilt the 2026 ZIP on Aug 17 2026 with Summary Ratings re-issued Jul 22 2026. 34 of 307 universe contracts have a different 2026 overall star, 33 higher, 21 now at or above 4.0 (about 1.12M members, $127.4M modeled addressable). Clover H5141 went 3.5 to 4.5. The universe file, tiering and any lead's `qbp_avg` still reflect the Oct 8 2025 table. Reason for the re-issue not confirmed. List: `rehearsal_25v26/Universe_2026_Reissue_Diff.csv`.

**Why:** a copy line stating a plan's rating can be wrong for those parents, and a plan that now earns the bonus is not a Stars target.

**How to apply:** before the messaging correction ships, re-check every live Stars lead's parent against the diff file. In October run with `--prior-zip october-flywheel/2026-star-ratings-data-tables_reissue-aug17-2026.zip`; without a prior ZIP new fallers cannot be detected at all. Still manual: QBP re-modeling, customer-file join key, PARENT_ALIASES. Related: [[naveen-gtm-physics-stars-relaunch-sep21]], [[october-refresh-runbook-v0]], [[star-ratings-universe-vintage]].
