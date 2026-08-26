# Cost-Mandate — H1 Primary-Source Verification (session 4)

**Run date:** 2026-07-16 · **Rule:** a specific $/%/count may be used ONLY if a primary source states THAT EXACT figure AND `signal_source_date` is within 90 days of today (i.e. on/after **2026-04-17**). Otherwise the row ships the qualitative no-number email. Verified by direct web/primary-source read, not Claygent prose.

## Verdicts

| # | Contact / Company | Claygent "disclosed" figure | Primary source found | Source date | In 90-day window? | Exact-figure match? | VERDICT | `signal_source_url` |
|---|---|---|---|---|---|---|---|---|
| 1 | Selva / **Citi** | "300 NY roles" | Crain's: 265 at 388 Greenwich (Mar 16 2026); bankingdive: 286 NY (Feb 2024 event); ThinkAdvisor: "over 300" aggregate (May 20 2026) | mixed | 265 = **NO** (122d); 286 = **NO** (2024); "over 300" = yes but **aggregate, not a single WARN** | **NO clean exact in-window figure** | **UNVERIFIED → qualitative, NO number** | *(blank)* |
| 2 | Shanahan / **Walmart** | 306 | CA WARN: 306 permanent layoffs, Sunnyvale product/engineering, effective Aug 21 2026 (americanbazaar 6/25/26; peoplematters; IBTimes) | 2026-06-25 | **YES** | **YES** (306) | **VERIFIED** — but tech/product-eng reorg, relevance-weak for service-workforce pitch | https://americanbazaaronline.com/2026/06/25/walmart-job-cuts-306-silicon-valley-employees-to-be-laid-off-soon-483517/ |
| 3 | Schneider / **Abbott** | (none captured) | No specific WARN/filing figure surfaced (only forum/Glassdoor + unquantified "device unit layoffs") | — | — | — | **UNVERIFIED → qualitative, NO number** (already no-number) | *(blank)* |
| 4 | Alagirisamy / **Nike** | 1,400 | CNBC: Nike cuts 1,400 roles, technology-team reshape, 2nd 2026 round (CIO Dive; Yahoo; Ecotextile) | 2026-04-23 | **YES** (84d, near edge) | **YES** (1,400) | **VERIFIED** — but technology-team reshape, relevance-weak | https://www.cnbc.com/2026/04/23/nike-job-cuts-layoffs.html |
| 5 | White / **J&J** | 56 | NJ WARN: 56 New Brunswick HQ, tied to DePuy Synthes orthopedics separation, effective Aug 21 2026 (njbiz; fiercepharma; biospace; NJ DOL WARN archive PDF) | 2026-05-29 | **YES** | **YES** (56) | **VERIFIED** — but divestiture-driven, 56 corporate roles, relevance-weak + small | https://njbiz.com/jnj-cutting-jobs-new-brunswick-hq/ |

## Sharper findings after reading the live Contacts table (2026-07-16)

Seeing the actual contacts tightened three verdicts:

- **J&J (Scott White): DIVISION MISMATCH → qualitative.** White is COO of J&J **Innovative Medicine** (pharma, Titusville NJ). The verified 56-role WARN is J&J **MedTech / orthopedics** (New Brunswick, DePuy Synthes separation) — a different division. Attributing that cut to White is factually wrong. Ship qualitative; do not populate signal_source_url.
- **Walmart (Kieran Shanahan): SITE-SCOPED → qualitative (Dallas's call).** 306 is a Sunnyvale product/eng campus cut. Shanahan is the Bentonville enterprise COO, and the critic's own rule fails "a company figure scoped to a single site/unit." Real and attributable, but wrong-domain + site-scoped. Default: qualitative. Populate only if Dallas explicitly wants the site-framed number.
- **Nike (Venkatesh Alagirisamy): the one survivor.** 1,400 is company-level, in-window (Apr 23 2026), exact, COO-owned. Populate signal_source_url = CNBC. Still a technology-team round — fair hook, honest attribution.

**Net: of 5 anchors, only Nike carries a number. Citi (stale/aggregate), Abbott (none), J&J (wrong division), Walmart (site-scoped) all ship the qualitative no-number email.** The fail-closed gates make every one of these safe; the open question is strategy, not safety (see decision note at bottom).

## What this means for the regen

- **2 of 5 anchors flipped to no-number by H1** (Citi, Abbott). Both ship the qualitative frame — still a strong message, zero risk.
- **3 of 5 carry a real, cited, dated figure** (Walmart 306, Nike 1,400, J&J 56). The number gate will now key on the populated `signal_source_url`, so the critic can trust them.
- **Relevance caveat (H5, for Dallas's judgment):** all three sourced cuts are tech-org or divestiture RIFs, not service-workforce cost mandates. The email frames the prospect's own figure as "the stakes," then pivots to headcount-free idle-capacity recovery — defensible as a hook, but a sharp COO may note the cited cut wasn't their service floor. This is the "would you bet your career" call. Options per row if you want tighter fit: (a) send as-is (safe, attributed), (b) swap to the qualitative no-number frame even where a figure exists, or (c) re-source a service-workforce/back-office cost signal for these accounts (new Claygent/Chrome pass, small credit cost).

## Primary sources (full)
- Citi: [Crain's — 265 at Tribeca HQ, 3/16/26](https://www.crainsnewyork.com/banking-finance/cny-citigroup-tribeca-layoffs-03162026/) · [bankingdive — 286 NY (2024 event)](https://www.bankingdive.com/news/citi-layoffs-job-cuts-286-nyc-new-york-warn-tech-global-markets-may-3/708931/) · [ThinkAdvisor — "over 300" aggregate, 5/20/26](https://www.thinkadvisor.com/2026/05/20/citi-discloses-over-300-new-york-layoffs-part-of-ongoing-job-cuts/)
- Walmart: [American Bazaar — 306 Sunnyvale, 6/25/26](https://americanbazaaronline.com/2026/06/25/walmart-job-cuts-306-silicon-valley-employees-to-be-laid-off-soon-483517/) · [PeopleMatters](https://www.peoplematters.in/news/strategic-hr/walmart-lays-off-306-tech-workers-as-it-reorganises-product-and-engineering-teams-50488)
- Nike: [CNBC — 1,400 roles, 4/23/26](https://www.cnbc.com/2026/04/23/nike-job-cuts-layoffs.html) · [CIO Dive](https://www.ciodive.com/news/nike-cuts-1400-roles-reshapes-technology-team/818477/)
- J&J: [NJBIZ — 56 New Brunswick](https://njbiz.com/jnj-cutting-jobs-new-brunswick-hq/) · [FiercePharma — orthopedics separation](https://www.fiercepharma.com/pharma/jj-separates-its-orthopedics-business-it-lays-56-new-jersey) · [NJ DOL 2026 WARN archive](https://www.nj.gov/labor/assets/PDFs/WARN/2026_WARN_Notice_Archive.pdf)

## Decision note (Dallas's call — the motion's premise)

This motion's hook is "I saw the number YOU disclosed." Verification shows that hook only holds for **Nike**. The other four are safe to send as qualitative no-number emails, but qualitative removes the personalization that justified building a separate Cost-Mandate motion for these accounts.

Three paths:
1. **Proceed qualitative + Nike numbered** (safe, fast). Regenerate now under the hardened prompts; 4 rows ship the strong no-number frame, Nike carries its cited figure. Fail-closed gates hold; nothing sends.
2. **Re-source service-workforce cost signals** for Citi/Walmart/Abbott/J&J (a real cost-to-serve / back-office / contact-center efficiency mandate, not a tech-org RIF) before regen. Small Claygent/Chrome credit spend; restores the "your number" hook with a relevant figure.
3. **Re-pick the accounts.** If these five don't have a service-workforce cost mandate on the public record, they may be the wrong five for THIS motion.

## Re-sourcing pass (Option B executed 2026-07-16 — primary sources, 0 Clay credits)

Searched each account for a REAL service-workforce cost mandate (not a tech-org RIF), using fresh Q2 2026 earnings + restructuring disclosures. Result: **re-sourcing confirmed the mismatch — it did not rescue the premise.**

| Account | Best available cost signal (re-sourced) | Fit for THIS motion | Decision |
|---|---|---|---|
| **Nike** | 1,400 roles, company-level, CNBC 2026-04-23 | Tech-team, but in-window/exact/COO-owned | **NUMBER (only survivor)** |
| **Citi** | Q2'26 efficiency ratio improved to 57.4%, opex $14.2B (this week); 20K simplification is 2024 | "Winning on cost" = anti-hook; no fresh cut figure | **Qualitative / no fit** |
| **Walmart** | ~1,000 corp roles merging tech+product, AI-efficiency, 5/13/26; 306 Sunnyvale WARN | Tech/product; Shanahan runs US stores/ops = wrong domain | **Qualitative / no fit** |
| **J&J** | Q2'26 (this week): raised outlook, growing; no cost/restructuring figure; ortho-sep costs unquantified | Growing + White is wrong division (Innov. Medicine) | **No fit** |
| **Abbott** | Q2'26 (7/16): raised EPS guidance, $2.1B returned; only routine $58M H1 restructuring line | Growing, no mandate | **No fit** |

**Engineering conclusion:** these five accounts are the wrong universe for a "cite your disclosed cost number" motion — three are growing/raising guidance or beating on cost, two have tech-org cuts irrelevant to their COO's service floor. The fail-closed + source-gate engine correctly refuses to fabricate. The durable asset is the hardened engine; the fix is feeding it accounts with a genuine public service-workforce cost mandate (the separate universe-wave GO). Sources: Citi/JNJ/Abbott Q2 2026 earnings releases; Walmart corporate restructuring (gurufocus/Yahoo, 5/13/26).
