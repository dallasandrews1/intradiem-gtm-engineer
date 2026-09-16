---
name: intradiem-verified-metrics
description: "Intradiem's source of truth for verified metrics, proof points, customer value stories, and positioning. Enforces citation discipline and 1:1/1:many approval tiers, plus the customer-sourced value tiers (CV-INTERNAL / CV-1:1 / CV-1:many) for Greenlight/Zuar per-account CTO/realized-value data. Primary source: 04-value-repository/Intradiem_Value_Repository.md + Customer_Value_Registry.md. Trigger when citing Intradiem stats, ROI, NRR, proof points, customer results, per-account CTO figures, or competitive positioning; when building outreach, strike plans, pitch prep, or webinar/marketing/QBR content with Intradiem data; or on \"what are our numbers,\" \"is that verified,\" \"what can I say about [customer],\" \"can I use their CTO number,\" \"update proof points,\" \"add a case study.\" Load proactively when output includes an Intradiem number or a customer's own usage figure, or when a new case study/deck is uploaded. Never skip because you \"remember\" a number — always check."
---

---
name: intradiem-verified-metrics
description: >
  Intradiem's source of truth for verified metrics, proof points, customer value stories, and
  positioning. Enforces citation discipline and 1:1/1:many approval tiers, plus the
  customer-sourced value tiers (CV-INTERNAL / CV-1:1 / CV-1:many) for Greenlight/Zuar per-account
  CTO (Cost Taken Out) / realized-value data. Primary source: 04-value-repository/Intradiem_Value_Repository.md +
  Customer_Value_Registry.md. Trigger when citing Intradiem stats, ROI, NRR, proof points,
  customer results, per-account CTO figures, or competitive positioning; when building outreach,
  strike plans, pitch prep, or webinar/marketing/QBR content with Intradiem data; or on "what are
  our numbers," "is that verified," "what can I say about [customer]," "can I use their CTO
  number," "update proof points," "add a case study." Load proactively when output includes an
  Intradiem number or a customer's own usage figure, or when a new case study/deck is uploaded.
  Never skip because you "remember" a number — always check.
---

# Intradiem Verified Metrics and Proof Points

## When to load this skill

TRIGGER when any of these are true:
- Generating, citing, or calculating with Intradiem statistics, NRR, ROI, customer results, or competitive claims.
- Using any customer's own Greenlight/Zuar figure (CTO / realized value, whitespace, maturity, NPS) in any output.
- Building strike plans, outreach, pitch prep, webinar slides, marketing collateral, QBR decks, or any customer-facing content that references Intradiem data.
- Answering "what are our numbers," "where did that stat come from," "is that verified," "what can I say about [customer]," "can I use their CTO number."
- Ingesting new source material (case studies, press releases, value decks, Greenlight exports) that may contain proof points.
- Running any ROI calculator or business case that uses Intradiem stats (including the strike engine).

LOAD PROACTIVELY when another skill or workflow will put an Intradiem number or a customer's own usage figure into output, or when a new case study or deck is uploaded.

DO NOT SKIP because you "remember" a number. Numbers change. Always check the repository.

## Purpose

This is the citation-discipline layer for every Intradiem stat in any output. It prevents
number drift, enforces source traceability, and governs which metrics can be used in which
contexts. Intradiem sells into regulated buyers (healthcare, insurance, financial services),
so an unverified number in front of a prospect is a brand and legal risk, not just a
credibility one. Customer-sourced value data (Greenlight/Zuar) adds a second risk class: a
customer's own data leaving its lane is a customer-trust / data-use breach, governed below.

## Data sources

- **Canonical:** `04-value-repository/Intradiem_Value_Repository.md`. Read it before citing any Intradiem number.
- **Customer value registry:** `04-value-repository/Customer_Value_Registry.md` — per-account CTO (Cost Taken Out) / realized-value figures, whitespace, maturity, NPS, from the Greenlight/Zuar portal. The repo governs how these may be used; the registry holds them. Read both before using any customer's own number.
- **Public verified:** intradiem.com, BusinessWire record-results releases (Feb 2025, Feb 2026).
- **Internal (to be added in the role):** Intradiem's official value deck, ROI methodology, customer reference list with approval status, and analyst materials. Replace the CONFIRM entries with these.

## Approval tiers

Company-level claims:
- `1:many` — public and broadly distributable (PR, website, analyst, marketing, webinar).
- `1:1` — individual prospecting and internal use only; blind customer names unless logo-approved.
- `CONFIRM` — not yet verified against an official Intradiem source. Never use externally.

