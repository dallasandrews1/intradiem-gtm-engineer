---
name: feedback-rep-word-is-the-truth
description: "Sep 20 2026 feedback: what an AM, AE or partner tells Dallas about an account is the truth; if they say it is a customer, that is fact, and a system that disagrees is the thing to correct"
metadata:
  type: feedback
---

Dallas, Sep 20 2026, mid-build on Alex Bauer's record sheets: always default to whatever the AMs, AEs and partners say is the truth. If they say an account is a customer, that is fact.

**Why:** the rep owns the account and knows it; Salesforce as it reaches Clay is incomplete (the Jul 10 Active Customers export holds Customer records for Citicorp Credit Services, AT&T Enterprise Group and Elevance Health that the Clay sync does not surface at all). Treating a system read as a veto over the rep produced "Citi is a Prospect, treat as net-new" on Alex's pages when Alex is the account owner of a Customer record.

**How to apply:**
- Never frame a rep's statement as something to confirm. Where a system disagrees with the rep, the row reads "your word stands, Salesforce to correct" and names who fixes the record (RevOps).
- Only ask the rep to settle a value when their OWN sources carry two values (Synchrony 5,700 seats vs 6,347 agents; Stacy Willis vs Stacy Tope).
- Customer status from a Clay Audiences read is a sync fact, not an account fact. For exclusion gates this cuts one way only: a rep saying "customer" always excludes, even when Clay reads Prospect.
- OPEN, Sep 20 2026: the live Citi and Elevance rooms still say "no Citi record reads Customer", "treated as net-new" and "no parent record". Dallas said leave the wording for this build before he gave this rule; it now conflicts with the rule and needs his call.

Related: [[alex-record-sheets-next-sep20]], [[feedback-seller-pages-no-fluff]], [[wfm-adjacency-customer-leak-open]].
