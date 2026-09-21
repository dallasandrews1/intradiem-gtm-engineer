---
name: intradiem-verified-metrics
description: >
  Intradiem's source of truth for verified metrics, proof points, customer value stories, and
  positioning. Enforces citation discipline and 1:1/1:many approval tiers, plus the
  customer-sourced value tiers (CV-INTERNAL / CV-1:1 / CV-1:many) for Greenlight/Zuar per-account
  CTO/realized-value data. Primary source: 04-value-repository/Intradiem_Value_Repository.md +
  Customer_Value_Registry.md. Trigger when citing Intradiem stats, ROI, NRR, proof points,
  customer results, per-account CTO figures, or competitive positioning; when building outreach,
  strike plans, pitch prep, or webinar/marketing/QBR content with Intradiem data; or on "what are
  our numbers," "is that verified," "what can I say about [customer]," "can I use their CTO
  number," "update proof points," "add a case study." Load proactively when output includes an
  Intradiem number or a customer's own usage figure, or when a new case study/deck is uploaded.
  Also governs the three claim lanes (Sep 21 2026): Intradiem and customer outcomes, public
  prospect facts (CMS data, rulings, filings: primary source, as-of date, send-time re-check),
  and modeled estimates (1:1, labeled). Never skip because you "remember" a number. Always check.
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

## Claim lanes (adopted Sep 21 2026)

One truth standard, three speeds. Decide the lane before anything else; the tiers below apply inside Lane 1.

- **Lane 1, Intradiem and customer outcome claims.** Any Intradiem statistic, ROI, customer result, customer name or Greenlight/Zuar figure. Governed by the Value Repository, the approval tiers and marketing's clearance list exactly as before. This is where the legal and customer-trust exposure sits, so nothing here loosens.
- **Lane 2, public facts about a prospect or market.** CMS Star Ratings data, a court ruling, an agency memo, a filing, an earnings statement. Self-serve: no approval step and no Value Repository entry required. Three conditions, all mandatory: (1) a PRIMARY source (the agency file or memo itself; analyst and trade press are secondary and only support), (2) an as-of date carried with the fact, (3) a re-check against the primary source at send time. Keep the humility clause on anything about the prospect's own numbers: they know their exact picture better than we do.
- **Lane 3, our own modeled estimates.** Forgone QBP, addressable percent, strike-engine ROI, any number we computed. 1:1 only, always labeled an estimate with its basis, never a headline number, never blended with a Lane 1 figure, never presented as Intradiem-verified.

Anything that fits no lane is `[UNVERIFIED]`.

Why Lane 2 has a freshness rule instead of an approval step: on Sep 21 2026 three confident Stars claims turned out stale, and none would have been caught by approval. CMS re-issued the 2026 Summary Ratings on Jul 22 2026 (34 of 307 universe contracts changed, 21 now at or above 4.0), and its Jun 17 2026 memo pulled complaints, appeals, members leaving, TTY and all Part D measures out of 2027 QBP ratings. A public fact that was true when filed can be wrong at send time.

## Data sources

- **Canonical:** `04-value-repository/Intradiem_Value_Repository.md`. Read it before citing any Intradiem number.
- **Customer value registry:** `04-value-repository/Customer_Value_Registry.md` — per-account realized-value (CTO) figures, whitespace, maturity, NPS, from the Greenlight/Zuar portal. The repo governs how these may be used; the registry holds them. Read both before using any customer's own number.
- **Public verified:** intradiem.com, BusinessWire record-results releases (Feb 2025, Feb 2026).
- **Internal (to be added in the role):** Intradiem's official value deck, ROI methodology, customer reference list with approval status, and analyst materials. Replace the CONFIRM entries with these.

## Approval tiers

Company-level claims:
- `1:many` — public and broadly distributable (PR, website, analyst, marketing, webinar).
- `1:1` — individual prospecting and internal use only; blind customer names unless logo-approved.
- `CONFIRM` — not yet verified against an official Intradiem source. Never use externally.

Customer-sourced value tiers (Greenlight/Zuar per-account data — added Jul 17 2026):
- `CV-INTERNAL` — default on ingest. Usable to rank, prioritize, and target accounts. **Never in prospect-facing copy.** Every Greenlight figure starts here.
- `CV-1:1` — citable **only** in outreach/materials directed back to that *same customer's* own buyers. Never to a third party, never blended across accounts, never public. Promotion out of CV-INTERNAL requires the measure's unit/definition confirmed in Greenlight (see unit note). This is the install-base personalization lane.
- `CV-1:many` — public / other-logo / deck use. Promotion out of CV-1:1 requires named-reference or logo approval + marketing sign-off; on promotion the claim graduates into the VERIFIED 1:many table. Today only Humana qualifies.

