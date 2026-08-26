# Blitz Build: Citizens + The Hartford (Aug 6 2026)

Trigger: Nathan's DM Aug 6 11:43 CDT, "Am I good to start pulling in contacts from Citizens and The Hartford into lemlist?" Dallas committed to having both sequences built and ready the same afternoon. These are Keegan's two first-sprint blitz accounts per `Keegan_Attainment_Engine_Aug3.md` (Citizens carried a 48-hour commitment from the Aug 3 sync).

Sender: Nathan Belfield (`usr_9rxD82ZfapeZBGSoz`). Both campaigns DRAFT, zero sends, send gate closed.

## Campaigns

| Account | Campaign | ID | Main seq | Leads |
|---|---|---|---|---|
| Citizens | Blitz - Citizens (Nate) | `cam_yWefPqaDhNNv4RyQK` | `seq_vWS3ceMs5oh8YB6E5` | 8 |
| The Hartford | Blitz - The Hartford (Nate) | `cam_fYp7Nh9wB72gfMke6` | `seq_jG8aiuxE8FCQD564C` | 8 |

Structure is an exact clone of the proven Nate Stars shape (21 steps, 5 sequences each):

1. E1 (day 0), A/B enabled: variant A = meeting ask, variant B = offer CTA (per `First_Touch_CTA_Doctrine_Aug3.md`, US A/B lane)
2. LinkedIn profile visit (day 0)
3. LinkedIn connect, no note, manual approval (day 1)
4. Conditional, invite accepted within 2 days
   - **Accepted:** LI message -> call 1 (no VM) -> LI voice note -> call 2 (VM) -> E2 -> breakup
   - **Not accepted:** conditional on `hasPhoneNumber`
     - **Has phone:** voicemail -> call -> E2 -> final double-tap call -> breakup
     - **No phone:** E2 -> like last post -> follow -> visit -> breakup

Call scripts are assembled from `motions/shared/Cold_Call_Playbook_Aug2.md`: four-beat opener, US 30-second contract, engage/ask/busy/brush-off branches, hard-stop rule on brush-offs. Voicemails are under 30 seconds and carry `{{vm_hook}}`.

## Motion angles (both are cost-mandate variants, NOT Stars)

**Citizens: the residual queue.** Citizens has publicly committed to a quarter of calls answered without a human by end of 2026, on the way to 50%+ (Brendan Coughlin, President, to American Banker, Mar 27 2026), inside the "Reimagine the Bank" program targeting $450M run-rate savings by 2028. The wedge is the second-order effect nobody plans for: when AI takes the easy half, the calls that still reach a person are all exceptions, so handle time climbs while the easy volume that used to absorb schedule slack disappears. The deflection is real and the savings can still leak back out through the human queue.

**The Hartford: the volatile side carries the promise.** Automation lands first on the predictable work because that is the easy place to put it; the unpredictable work stays human. So the volatile side of the operation ends up carrying the service promise, staffed to a forecast written before the week happened. Second beat (E2): across the industry the underwriting side of the AI story has a number attached and the claims/service side does not yet.

## Verified-claims gate

PASS. No Intradiem metric, customer outcome, or peer claim appears anywhere in either campaign. Every number in the copy is a public third-party figure, itemized:

- Citizens: "a quarter of calls answered without a human by the end of this year, on the way to half." CONFIRMED, Coughlin via American Banker, Mar 27 2026. Lives in the fixed E2 template (one place to correct if it ever changes), not in a per-lead variable.
- The Hartford: "small commercial written premium grew about seven percent last quarter." From Q2 2026 earnings coverage. Used in Gutierrez and Batman variables only. **[VERIFY]** against the Q2 2026 release before those two send.
- The Hartford: "Chris Swift put superior customer experience at the top of the themes on the last call." From Q2 2026 earnings coverage. Deane variable only. **[VERIFY]**.

**DROPPED at the gate:** "75% of admitted-lines quotes bound within minutes" appeared in one aggregator summary of The Hartford's Q2 2026 call and did NOT confirm on a second pass. It was the original spine of the Hartford angle and was removed rather than shipped. The Hartford E1 now rests on a pattern observation, not on that figure.

**Charter / Foss:** Jeffrey Foss's opener references Ted Lango (Intradiem SVP, Business Enablement, confirmed) and Foss's own Charter tenure. It makes no claim about Charter as a customer and attaches no outcome, so it does not touch the CV-INTERNAL Charter row in the Customer Value Registry. Naming a person Foss already knows is not a customer disclosure. No Charter result may be added to this sequence without a tier promotion.

