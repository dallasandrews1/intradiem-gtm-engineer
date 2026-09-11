# Recording sheet, click by click (v3)

> Seven screens, one browser window per act, your narration in every take. Rewritten Sep 4 2026 for `Demo_Recording_Script.md` v3. Every id below was read from the live workspaces on Sep 1 and Sep 2. Labels in `code` come from the tools' current docs; anything marked **(confirm)** you read off the screen. If a screen differs from a step, stop and tell me what you see; don't improvise a click.

## Windows, one per act

Open only the tabs for the act you're recording. Close the window when the take is done and open the next.

| Act | Window | Tabs, left to right |
|---|---|---|
| 1 | Cowork (or the terminal if you record there) | the finished strike-plan thread for B; a fresh empty thread for A; font large |
| 2 | Browser | (a) Clay Audiences People https://app.clay.com/workspaces/1180800 · (b) Clay table `Contacts (Buying Committee)`, view "All-hands demo", workbook Star Ratings, t_0thtm73HHxyiupTuepK · (c) https://backoffice-maps.pages.dev · (d) https://icp-committees.pages.dev |
| 3 | Browser | lemlist, campaign "All hands demo - recording" |
| Coda | Browser | https://gtm-partner-pilot.pages.dev/briefs/ally |

Browser at 125 percent, bookmarks bar hidden, Do Not Disturb on, every other window closed.

## Recording set-up (once)

1. QuickTime Player, File > New Screen Recording. In the toolbar pick **Record Selected Portion** and drag the frame over the browser window (or the terminal for act 1), leaving room beside it. Options: choose the built-in mic; turn on **Show Mouse Clicks** (**confirm** the option name).
2. Put the script beside the frame, outside it: a Preview window with the script, a second screen, or an iPad. Glance, don't read.
3. iMovie, new project. Import the four title cards from `title_cards/` (01_act1, 02_act2, 03_act3, 04_coda), 1920x1080. Add the takes as they land. Order: act 1 card, take 1, act 2 card, take 2a (Audiences), the enrichment clip, take 2b (maps and committee), act 3 card, take 3, coda card, coda take. Export 1080p with audio.

## Before any recording (in this order)

1. **Act 3 campaign.** "All hands demo - recording" (cam_WaDLXcAtit6auc8ay, draft, 11 leads, built Sep 5) is the act 3 tab; its sequence and every lead's variables were read Sep 5 and are clean. This is your own copy. Jack's original ("All hands demo", cam_SxnHzvAr3WsvWPPeY) stays untouched and is not the recording tab. Stars - Resurrection is not needed.
2. **Strike plan ahead of time run: done Sep 5** in a Cowork thread. That thread's finished output is recording B; keep it open.
3. **Act 2 demo view** (step 2.0) so the gate and sync columns are off screen.
4. **Contact center platforms column** added to the demo view first (`Tech_Stack_Column_UISheet_Sep5.md`), then the **act 2 enrichment clip** (step 2.3): a separate screen recording made ahead of time, no narration needed while it records, you talk over it in iMovie or at the end of take 2a. About 20 credits.
5. **Act 2 counts** re-read the morning you record (Salesforce sync moves them). Live Sep 4: 312 in the segment, 140,993 people.

---

## Act 1 · Strike rooms (about 1:05 of tape, one take)

### 1.1 Claude Code, the strike plan (Screen 1, 55 seconds, two recordings)
**ahead of time run, done Sep 5 (Cowork thread, the long prompt):** fit 82, tier 1, D-SNP expansion trigger, nine-person committee, five touches each, Humana figures checked against the Value Repository, no dollar or owner lines. That thread is recording B. Two lines to scroll past without pausing: the exclusion-list line near the top (customer names) and the "Status: human approval gate not yet cleared" line in the header.

**Recording A (the ask, 15 seconds), after B:** a brand new thread, empty. Start recording, two seconds of still, say the problem line, type `Build the strike plan for AmeriHealth Caritas.`, Enter, let it start working for ten to fifteen seconds, stop. Then stop that run; its output isn't needed.

