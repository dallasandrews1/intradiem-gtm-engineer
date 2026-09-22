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

EXTENSION, Sep 21 2026 (Dallas, drafting the Greenlight ask to Jason Dowden): the rule also governs how Dallas's own gates and tools are DESCRIBED to anyone outside GTM. Never frame a gate as compensating for rep carelessness. "Reps work accounts off records nobody's read" was cut because it is unsupported and because an SVP could repeat it to Sales. The true and safer framing is that context gets written down and cannot reach the next person who needs it, a retrieval problem (the Salesforce notes field caps at 255 characters everywhere Dallas can pull from), never a behavior problem. Dallas's words: "assuming reps work off of records nobody's read is not smart, but it is true that we need to make context something that never falls through the cracks."

Related: [[alex-record-sheets-next-sep20]], [[feedback-seller-pages-no-fluff]], [[wfm-adjacency-customer-leak-open]], [[greenlight-bespoke-agent-workaround-sep21]].


**Sep 21 2026 addendum (Frank QuickStart):** never report a rep's own intel back to them as confirmed ("your Heather test passed"). What they told you is fact; confirming it reads as doubt. Only report what the check found that they did not already know.


**Partner intel, Sep 21 2026 (Dallas on 3xG's S&P servicer figures):** a figure a partner attributes to a NAMED document they can open (a paywalled S&P servicer evaluation) is usable and carries that document as its source, even when Claude cannot open it. What stays held is a figure attributed to nothing, or contradicted by what could be opened. Wound-type figures (turnover, penalties, metrics below peers) go on a card as caller-side context, never as the opener.
