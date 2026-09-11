# All-hands demo, recording script v3

> Three acts and a coda, seven screens, under five minutes, narrated in the cut. Each act opens on a problem the room already understands, shows the engine working on it, and closes on what comes back. Click-by-click detail is in the recording sheet.

| Act | Problem | On screen | What comes back |
|---|---|---|---|
| 1 · Strike rooms | An AE has a target account and a blank page. | One ask in Claude Code builds the account plan and a ten-day, multi-channel sequence for the whole buying committee. | A day of research and drafting per account becomes minutes. |
| 2 · Back office, inside our customers | Our customers' front offices know us. Their back offices don't, and nobody introduces us. | Clay: the back-office leaders we already know at customer accounts; five rows enriching (email verified, what they post about, which contact center platforms their company runs, the first draft); the account maps built with the AM team; the buying committee with the deal in the middle and State Farm on the card. | Eighteen accounts mapped and checked against Salesforce; sellers start from a map, not a search bar. |
| 3 · Multi-channel sequences | Even with the list and the drafts, running email, LinkedIn and calls per person on a cadence is a job on its own. | lemlist: one lead's fully rendered sequence, every variable filled for that person. | Seven campaigns sending across two regions; reps own the conversation, not the typing. |
| Coda · Beyond outbound | | A partner brief for Alliances. The title card names the other two. | One engine. It runs work like this for any team. |

Rules: everything shown already exists and runs; nothing sends during the recording; no arithmetic on screen (bases live in the Q&A prep, "if pressed"); capacity created, never labor replaced; no 6sense anywhere in frame; no unfinished-work phrasing.

## Recording method

- Each act is its own take, mic on, script spoken as the screen moves. Two seconds of still at both ends. The take you like is the take you submit; the audio stays in.
- QuickTime, Record Selected Portion, frame over the browser window only. Script in a window beside the frame, or on a second screen.
- Title cards (`title_cards/`, four PNGs) sit at the act boundaries, three to four seconds each. Every tab switch happens behind a card.
- If a take runs long, cut words, not screens. Act 1 is two recordings joined by a straight cut (the ask, then the finished output), so the run's length never matters.
- Due Tuesday Sep 8 to Jason.

## Pre-flight, in this order

1. **Act 3 campaign: `DWO Executives - Live Pool (Nate)`** (cam_SiD4KmWcRuhiF6uhL, draft, 803 leads, 33 steps, three leaves). This is the recording campaign. It is the real US motion, the branching tree reads as a system rather than a list, and the accounts in it are names the room knows. The 11-lead UK copy ("All hands demo - recording", cam_WaDLXcAtit6auc8ay, Saga / Legal & General / Domestic & General / Ageas) is not used; Jack's original (cam_SxnHzvAr3WsvWPPeY) stays untouched.

   Three things to fix in that campaign before the take: pick a lead whose email is verified (four on the current first page carry `Not verified` badges and `FIND PHONE` buttons); frame so the blue **Launch for 803 leads** button and the out-of-schedule banner are off screen; and confirm the step body you hold on does not still carry the `[draft, Nate reads]` marker, which was added to every new step body on Sep 4.
2. **The ahead of time strike plan run.** Fresh Cowork thread, Opus 5 High, type only `Build the strike plan for Centene.` and nothing else. The skill carries every rule; if an output is only correct because rules were pasted with it, the demo's claim is false. Leave the thread open until recording B is captured. Before you run it, archive the "6sense integration with Clay" thread out of the sidebar, since the sidebar is in frame for both Act 1 halves.
3. **Add the Contact center platforms column** to the demo view (`Tech_Stack_Column_UISheet_Sep5.md`, three minutes, your hands). Then **record the enrichment clip** ahead of time (act 2, screen 3 below). That recording is the clip. Under 25 credits.
4. **One browser window per act,** only that act's tabs open.
5. **Screen hygiene:** Do Not Disturb, bookmarks bar hidden, browser at 125 percent, every unrelated window closed, credit balance off screen.

## Act 1 · 0:00 to 1:05 · Strike rooms

**Problem (say it first, over the act 1 title card or the empty terminal):** "Every rep starts an account the same way: a target, a blank page, and a day of research before the first message."

