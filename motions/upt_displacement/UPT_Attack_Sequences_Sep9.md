# UPT displacement: Verint attack and NICE attack sequences (drafted Sep 9 2026)

Sender: Nathan Belfield. Product: User Productivity Tracking (UPT), the desktop layer of the platform. Lists: `lists/verint_estate.csv` (60 prospect accounts) and `lists/nice_estate.csv` (146), Audiences segments in `lists/segments_made.json`. Doctrine: `motions/shared/Messaging_Doctrine_Sep3.md` including the Sep 4 pressure standard. Every Intradiem number below traces to a VERIFIED row in `04-value-repository/Intradiem_Value_Repository.md`; the back-office lines are the two blinded stories marketing lists as usable.

## The one idea, per attack

**Verint attack.** The desktop analytics report tells you where last week's idle time went. Intradiem sees the same desktop and acts on it while the window is still open: a coaching session, a training module, a break moved, a case pulled forward, on top of the Verint WFM you already run. Insight you already own becomes action you didn't have to staff.

**NICE attack.** Same idea, different starting point: the desktop analytics that came bundled with CXone shows the number and stops. Intradiem sits alongside CXone and turns the number into the next action. Never "replace NICE"; always "alongside CXone."

Rule that governs both (competitive-intel skill, Sep 3 doctrine): the wedge is the desktop-analytics module, never the WFM or the ACD. We integrate with Verint WFM and NICE; the UK base runs NICE IEX WFM. A line that disparages the layer breaks our own integration story.

## Who gets which angle (no two people at one account share one)

| Lane | Persona (title on file) | Angle | Worldview line |
|---|---|---|---|
| FO estate owner | Head of WFM, Director Real-Time or Command Center, Director Workforce Planning | The intraday layer the desktop report never finished. Practical, sits on top of the WFM they run. | "The report says where the idle time was. Nobody had a hand free to do anything with it." |
| FO ops director | Director or VP Contact Center Operations, Customer Care | Scale and timing: recovered minutes fund coaching without service dipping. | "Coaching happens when we're quiet, which is never." |
| FO performance | Director Operational Excellence, Performance, Quality | The last unmeasured variance, now measured and acted on. | "The biggest number never makes your dashboards, and when it does, it's history." |
| BO claims and shared services | VP or Director Claims Operations, Shared Services, Payment Ops, Document Processing | The backlog is a timing problem. The idle windows already inside the week are the capacity. | "The backlog cleared by Friday grows back by Monday." |
| VITO (COO, CAO) | Already in the DWO Executives campaign at 55 of these accounts | Air cover only, after an operational thread is live. Do not double-sequence. | |

## Cadence (Sep 4 pressure standard)

Four weeks, 18 business days, sixteen touches, one new thing per step, one breakup at the end.

| Day | Step | Note |
|---|---|---|
| 1 | Email 1 | Dated signal, what we do in one sentence, one question, no calendar |
| 1 | LinkedIn profile visit | |
| 2 | LinkedIn connect | Note under 300 characters, references the email |
| 3 | Call 1 + voicemail | Points at the note in their inbox; EA route if no direct line |
| 4 | Email 2 (in thread) | One new number, shorter than Email 1, direct ask allowed |
| 6 | LinkedIn DM 1 | Short version of Email 2 plus the conversation offer |
| 8 | Call 2 + voicemail, same-hour "just tried you" email in thread | Carries the number |
| 9 | LinkedIn like | On a recent post, only if one exists |
| 11 | Email 3, new subject on the vertical peak | Opens thread two |
| 13 | LinkedIn DM 2 | |
| 15 | Call 3 + voicemail | This-year-or-next question |
| 15 | Email 4 (thread two) | Names the colleague as a fact where the account has two seats |
| 17 | LinkedIn DM 3 | Names the colleague |
| 18 | Email 5, breakup | Under 60 words, names the re-entry condition, withdraws nothing else |
| 19 | Pending invite withdrawn | |

Phones are sourced before the campaign starts. All seats at an account enter the same day so the colleague line is true by day 3.

## Dated signal rule (sentence one of Email 1)

