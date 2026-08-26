# Copy-paste prompt for a new thread (Opus fallback) — Belfield strike rooms

Paste everything below the line into a fresh conversation in the Intradiem GTM Engineer project.

---

You're picking up a live workstream in this project: Nathan Belfield's 12-account strike-room list. Accounts 1-2 (Blue Shield of CA, Aflac) are done and set the quality bar. You continue with the exact same standards. Do these before anything else, in order:

1. Read project memory: `belfield-12-accounts-jul16`, `enrichment-laws-jul16`, `oneoff-accounts-stay-out-of-workbooks`, `strike-work-loads-strike-sequence-skill`, `no-aiisms-house-style`.
2. Read the tracker, the source of truth: `/Users/dallasandrews/Desktop/outputs/Belfield_Accounts_Tracker.md`.
3. Read ONE finished packet at the project root as the format bar: `StarRatings_BlueShieldCA_StrikeRoom_Sequence_v1.md` (Stars motion example) or `CostMandate_Aflac_StrikeRoom_Sequence_v1.md` (cost-mandate example). Match its structure and energy exactly.

Then build the next "Not started" account. Default order: GM Financial, T-Mobile, CapOne, Fidelity, Morgan Stanley, Walmart, National Grid, Avangrid, Lumen Technologies, IKEA. One account per conversation unless I say otherwise.

Build order per account. No skipping, no reordering:

1. Load the `intradiem-strike-sequence` skill FIRST and follow its gates, tiers, cadence, and copy standards. Run `intradiem-verified-metrics`, `intradiem-first-draft-engine`, and `intradiem-copy-sharpener` thinking on every message.
2. Customer-exclusion gate: check the account against `greenlight-pack/Active_Customers_SF_Jul10.csv` in the project folder (stage it via the device tools). Non-customer, proceed new-logo. Customer match, stop and tell me.
3. Pick the motion. Healthcare payer with Medicare Advantage contracts: Star Ratings (pull their contracts from `StarRatings_Targets_2026_Tiered.csv`; star-level precision and count-safe rules apply). Everything else: cost-mandate. If no layoff or cost event exists, run the SOFT variant like Aflac: pressure framed only from the prospect's own disclosed numbers (earnings calls, releases, WARN filings), never manufactured urgency. No idle-percentage stats, ever.
4. Research: prospect-disclosed and public facts only, every figure attributed and dated in the snapshot table.
5. Committee: 8 seats across the 5 tiers via Clay MCP contact searches (free), 2 must-win seats flagged for the extended arc. Bench the rest.
6. FULL enrichment BEFORE any drafting, through Clay ONLY (never Apollo, that's my free personal account): email waterfall via `find-and-enrich-list-of-contacts`; any miss gets a Custom deep-find datapoint retry via `add-contact-data-points`.
7. ZeroBounce sweep BEFORE any drafting, run by you via Claude-in-Chrome: open the Clay workbook `OneOff_CardinalHealth_ZB_Jul15`, Custom Table. Add rows with the Add-N control at the bottom. Type each email cell-by-cell (double-click, type, Return; never batch-type with newlines). The ZeroBounce column auto-runs on new rows at 0.1 credits/row. Read Status and Sub Status live off the page and bake them into the committee table. Note: blueshieldca.com-style catch-all domains return valid + catch_all; that's a report-it fact, not a blocker.
8. Write the .md packet matching the reference format: forcing function, one thesis, snapshot table with sources, committee table with ZB statuses, say/don't-say, cadence and staggered entry, full five-touch sequences per contact with a live-answer script behind EVERY voicemail (extended arc adds live call 1, live call 2, pattern interrupt, hail-mary breakup, in that order), objection quick-handles, claims basis, execution notes. Copy laws: no em dashes in message bodies; no AI-isms or banned words (including "compare notes"); all subjects unique; all CTAs different and payoff-naming; cold emails 80-120 words, follow-ups 100-150, LinkedIn 40-80, voicemails 45-70; `{{sender}}` tokens; humility clause at most once and only on a Stars-motion contract-owning seat; Humana is the ONLY customer proof, replies-only, as Humana told it publicly. Nothing not in the Value Repository ships as an Intradiem claim.
9. Response simulation: read every message AS that specific recipient on a busy Tuesday and ask only "would I reply?" "It's fine" is a no. Rewrite through the first-draft engine until you'd reply.
10. Branded PDF: stage `strike-room-kit/` from the project folder into the workspace (uploads is read-only, copy it out), follow its README, edit the template's marked per-account fields, run it. Green kit only, real logo, never fabricate the logo in CSS.
11. Ship, all in the same turn: SendUserFile the .md and .pdf, commit both to the project root via device_commit_files, set the account to "Dallas review" in the tracker (Desktop/outputs) with a log line, append the credit entry to `Clay_Credit_Ledger.md` at the project root (searches free; waterfall est ~12-20/account; ZB 0.1/row; meter-confirm pending), and update the `belfield-12-accounts-jul16` memory file.

Hard rules: one-off account work never lands in a Clay motion workbook (the doc and the scratch table are its only homes). Nothing sends to a prospect from you, ever; every output stops at my review. If a gate can't pass (customer match, no honest forcing function, enrichment dead-ends), stop and tell me exactly where and why rather than shipping around it.
