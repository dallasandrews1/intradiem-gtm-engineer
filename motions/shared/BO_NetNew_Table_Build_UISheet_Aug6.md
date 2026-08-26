# Back Office Net-New Prospect Table, Build Sheet (Aug 6 2026)

Supersedes the mobile-enrichment scope in `Mobile_Phone_Enrichment_UISheet_Aug6.md`. That sheet targeted `Back Office Contacts - Master List` (313 rows), which Dallas confirmed is **all current customers**. Enriching it for cold mobile outreach was the wrong spend and sits next to the customer-exclusion gate. The mobile waterfall design in that sheet is still correct; it just belongs on the new net-new contacts table below, not on the install-base one.

Workbook: **Back Office Motion**, `wb_0ti4jh8ATmjiCowc7JM`.

## The blocker to fix first

**The install-base table has no domain field.** `101 Install-Base Accounts (Full Universe)` (`t_0ti4jj1hfZyEWcfirfU`, 101 rows) carries `account_name` and nothing resembling a website or domain. Every other field is there: vertical, bo_priority, install_base, fo_risk_flag, owner_cleared, licenses, six signal booleans.

That matters because AE TAM lists arrive keyed on **website**. Keegan's is `Account Name, Website, Type, TAM, Account Owner`. Without a domain on the install-base side, the exclusion gate has to match on company *name*, and name matching is where customers leak. "State Employees Credit Union (SECU)" against an install-base row reading "SECU" does not match. A miss here puts a current customer into a cold campaign, which is the one failure mode that cannot happen.

**Fix it before building anything else.** It is 101 rows, one-time, and it makes every future exclusion gate reliable.

### The second gotcha, and it is the dangerous one

`install_base` on that table is stored as **text**, not boolean. The table's own scoring formula proves it:

```
{{fo_risk_flag}} == "TRUE" ? 0 : (({{install_base}} == "TRUE" ? 10 : 0) + ...)
```

Every gate formula below must do a **string compare against `"TRUE"`**. If anyone writes a truthiness check (`{{install_base} ? ...`), the string `"FALSE"` is also truthy, and an empty value reads falsy. Either way the gate silently inverts and a customer ships. This is the exact failure named in the standing Clay rules, now confirmed live on this table.

---

## Step 1. Add a domain column to the install-base table (prerequisite)

Table: `101 Install-Base Accounts (Full Universe)` (`t_0ti4jj1hfZyEWcfirfU`)

1. Open the table, click **+** at the end of the columns.
2. Search the enrichment for **Company Domain** (this is the managed function `function:t_0thx4oeCWHZgydZRRVv`, already in the workspace).
3. Map input **Company Name** → `account_name` (`f_0ti4jj2wiPhYXNvZZxA`).
4. Name the output column exactly **`domain`**.
5. Run on all 101 rows. Small, one-time, and it permanently hardens the gate.
6. Add one more column, a formula, named **`domain_key`**:
   ```
   {{domain}}?.toLowerCase()?.replace(/^https?:\/\//,"")?.replace(/^www\./,"")?.replace(/\/.*$/,"")?.trim()
   ```
7. **Eyeball the 101 results before moving on.** Any row where `domain` came back empty or obviously wrong is a hole in the gate. Fix those by hand. Tell me the count of empties and I will help resolve them.

---

## Step 2. Create the accounts table

New table in **Back Office Motion**. Name: **`BO Net-New Prospect Accounts (AE TAM Intake)`**

### 2a. Intake columns, named to match the AE handoff exactly

Create these as plain text columns so an AE's CSV imports with zero reshaping:

| Column | Source |
|---|---|
| `Account Name` | AE CSV |
| `Website` | AE CSV |
| `Type` | AE CSV (expect "Prospect") |
| `TAM` | AE CSV (expect "Target Market Account") |
| `Account Owner` | AE CSV (the AE's name) |

This is Keegan's exact header row, verified against `Keegan_TAM_Accounts_Aug3.csv` (103 accounts). Any AE who sends the same five columns imports clean.

### 2b. Normalization columns (formulas)

**`domain_key`**
```
{{Website}}?.toLowerCase()?.replace(/^https?:\/\//,"")?.replace(/^www\./,"")?.replace(/\/.*$/,"")?.trim()
```

**`account_name_key`**
```
{{Account Name}}?.toLowerCase()?.replace(/\(.*?\)/g,"")?.replace(/[^a-z0-9]/g,"")
```
(The `\(.*?\)` strip removes parenthetical aliases like "(formerly FLEETCOR)" and "(SECU)" before comparison.)

### 2c. The exclusion gate

**Column: `Install Base Lookup (domain)`** — enrichment **Lookup Single Row in Other Table**
- Table ID: `101 Install-Base Accounts (Full Universe)`
- Target Column: the `domain_key` field you created in step 1
- Filter Operator: `EQUAL`
- Row Value: `{{domain_key}}`

**Column: `Install Base Lookup (name)`** — same action, second pass
- Table ID: `101 Install-Base Accounts (Full Universe)`
- Target Column: `account_name` (`f_0ti4jj2wiPhYXNvZZxA`)
- Filter Operator: `EQUAL`
- Row Value: `{{account_name_key}}`

Two passes on purpose. Domain is the reliable key; name is the backstop for rows where step 1 left the domain empty.

**Column: `exclusion_status`** (formula). Mirrors the `Seed Contact Match Type` pattern already working on the master list:
```
(!{{Install Base Lookup (domain)}} || {{Install Base Lookup (domain)}}?.toLowerCase()?.includes("no record found")) && (!{{Install Base Lookup (name)}} || {{Install Base Lookup (name)}}?.toLowerCase()?.includes("no record found")) ? "net_new" : "INSTALL_BASE_HIT"
```

**Column: `cleared_for_outreach`** (formula). This is the send gate. Note every comparison is a string compare:
```
{{exclusion_status}} == "net_new" && {{Type}} == "Prospect" && ({{Install Base Lookup (domain)}}?.["fo_risk_flag"] != "TRUE") ? "TRUE" : "FALSE"
```

### 2d. Working columns

`ae_owner` (copy of Account Owner), `sourced_date`, `wave_status`, `contact_cap` (default 4, matching the install-base table's convention).

---

## Step 3. Validate the gate on real rows before sourcing a single contact

Non-negotiable, and it is the rule that exists because a synthetic pass can hide a real-row gate misfire.

1. Import Keegan's `Keegan_TAM_Accounts_Aug3.csv` (103 accounts) as the first load.
2. Run the two lookup columns and the two formulas.
3. **Read the real rows.** Report to me:
   - How many came back `net_new` vs `INSTALL_BASE_HIT`
   - The full list of `INSTALL_BASE_HIT` account names
   - How many have an empty `domain_key` (those rode on name matching alone and are the weak ones)
4. **Hand-check at least five `net_new` rows against the install base yourself.** If a known Intradiem customer is sitting in `net_new`, stop and tell me. That is the gate failing, and it fails silently.

Do not proceed to step 4 until this passes on real rows.

---

## Step 4. Create the contacts table

New table in the same workbook. Name: **`BO Net-New Prospect Contacts`**

1. Source it from `BO Net-New Prospect Accounts`, **filtered to `cleared_for_outreach == "TRUE"`**. The filter is the gate. Never source from the unfiltered account list.
2. Add contact sourcing: the managed function **`Find People at Company`** (`function:t_0thx4ojJXAZRsqAiqyv`), capped per account by `contact_cap`, targeting the back-office personas from the `intradiem-backoffice-icp` skill (claims ops, shared services, document processing, payment ops), Director+ per the Mary Ann hard gate.
3. **Contact-level dedup.** Add `Normalized Name Key`:
   ```
   {{Full Name}}?.toLowerCase()?.replace(/[^a-z0-9]/g,"")
   ```
   then a **Lookup Single Row in Other Table** against `Back Office Contacts - Master List` (`t_0tingaqoNzymfmSpEZh`), target column `Normalized Name Key` (`f_0tino9hcM53SA8TfF6k`), operator `EQUAL`, row value `{{Normalized Name Key}}`. This catches a person who already exists on the customer side. Same three-way classification: `net_new` / `DUP_IN_SEED` / `NEAR_MISS`.
4. **Work Email waterfall.** Do not rebuild it. The 12-provider waterfall on the master list is proven; copy that column group across (Clay infer → Findymail → Hunter → Prospeo → Kitt → Datagma → Wiza → Icypeas → Enrow → Dropcontact → LeadMagic → SMARTe, each with Findymail validation, merging to `Work Email`).
5. **Mobile Phone waterfall.** Now this belongs here. LeadMagic → SMARTe → Wiza → Datagma, all four already connected for email, all four return mobile. Output column named exactly **`Mobile Phone`** to match the managed function's naming. Test on 10 rows and read the real hit rate before running the rest, per `Mobile_Phone_Enrichment_UISheet_Aug6.md` step 3.

---

## The AE intake template

Send this to any AE handing over a list. Five columns, nothing else, no reshaping needed:

```csv
Account Name,Website,Type,TAM,Account Owner
State Employees Credit Union (SECU),www.ncsecu.org,Prospect,Target Market Account,Keegan Sanders
```

Rules to give them:
- One row per account, not per contact.
- `Website` is required. It is the join key for the customer-exclusion gate, and a blank one drops that row to weaker name-only matching.
- `Type` should read `Prospect`. If they mark an account `Customer`, it is filtered out before sourcing.
- `Account Owner` is how a booked meeting gets routed, which is the Barclays problem from the Aug 3 sync. Do not leave it blank.

---

## What I could not do, and why

Clay tables cannot be created or altered through the CLI, MCP, or the public API. Workflows are the only build surface exposed to an agent. Creating these two tables and adding these columns is your hands in the UI, which is why this is a click-by-click sheet rather than a build I ran.

Labels marked in the steps are grounded in field IDs I read from the live schemas, but the on-screen enrichment names can drift between Clay package versions. If a label does not match what you see, tell me what it says rather than picking the nearest match.

## Open question for you

`Back Office Contacts - Master List` is named as if it were the universe, but it holds 313 current-customer contacts. Once the net-new tables exist, that name will actively mislead whoever opens the workbook next. Worth renaming it to something like `BO Install-Base Contacts (Customers)`. Renaming is destructive-adjacent to anything referencing it by name, and the master list is already referenced by name in a lookup on itself, so tell me before you rename and I will trace the dependents first.