In order of preference, filled per lead at load, and the email does not ship without one:
1. A SKU signal on the account under 90 days old: a job posting naming Desktop and Process Analytics, Desktop Analytics, RTA or "desktop analytics", a LinkedIn profile at the account listing the product, a vendor case study or conference talk. This is the strongest opener because it proves the category is bought and staffed.
2. A war-room trigger at the account (`triggers.csv`).
3. The vertical peak line (the DWO Rule B lines, dated): open enrollment Oct 15, the Q4 claims and renewal peak, year-end close, winter season, holiday peak, device season.

## Verint attack, FO estate owner (Head of WFM / Real-Time)

**Email 1** · subject: `idle minutes at {{companyName}}`

Hi {{firstName}},

{{signal}}

Your Verint desktop reports already show where last week's idle minutes went. Seeing them was never the hard part; nobody has a hand free for a window that's open nine minutes at 10:40.

*Tier D variant (stack read shows Verint WFM only, no public or rep signal for the desktop module; 45 accounts): replace the paragraph above with:* "The WFM and adherence data you already run show where last week's idle minutes went. Seeing them was never the hard part; nobody has a hand free for a window that's open nine minutes at 10:40." *Tier A and B accounts keep the desktop-reports line. The `evidence_tier` column on each list row picks the variant at load.*

Intradiem reads the same desktop and WFM data you run and acts while the window is open: coaching slotted, a training module pushed, a break moved, a case pulled forward. Humana has it on the record: two hours back per agent per month.

Worth a conversation on how other real-time teams run this on top of Verint?

Nathan

**LinkedIn connect (day 2)**
Hi {{firstName}}, shot you a note by email about turning the desktop report at {{companyName}} into same-shift action on top of Verint, thought this might be quicker. Nathan, Intradiem

**Call 1 voicemail (day 3)**
{{firstName}}, Nathan Belfield at Intradiem. I sent you a note Monday about the idle minutes your desktop reports already show at {{companyName}} and what it takes to act on them inside the shift. It's in your inbox under "idle minutes at {{companyName}}". I'll try you again Thursday.

**Email 2** (in thread, day 4)
Subject: `re: idle minutes at {{companyName}}`

Hi {{firstName}},

One number I left out. In 2025 Humana's agents took 12,000 hours of voluntary time off that Intradiem found inside the schedule, which Humana counts directly as overtime avoided. Their agents call it a helper, not a big-brother tool, which matters when the desktop data is already there.

Twenty minutes before the Q4 peak. Which week works?

Nathan

**Email 3** (new subject, day 11) · subject: `{{peak}} at {{companyName}}`

Hi {{firstName}},

{{peak}} puts every idle minute on the table and every open req on the plan. The teams that get through it without overtime aren't the ones with the best report; they're the ones acting on it by the hour.

If the real-time desk at {{companyName}} could move coaching and breaks into the gaps as they open, on top of Verint, what would you do with the hours?

Nathan

**Email 5, breakup** (day 18) · subject: `re: {{peak}} at {{companyName}}`

Hi {{firstName}},

I'll leave this with you. If the desktop report lands the intraday question back on your desk after {{peak}}, or a Verint renewal puts the module spend under review, this is the conversation to have first. Good luck with the peak.

Nathan

## Verint attack, BO claims and shared services (VP / Director)

**Email 1** · subject: `Monday backlog at {{companyName}}`

Hi {{firstName}},

{{signal}}

The productivity reports on the claims desktop say the same thing every Monday: last week's idle time, in hindsight, next to a backlog that grew back over the weekend.

Intradiem's User Productivity Tracking reads that desktop live and acts while the window is open: the next case pulled forward, a training block in the gap, coaching when there's room, alongside the WFM and case system you run. A health insurer on the platform: productivity up 15 percent in nine months, idle time per associate down 14 hours a month.

Worth a conversation on how other claims operations run the week this way?

Nathan

**LinkedIn connect (day 2)**
Hi {{firstName}}, shot you a note by email about the Monday backlog at {{companyName}} and the idle windows already inside the week, thought this might be quicker. Nathan, Intradiem

**Call 1 voicemail (day 3)**
{{firstName}}, Nathan Belfield with Intradiem. Sent you a note about the claims backlog at {{companyName}} and the idle capacity the desktop reports already show. Subject line is "Monday backlog at {{companyName}}". Back to you Thursday.

**Email 2** (in thread, day 4)
Subject: `re: Monday backlog at {{companyName}}`

