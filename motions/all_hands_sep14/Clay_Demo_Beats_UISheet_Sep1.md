> **Superseded Sep 2 2026** by `Recording_UISheet_Sep2.md` (three-act cut). The Clay ids and rows below are still correct and are carried over there; beat 2 changed from the webinar segment to the back-office prospect-to-customer flip.

# Clay demo beats, click-by-click (your hands, work Mac)

Written Sep 1 2026 for the all-hands recording. Covers the three Clay beats in `Demo_Recording_Script.md` (beats 2, 3, 4). Every name and id below was read from the live workspace (1180800) on Sep 1. Labels in `code` are from Clay's Audiences docs read today; anything marked **(confirm)** is a label I could not verify and you should read off the screen. If the screen differs from a step, stop and tell me what you see; do not improvise a click.

Workspace: https://app.clay.com/workspaces/1180800

---

## Before any recording (in this order)

1. **Hide the audit columns in the beat 3 table (see beat 3, step 0).** Most rows show `voice_status = FAIL` and `send_ready = HOLD` today; those are gate columns doing their job, but on a projector they read as failures. They must be out of the demo view before the dry run.
2. **Dry-run beat 3 off camera** on the five rows listed under beat 3. A few credits per row, under the 100-credit line. If any cell errors, swap the row; never debug on camera.
3. **Stage the three Clay tabs** (Audiences, the table, the workflow), then set browser zoom to 125% and hide the bookmarks bar.

---

## Beat 2 · Clay Audiences (about 30 seconds of tape)

**What you're showing:** the People database synced from Salesforce, and one segment narrowing in real time. Not Companies, not Deals, not the sync settings.

Live counts read Sep 1 (Salesforce sync moves them; re-read the morning you record):
- `Sep 2 webinar invite, T2 contact-center ops and back office at prospect accounts` (`audseg_0tk4ivrtewkTk67M9GK`): **25,968**
- `Sep 2 webinar invite, T2 Director+ at prospect accounts` (`audseg_0tk4ivr8riXSR3RA4Vh`): **17,459**
- `Sep 2 webinar invite, T2 contact-center ops and back office at customer accounts` (`audseg_0tk4ivrqcYkdD83WFEQ`): **4,246**

1. Left sidebar, click **Audiences**. You land on the Audiences page: tabs for segments you created, segments others created, and `Drafts`; a `+` next to `My Audiences`.
2. Top of the page, click the `People` tab (next to `Companies`). The people count at the top should read about **140,805**. Hold 2 seconds. Say the number, don't zoom into it.
3. Optional 3 seconds: click `Companies` (**2,283**), then back to `People`. Skip if the take runs long.
4. Open **`Sep 2 webinar invite, T2 contact-center ops and back office at prospect accounts`** (~25,968). Let the count land.
   - The filter already on it, top to bottom: Account Type (Salesforce field) = Prospect · a title group for contact-center and back-office functions · **a seniority group with nine chips: Director, VP, Vice President, Head, Manager, Supervisor, Chief, President, Lead** · an exclusion group (Engineer, Software, Developer, Recruit, Sales) · email not empty · Lead Source does not contain Webinar.
5. Open the filter panel (`Criteria` per the docs, **confirm**), find the seniority group, and **remove three chips: Manager, Supervisor, Lead**. Count drops from ~25,968 to **~17,531** (verified by an ad-hoc count on Sep 1). That's the "count lands in seconds" moment. Hold on the new number for 3 seconds.
   - The saved `T2 Director+` segment (17,459) is the same idea with SVP/EVP/"Head of" chips instead of the bare "Head", which is why the two numbers differ by ~70. Nobody in the room will notice; don't explain it.
6. **Do not save.** Close the panel and discard the change (**confirm** the discard prompt wording). The saved segment stays as built.

