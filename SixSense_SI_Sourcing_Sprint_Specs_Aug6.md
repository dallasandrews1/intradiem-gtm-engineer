# 6sense SI Sourcing Sprint — Discovery Filter Specs (Aug 6 2026)

**Budget:** 183,318 SI credits. **Expire Sun Aug 30 2026.** Last working day **Fri Aug 28** = 16 business days from today.
**Rate:** 1 credit = 1 person, email(s) + phone(s) together. Unlock is free when no data exists; **CSV export charges 1 credit regardless**. Unlocked records re-enrich free for 12 months (through Aug 2027).

**Status: specs only. Nothing exported. Spend is Dallas's trigger.**

---

## Headline finding — read before the specs

Dallas asked me to flag any spec whose estimate exceeds what the motion can process. **The finding is the inverse.** Every motion with a defined account universe is orders of magnitude too small to absorb this pool:

| Motion | Accounts defined | Contacts at current cap rule | Contacts at full committee depth |
|---|---|---|---|
| Star Ratings Tier A+B | 32 (26 cold-eligible) | ~260 | ~1,000–1,500 |
| Back Office | 101 | ~400–500 | ~2,000–3,000 |
| Install Base | 101 (same accounts) | n/a | ~1,000 |
| **Subtotal** | | | **~4,000–5,500** |

That is **~3% of 183,318**. The cap rules (`3 per persona`, `2 per persona`, Tier-1-only) were written for Clay scarcity. They are the wrong constraint against a pool that expires in 16 days.

**The two motions that could absorb real volume have no account universe at all:**

- **WFM-Adjacency** is signal-first: "Clay technographic search (Verint / NICE / Calabrio / Genesys / Amazon Connect) + RTA/intraday job postings." `WFM_Adjacency_Clone_Pack_v1.md` line 97: *"The real signal-first universe wave is a separate credit GO — do not source it without explicit approval."* **That credit gate is now free.**
- **Cost-Mandate** is event-first. Accounts don't exist until a public cost mandate is announced in-window. Currently 1 locked account (Acrisure).

SI Discovery has a **Technology Used** filter (search + Status + Confidence Score range) and a **Job Postings** filter (Job Post Title + count + location + duration). Those are precisely the two inputs the WFM-Adjacency universe spec calls for.

**Recommendation: Spec 3 (WFM-Adjacency) is the priority, not Spec 1.** It is the only motion that can convert a meaningful share of this pool into a durable asset, and it has been blocked on exactly the credit gate that just disappeared.

Let the remainder expire. Sourcing out-of-ICP contacts to run the balance down costs Clay credits on every junk row downstream and poisons the tables.

---

## Four gate findings that must be resolved before any export

GATE-1 and GATE-2 came from the file review. GATE-3 and GATE-4 came from running the live functions and querying real rows on 2026-08-06.

### GATE-1 — The denylist screen will not catch 90+ current customers

`tam-outbound-engine/config/customer_denylist.json` contains **1 domain** (`hcsc.com`) and **10 name aliases** (hcsc, health care service, humana, unitedhealth, uhc, cvs health, aetna, molina, elevance, anthem).

It points at `greenlight-pack/Active_Customers_SF_Jul10.csv`, which holds **101 accounts**.

Any screen run against the JSON aliases alone passes ~90 current customers as cold-eligible. **Screen against the 101-row SF CSV, not the JSON.** The JSON is a hand-maintained overlay for brand/legal-name gaps, not the source of truth, and its own `_source` note says so.

Also: the SF export is dated **Jul 10**. It is 27 days stale going into a sprint that sources tens of thousands of contacts. Refresh it from Nate before export week.

### GATE-2 — 77% of Stars addressable value sits on the customer list

Six of the top seven Stars Tier A+B parents by addressable value are current Intradiem customers:

| Parent | addr_2028 ($M) | On customer list |
|---|---|---|
| Humana Inc. | 1,082.8 | Yes |
| UnitedHealth Group | 315.9 | Yes |
| CVS Health / Aetna | 224.5 | Yes |
| Centene Corporation | 187.0 | **No — clean** |
| Elevance Health | 142.9 | Yes |
| Health Care Service Corporation | 105.6 | Yes |
| Molina Healthcare | 69.9 | Yes |