## Customer-exclusion gate

PASS on three independent checks: neither account appears in the 101-account install base (Clay `t_0ti4jj1hfZyEWcfirfU`, query returned 0 rows), neither appears in `Customer_Value_Registry.md`, and the Aug 3 TAM ingest classified both "watch" while naming the three accounts that were customer-excluded. Real-row gate validation still runs at launch per the standing rule.

## Buying committees

**Citizens (8).** Jeffrey Foss (Contact Center Operations, the warm alumni anchor), Tashell Weaver (SVP, Director WFM Operations), Peg Marty (Head of Customer Service Operations), Natalie Higgins (SVP, Director Self-Service Strategy, owns the containment number), Michael Merritt (SVP, Head of Default & Customer Care), Mike Bartolazo (VP, WFM and Capacity Planning), Robert Soukkala (VP, Head of Mortgage Collections and SPOC), Patrick Savage (VP, Virtual Services Program Group).

**The Hartford (8).** Steve Deane (EVP & Chief Claims Officer, economic buyer), Stacy Gutierrez (SVP, Head of P&C Operations), Colleen Batman (SVP, Small Commercial & Personal Lines Operations), Samantha Elizondo (VP, STD and Absence Management Claims), Dakota Pelletier (Assistant Director, Operational Modeling and Analytics, WFM, the ex-Cox alumni contact), Jessica Capacete (Assistant Director, EB Customer Contact Center), Jeff Beausoleil (AVP, Transformation & Optimization, Claims & Operations), Tayton Lyon (AVP, Centralized Operations and PI Shared Services).

Each contact carries four per-lead variables written 1:1 for their seat and critic-checked: `opener_line`, `contract_line`, `vm_hook`, `voice_script`. The templates hold only the shared spine. E1 preview verified on a real loaded lead (Foss) and renders fully personalized.

## Defect found and corrected

**Dakota Pelletier (The Hartford) was loaded inside `cam_2gy9hmEvMjYEuPZ8A` "Stars - Fresh Pool / Finance (Nate)"** since Aug 3, the only non-health-plan lead in a Medicare Star Ratings campaign. She would have received quality-bonus-payment copy written for payer finance leaders. Nothing had sent (campaign is draft). She is now loaded correctly into the Hartford blitz as `lea_KvfdCSn3uAXzRE9no`. The stale Stars copy of her is `lea_CFjqC6KwebS3pcMzi` and must be deleted from the Stars Finance campaign before that campaign launches. Not deleted here; destructive actions stay Dallas's hand.

## Enrichment state: COMPLETE, 16/16 with email and direct dial

**The lemlist trial's enrichment credits ran out mid-job.** The Citizens batch consumed them, the Hartford batch silently returned empty rather than erroring, and an explicit retry returned `MISSING_FUNDS` on all 8. This is the single most useful operational finding of the build: a silent empty return looks identical to "no data found," and only the explicit retry revealed it was a funding wall. Any future lemlist enrichment job needs a post-run count check, not a trust of the return.

Enrichment was moved to Clay (`Enrich Person and Find Contact Details`, `function:t_0thx4ojyQd6uNhDf44G`, 12.8 credits per contact, ~128 credits total against a 72,677 balance). Runs `run_0tjd5laEyuJgrfKUswr` (Hartford, 8) and `run_0tjd5tmkNqoqGD5tdhi` (Citizens backfill, 2).

Two lemlist enrichment defects caught, then independently resolved by Clay:
- **Patrick Savage returned `patrick.savage@csn.edu`** from lemlist, College of Southern Nevada, a different person entirely. Clay returned `patrick.savage@citizensbank.com`. Because lemlist had matched the wrong human, its phone for Savage was discarded too and Clay's used instead.
- **Michael Merritt returned nothing** from lemlist. Clay returned `michael.merritt@citizensbank.com` plus a direct dial.

Clay also surfaced two surname mismatches that a pattern-guesser would have got wrong, which is evidence Clay resolved real directory entries rather than inferring: **Stacy Gutierrez's work email is `stacy.stanton@thehartford.com`** and **Tayton Lyon's is `tayton.guio@thehartford.com`**. Both are consistent with a name change. Worth a glance before send, but do not "correct" them back to the surname pattern.

Dakota Pelletier has a direct dial but no email resolved. Her surname pattern is not safely inferable given the two mismatches above, so her email was deliberately left blank rather than guessed. She reaches the phone and LinkedIn lanes and skips the email steps.

## Clay is now the single enrichment source (all 16)

