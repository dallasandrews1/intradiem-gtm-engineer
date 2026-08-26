# Claude Code + Clay Handoff: finish the Stars QBP campaign staging (Jul 10 2026)

For a Claude Code / Cursor session running the Clay Agent Plugin (CLI + MCP), authenticated to workspace **1180800** (Dallas Andrews). Read this first; it carries the full context so you don't re-derive it.

## The goal (one line)

Stage the Stars QBP Wave 1 outbound so the **messaging and the eligible contacts are loaded into the campaigns, ready to send when Dallas launches** — nothing sends now, and no customer contact ever enters an outreach campaign.

## UPDATE (Jul 10 PM) — two code-side actions to do now

The open question is resolved (no campaign surface — see below). Data prep + eligible lists are done (doc 15 CSVs). Two things are best done in code because they touch the live 137-row Contacts table and must be exact; the UI is too error-prone for them:

1. **Neutralize the hazard.** The ungated `Sync leads to campaign (2)` action on Contacts (`t_0thtm73HHxyiupTuepK`), destination = Persona 1 campaign (`t_0thzdvvWanM662s9WBc`), has an empty `conditional_run`. Either **delete it**, or set `conditional_run` to `customer_exclude != "TRUE" && Account Forgone QBP > 0 && persona_key == "stars_quality" && email_final present`. If the plugin can't edit/delete that table action, say so explicitly and leave it — Dallas will delete it in the UI.
2. **Build two clean, customer-free source tables** in workspace 1180800 so the UI load can't leak a customer:
   - `Wave1_P1_eligible` — the 16 rows from `greenlight-pack/15_Eligible_Load_List_Persona1_Jul10.csv`
   - `Wave1_Finance_eligible` — the 23 rows from `greenlight-pack/15_Eligible_Load_List_Persona2_Jul10.csv`
   - Columns each: `email_final`, `First Name`, `Company`, `Cliff-Edge Contracts (2026-cycle)`, `Account Forgone QBP ($M, 2026-cycle)`.
   - Report the new table IDs.

Then the Cowork/UI side connects each campaign to its clean table (safe — no customers present), pastes the v2.2 sequence, and leaves Draft. Everything below is reference.

## FIRST, resolve the open question (do this before anything else)

The Clay API/CLI clearly covers **tables, workflows, functions**. It is **not confirmed** to cover the **campaign sequencer** or **loading leads into a campaign**. Run `surfaces_list` / load the `clay:clay` skill and check whether any **campaign / sequence** surface exists.

- If a campaign/sequence surface exists → you can do this end-to-end in code (load leads + paste the 3-touch sequence per campaign).
- If it does NOT → do the **data prep** in code (build/verify the eligible, persona-split, customer-excluded lists; stage a clean lead table/view), and the **sequence paste stays in the Clay UI** (the standalone campaign shells already exist — see below).

Report which case we're in before executing.

## Getting the Clay CLI fully working (`clay tables`)

The CLI installed and authenticated fine (logged in as Dallas, workspace 1180800). What failed was the `clay tables` subcommand: "beta not enabled for this workspace." The plugin is open beta for everyone on all plans (no paywall), so this is a feature flag or a config gap, not a plan limit. Fix it in this order; don't block the data work on it (the MCP `table` surface already reads/writes the same data):

1. Read **GETTING_STARTED.md** in the repo (github.com/clay-run/agent-plugins). It covers `clay login`, getting `clay` on PATH, and choosing Search / Routines / Tables.
2. Register the tables in **`~/.clay/tables.json`** — the CLI's table surface is webhook-based and references tables **by name, not URL**. Map a name → the table's webhook for the Contacts table (`t_0thtm73HHxyiupTuepK`) and any campaign table you need. Then retry `clay tables` by name.
3. If it still says "beta not enabled" after registration, it's a workspace flag — request the CLI tables beta be enabled for workspace **1180800** via Clay support or the API/CLI community announcement thread. It's open beta, so it should just be toggled on.
4. Until then, use the MCP `table` / `read` tools for all reads/writes — same capability, different surface.

