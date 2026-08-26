# Gate Fix UI Sheet: Aug 3 2026

The hands-on steps that close the STOP-THE-LINE WFM-Adjacency leak and finish the Apollo Push hardening. Everything agent-executable already landed on Aug 3 (Apollo Push gate node edited + validated; TAM engine HCSC filter live and tested). What's below is Clay-UI-only: the tables CLI/API on this plan has no write path, and these columns have no workflow node behind them.

**Do the fixes in this order.** Fix 1a must land before Fix 1b (1b's lookup reads the flag 1a corrects). Fix 2's step is independent, do it anytime.

Verified live Aug 3: WFM L3 is at 518 HOLD / 6 READY, 5 of the 6 are Elevance Health (a current customer). Until 1a + 1b are done, the leak is still open.

---

## Fix 1a: WFM L1 `customer_flag` (root cause)

The column is a plain static text column, no formula, currently `"FALSE"` for Elevance Health and Molina Healthcare. This replaces it with the same 10-pattern denylist the Star Ratings Accounts (Master) uses, adapted to L1's `company_name` (L1 has no `parent_org`).

1. Open table **WFM_Adjacency_L1_Seed_Enriched_28** (`t_0tict25TSXgTgdJgtZZ`), workbook "WFM-Adjacency Motion".
2. Click the **`customer_flag`** column header to open the column menu and choose the edit/convert-to-formula option (label to confirm on-screen, likely "Edit column" or a pencil icon).
3. Paste this formula exactly:

```
["health care service","humana","unitedhealth","cvs health","aetna","elevance","molina","kaiser","scan health","scan group"].some(c => String({{company_name}}).toLowerCase().includes(c)) ? "TRUE" : "FALSE"
```

4. Save. Confirm both rows flip: Elevance Health → `TRUE`, Molina Healthcare → `TRUE`. `New Logo Eligible`, `Intent Score`, `intent_status`, and `Grade` all already reference `customer_flag` and self-correct on save; no further L1 edits.

## Fix 1b: WFM L3 customer check in `Send Ready`

L3 (`t_0tic8arWbZp8bSx87Ad`) has no customer field at all today. Three steps, strictly in order (each references the one before).

**Step 1: lookup column (first):**
1. In table **L3**, add a new column with action **"Lookup Single Row in Other Table"** (same action the Golden Scaffold's "Universe Lookup" uses).
2. Configure: Table to Search = `WFM_Adjacency_L1_Seed_Enriched_28` (`t_0tict25TSXgTgdJgtZZ`); Target Column = `domain` (`f_0tict26nU7DQakETTrR`); Filter Operator = `EQUAL`; Row Value = `{{Company Domain}}` (`f_0ti8tdrnCsHVcUNjmh8`).
3. Name it **`L1 Customer Lookup`**. Internal lookups are normally free, but check the credit estimate Clay shows before running it across the 524 rows.

**Step 2: `customer_exclude` field (second):**
1. Add a formula column named **`customer_exclude`**, boolean output:

```
{{L1 Customer Lookup}}?.record?.customer_flag?.toString()?.toUpperCase() === "TRUE"
```

**Step 3: `Send Ready` formula (last):**
1. Open the **`Send Ready`** column (`f_0ti9ygfsJv3y8g6Nkcz`) formula editor and replace with:

```
{{Final Audit Verdict}}?.verdict?.toLowerCase()==="pass"&&{{Final Voice Audit}}?.verdict?.toLowerCase()==="pass"&&!{{customer_exclude}}?"READY":"HOLD"
```

2. Save. Strictly stricter: it can only flip rows to HOLD, never to READY.

**Verify after 1a+1b:** the 5 Elevance READY rows (Noemi G., Carlos Doroteo, Donisha Jones, Jessica Sisneros, Melissa Zam) all read HOLD. Linda Reid (vnshealth.org) is not a confirmed customer and is unaffected. Expected end state: 523 HOLD / 1 READY at most.

Note for later: WFM L3 still has no `human_approved`/`bdr_claimed` concept, unlike the Golden Scaffold template. This sheet closes the customer leak only; full golden-parity is a separate decision.

## Fix 2: Apollo Push trigger wiring (makes the Aug 3 node edit functionally live)

The gate node in **Stars Post-Approval Apollo Push (Pilot)** (`wf_0titsor23E4P75KaM8t`) now requires `human_approved == True AND customer_exclude_bool == False`, but the Manual trigger doesn't declare `customer_exclude_bool` yet, so at runtime the value resolves to nothing and only the human_approved check bites. The workflow is dormant (all 16 customer rows are `human_approved = false`), so no urgency race, but close it before the pilot wakes up:

1. Open the workflow in Terracotta, click the **Manual** trigger node.
2. In the input-schema editor (where `email`, `human_approved`, etc. are listed), add field **`customer_exclude_bool`**, type **boolean**.
3. When this workflow later gets wired to an "Invoke Workflow" action column on **Contacts (Buying Committee)** (`t_0thtm73HHxyiupTuepK`), that column's Inputs must map:

```
"customer_exclude_bool": "{{f_0tigv0bPYTxSt3Zdh7s}}"
```

(`f_0tigv0bPYTxSt3Zdh7s` is the table's existing `customer_exclude_bool` boolean column, already derived from the text `customer_exclude` field.)
