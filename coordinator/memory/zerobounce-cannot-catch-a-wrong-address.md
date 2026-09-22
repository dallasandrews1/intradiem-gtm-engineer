---
name: zerobounce-cannot-catch-a-wrong-address
description: "Proved Sep 22 2026: a wrong-company email passes ZeroBounce as valid; deliverability and correctness are different gates and the domain check must run first"
metadata:
  type: reference
---

Demonstrated on the BCBS of Michigan committee, Sep 22 2026, with real rows.

Clay's email waterfall returned `raghu@umich.edu` and `vincep@umich.edu` for two BCBSM directors. Re-running the standalone `Work Email` routine with `company_domain` forced to `bcbsm.com` returned the same two addresses, so the waterfall holds nothing else for them. Both addresses were then swept through `Net-new contact: find + verify work email` (`workflow:wf_0tk4jo5z7RjGKo3rvR8`, Work Email + ZeroBounce) and **both came back `status: valid`**, exactly like the eleven correct bcbsm.com addresses in the same run.

**The point:** ZeroBounce answers "will this mailbox accept mail," not "is this the right person's work mailbox." A personal or alumni address for a real person is a live mailbox, so it passes, and the message then sends cleanly and never bounces. Nothing downstream ever flags it. This is the concrete instance of the failure mode in [[enrichment-doctrine-clay-not-lemlist]] and [[lemlist-trial-enrichment-credits-exhausted]].

**How to apply:** run a domain check BEFORE the deliverability check, and treat them as separate gates.
1. Does the returned email's domain match the company domain on the row? If not, it is not a work email, whatever ZeroBounce says. Discard it; do not "fix" it into a pattern guess and do not send to it.
2. Only then run ZeroBounce on what survives.
3. A seat with no work address is not a blocked row, it is a **mobile-and-LinkedIn lane**. Say so explicitly in the deliverable so nobody treats it as an open gap to chase. Clay's `Enrich Person and Find Contact Details` returns a mobile for nearly everyone, which is what a calling rep needs anyway.

One caveat in the other direction: a mailbox can be right and still look odd. Leilah Mack at Vanguard is `leilah_krohn@vanguard.com`, a surname change that never reached the mailbox. Domain matches, so it ships as returned. Match the domain, not the name.

Related: [[clay-enrich-person-contact-details-routine]], [[strikerooms-bcbsm-vanguard-sep22]]
