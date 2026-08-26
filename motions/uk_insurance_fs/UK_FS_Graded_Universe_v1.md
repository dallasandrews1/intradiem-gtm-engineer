# UK Insurance + Financial Services, graded universe v1

Built Jul 31 2026. Every number below comes from the Financial Ombudsman's own published business complaints data, not from an estimate or a model.

## Sources

- [Business complaints data H2 2025](https://www.financial-ombudsman.org.uk/files/324827/Business-complaints-data-H2-2025.xlsx) (July to December 2025, latest published)
- [Business complaints data H1 2025](https://www.financial-ombudsman.org.uk/files/324668/Business-complaints-data-H1-2025.xlsx) (January to June 2025, prior period, used for trajectory)
- [FOS case fees](https://www.financial-ombudsman.org.uk/businesses/resolving-complaint/case-fees): £680 per case for 2026/27, after a £2,000 annual case-fee allowance

## Method

1. Started from the ombudsman's published firm list rather than a firmographic search. A firm only appears in this data if it takes UK consumer complaints at volume, which is a harder filter than any industry code. 235 business groups after rolling entities up to their parent.
2. Split each group's cases into **addressable** products (Banking & Credit, Mortgages & Home Finance, General Insurance / Pure Protection) and **non-addressable** ones (Investments, Decumulation Life & Pensions, Funeral Planning). The first three are driven by handling, timing, capacity and coaching. The last three are driven by advice and product design, which workforce orchestration does not move.
3. **Addressability cut:** a group must have at least 60% of cases in addressable products and at least 500 addressable cases. 52 of 235 groups survive.
4. **Trajectory is the trigger.** Ranked on addressable volume weighted by period-over-period growth and uphold rate. Groups whose complaints are falling are deprioritised: they already have a story and a working fix.

## Ranked top 15

Fee exposure is addressable cases for the half year at the current 2026/27 rate of £680. Label it that way in any conversation. It's a current-rate estimate against last-published volumes, not a bill the firm has received, and the prospect knows their exact picture better than we do.

| # | Group | Addressable cases (H2 25) | Change vs H1 | Uphold % | Fee exposure at £680 |
|---|---|---|---|---|---|
| 1 | NatWest Group | 6,922 | +87.8% | 30.1 | £4.71M |
| 2 | HSBC | 5,913 | +76.4% | 26.8 | £4.02M |
| 3 | Barclays | 7,144 | +31.9% | 24.9 | £4.86M |
| 4 | Revolut | 5,503 | +83.1% | 26.0 | £3.74M |
| 5 | Monzo | 5,306 | +76.9% | 26.0 | £3.61M |
| 6 | Aviva | 2,856 | +70.4% | 33.3 | £1.94M |
| 7 | Nationwide | 3,067 | +68.1% | 24.9 | £2.09M |
| 8 | Admiral Group | 2,736 | +63.9% | 33.9 | £1.86M |
| 9 | PayPal UK | 1,915 | +128.0% | 37.6 | £1.30M |
| 10 | Direct Line Group | 1,881 | +57.9% | 28.9 | £1.28M |
| 11 | Advantage Insurance | 1,289 | +111.7% | 33.6 | £0.88M |
| 12 | Lendable | 1,119 | +162.1% | 31.1 | £0.76M |
| 13 | AXA (EXCLUDED Aug 3: current customer) | 1,465 | +63.6% | 39.2 | £1.00M |
| 14 | Clydesdale / Virgin Money | 1,723 | +48.2% | 27.4 | £1.17M |
| 15 | Zopa | 1,194 | +93.7% | 25.8 | £0.81M |

## Deliberately not in the top 15

- **Lloyds Banking Group** is the largest group in the data at 11,667 addressable cases, but complaints fell 20.1% period over period. Falling means they already have a fix in motion. Watchlist, not a target.
- **Volkswagen Financial Services** (down 82.5%) and **Vanquis Bank** (down 79.1%) collapsed from very high bases. Same logic.
- **NewDay** down 23.1%.

## Exclusions applied

- **American Express Services Europe** would otherwise rank on volume (1,671 addressable cases, £1.14M exposure) but is excluded. Matt Graves stated on the Jul 21 call that Amex is a customer. Pulled before it reached the target list.
- New entrants with no prior-period baseline (Amex, BMW Financial Services, Moneybarn) are held as an unranked watchlist. Without two periods there is no trajectory, and trajectory is the trigger.

**UK current-customer list arrived Aug 3** (`motions/UK_Current_Customers_Aug3.csv`, 7 accounts): Amex GBT, AXA (UK), British Gas, Capita, Centrica, Virgin Media O2, VitalityHealth. Applied to this universe:

- **AXA is out.** Current customer since 2018 (Genesys Cloud, ~5,000 agents, no WFM listed). Its 8 committee contacts are marked EXCLUDED in `UK_FS_Committee_Contacts_v1.csv`. The "two largest UK insurers" Jack meant are AXA (UK) and VitalityHealth; Vitality is not in this universe.
- **Aviva, Admiral and Direct Line are NOT on the customer list** and stay in as targets.
- Amex GBT on the list corroborates the American Express Services Europe exclusion already applied above.
- Capita, British Gas, Centrica and Virgin Media O2 are customers but do not appear in this FS universe or the airlines universe (checked Aug 3).

**Gate status (amended Aug 3 evening):** (1) ~~confirm DNC scope with Jack~~ closed by Dallas's standing rule that reps' sends are final full versions; the Aug 3 customer list is the complete DNC scope. (2) Still open and unchanged: the exclusion check runs on real rows at load time, including legal-name variants and subsidiaries, per `gate-integrity-fanout-first-run-jul27`.

## Committee contacts

155 deduped contacts across 13 accounts, Director level and above, UK and Ireland only. Exported to `UK_FS_Committee_Contacts_v1.csv`. Sourced via Clay search, which costs zero credits; nothing has been enriched, so nothing has billed yet.

Coverage by seat:

| Seat | Contacts |
|---|---|
| COO / Operations Director | 46 |
| Customer Operations | 20 |
| Complaints / Advocacy | 13 |
| Claims Operations | 4 |
| WFM / Resource Planning | 2 |
| Unclassified, needs a title pass | 70 |

**Honest read on this:** coverage is uneven and not yet sequence-ready. The COO seat over-pulled, the two seats that matter most for this wedge are thin, and 70 contacts have titles that need a manual classification pass. Direct Line, Zopa and Admiral's primary domain returned nothing under the domains tried, and Revolut returned two contacts with no seat match. That is a domain-resolution problem, not an absence of people.

What the pull does prove: the sharp seat exists and is findable. Monzo's Director of Complaints and AXA's Customer Operations & Complaints Director are exactly the entry point this motion is built around (the AXA one is now excluded as a customer contact, but the seat pattern holds for the rest of the universe).

## Next, in order

1. ~~Jack's do-not-contact list.~~ Customer list arrived Aug 3 and is applied (AXA out, 8 contacts excluded). Remaining: confirm with Jack that customers-only is the full DNC scope, and re-run the exclusion on real rows at load time.
2. ~~Title-classification pass on the 70 unclassified.~~ Done Aug 3 as part of the fs-v1.0 variable generation pass: all 147 non-excluded contacts classified (`seat_v2` column), 73 IN scope with critic-gated per-contact variables, 74 OUT-OF-SCOPE (wholesale/CIB, technology, HR, audit/controls, B2B-merchant seats; no copy generated by design). Source of truth: `UK_FS_Committee_Contacts_v1.csv` + `UK_FS_Wave1_Variable_Stage_Aug3.md`. Still open from this line: re-pull Direct Line, Zopa, Admiral and Revolut with corrected domains (Admiral netted 3 IN, Revolut 2, on thin pulls).
3. Enrich only the contacts that survive the exclusion gate. At roughly 4.7 credits per contact all-in, a 100-contact committee set costs about 470 credits against a live balance of 72,822.
4. Voice pass on the copy in `UK_Insurance_FS_Motion_Spec_v1.md` once Jack's booked-meeting messages arrive.
5. Build the Lemlist campaign paused and map its ID to `jack` in `automation/config/lemlist_channels.json`.
