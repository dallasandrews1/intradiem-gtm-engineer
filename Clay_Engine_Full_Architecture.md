# Clay Engine — Full Table Architecture
**Dallas Andrews · Intradiem GTM Engineer · the complete multi-layer build**

This is the exhaustive table map that sits around the core in `gtm-cohesion-layer/Clay_Build_Pack.md`. The Build Pack details the click-by-click for the five core tables. This document is the whole architecture: every table, what feeds it, what it writes to, and the automations that make it self-update. Build the core five first, then add the outer layers.

---

## 0. Operating model (answer to "CSV every time, or the MCP?")

Neither is your primary way of working at Intradiem. Both are supporting.

**Native Clay tables are the engine.** The living, auto-updating motion (tables writing into tables, conditional runs, scheduled refreshes) exists only as native Clay tables built in the UI. This is where you work day to day.

**The MCP-in-Claude is a complement,** for ad-hoc research, one-off pulls, and letting me feed data into your dashboards and briefs. It does find/enrich/read. It does not build or run the layered architecture. Use it to answer a question fast, not to run the motion.

**CSV import is a one-time bridge,** to seed a native table from an external file (the workbook, a list I pulled). After the seed, the native table owns the data and keeps it fresh. You do not re-export CSVs as a way of working; that produces snapshots that die when the market moves, which is the exact thing your engine exists to beat.

So: build the tables once, wire them, let them run. The CSV and the MCP are how data gets in and how you poke at it, not how it operates.

---

## 1. The layer map

```
L0  SOURCES            CMS Import · Install-Base Import · Signal Feeds
        │  (write-to-table, conditional on in-window)
        ▼
L1  ACCOUNTS           Accounts Master  ◄──────────┐
        │  (grade A/B/C → push)                    │ (write-back: intent, top_signal)
        ▼                                          │
L3  CONTACTS           Buying Committee     ◄── L2  SIGNALS (Stars · Back Office)
        │  (persona + valid email)
        ▼
L4  MESSAGING          Message Gen ◄── Reference: Verified Metrics · Product-Angle Map · ICP Rubric · Variant Library
        │
        ▼
L5  QA / APPROVAL       Send Queue (critic gate + human approval)
        │  (approved only)                 ▲ (gate)
        ▼                                  │
L6  DELIVERY           Outreach Sync ──── Deliverability / Domain Health
        │  (webhook → sequencer + Salesforce source-tags)
        ▼
L7  CLOSED LOOP        Reply & Meeting Sync → Attribution / Funnel  → dashboards
        │
        ▼
L8  REP HANDOFF        AE Territory/Assignment → AE Worklist (per rep)
```

Every arrow is a Clay **Write-to-table** or **Lookup** column. Depth is real: Sources → Accounts → Contacts → Message → Approval → Sync → Reply → Attribution → Worklist is eight hops.

---

## 2. Exhaustive table catalog

Each table: purpose · feeds from · writes to · key columns · run trigger. Tables already detailed click-by-click in the Build Pack are marked **[BP]**.

### L0 — Sources

**T0.1 · CMS Star Ratings Import** **[BP]**
Land the CMS file, filter to in-window, push qualifying rows into Accounts. Feeds from: CSV/scheduled CMS pull. Writes to: Accounts (conditional: `qbp_avg_stars < 4.0 AND not current customer`). Trigger: manual on load + scheduled re-import at each October CMS release.

**T0.2 · Install-Base Import** **[BP]**
Current Intradiem customers from Salesforce → back-office account seed. Feeds from: Salesforce accounts. Writes to: Accounts (`is_current_customer = true, motion = Back Office`). Trigger: scheduled Salesforce sync.

**T0.3 · Signal Feeds (raw landing)**
Optional raw landing for scheduled scrapes (EDGAR full-text, earnings transcripts, job postings, news) before they are matched to accounts. Feeds from: HTTP/API columns. Writes to: L2 Signals tables (matched by company). Trigger: scheduled (daily/weekly). Skip if you build signals as columns directly on the Signals tables.

### L1 — Account intelligence

**T1.1 · Accounts (Master)** **[BP]**
The Golden List hub. Scored, enriched, graded, signal-aware. Feeds from: T0.1, T0.2, and write-back from L2. Writes to: Contacts (conditional on grade A/B/C). Key columns: identity (account_id, company, motion, is_current_customer, qbp_avg_stars), firmographic + technographic waterfall (domain, employee_count, revenue_band, vertical, tech_stack, back_office_function_present), `fit_score`, `intent_score`, `grade`, `top_signal`, `last_refreshed`. Trigger: enrichment on new rows (only-run-if-empty); scheduled refresh of rows older than 30 days.

