# Mobile Phone Enrichment, Click-by-Click UI Sheet (Aug 6 2026)

Scoped after inspecting live table schemas rather than guessing. Live credit balance at time of writing: **72,403**.

## Scope decision, and why

I checked the candidate tables before recommending anything.

| Table | ID | Rows | Phone coverage today | Verdict |
|---|---|---|---|---|
| Back Office Contacts - Master List | `t_0tingaqoNzymfmSpEZh` | **313** | **none** | **DO THIS ONE** |
| Stars QBP Updated Messaging - Finance | `t_0tin68kqJbUJ2ihstZa` | 4 | none | Skip |
| Stars QBP Updated Messaging - Quality | `t_0tin6euXyjQe5SepEAG` | small | none | Skip |
| Stars QBP Updated Messaging - Operations | `t_0tinhg9t5zkFj5gfQGo` | small | none | Skip |

**Why the Stars messaging tables are out.** Finance holds 4 rows, not the 15 the campaign carries, and all three are wired to **Smartlead** (Clay Sequencer actions pointing at campaign `3712378`), not lemlist. They are a parallel legacy path. Spending credits to enrich 4 rows on a sequencer you are not launching through is waste. Flag for a separate conversation: these tables should probably be retired or re-pointed, because right now the Clay side and the lemlist side of Stars are two different systems.

**Why the Back Office master is in.** It is Mandate 3 (the 200+ back-office contacts), it holds 313 real rows, `LinkedIn Profile` and `Company Domain` are both populated fields, and it has **zero phone enrichment of any kind**. It is the largest active universe with the biggest gap.

## What you already have, so we don't rebuild

Two things worth knowing before adding anything:

1. **The managed function `Enrich Person and Find Contact Details`** (`function:t_0thx4ojyQd6uNhDf44G`) already outputs a **`Mobile Phone`** field. Its own description: "find and validate a work email **and a mobile phone number** … Outputs standardized values in the 'Work Email' and 'Mobile Phone' fields." Cost: **12.8 credits per run**. This is what got 17/17 contact details on the Citizens/Hartford blitz.

2. **The Back Office table already has a 12-provider Work Email waterfall** (Clay infer, Findymail, Hunter, Prospeo, Kitt, Datagma, Wiza, Icypeas, Enrow, Dropcontact, LeadMagic, SMARTe), each with a Findymail validation step, merging into the `Work Email` column (`f_0tinpieumh3unQ7oh5e`).

**This is the key insight:** four providers already connected for email also return mobile numbers. **LeadMagic** ("find work email **and mobile** data"), **SMARTe** ("verified work emails **and mobile numbers**"), **Wiza** ("verified emails **and phone numbers**"), **Datagma** ("find contact info"). So a Mobile Phone waterfall needs no new integrations, no new auth, no new vendor spend approval. You are turning on a capability you are already paying for.

## The recommendation

Build a **Mobile Phone waterfall** on `t_0tingaqoNzymfmSpEZh` using providers already in the workspace, rather than running the bundled function.

Reason: the bundled function at 12.8 credits/row × 313 rows = **4,006 credits** (5.5% of balance), and it would re-find the work email you have already solved with a 12-step waterfall. A phone-only waterfall does not redo that work.

**Test-first rule (non-negotiable, per the wave runbook).** Run on 10 rows, read the actual credit spend and hit rate off the run, then decide whether to run the remaining 303. Ten rows on the bundled function is ~128 credits, which is noise. Never authorize the full 313 before you have seen a real hit rate.

---

## Steps, in dependency order

Do these in order. Step 3 must not happen before step 2 or you will burn credits on all 313 rows.

### Step 1. Open the table

Go to `https://app.clay.com/workspaces/1180800/` and open workbook **Back Office Motion**, table **Back Office Contacts - Master List**.

Confirm before doing anything: bottom of the table should read **313 rows**. If it does not, stop and tell me, because the scope changed.

### Step 2. Add the first mobile provider as a new column

