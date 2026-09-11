# 3xG whitespace intake, 2026-09-01 00:31

Source: `Intradiem Work -Verint Partner Account Whitespace 2024.xlsx`. Sheets read: `Verint Partner Only 2024` (74 partner-sold rows + 9 direct back-office rows) and `Quantified Whitespac No SSA-IRS` (1161 distinct accounts, used for WFM footprint and seat fallback). Read-only; no Salesforce, Clay or lemlist call; 0 credits.

## Stripped before anything left the intake
- Matrix sheet: 27 columns dropped (every dollar whitespace column, Total, and the per-module license counts): `EDM-Rec`, `Rec`, `Encrp`, `QM`, `AQM`, `PM`, `Speech`, `RTAA`, `IQ`, `CF`, `XM`, `VFC`, `community`, `RecPubSafe`, `ChAuto`, `KMEnt`, `KMPro`, `Workflex`, `Quality Bot`, `Trans Bot`, `Wrap Up 624+128`, `Voice Capture`, `RT Coach w Trans`, `Redaction`, `Speech 480+120`, `Encryption`, `Total`
- Preamble rows (List Price, Total Opportunity) ignored.
- Exported fields only: rank, account, source_list, reseller_of_record, bucket, size_band, verint_seats, dpa_seats, dpa_whitespace_seats, model, back_office_product, vertical_alignment_as_given, wfm_in_footprint, flags, score.

## Customer and partner gate
- Sources: sf_customer_partner_segment_2026-09-01.csv (127); Active_Customers_SF_Jul10.csv (101); UK_Current_Customers_Aug3.csv (7); customer_denylist.json (10 aliases, 1 domains); tam_accounts.csv (6 names)
- Held (7), never ranked into a cold cohort:
  - Progressive Casualty Insurance Company (verint_no_dpa, 20700 seats): HOLD: SF Customer (Clay segment 2026-09-01), brand match on 'Progressive Leasing', AM confirms it is the same company
  - Citibank N.A (backoffice_deployment, 10000 seats): HOLD: SF Customer (Jul 10 export), brand match on 'Citicorp Credit Services', AM confirms it is the same company
  - Farmers Group, Inc. (dpa_deployed, 9554 seats): HOLD: SF Customer (Jul 10 export), brand match on 'Farmers Insurance', AM confirms it is the same company
  - Five9, Inc (backoffice_deployment, 6000 seats): HOLD: SF Partner (Clay segment 2026-09-01), 'Five9'
  - Cigna Corporation (operational_visualizer, 5100 seats): HOLD: SF Customer (Jul 10 export), 'CIGNA'
  - The Cleveland Clinic Foundation (verint_no_dpa, 3577 seats): HOLD: SF Customer (Clay segment 2026-09-01), brand match on 'Cleveland Clinic', AM confirms it is the same company
  - PNC Bank, National Association (operational_visualizer, 970 seats): HOLD: SF Customer (Clay segment 2026-09-01), brand match on 'PNC Financial', AM confirms it is the same company
- Near-names to confirm with the AM before outreach (1), still ranked:
  - Southern Company: CHECK near-name: SF Customer (Clay segment 2026-09-01), 'Southern California Edison Company', confirm not related before outreach

## Buckets (whole universe)
- operational_visualizer: 6
- backoffice_deployment: 3
- dpa_deployed: 38
- verint_no_dpa: 36

## Top 15 for the Sep 1 review

| # | Account | Bucket | Seats | DPA seats | WFM | Vert | Reseller | Back-office product |
|---|---|---|---|---|---|---|---|---|
| 1 | Ally Financial Inc. | operational_visualizer | 2306 |  | not on matrix sheet |  | Direct | Verint Operations Visualizer (AAMT) - SaaS |
| 2 | Maximus, Inc. | operational_visualizer | 1510 |  | not on matrix sheet |  | Direct | Verint Operations Productivity - SaaS |
| 3 | AIG Global Operations | operational_visualizer | 850 |  | not on matrix sheet |  | Direct | Verint Strategic Operations Visualizer |
| 4 | Intuit Inc. | operational_visualizer | 300 |  | not on matrix sheet |  | Direct | Verint Operations Productivity - SaaS |
| 5 | AmeriHealth Caritas Health Plan | dpa_deployed | 6246 | 3533 | yes | 1 | ConvergeOne, Inc |  |
| 6 | Mercury Insurance Services, LLC | dpa_deployed | 5863 | 2742 | yes | 1 | ConvergeOne, Inc |  |
| 7 | Ford Motor Credit | dpa_deployed | 3850 | 3850 | yes | 1 | Cisco Systems, Inc. |  |
| 8 | Christus Health Data Center | dpa_deployed | 2732 | 149 | yes | 1 | Avaya LLC |  |
| 9 | Manulife Financial | dpa_deployed | 2542 | 10 | yes | 1 | Connex Telecommunications Inc. |  |
| 10 | Allina Health | dpa_deployed | 2259 | 358 | yes | 1 | Avaya LLC |  |
| 11 | First Republic Bank | dpa_deployed | 1400 | 301 | yes | 1 | Amazon Web Services, Inc. |  |
| 12 | Genworth North America Corporation | dpa_deployed | 1201 | 500 | yes | 1 | BT AXA Group |  |
| 13 | Independence Blue Cross | dpa_deployed | 1201 | 1 | yes | 1 | Avaya LLC |  |
| 14 | American Family Life Assurance Company of Columbus (AFLAC) | dpa_deployed | 952 | 952 | yes | 1 | Avaya LLC |  |
| 15 | Medavie, Inc. | dpa_deployed | 851 | 600 | yes | 1 | Bell Canada |  |

Extended pool (matrix accounts with 500+ seats and WFM or DPA present, not on the partner sheet): 62 rows in `3xg_extended_pool.csv`.

## Ranking
Bucket first (operational visualizer 100, back-office deployment 80, desktop analytics deployed 60, Verint footprint without DPA 30), then seats on a log scale (max +30), vertical alignment as given (1: +15, 2: +8), WFM in the footprint (+10), TAM-list match (+10). Held accounts score -1 and carry no rank.

## To settle with Frank on Sep 1
- What the Vertical Alignment scale means (1 looks like the strongest fit to our six verticals; confirm before it stays in the ranking).
- The direct back-office block (Operations Visualizer, Work Manager) is Verint-direct, not partner-registered: is it in play for a 3xG motion, and who makes the intro?
- The Partner column is the Verint reseller of record (Avaya, ConvergeOne, Cisco, AWS), not 3xG. Outreach names 3xG only where Jeremy agrees; the reseller is never named.
- Any held account Frank wants worked goes through the account manager, not this pilot.
