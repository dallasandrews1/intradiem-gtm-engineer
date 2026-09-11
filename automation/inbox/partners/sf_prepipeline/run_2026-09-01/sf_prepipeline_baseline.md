# Partner pre-pipeline baseline, 2026-09-01

Source: `Partner_Pre_Pipeline_All_2026-09-01.pdf` (Salesforce printable view of Partner_Pre_Pipeline__c, filter All, 249 records). Read-only. No stage-change dates exist in this view, only Created Date, so speed (days to the 12-minute meeting) cannot be measured from it yet.

## Funnel today (all records, all partners)

| Stage | Records | Share |
|---|---|---|
| Register Lead | 39 | 16% |
| CAM to AE Intro | 48 | 19% |
| Delivered 12 Minute Meeting | 35 | 14% |
| Customer Meet | 12 | 5% |
| Converted to Opportunity | 35 | 14% |
| Disqualified | 80 | 32% |

- Reached the 12-minute meeting or beyond (Delivered 12 + Customer Meet + Converted): **82 of 249 (33%)**. The benchmark is 25%+ inside 45 days; this is the all-time share with no clock on it.
- Converted to Opportunity: 35 (14%). Disqualified: 80 (32%).
- Still in Register Lead or CAM to AE Intro: 87; of those **85 are older than 45 days** (created before 2026-07-18). That is the nurture pool.

## By partner (partner account, normalized; test rows dropped)

| Partner | Records | Register | CAM intro | 12-min | Cust meet | Converted | DQ | Reached 12-min+ |
|---|---|---|---|---|---|---|---|---|
| Five9 | 93 | 15 | 30 | 10 | 2 | 10 | 26 | 24% |
| SagesS3 | 41 | 7 | 4 | 6 | 6 | 4 | 14 | 39% |
| Genesys | 27 | 4 | 3 | 1 | 0 | 4 | 15 | 19% |
| Alvaria | 22 | 1 | 4 | 9 | 0 | 1 | 7 | 45% |
| ConvergeOne (C1) | 15 | 6 | 1 | 1 | 1 | 3 | 3 | 33% |
| Call Design AU | 15 | 2 | 3 | 2 | 1 | 7 | 0 | 67% |
| Avaya | 10 | 1 | 0 | 4 | 0 | 2 | 3 | 60% |
| Aspect | 8 | 0 | 0 | 0 | 0 | 1 | 7 | 12% |
| SPAR Solutions | 5 | 2 | 0 | 1 | 0 | 0 | 2 | 20% |
| Call Design NA | 4 | 0 | 1 | 0 | 1 | 1 | 1 | 50% |
| Capgemini | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0% |
| Connex | 2 | 1 | 0 | 0 | 0 | 1 | 0 | 50% |
| Barclays | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 100% |
| AWS Marketplace | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0% |
| Calabrio | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0% |
| NWN | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 100% |
| Sabio | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 100% |

## Created by month

194 of 249 records carry a Created Date of Jan 30 or Feb 2 2026: the bulk load when the object went live, not the registration date. Age and speed can only be read on records created from March 2026 on (55 records) until Status history is available.

| Month | Records |
|---|---|
| 2026-01 | 169 |
| 2026-02 | 38 |
| 2026-03 | 8 |
| 2026-04 | 11 |
| 2026-05 | 7 |
| 2026-06 | 7 |
| 2026-07 | 6 |
| 2026-08 | 3 |

## Priority and category as filled

Priority: 1: 52, 2: 73, 3: 93, blank: 31

Category: Expand: 83, Expand or New Pursuit: 67, New Pursuit: 87, blank: 12

## Overlap with the 3xG ranked list

| Grade | 3xG account | Pre-pipeline record | Partner | Status | Created |
|---|---|---|---|---|---|
| MATCH | Beth Israel Deaconess Medical Center | Avaya - Beth Israel Lahey Health | Avaya | Delivered 12 Minute Meeting | 2026-01-30 |
| MATCH | Intuit Inc. | Genesys - Intuit | Genesys | Disqualified | 2026-01-30 |
| MATCH | Manulife Financial | SagesS3 - Manulife Financial Corporation | SagesS3 | Disqualified | 2026-01-30 |
| MATCH | T-Mobile USA, Inc. | SagesS3 - T-Mobile | SagesS3 | Register Lead | 2026-01-30 |
| MATCH | Texas Health and Human Services Commission (HHSC) | C1 -Texas Health | ConvergeOne (C1) | Register Lead | 2026-01-30 |
| MATCH | The National Bank of Canada | SagesS3 - National Bank of Canada | SagesS3 | Converted to Opportunity | 2026-01-30 |
| CHECK | AIG Global Operations | Avaya - AIG | Avaya | Disqualified | 2026-01-30 |
| CHECK | AmeriHealth Caritas Health Plan | C1 - Amerihealth | ConvergeOne (C1) | CAM to AE Intro | 2026-05-11 |
| CHECK | AmeriHealth Caritas Health Plan | Genesys - Amerihealth | Genesys | Disqualified | 2026-02-02 |
| CHECK | American Family Life Assurance Company of Columbus (AFLAC) | SagesS3 - American Airlines | SagesS3 | Disqualified | 2026-01-30 |
| CHECK | American Family Life Assurance Company of Columbus (AFLAC) | SPAR - American Credit Acceptance | SPAR Solutions | Register Lead | 2026-01-30 |
| CHECK | Bank of Montreal (BMO) | Connex - Bank of Montreal | Connex | Register Lead | 2026-01-30 |
| CHECK | First Republic Bank | Five9 - First Citizens Bancshares | Five9 | Delivered 12 Minute Meeting | 2026-01-30 |
| CHECK | GE Healthcare (APCS CC Global Hub) | AWS Marketplace - GE Appliances - UPT POV | AWS Marketplace | Disqualified | 2026-02-20 |
| CHECK | HCA National Patient Account SVC KY | Genesys - HCA Healthcare | Genesys | Register Lead | 2026-01-30 |
| CHECK | PNC Bank, National Association | Genesys - PNC | Genesys | CAM to AE Intro | 2026-02-02 |
| CHECK | State of Washington - Department of Social and Health Services (DSHS) | Five9 - State Street Bank and Trust Company | Five9 | Register Lead | 2026-01-30 |
| CHECK | US Navysparwarsyscen | CapGemini - US Bancorp - UPT | Capgemini | CAM to AE Intro | 2026-04-29 |
| CHECK | US Navysparwarsyscen | SagesS3 - US Cellular | SagesS3 | Register Lead | 2026-01-30 |
| CHECK | United States Pharmaceutical Group LLC dba Convey Health Solutions LLC | Aspect - United Airlines | Aspect | Disqualified | 2026-01-30 |
| CHECK | United States Pharmaceutical Group LLC dba Convey Health Solutions LLC | SagesS3 - United | SagesS3 | Disqualified | 2026-01-30 |

MATCH = same first two name tokens; CHECK = first token only (Beth Israel Deaconess vs Beth Israel Lahey, Texas Health vs Texas HHSC), confirm before treating as registered.

Rule: an account already registered by another partner is not worked cold in the 3xG cohort; it goes to the registering partner's rep.

## Parse quality

ok: 237, no_category: 6, guessed_boundary: 6. Owner columns are split on a known-Intradiem-name list; rows with an empty intradiem_ae need a look.

Missing for the pilot read: Status change dates (field history on Status, or Last Modified Date plus a 12-minute-meeting date field), Prospect account link, ACV. Ask Sales Ops for a report on the object with those columns; the printable view cannot carry them.
