# Continuation prompt — TELUS Strike Room (account 3 of 3)

Paste everything below the line into a fresh session in the Intradiem GTM Engineer project. Bell Canada and BMO are complete. TELUS is the last of Nathan Belfield's July 29 2026 request.

---

Nathan Belfield asked on July 29 2026 for Strike Rooms on BMO, TELUS and Bell Canada. **Bell and BMO are complete** (`CostMandate_BellCanada_StrikeRoom_Sequence_v1.md`/`.pdf` and `CostMandate_BMO_StrikeRoom_Sequence_v1.md`/`.pdf`, both at project root). **Build TELUS**, to the same standard.

Load `intradiem-strike-sequence` FIRST, plus its chain: `intradiem-verified-metrics`, `intradiem-first-draft-engine`, `intradiem-copy-sharpener`. Read `CostMandate_BMO_StrikeRoom_Sequence_v1.md` as the structural reference — it is the better of the two and the PDF tooling is written against its exact section layout.

## The four open calls, already decided

These were live questions at the end of the BMO session. Dallas has since asked for a position on each rather than a menu. **Build on these unless he overrides.** The reasoning is included so he can disagree with the argument rather than just the conclusion.

### 1. Timing: build the packet now in two stages, launch the week of September 8

The framing everyone reaches for is "wait for Fuller or don't." That is the wrong gate. **The real gate is the Q2 earnings call, not David Fuller's start date.**

Here is why. The BMO packet works because Rahul Nalgirkar said a specific number, on the record, twice: $250 million, half in FY2026, half in FY2027. Every seat's copy hangs off that one sentence. **TELUS has no equivalent sentence yet.** What exists today is a press-release phrase from the July 22 reorganisation — "operational efficiencies" — with no figure, no split, no owner and no date. That is not a forcing function, it is a category.

Dodig and Chande are roughly four weeks into their jobs. Their first earnings call, expected in August, is the moment they have to put a number and a narrative on the record. Whatever Chande commits to on that call **is** the TELUS forcing function, and it will be far stronger than anything inferable today.

There is a second problem with entering now that has nothing to do with Fuller. The reorganisation was announced **seven days ago**. The directors and VPs beneath him do not yet know what their own remit is, who they report to, or what survives. That is the single worst moment in a company's life to ask someone for twenty minutes about operational change. They have no authority to act and every incentive to defer.

So:

- **Now:** build everything structural. Committee sourcing, ZeroBounce sweep, entity resolution, guardrails, cadence, objection handles, and every touch that does *not* cite the forcing function. Emails do not go stale in five weeks.
- **Leave deliberately blank:** the forcing-function paragraph in the account snapshot, and the Touch 1 and Touch 4 copy for the finance and executive seats. Mark them `[PENDING Q2 CALL]` in the markdown so it is obvious what is unfinished.
- **Morning after the Q2 call:** narrow research pass on that call only. Drop in what Chande actually committed to. Rebuild the PDF, which now takes minutes rather than an afternoon.
- **Launch the week of September 8**, not September 1. Fuller's first week is triage. Week two is when a new leader starts asking what is already in motion, and that is the week you want to already be a thread someone can point at.

This gets the packet built while the context is hot, the forcing function quoted from the CFO's own mouth, and the sends landing when the org has stopped moving.

**If Dallas wants something in market sooner**, the one defensible early entry is a single LinkedIn-only thread to the operational layer, opened on the TELUS Digital research finding below rather than on cost. That is a curiosity conversation, not a change conversation, and it survives the reorg uncertainty. Do not run the email sequence early.

### 2. Do not enter on Fuller. He is the escalation target.

Same pattern as BMO, where Mehrotra and Haward-Laird were deliberately left out of the committee. A brand-new P&L owner in his first fortnight will not take a cold meeting about operational tooling, and burning him early costs the one senior door that matters.

Enter on whoever owns customer operations **below** the P&L line and visibly survived the July 22 reorganisation — being confirmed in seat post-reorg is itself the qualifying signal, and it is checkable in Clay from `current_role_min_months_since_start_date`. Fuller becomes the escalation once a thread is warm, and "your team has been talking to us since August" is a far better first contact with him than a cold email.

### 3. Lead into the TELUS Digital objection. Do not defend against it.

The instinct is to route around the fact that TELUS Digital sells contact-centre AI commercially. That is backwards, and it is the single best thing about this account.

