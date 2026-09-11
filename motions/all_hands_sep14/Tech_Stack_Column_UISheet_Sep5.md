# Contact center platforms column, click by click

> One new enrichment column on the demo table so the recording shows, per person, which contact center and WFM platforms their company runs, with dates, from job posts. One credit per row. Written Sep 5 2026; the action and every id below were read from the live workspace and tested on the five demo companies the same day.

## What it is

Clay's PredictLeads action, display name **Find technology stack** (package `aa68bb13-b114-404a-a5cf-f920e72fbc90`, key `predict-leads-get-tech-stack-for-company-v3`). It reads job posts, site tags and DNS records and returns each technology with a first-seen and last-seen date. With the exact-match filter below it returns only contact center and WFM vendors.

Tested Sep 5 (one credit each):

| Company | Cell will show | Last seen |
|---|---|---|
| Devoted Health (Mel Chapman) | Calabrio, TalkDesk | Nov 2024 |
| Medica (Shawn Larsen, Krista Dusil) | Five9, Avaya, Avaya Call Management System, RingCentral | Apr 2026, Jan 2026 |
| Clover Health (Peter Kuipers) | Amazon Connect, Five9 | Dec 2025, Mar 2025 |
| Clever Care Health Plan (LaTonya Augustine) | empty | no contact-center read |
| AmeriHealth Caritas (act 1, not on this table) | Verint, Avaya CentreVu Supervisor, Avaya, Verint Workforce Management | Jan 2024 |

An empty cell for Clever Care is honest and fine on camera. If you want five filled cells, swap that row for another wave 2 prospect and tell me the company; one credit to check it first.

## Add the column (your hands, about three minutes)

Table `Contacts (Buying Committee)`, workbook **Star Ratings**, t_0thtm73HHxyiupTuepK. The table already has `Company Domain` (f_0thtm75xyuXYN6UMwTS), which is the only input the action needs.

