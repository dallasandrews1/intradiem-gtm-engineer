---
name: feedback-am-gate-removed-nate-reviews-sep2
description: Sep 2 2026: Dallas removed the AM-clearance filter on the back-office customer lane; names load into the vertical lemlist campaigns and Nate reviews them there before starting; the call step's "cleared" now means Nate-reviewed
metadata:
  type: feedback
---

Sep 2 2026, Dallas: "remove the filter for AMs clearing names, we can let Nate review the names after they've been uploaded to the campaigns." The owner_cleared / brand_safe gate no longer blocks a load. Customer-lane rows go into the four vertical campaigns with the neutral `enterprise_line` (brand_safe stays FALSE until an AM says otherwise), Nate prunes in lemlist, and the call task's "cleared names only" is Nate's judgment per name. The freshness and two-source email checks stay; they caught 13 leavers and 7 address variants on the first customer wave.

**Why:** waiting on AM clearance had produced zero cleared names in nine days; Dallas would rather Nate review a loaded list than wait on a sheet.

**How to apply:** stage six per account (executives first), run Enrich Person freshness plus the Work Email two-source check, load ready rows, hold the rest, tell Nate what to review. Loader: `motions/back_office_expansion/load_customer_wave.py`. Related: [[bo-expansion-council-aug24]], [[bo-netnew-package-sep2]], [[feedback-no-tasks-for-ams]].