**TELUS Digital's own June 2026 research found only 32% of enterprises have the automated quality assurance and coaching tools needed for feedback loops.** TELUS's own arm published the gap. The opener writes itself, roughly: your own research group put the number at 32%, and the interesting question is which side of it TELUS Corporation is on.

That does three things at once. It proves the research was done, it makes the "we do this ourselves" objection the *subject* of the conversation instead of the end of it, and it is impossible to argue with because they published it. Verify the finding and its exact wording before use — it came from the July 29 sweep and has not been re-checked.

The distinction to hold underneath: TELUS Digital sells CX services **to other companies**. That is a revenue line. It says nothing about how TELUS Corporation runs its own 2,800-fewer-people operation, and conflating the two is a mistake TELUS's own executives will not make.

### 4. Matt Turnbull stays LinkedIn-only. Do not spend more credits.

He is a Tier 3 back-office seat on an eight-seat committee where seven addresses came back valid. A second waterfall pass costs credits and session time for marginal coverage, and LinkedIn-first was the *designed* path for exactly this case on Bell (Ann Cullingham). If he engages on LinkedIn, resolve the email then, when it is worth something.

### 5. Bell: strike the bullet, rebuild the PDF, do not rewrite anything

Verified July 29 2026: the two unapproved figures appear **only** in the "What reps can and cannot say → Say" bullet. They are **not** in any sequence and **not** in the objection handles. Bell's actual prospect copy is clean.

So the fix is deleting one bullet and rebuilding the PDF. Do this at the very start of the TELUS session, while the kit is already staged and the tooling is already in hand — it is the cheapest moment it will ever be, and it closes the only outstanding compliance item on a document that is otherwise ready to send.

Replace that bullet with the current allowlist: the DWO positioning statement, and Humana for replies only.

## Build order (proven twice, on Bell and BMO)

### 1. Customer-exclusion gate — do it yourself, do not trust this brief

Screen against `greenlight-pack/Active_Customers_SF_Jul10.csv` (101 active accounts). TELUS is absent and clean for new-logo.

**Screen by industry AND country, not just the names in this document.** The BMO build proved why: the previous continuation brief named only RBC and Rogers as the Canadian exclusions, and a second independent screen found **CIBC and TD Bank Group are also customers**. Three of Canada's Big Five. A brief's exclusion list is a starting point, never the answer.

For TELUS specifically:
- **Rogers Communications Canada IS a customer.** Never named. This matters more here than it did on BMO, because Rogers is TELUS's direct competitor and is exactly the comparison a rep reaches for.
- **Bell is NOT a customer** — but Bell is a live prospect with its own strike room built the same day. Do not name it either; the two documents should not cross-reference each other.
- Charter Communications, AT&T Enterprise Group, Cox Enterprises and Liberty Global are all customers in Technology & Communications. None may be named.

### 2. Claims discipline — this changed on July 21 and the change is load-bearing

**The Value Repository is FROZEN as a prospect-facing source** as of July 21 2026 (Matt Graves, Director CSM, with Naveen). The reason: Matt confirmed the Zuar savings model is an internal averaged model that customers "will call us on" if it appears customer-facing, and financial-services buyers reject projected-value framing almost every time.

**The entire cleared-to-ship allowlist is three items:**

1. The Humana webinar claims
2. Public CMS Star Ratings math, always with the estimate label
3. The Dynamic Workforce Orchestration positioning statement

Nothing else. All per-account CTO, Zuar/Greenlight savings, whitespace and maturity data is internal targeting only.

**Customer-naming gate (new).** No customer may be named in prospect copy until cleared against **Jenna (Contracts)** and **Cheryl (Marketing)**. Default to category-level framing. **Humana is the sole confirmed exception.** Named use of anyone else, including JPMorgan Chase, is prohibited.

**Outstanding correction:** the Bell Canada document licensed two figures — a platform headcount figure (~350,000 contact centre professionals) and a 2025 net-retention percentage (above 114%) — that **are not in the Value Repository in any version**. Verified against both the working copy and the July 29 2026 export. Do not use either in TELUS. Flag to Dallas that Bell still needs them struck before it sends.

### 3. Live research — spawn a subagent, it takes about seven minutes

Your training data is stale for a July 2026 build. Demand a source URL and a date on every figure, and split company-disclosed (usable in copy) from third-party estimate (not usable). The BMO subagent ran 30+ queries and found three things this brief did not have; assume the same is true here.