Customer-sourced value tiers (Greenlight/Zuar per-account data — added Jul 17 2026):
- `CV-INTERNAL` — default on ingest. Usable to rank, prioritize, and target accounts. **Never in prospect-facing copy.** Every Greenlight figure starts here.
- `CV-1:1` — citable **only** in outreach/materials directed back to that *same customer's* own buyers. Never to a third party, never blended across accounts, never public. Promotion out of CV-INTERNAL requires the measure's raw unit confirmed in Greenlight (see unit note). This is the install-base personalization lane.
- `CV-1:many` — public / other-logo / deck use. Promotion out of CV-1:1 requires named-reference or logo approval + marketing sign-off; on promotion the claim graduates into the VERIFIED 1:many table. Today only Humana qualifies.

## CTO definition and unit (corrected Jul 18 2026 — supersedes the Jul 17 inference)

**CTO = "Cost Taken Out" per customer** — the cost savings attributable to Intradiem automation. It is **NOT** "Capacity/Time Optimized"; the earlier `CTO Total ÷ AB Fixed = minutes-of-optimized-time` reading was a corroborated inference and is now retired. In Product's **enhancement-prioritization formula**, CTO is the numerator term representing the *estimated* cost savings a customer would realize if a given enhancement were implemented (alongside customer demand and effort reduction).

In the Greenlight/Zuar portal, CTO appears in three forms:
- **Raw TOTAL CTO** (`total_cto_v2_sum` / `TOTAL CTO`) — the magnitude of cost taken out.
- **CTO Multiple** (`cto_over_ab_fixed_ratio` = TOTAL CTO ÷ AB Fixed) — continuous. Verified from the 2026-07-17 export: CVS Health 17.5x, Aetna 12.8x, Humana 5.81x, portfolio mean ~4.5x / median ~4.2x.
- **0–5 CTO5 prioritization score** — the bucketed value used in the prioritization formula:

  | Formula value | CTO Multiple |
  |---|---|
  | 0 | 0 |
  | 1 | 0.1–0.5x |
  | 2 | 0.6–1.0x |
  | 3 | 1.1–1.5x |
  | 4 | 1.6–2.0x |
  | 5 | 2.1x+ |

  (In raw portal exports `cto5_calc_daily_bi` is stored uncapped and can exceed 5; the strict 0–5 bucket is applied in the prioritization scoring layer.)

CTO also **decomposes by source**: Coaching, Efficiency, Handle Time, UPT Alerts, UPT Reports, Burnout, Staffing, Adherence, Break/Lunch.

**Common misreading — do not encode.** `TOTAL CTO` / `total_cto_v2_sum` is a **large raw magnitude** (e.g. Aetna 15.5M, CVS 15.1M over the period), *not* an "x" multiple and *not* the sum of the per-source CTO rows (verified 2026-07-18: TOTAL CTO runs several times larger than the summed source rows, so there are contributors beyond the broken-out sources). The "x" multiple is a **derived ratio = TOTAL CTO ÷ AB Fixed**. Any definition that says "Total CTO = the sum of individual CTO multiples (units = x)" describes an enhancement-prioritization abstraction, not the portal measure — never write it into the value docs, and never sum the portal per-account multiples to get a portfolio "x".

**Unit caution (still in force).** Although CTO means "Cost Taken Out," the raw magnitude's exact unit (true dollars vs. an internal cost index) is **not yet formally confirmed in Greenlight**. Until it is, **do not ship a hard "$X saved" derived from a per-account CTO figure externally.** The magnitude and multiple are usable **internally** (targeting, prioritization, QBRs). The all-time CTO rollup does **not** reconcile to the $529.6M company savings figure — different measure; never treat CTO as that dollar figure. Humana's 5.81x reconciles to its public "~2 hours of capacity per agent per month," so the only cleared external unit framing remains the Humana hours phrasing.

## Rules

### Must
1. Every Intradiem statistic in any output includes its source in parentheses, e.g., "net retention above 114% (BusinessWire, Feb 18 2026)."
2. Before using any Intradiem metric in customer-facing content, check it against the Value Repository. If it is not there, mark it [UNVERIFIED] in the output.
3. For any CONFIRM-tier number, state that it is not yet verified and give the safe alternative.
4. Any ROI model or strike plan that uses an Intradiem stat pulls the exact value from the repository, not from memory or a prior draft. The strike-engine ROI assumptions are internal placeholders until replaced with Intradiem's official methodology.
5. Respect the approval tier. A 1:1 metric may not go on a webinar slide, blog, or marketing one-pager without review.
6. Respect blinding. Blind customer names unless the story is logo-approved.
7. **A customer's own Greenlight/Zuar figure defaults to CV-INTERNAL and stays out of prospect copy** until promoted to CV-1:1. A CV-1:1 figure goes ONLY into outreach directed back to that same customer's own buyers.
8. **Never attach a hard dollar unit ($X) to a raw CTO figure externally** until the magnitude's unit is confirmed in Greenlight. CTO *means* Cost Taken Out, but the stored unit is unconfirmed. The all-time CTO rollup does NOT reconcile to the $529.6M company savings figure — different measure; never treat CTO as that dollar figure.