Per Dallas's instruction, every contact in both sequences has been resolved through Clay rather than lemlist. Third run `run_0tjd8joNFZhJMCRAf9G` covered the remaining 6 Citizens contacts that had originally come from lemlist.

**Emails:** 5 of those 6 matched lemlist character-for-character (Foss, Weaver, Higgins, Bartolazo, Soukkala). Two independent sources agreeing is the strongest verification available here. Peg Marty returned no email from Clay; her `peg.marty@citizensbank.com` is retained from lemlist and fits the pattern confirmed by seven colleagues.

**Phones disagreed on three, and this matters because these are the numbers Nathan dials.** Clay's value is loaded as primary (its field is explicitly "Mobile Phone"; lemlist's may be a desk or switchboard line). The lemlist alternates are kept here as fallbacks rather than discarded, so a missed dial has a second number to try:

| Contact | Loaded (Clay mobile) | Fallback (lemlist) |
|---|---|---|
| Jeffrey Foss | +1 910-379-4239 | +1 401-206-9565 |
| Robert Soukkala | +1 813-360-4888 | +1 847-863-6634 |
| Peg Marty | +1 503-806-4712 | none on file |
| Patrick Savage | +1 774-634-7247 | +1 774-992-3294 (discarded, lemlist had matched the wrong person) |

Weaver, Higgins and Bartolazo returned identical numbers from both sources and are unambiguous.

## Final state (end of Aug 6 session)

- **The Hartford: `validate_campaign_readiness` returns READY, zero errors.**
- **Citizens: still returns "Your step must have a specific sender."** Campaign-level senders, the `random` sender strategy, and repeated re-saves of every step type (invite, linkedinSend, voice note, A/B variant B) did not clear it. The same error stands on the pre-existing Stars Finance campaign, so this is an account-wide per-step sender binding that the API surface cannot set. It takes one pass in the campaign editor picking Nathan on the steps. Hartford clearing on its own is unexplained and is not evidence the API can fix Citizens.
- Dakota Pelletier deleted from Stars Finance. Her email (`dakota.pelletier@thehartford.com`) was captured from that record before deletion and written onto the Hartford lead, which closed the last data gap: **16/16 contacts now have both a verified email and a direct dial.** (Committee totals are 8 and 8. An earlier note in this session said 9 Hartford / 17 total; that was a miscount and 8/8/16 is correct.)
- Nathan's callback number (937-238-3179, from his email signature) is written into all four voicemail scripts. No placeholders remain.
- Reply handling set on both campaigns: a reply stops that lead and creates a task, without propagating to the rest of the account so the multithread survives; a booked meeting stops the whole account.
- **lemwarm cannot be activated on the free trial** ("You need a seat to activate lemwarm"). Warmup is therefore blocked on the purchase decision (~Aug 13), not on anything Nathan or Dallas can do now. Worth weighing in the funding case: the trial cannot demonstrate warmed-mailbox deliverability.

## Launch gates, all still closed

1. Assign a specific sender on each step in the lemlist UI. `validate_campaign_readiness` returns "Your step must have a specific sender" on both new campaigns **and on the pre-existing Stars Finance campaign**, so this is an account-wide UI step, not a defect in this build. Campaign-level senders and the `random` sender strategy are already set on both.
2. Replace `[YOUR NUMBER]` in every voicemail script with Nathan's callback number (6 steps across the two campaigns).
3. Nathan records his voice sample so the voice-note steps can move from manual to the AI clone. `teamVoices` is currently empty, so those steps are per-lead recording tasks.
4. Nathan's mailbox has `lemwarmActive: false`. Warmup should be running before a cold wave, and the 40/day send limit is well above this wave size, so volume is not the constraint.
5. Delete `lea_CFjqC6KwebS3pcMzi` (Pelletier) from the Stars Finance campaign.
6. Delete the two TEST leads in Jack's UK campaigns before those launch (pre-existing gate, unchanged).
7. Real-row gate validation immediately before the wave.
8. Confirm the two Hartford `[VERIFY]` figures.
9. Verify with Keegan whether Foss goes by "Jeff" or "Jeffrey" (currently Jeffrey throughout) and take his tribal knowledge on both accounts before launch, per the standing rule that Keegan gets a ping before any account goes live.

---

## Copy-sharpener + seam pass, Aug 6 2026 (applied)

Run after Dallas flagged the Hartford E1 in the lemlist UI. Both blitz campaigns audited against `motions/shared/Variable_Seam_Contract_Aug6.md` (seam-v1.0) and the copy-sharpener gate. Both still DRAFT, zero sends.