Push the subagent specifically on: what Dodig and Chande actually said on the Q2 call once it happens, the exact scope of the July 22 reorganisation, TELUS's own disclosures about contact-centre operations, and anything that would make outreach tone-deaf in the last 60 days.

### 4. Committee sourcing via Clay MCP — verify the entity before spending a credit

`find-and-enrich-contacts-at-company` with an `Email` contact data point. Two searches: customer-experience/contact-centre titles, and operations/finance titles. Target eight seats across five tiers.

**Read the returned `companies` object before you read the contact list.** Check `domain`, `locality`, `employee_count`, `country`. BMO cost five searches instead of two because `bmo.com` resolves to BMO **U.S.** (Chicago, 11,632) rather than the Toronto parent (60,903), and `linkedin.com/company/bmo` resolves to an unrelated **Austrian HR consultancy** that returned five plausible-looking "BMO" contacts with Canadian locations. Only the company object revealed it.

TELUS has the same shape of trap and worse: **TELUS Corporation, TELUS Digital (formerly TELUS International) and TELUS Health are different entities.** TELUS Digital is the commercial BPO/CX-services arm and its people are sell-side, not internal operations. That is this account's version of the Bell reseller problem, and it is bigger. Confirm which entity every contact actually sits in.

**Cross-check every enriched email against the LinkedIn identity.** Two BMO contacts returned emails whose surname did not match the profile slug and were dropped rather than guessed.

### 5. ZeroBounce sweep BEFORE drafting any copy

Not optional. Workbook `OneOff_ZB_Sweep_Jul29` already exists with two tables (`Bell_Committee_ZB`, `BMO_Committee_ZB`). **Add a third table** rather than a new workbook.

Sequence that works:
1. Chrome to `app.clay.com`, open the workbook, bottom bar `+ Add` → **Blank table**, name it `TELUS_Committee_ZB`.
2. **Take a fresh screenshot after clicking `+ Add`.** The dialog opens but the first screenshot comes back stale showing the old page. It is there; re-screenshot.
3. Set the row-count box next to `+ Add` to (seats − 1), click `+ Add`.
4. Type each email cell by cell: double-click → **wait 1 second** → type → wait 1s → Return. Without the wait the cell editor has not mounted and the text silently vanishes. Batches of four rows per `browser_batch` work reliably. Never paste multiple addresses with newlines; it merges cells.
5. `Add column` → `Add enrichment` → search `zerobounce` → `Validate Email`. The email column auto-maps.
6. `Continue to add fields` → toggle **Status** and **Sub Status** → `Save` chevron → "Save and run N rows in this view."
7. Read the page: "100% of table completed", and read the Status column verbatim before reporting anything.

Sweep two bench addresses alongside the sequenced seats. Costs 0.2 extra and means a ZB failure on a primary does not require a second billable pass. Cost is 0.1/row; Bell was 0.7, BMO was 0.8. Log it to `Clay_Credit_Ledger.md`.

### 6. Draft, gate, PDF, verify

**The tooling now exists — do not rebuild it.** In `strike-room-kit/` at project root:

- `build_strikeroom_pdf.py` — generalised builder, proven on Bell and BMO. Edit only the CONFIG block at the top. **Ignore `build_pdf_TEMPLATE.py`**, which is hard-wired to the Aflac structure and crashes on this document shape.
- `kit.css` / `kit_cover.css` — extracted green-kit styling, includes list and code-span rules the old template lacked.
- `quality_gate.py` — run as `python3 quality_gate.py <packet>.md`
- `merge_and_stamp.py` — `python3 merge_and_stamp.py TELUS Output.pdf`
- `VERIFY_RENDER.py` — `python3 VERIFY_RENDER.py Output.pdf 1 12 16`

Full run: stage the kit, copy out of the read-only uploads dir, then
`python3 build_strikeroom_pdf.py && python3 render.py && python3 merge_and_stamp.py TELUS CostMandate_TELUS_StrikeRoom_Sequence_v1.pdf`

**Two bugs are fixed in the script. Do not reintroduce them:** the touch label must use the literal `·` character with no Python `.upper()` (CSS does the uppercasing — the old code produced `&MIDDOT;` as visible text), and the Hook line needs its first letter capitalised explicitly. Both were invisible in the HTML and obvious in a render.