**$1,941.6M of the $2,511M Tier A+B addressable total is on the customer list.** Centene is the only clean name in the top seven.

This is not a problem to fix, it's a routing rule. Those six are **invalid for Stars cold outbound** (the Stars motion drops customers to zero) and **valid, warm, Tier-1 back-office targets** (`BackOffice_ICP_v1.md` names Aetna/UHG/Humana/Elevance/CVS/Molina/HCSC as Tier-1 anchors, where `customer_flag` is deliberately *not* an exclusion).

**Same parent orgs. Opposite gate treatment. Different destination tables.** Source them once under Spec 2, never under Spec 1.

### GATE-3 — the customer-exclude gate has a type mismatch and has never been tested on the rows that matter

Live inspection of the Stars send-readiness workflow (`wf_0tiegzuo3PzJ4UtUGFA`, node `1g. Customer-exclude gate`) on 2026-08-06:

- The node's `inputSchema` declares `customer_exclude` as **`"type": "boolean"`**.
- The node's rule compares it with **`Equal` against the string `"TRUE"`**.
- The live table (`t_0thtm73HHxyiupTuepK`) stores it as **text**: 16 rows `"TRUE"`, 127 rows `"FALSE"`.

A boolean `true` does not equal the string `"TRUE"`. Whether this fires depends on Clay's coercion behavior between the declared schema type and the rule operand, which cannot be settled by reading the config.

**Current state: no leak has occurred.** All 16 `customer_exclude = TRUE` rows were queried directly. Every one has `send_ready = HOLD` and a **null** email-1 draft. No copy has ever been generated for a customer.

**But 12 of those 16 also have `persona_key = null`**, which means node 2g would have caught them regardless. Only **4 rows** actually test node 1g in isolation:

| Company | Job Title | persona_key |
|---|---|---|
| Health Care Service Corporation | Divisional SVP, Pharmacy Finance and Actuarial | `coo_finance` |
| Health Care Service Corporation | Executive Director & Actuary | `coo_finance` |
| Health Care Service Corporation | Sr. Director Coding Compliance & Quality Improvement | `stars_quality` |
| BCBS of IL, MT, NM, OK & TX | Executive Director, Operations - Strategy and Performance Management | `cc_ops` |

For those four, node 1g is the **only** thing between a current customer and generated cold copy. Their clean state is consistent with the gate working, and also consistent with the workflow never having run on them.

**Required before the sprint loads volume:** run the workflow on one of those four real rows and confirm it exits `EXCLUDED` at node 1g. Per CLAUDE.md this is the one check that must run on a real row, never synthetic `--input`, because a synthetic pass can prove exclusion works while a real row slips through. Dallas triggers it; it is a live run.

Today the accidental `persona_key = null` second layer is doing work the gate is supposed to do alone. Sourcing 30,000 contacts with properly-populated persona keys removes that accidental layer.

### GATE-4 — 13 rows exit silently on a null persona key

The Stars persona gate (node `2g`) accepts `persona_key` ∈ **{`stars_quality`, `coo_finance`, `cc_ops`}**. Live table distribution: `coo_finance` 46, `stars_quality` 42, `cc_ops` 41, **null 13**, `bo_claims` 1.

So **14 of 143 rows (10%) exit as `HOLD_persona`** and never reach copy. The single `bo_claims` row is arguably correct routing. The 13 nulls are not; they are unclassified rows failing open into a hold state with no signal that anything was skipped.

**Doc drift, not a defect:** `StarRatings_PersonaPull_Runbook.md` step 4 specifies the finance persona key as **`medicare_finance`**. The live table and the live gate both use **`coo_finance`**. Any new sourcing that follows the runbook literally would tag `medicare_finance` and exit every finance contact at node 2g. **Spec 1 uses `coo_finance`.** Fix the runbook.

---

## Global filter settings (apply to every spec)

Exact SI Discovery filter names, verified against 6sense's current filter documentation:

