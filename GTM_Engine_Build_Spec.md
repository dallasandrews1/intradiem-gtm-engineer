# GTM Engine — Build Spec (Day-1 Ready)
**For Dallas Andrews · Intradiem GTM Engineer**
The implementable blueprint behind Section 05's Golden List. Built pre-start so the architecture is done before access. Implement in Clay + Salesforce on day one. Treat the back-office ICP and any scoring weights as **hypotheses to confirm with Naveen + Scott Kemme** before sourcing at volume.

---

## 1. GOLDEN LIST — data model (the live account intelligence layer)
Not a spreadsheet. A scored, enriched, signal-aware table that every campaign, sequence, and agent reads from. Two linked objects: **Accounts** and **Contacts**.

### Account record — fields
| Field | Type | Source | Purpose |
|---|---|---|---|
| account_id | key | CRM | join key |
| company_name | text | base | — |
| motion | enum (Star Ratings / Back Office) | logic | which play owns it |
| vertical | enum | enrich | payer / health system / BPO / insurance / etc. |
| employee_count, revenue_band | num | firmographic | size/fit |
| is_current_customer | bool | CRM | gates the back-office (install-base) play |
| back_office_function_present | multi | technographic/research | claims, enrollment, billing, payments |
| qbp_avg_stars (Star Ratings only) | num | CMS | <4.0 = in-window |
| tech_stack | multi | technographic | WFM/ACD/contact-center platforms |
| fit_score | 0–100 | computed | §2 |
| intent_score | 0–100 | computed | §3 |
| grade | A/B/C/D | computed | fit × intent tier |
| top_signal | text | signal engine | freshest firing trigger |
| last_refreshed | date | system | freshness/decay control |

### Contact record — fields
| Field | Type | Source | Purpose |
|---|---|---|---|
| contact_id | key | CRM | — |
| account_id | fk | — | link |
| name, title, seniority, function | text/enum | enrich | persona match |
| persona_match | enum (Primary / Secondary / Out) | logic | §4 ICP |
| email, email_status | text/enum | waterfall | deliverable? |
| linkedin_url, location | text | enrich | channel |
| **gtm_engine_sourced** | bool | **set at creation, read-only** | attribution |
| **source_motion** | enum | set at creation | attribution |
| **sourced_date** | date | set at creation | attribution |
| sequence_status | enum | Clay/CRM | where in outreach |
| reply_status | enum (none / reply / qualified reply / meeting) | logic | the credit line |

---

## 2. ACCOUNT SCORING (fit) — starter model (confirm weights w/ Naveen)
`fit_score = Σ(weighted attributes)`, 0–100.

**Star Ratings motion:**
- QBP avg 3.85–3.99 (closest to cliff) = 40 · 3.70–3.84 = 25 · <3.70 = 10
- Non-customer = 15 (customers excluded from new-logo motion)
- Contact-center / WFM tech present = 20
- Director+ in Finance/Stars/Medicare identified = 25

**Back-office motion:**
- Is current customer (install-base) = 35 (this is the stated wedge)
- Back-office function present (claims/enrollment/billing/payments) = 30
- Employee/transaction scale in band = 20
- WFM/ops tooling present = 15

**Grade:** A = fit ≥70 & intent ≥60 · B = fit ≥70 & intent <60 · C = fit 50–69 · D = <50. Reps work A→B→C; D parks until a signal fires.

---

## 3. SIGNAL LIBRARY — Clay-ready triggers (operationalized from Section 06)
Each signal: source, fire logic, action, and the score it adds. Tiers from the site.

**Tier 1 — act immediately (fires outreach):**
| Signal | Source / how to detect | Action | intent pts |
|---|---|---|---|
| October CMS Star Ratings release | CMS data pull / scheduled scrape | refresh stars, re-rank, trigger sequence to in-window accounts | +40 |
| Stars language in SEC filings | EDGAR full-text search ("Star Rating", "quality bonus") | trigger Finance-persona sequence | +35 |
| Earnings-call Stars mention | transcript monitoring | refresh angle, trigger sequence | +30 |