### Should
1. Label industry benchmarks as benchmarks, never as Intradiem results.
2. When several sources confirm a metric, cite the most recent and authoritative first (prefer the latest BusinessWire release or the Value Repository).
3. When a needed number is unverified, derive from verified figures instead of inventing one, e.g., do not claim a churn percentage; cite net retention above 114% and record customer savings, which are verified.
4. For a CV-1:1 send, prefer the reconciled Humana-style framing ("~X hours per agent per month") over the raw multiple or a raw dollar figure — it is the on-brand, prospect-legible form.

### Never
1. Never present a CONFIRM-tier or [UNVERIFIED] number as a confirmed Intradiem proof point externally.
2. Never position WFM vendors (Verint, NICE, Calabrio) as competitors. They are the layer Intradiem acts on top of.
3. Never fabricate or extrapolate an Intradiem-specific number, even if the math seems reasonable.
4. Never use a customer name externally without confirmed reference approval.
5. Never present the strike-engine's ROI assumptions as Intradiem-verified figures.
6. **Never cite one customer's CTO/realized-value figure to a different account, blend CV figures across accounts, or make a CV figure public** — that is a customer-data breach, not just an unverified claim. Cross-account or public use requires promotion to CV-1:many (reference + marketing sign-off).
7. Never frame a STALLED account (zero CTO on a live agent base) as a value/outcome story; it is a CS save signal. (2026-07-17 export: 8 stalled parents of 63.)

## New proof point ingestion workflow

When new material is provided (case studies, releases, value decks, Greenlight exports):
1. Extract every number, percentage, and quantified outcome.
2. Categorize into the repository sections; assign an approval tier (1:1/1:many/CONFIRM, or CV-INTERNAL/CV-1:1/CV-1:many for customer-sourced value); note blinding, sample size, unit, and caveats.
3. Cross-reference against existing entries; note any conflict; prefer the newest authoritative source.
4. Update the Value Repository (and Customer_Value_Registry.md for per-account value) with the source, date, location, tier, and usage notes.
5. Report what is new, updated, in conflict, and still CONFIRM.

## Key verified numbers (quick reference)

- ~350,000 contact center professionals on platform (intradiem.com) [1:many]
- Net retention above 114% in 2025 (BusinessWire Feb 18 2026) [1:many]
- Record net new bookings 2024 and 2025 (BusinessWire Feb 2025, Feb 2026) [1:many]
- Customer savings all-time high, full-year 2025 (BusinessWire Feb 18 2026) [1:many]
- eNPS 79 in 2025 (BusinessWire Feb 18 2026) [1:many]
- Next-generation platform released 2025 (BusinessWire Feb 18 2026) [1:many]
- Humana: 7X ROI five years in; ~2 hours of capacity per agent per month; 2.7M automated actions 2025; AHT −45s; occupancy +4% (public SWPP/Intradiem webinar) [1:many, named] — this is the CV-1:many bar. Corroborated by the Greenlight export: Humana CTO Multiple = 5.81x, which reconciles to the public "~2 hours/agent/month."
- Company-wide customer savings $529.6M all-time vs $509.6M target (Greenlight home, Jul 17 2026) [internal fact; excludes Harmoniq-migrated; not a per-account or prospect claim; NOT the CTO measure]
- Per-account CTO (Cost Taken Out) for 63 accounts (Customer_Value_Registry.md) [CV-INTERNAL]. Top by multiple: CVS 17.5x, Aetna 12.8x, Assurant 10.9x, Elevance 10.1x. Top by raw scale (90d): UnitedHealth 24.5M, CVS 15.1M, JPMorgan 14.4M, Aetna 10.5M. Portfolio: mean ~4.5x, 45/63 accounts ≥ 2.1x, 25/63 ≥ 5x. Raw magnitude unit unconfirmed — no external "$X" until confirmed in Greenlight.

CONFIRM before external use: NPS 71, 7x ROI / 3-month payback (generic), under 1% churn, the CTO raw-magnitude dollar unit, and all strike-engine ROI assumptions.

## Source hierarchy

When the same metric appears in multiple places, prefer in this order:
1. Intradiem Value Repository + Customer Value Registry (this system's canonical docs)
2. Latest BusinessWire record-results release
3. intradiem.com (platform, success stories, bios)
4. Greenlight/Zuar portal (internal customer usage — CV-tiered, never public without promotion)
5. Analyst / third-party (industry context only, never as an Intradiem claim)