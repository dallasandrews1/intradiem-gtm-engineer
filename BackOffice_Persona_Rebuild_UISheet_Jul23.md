# Back Office Motion — Persona Rebuild UI Sheet (Jul 23, post-Mary Ann)

---
## LIVE BUILD STATE + RESUME POINT (Cowork session, Jul 23 — stopped on Claude Enterprise usage cap, NOT Clay credits)

The Cowork/Chrome build got most of the way there before the Enterprise Claude account hit its monthly spend limit. Clay is untouched and everything below is SAVED in the live workbook. Resume from personal Cowork.

**Already built + saved in Clay:**
- **Account table (`t_0ti4pe0sGJBQb5QASzG`, 15 rows):** all four persona title columns populated across all 15 rows — `ops_leader_titles` (row-typed: payers/insurance rows 1-6,12,13 = claims string w/ the Update 2 additions; FS/BPO rows 7-11,14,15 = payment string), `bo_product_owner_titles` (WFM/WFO cluster string), `bo_claims_it_titles` (expanded claims-tech string), `exec_coo_titles` (COO string). `wfm_status` column added + left blank. Legacy `primary_/coo_` columns and the prior-pull contacts table left untouched. **Auto-run was turned OFF (table now Manual)** to prevent accidental spend — re-enable at will.
- **Seed table `Existing_BO_Campaign_Seed`:** 214 rows imported from `report1784825852835.csv` (First/Last/Company/Title/Email/Account Owner mapped), `persona = ops_leader` on all 214 via a constant formula.
- **Saved searches:** `BackOffice 4-Persona Director+ (15 accts)` (original combined, 19 filters — superseded) and `BO P1 ops_leader (Dir+, cap2, dedup seed)` (persona-1 template: titles Claims Operations/Payment Operations/Shared Services, Director+ gate, seed exclusion, cap 2 — needs cap raised to 4).

**Two real blockers found (both diagnosed, evidence-backed):**
1. **No company domains → free preview can't run.** The 15 accounts are company NAMES only; Clay's people search errors *"Invalid companies provided: please make sure you are using LinkedIn URLs or Company Domains."* **Fix (Dallas APPROVED): Company Domain waterfall enrich on the 15 accounts (~0.8 cr/row ≈ ~12 credits).** This was literally being configured (mapping Company Name → account_name) when usage ran out. **← EXACT RESUME POINT.**
2. **Native in-search dedup matches on LinkedIn URL, not email.** Seed has emails only, so "Exclude people" shows 0. True email-dedup runs as a **post-import lookup against the seed's email column** before the waterfall. Same result, correct mechanism.

**Locked final spec (optimize for best stakeholder list, not min spend):** four per-persona searches, all Director+ (C-suite/VP/Director/Head), deduped vs seed on email (post-import). Caps/account: ops_leader **4**, bo_product_owner **6**, bo_claims_it **6**, exec_coo **3** (~285 max finds). On deduped survivors: Work Email waterfall → email verification (ZeroBounce/Clay validator) + status column → LinkedIn URL + standardized title/seniority → `account_owner` carried by company → `persona` label. Output = one clean contacts table grouped by account, sorted persona then seniority. Free preview all four FIRST, report per-persona counts + combined estimate, then HARD STOP for go before the import/enrichment charge. Full-run estimate ~660-900 credits (~1% against the 63,242.6 live balance pulled Jul 23; always re-pull `clay credits` at run time, never cite a remembered figure).

**Resume order (personal Cowork):** reopen workbook → account table → finish + RUN the Company Domain waterfall (~12 cr, approved) → confirm domains resolved → raise P1 cap to 4, stamp P2-P4 from the template → free preview all four → report counts + estimate → STOP for go.

---

**Workbook:** Back Office Motion (`wb_0ti4jh8ATmjiCowc7JM`, workspace 1180800)
**Account input table:** BackOffice_Sample50_Accounts (`t_0ti4pe0sGJBQb5QASzG`, 15 Tier-1 parent accounts)
**Why we're rebuilding:** Mary Ann's verdict on the first ~111-contact pull — *"right operations people, not the right people making the decisions on the tools."* We're moving from one claims-ops layer to a 4-persona buying committee with a hard Director+ gate.

> Do this AFTER folding in Savannah's maintained back-office list, the Jean Marie / Rich Cigna reference titles, and Cheryl's marketing titles doc. Pull a SMALL corrected sample first, not the full universe. Don't burn credits re-sourcing until Mary Ann has smoke-checked the new criteria.

---

## Step 0 — reconcile the first pull (before spending again)
1. Open the People/contacts table that produced the ~111 rows. Confirm how many credits that pull spent, and log it in `clay_credit_ledger.csv` under the back-office motion.
2. Do NOT delete it yet. Keep it as the "operations layer" reference — Mary Ann said ops is still valuable to market to, just not the decision seat. Tag these rows `persona = ops_leader` so they survive the rebuild.

## Step 1 — add the persona dimension (4 layers, not 1)
On the account input table (`t_0ti4pe0sGJBQb5QASzG`), the current columns are `primary_persona` + `primary_titles` and `coo_persona` + `coo_titles`. Expand to four persona/title pairs. Triple-click a fresh column header to rename (single/double-click is unreliable in Clay).

| Persona key | Who | Sourcing role |
|---|---|---|
| `ops_leader` | Claims / back-office operations leaders | Market to, not the tool buyer |
| `bo_product_owner` | Owner the tool sits under (separate from WFM owner) | Post-purchase champion |
| `bo_claims_it` | Claims-technology / claims-IT decision maker | The IT decision on the tool |
| `exec_coo` | COO / SVP Operations | Marketing top-of-funnel |

