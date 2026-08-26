# Continuation prompt — BMO and TELUS strike rooms

Paste this into a fresh session in the Intradiem GTM Engineer project. Bell Canada is done; these are accounts 2 and 3 of Nathan Belfield's July 29, 2026 request. Run one per session.

---

## The prompt

> Nathan Belfield asked on July 29, 2026 for Strike Rooms on BMO (Bank of Montreal), TELUS, and Bell Canada. Bell Canada is complete (`CostMandate_BellCanada_StrikeRoom_Sequence_v1.md` and `.pdf` at project root). Build **[BMO / TELUS]** next, to the same standard.
>
> Load `intradiem-strike-sequence` FIRST, plus its chain: `intradiem-verified-metrics`, `intradiem-first-draft-engine`, `intradiem-copy-sharpener`. Then follow the build order below.

---

## Build order (proven on Bell, Jul 29)

1. **Customer-exclusion gate.** Screen against `greenlight-pack/Active_Customers_SF_Jul10.csv`. Already run for all three: **BMO, TELUS and Bell are all absent, so all three are clean for new-logo.** Royal Bank of Canada and Rogers Communications Canada ARE customers, so neither may be named in any Canadian-account copy.
2. **Live research.** Your training data is stale for a July 2026 build. Web-search and fetch everything, and demand a source URL plus a date on every figure. Separate company-disclosed figures (usable in copy) from third-party estimates (not usable). Spawn a research subagent per account; it takes about seven minutes and returns a full forcing-function brief.
3. **Committee sourcing via Clay MCP.** `find-and-enrich-contacts-at-company` on the corporate domain with an `Email` contact data point. Run two searches, one for customer-experience and contact-centre titles and one for operations and finance titles, then poll `get-task-context` for the email waterfall results. Target eight seats across the five tiers. Exclude sell-side titles: at Bell, "Contact Center Solutions Specialist" and similar were the company's own reseller organization, not its internal operations.
4. **ZeroBounce sweep BEFORE drafting any copy.** This is the enrichment law and it is not optional.
5. **Draft**, then **PDF**, then **verify**.

---

## ZeroBounce mechanics (updated Jul 29, this corrects the older note)

The old scratch table `OneOff_CardinalHealth_ZB_Jul15` **no longer exists** in the workspace. A fresh one was created on Jul 29: workbook `OneOff_ZB_Sweep_Jul29`, table `Bell_Committee_ZB`. Add a new table in that workbook for each account rather than creating a new workbook each time.

**An agent CAN create Clay workbooks and tables through the Chrome UI.** The older memory note saying agents cannot create tables refers to the API and MCP surfaces only. Via Chrome: `+ New` → `Workbook` → `Blank table`.

Sequence that works:

1. Chrome to `app.clay.com`, open the workbook, add a blank table, name it.
2. Set the row-count box next to `+ Add` to (seats − 1), click `+ Add`.
3. **Type each email cell by cell, and put a 1-second wait between the double-click and the typing.** Without the wait the cell editor has not mounted and the text silently goes nowhere. This is the single biggest time-waster in the whole flow. Batching double-click → wait 1s → type → wait 1s → Return works reliably in `browser_batch`. Never paste multiple addresses with newlines; it merges cells.
4. `Add column` → `Add enrichment` → search `zerobounce` → `Validate Email` (ZeroBounce, 0.1/row). The email column auto-maps.
5. `Continue to add fields` → toggle **Status** and **Sub Status** → `Save` chevron → **Save and run N rows in this view**.
6. Confirm on the page: "100% of table completed", and read the Status column verbatim before reporting anything.

Cost: 0.1 credits per row. Bell was 0.7 for seven addresses. Log it to `Clay_Credit_Ledger.md`.

---

## PDF pipeline

`strike-room-kit/` at project root. Stage it, copy out of the read-only uploads directory, then:

- The stock `build_pdf_TEMPLATE.py` is hard-wired to the Aflac markdown structure. **A generalized build script that matches the Bell document structure exists and is the better starting point.** It splits on `---`, handles `###` subheads, bullet and numbered lists, and blockquotes, and detects live-answer scripts by the label containing "Live-answer", "full script" or "Call #".
- Two bugs were found and fixed on Jul 29, do not reintroduce them:
  - The touch label runs `.upper()` last, which turns `&middot;` into `&MIDDOT;` and prints it literally. Use the actual `·` character, not the HTML entity.
  - The Hook line needs its first letter capitalized explicitly; the markdown starts it lowercase after `Hook:`.
- Run `python3 <build>.py && python3 render.py`, then merge cover and body with pypdf and stamp page numbers with reportlab per the kit README.
- **Always render two or three pages to PNG and actually look at them** before shipping. Both bugs above were invisible in the HTML and obvious in the render.