| Filter | Setting | Why |
|---|---|---|
| **Has Direct Dial** | `True` | Solves the CSV-export-charges-on-no-data trap. Never export a record with no phone. |
| **Direct Dial Type** | `Both` (work + mobile) | Mobile is the goal; work phone is acceptable fallback at no extra cost. |
| **Email Confidence** | `A+`, `A` (add `B` only if volume is short) | Bounce protection. Single-domain concentration is what burned the Hartford load. |
| **Unlocked Contacts** | `False` | Dedup against anything already unlocked. Prevents paying twice. |
| **Exported Contacts** | `False` | Dedup against past exports. |
| **Contact Location** | Country = United States (Canada for BMO/TD/RBC/Bell/TELUS rows) | Motions are NA. UK lanes are Jack's and out of scope here. |

**Note on phone:** `BackOffice_PersonaPull_Spec.md` says *"email-first; skip mobile/phone this pass."* That was a Clay cost decision. At 1 credit for email **and** phone together, that constraint no longer applies. **Every spec below pulls phone.** This also finally feeds the Cold Call Playbook (`motions/shared/Cold_Call_Playbook_Aug2.md`), which has had no dialable numbers behind it.

**Seniority values available:** C-Level, Vice President, Director, Manager, Senior, Staff, Other.
**Job Function values:** 23 categories including Customer Service & Support, Operations, Finance, Healthcare Services, Management, Information Technology.
**Company Search and Job Title both accept bulk comma-separated values** — paste account lists and title strings directly.

**Export ceilings:** CSV 25,000 / CRM 10,000 / SEP 50. SEP is useless at volume; CSV is the path, then Clay ingests in waves.

---

## SPEC 1 — Star Ratings Tier A+B

**Source list:** `StarRatings_PersonaPull_RunConfig_TierAB.csv` (32 parents)
**After GATE-2 screen: 26 cold-eligible parents.** Remove Humana, UnitedHealth, CVS/Aetna, Elevance, HCSC, Molina → route to Spec 2.

**Domain problem:** 17 of the 32 rows carry `VERIFY` in `suggested_domain` (the runbook says 13 — the config has drifted, reconcile before export). Use **Company Search** with bulk comma-separated *names* as the fallback; SI resolves org names natively, so this is less painful than it was in Apollo. Still verify each resolves to the health-plan entity, not a parent health system.

**Provider-owned parents** (Presbyterian, Lumeris, IEHP, L.A. Care, CalOptima, Baystate, Mass General Brigham, NYC H+H): filter to the **health-plan entity**, not the delivery system. This is the single highest-noise risk in this spec.

### Personas

| Persona | Job Title strings (bulk paste, OR) | Seniority | Job Function |
|---|---|---|---|
| **P1 `stars_quality`** | Stars, Star Ratings, Stars Improvement, Medicare Stars, Quality Improvement, Quality Performance, CAHPS, HEDIS, Quality & Risk Adjustment, Medicare Quality, Health Plan Quality, Member Experience | Director, VP, C-Level | Healthcare Services, Operations, Management |
| **P2 `medicare_finance`** | CFO, Chief Actuary, VP Actuarial, VP Finance, SVP Finance, Head of Medicare Finance, Medicare Segment CFO, VP Finance Government Programs, VP Financial Planning | VP, C-Level (Director only at parents <100k members) | Finance, Accounting, Management |
| **P3 `cc_ops`** | Contact Center, Member Services, Customer Service, Customer Care, Service Operations, Member Engagement, Operations Medicare | Director, VP, C-Level | Customer Service & Support, Operations |
| **P4 `economic_buyer`** | President Medicare, President Medicare Advantage, President Government Programs, Market President, COO Medicare, GM Government Programs | C-Level, VP | Management, Operations |

**Exclusions (hard):** Provider Quality, Hospital Quality, Clinical Quality (unless paired with Stars/Medicare/plan), Quality Assurance (IT/QA), Quality Engineer, standalone Pharmacy Quality, standalone Accreditation, Controller, Accounting, Audit, Tax, Investor Relations, Procurement, Revenue Cycle. Plus the house rubric excludes: IT/Security, Clinical, Legal/Compliance, Sales/Marketing/HR.

