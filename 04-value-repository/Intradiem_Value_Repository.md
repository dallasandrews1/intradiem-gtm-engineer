# Intradiem Value Repository
**Started Jul 8 2026 by Dallas Andrews. Dallas is the sole owner** — he defines the tiers and approves every entry; there is no external repository owner to route sign-off through. Living source of truth for every claim that may appear in prospect-facing copy. The MessageGen token `product_angle` and the intradiem-verified-metrics skill read from THIS file. A claim not in this file does not ship. Grows over time as internal materials, case studies, and approved metrics become available; starting thin is the design, not a gap.

## Tier definitions
- **VERIFIED:** citable as fact in prospect copy, source attached, approval tier noted (1:1 vs 1:many).
- **DRY-RUN:** may appear in internal demos only, never reaches a prospect.
- **DO-NOT-SEND:** known placeholder or unverified figure; listed here so nobody reintroduces it by accident.

### Customer-sourced value tiers (added Jul 17 2026 — for Greenlight/Zuar per-account realized-value data)
Internal-system customer usage/value data (e.g. the Greenlight/Zuar CTO measure) is *verified that it happened* but is the **customer's own data**, so it is governed by where the number is allowed to travel, not just whether it's true. Three states, promotion is one-directional and gated:
- **`CV-INTERNAL`** (default on ingest): usable to rank, prioritize, and target accounts. **Never in prospect-facing copy.** Every Greenlight figure starts here.
- **`CV-1:1`**: citable **only** in outreach/materials directed back to that *same customer's* own buyers. Never to a third party, never blended across accounts, never public. Promotion out of `CV-INTERNAL` requires the measure's **unit/definition confirmed in Greenlight** (see unit caveat below). This is the Install-Base personalization lane.
- **`CV-1:many`**: public / other-logo / deck use. Promotion out of `CV-1:1` requires **named-reference or logo approval + marketing sign-off**; on promotion the claim graduates into the VERIFIED 1:many table below. Today only Humana qualifies.

**The only external gate that survives** (Dallas owns the repo, so there is no owner to ask about structure): the single moment a customer's number crosses `CV-1:1 → CV-1:many`. That crossing is a customer-data / marketing-legal question, independent of the repo. Everything up to that line is Dallas's call.

**CTO definition (verified against the Zuar export dated Jul 17 2026; supersedes any earlier "Capacity/Time Optimized" wording):** CTO = **"Cost Taken Out"** per customer, the cost savings attributable to Intradiem automation. It is NOT "Capacity/Time Optimized." In Product's enhancement-prioritization formula it is the numerator term (estimated cost savings if an enhancement were implemented), alongside customer demand and effort reduction. In the Greenlight/Zuar portal it appears in three forms: **TOTAL CTO** (`total_cto_v2_sum`), a raw magnitude of cost taken out (e.g. UnitedHealth 24.5M, CVS 15.1M), which is NOT an "x" multiple and is NOT the sum of the per-source rows; **CTO Multiple** (`cto_over_ab_fixed_ratio`) = TOTAL CTO / AB Fixed, the derived "x" (CVS 17.5x, Aetna 12.8x, Humana 5.81x; portfolio mean ~4.5x, median ~4.2x); and **CTO5**, a 0-to-5 bucketed prioritization score (5 = 2.1x and up). Source decomposition: Coaching, Efficiency, Handle Time, UPT Alerts, UPT Reports, Burnout, Staffing, Adherence, Break/Lunch, TM.

**Unit caveat (load-bearing):** CTO means cost taken out, but the raw magnitude's exact unit (true dollars vs. an internal cost index) is **NOT yet confirmed** in Greenlight, and the all-time TOTAL CTO rollup does **not** reconcile to the $529.6M company-wide savings number (different measure). No unit-bearing phrasing ("$X saved," "Y hours," "Z% efficiency") ships from any CV figure until the unit is confirmed. Humana's 5.81x reconciles to its public "~2 hours of capacity per agent per month," the only cleared external framing. Until confirmed, CV numbers are relative-magnitude / targeting signals only. Never sum the portal per-account multiples into a portfolio "x" (that is an enhancement-prioritization abstraction, not the portal measure).