---

## Quality gate (run it programmatically, it catches real things)

On Bell this caught three genuine defects after the copy felt finished:

- **Humility clause used twice.** Spec is at most once across the whole committee. Grep for it.
- **Two cold emails over the 80-120 word ceiling** (136 and 129).
- **One voicemail under the 45-word floor.**

Script the checks: banned-word scan, humility count, subject-line uniqueness (breakups all sharing "leaving it here" is correct and expected), Touch-1 word counts 80-120, voicemail 45-70, LinkedIn 40-80, em-dash count zero.

---

## Account-specific notes from the Jul 29 research

### BMO (Bank of Montreal)

- **Forcing function:** $202M pre-tax severance in Q1 FY2026 bought approximately **$250M in annualized savings, half to be realized in FY2026 and the rest in 2027** (CFO Rahul Nalgirkar, Feb 25 2026; reaffirmed by CEO Darryl White, May 27 2026). The savings are booked and the execution is not.
- **Best stack wedge:** BMO's **"Call Assist"** won Best Agent-Assist/Copilot Deployment for Contact Centre in May 2026. They have already bought into real-time help *during* the call. The adjacent thing they have not solved is the time *between* contacts, and the back office. **"SAFE"** is their back-office document automation, further proof they are already spending here.
- **Second wedge:** FCAC imposed a **$4,000,000 penalty announced Feb 2, 2026** for failing to disclose charges on personal deposit accounts, **101,091 customers affected**, 2010 to 2024. That is a frontline process-adherence and oversight failure, not a policy one. Pair it with their own Customer Complaint Appeal Office report: the largest complaint category "related to customer frustration with earlier stages of the complaint handling process."
- **Targeting read:** a June 2025 reorg split North American Personal & Business Banking into a co-head structure. **Mat Mehrotra** (client-facing retail) and **Sharon Haward-Laird** (shared services and operations) are both about twelve months in seat, and neither owns a legacy stack decision. CFO Nalgirkar is roughly seven months in and personally owns the $250M. **Steve Tennyson** is Chief Technology & Operations Officer.
- **Clock:** Q3 FY2026 reports **August 25, 2026**.
- **Unverified, do not use:** contact-centre headcount, locations, call volumes, WFM vendor, CCaaS platform. None are disclosed. The Verint deployment reference found in search is roughly two decades old.

### TELUS

- **Forcing function:** a brand-new CEO (**Victor Dodig**) and CFO (**Gopi Chande**), both effective **July 1, 2026**, reorganized the whole telecom business on **July 22, 2026** under a mandate to both "improve how we serve our customers" and realize "operational efficiencies", after cutting **2,800 Canadian jobs in 2025** and posting a **78% increase in CCTS complaints**, the worst of the big three.
- **Why it was not chosen first:** TELUS Digital sells contact-centre AI services commercially, including a Cresta partnership announced June 15 2026, so the "we do this ourselves" objection is structural rather than incidental. And **David Fuller**, who will own the consolidated telecom P&L, does not start until **September 1, 2026**. Sequencing into a seat that is not occupied yet is a real problem.
- **How to handle that:** either wait for Fuller and enter early September, or sequence the layer beneath him now and let the timing work in your favour, since a new leader arriving to an operation that has already been thinking about this is a friendlier landing. Worth putting to Dallas as a question rather than deciding silently.
- **Useful borrowed language:** TELUS Digital's own June 2026 research found only **32% of enterprises have the automated quality assurance and coaching tools needed for feedback loops**. They diagnosed the gap themselves.
- **Do not cite Unifor.** The union at TELUS is **USW Local 1944**. Unifor represents Bell workers, not TELUS.
- **Verint Workforce Engagement** was deployed across roughly 30,000 TELUS International team members, but that announcement is from **May 2021** and post-privatization status is unconfirmed.
- **Clock:** Q2 2026 will be Dodig's and Chande's first call, expected August.

---

## Standing laws that applied to Bell and apply to these

- One-off account strategy. **Never** goes into a Clay motion workbook.
- Every voicemail has a live-answer script behind it, in case they pick up.
- No idle-time percentage, no efficiency statistic, no modelled ROI for the account.
- Humana proof (7X ROI, ~2 hours per agent per month) is replies and objection handling only, never a cold touch.
- Deliver **both** the plain `.md` and the branded green-kit PDF.
- Green kit only: forest `#16432C`, green, lime, Playfair Display, DM Sans, JetBrains Mono, orange `#FE5000` as an eyebrow spark only. Never the orange/Outfit system in `claude-design-handoff/02_BRAND_intradiem.md`, which is retired. Never rebuild the logo in CSS; use the production asset.
- Nothing sends. Every output stops at the human approval gate.
