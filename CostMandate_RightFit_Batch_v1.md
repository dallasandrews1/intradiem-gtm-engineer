# Cost-Mandate — Right-Fit Account Batch v1 (2026-07-16)

Corrected signal filter (after H1/re-sourcing showed the original 5 don't fit): a **public, in-window (>= 2026-04-17), service-workforce cost mandate** (contact-center / back-office / operations cost-to-serve pressure) in an Intradiem vertical (Healthcare, Financial Services, Insurance, Retail, Telecom, Utilities) — NOT a tech-org RIF, NOT a divestiture, NOT a company that's growing/raising guidance. Every figure verified against a primary source. 0 Clay credits (web verification).

## LOCKED — Account #1: Acrisure (Insurance)

- **Signal:** ~2,250 roles cut (~11% of ~19,000), commenced **2026-05-21**, phasing into 2027. CEO Greg Williams tied it explicitly to AI/tech changing "how clients expect to be served"; NA insurance reorganized around business lines (Grahame Millwater → advisory).
- **Why it fits:** insurance vertical, company-level exact figure, in-window, service-delivery-framed, private (no earnings-guidance "we're growing" contradiction). Not a known Intradiem customer (confirm against Nate's SF exclusion file before load).
- **Primary sources:** [Insurance Journal 5/22/26](https://www.insurancejournal.com/news/national/2026/05/22/871138.htm) · [The Insurer 6/9/26 — NA reorg](https://www.theinsurer.com/ti/news/exclusive-acrisure-reorganizes-north-america-insurance-around-business-lines-as-2026-06-09/)
- **Contact:** Mark Wassersug, Chief Operating Officer (cost_finance persona). Alt: Matt Schweinzger, President NA Insurance Solutions (owns service delivery). `signal_source_url` = Insurance Journal; `signal_source_date` = 2026-05-21.

### Exemplar Email 1 (hardened §2 compliant, cost_finance, sender = assigned rep)
> **Subject:** the 11% and what carries the service
>
> Mark, the 2,250 roles you started taking out in May, about 11% of the company, reset what the remaining teams have to carry as clients keep expecting the same service. The piece that rarely makes the reorg plan: the people who stay still have paid idle minutes inside every day, and recovering them holds service against the new math without another hire. It isn't a re-org or a system swap, it works the gaps your current setup already leaves. I can send the read on where that recoverable capacity sits across your operations, or better, 15 minutes to walk it. Worth it?
>
> [rep first name]

**Compliance check:** 102 words (70-110 ✓), subject 7 words (≤8 ✓); number = their own 2,250/11%, attributed + dated (May) + `signal_source_url` populated → passes H1 gate + critic; no Intradiem mention (brand-light T1 ✓); no banned words, no em dash, contractions ✓; close = artifact + 15 min, ends on question ✓; insurance vertical so no Humana beat, product_angle empty so no proof claim ✓.

## NEXT — candidates to verify before load (not yet locked)
- **Lumen (Telecom):** ~$1B cost-reduction program, "halfway there." Prime vertical (large contact centers), but verify freshness of the figure + service-workforce relevance, and the pending AT&T acquisition muddies the account. [mlq.ai](https://mlq.ai/news/lumen-technologies-is-halfway-to-its-1-billion-cost-reduction-goal-heres-how-it-plans-to-finish/)
- **Health payers under 2026 cost pressure** (Becker's "15 payers cutting jobs 2026") — strong fit BUT highest customer-exclusion risk (Humana etc. are Intradiem customers); screen every name against the SF exclusion file first.
- **REJECTED:** Truist ($750M program is Sept 2023, stale). The original 5 (Citi/Walmart/Nike/J&J/Abbott) — see `CostMandate_H1_Source_Verification.md`.

## Immediate next steps
1. Load Acrisure (Wassersug + Schweinzger) into the Cost-Mandate workbook, paste the hardened §2/§4 into the live columns, populate `signal_source_url`/`date`, run MessageGen + critic → confirm PASS + HOLD (rep approves later).
2. Verify 4-5 more right-fit accounts to fill a first wave (Lumen + screened payers + telecom/retail/utility cost programs).
3. Run the H2 critic plant-test once the live §4 is pasted (proves the critic discriminates).