1. Scroll to the far right of the table and click the **+** at the end of the column headers.
2. In the enrichment search box, type **LeadMagic**.
3. Choose the action **Find mobile** (label to confirm on screen; LeadMagic's phone action may read "Find Mobile Phone" or "Mobile Finder" depending on the current package version. If none of those appear, tell me what you see and I will re-map it).
4. Map the inputs:
   - **Person's professional URL / LinkedIn URL** → `LinkedIn Profile` (field `f_0tingd3AbPFggbCBsbo`)
   - **Company Domain**, if the action asks for it → `Company Domain` (field `f_0tingd3hJ4VTFVNk7N8`)
5. **Before saving, find the "Run settings" / conditional run toggle and set it to run on NO rows, or leave the column unsaved-but-configured.** The goal is that saving does not immediately fire 313 runs. In current Clay this is the **"Only run if…"** condition or the **Auto-update** toggle. Set the condition to something false for now, e.g. `1 == 2`, or turn auto-run off.
6. Save the column.

### Step 3. Test on 10 rows, and read the result

1. Select the first 10 rows using the row checkboxes.
2. Use **Run selected rows** (or the ⚡ / "Run" action on the column header, scoped to selection).
3. Wait for all 10 to resolve.
4. Record three numbers and send them to me:
   - **Hit rate**: how many of 10 returned a mobile number.
   - **Credits consumed**: check `clay credits` before and after, or read the column's per-run cost shown in the UI.
   - **Quality spot-check**: pick 2 hits and confirm the number looks like a mobile, not a switchboard.

**Do not proceed to step 4 until you have those three numbers.** If the hit rate is under about 40%, a single provider is not worth the waterfall and we should go straight to the bundled function instead.

### Step 4. Add the fallback providers as a waterfall

Only after step 3 passes.

1. Click the **LeadMagic mobile column header → "Add to waterfall"** (label to confirm; Clay's current pattern is to select the column and choose **Combine into waterfall** or **Add fallback provider**).
2. Add, in this order, each mapped to `LinkedIn Profile` and `Company Domain` the same way:
   - **SMARTe** → mobile / phone action
   - **Wiza** → phone action
   - **Datagma** → phone action
3. Name the merged output column **`Mobile Phone`** so it matches the naming the managed function already uses. This matters: keeping the field name identical across tables means downstream lemlist loads and any future workflow can reference one name.

Order rationale: LeadMagic and SMARTe both advertise mobile specifically, so they lead. Wiza and Datagma are broader contact-info providers and are more likely to return a desk line, so they sit last as a backstop.

### Step 5. Run the remaining rows

1. Select all rows, or set the column's run condition to `{{Mobile Phone}}` is empty so it only fills gaps.
2. Run.
3. Immediately after, run `clay credits` and send me the new balance so the credit ledger stays accurate.

### Step 6. Tell me when it's done

I will append the run to `Clay_Credit_Ledger.md` with credits in, hit rate, and cost per mobile number found, so this shows up in the receipts story rather than as an untracked burn.

---

## Things I could not verify, flagged rather than guessed

- **Exact per-provider phone credit costs.** Clay shows these in the UI at the moment you add each provider, and they are not exposed through the API. Read them on screen at step 2 and step 4. The only cost I can state precisely is the bundled function at 12.8 credits/run.
- **Exact button labels.** I verified the table structure, field IDs and provider list through the API, not through the current UI. Every label above that I am not certain of is marked "to confirm". If a label does not match, tell me what you see rather than guessing at the nearest match.
- **Mobile vs direct dial.** The blitz enrichment returned what the build doc called "direct dial". Whether those were true mobiles is unverified. If mobile specifically is what you need for the multichannel steps, the step 3 quality spot-check is where that gets settled.

## Not done, and why

I did not run any enrichment. Adding columns and running enrichment on a live table spends credits and is your hand by standing convention, and the CLI/MCP/API cannot create or alter Clay table columns regardless. Workflows are the only build surface available to me there.