## Step 2 — title strings per persona (paste into each People search)

**ops_leader** — payers/insurance:
```
"VP Claims" OR "Director Claims" OR "Claims Operations" OR "VP Appeals" OR "Director Grievances" OR "Utilization Management" OR "Director Fraud" OR "VP Fraud"
```
**ops_leader** — financial services / BPO:
```
"VP Payment Operations" OR "Director Payment Ops" OR "Disputes" OR "Collections" OR "Document Processing" OR "Shared Services" OR "Enrollment Operations" OR "Revenue Cycle" OR "VP Back Office" OR "Director Back Office"
```
**bo_product_owner / workforce** (all verticals) — WIDENED from Savannah's list; this is the WFM/WFO cluster our tool sits under:
```
"Workforce Management" OR "Workforce Planning" OR "Workforce Engagement" OR "Workforce Effectiveness" OR "WFM" OR "WFO" OR "Real-Time Operations" OR "Real Time Operations" OR "Back Office Workforce" OR "Product Owner" OR "Middle Office Product"
```
**bo_claims_it** (Mary Ann's emphasis — claims-technology, distinct from generic IT) — EXPANDED from real titles in Savannah's list:
```
"Claims Technology" OR "Claims IT" OR "Claims Systems" OR "Claims Applications" OR "Provider Technology" OR "Workforce Engagement Engineering" OR "Application Services" OR "IT - Claims" OR "Head of IT" OR "Business Systems" OR "Operations Technology" OR "Health Plan Technology"
```
**exec_coo** (all verticals):
```
"Chief Operating Officer" OR "SVP Operations" OR "EVP Operations" OR "Head of Operations"
```

> Cross-check every string against Savannah's maintained list and Cheryl's doc before running. Add any real titles they use that aren't here (e.g. Rich = "Director, Workforce Engagement Engineering" — already folded into bo_claims_it).

## Step 3 — the hard gate: Director and above
Add a `seniority_gate` filter on the People search:
- Keep only **Director, Senior Director, VP, SVP, EVP, C-level**.
- Exclude Manager, Analyst, Specialist, Coordinator, Lead, Associate.
- Mary Ann was explicit: manager/IT-level below director = do not source.

## Step 4 — tag the account segment (changes who we target)
Add `wfm_status` on the account table, values `wfm_deployed` / `no_wfm`:
- `wfm_deployed`: source all four personas (they have a WFM product owner + separate back-office product/IT).
- `no_wfm`: source `ops_leader` + `bo_claims_it` + `exec_coo` only. No back-office product owner exists yet — skip `bo_product_owner`.
- Seed from Savannah's list / AM knowledge; leave blank = treat as `wfm_deployed` default until confirmed.

## Step 5 — pull the first list across the 15 Tier-1 accounts
Scope decision (Jul 23): first list = the **15 Tier-1 accounts**, not Cigna-only and not the full 101 yet. Highest-fit slice, cleanest list for the AMs, credit-disciplined. Expand to the full install base only after the AMs nod.
1. Run the four persona searches across all 15 Tier-1 accounts, Director+ gate on, deduped against Savannah's 214 seed table.
2. Caps per persona per account kept modest so the list stays targeted (Mary Ann liked "targeted, not 600 people").
3. Waterfall email enrich only the deduped survivors.
4. The criteria are already validated free against Savannah's list — no separate paid validation run needed. The only reason to stage is credit-cost measurement, which the Cowork hard-stop estimate covers.

## Step 6 — this enriched list IS the deliverable
Export the enriched 15-account list and send it with the follow-up email (draft: `BackOffice_Followup_Email_Group_Jul23.md`) for the AMs to smoke-check, routed by Account Owner (see calibration section). The optional Cigna one-pager (`BackOffice_Cigna_Calibration_Jul23.html`) is a pre-read only, since Mary Ann asked about Cigna by name — it is NOT the deliverable. Only after the nod do you widen to the full 101-account universe.

---

---

## Calibration against Savannah's maintained list (214 contacts, "Cust Sales - Back Office Contacts")
- Her list is **73% claims (157/214), 66% Director+**. It is the operations layer, senior on ops, thin on product-owner / claims-IT / exec. That thinness is where Clay adds value.
- **Director+ gate drops ~72 of her rows** (managers, supervisors, analysts, adjusters). The new pull will be leaner and more senior by design.
- **AM clearance routing (Account Owner column):** Inger Escamilla 70, Omar Velasquez 52, Alex Bauer 36, Mary Ann Chandler 35, Andy Giemza 11, Rachel DiBello 7. Route each account's smoke-check to its owner, not just Mary Ann.
- **Cigna proof (send this to Mary Ann):** her 5 Cigna contacts under the rebuilt criteria — Brianna Shea (STD Claims Manager) and Sandy Brick (Divisional Manager) dropped by the Director+ gate; Melissa Foy (Global Director, Claims Services) → ops_leader; **Rich Turner (Director, Workforce Engagement Engineering) → bo_claims_it**; **Jeanmarie Morrison (Sr Director Back Office Workforce Planning) → bo_product_owner**. The two people Mary Ann named by seat are caught by the two new personas.
- **Seed move:** import her 214 as the `ops_leader` seed + dedup source so the Cigna pull doesn't re-source people she already has, and so her real WFM/IT names anchor the new personas per account.

### Guardrails
- Warm relationships, so no cold MessageGen here — messaging is Sierra/marketing-led. Don't wire outreach AI columns into this table for send.
- Credit discipline: Cigna-only sample is the smallest spend that proves the new criteria. Log every run in the ledger.
- Clay does no phone numbers — flag ZoomInfo as the separate source if numbers are needed.
