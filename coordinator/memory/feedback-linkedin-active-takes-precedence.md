---
name: feedback-linkedin-active-takes-precedence
description: "Dallas's Aug 25 2026 rule: contacts who are active on LinkedIn take precedence over dormant profiles when choosing who goes on a back-office map and who gets outreach; the free sourcing path carries no activity signal, so it must be added (Sales Nav 'posted in past 30 days' filter, or a paid activity enrichment with a go)"
metadata:
  type: feedback
---

Aug 25 2026: "I don't want you missing the contacts that are actually active on LinkedIn either. those contacts take precedence over someone who has a dormant LI profile."

**Why:** the sequence is email then LinkedIn; a dormant profile never sees the connect or the message, so an active director beats a dormant VP for the map's purpose.

**How to apply:** `inger_backoffice_candidates.csv` now carries `li_active` (yes/blank) and `li_last_post`; `build_map_build_sheets.py` ranks active profiles first for the 30-lead cap and the sibling cap and writes `li_active` to the sheet; the page shows a green "active on LinkedIn" tag. Populate the column from Sales Nav (filter "Posted on LinkedIn in past 30 days", free, Dallas's hand) or a Clay activity enrichment (credits, 10-row test and estimate first). Related: [[inger-account-maps-build-aug25]], [[feedback-org-chart-density]], [[signals-134-build-aug25]].
