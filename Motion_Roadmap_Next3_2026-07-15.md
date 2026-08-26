# GTM Motion Roadmap: Next 3 Motions
**After Star Ratings + Back Office, Dallas Andrews, GTM Engineer, 2026-07-15**

Each motion is a **two-layer build**, not one. The repo/engine (config + universe + registry) is the brain and the spec. **Clay is where the motion actually runs and where Nathan and the reps consume it** (tables, enrichment, MessageGen, critic gate, native campaigns). A motion is not "built" until both layers exist and stay in sync: the engine config defines the triggers, personas, and proof; the Clay table and campaign are what put contacts in a rep's queue. This doc specs both layers for all three.

---

## Current config state (verified 2026-07-15)

Answering "are the other motions already configged": partly, and unevenly across layers. Verified against `tam-outbound-engine/config/triggers.json`, `intradiem-signal-engine/config/thresholds.json`, and the strike-sequence Motion Registry.

| Motion | TAM trigger taxonomy | Signal engine | Strike-seq Motion Registry | Clay (live tool) |
|---|---|---|---|---|
| **Star Ratings** | Populated (`qbp_earnings_pressure`, `quality_identity_gap`) | base/default motion | **POPULATED** (full pack + Centene reference) | **Live** (Contacts table, gate-fed P1/P2 campaigns, MessageGen + critic) |
| **Back Office** | not in taxonomy | **Configged** (`motion_overrides.back_office` fork, 6 BO signals, `--motion` CLI) | **STUB** (proof TBD) | **Live** (101-row universe + 59 contacts) |
| Cost-Mandate | trigger exists (`cost_mandate` wt 24, generic) | no | **STUB** (Registry slot 5) | not built |
| WFM-Adjacency | partial (`wfm_hiring` only) | no | **STUB** (Registry slot 4, Competitive) | not built |
| Install-Base | no | **Configged** (the 6 signals ARE this motion) | **STUB** (Registry slot 3) | not built as an outbound table |

Two things this makes clear. First, all three new motions already have a **Registry slot** (3, 4, 5), all stubs, so this is populate-the-stub, not create-from-scratch. Second, "configged in the engine" is not the same as "live", both engines carry `data_source: "mock"` in their meta/threshold files, so even Stars is scoring on seeded fixtures in the repo. The live data lives in Clay. That's exactly why the Clay layer below is the half of the build that actually books meetings.

---

## Build order (ratified 2026-07-15)

Cost-Mandate leads. Rationale you set: internal usage-data access and warm CSM/AE intros are the slow track here, so the two motions that run entirely on external data ship first, and the internally-gated one scaffolds now and populates as access matures.

1. **Cost-Mandate / Efficiency**, external data, zero internal dependency. **Build now.**
2. **WFM-Adjacency / Idle-Time**, external data (job posts, tech-stack signals), zero internal dependency. **Build next.** Also functions as a targeting/conversion overlay on #1 and on Stars.
3. **Install-Base Expansion & White-Space**, highest value, but its live signal needs internal product-usage data and its intros need relationships you're still building. **Scaffold now** on the existing signal engine; turn on the live universe as data access + intros clear.

WFM-Adjacency sits ahead of Install-Base only because of the dependency profile you flagged, it runs on external signals today, Install-Base's high-value version does not. If an intro track opens faster than expected, Install-Base moves up.

---

## Shared guardrails (all three motions)

