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
| Official value deck, market leadership slide: 7X ROI with payback in as little as 3 months; rapid deployment and time to value 90 to 120 days; 6 to 10 percent productivity savings within weeks of deployment; 68 NPS; 100 percent plus net customer retention; 30 years of earning customer trust. | IntradiemValueInitialization decks (General v2, Insurance/Banking/Healthcare/Media/Utilities v3-v4, Apr 2026), SharePoint Sales Resources / Xfactor / Assets. Official sales asset. | 1:1 (sales-deck use; for 1:many prefer the BusinessWire wording of net retention above 114 percent) | Sep 3 2026 |
| Forrester Total Economic Impact study: 342 percent ROI, validated in an independent study. | 2022_Intradiem_TEI_FINAL.pdf (intradiem.com, attached to the MetLife story) and the Mar 1 2022 TEI webinar; restated on Naveen's Aug 27 2026 concept site. Cite as "a 2022 Forrester study". | 1:1 and 1:many with the 2022 date | Sep 3 2026 |
| Marketing customer stories registry: 16 published stories with validation points; only Humana and Virgin Media are marked "Cleared to use" by name; all others cite BLINDED. See `Customer_Stories_Registry_Jul21.md` for every figure. Back-office stories usable blinded: McKesson (5.9 percent more active work time) and Optum (15 percent productivity, 15.4X ROI). | Customer-Stories-on-Website_20260721.xlsx, SharePoint Marketing site, Customer Reference Guidelines (marketing's live doc, modified Jul 29 2026) | Per the registry Status column: named only when Cleared, otherwise blinded 1:1 and 1:many | Sep 3 2026 |
| Marketing's back-office outreach framework (UPT + BOO, three industry tracks): Optum named in email copy with 18.4 percent productivity within nine months, more than 14 fewer idle hours per associate per month, 15.4X ROI; a healthcare services company (McKesson, blinded) 90-day pilot with 5.9 percent more active work time and 1,649 active work hours gained; combined value proposition "recover capacity, strengthen service performance"; rules: results are from existing back-office automation stories, not BOO or joint deployments, never guarantees; 18.4 percent is not a cost reduction; 1,649 hours is a pilot total, not per associate; no product names or acronyms in outreach ("Intradiem's back-office automation solutions"); never name Elevance or Carelon. | `BOO_Industry_Outreach_Messaging_Framework_V04.pdf` (Sierra Jones, marketing, delivered Sep 9 2026; in Downloads). Dallas's standing rule (Sep 9 2026): anything Sierra delivers on behalf of marketing is approved as-is and counts as marketing sign-off for this gate. Public story page reads 15 percent; marketing's figure governs outreach. | 1:1 and 1:many in EMAIL and LinkedIn outreach; Optum's name never on the website or public assets | Sep 9 2026 |
| Back Office Optimizer positioning, ICP, four personas, elevator pitch, long description, outcomes, pain points, how it works, tone of voice. No customer proof yet; the only figure is an illustrative model. | Back-Office-Optimizer_Messaging-Framework.docx (Cheryl Eckel, Jun 26 2026); local copy `BOO_Messaging_Framework_Jun26.md`. Beta and commercial terms from BOO_Sales_Enablement (v9 Aug 4 2026). | 1:1 and 1:many for positioning language; the $748K worked example is ILLUSTRATIVE and ships only labeled as a model, never as a result; OPX heritage "14 to 24 percent productivity uplift" and "25 to 30 percent analyst capacity" are internal enablement figures, CONFIRM before prospect use | Sep 3 2026 |

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

## UK sales standard claims (added Sep 3 2026; sources traced the same day)
Source: Jack O'Hagan's `vertical-strategy-pack` skill, section 1 "Product facts", and the UK Outreach Bookings tab marketing keeps in the customer stories registry. Traced Sep 3 2026 against Naveen's Aug 27 concept site and the official value deck.

| Claim (Jack's wording) | Status | Source and note |
|---|---|---|
| Payback is contractually guaranteed | VERIFIED 1:1 | Naveen's concept site (Aug 27 2026), "The commitment": "We guarantee 2X. In the contract. 2X is the floor, not the ceiling." Say "guaranteed in the contract" or "a 2X guarantee written into the contract"; confirm the exact contract wording with Sales Ops before quoting a multiple in writing to a US prospect |
| 7x ROI with a 3-month payback (AXA Health message) | VERIFIED 1:1 | Official value deck: "7X ROI with payback in as little as 3 months". Keep "as little as" |
| Intradiem recovers 15 to 20 minutes per agent per day automatically | CONFIRM | Not in the value deck, the concept site, or any published story. Closest published figures: Humana ~2 hours per agent per month; CAA 486 minutes per agent reclaimed. Ship in UK copy on Jack's authority only |
| Contact centres lose 30 to 40 minutes per agent per day to unmanaged idle time | CONFIRM | Not sourced. The concept site's sourced figure is "45 to 65 percent utilisation" (Salesforce, 2024). Prefer that with its source |
| Triple-digit headcount equivalent without a single reduction | CONFIRM | Derived from the two rows above; falls with them |
| Rules-based, no models to govern, no AI governance burden | CONFIRM | Positioning statement; the Engagement Hub QBR deck describes a bounded LLM recommendation engine with human in the loop, so "rules-based" is true of the core platform, not of every product. Confirm with Product before US use |
| Sits on top of the existing WFM, never replaces it; integrates natively with Genesys Cloud, NICE and others | VERIFIED | Rule 4, the UK stack-diversity row, and the BOO framework ("integrates alongside existing WFM (NICE, Verint, Calabrio) without replacing it") |

## DO-NOT-SEND (known placeholders, do not reintroduce)
| Claim | Why blocked |
|---|---|
| "12-18% of paid agent time is idle" or any idle-% stat | proof.json self-labeled placeholder; no verified source |
| Any peer/customer outcome (named or blind) EXCEPT the Humana webinar claims above | Humana (Jul 11 2026) is the only verified customer story cleared for prospect copy; Greenlight CV figures are CV-INTERNAL until promoted. The blinded UK install-base facts (Aug 3 2026 section above) are existence/tenure/stack facts, NOT outcomes — they may ship blinded 1:1, but no outcome, ROI, or savings claim may be attached to them. |
| Naming any UK customer (AXA UK, VitalityHealth, or the other five) in prospect-facing copy | No reference approval exists for any UK account; blinded phrasing only until an approval is recorded in the UK install-base section |
| Referencing JPMC (JP Morgan Chase), AT&T, or Liberty Mutual in ANY outreach, named or blinded | Marketing's EXCLUSIONS tab in the customer stories registry (Jul 2026). Hard exclusion, not a blinding rule |
| Naming any customer other than Humana, Virgin Media, or Optum (email and LinkedIn outreach only, Sep 9 2026) in prospect copy | Marketing's registry Status column plus the Sep 9 V04 addendum. Everyone else is blinded until marketing clears the name. Standing rule: a Sierra deliverable on behalf of marketing is the clearance |
| Any Intradiem ROI, NRR, or performance metric not in the VERIFIED table above | The official value deck and the Forrester TEI now cover 7X ROI, 3-month payback, 6 to 10 percent productivity, 68 NPS, 100 percent plus retention, 342 percent ROI; anything beyond those stays out |
| Any Greenlight/Zuar CTO figure cited to a third party, blended across accounts, or with a fabricated unit ($/hours/%) | CV data is 1:1-locked and unit-unconfirmed; cross-account or unit-bearing use is a customer-data breach, not just an unverified claim |
| Intercom / Rippling proof points | External vendors' results, cut per Jul 7 review; never Intradiem's to claim |
| 157 Director+ contacts / 38 sub-4.0 plans | Stale prior-cycle counts, superseded |

## How to add a claim
1. Attach the source (document, deck, named customer approval, public filing, or Greenlight export + pull date).
2. Assign tier and approval level (VERIFIED 1:1 / 1:many, or CV-INTERNAL / CV-1:1 / CV-1:many for customer-sourced value).
3. Date it.
4. Mirror the change into the Verified Metrics / Claims table in the GTM Engine workbook so the guardrail and the repository never diverge.
5. For customer-sourced value: the number lives in `Customer_Value_Registry.md`; this file governs its tier and usage. To promote a CV figure, record the trigger (unit confirmed → CV-1:1; reference/marketing approval → CV-1:many) and the date next to the account.