**Tier 2 — prioritize this week:**
| Signal | Source | Action | intent pts |
|---|---|---|---|
| New quality/Stars leadership | LinkedIn/news job-change monitoring | trigger "new leader" angle | +25 |
| Quality hiring clusters | job-board / Apollo job postings | raise priority, queue sequence | +20 |
| Contract just under 4.0 | CMS | confirm in-window, sequence | +20 |

**Tier 3 — supporting context (raises priority, no auto-fire):** general news, funding, M&A chatter → +5–10, lifts grade only.

**Back-office signals (build alongside):** BPO/outsourcing announcements, claims-backlog or call-volume news, operations-leadership changes, RPA/automation initiatives, layoffs/efficiency mandates in ops → fire the back-office angle.

---

## 4. BACK-OFFICE ICP — HYPOTHESIS (confirm with Scott Kemme before sourcing)
The site flags the buyer is genuinely unknown (front-office customers couldn't supply back-office leads). Starting hypothesis to pressure-test, **not** a finalized ICP:

**Account:** current Intradiem customers with sizeable back-office operations — claims processing, enrollment, billing/payment ops — in payer, health-system, insurance, and BPO verticals.

**Primary persona (senior ops/WFM tech officers, per the site):** VP/Director of Operations · VP/Director Back Office / Shared Services · VP/Director Claims or Enrollment Operations · Head of Operational Excellence · VP/Director Workforce Management.

**Secondary persona:** COO org, VP Customer Care (cross-over), Continuous Improvement / Automation leads, Finance ops owners.

**Out of ICP:** pure front-office/contact-center-only titles with no back-office remit; IC-level roles.

**Pain hypotheses to validate:** manual back-office work, backlog/SLA pressure, idle/shrinkage in non-phone work, no real-time orchestration off the phones, efficiency mandates. **Validate each with Scott Kemme + 2–3 customer conversations before scaling sourcing.**

---

## 5. ENRICHMENT WATERFALL (AI Enrich capability)
Ordered fallback across sources so coverage is maximized and cost controlled. Stop at first verified hit per field.
1. **Firmographic** (size, revenue, vertical): CRM → primary provider → secondary → web.
2. **Contact + email** (verified, deliverable): provider A → provider B → pattern-match + verification. Reject `email_status != valid`.
3. **Technographic** (WFM/ACD/contact-center stack): technographic provider → job-posting inference → site scrape.
4. **Intent/signals** (§3): CMS/EDGAR/transcripts/job boards/news.
**Rule:** every record carries `last_refreshed`; re-enrich on a cadence so the list "updates as the market moves." Never source faster than you can keep warm (decay control).

---

## 6. ATTRIBUTION + INSTRUMENTATION SCHEMA (the rails)
**Salesforce source-of-truth fields** (write at record creation, read-only after, on every opportunity):
- `gtm_engine_sourced` (Y/N) · `source_motion` (Star Ratings / Back Office) · `sourced_date`.

**Credit rule:** engine owns *sourcing* credit, locked at the source tag regardless of who works the reply; reps own *conversion* credit from the reply forward. Both true at once.

**Dashboard funnel (split by motion, all from tagged records):**
`contacts enriched → messages sent → deliverability/open rate → replies → qualified replies → meetings booked & confirmed.`

**Metric definitions to ratify with Naveen:**
- *Vetted meeting:* engine-sourced + persona match + target account + booked-and-confirmed (not "held").
- *10× throughput:* 10× the written 1× baseline, measured as **qualified replies/week**, gated by deliverability floor (open ≥ baseline, spam < threshold).
- *Qualified back-office contact:* ICP match + in install base + verified email + source-tagged. 200 of these.
- *Engine build (Goal 4):* deliverables shipped + kept live + documented repeatable motion — judged on "is it repeatable and running," not tool count.

**Guardrail (their words):** AI enriches, people judge, human approval before anything sends.

---

## 7. AUTOMATE — agent roadmap (build after the list + sequences work)
Order matters; don't automate an unproven motion.
1. **Enrichment/refresh agent** — keeps the Golden List current on a cadence.
2. **Signal-watch agent** — monitors §3 sources, fires triggers, updates `top_signal`/intent.
3. **Follow-up agent** (the pilot's Wk5–6 deliverable) — works no-reply contacts with human-approved variants.
4. **List-build agent** — expands the back-office list against the confirmed ICP.