- **Verified-claims discipline (source-level):** only Value Repository VERIFIED claims reach a prospect. Humana is the one verified customer story. By-vertical public stats (below) are positioning-tier: usable, labeled "public," approval tier confirmed before external send. Idle-% stats, any non-Humana customer outcome, and Intradiem NRR/ROI stay **DO-NOT-SEND**. This gate lives in Clay as the `msg1_critic` column, not just in `config/proof.json`; both must carry the same rule.
- **Customer exclusion / inclusion:** Cost-Mandate and WFM-Adjacency are net-new (exclude current customers via `customer_flag`). Install-Base is the inverse, customers only (the same inverted-kill-switch pattern already used for Back Office).
- **Dry-run default; sender = the rep, not Dallas.** Every Clay campaign ships gate-fed: Draft + rep review + `msg1_critic` PASS before anything sends.
- **WFM vendors are the layer we sit on top of, never a rip-and-replace.** Adjacency, not displacement.
- **Clay credits:** every enrichment run gets a pre-run estimate and a ledger row before it executes (credit-steward standing rule: no un-budgeted runs). Tier enrichments, firmographics cheap-and-broad first, waterfall/technographic/intent only on rows that already cleared fit. Estimates below are first-pass; sample 10 rows to confirm any unknown per-provider cost before the full run.
- **Clay build mechanism:** tables and columns are built via Chrome (the Clay MCP can't create tables); verify current Clay UI/pricing before any click-by-click, don't instruct from memory.
- **Annotation keys** prefixed `_` (e.g. `_note`) are comments, consistent with the existing `_comment` at the top of `triggers.json`; strip or ignore at load.

---

## Motion 1: Cost-Mandate / Efficiency  `[BUILD NOW]`  (populates Registry slot 5)

**Motion key:** `cost_mandate_xvert`
**One-liner:** Recover labor cost already on the payroll. No new headcount, no transformation project, bookable this fiscal period.

**Why this is the lead motion:** it's the universal buying trigger and the one that takes you off the single-season, single-vertical Stars bet. It's vertical-agnostic, so it opens the five verticals Stars can't reach (Financial Services, Insurance, Retail, Telecom, Utilities) and feeds Mandate 1 (15 new-logo meetings) from a TAM many times larger than MA payers. Runs 100% on external data you control today.

**Universe / targeting:** net-new logos across all six verticals with structured, high-volume workforces (contact center and/or back office) showing a public cost or efficiency signal.

**Primary persona route:** `finance` / `coo_finance` (COO, CFO, VP Finance, SVP/VP Operations, the cost owner who sees both floors). Secondary: `cc_ops`, `bo_shared` / `bo_claims` (the floor owners who feel the mandate).

### Engine layer

**Triggers, paste-ready for `config/triggers.json`** (`cost_mandate` already exists at weight 24; this motion activates it and adds sharper variants):

```json
"efficiency_mandate_public": {
  "label": "Public efficiency / cost-takeout mandate (earnings, guidance, memo)",
  "weight": 24,
  "play": "Mirror the company's own disclosed cost language back, then localize to the workforce: the target names efficiency; the fastest recoverable dollar is idle labor already on the payroll, no new headcount and no transformation project.",
  "stakes": "The mandate is committed publicly and due this fiscal period, so budget and executive attention exist now; recoverable labor cost is the fastest line to book against it.",
  "route_personas": ["finance", "cc_ops", "bo_shared"]
},
"rif_workforce_reduction": {
  "label": "Layoff / RIF / restructuring announced",
  "weight": 21,
  "play": "They are cutting heads to hit a number. Reframe from cut-capacity to recover-capacity: automation recovers the idle time of the remaining workforce so service does not degrade after the cut.",
  "stakes": "Post-RIF is exactly when SLAs slip and the remaining team burns out; recovering idle capacity protects service without rehiring what was just cut.",
  "route_personas": ["finance", "cc_ops", "bo_shared"]
},
"margin_pressure_earnings": {
  "label": "Margin / cost-to-serve pressure disclosed in earnings",
  "weight": 20,
  "play": "Localize the disclosed margin pressure to the labor line: cost-per-transaction and cost-to-serve are where idle-time automation books recoverable cost this period.",
  "stakes": "Guidance has named the pressure, so the finance owner is measured on it now; this is a recoverable-cost lever that does not wait on a transformation cycle.",
  "route_personas": ["finance", "coo_finance"]
},
"hiring_freeze": {
  "label": "Hiring freeze / do-more-with-less",
  "weight": 18,
  "play": "Volume is not frozen even though headcount is. Recover capacity from the existing workforce's idle time to absorb the load the freeze would otherwise break.",
  "stakes": "Under a freeze, every point of demand growth lands on a fixed team; recovered idle capacity is the only headcount-free way to close that gap.",
  "route_personas": ["finance", "cc_ops"]
}
```

(`wfm_hiring` already in the file, the automate-versus-hire math, also routes into this motion.) Also: populate Registry slot 5 (product angle = Queue Optimizer + Back Office Optimizer, framed as capacity gained from existing headcount), add the cross-vertical universe CSV to `data/`, map proof in `config/proof.json`.

### Clay layer

- **Table:** new net-new universe table `Cost-Mandate Universe (x-vert)` (accounts across the 6 verticals) feeding a `motion = cost_mandate` segment on the Contacts table, so it reuses the existing enrichment, critic, and campaign machinery rather than a parallel stack.
- **Columns to add:** vertical + workforce-size firmographics; the 4 cost signals as enrichment/formula columns (earnings/news + job-postings sources); `fit_score`; `customer_flag` (exclude current customers, same gate as Stars); waterfall email + ZeroBounce; a MessageGen variant with `product_angle = recover-idle-cost/ROI`; `msg1_critic` PASS/FAIL gate; `send_ready`; the hidden Sync-to-campaign column.
- **Enrichment + credit estimate:** firmographics cheap-and-broad across the full universe; waterfall + ZeroBounce (~1.46 cr/contact) only on fit-cleared rows; job-postings/news enrichment for the cost signals (per-provider cost unknown, sample 10 rows first). First wave ~200 contacts ≈ **~350-500 credits** (est., sample-then-confirm), the signal-enrichment line is the variable.
- **Campaign:** new native-sequencer campaign `Cost-Mandate (Finance/COO)`, optional Ops lane, gate-fed (Draft + rep review + critic PASS), sender = the assigned rep.

**Proof mapping:**
- Healthcare accounts → **Humana** 7X ROI at five years, first-year in-year return, 2 hours of capacity recovered per agent per month (VERIFIED, public, customer-told).
- Match-the-vertical public stats (positioning tier, label "public," confirm approval before external): FinServ 11% handle-time reduction; Telecom 5% productive capacity recovered; Insurance 31% reduction in stuck-on-call; Retail 16-second hold-time cut; Utilities Centrica 20% training-delivery boost; Healthcare $7M annual savings (top-5 US org).
- **DO-NOT-SEND:** idle-% stats, Intradiem NRR/ROI, any non-Humana customer outcome.

**Reuses / net-new:** engine, `cost_mandate` trigger + ROI business-case skill exist; net-new = 4 trigger variants + x-vert universe + proof map + Registry slot 5. Clay, reuses Contacts enrichment/critic/campaign pattern; net-new = universe table + cost-signal columns + a campaign. **Build cost: LOW-MED engine / MED Clay.**

---

## Motion 2: WFM-Adjacency / Idle-Time  `[BUILD NEXT]`  (populates Registry slot 4, Competitive)

**Motion key:** `wfm_adjacency`
**One-liner:** You have WFM. You don't have the layer that acts in the idle time WFM never touches, and WFM stops at the contact center while your back office runs uncovered.

**Why second:** a large share of the addressable market already has Verint / NICE / Calabrio and believes it's covered, so this is the wedge that wins the meetings the other motions lose. It's structural and hard to refute, WFM schedules and forecasts, it does nothing in the gaps between scheduled activities, and it's contact-center-only. It also runs entirely on external signals, so no internal dependency. Doubles as an overlay: the same signal sharpens targeting on Cost-Mandate and Stars accounts.

**Primary persona route:** `wfm` (Manager/Director WFM, Capacity Planning, Intraday, RTA, the entry and technical validator), routed up to `cc_ops` and `coo_finance`.

### Engine layer

**Triggers, paste-ready for `config/triggers.json`:**

```json
"wfm_purchase_renewal": {
  "label": "WFM/WEM purchase or renewal (Verint, NICE, Calabrio, Genesys, Amazon Connect)",
  "weight": 20,
  "play": "They just invested in scheduling and forecasting. That is the layer we sit on top of: WFM plans the day, it does nothing in the idle gaps between scheduled activities, and it stops at the contact center while the back office runs uncovered. Position as the execution layer on top of the investment they just made, never as a replacement for it.",
  "stakes": "The WFM decision is fresh, so the workforce-execution gap it leaves is top of mind and unbudgeted-for; closing it now compounds the ROI of the spend they just approved.",
  "route_personas": ["wfm", "cc_ops", "finance"]
},
"rta_hiring": {
  "label": "Hiring real-time analysts / intraday managers / RTA",
  "weight": 22,
  "play": "They are paying people to do by hand what the idle-time layer automates: watching the floor and reallocating in real time. Lead with the automate-versus-staff math before the roles fill.",
  "stakes": "Once those reqs close, manual real-time management locks into run-rate and still cannot cover the idle time automation would; cheaper to close the gap before the offers go out.",
  "route_personas": ["wfm", "cc_ops", "finance"]
},
"wfm_migration": {
  "label": "WFM/CCaaS migration or vendor switch in progress",
  "weight": 17,
  "play": "A migration is an open-hood moment for the whole workforce stack. Enter as the execution layer that rides on whichever WFM they land on, and extends past the contact center into the back office the migration does not touch.",
  "stakes": "The evaluation window is open now; after cutover the stack refreezes for years, and the back-office gap goes uncovered the whole time.",
  "route_personas": ["wfm", "cc_ops"]
}
```

Populate Registry slot 4 (Competitive displacement) with the WFM-adjacency framing rather than a rip-and-replace one, load `intradiem-competitive-intel` alongside.

### Clay layer

- **Table:** run as a **signal overlay on the Cost-Mandate net-new table**, not a separate stack, these are technographic/job-posting signals that enrich the same accounts. Add a `motion = wfm_adjacency` tag/segment and a WFM-angle MessageGen variant.
- **Columns to add:** WFM technographic (which vendor: Verint/NICE/Calabrio/Genesys/Amazon Connect) via technographic enrichment; RTA/intraday hiring signal (job-postings enrichment, reuses the `parent_hiring_lookup` infra already in the L2 layer); `wfm_signal_score`; a MessageGen variant with `product_angle = idle-time-on-top-of-WFM`; `msg1_critic` gate; a `wfm` persona contact sourced as the entry point.
- **Enrichment + credit estimate:** technographic enrichment is the main new cost (per-provider, verify current Clay cost, sample 10 first); job-postings reuse existing hiring infra; contacts largely overlap the net-new universe so incremental waterfall is low. Incremental first wave ≈ **~150-300 credits** (est., sample-then-confirm).
- **Campaign:** a WFM-persona lane, either a segment of the Cost-Mandate campaign or a dedicated `WFM-Adjacency (WFM/RTA)` campaign; gate-fed; sender = rep.

**Proof mapping:**
- Idle-time-gap positioning: Intradiem acts in the idle time between scheduled activities, the gap WFM never addresses; orchestrates front **and** back office where WFM is contact-center-only (VERIFIED positioning).
- **Humana** occupancy +4%, AHT down 45 seconds, 2 hours of capacity per agent per month, what the layer delivers on top of existing WFM (VERIFIED).
- **DO-NOT-SEND:** any competitor's named results; any claim that frames WFM as replaced.

**Reuses / net-new:** engine, war-room WFM/CCaaS sweep + competitive-intel + "We Have WFM" objection handler exist; net-new = 3 triggers + Registry slot 4 framing. Clay, overlays the Cost-Mandate table; net-new = technographic + RTA columns + a WFM MessageGen variant. **Build cost: LOW engine / LOW-MED Clay.**

---

## Motion 3: Install-Base Expansion & White-Space  `[SCAFFOLD NOW, TURN ON AS ACCESS CLEARS]`  (populates Registry slot 3)

**Motion key:** `installbase_expansion`
**One-liner:** Mine the installed base (~350K agents, 114% NRR) for the next dollar, the Humana land-and-expand arc, productized.

**Why it's third here (not by value, by dependency):** this is the highest-value motion, warmest audience, shortest cycle, best closed-won rate, and it retires Mandate 3 (200 back-office contacts inside existing customers). But its high-value signal needs internal product-usage data (governed, slow here) and its warm intros need CSM/AE relationships you're still building. So scaffold the wrapper now and populate the live universe as data access and intros mature.

**Reuses (this is the key point):** the `intradiem-signal-engine` **already computes the six signals**, `seat_utilization`, `coaching_coverage`, `rule_engine_active`, `crm_not_connected` (expansion → route AE/CSM), and `automation_volume_drop`, `champion_job_change` (risk). This motion = wrap `signals.json` into Registry slot 3 as an expansion/save motion. The wrapper is LOW build cost; the gate is data access, not code.

**Primary persona route:** existing champion + owner of the dark workforce, `bo_claims` / `bo_shared` when a contact-center customer has a dark back office, `cc_ops` when a back-office customer has a dark contact center, plus `coo_finance` for multi-BU expansion.

### Engine layer

**Triggers, paste-ready for `config/triggers.json`:**

```json
"usage_whitespace": {
  "label": "Heavy usage in one workforce, adjacent workforce dark",
  "weight": 26,
  "play": "The customer already proves the mechanic in one workforce. Extend the same idle-time orchestration to the adjacent workforce not on platform yet, contact center to back office, or one BU to the rest.",
  "stakes": "The proof is already in-house and the champion already believes it; the only thing between them and the next result is turning it on where it is dark.",
  "route_personas": ["bo_claims", "bo_shared", "cc_ops", "coo_finance"],
  "_note": "requires internal product-usage data (governed), see dependency note; gated track"
},
"usage_decline": {
  "label": "Automation volume drop (maps to signal-engine automation_volume_drop), churn save",
  "weight": 24,
  "play": "Usage is sliding. Get ahead of the renewal risk with a re-engagement play that re-seats the automation and re-proves value before the renewal conversation.",
  "stakes": "A usage decline that reaches the renewal desk becomes a downgrade conversation; catching it now turns a save into an expansion.",
  "route_personas": ["cc_ops", "coo_finance"],
  "_note": "internal signal-engine risk signal; gated track"
},
"multi_bu_expansion": {
  "label": "Customer with multiple BUs / subsidiaries not all on platform (firmographic, ungated)",
  "weight": 20,
  "play": "One BU is live and referenceable. Use it as the internal proof to expand to the sister BUs still running on overtime and backlog.",
  "stakes": "The internal reference is the warmest proof in the market; every quarter the sister BUs stay dark is forgone capacity the customer already knows how to recover.",
  "route_personas": ["coo_finance", "cc_ops", "bo_shared"]
}
```

The two `usage_*` triggers already have their scoring logic in `thresholds.json`, this is wiring, not new signal design. Populate Registry slot 3 (existing-customer lane; Gate B routes here rather than excluding).

### Clay layer

- **Table:** a **customers-only table** (inverted `customer_flag`, the same "fork not copy" pattern already used for Back Office). Reuse already-enriched install-base contacts from the customer file (101 accounts) and the Contacts table, so most rows need no new enrichment.
- **Columns to add:** the 6 signal-engine signals as columns (populated from the internal usage export when it lands, gated); `multi_bu_expansion` firmographic flag (ungated, buildable now); `expansion_type`; AE/CSM owner routing with an `owner_cleared` send gate; a MessageGen variant with `product_angle = land-and-expand / Humana arc`; `msg1_critic` gate.
- **Enrichment + credit estimate:** LOWEST of the three. Ungated interim = firmographic BU/subsidiary mapping on existing customer accounts + any gap-fill contacts; the gated signal columns read the internal usage export (not Clay credits). First wave ≈ **~50-150 credits** (est., sample-then-confirm), most cost avoided because the base is already enriched.
- **Campaign:** warm-intro-fed, routed through the AE/CSM (not the cold sequencer), or a low-volume expansion campaign gated on `owner_cleared`. Sender = the AE/CSM, not a BDR.

**Proof mapping:**
- **Humana** land-and-expand arc, contact center into back office, 7X over five years, first-year in-year return (VERIFIED, public). This is the archetype for the exact motion, so it's the lead proof.
- The customer's **own** results, once surfaced through the AE/CSM (strongest possible proof; per-account, respect approval tier).
- 114% NRR is company-level internal framing, **DO-NOT-SEND** to prospects.

**Reuses / net-new:** engine, full signal engine (6 signals) + Registry slot 3 stub exist; net-new = registry wrapper + ungated firmographic list. Clay, reuses enriched customer base; net-new = customers-only table + signal columns (gated) + owner-gated campaign. **Build cost: LOW engine / LOW Clay (ungated), gated go-live tracks usage-data access.**

---

## What "build" means per motion (both layers)

| Motion | Engine layer (net-new) | Clay layer (net-new) | Clay credit est. (first wave) | Data dependency |
|---|---|---|---|---|
| Cost-Mandate | 4 trigger variants, x-vert universe CSV, proof map, Registry slot 5 | universe table + 4 cost-signal columns + campaign | ~350-500 cr | None (external) |
| WFM-Adjacency | 3 triggers, Registry slot 4 framing | technographic + RTA columns (overlay on #1) + WFM MessageGen variant | ~150-300 cr | None (external) |
| Install-Base | registry wrapper, ungated firmographic list | customers-only table + 6 signal columns (gated) + owner-gated campaign | ~50-150 cr | Internal usage data (slow) + CSM intros |

First-wave total estimate ~550-950 credits for all three, roughly one-fifth of the 5,000 allocated (against the ~3,000 quarter worst-case planning frame). Every run gets a 10-row sample + ledger row before it executes.

---

## Config-change checklist (two tracks per motion)

**Engine track (repo):**
1. Add the trigger entries above to `config/triggers.json`.
2. Add/confirm persona definitions in `config/personas.json` for any new keys (`bo_claims`, `bo_shared`, `finance`/`coo_finance`).
3. Populate the Registry slot in the strike-sequence skill (slots 3, 4, 5 already exist as stubs, fill the why-now, product angle, persona pains, approved proof, don't create a new slot).
4. Drop the universe CSV into `data/`, the documented swap-in point; don't touch engine logic.
5. Map proof in `config/proof.json` and mirror into the Value Repository so the guardrail and the repo never diverge.

**Clay track (live tool, via Chrome):**
6. Pre-run credit estimate + ledger row (no un-budgeted runs); sample 10 rows to confirm any unknown per-provider cost.
7. Build the universe/customers table and columns (Clay MCP can't create tables, use Chrome; verify current UI first).
8. Tier enrichment: firmographics on all rows, waterfall/technographic only on fit-cleared rows.
9. Add the motion's MessageGen `product_angle` variant + the `msg1_critic` gate carrying the same verified-claims rule as `proof.json`.
10. Stand up the gate-fed campaign (Draft + rep review + critic PASS; sender = rep or, for Install-Base, the AE/CSM).
11. Append actuals to `Clay_Credit_Ledger.md` after the run; drift over 25% gets a cause note.

---

## Open items / assumptions flagged

- **Persona-key normalization: RESOLVED 2026-07-15.** Standardized `finance` to `coo_finance` across the engine config, generated plays, and tests (25/25 green); canonical = the ICP rubric keys. The trigger stubs above still show `finance`, read them as `coo_finance`. Clay `persona_key` is a separate motion-label layer, untouched.
- **By-vertical public stats** (FinServ 11%, Telecom 5%, etc.) are positioning-tier and need an approval-tier confirmation before any external send. Treated as "public, verify before external" throughout, in both `proof.json` and the Clay `msg1_critic` rule.
- **Engines are on mock data** (`data_source: "mock"` in both meta/threshold files). The repo scores fixtures; Clay holds the live data. Flip to "live" only when a real TAM/CRM/usage export replaces the seed.
- **Install-Base go-live date is unknown** and deliberately uncommitted, it tracks whenever event-level usage access clears, not a calendar date.
- **Clay per-provider costs** (technographic, news/signal enrichment) are the unknowns in the credit estimates, sample 10 rows and confirm against current Clay pricing before each full run.
- Weights above are first-pass relative to the existing `cost_mandate` = 24 anchor; tune against real reply data once the motions run.