1. Open the table in the **All-hands demo** view.
2. Add a column (**confirm** the control: the `+` at the right end of the header row, or `Add column` in the toolbar). Choose the enrichment picker (**confirm**: "Add enrichment" / "Enrich data").
3. Search **technology stack**. Pick the PredictLeads one, **Find technology stack** (**confirm** the provider label reads PredictLeads; there are four look-alikes in the catalog: BuyerCaddy, HG Insights, Pubrio, SMARTe, and the workspace's own `Website Technology Stack` function, which is BuiltWith and reads the marketing site. Not those).
4. Inputs:
   - **Domain**: map to the `Company Domain` column.
   - **Technology Names**: paste this exactly:
     `NICE CXone, NICE inContact, NICE Workforce Management, NICE IEX, NICE, Five9, Genesys, Genesys Cloud, Genesys Cloud CX, Verint, Verint Workforce Management, Calabrio, Calabrio ONE, Aspect Workforce Management, Alvaria, Amazon Connect, TalkDesk, Talkdesk, Avaya, Avaya Aura, Avaya CentreVu Supervisor, Avaya Call Management System, Avaya Experience Portal, Cisco Unified Contact Center, Webex Contact Center, RingCentral`
   - **Use Exact Technology Match**: on. (Off, the fuzzy filter adds Cisco routers, Amazon retail and the C language to every cell.)
   - **Last Detected Date After**: leave empty.
5. Name the column **Contact Center Platforms** (note the capitalization: whatever you type here is the name every formula must reference exactly). Turn auto-run off if the picker offers it (**confirm**), so it only runs when you run it.
6. Save. Do not run on all rows. 143 rows is 143 credits; the demo needs five.
7. In the **All-hands demo** view, drag the column to sit after the posts column (`Get a person's professional posts and shares`) and before `Persona Key`, so the enrichment reads left to right: email, posts, platforms, research. (No draft column: the Clay MessageGen path is retired as of Sep 5; the engine writes the copy.)
8. Off camera, run it on the five demo rows once (column header menu, run on selected rows, **confirm** the item) to see the cells fill. Five credits. Then clear the cells before recording the clip, or accept that the clip shows them filling from already-filled state (the clip re-runs them anyway; PredictLeads returns the same values).

**In the "Add data as columns to your table" dialog, turn on exactly one toggle: `Technologies Found`.** That is the comma-separated list ("Calabrio, TalkDesk") and it is the on-camera visual. Leave everything else off. In particular, every toggle inside the **Technologies** group is governed by the "return results of the first item" dropdown above it, so switching on Last Seen At or Title there returns only the FIRST technology's value, not all of them; Medica would show one vendor instead of five. Nothing is lost by skipping them, because the action column itself keeps the full JSON, which is what the formula column below reads.

Clay names the resulting text column `Technologiesfound`. Rename it to **Technologies Found** if you want it readable on camera; renaming is safe because formulas reference the column id, not the name.

## The AI-prompt column, tested and parked

Sep 5, two runs of a tightened research prompt (careers site, LinkedIn skills, vendor case studies, G2, structured output with a source and date) on the two rows where it would matter: Clever Care (empty PredictLeads cell) and AmeriHealth Caritas (stale Jan 2024 read). Both returned "none found". PredictLeads had Verint and Avaya for AmeriHealth from the same public job posts. So the prompted column costs two to three credits a row and, on this evidence, adds nothing the job-post index doesn't already carry. Not added. Revisit only for product-within-vendor questions (CXone versus IEX) on an account that is already in a live sequence.

## Second column: `Contact center platform, latest` (formula, your hands, two minutes)

One plain vendor name per row, chosen by the most recent last-seen date among the ACD vendors, so a formula or a MessageGen prompt can use it without parsing a list. Zero credits.

1. Add a column, choose **Formula** (**confirm** the picker label).
2. Name it **Contact center platform, latest**.
3. Paste the formula below. Clay's formula editor takes JavaScript with column references in double braces (**confirm** the editor accepts the multi-line form; if it only takes a single expression, use the AI formula helper with the plain-English line under the code and check its output against the expected values).

```
?.technologies?.filter(t=>["nice","five9","genesys","amazon connect","talkdesk","avaya","cisco","ringcentral","verint","calabrio","aspect","alvaria"].some(v=>(t?.title||"").toLowerCase().includes(v))).sort((a,b)=>(b?.last_seen_at||"").localeCompare(a?.last_seen_at||"")||(b?.score||0)-(a?.score||0)).map(t=>(t?.title||"")+" (last seen "+(t?.last_seen_at||"").slice(0,10)+")")[0]||""
```

**How to enter it, exactly (this is where it broke on Sep 4):**

1. Clear the natural-language box at the TOP of the panel completely. Leave it empty. If any wording stays in it, Regenerate rewrites your formula and reintroduces the bug below.
2. Clear the formula box completely. No stray `{{` or `}}` anywhere.
3. Type `/` and pick **Contact Center Platforms** from the picker so a green chip appears as the first thing in the box.
4. Paste the block above immediately after the chip. It starts with `?.technologies`, so the finished line reads: chip, then `?.technologies?.filter(...`.
5. **Read the finished line back before you save.** It must show `?.technologies` exactly ONCE. If it reads `?.technologies ?.technologies?.filter(` or `?.technologies?.technologies?.filter(`, the box was not empty at step 2 and the paste landed on top of leftover text. Clear everything and redo from step 2.

**This is what actually happened on Sep 5** (read from the live column on Sep 4 2026): the stored formula was `{{f_0tkvfhmrG47gd85qKVm}}?.technologies ?.technologies?.filter(...)`. JavaScript ignores the space, so it resolved to `technologies.technologies`, which is undefined; the optional chain short-circuited and `||""` returned an empty string on every row. The action column and `Technologies Found` were both filling correctly the whole time. A duplicated accessor is silent: no error, no `Invalid field`, just empty cells.

**Why the earlier attempts failed (root cause, confirmed Sep 4 against the live column settings):** the column's real name is `Contact Center Platforms` in title case. Every formula in the box, both the AI-generated one and the hand-pasted one, referenced the name in lower case as `Contact center platforms`. Clay stores a column reference as its column id (the sibling column stores `{{f_0tkvfhmrG47gd85qKVm}}?.technologiesFound`), so a name that does not match any column never resolves, and the panel reports **Invalid field**. The AI-generated version had a second bug on top of that: it read `?.vendor_name`, a key PredictLeads does not return.

**The real output shape** (read Sep 4 by running the action once on medica.com, 1 credit): top level `domain`, `total_count`, `technologies[]`, `technologiesFound`; inside each technology `title`, `last_seen_at`, `first_seen_at`, `score`, `url`, `domain`, `categories`, `source_count`, `behind_firewall`, `location_data`, `department_onet_codes`. No `vendor_name`.

The expression above was run against that real payload before being written here: Medica returns `Five9 (last seen 2026-04-17)`, and an empty cell, a no-match row and an empty array all return an empty string. The score tie-break is load-bearing, not decoration: Medica has RingCentral and Five9 tied on the same last-seen timestamp, and score is what puts Five9 (0.61) ahead of RingCentral (0.25).

It returns the product title rather than a mapped vendor family, so an Avaya row can read `Avaya Call Management System (last seen ...)`. That is fine for MessageGen plumbing; mapping product names back to a vendor family is what bloated the original into something the editor rejected, and the workflow's code step already does that mapping properly at scale.

Expected values on the five demo rows: Devoted "Talkdesk (last seen 2024-11-16)", Medica "Five9 (last seen 2026-04-17)", Clover "Amazon Connect (last seen 2025-12-03)", Clever Care empty. A WFM twin of this column uses the same shape with the WFM map: NICE Workforce Management, NICE IEX, NICE, Verint, Verint Workforce Management, Calabrio, Calabrio ONE, Aspect Workforce Management, Alvaria.

## The same read at scale: workflow on an Audiences segment (built Sep 5, draft)

Workflow **Tech stack read (PredictLeads -> Audiences company)**, wf_0tkv9u0BKvNYsV4NsQx, [open in Clay](https://app.clay.com/workspaces/1180800/terracotta/tc-workflows/wf_0tkv9u0BKvNYsV4NsQx). Draft, validated, tested end to end on Sep 5.

| Step | What it does | Credits |
|---|---|---|
| Trigger | Segment `CC Platforms: needs read (Prospect, PredictLeads empty)`, audseg_0tkv9vq4SZBjZdJuiYi: SF Prospect accounts with no platform read yet. It drains itself as the field fills (1,841 before the test, 1,840 after). | 0 |
| 1. Find technology stack | PredictLeads on the normalized domain, exact match on the vendor list | 1 per company |
| 2. Latest ACD and WFM vendor | Code step: most recent last-seen date wins, score breaks ties, product names map to the vendor (Avaya Call Management System becomes Avaya) | 0 |
| 3. Write back to Audiences | Upsert by domain into `CC Platform (latest)`, `CC Platform last seen`, `WFM Platform (latest)`, `CC Platforms (all, PredictLeads)`. Blank reads leave the fields untouched, so the company stays in the queue for a later pass. | 0 |

Test run on one member: Medica. Written back: all platforms Avaya, Avaya Call Management System, Avaya Experience Portal, Five9, RingCentral with dates; WFM blank; CC Platform (latest) Five9 (2026-04-17) after the score tie-break was added (the first pass wrote RingCentral on a same-day tie, corrected by hand). Two credits spent across the two test runs.

**Sep 5 evening, step 2 ran on the in-motion companies.** 46 companies with a lead in a live or staged lemlist campaign, Nate's six, and the Star Ratings parents (segment `CC Platforms: in-motion companies`, audseg_0tkveh3sx8nVaV3gZ2T). 37 came back with a dated vendor. Every read is on the company record in Audiences and in `tam-outbound-engine/data/cc_platform_reads_sep5.csv`. Highlights: Centene Amazon Connect (Aug 2026) + Calabrio; Humana Genesys (Sep 2026) + Aspect; Aetna Genesys (Sep 2026); The Hartford Genesys (Aug 2026) + NICE WFM; Maximus NICE CXone (Jul 2026) + Calabrio, with Nate's Verint stamped as the rep-confirmed fact; Optum NICE CXone (Aug 2026) + Calabrio; Cigna Amazon Connect (Aug 2026) + Calabrio; Truist RingCentral (2024, weak). No read for Goldman Sachs, US Bank, UnitedHealthcare, Molina, CVS Health, Anthem, BB&T, Lumeris.

Two changes landed on the way: the queues now drain on a text field `CC Platforms read status` that is written on every pass (the date field alone could not be written by the runtime), and a fifth field `CC Platform (rep confirmed)` exists for facts a rep states, written by a small manual workflow, **Stamp rep-confirmed contact center platform**, wf_0tkvfmv6eijJvqx4hgM, inputs `domain` and `value`. One cleanup item is yours: a node test created a junk company record `check-none.example` in Audiences; delete it from the Companies view.

**Sep 5, after midnight: both queues drained.** 1,880 companies now carry a read. Prospects: 1,793 read, 832 with a vendor (46 percent), 469 with an ACD seen in the last twelve months. Customers: 82 read, 59 with a vendor (71 percent). ACD mix across the base: Avaya 225, Genesys 224, Amazon Connect 115, Five9 111, NICE 81, Talkdesk 31, RingCentral 25, Cisco 10. WFM: Calabrio 155, Aspect 57, Verint 55, NICE 14. Spend 1,852 credits. Full export in `tam-outbound-engine/data/cc_platform_reads_all_sep5.csv`; the customer cut for the back-office copy in `motions/back_office_expansion/BO_Customer_CC_Platforms_Sep5.csv` with a usage note beside it.

**Still open:** publishing the workflow, which would read every new Salesforce account on arrival at about a credit each. The queues stay ready either way. The original run order, for the record:
1. Ten-row test is done (nine of ten with a vendor). The backfill runs ten at a time (`--limit` caps at 10) and the queue drains by exactly the batch size, which is the check that stops a runaway loop.
2. If the ten look right, decide the scope. A tighter segment (the Star Ratings accounts, or one vertical) keeps a run under the 200-credit line; the full Prospect queue needs an explicit go. Say the segment and the number and I'll stage that run.
3. Publishing the workflow makes it fire on every new Prospect account that lands in Audiences from Salesforce (about a credit per new account). Leave it unpublished until the scope decision is made.

These four fields are now on every company record, so any segment can filter on them, any table can pull them, and the strike-sequence skill can read them for a named account.

## Verify column: HG Insights `Verify technology usage` (your hands, on request Sep 4)

The confirmation layer, not discovery: you name the vendors, HG Insights returns its install-intelligence records for them, each with a last-verified date. Use it on rows where copy will say the vendor's name, or to freshen a stale PredictLeads read. Catalog identity (read from the live workspace Sep 4): provider HG Insights, display name **Verify technology usage**, package `b7f3454a-5095-4cb2-b91b-79cdb54e0dd2`, key `hg-insights-get-company-tech-stack-v3`. NOT tested on the demo rows yet; do not add it to the recording.

**The cost trap first: this action charges per record RETURNED (the 4/result badge), and its `limit` defaults to 10.** An unfiltered row can return 10 records = 40 credits. The vendor filter and the limit below are not optional.

1. Add a column, choose the enrichment picker, search **verify technology usage**. Pick the HG Insights one, badge "4 / result", tag Enterprise Accuracy (**confirm**; BuyerCaddy has a same-named action at 3/row, and Clay's own "Verify Technology Usage" waterfall sits above it. Not those).
2. Inputs (names from the action schema; the UI may label them slightly differently, read the screen):
   - **company_identifier** (required): map to the `Company Domain` column.
   - **vendor_names**: the vendors to verify, case-insensitive substring match. For the ACD/WFM set paste: `NICE, Five9, Genesys, Verint, Calabrio, Talkdesk, Avaya, Aspect, Alvaria, Amazon`
   - **product_last_verified_date_min**: set to twelve months back (e.g. `2025-09-04`) so only fresh installs return and stale records don't bill.
   - **limit**: **3**. Hard cap on billable records per row; raise it only after you've seen real outputs.
   - Leave country, product ids/categories/attributes, offset empty.
3. Name the column **CC platform verify (HG)**. Auto-run off (**confirm** the toggle).
4. Do not run it yet. First use is the 10-account test against known truths (rough cost 40 to 120 credits at limit 3 depending on how many records return; state the actual after). Paste back: "Run the HG Insights Verify test" and I'll stage the account list and read the results.

Division of labor once both exist: PredictLeads discovers at 1 credit and fills the demo visual; HG verifies the named vendor before the strike-sequence or MessageGen copy is allowed to say it. The copy gate keeps honoring the twelve-month freshness rule either way.

## AI-prompt column: the tested research prompt (your hands, if you want it on the table)

Parked on Sep 5 evidence: two runs (Clever Care, AmeriHealth Caritas) both returned "none found" while PredictLeads had Verint and Avaya for AmeriHealth from the same public job posts, at 2 to 3 credits a row against PredictLeads' 1. Adding it anyway is fine for product-within-vendor questions (CXone versus IEX) on accounts already in a live sequence; expect empty cells to be the common case.

1. Add a column, choose the AI / agent option in the picker (Claygent; **confirm** the current label, the picker has renamed this before).
2. Model: the strongest option offered (**confirm** the names on screen); per house rule, never tier research down.
3. Column name: **CC platform research (AI)**.
4. Prompt, paste exactly (this is the Sep 5 tested spec, reconstructed to the same shape):

```
Find which contact center (ACD/CCaaS) and workforce management (WFM) platforms {{Company}} ({{Company Domain}}) runs internally. Check, in order: their careers site and current job postings; LinkedIn profiles of their contact center and WFM staff (skills and job descriptions); vendor case studies and press releases naming them as a customer; G2/TrustRadius reviews written by their employees. Vendors to look for: NICE (CXone, IEX), Five9, Genesys, Verint, Calabrio, Aspect/Alvaria, Amazon Connect, Talkdesk, Avaya, Cisco/Webex, RingCentral. Output JSON: {"platforms":[{"vendor":"","product":"","evidence_url":"","evidence_date":"YYYY-MM"}]}. Only include a platform when you found a specific source; if you find nothing, return {"platforms":[]}. Never guess from company size or industry.
```

5. Output type: JSON (**confirm** the field), auto-run off, run on selected rows only.
6. Keep it OUT of the All-hands demo view either way; on camera an empty cell next to a filled PredictLeads cell reads as the tool failing.

## Traps

- Fuzzy match off, exact match on, or the cells fill with networking gear.
- Never run on all rows. Selected rows only.
- The read is what job posts say. A last-seen date older than twelve months is context, not a claim; the copy gate in the engine and the strike skill will not put that vendor's name in an email.
