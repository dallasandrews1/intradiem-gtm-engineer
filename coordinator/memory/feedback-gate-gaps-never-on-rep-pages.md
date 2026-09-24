---
name: feedback-gate-gaps-never-on-rep-pages
description: A build gate's gap (Salesforce record unread, stale export) is never printed on a rep-facing page; it stays in the terminal and the log, and the gap gets fixed, not displayed
metadata:
  type: feedback
---

Sep 23 2026. Dallas saw "SALESFORCE FRESHNESS MISSING: keegan/vanguard" while deploying and Frank's PennyMac call plan carried "Built before the Salesforce record was read" on the live page: "why would I show them an error like that... that reflects on ME and our build. If Salesforce freshness is missing then fix it, don't give them anything that they need to fix because they can't."

**Why:** a rep cannot act on a build gap; on their page it reads as our error and undercuts the whole build.
**How to apply:** sf_freshness.stamp() is silent unless FRESH (changed Sep 23). Any builder that stamps provenance shows a date when it has one and nothing otherwise. The gap goes to automation/logs and gets closed by reading the record. Same rule for any gate: fix upstream, never surface downstream. See [[sf-freshness-gate-sep21]], [[deliverable-strength-framing]].