### L2 — Signals (write back into Accounts)

**T2.1 · Account Signals — Star Ratings**
Per-account intent monitoring for the new-logo motion. Feeds from: Accounts (account list) + T0.3 / live API columns (EDGAR "Star Rating"/"quality bonus", earnings-call mentions, CMS release, new quality/Stars leadership, quality hiring clusters). Writes to: Accounts (`intent_score`, `top_signal`, freshness). Key columns: one point-valued column per signal (Tier 1 fires outreach, Tier 2 raises priority), `signal_fired_date`. Trigger: scheduled; Tier-1 signals can also fire a row straight into Send Queue via the signal path.

**T2.2 · Account Signals — Back Office**
Same pattern, back-office triggers: BPO/outsourcing announcements, claims-backlog or volume news, ops-leadership change, RPA/automation initiative, efficiency/layoff mandate. Feeds from: install-base Accounts. Writes to: Accounts. Trigger: scheduled.

### L3 — Contacts

**T3.1 · Contacts (Buying Committee)** **[BP]**
People, linked to Accounts, carrying the attribution tags. Feeds from: Accounts (grade A/B/C push). Writes to: Message Gen and Send Queue (conditional: valid email + persona match + grade). Key columns: find-people (ICP-filtered), persona_match (Primary/Secondary/Out), email waterfall + email_status (reject if not valid), **gtm_engine_sourced / source_motion / sourced_date (set at creation, read-only)**, sequence_status, reply_status, variant_id. Trigger: created by Accounts push; email waterfall only-run-if-empty. Use the locked ICP filter (Reference T-R3).

### L4 — Messaging

**T4.1 · Message Generation**
Per contact, generate personalized variant copy. Feeds from: Contacts + account why-now (top_signal, forgone QBP) + product angle. Writes to: Contacts (draft, variant_id) and Send Queue. Key columns: AI/Claygent copy columns per variant, tone/persona rubric, `variant_id`. Reads reference tables so claims stay approved. Trigger: on new eligible contact.

**T-R1 · Verified Metrics / Claims Library (reference)**
Approved stats the AI copy may cite (enforces citation discipline). Feeds from: manual/maintained. Read-only lookup for T4.1. This is the guardrail against unapproved numbers reaching a payer.

**T-R2 · Product-Angle Map (reference)**
Title/function → Queue Optimizer vs Back Office Optimizer vs both. Read-only lookup used by T4.1 to pick the angle. (Contact center/customer care → QO; claims/appeals/UM → BOO; COO/core ops → both.)

**T-R3 · ICP Filter / Persona Rubric (reference)**
The locked people-find config (proven Jun 30): include contact center, member services, customer care, workforce management, care/claims operations, member experience, service operations; exclude IT, cyber, network, infrastructure, clinical, pharmacy, sales, provider data, legal, comms, procurement, engineer. Used by T3.1's find-people and persona_match.

**T-R4 · Message Variant Library (reference)**
The starter variants per segment (3+ per motion). Source for experiment tracking; `variant_id` links back for win-rate analysis.

### L5 — QA / approval gate

**T5.1 · Send Queue (critic gate + human approval)** **[BP, expanded]**
The single egress. Nothing sends from Clay directly. Feeds from: Contacts + Message Gen. Writes to: Outreach Sync (approved rows only). Key columns: critic checks (email_status valid, in-scope motion per WIP, claims-verified regex, length), `critic_status` (pass/held + reasons), `approval_status` (pending/approved/rejected, human-set), `released_by`. Trigger: conditional write from Contacts; human approves before egress.

### L6 — Delivery / sync

**T6.1 · Outreach Sync (egress webhooks)** **[BP]**
Hands approved copy + verified email to the sequencer and writes source-tags to Salesforce. Feeds from: Send Queue (approved). Writes to: external sequencer + Salesforce (`gtm_engine_sourced`, `source_motion`, `sourced_date` on Lead/Contact + Opportunity). Trigger: on approval. Sender webhook stays OFF until deliverability is green.

**T6.2 · Deliverability / Domain Health (monitor + gate)**
Warmup status, inbox rotation, spam/blacklist, bounce rate. Feeds from: sender/monitoring API. Gates T6.1 (send blocked unless green). Trigger: scheduled. This is the P1 that stops spray-and-burn.

### L7 — Closed loop / reporting

**T7.1 · Reply & Meeting Sync (reverse webhook)**
Writes `reply_status` (none/reply/qualified reply/meeting) back onto Contacts. Feeds from: sequencer/CRM reply data. Writes to: Contacts (the credit line) + Attribution. Trigger: scheduled/reverse-webhook.