**One-click alternative** if chip removal is fiddly on camera: in the same segment, change the first filter from Account Type = Prospect to **= Customer**. Count drops ~25,968 → **~4,246** (that's exactly the saved customer segment). Narration flips to "same roles, now only at our customers, in one click." Still don't save.

What NOT to show: `Cold-Outbound Exclusion`, `Account Type Missing`, `Heat *`, `SF Activity *`, `JC Watch *` segments (internal gate and signal plumbing; the names invite questions you don't want in a 10-minute slot). Don't open a person record; the Salesforce fields on it are a rabbit hole.

Narration (from the script): "Everyone we know, in one place, synced from Salesforce. Watch what a list build looks like now." Pause for the count. "That used to be days of export and spreadsheet work. Zero cost, and it stays current on its own."

---

## Beat 3 · The motion table, rows enriching live (60 to 80 seconds of tape, the centerpiece)

**Table:** `Contacts (Buying Committee)` in workbook **Star Ratings**. Table id `t_0thtm73HHxyiupTuepK`, 143 rows. This is the Stars motion table with the full pipeline on it.

Left sidebar, `Workbooks` (**confirm** label), open **Star Ratings**, open **Contacts (Buying Committee)**.

### Step 0 (before the dry run): make a demo view

Create a saved view (**confirm**: Clay calls these views; look for the view selector near the table name) named **All-hands demo** that shows ONLY these columns, in this order left to right:

| Show | Why |
|---|---|
| Full Name, Company, Job Title | who |
| `email_final`, `Validate Email` (action) and `Status` (rename to **Email check** if you like; safe, formulas use the column id) | "email verified". The `Email Status` column is NOT the validator: it reads the SalesNav staging import and is empty on every row. The live chain is `email_final` (the address) -> `Validate Email` (action) -> `Status` (the verdict, reads `valid` on all five demo rows, checked Sep 4). |
| `Get a person's professional posts and shares` (action) — shows `✅ 3 posts or shares found` | "we swept what they've said publicly". **Do NOT show `li_recent_post_hook`**: it is a guardrail column that returns an empty string unless a post is under 30 days old AND about Stars, CAHPS, member experience or contact-center ops. It has run on 59 rows in this table and returned empty on every one, and the cell displays the literal word `Response`. Newest posts on the five demo rows are June and July 2026, so it will stay empty on camera. |
| `Persona Key`, `Product Angle`, `Why Now (2026-cycle)` | the research summary |
| `MessageGen Email` (action), `Msg1Subject`, `Msg1Body` | the draft |

Hide everything else. In particular hide: `Sync Leads - Star QBP Wave 1 Persona 2`, `Sync Leads - Stars QBP Wave 2 - Persona 1`, `Invoke Workflow` (these push leads out; nothing must run them on camera), `Draft Audit`, `Voice Audit`, `voice_status`, `voice_reason_readout`, `msg1_critic Status`, `Msg1Critic Reason`, `send_ready`, `human_approved`, `customer_exclude`, `customer_exclude_bool`, both `Lookup Single Row` columns, `Wave 2 Audit`, and all eleven `New Column` placeholders.

### Rows to use (read from the live table Sep 1; all prospects, `customer_exclude = FALSE`, wave 2, drafts already exist)

| Row id | Person | Company | Title |
|---|---|---|---|
| r_0thvacw5dJyCWuV9Kaj | Mel Chapman | Devoted Health | Senior Director of Member ... |
| r_0thvacwCN8reRjtCHAb | Shawn Larsen | Medica HealthCare Plans | Vice President Quality, St... |
| r_0thvacwmcH4cxdB5SSQ | Krista Dusil | Medica | Chief Financial Officer |
| r_0thvacwxYkJKwhroG29 | LaTonya Augustine | Clever Care Health Plan | Director of CAHPS and Star... |
| r_0thvacx83jBxHR9ei9e | Peter Kuipers | Clover Health | Chief Financial Officer |

Do NOT use Jeff Ingram (left L.A. Care, removed from lemlist Aug 31) or any row with an initial for a surname ("Nancy H.", "Donna S.").

Filter the view to these five (filter on Full Name, or select them; **confirm** how the view filter is labeled) so the room sees five rows, not 143.

### Dry run (off camera)

1. In the demo view, on the five rows, run these columns in this order: `Validate Email`, then `Get a person's professional posts and shares`, then `MessageGen Email`. Use the column header menu, run on selected rows only (**confirm** the exact menu item; it is a "run" option scoped to selected or filtered rows, not "run all rows"). 143-row runs are the trap here.
2. Confirm every cell fills clean: `Status` = `valid`, the posts column showing `✅ N posts or shares found`, `Msg1Subject` and `Msg1Body` rewritten. Note: MessageGen overwrites the existing draft on those rows; that's fine, these rows are not what is loaded in lemlist (lemlist holds its own copy).
3. If a cell errors, swap that row for another wave 2 row with `customer_exclude = FALSE`, and rerun.

### On camera

1. Table open in the **All-hands demo** view, five rows visible, columns readable at 125%.
2. Run `Validate Email` on the five rows (same menu as the dry run). Cells fill.
3. Run `Get a person's professional posts and shares`. Cells fill.
4. Run `MessageGen Email`. `Msg1Subject` and `Msg1Body` fill. Click into one `Msg1Body` cell at the end so the room can read one full email (**confirm** the cell expands on click).
5. Record 2 seconds of still screen at the end.

If the runs are fast enough to overlap, run all three in a row without waiting; left-to-right fill is the whole visual. If a run takes longer than 20 seconds, that is what the 3x speed ramp in the edit is for.

Narration (from the script): "Here's the part that used to be a full-time job. For every contact: find them, verify the email, confirm they're still in the seat, research what they care about, and write five touches in the rep's own voice. Watch it happen for five people at once." Then silence for 10 to 15 seconds. Then: "Every draft still passes a checkpoint before anything sends. The checkpoints are tuned per motion and widen as each motion earns trust."

---

## Beat 4 · The webinar workflow (20 to 25 seconds of tape)

**Workflow:** `Webinar Registrant Enrich + Route`, id `wf_0tk333zvDnGg4YcikFp`, published, live.
Direct URL: https://app.clay.com/workspaces/1180800/terracotta/tc-workflows/wf_0tk333zvDnGg4YcikFp

1. Open the URL above. The graph should show: the segment trigger (on `Webinar Leads (Lead Source contains Webinar)`) → Normalize → Triage gate → Enrich Person → Merge profile → Persona key → Persona gate → route (bdr_review / nurture) → Write back to Audiences. One slow pan across it, left to right, 8 seconds.
2. Open the run history (**confirm** the tab name; "Runs" or similar). Today the live workflow shows the first 20 runs from Aug 20, all `completed`.
3. **If that list looks thin on screen**, switch to the bulk backfill twin instead: `Webinar Registrant Enrich + Route (bulk backfill)`, id `wf_0tk344sg8uVq27RAKd3`. Its run history is the 1,016-registrant backfill (the CLI pages 50 at a time, all `completed`). Same graph, denser history. Decide during staging, not on camera.
4. Click into one completed run so the room sees a real registrant flowing through the nodes (5 seconds), then back out.

What NOT to show: the trigger settings panel (it names segment ids), the code inside the nodes, and any run with a competitor registrant (Nice, Verint, Aspect) if you can see the company name at a glance.

Narration (from the script): "This one runs without me. Someone registers for a webinar, and by the time marketing looks up, they're enriched, classified, and routed to the right owner. It handled a thousand registrants the week we turned it on."

---

## Traps, in one place

- Beat 2: don't save the edited segment (chip removal or the Customer flip, either way discard).
- Beat 3: never run a column on "all rows"; never click either `Sync Leads` column or `Invoke Workflow`; the demo view exists so those columns are not on screen at all.
- Beat 3: the two `Lookup Single Row` columns and `customer_exclude` are the customer gate. Hidden, not deleted.
- Beat 4: stay on the graph and run history; the trigger panel exposes internal ids.
- Everywhere: credit balance off screen where the UI allows; no 6sense.
