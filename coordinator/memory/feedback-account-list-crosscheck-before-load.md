---
name: feedback-account-list-crosscheck-before-load
description: "Sep 3 2026 rule from Dallas: before any lead loads into a motion campaign, cross-check the prospect's CURRENT company against the motion's account list in the Clay workbook (Stars = Accounts (Master) t_0thuumoUcu6wAAhovti), never just the search domain list"
metadata:
  type: feedback
---

Sep 3 2026, after the Quality fresh pull: "always double check the workbook in Clay to ensure we are always ensuring that the company these prospects are currently at are actually among the list of accounts this star ratings campaign is based off of."

**Why:** the search runs on a hand-typed domain list, the bridge returns whatever company LinkedIn shows today, and a person can sit at a subsidiary, a sister brand, or a company that left the universe (merger, tier change, customer conversion). Only the workbook's account table is the campaign's real universe; a lead whose current employer is not on it gets copy about a plan position that does not apply.

**How to apply:** after the bridge and before the lemlist load, read the motion's account table (Stars: Accounts (Master) `t_0thuumoUcu6wAAhovti`; other motions: their registry table) and match every lead's bridged current company or email domain to a parent row. Anything unmatched is benched with the reason, never loaded on the strength of the search domain. Log the match count in the roster CSV (a `universe_match` column) and on the review page. Related: [[quality-fresh-pull-sep3]], [[feedback-motion-fit-on-company-change]], [[clay-free-sourcing-path]].