## Hard constraints (non-negotiable)

- **Customer exclusion is absolute.** Any Contacts row with `customer_exclude == TRUE` (16 rows) must NEVER load into a campaign. This is the whole point of today's wire.
- **Draft only. Nothing sends.** Launch waits on mailbox warmup + a walkthrough meeting (weeks out). Do not launch, do not enable sending.
- **Never check `human_approved`.** That is Dallas's sign-off before send. You may load eligible contacts for staging (he authorized that), but you do not approve.
- **Zero credit spend without an explicit estimate + go.** Syncing table→campaign is not an enrichment and should be free; any enrichment/AI-column run that consumes credits needs a pre-estimate and Dallas's OK first.
- **Verified-claims discipline.** No Intradiem stat/customer claim in prospect copy unless it's in the Value Repository. The current campaign copy uses only the prospect's own public-CMS figures, so it's clean — keep it that way.

## Key workspace facts

- Workspace: **1180800**. Workbook "GTM Engine": `wb_0thtlocqNeb46szQtAf`.
- **Contacts (Buying Committee)** table: `t_0thtm73HHxyiupTuepK` — 137 rows. This is the source of truth for contacts.
- Relevant Contacts columns: `First Name`, `Last Name`, `Full Name`, `Job Title`, `Company`, `Company Domain`, `email_final` (THE deliverable/send email — use this as the lead email, not raw `Email`), `Cliff-Edge Contracts`, `Account Forgone QBP ($M, 2026-cycle)`, `parent_key`, `persona_key`, `customer_exclude`, `bdr_claimed`, `send_ready`, `human_approved`.
- Counts (verified in UI Jul 10): 137 contacts total; **16** `customer_exclude==TRUE` (HCSC 4 + Humana 4 + UHC 4 + CVS 4); **121 eligible** non-customer contacts.
- Persona split via `persona_key`: `stars_quality` → Persona 1 campaign; `coo_finance` → Persona 2 (Finance) campaign; `cc_ops` → HELD (no approved copy yet, keep out of both).

## Eligible target definition (the filter to apply)

Eligible for loading = `customer_exclude != TRUE` AND `Account Forgone QBP > 0` AND `email_final` present.
Then split by `persona_key`: `stars_quality` → Persona 1, `coo_finance` → Persona 2. Hold `cc_ops`.