**Hard gate failure, fixed.** Hartford E1 variant A closed on "Thought it might be worth **comparing notes** on...". "Comparing notes" is a hard-banned phrase in the house style and in voice_core's banned list. Replaced with "Thought it might be worth hearing how you're holding service steady when the week doesn't match the plan." Citizens was clean on this.

**Seam collision, fixed.** The Hartford E1 spine opened "The pattern I keep seeing across carriers is that...", and Dakota Pelletier's `opener_line` ended "The pattern I see everywhere is that...". Rendered, the prospect read the same construction twice in consecutive sentences. The spine was rewritten to drop the "pattern" frame entirely (also cutting it from 52 to 44 words, bringing E1 inside the 80-120 word spec), and Dakota's opener was rewritten.

**Forbidden word, fixed.** Jeff Beausoleil's opener began "transformation and optimization inside claims is the seat where...", which is both a banned word and the opener rule's ban on narrating the prospect's job back at them. Rewritten.

**Duplicate forcing function, fixed.** Colleen Batman and Stacy Gutierrez, both SVPs in the same account and likely peers, both opened on "small commercial written premium up ~7% last quarter". Colleen keeps the number (small commercial is literally her book); Stacy moved to a P&C-operations-absorbs-the-quarter angle. **This also halves the [VERIFY] surface: only Colleen now carries the 7% figure.**

**Echo, fixed.** Steve Deane's opener ended "claims is the least predictable work in the building" directly before the spine's "automation lands on the predictable work first". Reworded to "on the days claims volume doesn't behave."

Openers left alone as already clean: Tayton Lyon, Samantha Elizondo, Jessica Capacete.

**Brand-light violation, fixed in both campaigns.** On the no-phone/no-LinkedIn branch, E2 fired at **Day 4** while naming Intradiem, inside the Days 1-5 brand-light window. The other two branches land it at Day 6 and Day 8, which is legal. Fixed by delay 1 -> 3 on `stp_BCcEf8PwC4Qn6vZb9` (Hartford) and `stp_ZNej6Ez543J6P5vmu` (Citizens), pushing both to Day 6. Copy untouched.

**Voicemail spec, fixed in both campaigns.** Scripts instructed "Under 30 seconds"; the standard is under 25 seconds (50-60 words). Worse, the fixed frames were 37 words (Hartford) and 41 words (Citizens), leaving almost no room for `{{vm_hook}}`. Frames trimmed to 33 and 31 words, instruction corrected to 25 seconds, and a tie-breaker added: "If it runs past 25 seconds, cut the hook, not the callback line." Steps: `stp_Exk874hWjGJzWJzPx`, `stp_5sNTrLPNrS7xqfobc`, `stp_usi9YgduCawPoMniK`, `stp_oewTS8bXHTpAgwavt`.

**Qualifier, fixed.** Hartford E2's "In my experience that number turns up..." became "That number usually shows up...". Applied to all three copies of the step.

**Ordering trap, closed.** Both campaigns had a live variant-B offer CTA with **no matching note in `Offer_Notes_Aug3.md`**, which is exactly the failure that file exists to prevent: a "yes, send it over" would have got silence. Written and added: note 6 (Hartford, the cheap vs expensive volatile week) and note 7 (Citizens, the human side once deflection gets real). Both pattern-level, zero stats, zero customer names.

**Not a defect, checked.** The stored HTML in both campaigns is correctly `<p>`-wrapped and matches the other five campaigns. The odd spacing and the `{{Contact > firstName}}` chips in the UI are how the lemlist editor renders resolved variables; the underlying tokens are plain `{{firstName}}` / `{{opener_line}}` and they preview correctly on real loaded leads.

### Correction to an earlier finding

An earlier note in `Variable_Seam_Contract_Aug6.md` concluded that lemlist silently discards `message` on a manual voice-note step. **Both blitz campaigns disprove that**: `stp_7QNCWBL6JigjN5Efs` and `stp_r74setWyajvdR2yPm` both hold `{{voice_script}}` in the body and persisted it. The difference is the write path, not the field: these were set at creation via `add_sequence_step`, whereas `update_sequence_step` is what silently no-ops on this field. So the fix for the other four campaigns' empty voice-note bodies is delete-and-re-add, not an update. That is a destructive op on four live-ish drafts and was not done unilaterally.

### Still open on these two campaigns

1. The two Hartford `[VERIFY]` figures, now reduced to: the ~7% small commercial written premium growth (Batman only) and the Chris Swift customer-experience quote (Deane only). Both must be confirmed against the Q2 2026 release before those two send.
2. The build table says 9 Hartford leads; the committee list names 8 and 8 are loaded. Worth reconciling whether a ninth contact was dropped.
3. All nine pre-existing launch gates above, unchanged.

