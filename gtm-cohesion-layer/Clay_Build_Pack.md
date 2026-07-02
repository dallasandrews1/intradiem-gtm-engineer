# Clay Build Pack — Day-1 Implementation Layer
**For Dallas Andrews · Intradiem GTM Engineer**
The click-by-click build below `GTM_Engine_Build_Spec.md`. The Spec is the *architecture*; this is the *build sheet*. Goal: on Day 1, with Clay access live, rebuild the whole engine from this pack in ~2 hours instead of designing in the UI.

> **Honest constraint:** No Clay pre-access until Jul 6. Nothing here is provisioned live yet. Treat the back-office ICP, scoring weights, and enrichment provider order as **hypotheses to confirm with Naveen + Scott Kemme before sourcing at volume.** Build the tables Day 1; do not turn on volume until deliverability is green and attribution is ratified.

---

## 0. Workspace layout (build in this order)
Three tables, two of them feed the third. Build top-down so dependencies resolve.

1. **`Accounts`** — the scored, signal-aware account layer.
2. **`Contacts`** — people, linked to Accounts, carrying the attribution tags.
3. **`Send Queue`** — approved-to-send rows only; the webhook source into Nate's sender + Salesforce.

Plus two **source/import tables** that feed Accounts: `CMS Star Ratings Import` and `Install-Base Import` (current customers from Salesforce). Keep imports separate from the live `Accounts` table so re-imports never clobber enrichment.

---

## 1. TABLE: `CMS Star Ratings Import` (source → Star Ratings motion)
Purpose: land the CMS file, filter to in-window, push qualifying rows into `Accounts`.

| # | Column | Type | Config |
|---|---|---|---|
| 1 | contract_id | Import | from CMS file |
| 2 | company_name | Import | parent org / plan name |
| 3 | qbp_avg_stars | Import | numeric |
| 4 | is_current_customer | Lookup | match company_name against Install-Base table → bool |
| 5 | in_window | Formula | `qbp_avg_stars < 4.0 AND is_current_customer == false` |
| 6 | **Write to `Accounts`** | Write-to-table | **Conditional run:** only if `in_window == true`. Map: company_name, qbp_avg_stars, motion="Star Ratings". |

> Build note: use a **conditional run** on the write column (only run when `in_window` is true) so you never spend credits enriching out-of-window plans.

---

## 2. TABLE: `Install-Base Import` (source → Back Office motion)
Purpose: current Intradiem customers from Salesforce → seed back-office account list.

| # | Column | Type | Config |
|---|---|---|---|
| 1 | account_id | Import | Salesforce account id (join key) |
| 2 | company_name | Import | — |
| 3 | is_current_customer | Constant | true (this table is install base by definition) |
| 4 | **Write to `Accounts`** | Write-to-table | Map: account_id, company_name, is_current_customer=true, motion="Back Office". |

---

## 3. TABLE: `Accounts` — build order
Columns must be created in this sequence; later columns reference earlier ones.

### 3a. Identity & base (imported/written in)
| # | Column | Type | Notes |
|---|---|---|---|
| 1 | account_id | Text (key) | join key to Salesforce/Contacts |
| 2 | company_name | Text | — |
| 3 | motion | Dropdown | `Star Ratings` / `Back Office` |
| 4 | is_current_customer | Checkbox | gates back-office play |
| 5 | qbp_avg_stars | Number | Star Ratings only |

### 3b. Enrichment waterfall — firmographic (run only if empty)
Add as **enrichment columns**, each set to **"only run if [target] is empty"** so each is a true fallback and you stop at first hit.

| # | Column | Provider/step | Fallback rule |
|---|---|---|---|
| 6 | domain | Enrich Company (provider A) | — |
| 7 | domain (fallback) | Enrich Company (provider B) | run only if col 6 empty |
| 8 | employee_count | from enrichment | — |
| 9 | revenue_band | from enrichment | — |
| 10 | vertical | AI column ("classify into: payer / health system / BPO / insurance / retail / telecom / utilities") | input = company + domain |

### 3c. Enrichment waterfall — technographic
| # | Column | Step | Fallback |
|---|---|---|---|
| 11 | tech_stack | Technographic provider | — |
| 12 | tech_stack (infer) | AI from job postings + site scrape | run only if col 11 empty |
| 13 | back_office_function_present | AI column → multi-select (`claims / enrollment / billing / payments / none`) | input = site + job postings; Back Office motion only (conditional run) |

