# Proposed Email 1 edit, BO Net-New - Back Office (Nate) cam_DNErdZPANvC2sqRCK (Sep 2 2026)

Step: stp_fgmFp3zcdyuGEYkbF (Email 1, subject `two clocks`), sequence seq_tegzQbC5PCQ78qHBm. Campaign holds zero leads, so the edit is safe by API. NOT applied; waits for Dallas's go.

## Before (live today)

Hi {{firstName}}, there's a blind spot most back-office operations share: the contact center gets managed minute by minute, while {{function}} runs on yesterday's report. Same company, same pressure on cost, two different clocks. The gap shows up as idle windows nobody can see while they're open, and overtime approved after the fact to clear work that could have been absorbed in the moment.

Might be helpful to walk through how operations teams are starting to close that gap.

Worth 15 min in the next few weeks?

Nathan

## After (chosen Sep 2, Dallas delegated the call)

Hi {{firstName}}, {{opener_line}}

The pattern underneath is one most back-office operations share: the front office gets managed minute by minute while {{function}} runs on yesterday's report, so idle windows go unseen and overtime gets approved after the fact.

Might be helpful to walk through how operations teams are closing that gap without adding headcount.

Worth 15 min in the next few weeks?

Nathan

## The six opener_line values (account level, carried on every staged row; each follows "Hi {{firstName}}, ")

- Centene: your CFO framed this year's optimization as adapting to volume changes with fewer people, and claims, appeals and enrollment feel that first because the work doesn't shrink on the same clock as the headcount.
- Fidelity: Fidelity is building its own workforce-management platform for the phone side, which leaves an open question for the processing queues behind it, where the day's work lands on a different clock.
- National Grid: three National Grid companies missed the New York call-answer standard for 2025, and with New York and New England now under one US president, intraday capacity in billing, collections and customer operations is squarely on the table.
- Truist: a new CEO on a 90-day clock and an expense line held near flat means every operations leader at Truist is about to be asked what capacity can be freed without adding headcount.
- Paychex: Paychex just published that one in five service conversations now closes with no person on it, which makes the other four the operations question: the queue that's left is lumpier and harder to staff than the one you had.
- Regions: Regions reaffirmed flat expense growth in the same year deposit operations runs a legacy core beside a Temenos pilot, with the migration wave landing in 2027.

Why this version: the first line is about the reader's own company and this month, in their own public words, which is the strongest reply driver a cold email has; the two-clocks idea stays as the second paragraph so the sequence's later steps still land; the CTA now names the constraint ("without adding headcount") that every one of the six accounts is publicly under. Word count 95 to 115 per account, inside the E1 range. Gate: prospect facts only, no Intradiem figure, no customer claim, no product tell, contractions throughout.

## Apply (agent-buildable)

`python3 apply_e1_opener.py --go` reads the After block, PATCHes the step by API, re-reads the sequence and prints the stored message. Applied Sep 2 2026 on Dallas's delegation, while the campaign held zero leads.
