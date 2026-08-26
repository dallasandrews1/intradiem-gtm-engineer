# WFM-Adjacency customer-exclusion leak: UI fix sheet (Aug 7 2026)

Every ID and count below was read live from workspace 1180800 on 2026-08-07, not carried forward
from the Aug 3 gate-integrity log. Read-only throughout; nothing was edited, deleted, or run.

**Nothing has reached a prospect.** All eight lemlist campaigns are draft, zero sends, and
WFM-Adjacency is parked. This is exposure, not a breach. It is also the third audit in a row
that has flagged it, so it should not survive a fourth.

---

## What is actually wrong (three defects, not one)

The Aug 3 log described this as a single missing check. It is three independent failures that
happen to stack. **Fixing any one of them alone changes nothing**, which is probably why the
previous two passes did not close it.

### Defect 1. L1's `customer_flag` was never populated at all

`WFM-Adjacency L1` (`t_0tict25TSXgTgdJgtZZ`, 28 rows). The `customer_flag` column
(`f_0tict27m8jMKrMoFjFE`) is a **plain text column with no formula**, and **all 28 rows read the
literal text `FALSE`** including Elevance Health and Molina Healthcare.

This is worse than the audit said. The audit read it as "two accounts misclassified." It is not a
misclassification, it is an **empty column that was hand-filled with a default and never wired to
anything**. No account in this motion has ever been customer-checked at the account layer.

The correct logic already exists one workbook over, on `Accounts (Master)`
(`t_0thuumoUcu6wAAhovti`, field `f_0thv8lnWsSHNnk6xwoa`), where 54 rows across 6 parents are
correctly flagged.

### Defect 2. L3's `Send Ready` formula never mentions customer status

`WFM-Adjacency L3` (`t_0tic8arWbZp8bSx87Ad`, 524 rows, 63 columns). `Send Ready`
(`f_0ti9ygfsJv3y8g6Nkcz`) is, verbatim today:

```
{{f_0ti9hp0WEN6VU2hVWsG}}?.verdict?.toLowerCase()==="pass"&&{{f_0tidtseMQ33YDojtMEd}}?.verdict?.toLowerCase()==="pass"?"READY":"HOLD"
```

Two AI critic verdicts, nothing else. I listed all 63 columns: there is **no `customer_exclude`,
no `human_approved`, no `bdr_claimed`, and no `customer_flag`** on this table.

### Defect 3. The workflow's kill switch is wired to a field that does not exist

This one is new and is not in any prior log.

`WFM-Adjacency 5-Touch Send-Readiness (Alpha)` (`wf_0tie30io3hiPqSzVRU2`) **does** have a customer
kill switch: node `1. Eligibility kill switch` (`wfn_0tie374z8msrriJTBDt`) runs the shared
`fn_eligible` function. So the workflow looks protected.

It is not, for two compounding reasons:

1. Its `Customer Flag` input is wired to `$.customer_flag` **on the L3 table trigger**, and L3 has
   no `customer_flag` column. The kill switch receives nothing.
2. Its gate (`1g. Eligibility gate`, `wfn_0tie37dgbfKmaoxhjV4`) routes on rule `eligible == False`
   to EXIT, with the **default route going onward to persona routing**. `eligible` is typed as a
   string. So an empty, null, or unexpected-case value does not match the rule and takes the
   default, which **continues**.

That is a gate that **fails open**. A gate that fails open is more dangerous than no gate, because
it reads as protection in the graph and in the node description.

---

## Live exposure, confirmed today

| Fact | Value |
|---|---|
| Rows at `Send Ready = READY` on L3 | **6** (5 Elevance Health directors + 1 VNS Health) |
| Named Elevance rows READY | Noemi G., Melissa Zam, Jessica Sisneros, Carlos Doroteo, Donisha Jones |
| Elevance contacts in the table | **159** |
| Molina contacts in the table | **133** |
| Total under the broken gate | **292** |
| Elevance / Molina status on `Accounts (Master)` | `customer_flag = TRUE`, `new_logo_eligible = FALSE`, `intent_status = excluded` |

Elevance Health and Molina Healthcare are current Intradiem customers. The two tables in this one
workspace currently disagree about that.

---

## THE ORDERING TRAP, read this before you touch anything

