---
name: stars-child-shells-sep26
description: "Sep 26 2026: six Stars trigger-cohort child campaign shells exist in lemlist as DRAFT with zero leads (ids in automation/logs/stars-child-shells-2026-09-26.md); Email 1 A/B and LinkedIn message rewritten per cohort, DWO named with Queue Optimizer on the side; calls and emails 2-3 still carry the parent lane copy"
metadata:
  type: project
---

Six child campaigns duplicated from the live Quality lane (five) and Finance lane (one) on Dallas's Sep 26 ask, gate closed. Names follow the Sep 22 proposal cohorts in plain words: A service measure dropped, Close to 4 stars big Medicare book, New Medicare or quality exec, Fell while their market rose, Talked about Stars publicly, Growing faster than service. All `(Nate)`.

**How the write was done, reuse it:** lemlist REST `PATCH /sequences/{seq}/steps/{stp}` REQUIRES `type` in the body (`{"type":"email","message":...}`), otherwise 400 "Type is required". Variant B goes through the connector's `set_ab_variant` (REST PATCH does not reach it). Script `motions/star_ratings/child_shells_sep26/shells.py` (dry run by default, `--apply` writes and reads back).

**Still owed before any launch:** per-cohort `vm_hook` values and emails 2 and 3 per cohort; cohort membership from the trigger scoring; customer exclusion at load; the group's nine-on-ten; Dallas's go. The proposal's rule stands: the trigger decides why we write today, the measure read is the payload.

Related: [[stars-trigger-cohorts-sep22]], [[naveen-gtm-physics-stars-relaunch-sep21]], [[john-exec-brief-biweekly-sep26]].