(Note: the original brief also gated on `send_ready == READY`, which requires Dallas's approval pass. He has since authorized loading the eligible set now for staging, so `send_ready` is NOT required for the load — but sending still waits on his approval + launch.)

## What already exists (don't rebuild)

- **customer_exclude** wired and finalized on both Accounts (Master) and Contacts (HCSC now excluded; Centene stays in). 6 of 32 Tier A+B parents excluded → 26 new-logo-eligible parents.
- **persona_key** logic live on Contacts.
- Standalone campaign shell **"Stars QBP Wave 1 - Persona 1 (Stars/Quality)"** already created (table `t_0thzdvvWanM662s9WBc`, in the GTM Engine workbook). It has a working sequence editor. Persona 2 (Finance) clone still needs building.
- Old embedded campaign **"Stars QBP Wave 1 - Tier A Committee (GATED)"** (`t_0thuwyhMyNV7C7rrwmX`) is a dead end — its sequence editor is not reachable and its sync destination is locked. Abandon it; don't sync to it.

## Why the UI stalled (so you don't repeat it)

- The only gated table→campaign sync has a **locked destination** (the dead embedded campaign); duplicating it inherits the lock.
- The campaign-side "Add lead list" is **ungated** — it pulls every Contacts row with an email, including the 16 customers. That's why this needs to be done as a **filtered** load (code, or a filtered source view), never a raw connect.

## HAZARD to fix first: the unfiltered `Sync leads to campaign (2)` column

There is a **`Sync leads to campaign (2)`** action on the Contacts table whose destination is the **new Persona 1 campaign table** (`t_0thzdvvWanM662s9WBc`) and which has **NO run condition at all** — completely unfiltered. It was created (and orphaned) during a campaign-side "Add lead list" connect/disconnect on Jul 10. **Do not run it as-is** — it would push all 137 contacts, including the 16 `customer_exclude==TRUE` customers, into the Persona 1 campaign.

This is also the fix path (it's the one Contacts-side sync that CAN target the new campaign — the old gated sync's destination is locked to the dead embedded campaign). Turn it into the gated Persona 1 load by adding the run condition:

`customer_exclude != TRUE  AND  Account Forgone QBP > 0  AND  persona_key == "stars_quality"  AND  email_final is present`

Then it safely loads only eligible Persona 1 contacts. Do the equivalent for Persona 2 (a `coo_finance` sync to the Finance campaign). If it's cleaner to delete `(2)` and recreate gated, that's fine — just never run an unfiltered sync into a campaign.

## Deliverable from this session (hand back to the Cowork/UI side)

Produce and report, so the campaign load in the UI is exact and customer-safe:

1. The **eligible Persona 1 (`stars_quality`) list** and **eligible Persona 2 (`coo_finance`) list** — customer-excluded, `QBP>0`, `email_final` present — as a clean CSV and/or a dedicated customer-free Clay table (name it clearly, e.g. `Wave1_P1_eligible` / `Wave1_Finance_eligible`). A clean source table makes even the ungated campaign "Add lead list" connect safe, since there are no customers in it to leak.
2. **Final counts**: rows per persona list, and confirmation of **zero `customer_exclude==TRUE` leakage** in each.
3. A note on which remaining steps are **UI-only** (campaign build, lead load, sequence paste) vs. done in code, so the UI operator knows exactly what to click.

## The remaining work

1. Load the **eligible stars_quality** set into the Persona 1 campaign, `email_final` as the send email, mapping `First Name`, `Company`, `Cliff-Edge Contracts`, `Account Forgone QBP` for merge fields. Verify **zero** `customer_exclude==TRUE` rows landed.
2. Paste the **3-touch Persona 1 sequence** (v2.2) — source: `greenlight-pack/11_Campaign_Load_Sheet_Jul10.md`, "CAMPAIGN 1: Persona 1" (Day 0 / Day 4 / Day 9). Plaintext, HTML off.
3. Build the **Persona 2 (Finance) campaign**, load eligible `coo_finance` set the same way, paste "CAMPAIGN 2: Persona 2, Finance" (Day 0 / Day 4 / Day 9) from the same load sheet.
4. Settings per load sheet: plaintext / HTML off, min 20 min between sends, max 10 new leads/day, Tue–Thu, recipient-market Eastern, auto-stop on reply. **Leave start date unset. Do not launch.**
5. Verify: preview a Centene row per campaign, confirm merge fields render, confirm both campaigns Draft with 0 sent and no customer contacts present. Confirm zero credits consumed.

## Copy + reference files (all in this repo)

- Campaign copy (v2.2, sharpened Jul 10): `greenlight-pack/11_Campaign_Load_Sheet_Jul10.md`
- Exclusion/persona logic + net universe: `greenlight-pack/12_Customer_Exclude_Final_Jul10.md`
- Gate order / sequencer prep: `greenlight-pack/10_Sequencer_Prep_Runbook_Jul10.md`
- MessageGen AI-column deployment (v2.2, still gated on a Value Repository being built out): `greenlight-pack/03_MessageGen_Deployment_Sheet.md`
- v2.2 messaging standard (prompt): `Clay_MessageGen_SystemPrompt_v2.md`

## Open sign-off note for Dallas

Before launch (not now): confirm the campaign signature block so per-touch sign-off is right (first name Days 1–5 = Nathan; full name Day 6+ = Nathan Belfield on Day-9 closers). If the campaign auto-appends a signature, leave message bodies unsigned to avoid doubling.