**CTO definition and unit note (verified against the Zuar export dated Jul 17 2026; supersedes any earlier "Capacity/Time Optimized" wording):** CTO = **"Cost Taken Out"** per customer, the cost savings attributable to Intradiem automation. It is NOT "Capacity/Time Optimized." In Product's enhancement-prioritization formula it is the numerator term (estimated cost savings if an enhancement were implemented), alongside customer demand and effort reduction. In the Greenlight/Zuar portal CTO appears in three forms:
- **TOTAL CTO** (`total_cto_v2_sum`): a RAW MAGNITUDE of cost taken out (e.g. UnitedHealth 24.5M, CVS 15.1M over the period). It is NOT an "x" multiple, and it is NOT the sum of the per-source CTO rows (TOTAL runs materially larger than the broken-out sources).
- **CTO Multiple** (`cto_over_ab_fixed_ratio`): TOTAL CTO divided by AB Fixed, the derived "x." Verified: CVS 17.5x, Aetna 12.8x, Humana 5.81x; portfolio mean ~4.5x, median ~4.2x; 45/63 accounts at or above 2.1x, 25/63 at or above 5x; 8/63 stalled at 0x.
- **CTO5**: a 0-to-5 prioritization score, bucketed 0 -> 0, 1 -> 0.1-0.5x, 2 -> 0.6-1.0x, 3 -> 1.1-1.5x, 4 -> 1.6-2.0x, 5 -> 2.1x and up. Raw `cto5_calc_daily_bi` is stored uncapped; the strict 0-to-5 bucket is applied in the prioritization layer.

Source decomposition of CTO: Coaching, Efficiency, Handle Time, UPT Alerts, UPT Reports, Burnout, Staffing, Adherence, Break/Lunch, TM.

**Unit caution (load-bearing):** CTO means cost taken out, but the raw magnitude's exact unit (true dollars vs. an internal cost index) is NOT yet confirmed in Greenlight. Do not publish a hard "$X saved" from a per-account CTO figure until confirmed. TOTAL CTO does NOT reconcile to the $529.6M all-time company savings figure (different measure). Humana's 5.81x reconciles to its public "~2 hours of capacity per agent per month," the only cleared external framing. Until the unit is confirmed, CTO stays CONFIRM-tier for unit-bearing phrasing: no "$X," "Y hours," or "Z%" derived from CTO ships.

**Guardrails (do NOT let these get miswritten):**
- Never define "Total CTO = sum of individual CTO multiples (units = x)." That is an enhancement-prioritization abstraction, not the portal measure. Never sum the portal per-account multiples into a portfolio "x."
- The CTO Multiple's denominator is AB Fixed, not the licensed-agent count. Do not redefine it as "CTO divided by agent base."

## Rules

### Must
1. Every Intradiem statistic in any output includes its source in parentheses, e.g., "net retention above 114% (BusinessWire, Feb 18 2026)."
2. Before using any Intradiem metric in customer-facing content, check it against the Value Repository. If it is not there, mark it [UNVERIFIED] in the output.
3. For any CONFIRM-tier number, state that it is not yet verified and give the safe alternative.
4. Any ROI model or strike plan that uses an Intradiem stat pulls the exact value from the repository, not from memory or a prior draft. The strike-engine ROI assumptions are internal placeholders until replaced with Intradiem's official methodology.
5. Respect the approval tier. A 1:1 metric may not go on a webinar slide, blog, or marketing one-pager without review.
6. Respect blinding. Blind customer names unless the story is logo-approved.
7. **A customer's own Greenlight/Zuar figure defaults to CV-INTERNAL and stays out of prospect copy** until promoted to CV-1:1. A CV-1:1 figure goes ONLY into outreach directed back to that same customer's own buyers.
8. **Never attach a unit ($ / hours / %) to a CTO figure** until the measure definition is confirmed in Greenlight. CTO is "Cost Taken Out" (cost savings), but do not publish it as a hard $ figure until the raw magnitude's unit (true dollars vs. an internal cost index) is confirmed. The all-time CTO rollup does NOT reconcile to the $529.6M company savings figure (different measure). Never sum the portal per-account CTO multiples into a portfolio "x."