**Do Step 1 before Step 2.** If you fix L3's formula first, it will look fixed and change nothing:
the new formula reads `customer_flag` through the lookup into L1, and L1 currently says `FALSE`
for Elevance. Every one of those 5 rows would stay `READY` and you would have a green-looking
formula sitting on top of the same leak.

If you only have time for one step today, **do Step 1**. It closes the account layer on its own
and also repairs `New Logo Eligible`, which gates upstream paid enrichment.

---

## Step 1. Populate L1's `customer_flag` from the canonical denylist

Table: **WFM-Adjacency L1** `t_0tict25TSXgTgdJgtZZ`
Column: **customer_flag** `f_0tict27m8jMKrMoFjFE`

1. Open the L1 table and click the `customer_flag` column header.
2. Choose the option to edit the column and switch it from a plain text column to a **formula**.
   (In the current UI this is the "Formula" / "Write formula" option in the column type list. If
   the label differs on your build, it is whichever option lets you type an expression against
   other columns, the same editor `New Logo Eligible` already uses.)
3. Paste exactly:

```
["health care service","humana","unitedhealth","cvs health","aetna","elevance","molina","kaiser","scan health","scan group"].some(c => String({{f_0tict26nkmbatxnWQdr}}).toLowerCase().includes(c)) ? "TRUE" : "FALSE"
```

`f_0tict26nkmbatxnWQdr` is L1's `company_name`. This is the **same 10-pattern list** that
`Accounts (Master)` uses, so the two tables stop disagreeing. Keep it character-identical; do not
improve it here. If the list needs to change it changes in both places, which is exactly the
convergence problem in Step 4.

**Dependency check, already done for you.** The only column that consumes `customer_flag` on L1 is
`New Logo Eligible` (`f_0ticv0bEddFcpWNrYVY`):

```
!{{f_0tict27m8jMKrMoFjFE}}?.toLowerCase()?.includes("true") && !{{f_0tict4puMGwAfatSERb}}
```

It is already text-aware (`.toLowerCase().includes("true")`), so it will start returning the right
answer the moment Step 1 lands. **No re-pointing needed.**

### Verify Step 1 before moving on

Filter or sort L1 on `customer_flag`. You should see **exactly 2 rows at `TRUE`**: Elevance Health
and Molina Healthcare. The other 26 stay `FALSE`. `New Logo Eligible` should flip to false on
those same 2 rows.

If you get 0 rows at TRUE, the formula did not save or is reading the wrong column. Do not
continue to Step 2.

---

## Step 2. Add the customer check to L3's `Send Ready`

Only after Step 1 verifies.

Table: **WFM-Adjacency L3** `t_0tic8arWbZp8bSx87Ad`
Column: **Send Ready** `f_0ti9ygfsJv3y8g6Nkcz`

Replace the whole formula with:

```
{{f_0ti9hp0WEN6VU2hVWsG}}?.verdict?.toLowerCase()==="pass" && {{f_0tidtseMQ33YDojtMEd}}?.verdict?.toLowerCase()==="pass" && String({{f_0ti8uifTiAtoDgVYQTh}}?.record?.["customer_flag"] ?? "TRUE").trim().toUpperCase() !== "TRUE" ? "READY" : "HOLD"
```

Three things in that line are deliberate and are the whole point:

- **`{{f_0ti8uifTiAtoDgVYQTh}}?.record?.["customer_flag"]`** reaches L1 through the existing
  `Universe Lookup` column, which already joins L3 to L1 on domain. This path is proven: the
  `Vertical` column on this same table already reads `?.record?.["primary_industry"]` through it.
  You are not adding a new join.
- **`?? "TRUE"`** makes it **fail closed**. If the lookup misses, errors, or returns nothing, the
  row is treated as a customer and HOLDs. A missing lookup must never read as "not a customer."
- **`String(...).trim().toUpperCase() !== "TRUE"`** and not `!{{...customer_flag}}`. This is the
  live example from your own house rules: `customer_flag` is stored as the **text** `"TRUE"`, not
  a boolean, and in JS the string `"FALSE"` is **truthy**. Writing `!{{customer_flag}}` would be
  wrong in both directions and would look correct while doing it.

### Verify Step 2 on real rows