**Depth:** drop the `2–3 per persona` cap. Take **up to 10 per persona per parent**. The cap existed to ration Clay credits.

**Estimate:** 26 parents × 4 personas × ~10 = **~1,040 contacts. Budget 1,500 credits.**
**Batching:** one CSV. Well under the 25K ceiling.
**Capacity flag:** none. The motion processes this comfortably; Wave 1 is already staged.

---

## SPEC 2 — Back Office (Mandate 3)

**Source list:** `BackOffice_Target_Universe_v1.csv` — **all 101 accounts**, not Tier 1 only. The Tier-1-first rule was a credit-rationing decision; it no longer applies. Tier breakdown: T1 56, T2 35, T3 10.
**Verticals present:** Financial Services 25, Healthcare Payer 20, Healthcare Provider 18, Utilities 9, Insurance 9, Telco/Cable 8, Retail 3, Travel 3, BPO 2, Review 4.

**Add the six GATE-2 orgs here.** They are Tier-1 back-office anchors and warm.

**`customer_flag` is NOT an exclusion in this motion.** It is the qualifying condition. `fo_risk_flag` suppresses and `owner_cleared` gates the send, per `motion_overrides.back_office`. Neither blocks sourcing.

### Personas

| Persona | Job Title strings (bulk paste, OR) | Seniority | Job Function |
|---|---|---|---|
| **`bo_claims`** | VP Claims, Director Claims, Claims Operations, Claims Transformation, VP Appeals, Director Grievances, Utilization Management | Director, VP, C-Level | Operations, Healthcare Services |
| **`bo_shared`** | VP Payment Operations, Director Payment Ops, Disputes, Collections, Document Processing, Shared Services, Enrollment Operations, Underwriting Support, Revenue Cycle, VP Back Office | Director, VP, C-Level | Operations, Finance |
| **`coo_finance`** | Chief Operating Officer, SVP Operations, VP Operations, CFO, VP Finance | VP, C-Level | Management, Operations, Finance |

**Exclusions (hard):** IT/Security (CIO, CTO, VP IT — RPA owners are an objection source, not the buyer), Clinical (CMO, nursing), Legal/Compliance, Sales/Marketing/HR, **contact-center titles** (covered by the front-office relationship and by Spec 5), functions under ~50 FTEs.

**Provider caveat:** the 18 Healthcare Provider rows are Tier 2 precisely because several are clinical-side footprints. Provider back office = revenue cycle, coding, billing, scheduling. **Not clinical.** Confirm with the CSM before sourcing a heavily-clinical account.

**Depth:** raise from `4–5 per account` to **up to 20 per account** across the three personas.

**Estimate:** 101 accounts × ~20 = **~2,020 contacts. Budget 3,000 credits.**
**Batching:** one CSV.
**Capacity flag:** **Yes — soft.** Mandate 3 is 200+ contacts. This sources ~10x that. The overage is deliberate (free to source, free to re-enrich for a year) but the **owner-review gate does not scale**: `BackOffice_PersonaPull_Spec.md` requires AE/CSM review of the first 50 before the pull scales, and `owner_cleared` defaults FALSE. Sourcing 2,000 does not mean sending to 2,000. Land them, review in waves, send only what owners clear.

---

## SPEC 3 — WFM-Adjacency ★ PRIORITY

**There is no account list to source from. This spec builds one.** That is the point, and it is where the pool should go.

`WFM_Adjacency_Clone_Pack_v1.md` line 42 defines the universe as *"signal-first: Clay technographic search (Verint / NICE / Calabrio / Genesys / Amazon Connect) + RTA/intraday job postings. Overlaps Cost-Mandate accounts."* SI Discovery does both natively.

### Stage A — build the account universe (0 credits, company-level filtering is free to browse)

