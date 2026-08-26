# Keegan Attainment Engine, v1 (Aug 3 2026)

The end-to-end plan to make the GTM engine the number one source of Keegan Sanders's pipeline number: **8,400 seats added to pipeline this calendar year, roughly $3.3M** (his figures from the Aug 3 sync; the ~$393/seat implied rate is derived, not his quote).

## The math

8,400 seats over the remaining calendar is roughly **one 700-seat opportunity a month**, or fewer, bigger ones. Citizens or The Hartford sized wins cover multiple months each. Every account decision below is measured in seats: an account only earns blitz priority if its agent plus back-office headcount can actually move the number. Seats are the north star Keegan tracks, so seats are what the engine reports.

## What Keegan told us (ground truth from the Aug 3 call)

- **His number:** 8,400 seats to backfill pipeline for the calendar year, ~$3.3M. Seat count is how he sizes accounts ("how many agents do you support" is a normal first-call question).
- **His conviction:** warm beats cold 10x. The former-customer report is his most underutilized asset: **264 contacts, Director to C-level, in his TAM**, in contact center, customer service, and WFM roles, all with prior Intradiem (or Knowlagent-era) experience.
- **First two blitz accounts, his picks:** **Citizens** and **The Hartford**. Citizens gets contacted inside 48 hours (committed on the call).
- **His discovery question that lands:** "You're sitting on a mountain of real-time insights, but you're still throwing it at your team to act on. What are you doing to act on it in real time? What if you could unload 30 to 70% of that work?"
- **His analogy that lands:** Intradiem is the airport's air traffic controller, but automating the actions. A contracts person called him back to say it was the clearest explanation they'd heard.
- **His working style:** doesn't micromanage, happy to share non-Slack tribal knowledge before any account touch, wants Dallas in the Thursday 8:30am CT weekly sync.

## The four lanes

### Lane 1: Alumni motion (the 264)
The highest-conversion lane and the seed for everything else. Keegan owns cleaning the Sales Nav list (adding customers won since it was built) and sharing it; Nate is backup relay Tue/Wed Aug 4-5. Sales Nav has no export, so extraction is screenshots, 25 at a time, then Claude does the parsing.

Once the list lands:
1. Extract all 264 into `motions/keegan/alumni/Keegan_Alumni_264.csv` (name, title, account, former customer employer, level).
2. Enrich in Clay (check existing workflows first per standing rule; prefer extending an existing enrichment function).
3. Score and rank **by account**, not by contact: alumni density x estimated seat count x role power (SVP/C > VP > Director) x vertical fit x signal recency. Keegan's own hypothesis: Hartford with 10 alumni beats Vanguard with 2. The scorer proves or corrects that.
4. Deliver the ranked pecking order to Keegan before Thursday's sync. This was promised as fast turnaround on the call; make it same-day when the list arrives.

The angle for this lane: lead with their own history. "You saw this work at Charter / Cox" beats any cold claim. Note: alumni from 15+ years ago knew the company as **Knowlagent**; the name may be the recognition hook, use it deliberately.

### Lane 2: Rolling two-account blitz engine
Two accounts in flight at all times, 10-day multi-channel blitz each (email, call, voicemail, LinkedIn DM and voice note), 3 to 8 buying-committee members per account, from strategy owner down to the person living in the fire. As one account's 10 days complete, the next ranked account enters. That's roughly 4 accounts a month under sustained pressure, every one of them seat-qualified.

**Now:** Citizens first (48-hour commitment), Hartford immediately after.