9. **Lane 2 facts carry a primary source and an as-of date, and are re-checked at send time.** If the source has been re-issued or superseded, the fact is re-pulled before it ships. Secondary coverage alone does not qualify a fact for Lane 2.
10. **Lane 3 estimates are labeled as estimates with their basis** ("estimate from public CMS data") and stay 1:1. If the inputs are known stale (for example `stale_econ_carryforward`, or a pre-Clover `addressable_pct`), say so or leave the number out.

### Should
1. Label industry benchmarks as benchmarks, never as Intradiem results.
2. When several sources confirm a metric, cite the most recent and authoritative first (prefer the latest BusinessWire release or the Value Repository).
3. When a needed number is unverified, derive from verified figures instead of inventing one, e.g., do not claim a churn percentage; cite net retention above 114% and record customer savings, which are verified.
4. For a CV-1:1 send, prefer the reconciled Humana-style framing ("~X hours per agent per month") over the raw multiplier once the unit is confirmed — it is the on-brand, prospect-legible form.

### Never
1. Never present a CONFIRM-tier or [UNVERIFIED] number as a confirmed Intradiem proof point externally.
2. Never position WFM vendors (Verint, NICE, Calabrio) as competitors. They are the layer Intradiem acts on top of.
3. Never fabricate or extrapolate an Intradiem-specific number, even if the math seems reasonable.
4. Never use a customer name externally without confirmed reference approval.
5. Never present the strike-engine's ROI assumptions as Intradiem-verified figures.
6. **Never cite one customer's CTO/realized-value figure to a different account, blend CV figures across accounts, or make a CV figure public** — that is a customer-data breach, not just an unverified claim. Cross-account or public use requires promotion to CV-1:many (reference + marketing sign-off).
7. Never frame a STALLED account (zero CTO on a live agent base) as a value/outcome story; it is a CS save signal.

8. Never ship a Lane 2 fact on memory of an earlier pull, and never let a Lane 2 or Lane 3 item read as an Intradiem result. A public fact about a prospect proves we did the reading, not that Intradiem moved the number.

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
- Humana: 7X ROI five years in; 2 hours of capacity per agent per month; 2.7M automated actions 2025; AHT −45s; occupancy +4% (public SWPP/Intradiem webinar) [1:many, named] — this is the CV-1:many bar
- Company-wide customer savings $529.6M all-time vs $509.6M target (Greenlight home, Jul 17 2026) [internal fact; excludes Harmoniq-migrated; not a per-account or prospect claim]
- Per-account CTO for 63 accounts (Customer_Value_Registry.md). CTO = "Cost Taken Out" (cost savings from automation). TOTAL CTO is a raw magnitude (e.g. UnitedHealth 24.5M, CVS 15.1M); the CTO Multiple = TOTAL CTO / AB Fixed (CVS 17.5x, Aetna 12.8x, Humana 5.81x; portfolio mean ~4.5x). [CV-INTERNAL; raw-magnitude unit CONFIRM in Greenlight before any unit-bearing use]
- UK install base, blinded (Salesforce UK export, Aug 3 2026; repo section "UK install base — blinded facts"): two well-known UK insurers (general insurer since 2018, ~5,000 agents; private health insurer since 2022, ~1,100 agents) among seven UK accounts across six industries; longest UK tenure since 2015; roughly 37,000 CRM-recorded agents total. [1:1 BLINDED ONLY — existence/tenure/stack facts, never outcomes; never name a UK customer without recorded reference approval; the "two of the largest UK insurers" superlative is UNVERIFIED — say "well-known" or "major"]

CONFIRM before external use: NPS 71, 7x ROI / 3-month payback, under 1% churn, the CTO measure unit, and all strike-engine ROI assumptions.

## Source hierarchy

When the same metric appears in multiple places, prefer in this order:
1. Intradiem Value Repository + Customer Value Registry (this system's canonical docs)
2. Latest BusinessWire record-results release
3. intradiem.com (platform, success stories, bios)
4. Greenlight/Zuar portal (internal customer usage — CV-tiered, never public without promotion)
5. Analyst / third-party (industry context only, never as an Intradiem claim)

Lane 2 facts sit outside this hierarchy: they cite the primary public source directly (the CMS file, the memo, the filing), with analyst and trade press as support only.