| Filter | Setting |
|---|---|
| **Technology Used** | Verint, NICE, NICE inContact, Calabrio, Genesys, Amazon Connect, Five9, Talkdesk, Aspect, Alvaria, Injixo, Assembled, Playvox — set Status = installed/current, Confidence Score = medium and above |
| **Industry** | Healthcare, Financial Services, Insurance, Retail, Telecom, Utilities (Intradiem's six verticals) |
| **Employee Range** | 1,000+ floor; run 5,000+ as the priority band first |
| **Location** | United States, Canada |
| **Company List → Exported Companies** | `False` |

Then **subtract the 101 accounts** in `Active_Customers_SF_Jul10.csv`. Per GATE-1, screen against the full CSV, not the JSON aliases.

**Optional second signal (adds precision, do this if Stage A returns more than ~3,000 companies):** layer **Job Postings** → Job Post Title contains `Workforce Management`, `WFM`, `Real Time Analyst`, `RTA`, `Capacity Planning`, `Intraday`, `Forecasting and Scheduling`; duration = last 90 days. A company hiring RTA/intraday right now is staffing around exactly the gap Intradiem closes. This is the sharpest fit signal available and it costs nothing to apply.

### Stage B — personas

| Persona | Job Title strings (bulk paste, OR) | Seniority | Job Function |
|---|---|---|---|
| **`wfm` (entry)** | Workforce Management, WFM, Capacity Planning, Intraday, Real-Time Analyst, Real Time Analytics, RTA, Resource Planning, Forecasting and Scheduling | Manager, Director, VP | Operations, Customer Service & Support |
| **`cc_ops`** | Contact Center, Customer Care, Customer Service Operations, Service Operations, Member Services | Director, VP, C-Level | Customer Service & Support, Operations |
| **`coo_finance`** | Chief Operating Officer, SVP Operations, VP Operations, CFO, VP Finance | VP, C-Level | Management, Operations, Finance |

Note `wfm` accepts **Manager** seniority (per `ref_ICP_Persona_Rubric.csv`, WFM is Manager+ while everything else is Director+). Do not raise the floor here; the WFM manager is the entry persona and the one who feels the pain daily.

**Estimate:** the elastic spec. Scale to the credits.

| Band | Companies | Contacts/co | Contacts | Credits |
|---|---|---|---|---|
| Conservative (5,000+ employees, tech-confirmed, hiring signal) | ~800 | 6 | ~4,800 | ~5,000 |
| **Recommended** (1,000+ employees, tech-confirmed) | ~2,500 | 8 | ~20,000 | ~20,000 |
| Aggressive (1,000+, tech OR job-posting signal) | ~6,000 | 10 | ~60,000 | ~60,000 |

**Recommended band: ~20,000 credits.** That's 11% of the pool for a universe the motion has never had.

**Batching:** 1 CSV at conservative, 1 at recommended, 3 at aggressive (25K ceiling).

### Capacity flag — RESOLVED. The reported blocker is stale.

The Jul 17 finding ("`fn_persona_key` has no `wfm` branch, node 2 exits every primary contact as `HOLD_persona`, the motion drafts nobody") **is no longer true.** Re-verified live 2026-08-06 by running `fn_persona_key` (`t_0tiahksb4jmyFfMSQYd`, 0 credits/run) via `clay routines runs start`:

| Job Title | Returns |
|---|---|
| Director of Workforce Management | `wfm` ✅ |
| VP Capacity Planning | `wfm` ✅ |
| Manager, Intraday Operations | `wfm` ✅ |
| Real-Time Analyst | `wfm` ✅ |
| WFM Analyst | `wfm` ✅ |
| Forecasting and Scheduling Manager | `wfm` ✅ |
| VP Contact Center Operations | `cc_ops` ✅ |
| Chief Operating Officer | `coo_finance` ✅ |

The `wfm` branch is live and correct. **No Clay UI fix is required before sourcing, and there is no ordering trap here.** `WFM_Adjacency_Clone_Pack_v1.md` PRE-REQ 0 should be marked resolved.

**Two title gaps remain** (both return `out_of_icp` when they should return `wfm`):

- `Resource Planning Manager` — "Resource Planning" is in the clone pack's intended pattern list but does not match
- `Senior Real Time Analytics Specialist` — the branch matches "Real-Time Analyst" and "RTA" but not "Real Time Analytics"

Neither blocks the motion (the six core WFM patterns route fine). Both are worth a one-line pattern add in the Clay UI whenever `fn_persona_key` is next open. Until then, **drop "Resource Planning" and "Real Time Analytics" from the Spec 3 Stage B title strings** so you don't source contacts that will exit at node 2.

**Functions remain non-editable outside the Clay UI.** Verified three ways on 2026-08-06: `clay functions` exposes `list` only; `clay routines update` accepts `--name`, `--description`, `--entity-type` (metadata, not logic); the MCP `read`/`edit_node` tools operate on workflows only and reject a function id with "Workflow not found." The CLI can list, read metadata, and *run* functions, which is enough to test them but not to change them.

---

## SPEC 4 — Cost-Mandate (bench pre-source)

**Cost-Mandate cannot pre-source an account universe.** The qualifying signal is a *public, in-window (≥ 2026-04-17), service-workforce cost mandate*. Accounts don't exist until the announcement lands. Currently one locked account (Acrisure) plus unverified candidates. Nothing to enumerate.

**But the personas are stable and the 12-month free re-enrich changes the math.** Pre-unlock the cost-owner layer at a broad bench of companies that *would* qualify if a mandate fires, so that when one does, contacts are already in hand and free to refresh. Today the motion loses days to sourcing after a signal fires — that is the whole latency problem.

| Filter | Setting |
|---|---|
| **Industry** | Healthcare, Financial Services, Insurance, Retail, Telecom, Utilities |
| **Employee Range** | 10,000+ (cost mandates are a large-employer event) |
| **Location** | United States, Canada |
| Subtract | the 101 customer accounts (GATE-1) and everything already pulled in Spec 3 (`Exported Contacts = False` handles this automatically) |

| Persona | Job Title strings | Seniority |
|---|---|---|
| **`cost_finance`** | CFO, VP Finance, SVP Finance, Chief Operating Officer, SVP Operations, VP Operations | VP, C-Level |
| **`cost_ops`** | Contact Center, Back Office, Shared Services, Service Delivery, Operations Transformation, Business Operations | Director, VP |

**Estimate:** **the overflow bucket.** Size it last, after Specs 1–3 land, against whatever remains. Roughly ~1,500 companies × 4 = ~6,000 contacts / ~6,000 credits at a sensible depth. Expand only if credits are genuinely going unused in the final week.

**Capacity flag:** **Yes — hard, and it caps this spec.** Cost-Mandate has **one** locked account. The motion cannot process a 6,000-contact bench; those contacts sit dormant until a signal fires against their employer. That is an acceptable use of expiring credits (the bench is free and stays refreshable for a year) but it is **storage, not pipeline**. Do not let this spec's volume read as motion progress in the Friday readout. It is optionality, and it should be counted and described as optionality.

---

## SPEC 5 — Install Base (front office) — SEPARATE TABLE

**Same 101 accounts as Spec 2. Different personas. Different destination. This is the one that can leak.**

Spec 2 targets the *back office* at customer accounts (expansion). Spec 5 targets the *front office* at those same accounts (expansion + risk). Same orgs, and the contacts are adjacent enough that a commingled table is a real hazard.

### Non-negotiable handling

1. **Separate CSV. Separate destination table. Never merged with Spec 1, 3, or 4 output.**
2. Every row carries `customer_exclude = TRUE`, `universe = install_base`, `source_motion = install_base`.
3. `customer_exclude` is stored as **text** `"TRUE"` while gate logic treats it as a **boolean**. Per CLAUDE.md this has already produced a live misfire. Before any wave that touches these rows, run the gate check **on real rows, not synthetic `--input`** — a synthetic pass can prove exclusion works while a real row slips a customer into a cold campaign.
4. These contacts are **never** eligible for Stars, WFM-Adjacency, or Cost-Mandate campaigns. Different motion, different sender, different message.

| Persona | Job Title strings | Seniority | Job Function |
|---|---|---|---|
| **`cc_ops`** | Contact Center, Customer Care, Member Services, Customer Service Operations, Service Operations | Director, VP, C-Level | Customer Service & Support, Operations |
| **`wfm`** | Workforce Management, WFM, Capacity Planning, Intraday, RTA, Resource Planning | Manager, Director, VP | Operations, Customer Service & Support |
| **`cx`** | VP Customer Experience, Member Experience, CSAT, Voice of the Customer | Director, VP, C-Level | Customer Service & Support, Marketing |

**Estimate:** 101 accounts × ~10 = **~1,010 contacts. Budget 1,200 credits.**
**Batching:** one CSV.
**Capacity flag:** none on volume. The flag is the gate, above.

---

## Budget roll-up

| Spec | Contacts | Credits | Priority |
|---|---|---|---|
| 3. WFM-Adjacency (recommended band) | ~20,000 | ~20,000 | **1** |
| 2. Back Office | ~2,020 | ~3,000 | 2 |
| 1. Star Ratings (26 cold-eligible) | ~1,040 | ~1,500 | 3 |
| 5. Install Base | ~1,010 | ~1,200 | 4 |
| 4. Cost-Mandate bench | ~6,000 | ~6,000 | 5 (overflow) |
| **Total** | **~30,000** | **~31,700** | |

**~31,700 of 183,318. ~152,000 credits will expire unused.**

That is the correct outcome, and it should be stated plainly in the Friday readout rather than hidden. The constraint was never credits. It's that Intradiem's defined ICP, screened honestly against the customer list, is roughly 30,000 contacts deep. Sourcing past that buys noise and costs Clay credits downstream on every junk row.

If there's appetite to use more, the only defensible expansions are:
1. Push Spec 3 to the **aggressive band** (~60,000 credits, +40,000). Real, if the motion can eventually work it.
2. Widen Spec 4's employee floor from 10,000+ to 5,000+.
3. Add the UK/Europe lanes (Jack's `uk_insurance_fs`, `uk_airlines`) — but those are blocked on contact data from Jack and are not Dallas's to source unilaterally.

Nothing else earns its place.

---

## Sequence

| When | What | Whose hands |
|---|---|---|
| **Now** | Refresh the SF Active Customers export from Nate (Jul 10 is stale) | Dallas |
| **Now** | Reconcile the 17 vs 13 `VERIFY` domain discrepancy in the Stars run config | Claude |
| **Now** | Decide where the master export lives (Supabase or restricted Drive — not the git repo, this is PII at volume) | Dallas |
| **Before export** | Rebuild the denylist screen against the 101-row CSV, not the JSON aliases (GATE-1) | Claude |
| **Wk of Aug 10** | Spec 3 Stage A: build and eyeball the WFM account universe before unlocking anyone | Dallas (SI UI) |
| **Wk of Aug 10** | Spec 3 Stage B export, then Specs 2, 1, 5 | Dallas (SI UI) |
| **Before volume** | Real-row test of node 1g on one of the 4 GATE-3 rows, confirm EXIT: EXCLUDED | Dallas (live run) |
| **Optional, low priority** | Add `Resource Planning` + `Real Time Analytics` patterns to `fn_persona_key` | Dallas (Clay UI) |
| **Wk of Aug 17** | Spec 4 bench, sized against what's left | Dallas (SI UI) |
| **Wk of Aug 24** | Buffer. Gaps and re-runs only. Nothing first-time. | Dallas |
| **After Aug 28** | Clay ingests in waves on the existing runbook | Claude |

**Ordering trap:** the only hard sequencing left is GATE-3. Do not load sourced volume into the Stars or Install-Base tables until node 1g is confirmed on a real row. Everything else can run in parallel, and the `fn_persona_key` pattern add is cosmetic, not blocking.

---

## Open items I could not resolve from the files

- **Exact SI credit-per-record behavior on a bulk export where some rows have no phone.** Docs say unlock is free on no-data but CSV export charges regardless. The `Has Direct Dial = True` filter should make this moot; confirm on a 50-row test export before running a 25K batch.
- **Whether the three credit pools (SI 183,318 / Data Workflows 15,225 / ABM 15,471) draw down independently.** 6sense's docs suggest SI and Workflows can share a pool; Dallas sees separate balances. Confirm at Settings → Credits before going wide.
- **The 17 vs 13 `VERIFY` domain count** between `StarRatings_PersonaPull_RunConfig_TierAB.csv` and `StarRatings_PersonaPull_Runbook.md`.
- **Whether the Jul 10 SF export is still current** — 27 days stale, and it gates every cold spec here.