- **Citizens:** Jeffrey Foss, SVP Contact Center Operations, was a senior business sponsor at Charter (current customer, good ongoing success) and knows Ted Lango. This is a warm re-entry, not cold outreach. Gate check before any Charter claim reaches him: Charter results are customer-sourced value, verify tier in the Value Repository / Customer Value Registry before citing.
- **The Hartford:** finance vertical (Keegan and Nate's top vertical read), recent Six Sense activity, multiple alumni including a former Cox Automotive assistant director of workforce management and operational modeling. Nate also flagged M&T Bank and CardWorks as bench.
- **Bench (next up, pending Lane 1 ranking):** Vanguard (4 recent website visits), M&T Bank, CardWorks, Republic Services.

### Lane 3: Signal layer on Keegan's TAM
Nate's CSV of Keegan's accounts is in hand (received Aug 3). Next:
1. Load it as a named watchlist the daily war room sweeps (earnings, cost mandates, outages, WFM/ACD/CCaaS stack moves, leadership changes).
2. Cross-reference against the **98-payer Stars universe**: any healthcare account in Keegan's TAM that's already in the Stars motion gets the Stars attack plan, and gets deduped so nobody is double-touched by two motions.
3. Website-visit and Six Sense spikes jump the line for the next blitz slot (Vanguard's 4 visits is the template case).
4. The new **alumni-champion-watch** agent (built today) watches the alumni roster weekly for job changes. The Citizens pattern, a former sponsor landing as an SVP in TAM, is exactly the event it exists to catch, and it catches the next one automatically instead of Keegan stumbling on it in a report.

### Lane 4: The seat ledger, keeping score
`motions/keegan/Keegan_Seat_Ledger.md` tracks every account the engine touches: estimated seats, stage (queued / in blitz / replied / meeting / opp), and seats surfaced vs seats realized, never blended. It answers "how far toward 8,400" at any moment, feeds the Wednesday one-pager, the Thursday sync, and the Friday Naveen readout. When the engine's fingerprints are on a meeting, the ledger says so with receipts.

## The message every account hears (feeds MessageGen / first-draft engine as Keegan-motion slots)

One story every contact at an account hears, from their own angle:
- **The problem:** you already have the real-time insight (your ACD, your AI stack); a human still has to act on it, usually via an end-of-day report.
- **The picture:** the air traffic controller that also moves the planes. Automate the action, not just the insight.
- **The question:** what are you doing to act on it in real time?

Alumni variant adds the personal layer: they've already seen it work. All copy passes first-draft engine, then copy-sharpener, then the verified-claims gate. No exceptions for warm contacts; warm is where a sloppy claim costs the most.

## Week-to-week rhythm with Keegan

- **Thursday 8:30am CT weekly sync:** Dallas attends. Bring one page, not a deck.
- **Sync prep, not a separate post:** Wednesday's regular daily brief carries a short "before tomorrow's sync" section: blitz status per account, replies and meetings, seat ledger position, next two accounts entering, the one thing needed from Keegan. First one Wed Aug 5. Channel rule: no post exists that isn't someone's cue to act; show the rhythm, don't announce it.
- **Slack:** Keegan joins the GTM Outbound Nathan channel (Dallas adds him) and catches up on the daily blitz there. No new DM streams; the single-morning-brief rule stands.
- **Before any account launches:** one ping to Keegan for tribal knowledge (he offered; use it every time).
- **When a meeting books:** pre-call one-pager in his hands the day before (committed on the call as an experiment; iterate on his feedback).

## Gates, standing, never skipped

1. **Customer exclusion** on every load (Charter is a customer; Citizens and Hartford are not; verify at load time, on real rows, before any wave).
2. **Verified claims** on every number, hardest on Charter-sourced proof aimed at Foss.
3. **Dry-run default**; no send gate flips without Dallas's explicit ask.
4. **Dedupe across motions** so a Keegan account never gets hit by Stars and the blitz in the same window.

## This week, in order (traps called out)

1. **Today:** Add Keegan to the Slack channel. Fire the Citizens strike-sequence build (the 48-hour clock is running). Hold Hartford until Citizens copy is done, then fire Hartford, same session pattern.
2. **Today, blocked but cheap:** verify work email on LinkedIn so Keegan can share the Sales Nav list directly (transcript blocker; screenshots path works regardless via Nate).
3. **Today or tomorrow (CSV already in hand):** ingest the TAM, run the Stars overlap dedupe FIRST, then register the war-room watchlist. Trap: registering the watchlist before deduping risks two motions firing on one account.
4. **Tue/Wed, when the alumni list lands:** extract, enrich, rank, deliver the pecking order same day. Trap: don't run the ranking until Keegan's updated version arrives; the stale list is missing newly won customers and will misrank.
5. **Wed night:** first one-pager. **Thu 8:30 CT:** first sync, walk the ranked list and the Citizens blitz live in channel.

## How we'll know it's working

- Every meeting sourced through these lanes lands in the ledger with seats attached, surfaced vs realized kept separate.
- Quarter one of this motion (through Oct): Citizens and Hartford blitzes complete, alumni ranking driving the queue, at least the first engine-sourced meetings on the board and attributed cleanly.
- The year: the ledger, not memory, shows what share of 8,400 came through the engine.