## Launch gates worked down, Aug 6 2026

Re-checked live rather than carried forward as a static list. Four closed, one reframed, four genuinely need a human.

**CLOSED. Gate 1, specific sender per step.** Not a UI job and never was. `set_campaign_senders` documents sender assignment as a campaign-level setting, explicitly "NOT configurable per step". Hartford now returns `status: ready`, zero errors. Citizens still returns the error and the one-line fix was attempted but blocked by the permission classifier, so it needs either Dallas's approval of that call or ten seconds in the UI.

**CLOSED. Gate 8, the two Hartford [VERIFY] figures.** Both confirmed against Q2 2026 coverage:
- Small business written premium growth of 7%, underlying combined ratio 86.5%, driven by double-digit package and E&S binding growth. Management attributed the outperformance to automation investments enabling faster quoting. Batman's opener stands.
- Swift pointed to the company's "commitment to a superior customer experience" and differentiated risk selection as key themes. Deane's opener stands, and it is close to verbatim.
- Bonus finding that strengthens E2: on AI efficiencies Swift named underwriting operations, customer-facing activities **and claims**. The Hartford E2 angle ("a number on the underwriting side, not yet on claims and service") is now better supported than when it was written.

**REFRAMED, and it supersedes most of the others. Gate 4 was recorded as "Nathan's mailbox has lemwarmActive: false".** Live state is worse and simpler: `get_user_channels` returns plan `Freetrial`, `email.connected: false`, `email.available: false`, and `list_mailboxes` returns an empty array. There is no connected sending mailbox on this workspace at all. Warmup is not the blocker; having any email channel is. This ties directly to the unresolved Lemlist paid-seat spend (Matt and Naveen, per `Jack_UK_Engine_Aug3.md`). Note that Hartford still validated as `ready` with no email channel connected, so lemlist's readiness check does not cover this. Do not read `ready` as sendable.

## Variable-layer slop sweep, Aug 7 2026 (applied)

The Aug 6 copy-sharpener pass cleaned the step templates but never reached the per-lead variables. A sweep of all four variables across all 16 leads found five defects, all fixed via `update_lead_variables` (that write path works; it's only voice-note step bodies the API no-ops on):

1. **"compare notes" (hard-banned) survived in three `voice_script` variables:** Beausoleil (Hartford), Savage and Merritt (Citizens). Each close rewritten with a distinct construction so no two scripts share an ending verbatim.
2. **Stacy Gutierrez still carried the 7% figure in `vm_hook` and `voice_script`.** The Aug 6 dedup (Colleen keeps the number) only touched her `opener_line`. Both rewritten to the strong-quarter-lands-a-quarter-later angle with no stat. The earlier claim that "only Colleen now carries the 7% figure" is TRUE only as of this pass; the [VERIFY] surface is now genuinely Batman-only.
3. **Peg Marty's `opener_line` used "transformation"** (banned, same word cut from Beausoleil's opener Aug 6). Now "redesign," which also matches the Citizens call-mix-redesign frame.
4. **Peg Marty's `voice_script` opened a claim with "In my experience"**, the same qualifier the Aug 6 pass stripped from Hartford E2. Now "The hard part usually isn't."

Left alone on purpose: the Tuesday motif (house frame, different recipients), "the pattern I see/keep seeing" in Dakota and Beausoleil voice scripts (the E1 spine no longer uses the pattern frame, so no seam collision), and Deane's "least predictable work in the building" in his voice script (the Aug 6 echo fix was about same-email adjacency; the voice note lands days later on another channel).

The blank AI-voice template on the Hartford main-sequence voice note step takes `{{voice_script}}`, pasted in the UI (Dallas, Aug 7). Citizens' equivalent step needs the same paste when its sender fix happens.

**Still needs a human, and why:**
- Gate 2, `[YOUR NUMBER]` in 6 voicemail scripts. Blocked on one fact: Nathan's callback number. Once supplied this is a single pass across both campaigns.
- Gate 3, Nathan's voice sample for the AI clone. Blocked on Nathan. `teamVoices` still empty.
- Gates 5 and 6, deleting `lea_CFjqC6KwebS3pcMzi` (Pelletier, stale in Stars Finance) and the two TEST leads in Jack's UK campaigns. Destructive, and destructive stays Dallas's hand by standing convention.
- Gate 9, Keegan's tribal knowledge and the Jeff/Jeffrey question. Human.
- Gate 7, real-row gate validation immediately before the wave. Cannot be closed early by definition.
