# Fable prompts B–E — portable, plug-and-play (updated with real data)

Prompt A (QBP) is handled separately in `Fable_Prompt_QBP_Rerun.md`. These are the remaining four. Paste each into the same Fable thread. No edits needed. Every return format is keyed to my real column headers and engine schemas.

Division of labor stays the same: Fable produces B, C, E and the D spec; I run the Apollo pull, the Clay build, and the conductor rehearsal here where the tools live.

---

## Prompt B — Earnings / financial-disclosure intent signal
Feeds: Clay Signals layer (L2) and a quotable line into Message Gen (L4). This is Naveen's second stated intent-signal idea (earnings calls, QBP lost-revenue commentary).

> I need an intent signal built from public financial disclosures for the parent organizations behind my 93 sub-4.0 Star Ratings contracts. The parents and their sub-4.0 enrollment are listed at the bottom, with a flag for whether they hold public earnings calls. Only 9 are public; prioritize by enrollment (Humana and UnitedHealth alone are more than half the prize).
>
> Source rules by parent type:
> - earnings_calls = yes: sweep the two most recent earnings calls, the latest 10-K and 10-Q. Look for Medicare Advantage margin pressure, Star Ratings or quality-bonus impact, membership or benefit cuts tied to Stars, and cost-reduction commitments.
> - earnings_calls = no (Blues, provider-owned, mutuals, PE-backed): there is no earnings call. Use press releases, state DOI rate filings, audited financial statements, and ratings-agency commentary (AM Best, Moody's) instead. If nothing public exists, say so for that parent rather than inventing.
>
> Return two things:
>
> 1. The sweep results as a CSV code block, columns EXACTLY:
> `parent_org,source_type,fiscal_period,verbatim_quote,url,angle_line,retrieved_date`
> (source_type = earnings_call / 10-K / 10-Q / press / rate_filing / ratings_agency; angle_line = the one sentence a rep could quote back to that account; verbatim_quote must be real and sourced to a working URL. Include a row with empty quote fields for any parent you checked and found nothing, so I know it was covered.)
>
> 2. A signal definition block I can wire in. My TAM engine's ONLY valid persona keys are exactly `cc_ops`, `wfm`, `cx`, `finance` — do not invent others (the Stars/Quality persona is handled in my Clay motion layer, not this engine). Return it in this shape:
> ```
> "qbp_earnings_pressure": { "label": "...", "weight": <0-25>, "play": "...", "stakes": "...", "route_personas": ["finance", "cc_ops"] }
> ```
> Plus one line on the threshold logic: how many/what kind of disclosure hits should make this signal fire for an account.

---

## Prompt C — Clay Message Gen system prompt v2
Feeds: Message Gen table (L4), the brain the Clay consultant left weak. Fastest visible week-one win since the pipe already exists.

> Draft the replacement system prompt for the AI column in my Clay Message Gen table. It takes an enriched contact row and writes the outreach for my Star Ratings motion. Note: this is NOT the contact-center idle-time pitch; it is the Star Ratings / QBP angle, so write fresh, do not borrow generic idle-time framing.
>
> It must encode:
> - Two priority personas with distinct angles: Persona 1 = VP Stars/Quality (leads with the star gap and the measures we can move); Persona 2 = CFO / Finance / Chief Actuary (leads with the dollar figure).
> - The addressability framing, which is my core POV: our platform moves the customer-service and admin Star measures (CAHPS, complaints, call center, appeals, access), NOT clinical/HEDIS. So the dollar I lead finance with is the ADDRESSABLE forgone QBP (the CS-attributable slice), not the gross number. Contracts whose clinical stars are already at 4.0+ are the best fit, because their entire sub-4.0 gap is on the side we own; make the prompt recognize and lean into that.
> - The Dynamic Workforce Orchestration platform pitch: a suite and a vision moving multiple metrics, positioned against what pure-human and pure-AI investments have failed to deliver. Not Queue Optimizer alone.
> - My copy rules: no em dashes, no AI-isms, contractions, one idea per message, prospect is the hero, make the meeting feel like their idea, front-load the point, brand-light.
> - Verified-claims-only: never state an Intradiem metric that isn't in the approved repository. Approval-tier discipline for 1:1 vs 1:many.
> - Standing external proof line (verified, third-party, so no Intradiem approval-tier limit): UnitedHealthcare told a federal court that a single failed call-center secret-shopper call cost it $190M in Star bonus payments under the prior rules (CMS Call Center Monitoring measure, retired for 2028 Stars; a judge ordered CMS to recalculate). Make this available as an optional credibility beat, especially for finance, as historical proof that one CS measure priced QBP money. Cite it as UHC's own stated figure under the old rules; never imply moving that measure still earns bonus.
>
> These are the real enriched columns available as tokens (use these exact names in your manifest): `first_name, last_name, full_name, job_title, company, company_domain, seniority_tier, members_sub4, cs_star, clin_star, gross_forgone_qbp_musd, addressable_forgone_qbp_musd, addressable_pct, cliff_edge_contracts, product_angle, why_now, earnings_angle_line, source_motion`.
>
> Return three things:
> 1. The full system prompt as ONE fenced text block, ready to paste into Clay.
> 2. A variable manifest table: each token above the prompt uses, and the fallback behavior if it's empty (e.g. if earnings_angle_line is blank, omit that beat).
> 3. Two worked examples generated from a plausible enriched row: one for Persona 1, one for Persona 2, so I can judge quality before wiring.

---

## Prompt D — Persona 1/2 coverage search SPEC (I run the Apollo pull here)
Feeds: Buying Committee / Contacts table (L3). Fable can't run my Apollo, so produce the spec and diff logic; I execute the enrichment here.

> I need to audit whether my existing Director+ contacts actually cover my two priority personas across all 93 sub-4.0 contracts (48 parent orgs), then produce a gap-fill target spec. I run the enrichment; you produce the specification.
>
> Return three things:
> 1. A search-spec table, one section per persona:
> - Persona 1 (VP Stars/Quality): exact title strings to INCLUDE (Stars, Star Ratings, Quality Improvement, CAHPS, HEDIS, Risk Adjustment/Quality), titles/departments to EXCLUDE (provider or hospital quality, clinical quality unrelated to plan Stars), seniority floor (Director+, bias VP+).
> - Persona 2 (Finance/Actuary): include titles, exclude titles, seniority floor. Large-parent special case, name these explicitly: for Humana, UnitedHealth, Centene, CVS/Aetna, Elevance, and Cigna, target the Medicare-segment finance lead or Chief Actuary, NOT the corporate CFO.
> 2. The gap-analysis logic as numbered steps: how to diff a fresh persona pull against my existing contacts to find uncovered contract-by-persona cells, and how to prioritize gaps (weight by addressable forgone QBP, so I fill the biggest-dollar uncovered accounts first).
> 3. The exact output schema my fill list should land in, so my Apollo pull matches my Clay import. Target these headers verbatim:
> `First Name,Last Name,Full Name,Job Title,Company,Company Domain,LinkedIn URL,Email,Email Status,Seniority Tier,Account Forgone QBP ($M),Cliff-Edge Contracts,Product Angle,Why Now,Source Motion,Sourced Date,GTM Engine Sourced`

---

## Prompt E — First 1-1 agenda + Bitbucket access outline (the Naveen docs)
The week-one moves that unblock the build (attribution, hours, Clay ownership, the repo access Naveen already asked me to justify).

> Draft two documents for my manager Naveen. Peer-level, no filler, no em dashes. Never frame my pre-start work as finished; it's a head start on an ongoing build.
>
> Context to weave in: my Star Ratings idea is an addressability cut: I score each sub-4.0 contract by the customer-service Star slice we can actually move, not the gross gap, so we target the biggest ADDRESSABLE dollar rather than just the biggest plan. The Q3 targets he called a rough sketch are ours to co-shape.
>
> Return two fenced markdown blocks:
> 1. First 1-1 agenda. Cover: finalizing the email sequencer approach (native Clay now, dedicated tool at volume); co-shaping the Q3 targets; defining what good looks like for attribution across my motion and Nate's current Star Ratings outbound (partnership framing, not credit defense); squad hours across the three motions; my addressability-cut Star Ratings idea; and the handoff of Clay-environment ownership he offered me.
> 2. Bitbucket access outline (the brief outline he asked for). Cover: version control for my signal, TAM, and cohesion engines; the Clay build pack and configs; test/CI; and read access to anything Engineering holds that touches GTM data. A short specific paragraph plus a bulleted access list.

---

## Parent-org universe for Prompt B (paste is already inside the prompt above)

```csv
parent_org,sub4_members,contracts,earnings_calls
Humana,3750073,8,yes
UnitedHealth,1380796,12,yes
Centene,225753,7,yes
CVS / Aetna,131184,6,yes
Medica Holding Company,111604,1,no
EmblemHealth  Inc.,86531,3,no
Blue Cross and Blue Shield of Massachusetts  Inc.,86193,2,no
Horizon Mutual Holdings  Inc,76022,2,no
California Physicians' Service,64672,2,no
Visiting Nurse Service of New York,60060,1,no
PacificSource,53306,1,no
Cambia Health Solutions  Inc.,52151,1,no
Imperial Health Plan of California,49913,1,no
Blue Cross Blue Shield of Michigan Mutual Ins. Co.,45000,1,no
Intermountain Health Care  Inc.,45000,1,no
UCare Minnesota,45000,1,no
Elevance,44411,2,yes
Blue Cross Blue Shield of Arizona,43003,1,no
The Cigna Group,37336,1,yes
Louisiana Health Service & Indemnity Company,36665,1,no
Hawaii Medical Service Association,35723,1,no
Zing Health Consolidator  Inc,32919,1,no
CareSource,29364,1,no
HCSC,28966,2,no
Devoted Health  Inc.,25262,4,no
Thomas Jefferson University,25023,1,no
Commonwealth Care Alliance  Inc.,18086,1,no
Banner Health,17932,2,no
Mass General Brigham Incorporated,17040,1,no
Baystate Health  Inc.,14602,2,no
SCAN Group,14455,2,no
CareOregon  Inc.,13962,1,no
Molina,13391,2,yes
LifeBridge Health  Inc.,13103,1,no
Point32Health  Inc.,12991,2,no
BMC Health System  Inc.,12000,1,no
Ochsner Clinic Foundation,12000,1,no
Aware Integrated  Inc.,11563,1,no
Indiana University Health,11476,1,no
Fallon Community Health Plan  Inc.,9927,1,no
Alignment Healthcare USA  LLC,9056,1,yes
Guidewell Mutual Holding Corporation,6676,1,no
Centers Plan for Healthy Living  LLC,5464,1,no
Denver Health and Hospital Authority,5091,1,no
Clover Health Holdings  Inc.,3632,1,yes
Rifkin Managed Care Holding  LLC,2566,2,no
Longevity Health Founders  LLC,898,1,no
AIDS Healthcare Foundation,607,1,no
```