### 3d. Formula columns — FIT score (confirm weights w/ Naveen)
Create one **Formula** column per motion, then a combined one. Weights mirror Spec §2.

`fit_star` (Formula, runs when motion = "Star Ratings"):
```
( qbp_avg_stars >= 3.85 && qbp_avg_stars < 4.0 ? 40 : qbp_avg_stars >= 3.70 ? 25 : 10 )
+ ( is_current_customer ? 0 : 15 )
+ ( tech_stack contains WFM/contact-center ? 20 : 0 )
+ ( director_plus_finance_or_stars_found ? 25 : 0 )
```

`fit_bo` (Formula, runs when motion = "Back Office"):
```
( is_current_customer ? 35 : 0 )
+ ( back_office_function_present != none ? 30 : 0 )
+ ( employee_count in band ? 20 : 0 )
+ ( wfm_ops_tooling_present ? 15 : 0 )
```

| # | Column | Type | Formula |
|---|---|---|---|
| 14 | fit_star | Formula | as above |
| 15 | fit_bo | Formula | as above |
| 16 | **fit_score** | Formula | `motion == "Star Ratings" ? fit_star : fit_bo` (0–100) |

### 3e. Signal columns (intent) — see §6 for the library
| # | Column | Type | Notes |
|---|---|---|---|
| 17 | intent_score | Formula | sum of fired signal point-columns (§6), cap 100 |
| 18 | top_signal | Formula/Text | freshest firing trigger label |
| 19 | **grade** | Formula | `fit>=70 && intent>=60 ? "A" : fit>=70 ? "B" : fit>=50 ? "C" : "D"` |

### 3f. Control columns
| # | Column | Type | Notes |
|---|---|---|---|
| 20 | last_refreshed | Date | set by enrichment/refresh run; drives decay control |
| 21 | push_contacts | Write-to-table → `Contacts` | **conditional:** only when `grade in (A,B,C)`. Triggers contact-find for that account. |

---

## 4. TABLE: `Contacts` — build order
Created from `Accounts` (col 21). Carries the attribution tags — **this is where the credit war is won or lost.**

### 4a. Find & enrich people
| # | Column | Type | Config |
|---|---|---|---|
| 1 | account_id | from source row | link to Accounts |
| 2 | company_name | from source | — |
| 3 | find_people | Enrichment ("Find people at company") | **Filter by title/seniority** to the ICP personas (§5). Limit N per account. |
| 4 | name, title, seniority, function | from find_people | — |
| 5 | persona_match | AI column → `Primary / Secondary / Out` | input = title + function, rubric = §5 |
| 6 | drop_out_of_icp | Formula/conditional | stop processing if persona_match == "Out" (saves credits) |

### 4b. Email waterfall (reject anything not deliverable)
| # | Column | Type | Fallback |
|---|---|---|---|
| 7 | email | Find/verify email (provider A) | — |
| 8 | email (fallback) | provider B | run only if col 7 empty |
| 9 | email (pattern) | pattern-match + verify | run only if col 8 empty |
| 10 | email_status | Verify | **reject row if != "valid"** (conditional gate before any send) |
| 11 | linkedin_url, location | enrichment | channel data |

### 4c. Attribution tags — set at creation, READ-ONLY after
> These three are the whole ballgame. Set them the instant the row is created, never let a downstream step overwrite them.

| # | Column | Type | Value |
|---|---|---|---|
| 12 | **gtm_engine_sourced** | Checkbox (Formula → true) | always true for engine-created rows |
| 13 | **source_motion** | Lookup from Accounts | `Star Ratings` / `Back Office` |
| 14 | **sourced_date** | Formula (now) | locked at creation |

### 4d. Outreach state (updated by the loop, not by Clay)
| # | Column | Type | Notes |
|---|---|---|---|
| 15 | sequence_status | Dropdown | none / queued / sent / bounced |
| 16 | reply_status | Dropdown | `none / reply / qualified reply / meeting` — **written back by the reply-sync agent**, this is the credit line |
| 17 | variant_id | Text | which message variant (experiment tracking) |
| 18 | **Write to `Send Queue`** | Write-to-table | **conditional:** only when `email_status==valid AND persona_match!=Out AND grade in (A,B,C)`. |

---

