# Pipeline Council: what the dashboard measures and how GTM Engineering gets a row

Source: `Pipeline Council Dashboard View - July 2026.xlsx` (copy in this folder), Genna Barrett-Moeller's Salesforce-built workbook, sent by Melissa Spies to Dallas and Naveen on Aug 24 2026. Report month end Jul 31 2026, 18-month rolling cohort (Feb 2025 through Jul 2026). Every figure below is read straight from the workbook; nothing is estimated.

## 1. Anatomy of the workbook

| Tab | What it is | Who feeds it |
|---|---|---|
| Marketing Dashboard | The council view. One row per channel (Digital, Events, Cold, Alliances, TOTAL), 23 metric columns, plus 12-month trend, MoM spend, opp quality, aging and velocity | Formulas over the raw tabs |
| TOTAL, Digital, Events, Cold Outreach, Alliances | "Big Picture" per channel: last month and running total across MQL/MQA, Meetings, Opps, Late Stage, Closed Won, and $1-spend-drives ratios | Formulas |
| helper tab | The Lead Source to Channel map and the stage ladder. This is where a channel is defined | Genna, by hand |
| Opps Created | Salesforce report "Pipeline Council - NL Opps Created" (new logo), 533 opps with Lead Source, Partner, Primary Campaign Source, Owner, Stage, Total Net New ACV | SF export |
| Stage History | SF report "Pipeline Council - Opp Stage History", 790 stage changes, drives Late Stage / Won flags and aging | SF export |
| Cold outreach data | A hand-kept meeting log, 250 rows: Name, Account, Date of Meeting, Category (Core / Anchor / Partner), AE, ISR, Meeting Complete, Status, Source, Stage, Channel, MQA flags | Manual (Sierra / Genna, from Nate, Jack, memoryBlue) |
| Cold Outreach Spend Raw | One number per month: $11,500 Jan-Jun 2025, $32,475 every month since Jul 2025 (the memoryBlue retainer) | Manual |
| Digital Leads Raw, Digital Spend Data, Event Spend Raw, Alliances Data Raw, Alliances Spend | The other channels' raw feeds | Manual + SF |
| Aging Detail | Outlier list with an Include-in-Aging toggle per deal | Genna |

## 2. The definitions the council runs on

- **Channel is derived from Lead Source** via the helper tab. Cold = BDR Outbound, memoryBlue-US, memoryBlue-UK, Outbound Email, Lusha, Zoominfo, Inside Sales, Inbound Email, Marketing Research, Cold. Digital = Website, Google/Bing search, Google Ad - SEM, LinkedIn Ad, Display Ad, Webinar, 6sense, LinkedIn Sales Navigator, webhelp. Events = Event, Events, Hosted Event. Alliances = Partner, Partner Program, Third Party.
- **Exclude** = Sales, Sales Initiated, Current customer, Referral. These opps exist in the export but never appear in a channel row. 253 of the 533 opps in the cohort sit here.
- **Funnel columns:** Spend, MQL, MQA, Meetings, Opps Created, Total Amount Created, ACV Created, Late Stage, Cost/MQL, Cost/Meeting, Cost/Opp, Meeting Rate (Meetings/MQL), Meeting Rate (Meetings/MQA), Opp Rate (Opps/Meetings), Spend / $ Created, Spend / $ Late Stage, Won Deals, Won Net New ACV, ACV Conversion %, Total Amount Won, Total Lost ACV, Win Rate (Decided).
- **Late Stage** = Propose or Procure. Stage ladder: Unqualified, Discovery, Qualification, Solution Design/Value Creation, Prove, Propose, Procure, Negotiate, Closed Won / Closed Lost.
- **A meeting** is a row in the Cold outreach data tab with Meeting Complete = Yes. The cold MQA flags are computed off that tab, not off Salesforce.
- **Velocity:** Days Created to Late Stage, Late Stage to Won, Days Created to Won, open opp age; averages and medians, with stale deals toggled out.

## 3. Where Cold stands today (the row GTM Engineering will sit next to)

18-month cohort, Cold channel ("memoryBlue / Nathan" per the tab note):

| Metric | Cold, 18 mo | Cold, July | TOTAL, 18 mo |
|---|---|---|---|
| Spend | $479,675 | $32,475 | $1,967,772 |
| MQL / MQA | 178 / 138 | 6 / 6 | 822 / 628 |
| Meetings | 141 | 6 | 269 |
| Opps created | 27 | 1 (Skipton Building Society, memoryBlue-UK, $100.8K ACV) | 133 |
| ACV created | $6,961,560 | $100,800 | $40,337,773 |
| Moved to late stage | 2 ($1.27M) | 1 ($607K ACV) | 12 |
| Won | 4 ($219,386 ACV) | 0 | 31 ($3,037,724) |
| Cost / meeting | $3,402 | $5,413 | $7,315 |
| Cost / opp | $17,766 | $32,475 | $14,795 |
| Meeting to opp rate | 19% | 17% | 49% |
| $ ACV created per $1 spend | $14.51 | $3.10 | $30.81 |
| Win rate (decided) | 3% | | 14% |
| Median days to late stage | 191 | | 66 |

Cold meetings by month in 2026: Jan 25, Feb 19, Mar 24, Apr 26, May 19, Jun 7, Jul 8, Aug 4 so far. The last row from Jack is Jun 10. ISR split across the whole log: Nate 82, memoryBlue 67, Jack 58, Tommy 16, Mesa 8, Nick 7, Tyler 6, Nolan 4.

## 4. Four things the workbook shows that matter to us

