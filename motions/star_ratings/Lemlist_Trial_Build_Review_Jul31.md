# Lemlist Trial Build, Review Package (Jul 31 2026)

Everything built in the Lemlist workspace tonight, plus the hand-verified lead lists and every flag that needs your eyes BEFORE any lead loads. Nothing sends today: all three campaigns are Draft, zero leads are loaded, and lead loading waits on your review of this doc.

## 1. What is live in Lemlist right now

Workspace: Dallas Andrews's Team (tea_h82tSpLDH9vt59tkJ). Nate is invited and on the team (member). All sends will carry Nate's identity once his channels connect.

| Campaign | ID | Status | Schedule | Tracking |
|---|---|---|---|---|
| Stars - Resurrection (Nate) | cam_sh3JCJoxtEHyjGrsw | Draft | Mon-Fri 9:00-18:00 ET | opens+replies ON, clicks OFF |
| Stars - Fresh Pool / Quality (Nate) | cam_viEbB6HkYsCPtxKbi | Draft | Mon-Fri 9:00-18:00 ET | opens+replies ON, clicks OFF |
| Stars - Fresh Pool / Finance (Nate) | cam_2gy9hmEvMjYEuPZ8A | Draft | Mon-Fri 9:00-18:00 ET | opens+replies ON, clicks OFF |

All three also have: on reply = STOP the lead AND stop everyone else at the same company (committee choreography survives the tool switch), on meeting booked = same, out-of-office detection on, LinkedIn steps set to manual-approve so nothing outbound fires on LinkedIn without a human click.

## 2. The adaptive trees (sequences react to prospect behavior)

Built from Lemlist's own sequence-pattern playbook (multichannel fast + ABM + re-engagement patterns).

**Fresh Pool Quality and Finance (identical structure, lane-specific copy):**

```
Day 0  Email 1 (lane opener)
Day 1  LinkedIn profile visit          <- they see Nate's name before the ask
Day 2  LinkedIn connect (manual)
       CONDITION: accepted within 2 days?
  YES  -> conversation moves to LinkedIn
         LI message (manual) -> Email 2 (+2d) -> Breakup (+3d)
  NO   -> CONDITION: lead has a phone number?
     YES -> Voicemail task -> Email 2 (+2d) -> Breakup (+3d)
     NO  -> Email 2 (+1d, tightened) -> Breakup (+3d)
```

