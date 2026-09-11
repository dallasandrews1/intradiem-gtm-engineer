# Customer contact center platforms, read Sep 5 2026

> One row per Salesforce Customer account, with the contact center (ACD) and workforce (WFM) platforms their own job posts name, and the date each was last seen. Source: PredictLeads through Clay, one credit per company. File: `BO_Customer_CC_Platforms_Sep5.csv`. The same fields sit on every company record in Audiences.

## What it is for

The back-office expansion copy talks to people whose front office already runs Intradiem. Naming the platform their operation runs on, when we have it fresh, is the one line that proves the note was written for them. This file is where that line comes from.

## How to use it in copy

- Use a platform name only when `acd_fresh_12mo` is `yes`. Older reads are context for the rep, not a line in an email.
- A rep-stated fact beats the read. `rep_confirmed` carries the vendor, who said it, and when (Maximus: Verint for the back office, per Nathan, Sep 4).
- WFM is the more useful name for a back-office note than the ACD, because the back office lives in the WFM calendar. Calabrio, Aspect, Verint and NICE WFM are the ones on file.
- Blank means no public read. Say nothing about platforms; do not guess.

## The numbers, Sep 5

| | Count |
|---|---|
| Customer accounts read | 82 |
| With a vendor on file | 59 |
| With an ACD seen in the last 12 months | 35 |
| With a WFM vendor | 18 |

WFM on customer accounts: Calabrio 8, Aspect 6, Verint 2, NICE 2. Amazon Connect, Genesys and Avaya lead the ACD side.

## Where the rest lives

Every prospect read is in `tam-outbound-engine/data/cc_platform_reads_all_sep5.csv` (1,880 companies, 46 percent with a vendor). The workflow that refreshes both is `Tech stack read (PredictLeads -> Audiences company)` in Clay; the queues are `CC Platforms: needs read (Customer)` and `(Prospect)`, and they drain themselves.
