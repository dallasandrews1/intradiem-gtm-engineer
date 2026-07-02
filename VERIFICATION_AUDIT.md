# Verification audit: Intradiem stats and customer claims vs the Value Repository

Date: 2026-06-28. Scope: every Intradiem performance number and customer/peer claim in the Day 1 package, checked against the Intradiem Value Repository (the intradiem-verified-metrics skill, copied into environment-only/value-repository/). Regulatory figures (CMS Star Ratings) and tool pricing are out of the Repo's domain and noted separately at the end.

Headline: the account list was not the exposure. The outbound copy is. Every per-account dollar figure and every peer-outcome story in the TAM engine is unverifiable against the Repo, and both are already baked into send-ready email bodies.

---

## Ground truth: what the Repo actually verifies

1:many (usable externally, with source):
- ~350,000 contact center professionals on platform (intradiem.com)
- Net retention above 114% in 2025 (BusinessWire Feb 18 2026)
- Record net new bookings 2024 and 2025 (BusinessWire)
- Customer savings all-time high, full-year 2025 (BusinessWire)
- eNPS 79 in 2025 (BusinessWire)
- Next-generation platform released 2025 (BusinessWire)

1:1 / blinded (prospecting + internal only, not marketing/webinar):
- Healthcare customer: 4.5X annualized ROI in first quarter (intradiem.com)
- Healthcare customer: 1,700 hours of agent off-phone time saved (intradiem.com)
- Retailer: hold time cut by 16 seconds (intradiem.com, 1:1 unless logo-approved)

CONFIRM tier, never external: NPS 71, 7x ROI / 3-month payback, under 1% churn, and ALL strike-engine ROI assumptions.

Governing rules invoked below: Must #2 (mark [UNVERIFIED] if not in Repo), Must #4 (strike-engine ROI is internal placeholder), Never #4 (no customer claim externally without approval), Never #5 (never present strike-engine ROI as Intradiem-verified), Should #1 (label benchmarks as benchmarks).

---

## VERIFIED, safe (no action)

The only Intradiem performance numbers in the package that check out are in strategy-docs/Grand_Strategy_6_12_Month.md:
- 114% net retention (lines 10, 22, 47) - matches Repo
- record net-new bookings (line 10) - matches Repo
- ~350,000 agents (line 10) - matches Repo

All [1:many]. Note: this is a strategy doc for internal use, not prospect copy, so even these carry low exposure.

The Repo's verified proof points (eNPS 79, 4.5X ROI, 1,700 hours, 16-second hold time) appear NOWHERE in the package. The outbound engine leans entirely on unverified figures while the safe, citable ones sit unused. That is the core structural problem.

---

## NOT VERIFIABLE in the Value Repository (the exposure)

### 1. Per-account ROI dollar figures - strike-engine output, prohibited as Intradiem-verified (Never #5, Must #4)

| Figure | Where | Status |
|---|---|---|
| $7.1M/yr and $2,380/agent | AmeriHealth_Strike_Plan_example.md lines 9, 27, 40, 99, 112 | strike-engine assumption, not in Repo |
| $11.9M, $6.7M, $6.0M, $5.2M, $4.8M | mcp-servers/tam-outbound-engine/data/tam_seed.json; regenerated into email bodies in data/tam_plays.json and account_plays.json | strike-engine assumption, not in Repo |
| roi_model constants: 3 idle min/agent-hr, 1700 productive hrs, $28 loaded cost | config/roi_model.json | self-labeled placeholder defaults |
| $41.6M opportunity, $180K pipeline | cohesion-layer/engine_state.json | seeded placeholder |
| $50M bonus + 4.2 points in 90 days | engine_state.json draft example | already HELD by the reviewer gate as unverified - control working |

roi_model.json and proof.json each carry a "PLACEHOLDER, replace before sending" comment, but the generated plays do not inherit that warning, so the caveat is lost at the point of send. These dollar figures currently sit inside prospect-facing email bodies aimed at regulated buyers.

### 2. Peer-outcome customer claims - none in the Repo, all invented (Never #4, Must #2) - HIGHEST LEGAL RISK

Every generated email closes with one of these, sourced from config/proof.json:
- "A Medicaid plan about your size recovered the equivalent of 40-plus agents of capacity in two quarters, with no new hires" (Health Insurance)
- "A lender your size deferred a full planned hiring class after recovering idle agent time" (Financial Services)
- "A bank your size pulled back a seven-figure idle-labor line in under two quarters" (Banking)
- "A national carrier your size held CSAT steady through a ramp while cutting idle time" (Insurance)
- "A healthcare services team your size recovered meaningful capacity without adding heads" (Healthcare Services)

The Repo's only customer stories are healthcare 4.5X ROI, healthcare 1,700 off-phone hours, and retailer 16-second hold time, all 1:1/blinded. None of the peer outcomes above map to any of them. Grand_Strategy.md line 13 flags this exact risk: "ROI numbers and peer references aimed at health plans are legally sensitive."

### 3. Idle-time benchmark "12 to 18%" (and "5% / three times that")

Appears in every persona template (config/personas.json) and every email. No source in the Repo. Framed as a benchmark, which Should #1 permits, but only if labeled AND sourced. It currently has no citation, so it reads as an Intradiem claim.

---

## Checked and CLEAR (out of Repo scope or self-caveated)

- CMS / Star Ratings figures: $12.7B quality bonus payments, 5% bonus, 50/65/70 rebate retention, 516 contracts, 3.66 avg, 40%+ over 4.0 (operator-test-molina-by-hand.md, star-ratings-bdr-playbook.md). Regulatory data sourced to KFF, Urban Institute, CMS. Verify against CMS, not the Repo. Not Intradiem proof points.
- $10.7M revenue (Grand_Strategy.md line 15): self-flagged "implausibly low, do not anchor." Fine.
- Tool pricing $63 / $99 (sequencer-mcp-intel-for-naveen.md): Clay/Lemlist pricing, not an Intradiem claim.
- Intercom ~$1M pipeline / Rippling 2x, 60% open, 10% reply (Q3_Bulletproof_Operating_Plan.md line 44): Clay proof-class benchmarks, labeled as such, not Intradiem claims.

---

## One collision to watch

config/roi_model.json uses productive_hours_per_year: 1700, which coincidentally equals the Repo's verified "1,700 hours of agent off-phone time saved." Different meaning (a per-year denominator vs a customer outcome). Make sure no one ever cites the 1700 constant as if it were the verified proof point.

---

## Recommended fix (one structural edit closes most of it)

The outbound engine runs entirely on invented figures while the verified, citable numbers sit unused. Replace the config/proof.json peer outcomes with the Repo's blinded-but-verified stories (healthcare 4.5X first-quarter ROI; healthcare 1,700 off-phone hours), respecting the 1:1 approval tier so they go only into individual prospecting, never mass sends or marketing. Pair every per-account dollar figure with an explicit "modeled estimate, assumptions attached" label until the strike-engine ROI is replaced with Intradiem's official methodology on Day 1. The reviewer gate already catches these when it runs (see the $50M example in engine_state.json); the fix is to make that gate mandatory on every send path, not just the conductor.