**Resurrection (re-engagement pattern, references Nate's earlier note):**

```
Day 0  LinkedIn profile visit
Day 1  LinkedIn connect (manual)
       CONDITION: accepted within 2 days?
  YES  -> LI message (manual) -> Call task (+1d) -> Breakup email (+3d)
  NO   -> Call task -> "just tried you" email (same day)
          CONDITION: opened within 3 days?
            YES -> warm breakup ("leaving it here")
            NO  -> cold-read breakup ("closing the loop", asks for redirect)
```

Behavior notes for Nate's operating rhythm:
- Manual steps (all LinkedIn sends/invites, all call tasks) HOLD the lead until he completes or skips the task in the Tasks view. Skipping advances the lead; nothing is silently stuck.
- Voicemail scripts and call scripts are embedded in each task with merge fields filled per lead; the phone number placeholder [number] is Nate's own callback number, he says it live.
- A lead with no LinkedIn URL fails the invite step gracefully; the invite-accepted condition then falls to NO and the lead continues down the email/phone path.

## 3. All sequence copy (as loaded, verbatim)

Merge fields: {{firstName}}, {{plan_name}}, {{qbp_avg}}. Zero Intradiem stats anywhere; every number is the prospect's own public-CMS picture with the humility clause; Intradiem named only from Email 2 onward and once in voicemails. All copy is the Jul 13 send-ready Wave 1 set adapted to Lemlist, plus new Resurrection copy in the same voice.

### Quality lane
- **Email 1** | subject: the last stretch to 4.0
  Hi {{firstName}}, your weighted average looks to be right around {{qbp_avg}}, though you'll know the exact picture far better than I do. What caught my eye is how close that is. For a book sitting there, the last few points usually come from the customer-service measures, and they're being set right now, in this measurement year, not on the October release. / Thought it might be worth finding time to talk through which of your contracts sit closest to the line and which measures still move them this cycle. Have 15 minutes in the next few weeks? / Nathan
- **LinkedIn connect note**: {{firstName}}, I work the operations side of Medicare Stars, the gap between what the service measures capture and what actually happens on the floor under load. Seemed worth connecting. (Premium variant adds the CAHPS phrasing and {{plan_name}}.)
- **LinkedIn message (accepted path)**: Thanks for connecting, {{firstName}}. The short version of my note: the last few points to 4.0 usually sit in the customer-service and CAHPS measures, and they're being decided in the live weeks between now and December, not on the October release. Worth 15 minutes on the contracts nearest your line?
- **Voicemail (phone path)**: {{firstName}}, this is Nathan with Intradiem. I sent you a note on the customer-service measures inside your last half-star, and why they're decided this year, on the floor during peak weeks, rather than on the October release. I can walk which of your contracts sit closest to the line and which measures still move them. I'm at [number], or just reply to the email. Thanks {{firstName}}.
- **Email 2** | subject: the window is more than half spent
  Hi {{firstName}}, the reason this is a now question and not an October one: the measurement that sets the next rating is running across this year and is already more than half spent. Every peak week where service slips under load counts toward the next cliff before the number ever publishes, and the customer-service measures are the first to feel it. The contracts near {{qbp_avg}} are the ones where holding steady this cycle still moves the rating. / Holding that experience steady under load, in real time rather than after the report, is the piece Intradiem works on. Fifteen minutes and I'll walk the specific measures where a book near your line usually wins or loses the half-star before the window closes. / Nathan Belfield
- **Breakup** | subject: leaving it here
  Hi {{firstName}}, I'll stop here. One parting thought: the customer-service measures are the first to slip under load and the slowest to recover once a scoring window closes, which is why holding them in real time is worth more than fixing them after. When protecting the last half-star becomes a focus, that's the seam I work. Glad to help whenever the timing's right. / Nathan Belfield

### Finance lane
- **Email 1** | subject: the bonus at {{qbp_avg}}
  Hi {{firstName}}, from the finance seat the 4.0 line is really a quality-bonus question, and {{plan_name}} looks to be sitting right under it at about {{qbp_avg}}. You'll know the exact picture far better than I do. The measures still movable this cycle are mostly operational, not clinical. / Open to 15 minutes on how you're modeling the cliff? / Nathan
- **LinkedIn connect note**: {{firstName}}, reached out on the finance side of the Stars cliff, the quality-bonus dollars that turn on a half-star and the operational measures that still move it. Worth connecting here.
- **LinkedIn message (accepted path)**: Thanks for connecting, {{firstName}}. The heart of my note: near 4.0 the bonus turns on a half-star, and the half-star is mostly an execution question in the service measures, not a clinical one. Worth a short call on how you're modeling the exposure?
- **Voicemail (phone path)**: {{firstName}}, this is Nathan with Intradiem. I emailed you on the quality-bonus exposure at {{plan_name}} sitting near the 4.0 line, and why the points still movable this cycle are the operational ones, not the clinical ones. Fifteen minutes on how you're modeling the cliff versus what closing it returns? I'm at [number]. Thanks {{firstName}}.
- **Email 2** | subject: the cliff is being priced in now
  Hi {{firstName}}, one point on timing for the finance model specifically. The measurement that sets the next rating is running across this year, so the contracts near the line are being decided in the peak weeks between now and year end, not on the October release. Every week service holds under load is a week toward clearing the bonus line; every week it slips is priced into the next cycle before you ever see the rating. / Making that execution consistent under load is what Intradiem does, which is why the movable measures stay movable. Fifteen minutes and I'll walk the finance view on what holding the next half-star costs versus what the bonus returns. / Nathan Belfield
- **Breakup** | subject: leaving it here
  Hi {{firstName}}, I'll leave it here. One thought worth keeping: missing the line by a fraction and missing it by a lot cost the same one cycle of bonus, and the cheapest half-star to buy back is always the contracts already sitting closest to it. When the cliff becomes a finance priority, the operational-execution angle is where I'd start the model. Glad to help whenever the timing fits. / Nathan Belfield

### Resurrection (both personas, references the earlier note)
- **LinkedIn connect note**: {{firstName}}, I emailed a few weeks back on the last half-star at {{plan_name}}. Figured I'd connect here too, worth having the thread open either way.
- **LinkedIn message (accepted path)**: Thanks for connecting, {{firstName}}. I emailed a few weeks back on the last half-star at {{plan_name}}, and the scoring window's kept narrowing since. If it's worth a fresh look before the peak stretch, have 15 minutes this week or next?
- **Call script (both paths)**: {{firstName}}, this is Nathan with Intradiem. I sent you a note a few weeks back on the last half-star at {{plan_name}} and the service measures that still move it this cycle. That window keeps closing a week at a time, which is why I'm circling back. I can walk which of your contracts sit closest to the line. I'm at [number], or just reply to the email. Thanks {{firstName}}.
- **"Just tried you" email** | subject: just tried you
  Hi {{firstName}}, just tried your line, no luck, so leaving this here instead. I emailed a few weeks back about the last half-star at {{plan_name}} and the service measures that still move it this cycle. That window's kept closing a week at a time since, which is the only reason I'm circling back. / If it's worth a fresh look before the peak stretch, have 15 minutes this week or next? / Nathan
- **Warm breakup (opened the email)** | subject: leaving it here
  Hi {{firstName}}, I'll stop here. One parting thought: the measures still movable this cycle are the operational ones, and they're being scored right now, in the live interactions, not on the October release. When the last half-star becomes a focus, that's the seam I work. Glad to help whenever the timing's right. / Nathan Belfield
- **Cold breakup (never opened)** | subject: closing the loop
  Hi {{firstName}}, closing the loop on my notes about the last half-star at {{plan_name}}. If this sits on someone else's desk, glad to be pointed the right way. Either way I'll leave it here until the timing fits. / Nathan Belfield

## 4. Customer-exclusion hand-check, VERIFIED

Method: pulled all 143 live rows from Contacts (Buying Committee) (t_0thtm73HHxyiupTuepK) read-only, filtered to eligible fresh-pool candidates (94: 63 Quality-lane incl. cc_ops fold-in, 31 Finance), then hand-compared every unique parent company against the full 101-account SF customer file (Active_Customers_SF_Jul10.csv), NOT the Clay flag. Alias traps checked by hand: HCSC as "Health Care Service Corporation", all 12 Kaiser entities, SCAN, Molina, Elevance, BCBS North Carolina, the Aetna/CVS/UHC subsidiary cluster, CIGNA, Evolent, Baylor Scott & White, Cleveland Clinic, and the Medica trap (Medica of Minnesota is independent; "Medica HealthCare Plans" of Florida is a UHC subsidiary; all 7 cohort rows are @medica.com = Minnesota = clean).

**Result: ZERO customer hits across all 94 candidates.** The 16 customer contacts (HCSC, Humana, UHC, Aetna/CVS cluster) are all correctly flagged in Clay and none leaked into the cohorts. The Clay allowlist (6 names) is narrower than Accounts(Master)'s customer_flag (adds kaiser, scan), but neither Kaiser nor SCAN has any contact in this table, so no gap today.

Verified parents in the pool (24): Solis, HMSA, CalOptima, Point32Health, Devoted, Medica (MN), Clever Care, Imperial Health, Blue Shield of California, Centene, Clover, ATRIO (incl. AllyMar alias), Zing, L.A. Care, IEHP, CHPW, Cambia, NYC Health + Hospitals, CareFirst, Baystate, GuideWell, Excellus, Mass General Brigham, Lumeris.

## 5. Flags: RULED Jul 31 (Dallas approved all recommendations)

1. **CUT the 13 rows at the four clinical-gap parents** (CareFirst: Haynes, Sening, Phillips, Bridges. Lumeris: Barwick, Eschbach, Grabski, Gardner. Mass General Brigham: DeRoche, Gandhi. GuideWell: Szkotnicki, Petruzzellis, Goddard). DECIDED: cut.
2. **HOLD Excellus's 2 rows** (Mark Wagner, Alex Levi) out of the email-led campaigns per the Wave 1 email-hold guardrail. DECIDED: hold.
3. **CUT the 5 wrong-persona/identity rows in cc_ops** (Scutella, Dahlen, O'Toole, Straka, plus the mismatched dave.chokshi@nychhc.org row). DECIDED: cut.
4. **cc_ops fold-in**: stays IN per the ratified Wave 1 ops-lane design (ops folds into the Quality lane), minus the cuts above, leaving 18 cc_ops rows. They'll be shown as their own block in the final pre-load counts so the last human gate sees them separately.
5. **{{qbp_avg}} source**: pull the weighted-average estimate from Accounts (Master) per parent where it exists; any lead without a defensible number runs the 1B "measurement window" opener, which doesn't use the figure.

**Load math after cuts (before the Wave 1 de-dupe):** Quality lane 50 (32 stars_quality + 18 cc_ops), Finance lane 24. The Wave 1 export still has to remove the already-emailed overlap before anything loads.
6. **Resurrection cohort is unbuildable from the API side.** Sent/reply truth lives in the Clay campaign Leads tabs, which no CLI/MCP path can read (Enterprise observability gate). Need your export (step 2 below).
7. **qbp_avg does not exist as a per-contact column.** The table carries cs_star/clin_star and account-level Forgone QBP ($M). The copy's {{qbp_avg}} is the weighted-average star estimate; before load we either pull it from Accounts (Master) per parent or switch affected leads to the variant-1B opener that doesn't use the number. Blank cliff-map cells (Solis, HMSA, ATRIO, Zing, CalOptima and others) can't run variant 1A as-is.
8. **No phone column exists in the Contacts table.** Connor's ~50 ZoomInfo numbers live outside this table; wherever that file is, it feeds the phone merge field at load time. Leads loaded without a phone automatically take the no-phone path (that's what the hasPhoneNumber branch is for), so this is a data-enrichment opportunity, not a blocker.

## 6. Your action list, in dependency order

1. **Nate connects his channels** (can happen anytime, nothing else depends on it until launch): his mailbox via OAuth in Lemlist Settings, his LinkedIn via the Lemlist Chrome extension on his machine. Until then no sender can be assigned (Lemlist rejected the assignment: "no required capabilities", verified tonight). After he connects, tell me and I assign him as sender on all three campaigns.
2. **Export the Wave 1 ground truth from Clay** (unblocks Resurrection AND the fresh-pool de-dupe): open the live "Stars QBP Wave 1 - Persona 1 (Stars/Quality)" and "- Persona 2 (Finance)" campaigns, Leads tab, export (or screenshot) with Sent and Replied columns. Alternative: paste me each campaign table's t_ id from the URL and I read them directly.
3. **Rule on flags 1-4 and 7** (cut lists and the qbp_avg source). One line each is enough.
4. **Then I load the leads** into all three campaigns with merge fields mapped, and you do the final eyeball of rendered emails in the Leads tab before anything starts.
5. **Launch stays your hand only**: pressing Start on any campaign is yours, after Nate's mailbox is connected and you've read rendered sends. Trial caps: keep ~20-25 emails/day shared with whatever native sending Nate's mailbox is doing.

Copy-paste prompt for when you have the export (drop the file anywhere in the project or paste rows in chat):

```
Here's the Wave 1 sent/replied export. Build the Resurrection load list (sent minus repliers),
de-dupe the Fresh Pool Quality/Finance lists against everyone already emailed, apply the cuts
we agreed in the review doc, resolve qbp_avg per lead, and load all three Lemlist campaigns.
Show me final counts per campaign before I press anything.
```

## 7. Slack layer: the rep channels are wired in (dry-run until you flip it)

The two channels you created are the delivery surface for Lemlist's behavior signals: #gtm-outbound-nathan (C0BM9V6KGSG) and #gtm-outbound-jack (C0BN0JT9D6U). Built tonight, all validated:

- `automation/run_lemlist_relay.sh` + `com.dallasandrews.gtm.lemlistrelay.plist` (weekdays 8:10 and 13:30): polls Lemlist activity, diffs against seen events, and turns prospect behavior into rep action items:
  - **Reply lands** -> alert in the rep's channel with lead/company/campaign PLUS a drafted response in Nathan's voice (peer-level reframe, zero stats, labeled "edit and send from your own inbox"). The Reply Engine discipline, delivered where Nate already works.
  - **Connect accepted** -> alert that the LinkedIn message task just unlocked in Lemlist Tasks (that's the time-sensitive branch of the adaptive tree).
  - **Meeting booked** -> flagged in channel and prominently in the log (receipts for the day-14 story).
  - **Bounce / send-fail / unsubscribe** -> one-line hygiene warning, same day.
  - **Open task digest** -> pending calls and LinkedIn approvals, so the manual steps never silently pile up.
- Routing lives in `automation/config/lemlist_channels.json`: all three trial campaigns map to Nathan's channel today; when Jack gets a motion, his campaigns are one config line, no rebuild.
- **The gate: `"live": false` in that config.** Until you flip it to true, every run writes what it WOULD have posted to `automation/logs/lemlist-relay-DATE.md` and touches no channel (the nobody-but-Dallas rule stays intact). Flip it at launch, after you've read a dry-run log or two.
- The relay never DMs you; the daily rundown reads its log (single-morning-brief rule holds). Load the plist at launch alongside your other jobs: `cp` it to ~/Library/LaunchAgents and `launchctl load` it, same as the others.

Webhooks stay unnecessary: nothing in the stack runs a listener URL, and twice-daily polling covers the trial's volume. If reply latency ever matters more, the upgrade is a small Cloudflare Worker plus one `create_webhook` call filtered to emailsReplied.

## 9. FINAL LOAD LISTS (locked Jul 31 night, from the 5 status tables' Smartlead event logs)

Ground truth: 220 events across the 5 status tables. 72 unique contacts have at least one EMAIL_SENT, 10 replied, 2 bounced (hiep.pham@clevercarehealthplan.com, alan.ngan@ccmapd.com), zero unsubscribes. Customer-leak check CLEAN: angela_martinez@hcsc.com and kevin_burbridge@bcbsil.com have zero events anywhere, no send ever went to a customer contact.

**RESURRECTION, 48 leads** (sent at least once, never replied, never bounced, all rulings applied). By parent: Medica: Stewart, McAdam, Larsen, Smith, Thorstad. Devoted: Chapman, Rosenbaum, Gerstein, Yale, Quinn, Shah, O'Connor. Centene: Lewis, Hoseini, Hiltibidal. Clever Care: Haggard, Manetti, Greene, Katula. Imperial: Dahlkamp, Barsegyan, Bindra. CalOptima: Lee, Choo, Gomez. Blue Shield CA: Maroney, Oubre. Clover: Addison, Kuipers, Holmes. Solis: Martin, Soler, Romay. HMSA: Teehankee, Sugai, Morgan. NYC H+H: Sudha S. Zing: Weaver, Munoz. CHPW: Graham, Dabney. Point32: Dowd, Kurup. ATRIO: Stone, Lowman. L.A. Care: Donna S. IEHP: Remington P. Cambia: Schweikert.
Emailed-but-cut per rulings (12, they simply go quiet): Haynes, Sening (CareFirst), Eschbach, Barwick (Lumeris), DeRoche (MGB), Szkotnicki (GuideWell), Wagner, Levi (Excellus), Scutella, Dahlen, O'Toole, Straka (wrong persona).
Resurrection copy uses only {{firstName}} and {{plan_name}}, no qbp_avg needed.

**FRESH POOL QUALITY, 2 leads** (in campaign rosters but never actually sent): Pedro Rivera (NYC H+H, qbp_avg 3.5), Andrew Breuckman (CHPW, qbp_avg 3.0).

**FRESH POOL FINANCE, 15 leads** (never touched): Goldberg (Point32, 3.5), Marrone (Point32, 3.5), Ingram (L.A. Care, 3.0), Martin (Baystate, 3.0), Rains (Cambia, 3.0, both contracts 3.0 so the average is exact), Qin (Blue Shield CA, 3.5), Hoenstine (Zing, 2.5), Thornton (Clover, 3.5), Chio (IEHP, 3.0), Battersby (CHPW, 3.0), Faulring (CHPW, 3.0), Miyasato (HMSA, 3.5), Yang (NYC H+H, 3.5), Lynch (Solis, 3.5), Huang (CalOptima, 3.0).
qbp_avg = the parent's overall_star_2026 from Accounts (Master); every fresh lead has a single defensible value (all multi-contract parents landed in Resurrection, where the number isn't used).

**REPLY LANE, 10 (never load, reply engine territory):** Bachmeier, Hedrick, Hermosillo (Blue Shield CA), Augustine, Tran, Dusil, Weiss, Ricciardi, Bernstein, Chokshi. That's 10 replies against ~70 emailed contacts.

**Sequencer defects the Lemlist build already fixes:** Smartlead kept sending AFTER a reply twice (Bachmeier got a send 3 days post-reply, Tran 2 days post-reply); the Lemlist campaigns stop the lead AND the company on reply. Ten contacts were double-enrolled across two campaigns; Resurrection consolidates each contact into exactly one campaign.

## 8. Open items on my side

- Sender assignment (waiting on Nate's channels).
- Lead load (waiting on your export + flag rulings).
- Optional: schedule lemlist-pulse as a launchd job alongside the other morning jobs; right now it runs on demand.