**Recording B (the result, 40 seconds):** the Cowork thread, output scrolled to the top of "Fit score and tier". Start recording, scroll at reading pace: fit score, the trigger, the buying committee table, the "What reps can and cannot say" block (hold 3 seconds, that's the checkpoint), then Scott Mullaney's block with the Day 1 email, the Day 2 LinkedIn note and the Day 4 voicemail. Say the outcome line. Hold 3 seconds. Stop.

In iMovie, A then B, straight cut. The 2x ramp is not needed.

What NOT to show: any dollar or ROI line, the Owner line, any `[UNVERIFIED]` tag, the EXCLUDED line at the bottom of the ranking, any file path.

---

## Act 2 · Back office, inside our customers (about 2:30 of tape, two takes and a clip)

### 2.1 Clay Audiences, one count (Screen 2, 20 seconds, take 2a)
Live counts read Sep 2:
- `BO Leaders (customers, Dir+)` (audseg_0tk324gWiTQKCqVz4tx): **312**
- `BO Leaders (prospects, Dir+)` (audseg_0tk324ghMPTbzvR8pGK): **1,523** (not on screen in v3; keep in your head for the room)
- Insurance-only alternative: `BO Insurance Titles - Customers` (audseg_0tk8rc0Kc2YeAJXC7uq) **17**. The bigger segment reads better on a projector.

1. Tab (a). Left sidebar, click **Audiences**. Top of the page, click the `People` tab. The count should read about **140,800**. Hold 2 seconds while you say the first line.
2. Open **`BO Leaders (customers, Dir+)`**. Let the count land (~312). Hold 3 seconds on the number. Say the rest.
3. Don't open the filter panel. Don't open a person record. Stop the take here; the enrichment clip goes next in iMovie.

What NOT to show: `Cold-Outbound Exclusion`, `Account Type Missing`, `Heat *`, `SF Activity *`, `JC Watch *` segments.

### 2.3b What to say about the posts cell and where the data goes

The posts cell is the moment the room most needs a "so what", because `✅ 3 posts or shares found` means nothing on its own. The verified chain behind it, read from the live column settings on Sep 4:

1. `Get a person's professional posts and shares` pulls their last three LinkedIn posts into the row, with the text and the date.
2. `li_recent_post_hook` reads those posts and tries to write one opening line, but only when the post is under 30 days old and actually about Stars, CAHPS, member experience or contact-center operations. Otherwise it returns nothing.
3. The hook, when it exists, is what the engine opens the first email on. When it is empty, the email opens on the account's numbers instead. (The Clay `MessageGen Email` column that used to consume it is retired as of Sep 5; the engine writes the copy Claude-side. Do not run it.)

On all five demo rows the hook is empty, because the newest posts are months old and about volunteering and hiring. That is the guardrail working, and it is a better story than a filled cell.

**Say roughly:** "It just pulled their last three posts. Not to flatter anyone, but to answer one question: has this person said something recently that a first email should open on? If yes, the email opens on their words. If no, and today the answer is no for all five, it opens on their numbers instead. What it will not do is pretend to have seen a post from four months ago. That rule is written into the engine, not left to whoever is drafting at 6pm."

**Then, the handoff line, on the filled rows:** "Everything on this screen has one destination. The engine writes each person's first touch from it, checks it for facts and voice, and what clears goes to the rep's campaign with every line already written. The rep opens their queue and finds the research done and the first touch drafted. They own the send and the conversation."

**Do not say** that the posts made the email more personal on these rows. They did not.

### 2.0 Demo view (before the clip)
Table `Contacts (Buying Committee)`, workbook **Star Ratings**, t_0thtm73HHxyiupTuepK (143 rows). Left sidebar `Workbooks` (**confirm**), open Star Ratings, open the table.

Create a saved view (**confirm**: look for the view selector near the table name) named **All-hands demo** showing ONLY, left to right:

| Show | Why |
|---|---|
| Full Name, Company, Job Title | who |
| `Email`, `Validate Email` (action) and `Status` (rename it **Email check** for the camera if you like; rename is safe, formulas reference the column id) | "email verified". Show `Email` (the address as imported) and hide `email_final`; on all five demo rows they hold the same address (checked Sep 5), and the validator reads `email_final` whether it is visible or not. The `Email Status` column is NOT the validator: it reads the SalesNav staging import and is empty on every row. The live chain is `email_final` -> `Validate Email` (action) -> `Status` (the verdict, reads `valid` on all five demo rows). |
| `Get a person's professional posts and shares` (action): shows `✅ 3 posts or shares found` | "we swept what they've said publicly". **Do NOT show `li_recent_post_hook`**: it is a guardrail column that returns an empty string unless a post is under 30 days old AND about Stars, CAHPS, member experience or contact-center ops. It has run on 59 rows in this table and returned empty on every one, and the cell displays the literal word `Response`. Newest posts on the five demo rows are June and July 2026, so it will stay empty on camera. |
| `Contact Center Platforms` (PredictLeads Find technology stack; add it per `Tech_Stack_Column_UISheet_Sep5.md`) | "which platforms they run" |
| `Persona Key`, `Product Angle`, `Why Now (2026-cycle)` | the research summary |

Hide everything else, in particular: `MessageGen Email`, `Msg1Subject`, `Msg1Body` (retired Sep 5, never run again), `Sync Leads - Star QBP Wave 1 Persona 2`, `Sync Leads - Stars QBP Wave 2 - Persona 1`, `Invoke Workflow` (these push leads out), `Draft Audit`, `Voice Audit`, `voice_status`, `voice_reason_readout`, `msg1_critic Status`, `Msg1Critic Reason`, `send_ready`, `human_approved`, `customer_exclude`, `customer_exclude_bool`, both `Lookup Single Row` columns, `Wave 2 Audit`, and all eleven `New Column` placeholders.

Filter the view to these five rows (all prospects, `customer_exclude = FALSE`, wave 2, drafts already exist):

| Row id | Person | Company | Title |
|---|---|---|---|
| r_0thvacw5dJyCWuV9Kaj | Mel Chapman | Devoted Health | Senior Director of Member ... |
| r_0thvacwCN8reRjtCHAb | Shawn Larsen | Medica HealthCare Plans | Vice President Quality, St... |
| r_0thvacwmcH4cxdB5SSQ | Krista Dusil | Medica | Chief Financial Officer |
| r_0thvacwxYkJKwhroG29 | LaTonya Augustine | Clever Care Health Plan | Director of CAHPS and Star... |
| r_0thvacx83jBxHR9ei9e | Peter Kuipers | Clover Health | Chief Financial Officer |

Not Jeff Ingram (left L.A. Care) and no row with an initial for a surname.

Note on the story: these five are Stars prospects, not customer back-office names, because that is the table with the full pipeline on it today. The narration is written generically ("for every one of them") so it holds. If you'd rather the rows match the act, say so and I'll stamp a five-row back-office demo table from the 312 (about 15 credits); that's a Clay table build, so it's your hands in the UI or a workflow run on a segment.

### 2.3 The enrichment clip (Screen 3, 55 seconds, a separate screen recording made ahead of time)
This recording IS the clip. Make it before the narrated takes: Record Selected Portion over the table window, mic optional, no narration needed while the cells fill. It drops into iMovie between take 2a and take 2b, and you narrate over it there or let it play under the last lines of take 2a.

1. Tab (b), demo view, five rows visible at 125 percent. Start recording, two seconds of still.
2. Run in this order, back to back: `Validate Email`, then `Get a person's professional posts and shares`, then `Contact Center Platforms`. Column header menu, run on selected rows only (**confirm** the menu item; never "run all rows"). Cells fill left to right. Expected platform cells: Devoted Calabrio + TalkDesk; Medica Five9 + Avaya; Clover Amazon Connect + Five9; Clever Care empty. Do not run `MessageGen Email`; it is retired and it costs credits.
3. When the platforms column has filled on all five, hold 3 seconds on the full rows so the research reads left to right. Stop.
4. Check every cell filled: `Status` (`valid`), the posts column (`✅ N posts or shares found`), `Contact Center Platforms` (Clever Care's is empty by design).
5. Any error or blank: swap the row for another wave 2 row with `customer_exclude = FALSE`, and record again from step 1. Never keep a clip with an error cell.
6. In iMovie, if the fill takes longer than 55 seconds, speed the middle to 2x; keep the first cell filling and the final hold at normal speed.

### 2.4 Back-office maps (Screen 4, 35 seconds, take 2b starts here)
1. Tab (c), https://backoffice-maps.pages.dev. Twelve accounts on the page (Assurant, Cleveland Clinic, Cox, DIRECTV, Goldman Sachs, Guardian, McKesson, MetLife, Prudential, Rogers, Travelers, Zurich); six more for Nate under /nate (Centene, Fidelity, National Grid, Paychex, Regions, Truist).
2. Start recording on the index, two seconds of still. Open **MetLife** (insurance, back office is claims and policy admin; reads cleanly). Scroll top to bottom at reading pace: the senior executive, the lanes, who reports up to whom, the bench. Keep scrolling; don't park on one person.

### 2.5 Buying committee (Screen 5, 35 seconds, same take)
1. Tab (d), https://icp-committees.pages.dev. Click the **Back Office Optimizer** product.
2. The ring: the deal in the middle, four roles around it. Click the **State Farm** card (the page's back-office example: Wensley J. Herbert, SVP P&C Claims as economic buyer; Sean Rae, Director Workforce Analytics as evaluator; Dana Jokerst, Senior Operations Manager P&C Claims as champion; Andrew Galligan, Technology Director P&C Claims as integration owner). Hold 5 seconds.
3. Say the outcome line on the ring. Hold 3 seconds. Stop.

The role names on screen are Economic buyer, Evaluator, Champion, Integration owner (renamed from Gatekeeper on Naveen's Aug 10 recast). Use those words in the narration, not "influencer".

---

## Act 3 · Multi-channel sequences (about 50 seconds of tape, one take)

### 3.1 lemlist, the campaign (Screen 6, 45 seconds)
Campaign "All hands demo - recording" (cam_WaDLXcAtit6auc8ay, 11 leads, Jack's UK accounts: Saga, Legal & General, Domestic & General, Ageas). Steps in the sequence: email 1, LinkedIn visit, LinkedIn invite, a call branch, email 2, a LinkedIn message or call branch, breakup email. **No voice note step exists in this campaign.**

The campaign is a **draft** and has never launched, so nothing can send while you record. The signature is written into the three email bodies as literal text rather than the `{{signature}}` variable, because that variable only resolves once leads are reviewed and reviewing them would arm a live send to real UK prospects. On screen it renders identically to Jack's.

1. Open the campaign. Start recording on the leads list, two seconds of still: the loaded names, their companies, the step each is on. 5 seconds.
2. Click **Kate Taphouse** (Director of Customer Operations, Saga, lea_iewAHWD8KE9bw6stP). Every one of her variables was checked filled on Sep 4: subject, personalisation, ask, connect note, email 2, LinkedIn message, phone ask, breakup line.
3. Open her sequence preview. Hold 4 seconds on email 1 (public Saga figures only). Scroll through the LinkedIn invite and hold 3 seconds on the call step. Scroll past email 2 and the LinkedIn message without pausing (both carry a minutes-per-agent figure that sits at CONFIRM in the Value Repository, UK copy on Jack's authority). End on the breakup email. Say the outcome line. Stop.
4. If anything shows an unrendered `{{variable}}`, stop, pick Robin Spooner (Ageas UK) instead, start the take again.

What NOT to show: the campaign settings and sending-mailbox screens (domains and warmup), the stats tab (early numbers invite the wrong questions), any lead flagged bounced.

### 3.2 Slack (cut)
Checked Sep 4: #gtm-outbound-nathan and #gtm-outbound-jack hold only your own posts from Jul 31 to Sep 1. No relay post has landed in either, so there is nothing to put on screen. The "every reply comes back to the rep" line is narration over the lemlist screen.

---

## Coda · Beyond outbound (about 25 seconds, one take)

1. The coda title card carries "Partner briefs, webinar routing, product prototypes." so all three lines are named on screen before the take.
2. Tab, the Ally partner brief. Start recording on the hero, two seconds of still. One slow scroll from the hero to the people table, 15 seconds, while you say the coda lines. (Partner-safe copy: no seat counts, no dollars.)
3. Scroll back to the hero. Hold 4 seconds. Stop. This is the last frame; Naveen closes in the room.

---

## Traps, in one place

- Act 1: keep the EXCLUDED line and any file path out of frame.
- Act 2: don't open the Audiences filter panel; never run a column on all rows; never click `Sync Leads` or `Invoke Workflow`; the demo view exists so they aren't on screen at all.
- Act 2: the two `Lookup Single Row` columns and `customer_exclude` are the customer gate. Hidden, not deleted.
- Act 2: the enrichment clip is recorded once and reused; if you re-record it, re-check every cell before it goes in the cut.
- Act 3: if you use Stars - Resurrection, the STRAY steps go first or the sequence editor stays closed.
- Coda: the internal partner brief (with 3xG seat counts) is a local file; the public /briefs/ page is the one on screen.
- Act 3: no "voice note" in the narration; the campaign has none.
- Everywhere: credit balance off screen, no 6sense, no stats tabs, no dollar figures, the script window outside the recording frame.