1. **Cold is the channel that dropped.** Meetings fell from 24-26 a month in March-April to 7-8 in June-July. The council will be looking at exactly the gap GTM Engineering is meant to fill, and the July cold row is six meetings for $32,475.
2. **BDR-sourced wins are being credited elsewhere.** Every 2026 cold-channel opp (5 of them) is memoryBlue. Nate's "Opportunity" outcomes in the meeting log (Ecolab, Johnson & Johnson, Mercer, Renewal by Andersen, Alorica, National Debt Relief, Princess Cruises, Priceline, BCBS of Arizona, Point32 Health, Global Credit Union, Penske, Mapfre) carry Source = Warm and Channel = Event or Digital, so they roll up to marketing's rows. On top of that, 29 opps and $6.3M ACV created in 2026 carry Lead Source = Sales and sit in Exclude, invisible to the channel view. Without our own Lead Source, our results will land in the same two places.
3. **Back-office expansion inside customers has no home on this dashboard.** Lead Source "Current customer" maps to Exclude, and the opp report is explicitly "NL Opps Created" (new logo). The GTM Engineering channel Naveen took to the council is the only way the BO expansion motion is counted at all, and it needs Genna to include Lead Source = GTM Engineering regardless of account type, or to add an expansion line.
4. **6sense and Sales Navigator are Digital.** "6sense SI" and "LinkedIn Sales Navigator" lead sources map to marketing's Digital row. Any contact we source through either tool must be stamped GTM Engineering at creation, or marketing gets the credit.

## 5. The GTM Engineering row, specified

**Salesforce (Genna / Sierra):**
- One new Lead Source picklist value: `GTM Engineering`. One value, not one per motion; the motion is carried by Primary Campaign Source (one SF campaign per Lemlist campaign, e.g. `GTM Eng - Back Office Expansion - Healthcare`, `GTM Eng - Star Ratings`), which Genna already breaks out on the Opps Created tab.
- Lead Origin (the required field Sierra flagged Jul 16, currently Sales or Marketing): add `GTM Engineering`. If it stays Sales, the opp maps to Exclude and disappears.
- helper tab: add row `GTM Engineering | GTM Engineering`. Council view: a fifth channel row with the same 23 columns.
- Expansion: the NL report filter has to admit Lead Source = GTM Engineering at customer accounts, or a parallel "GTM Engineering (Expansion)" line. Decision for Naveen with Melissa and Genna.

**Spend column (ours to supply monthly):** Clay credits consumed by the motion at contract rate (from the credit ledger), Lemlist subscription, 6sense if renewed. Same basis as the memoryBlue retainer, tool and vendor cost only.

**Meetings feed (ours to supply monthly, in the Cold outreach data schema):**

`Name | Account | Date of Meeting | Category | AE | ISR | Meeting Complete | Status | Source | Stage | Channel`

Category = Anchor for TAM tier A, Core otherwise. ISR = Nate or Jack. Source = `GTM Engineering`. Channel = `GTM Engineering`. Emitted from the receipts ledger (`automation/logs/credit_pipeline_receipts.md`) and `impact/outcomes.csv`, which already carry date, account, and meeting rows; the meeting-capture agent adds Name, AE, Status. Handed to Genna as a CSV before her month-end build, so nothing is tracked by hand twice.

**Mapping to our own files:**

| Council column | Our source |
|---|---|
| MQL / MQA | Not applicable to outbound; report replies (qualified) in the MQA slot, labeled as such, or leave blank. Cold today records MQL = meetings |
| Meetings | `outcomes.csv` type = meeting, plus receipts ledger booked meetings |
| Opps Created / ACV Created | `outcomes.csv` type = pipeline (value = ACV). Candidate deals from the Audiences deal join stay "confirm before counting" |
| Late Stage / Won | `outcomes.csv` type = won; late-stage moves come from Genna's Stage History, we do not track stage ourselves |
| Spend | Credit ledger $ + Lemlist + 6sense |
| Cost / meeting, Cost / opp, Opp Rate, $ per $1 | Receipts tracker already computes cost per qualified reply and meeting; add cost per opp and ACV per $1 |

## 6. Baselines the council will hold the row to

Cold, 18 months: $3,402 per meeting, $17,766 per opp, 19% meeting to opp, 7% of opps reaching late stage (2 of 27), $14.51 ACV per $1. July cold: 6 meetings. These are the comparison points, not targets.

## 7. OKR phrasing in the council's units, no dollar commitment

- Sequences live on cleared back-office contacts across the 15 customer accounts by the all-hands (week of Sep 14); count reported as contacts in sequence, not sent.
- Meetings from GTM Engineering appear on the council's meeting log under their own Source from September onward.
- Opps created carry Lead Source = GTM Engineering and show as their own channel row on the September dashboard.
- Cost per meeting and meeting-to-opp rate reported monthly against the Cold baseline ($3,402 and 19%).
- Targets stay provisional until two months of the row exist; ranges get set with Naveen, not defended.

## 8. Decisions needed

| Decision | Owner | Needed by |
|---|---|---|
| Lead Source and Lead Origin value name (`GTM Engineering`) | Naveen with Genna, Sierra files the ticket | Before the first Lemlist send |
| Whether expansion opps at customer accounts are admitted to the council view | Naveen with Melissa and Genna | Same |
| Spend basis for our row (credits at contract rate + Lemlist + 6sense) | Naveen | September build |
| Monthly meeting CSV to Genna, who sends it and when (proposal: Dallas, by the 2nd business day) | Dallas with Genna | September build |