## VERIFIED claims
| Claim | Source | Approval tier | Added |
|---|---|---|---|
| UnitedHealthcare told a federal court a single disputed call-center secret-shopper call (CMS Call Center Monitoring measure) cost it $190M in Star bonus payments; a judge ordered CMS to recalculate. Cite as UHC's stated figure UNDER THE PRIOR RULES; the measure is retired for 2028 Stars. Historical proof only; never imply moving that measure still earns bonus. | Becker's, Healthcare Finance News, Healthcare Dive | 1:1 and 1:many (third-party, not an Intradiem claim) | Jul 8 2026 |
| Public CMS Star Ratings math (star levels, forgone-QBP estimates, cliff-edge counts) computed from CMS 2026 release + enrollment + KFF/MedPAC methodology. Always labeled "estimate from public CMS data" with the humility clause: the prospect knows their exact picture better than we do. | CMS Oct 8 2025 release; Dallas's canonical universe files | 1:1 and 1:many with estimate label | Jul 8 2026 |
| Intradiem sells Dynamic Workforce Orchestration across contact centers AND back offices, six verticals (Healthcare, Financial Services, Insurance, Retail, Telecom, Utilities). | Company positioning (Naveen's onboarding site) | 1:1 and 1:many | Jul 8 2026 |
| Humana (named customer, on the record): partnership since 2020; first-year in-year return; 7X ROI five years in; 2.7M automated contact-center actions in 2025; 2 hours of capacity unlocked per agent per month in 2025 (16,000 dynamic work hours, 45,000 automated sessions); AHT reduced 45 seconds; occupancy up 4%; 12,000 voluntary time-off hours generated (overtime avoidance); "Automation is no longer a nice to have, it's considered table stakes for Humana" (Melinda Dippolito, Humana, from 42:57 in the recording). | Public SWPP/Intradiem webinar, on-demand at intradiem.com (webinar-case-study-how-humana-leverages-automation); sent by Nathan Belfield. For outreach messaging / MessageGen prompt use, not exec presentation material | 1:1 and 1:many (public, customer-told) | Jul 11 2026 |

### Humana — verified quotables (public SWPP/Intradiem webinar; VERIFIED 1:1 and 1:many)
Source: public SWPP/Intradiem webinar, on-demand at intradiem.com (webinar-case-study-how-humana-leverages-automation), sent by Nathan Belfield. Customer-told, on the record. Cleared for prospect copy (outreach / MessageGen `product_angle`), not exec-deck material. Every line is prospect-citable with the Humana / public label. This is the source shelf the Stars social-proof menu selects from; all figures are contact-center / service-measure outcomes (no clinical or HEDIS claim).

- Humana is one of the largest healthcare insurers in the US (Top 40 Fortune 500).
- "Automation is no longer a nice to have... it's considered table stakes for Humana." — Melinda Dippolito, Humana.
- Partnership with Intradiem started in 2020.
- Rollout was fast, with a first-year in-year return.
- In 2025 alone: 2.7 million automated actions in their contact center with Intradiem.
- Five years in: 7X ROI on their Intradiem investment.
- In 2025 alone: 2 hours of capacity unlocked per agent per month (equating to 16,000 dynamic work hours and 45,000 automated sessions).
- AHT (average handle time) reduced by 45 seconds.
- 4% increase in occupancy.
- Agents consider Intradiem a helper, not a "Big Brother" technology.
- 12,000 voluntary time-off hours generated (translating directly into overtime avoidance).

### UK install base — blinded facts (Salesforce export, Aug 3 2026; VERIFIED 1:1, blinded only)

Source: internal Salesforce UK account export received Aug 3 2026, saved at `motions/UK_Current_Customers_Aug3.csv`. These are install-base EXISTENCE, TENURE, and STACK facts, not customer outcomes — no ROI, savings, or performance claim attaches to any of them. All entries are blinded; **naming any UK customer externally requires confirmed reference approval** (none exists today; record the approval and date here on promotion). Agent counts are CRM-recorded, not audited — phrase as approximate. Built for Jack's UK Insurance/FS and Airlines motions.

- Two well-known UK insurers are current Intradiem customers: a major UK general insurer (customer since 2018, ~5,000 agents, Genesys Cloud) and a leading UK private health insurer (customer since 2022, ~1,100 agents, Aspect Via ACD + Aspect WFM). [1:1, blinded. Jack's "two of the LARGEST UK insurers" superlative is his characterization — [UNVERIFIED], use "well-known" or "major" instead.]
- The UK install base spans seven accounts across insurance, health insurance, energy/utilities, telecom/cable, technology/BPO services, and corporate travel. [1:1, blinded]
- Longest-tenured UK customer has run Intradiem since 2015: a major UK energy supplier with ~13,000 agents. Average tenure across the UK base is roughly 7 years (active-since range 2015–2023). Retention/stickiness proof. [1:1, blinded]
- Roughly 37,000 agents sit across the six UK accounts with recorded counts (one account has no count on record). CRM-recorded, approximate. [1:1, blinded; prefer "tens of thousands of agents across our UK base" in copy]
- UK stack diversity: customers run Amazon Connect (3 accounts), Genesys Cloud, Cisco, and Aspect Via ACDs, with Aspect and NICE IEX WFM. Supports the "acts on top of whatever ACD/WFM you already run" positioning — never framed as displacing those vendors. [1:1; also fine 1:many as an anonymous capability statement]
- A major global travel-services company runs Intradiem in its UK operations (customer since 2019, ~6,500 agents), and a leading UK BPO/technology services provider joined in 2023. [1:1, blinded]

**Promotion trigger to record here:** named use of any UK account = reference approval + date. Until then, blinded phrasing only, and never in a message TO that same customer's own staff as if they were a prospect (all seven are excluded from cold motions per the customer-exclusion gate).

## Customer-verified value data (Greenlight/Zuar)
| What | Where | Tier | Added |
|---|---|---|---|
| Per-account CTO ("Cost Taken Out"; TOTAL CTO `total_cto_v2_sum` + CTO Multiple + CTO5) for 63 customer accounts, plus whitespace-by-solution, maturity scores, NPS trend. The numeric layer behind the Install-Base + Back-Office motions. | `04-value-repository/Customer_Value_Registry.md` (this folder). Source: Greenlight/Zuar portal, pull dated Jul 17 2026. | All rows default `CV-INTERNAL`; promote per the customer-sourced value tiers above. Raw-magnitude unit UNCONFIRMED. | Jul 17 2026 |
| Portfolio whitespace: 545,807 licensed agents, 75.3% portfolio whitespace; Back Office Optimizer 138,820 unused / 100% whitespace; Queue Optimizer 100%; Burnout/Engagement 93.5%; User Productivity 92.4%. | Greenlight whitespace dashboard, Jul 17 2026 (excludes Harmoniq-migrated accounts — directional, not absolute). | Internal targeting only (CV-INTERNAL class); not a prospect claim. | Jul 17 2026 |

## Internal process facts (usable internally, never as customer outcomes)
| Fact | Note |
|---|---|
| 5,000 Clay credits allocated to this motion; ~204.0 spent through Jul 9 2026 (142.3 work-email waterfall + 7.8 ZeroBounce validation + ~48 cc_ops gap-fill waterfall + 5.9 recovery re-validation; exact figure to confirm on the Clay Usage page) | Say "allocated," never "purchased," "monthly," or "total workspace" (workspace plan is larger; the ratified frame is ~3,000 worst case for the quarter) |
| 40+ data sources available through Clay enrichment | Capability statement, not an outcome |
| Company-wide customer savings $529.6M all-time vs $509.6M target (+$20M); $19M YTD growth; 63 customers / 82 accounts; 252.6K avg users/7-day (Greenlight home, Jul 17 2026) | Internal fact; EXCLUDES Harmoniq-migrated accounts. Not a per-account or prospect-facing claim; do not divide into per-customer numbers. |

## DO-NOT-SEND (known placeholders, do not reintroduce)
| Claim | Why blocked |
|---|---|
| "12-18% of paid agent time is idle" or any idle-% stat | proof.json self-labeled placeholder; no verified source |
| Any peer/customer outcome (named or blind) EXCEPT the Humana webinar claims above | Humana (Jul 11 2026) is the only verified customer story cleared for prospect copy; Greenlight CV figures are CV-INTERNAL until promoted. The blinded UK install-base facts (Aug 3 2026 section above) are existence/tenure/stack facts, NOT outcomes — they may ship blinded 1:1, but no outcome, ROI, or savings claim may be attached to them. |
| Naming any UK customer (AXA UK, VitalityHealth, or the other five) in prospect-facing copy | No reference approval exists for any UK account; blinded phrasing only until an approval is recorded in the UK install-base section |
| Any Intradiem ROI, NRR, or performance metric EXCEPT the Humana webinar claims above | Not yet sourced from internal materials beyond the public Humana webinar |
| Any Greenlight/Zuar CTO figure cited to a third party, blended across accounts, or with a fabricated unit ($/hours/%) | CV data is 1:1-locked and unit-unconfirmed; cross-account or unit-bearing use is a customer-data breach, not just an unverified claim |
| Intercom / Rippling proof points | External vendors' results, cut per Jul 7 review; never Intradiem's to claim |
| 157 Director+ contacts / 38 sub-4.0 plans | Stale prior-cycle counts, superseded |

## How to add a claim
1. Attach the source (document, deck, named customer approval, public filing, or Greenlight export + pull date).
2. Assign tier and approval level (VERIFIED 1:1 / 1:many, or CV-INTERNAL / CV-1:1 / CV-1:many for customer-sourced value).
3. Date it.
4. Mirror the change into the Verified Metrics / Claims table in the GTM Engine workbook so the guardrail and the repository never diverge.
5. For customer-sourced value: the number lives in `Customer_Value_Registry.md`; this file governs its tier and usage. To promote a CV figure, record the trigger (unit confirmed → CV-1:1; reference/marketing approval → CV-1:many) and the date next to the account.