Hi {{firstName}},

The number behind it: a health insurer running Intradiem in the back office saw 15.4X return, and the associates read it as a helper rather than a monitor, because the action is a case or a training block, not a report on them.

Twenty minutes before {{peak}}. Which week works?

Nathan

Emails 3 to 5 follow the FO shape with the claims peak in the subject and the shared-services colleague named as a fact in Email 4.

## NICE attack, FO ops director (Director / VP Contact Center Operations)

What changes from the Verint copy: the report came bundled, so the reader may not know they have it, and the incumbent is the ACD they will not move. Never "replace NICE." The angle is that CXone already holds the desktop number and Intradiem turns it into the next action, alongside CXone.

**Email 1** · subject: `the number CXone already has at {{companyName}}`

Hi {{firstName}},

{{signal}}

CXone already knows how much of the shift at {{companyName}} sits idle; the desktop analytics that came with it puts the number in a report. The report is where it stops.

Intradiem sits alongside CXone and acts on that number while the window is open: coaching slotted, training pushed, breaks moved, a case pulled forward. Humana has it on the record: two hours back per agent per month, 45 seconds off handle time, seven times the investment five years in.

Worth a conversation on how other operations teams run this alongside CXone?

Nathan

**LinkedIn connect (day 2)**
Hi {{firstName}}, shot you a note by email about the idle number CXone already has at {{companyName}} and what acting on it looks like, thought this might be quicker. Nathan, Intradiem

**Email 2** (in thread, day 4)
Subject: `re: the number CXone already has at {{companyName}}`

Hi {{firstName}},

One thing I left out. Coaching in most operations happens "when we're quiet," which is never. Humana's agents got two hours a month back for exactly that, and occupancy went up four points at the same time, not down.

Twenty minutes before {{peak}}. Which week?

Nathan

Emails 3 to 5, calls and DMs follow the Verint FO shape with "alongside CXone" in place of "on top of Verint."

## Coordination note (every account)

Operational seats (WFM, ops director, claims) enter the attack sequence the same day. The COO or CAO at 53 of these accounts is already in the DWO Executives campaign; they do not enter this one. Email 4 and DM 3 name the operational colleague as a fact. Nate pulls the WFM lead into any COO reply and the reverse. This team compares notes: keep every message identical on the numbers. Maximus stays in the BPO customer-lane campaign where it already sits (Nate loaded five leads Sep 4); it is the reference case for the rep-confirmed field, not a second sequence.

## Eight-line QC plus lines 9 to 12

1. Email 1 opens on a dated signal and says what we do by sentence three. Yes, on every variant; the signal is a per-lead variable and the email does not ship blank.
2. Numbers: Humana (2 hrs/agent/month, 12,000 VTO hours, 45 s AHT, 4 pts occupancy, 7X, "helper not Big Brother") from the VERIFIED Humana row, 1:many. Blinded back-office lines from the customer stories registry (McKesson 5.9 percent active work time; Optum 15 percent, 14 hours, 15.4X), blinded, never to themselves. No prospect numbers in the shell.
3. Email 1 ends on one question, no calendar. Yes.
4. Word counts with the signal token counted as one word: FO Verint E1 86 (tier D variant 87), BO Verint E1 96, NICE E1 95; a real signal sentence of up to 20 words keeps each under 110. E2s shorter; breakup 43. Connect notes 184, 181, 184 characters.
5. No two people at one account share an angle: FO estate owner, FO ops director, FO performance, BO claims each carry a different idea.
6. No em dashes, no banned words, first-name sign-off. Checked.
7. Coordination note present.
8. Customer-exclusion gate: 11 customers dropped at the list build (`lists/excluded_customers.csv`); the gate runs again at load.
9. Every call step has a voicemail and an EA route.
10. No admission of not knowing the org; colleague lines are facts from the pool.
11. No apology or exit phrase except the single breakup.
12. Delays written as relative days before lemlist.

## Still to fill before a wave loads
- `{{signal}}` per lead from the SKU sweep (job postings, LinkedIn skills, case studies) or the peak line.
- Phones on every operational seat (sourced before, never after).
- Nate's read on the copy; Naveen's messaging document may replace the product sentence the day it lands.
- The AE or Nate confirms the desktop-analytics SKU per account (rep-confirmed field) before that account loads.