**T7.2 · Attribution / Funnel Reporting**
Reads tagged records, computes the two-motion funnel (enriched → sent → open → replies → qualified replies → meetings) and engine-sourced credit at the qualified-reply line. Feeds from: Contacts (tagged) + Reply Sync. Writes to: dashboards (command-center, attribution board). Trigger: scheduled.

### L8 — Rep / AE handoff

**T8.1 · AE Territory / Assignment**
Maps accounts to owner (AE/BDR) so contacts route to the right rep. Feeds from: Accounts + a territory rules table. Writes to: Contacts (owner) and AE Worklist. Trigger: on account create/update.

**T8.2 · AE Worklist (per-rep view)**
The daily "who to work today" for each rep: A/B graded, signal-fresh accounts + their committee, with the why-now line and the suggested product angle, filtered to that rep's territory. Feeds from: Contacts + Accounts + Assignment. This is what a rep opens each morning; it is the human-facing end of the engine. Trigger: live view / scheduled refresh.

---

## 3. How tables "point to" other tables (the wiring mechanics)

Three Clay column types do all the connective work. This is the "three-plus layers deep" you described.

**Send Table Data** (formerly "Write to Other Table") — found under the table's **Actions** menu, NOT the Add Column list. It sends rows from one table into another (create/append). Use "Send row" to pass each row, or "Flatten Lists" to split a list (e.g., people found at a company) into one row each. Filter the source view first to control which rows go (e.g., only Grade A). Clay sends linearly (A→B→C, no loops back), so any write-back to source data goes through the CRM/webhook, not a Clay table pointing at itself. This is the forward flow.

**Lookup** — a column that reads a value from another table by a join key (e.g., Contacts looks up `source_motion` from Accounts; Message Gen looks up an approved stat from the Verified Metrics table). This is how reference tables and write-backs work.

**Conditional run + only-run-if-empty** — gates every enrichment so you never spend credits on out-of-window, out-of-ICP, or already-filled rows. This is what makes the engine cheap enough to run continuously.

Chain them and you get depth: `Accounts → (write, if grade≥C) → Contacts → (write, if email valid) → Send Queue → (write, if approved) → Outreach Sync → (reverse webhook) → Contacts.reply_status → (lookup) → Attribution`.

---

## 4. Automations (what makes it self-update)

These are scheduled runs on the tables above, not new tables. Build after the list and sequences work.

1. **Enrichment / refresh agent** — re-runs stale Accounts rows (`last_refreshed` > 30 days) on a schedule. Keeps the list current.
2. **Signal-watch agent** — scheduled runs of the L2 Signals tables; fires Tier-1 triggers.
3. **Follow-up agent** — works no-reply Contacts with human-approved variants (the pilot's Week 5-6 deliverable).
4. **List-build agent** — expands the back-office list against the confirmed ICP once it is validated with Scott Kemme.

---

## 5. Build order (do not skip)

1. Core five **[BP]**: CMS Import + Install-Base Import → Accounts (identity → fit) → Contacts → Send Queue. Prove on a 10-row slice.
2. Reference tables (T-R1 to T-R4): Verified Metrics, Product-Angle Map, ICP Rubric, Variant Library. Small, static, build once.
3. Signals (T2.1 first, Tier-1 only; T2.2 alongside). Wire the write-back to Accounts.
4. Message Gen (T4.1) reading the reference tables.
5. Deliverability monitor (T6.2) and Outreach Sync (T6.1) with the sender webhook OFF.
6. Reply Sync (T7.1) + Attribution (T7.2).
7. AE Assignment + Worklist (T8.1, T8.2).
8. Automations last, and only on motions already proven on a slice.

Governing rule, same as everywhere: measurement before volume, ICP before sourcing, human before send. Ratify scoring weights + ICP + baseline with Naveen and Scott before removing the test-slice limit.

---

## 6. What this means for actually creating them

I cannot instantiate live Clay tables through the connector; it only finds, enriches, and reads. Standing these up happens in Clay's UI. Two clean paths:

- **Day 1, in the Intradiem workspace, together.** I read you each table from this doc and you build it live; the core five take about two hours, the full architecture a day or two, paced behind the go-live gates. This is the recommended path: the data lands where the motion runs and uses the Intradiem credits set aside for it.
- **Now, in your personal Clay, as practice.** Build the core five plus the reference tables so the muscle memory is there. Hold the signals, sync, and AE layers for the real workspace so you are not maintaining a throwaway copy of the whole thing.

Either way, this document is the exhaustive list you asked for. Every table is specified and build-ready.