Per the standing rule, this check runs on real rows, never a synthetic input.

1. Filter L3 on `Send Ready = READY`. Before the change it returns 6.
2. After the change it should return **1**: Linda Reid at vnshealth.org only.
3. Confirm all five Elevance directors by name have moved to `HOLD`: Noemi G., Melissa Zam,
   Jessica Sisneros, Carlos Doroteo, Donisha Jones.
4. Spot-check one Molina row and confirm it is `HOLD`.

**On Linda Reid / VNS Health:** she is correctly still eligible on every source available. VNS
Health reads `customer_flag = FALSE`, `new_logo_eligible = TRUE`, `intent_status = in_motion` on
`Accounts (Master)`. She is not a leak. If she should be excluded, that is a targeting decision,
not a gate defect, and it belongs on the denylist rather than in this formula.

---

## Step 3. Make the workflow gate fail closed

This one I could have edited through the API and deliberately did not.

`fn_eligible` is a Clay **function table**, and function tables are not readable through the CLI
or MCP (`clay tables columns get` returns `not supported by this API`). So I cannot see what it
returns for an empty input, and I will not change the routing semantics of a live 57-node gate
based on a guess about its return casing. Guessing at a coercion is the exact failure in Defect 2.

Do this in the workflow editor, in this order:

1. Open `wf_0tie30io3hiPqSzVRU2`, node `1. Eligibility kill switch` (`wfn_0tie374z8msrriJTBDt`).
2. Look at the `Customer Flag` input. It is currently bound to `$.customer_flag` from the table
   trigger. **Confirm for yourself that L3 has no such column** (it does not; I checked all 63).
3. Re-point it to a field that exists. After Step 1 and Step 2 land, the clean source is the
   `customer_flag` value coming through `Universe Lookup`.
4. Then open `1g. Eligibility gate` (`wfn_0tie37dgbfKmaoxhjV4`) and **invert the routing** so the
   safe path is the default:
   - rule matches **eligible confirmed** and routes onward to `2. Persona routing`
   - **default route** goes to `EXIT: EXCLUDED`
   Today it is the other way round, so anything unexpected continues.
5. Run one real row through and read the exit status before trusting it.

Until Step 3 is done, treat the workflow as unprotected regardless of what its node descriptions
say, because the description already claims a protection the wiring does not deliver.

---

## Step 4. The strategic fix, and it is your call not mine

A correct shared function, **`fn_send_ready` (`t_0tiahe2mzsH9CCaC4Sx`)**, already exists. **No live
send table calls it.** Star Ratings, Cost-Mandate and WFM-Adjacency each run their own hand-rolled
local formula and have drifted apart. WFM-Adjacency's diverged from the Golden Scaffold pattern
after it was stamped.

The Golden Scaffold's own formula is the reference and is correct:

```
{{msg1_critic Status}} == "PASS" && {{human_approved}} && !{{bdr_claimed}} && !{{customer_exclude}} && {{Email Voice Audit}}.verdict == "PASS" ? "READY" : "HOLD"
```

Steps 1 to 3 fix this instance. They do not fix the class. The class only closes when every send
table calls one function, and that is a real trade rather than an obvious win: one function means
one edit can move every motion at once. That is the first of the four threads on the engine-room
page, and it wants your decision, not a patch.

---

## What NOT to do

- **Do not delete the 5 Elevance rows or the 292 contacts.** They are correct rows in a research
  table. The gate is what is wrong, and destructive stays your hand by standing convention.
- **Do not flip any send gate or start any campaign** as part of this. Nothing here requires it.
- **Do not "prove" the fix with a synthetic input.** Gate semantics here depend on real
  null-versus-empty and text-versus-boolean behavior, which is precisely what a synthetic pass
  hides. Real rows only.
- **Do not edit `fn_eligible` itself** while three motions still reference it, until Step 4 is
  decided.

---

## When it is done

Run the gate-integrity agent manually rather than waiting for Monday 7:20:

```
bash automation/run_gate_integrity.sh
```

Then read `automation/logs/gate-integrity-<date>.md`. The WFM-Adjacency verdict should move from
CRITICAL FLAG to PASS, and the headline should stop naming Elevance. If it does not, the fix did
not take and the log will say which layer still fails.