## 5. ICP FILTER (paste into the persona_match AI column rubric)
**Primary (senior ops/WFM tech officers):** VP/Director Operations · VP/Director Back Office / Shared Services · VP/Director Claims or Enrollment Operations · Head of Operational Excellence · VP/Director Workforce Management.
**Secondary:** COO org · VP Customer Care · Continuous Improvement / Automation leads · Finance-ops owners.
**Out:** contact-center-only titles with no back-office remit · IC-level roles.
> Confirm with Scott Kemme + 2–3 customer conversations before scaling. The back-office buyer is genuinely unknown — treat the first 50 contacts as ICP discovery, not volume.

---

## 6. SIGNAL LIBRARY — Clay column recipes (intent)
Each signal = one column that outputs its point value when it fires; `intent_score` (Accounts col 17) sums them.

**Tier 1 — fires outreach (writes a row into Send Queue via the signal path):**
| Signal | Clay build | Points |
|---|---|---|
| Oct CMS Star Ratings release | scheduled re-import of CMS file → re-run fit/grade | +40 |
| Stars language in SEC filings | HTTP API column → EDGAR full-text search ("Star Rating","quality bonus") → AI parse | +35 |
| Earnings-call Stars mention | HTTP/transcript source → AI keyword detect | +30 |

**Tier 2 — raise priority this week:**
| Signal | Clay build | Points |
|---|---|---|
| New quality/Stars leader | job-change monitoring (LinkedIn/news enrichment) | +25 |
| Quality hiring clusters | job-postings enrichment (count quality/ops roles) | +20 |
| Contract just under 4.0 | from CMS import formula | +20 |

**Tier 3 — context only (+5–10, lifts grade, no auto-fire):** general news / funding / M&A.

**Back-office signals (build alongside):** BPO/outsourcing announcements · claims-backlog or volume news · ops-leadership change · RPA/automation initiative · efficiency/layoff mandate in ops → fire back-office angle.

> Build Tier 1 first (highest leverage, scheduled). Add Tier 2 in Week 3. Tier 3 last.

---

## 7. WEBHOOKS / OUTPUTS (the connective tissue)
The `Send Queue` table is the single egress. Three webhook/HTTP columns:

1. **→ Approval Queue** (HTTP/webhook column): every Send-Queue row POSTs to the approval queue dashboard payload (`approval_queue.items[]` in `engine_state.json`). **Nothing sends from Clay directly.** Human approves first.
2. **→ Salesforce** (on approval): write `gtm_engine_sourced`, `source_motion`, `sourced_date` onto the Contact/Lead + Opportunity. These must exist in SF as fields — confirm Day 1 or flag as a build.
3. **→ Sender** (Nate's setup, on approval only): hand off approved copy + verified email + variant_id.

**Reverse webhook (into Clay):** reply-sync agent writes `reply_status` back onto the Contact row. That's what lights up the funnel.

---

## 8. CREDIT & DECAY CONTROLS (don't burn 5,000 credits in week 1)
- Every enrichment column set to **"only run if empty"** → no double-spend.
- **Conditional runs** on all write-to-table and people-find columns → never enrich out-of-window / out-of-ICP rows.
- `last_refreshed` + a scheduled refresh that only re-runs rows older than 30 days → freshness without waste.
- **Never source faster than you can keep warm.** Pace contact creation to deliverability capacity (§ deliverability monitor). 200 back-office contacts paced to real BOO GA, not dumped.

---

## 9. DAY-1 BUILD CHECKLIST (in order)
1. [ ] Confirm SF attribution fields exist: `gtm_engine_sourced`, `source_motion`, `sourced_date`. If not → flag as build to Naveen.
2. [ ] Build `Install-Base Import` + `CMS Star Ratings Import`; load the 38 + 157.
3. [ ] Build `Accounts` cols 1–16 (identity → fit). Run on a 10-row test slice first.
4. [ ] Add signal cols 17–19; verify intent/grade compute.
5. [ ] Build `Contacts` 1–14; **verify attribution tags lock and don't overwrite.**
6. [ ] Build `Send Queue` + the three webhooks; point #1 at the approval queue, leave #3 (sender) OFF until deliverability green.
7. [ ] Ratify scoring weights + ICP + baseline with Naveen/Scott BEFORE removing the test-slice limit.
8. [ ] Turn on Tier-1 signals (scheduled). Hold Tier 2/3.
9. [ ] First real run: 3 variants × segment, small, human-approved. Watch deliverability.

> Order is the point: **measurement before volume, ICP before sourcing.** Build the rails, prove on a slice, then scale.