**Screen 1 (0:00 to 0:55):** Claude Code, terminal full screen, font at 16pt. Type: `Build the strike plan for Centene.` Record the ask and the first ten to fifteen seconds of it working. Then, in iMovie, jump cut to the finished output from the ahead of time run (a second recording: the finished plan already on screen, you scrolling it): the trigger that fired with its date and source, the buying committee, then the sequence. Pause on the **Proof you can use** block long enough for the room to read its closing line, "every line above is sourced and cleared" (that's the checkpoint, on screen, stated as a guarantee rather than a restriction), then scroll to one committee member's block so the room sees the email, the LinkedIn note and the voicemail for one named person. The run itself is never on tape end to end. Re-run needed: the Sep 5 AmeriHealth Caritas output is retired (seed TAM record, no sourced committee). Redo it on Centene, Opus 5 High, with the bare sentence and nothing pasted alongside it.
**Say roughly:** "One ask, in plain English. The engine names the buying committee and writes the ten-day plan: emails, LinkedIn notes, voicemails, for every person on the committee, in the rep's voice. This is what Nate and the sales team run from today. The same engine built the buying-committee pages leadership is working from. And it isn't a one-off: two dozen agents run overnight on scans, triggers and audits, and a short brief is waiting at 7:50 every morning."

**Hold (0:55 to 1:05):** last frame, then the act 2 title card.
**Outcome line:** "A day of work per account. Now minutes."

Keep out of frame: any dollar figure or ROI line, the Owner line, the EXCLUDED line, any `[UNVERIFIED]` tag, any file path, the model picker in the bottom right, and the Cowork sidebar's recent-chat list (archive the 6sense thread before you record).

**No fit score in this act.** Every row in `tam-outbound-engine/data/tam_accounts.csv` is still the Jul 1 2026 seed: no `source` citation, invented firmographics and triggers. The engine now prints a `!! SEED RECORD !!` banner and the skill refuses to put a seed row's score, tier, agent count, ROI or triggers in a plan. So the number in the first take (82, Tier 1) and the engine's own 75 are both arithmetic on invented inputs, and neither goes on screen. The act does not need it: the progress panel, the dated public-record why-now, the named committee and the five touches per person are the shot.

**Account: Centene, not AmeriHealth Caritas.** Centene is the skill's built-in reference example with a real, tiered, verified committee; it is already on screen in act 2's committee ring; it is a name the whole company knows; and it is a confirmed non-customer. AmeriHealth Caritas had one advantage, the engine fit score, and that advantage does not exist. It also has no committee: the 5 Sep run reported "the TAM engine returns personas, not people, and there is no Clay export for this account." Any named committee in a plan for it was not sourced from a roster.

## Act 2 · 1:05 to 3:35 · Back office, inside our customers (the centerpiece)

**Problem (say it first):** "Our customers' front offices know us well. Their back offices, claims, billing, enrollment, payments, mostly don't, and the front office doesn't introduce us. So we went and found them."

**Screen 2 (1:05 to 1:25):** Clay Audiences, People tab, the top line at about 140,000 people synced from Salesforce. Open the saved segment **BO Leaders (customers, Dir+)**. The count lands at 312 (live Sep 4; all people 140,993). Hold on the number. Don't open the filter panel or a person record.
**Say roughly:** "Everyone we know, in one place, synced from Salesforce. Back-office leaders, director and up, inside accounts we already serve." Pause for the count. "Three hundred people who have never heard from us. That used to be a week of exports and spreadsheets. Zero cost, and it stays current on its own."

**Screen 3 (1:25 to 2:20, the separate clip, recorded ahead of time):** Clay, workbook **Star Ratings**, table **Contacts (Buying Committee)**, saved view **All-hands demo**. Five rows, columns left to right: Full Name, Company, Job Title, then the enrichment columns, then the research columns. No draft column: Clay does the research, the engine writes the copy (decision Sep 5, `motions/shared/Clay_MessageGen_Retirement_Sep5.md`).

Run these three action columns in this order, each on the five selected rows only (column header menu, run on selected rows, never run all rows):

| Run this column | It fills | What the room sees |
|---|---|---|
| `Validate Email` | `Email Status` | the email checks out |
| `Get a person's professional posts and shares` | the same column, `✅ N posts or shares found` | that we swept what they've said publicly. `li_recent_post_hook` stays hidden: guardrail column, empty on all 59 rows it has run on, displays `Response` |
| `Contact center platforms` (PredictLeads, Find technology stack) | the same column | which contact center and WFM platforms their company runs, from job posts |

`Persona Key`, `Product Angle`, and `Why Now (2026-cycle)` are already filled on these rows; they stay on screen as the research summary and are not re-run. When the platforms column has filled on all five, hold three seconds on the full row so the room reads it left to right: verified, posted, platforms, persona, angle, why now.

The platforms column is new as of Sep 5. It reads job posts (PredictLeads through Clay, one credit per company) and returns each vendor with the date it was last seen, so what the room sees for these five is: Devoted Health on Calabrio and Talkdesk, Medica on Five9 and Avaya, Clover Health on Amazon Connect and Five9, Clever Care no read. The same read now feeds the strike plan in act 1: a vendor name reaches a rep's email only when it was seen in the last twelve months, otherwise the copy says "on top of WFM" and never guesses.

The five rows (all prospects, `customer_exclude = FALSE`, wave 2): Mel Chapman (Devoted Health), Shawn Larsen (Medica HealthCare Plans), Krista Dusil (Medica), LaTonya Augustine (Clever Care Health Plan), Peter Kuipers (Clover Health). Row ids are in the sheet. If any cell errors, swap the row for another wave 2 prospect row and record again; never keep a clip with an error cell.

**Say roughly:** "For every one of them: verify the email, read what they've been talking about, find out which contact center platforms their company runs, and pull the persona and the angle. Here's that research running on five people at once." (These five are Stars prospects, so the words are "that research", not "these three hundred".) Ten seconds of silence; the screen carries it. "Then the engine writes the first touch for each person from exactly this, and every draft passes a fact check and a human before it moves. You'll see the writing in a minute, where the rep sees it."

**Screen 4 (2:20 to 2:55):** backoffice-maps.pages.dev, MetLife. Scroll the map top to bottom: the senior executive, the lanes, who reports up to whom, the bench. Keep scrolling; don't park on one person.
**Say roughly:** "Then the engine turns the names into the org. When the account management team needed back-office maps for their strategic accounts, it sourced the people, checked every name against Salesforce, and delivered these as a live page. Eighteen accounts so far, with the AM clearing every name before a word goes out."

**Screen 5 (2:55 to 3:30):** icp-committees.pages.dev, Back Office Optimizer. The ring: the deal in the middle, four roles around it. Click the State Farm card: economic buyer, evaluator, champion, integration owner, each a named person with a title. Hold.
**Say roughly:** "And inside every org there's a buying committee. We used to sell to one person. Now we sell to four: the economic buyer, the evaluator, the champion, and the integration owner. Here's State Farm's. The same committee is built for every target account, across every industry we sell into. This is the targeting standard now."

**Hold (3:30 to 3:35):** the ring, then the act 3 title card.
**Outcome line:** "From three hundred names to eighteen maps and a named committee per account. Sellers start from a map, not a search bar."

Keep out of frame: the Cold-Outbound Exclusion, Account Type Missing, Heat, SF Activity and JC Watch segments; the Sync Leads, Invoke Workflow, Lookup Single Row, customer_exclude and audit columns (the demo view hides them).

## Act 3 · 3:35 to 4:25 · Multi-channel sequences

**Problem (say it first):** "Now the rep has the people and the drafts. Running five touches across email, LinkedIn and the phone, per person, on the right day, is a job on its own. So that's automated too."

**Screen 6 (3:35 to 4:20):** lemlist, campaign `DWO Executives - Live Pool (Nate)`. Open on the Sequence tab for five seconds so the room sees the branching tree (the accepted-connect split is the shot), then move to the Launch tab and one named lead whose email is verified. Her or his rendered sequence: email 1, LinkedIn visit, the invite with the connect note, the call step with the voicemail script, email 2. Hold on email 1 and on the call step so the room reads copy written for that individual, not a template.

The Humana lines in this copy (partnership since 2020, two hours of capacity per agent per month, handle time down 45 seconds, occupancy up 4 percent) are all VERIFIED 1:1 and 1:many in the Value Repository and are safe to hold on. The figure to keep off screen is "15 to 20 minutes per agent per day", which is still CONFIRM; read the step body before you frame it.
**Say roughly:** "Cleared contacts land here. Email, LinkedIn and a call step per person, on a cadence, and every line you see was drafted by the engine for that individual. The rep owns the send and every reply comes back to them; the engine did the hours behind it. Every motion is measured on cost per meeting like any other channel. Seven campaigns are sending today across North America and the UK."

**Hold (4:20 to 4:25):** then the coda title card.

Keep out of frame: campaign settings and sending-mailbox screens, the stats tab, any lead flagged bounced. The Slack outbound channels are not in this act; no relay post has landed in them yet, so there is nothing clean to show.

## Coda · 4:25 to 4:50 · Beyond outbound

**Screen 8 (4:30 to 4:45):** the partner brief (https://gtm-partner-pilot.pages.dev/briefs/ally), one slow scroll from the hero to the people table.
**Say roughly:** "It doesn't stop at outbound. The Alliances team asked for account research and a follow-up one-pager per partner account; two skills build both in about five minutes, and Frank runs them himself. The same engine enriched and routed a thousand webinar registrants the week that workflow went live, and the product team is clicking through prototypes instead of reading specs. One engine, and it runs work like this for any team."

**Last frame (4:45 to 4:50):** the brief's hero, held. Naveen closes in the room.

## Fallbacks

- Screen 1 is the only live moment and it is only the first fifteen seconds; the finished output comes from the ahead of time run.
- Screen 3 is a clip; it cannot fail on the day.
- Every other screen is read-only.
- If the whole take collapses, the operating map's animated system view (gtm-operating-map.pages.dev) narrates the same three acts slide-style.

## Timing

4:50 as written, 5:30 hard cap. Act 2 is the only act that may run long. If anything else runs over, cut words, not screens; the room reads a screen faster than it listens.