**Always render two or three pages to PNG and actually look at them before shipping.**

### 7. The quality gate finds real things — trust check 7 over the rest

On Bell it caught three defects after the copy felt finished. On BMO the word counts and banned-word scans found **nothing**, and the template-creep check (item 7) found three real defects: six of seven Touch-1 emails closing on a near-identical product paragraph, two seats ending on the same hail-mary, and the same statistic framed identically across two seats who sit adjacent on the org chart.

If your gate reports zero problems, be suspicious of the gate before you believe the copy. Also note the gate's first run will report false positives if you scope it wrong — em-dashes must be counted in prose only (structural markdown is the house convention), and a contact's last touch block will swallow the following section unless you bound it. Both are already handled in `quality_gate.py`.

## Account-specific research from the July 29 sweep

Treat all of this as a starting point to verify, not as fact. It was gathered before the Q2 call.

**Forcing function.** A brand-new CEO (Victor Dodig) and CFO (Gopi Chande), both effective July 1 2026, reorganised the whole telecom business on July 22 2026 under a mandate to both "improve how we serve our customers" and realise "operational efficiencies" — after cutting 2,800 Canadian jobs in 2025 and posting a 78% increase in CCTS complaints, the worst of the big three.

**The structural objection.** TELUS Digital sells contact-centre AI services commercially, including a Cresta partnership announced June 15 2026. "We do this ourselves" is structural here, not incidental. It must be answered in the copy rather than avoided, and it is the reason the entity-resolution work in step 4 is not optional.

**Useful borrowed language.** TELUS Digital's own June 2026 research found only 32% of enterprises have the automated quality assurance and coaching tools needed for feedback loops. They diagnosed the gap themselves — that is a far better wedge than anything we could assert.

**Do not cite Unifor.** The union at TELUS is **USW Local 1944**. Unifor represents Bell workers. Getting this wrong in a message to a TELUS operations executive ends the conversation.

**Verint Workforce Engagement** was deployed across roughly 30,000 TELUS International team members, but that announcement is from **May 2021** and post-privatization status is unconfirmed. Treat the WFM stack as a discovery question. Note that on BMO the equivalent Verint evidence turned out to be a decade stale — check the date on anything Verint-related before believing it.

**Clock.** Q2 2026 will be Dodig's and Chande's first call, expected August — **confirm the exact date from TELUS investor relations early, because the whole build plan pivots on it.** Fuller starts September 1. Target launch the week of September 8. Build the sequence to go dark around the earnings date the way BMO's does around August 25.

## Standing laws

- One-off account strategy. Never goes into a Clay motion workbook.
- Every voicemail has a live-answer script behind it, in case they pick up.
- No idle-time percentage, no efficiency statistic of Intradiem's own, no modelled ROI for the account.
- The Humana proof (7X ROI five years in, ~2 hours of capacity per agent per month, 2.7M automated actions in 2025) is **replies and objection handling only, never a cold touch.**
- At most one humility clause across the entire committee.
- Deliver both the plain `.md` and the branded green-kit PDF, and commit both to project root via `device_commit_files`.
- Green kit only: forest `#16432C`, green, lime, Playfair Display, DM Sans, JetBrains Mono, orange `#FE5000` as an eyebrow spark only. Never the orange/Outfit system in `claude-design-handoff/02_BRAND_intradiem.md`, which is retired. Never rebuild the logo in CSS; use the production asset.
- Update `Clay_Credit_Ledger.md` and project memory before you finish.
- **Nothing sends.** Every output stops at the human approval gate.

## What "done" looks like for this session

1. Bell's guardrail bullet struck and its PDF rebuilt (five minutes, do it first).
2. TELUS committee sourced, entity-verified, ZeroBounce swept, logged to the ledger.
3. Full packet built with the forcing-function paragraph and the finance/exec Touch 1 and Touch 4 marked `[PENDING Q2 CALL]`.
4. Quality gate passing, including check 7.
5. PDF rendered, two or three pages actually looked at, both files committed to project root.
6. A one-line note to Dallas stating the confirmed Q2 earnings date and the resulting launch week.

The packet is not finished this session, and that is the plan rather than a shortfall. It is finished the morning after the Q2 call, in a session that should take under an hour because everything else is already standing.

**Nothing sends.** Every output stops at the human approval gate.
