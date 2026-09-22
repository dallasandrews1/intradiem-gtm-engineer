---
name: contract-identity-check-sep22
description: "Sep 22 2026: a staged Stars email named a contract as the wrong product line and two copy reviews missed it, because reviewers check quote fidelity and never check contract identity against the CMS marketing_name column"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: eb7aa043-b846-44a2-9ee2-93981bef4bc7
  modified: 2026-09-22T17:48:41.543Z
---

Sep 22 2026, building the Stars relaunch three-part sequence: a rendered Email 1 called H8330 "the Harvard Pilgrim contract" at Point32Health. The CMS universe file's `marketing_name` column says H8330 is a Tufts Health Plan contract, and Point32Health's other Tufts contracts sit at 4.0. The quote paired with it (Patty Blake, "unprecedented eighth year" at 5 stars) was about Tufts Medicare Preferred. The email would have told a Point32Health reader their Tufts book was the weak one, on their own brand. Kristen Dowd, VP of the Medicare Stars Program there, is a loaded lead and is the "Kristen" in Naveen's Jul 22 sample email.

Two gtm-copy-reviewer passes ran on that file and neither caught it. Both verified the quote against the research CSV and the numbers against the Value Repository. Neither checked whether the contract ID belonged to the product line the copy named, because nothing in the gate asks for that.

**Why:** a wrong rating is survivable, a wrong product line is not. The reader knows their own contract portfolio cold, and it is checkable in seconds. The failure mode is invisible to a quote-fidelity review because every quoted word is correct.

**How to apply:** before any Stars copy ships, join every contract ID in it to `marketing_name` and `members` in `october-flywheel/rehearsal_25v26/StarRatings_Universe_2026.csv` and confirm the product line the copy names. Same check when a parent has a proud public rating beside an under-4 contract: find which contract the proud statement is about before pairing them. Add the contract-identity line to the copy-review prompt, since the reviewer will not invent it. Related: [[stars-relaunch-mined-lines-sep22]], [[stars-refresh-rehearsal-sep21]], [[talking-points-defend-before-delivery]].
