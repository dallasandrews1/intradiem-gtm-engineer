# Clay Build Audit, L2 Intent Layer, End to End (Jul 12 2026)

Adversarial red-team of the live Clay GTM build and the L2 intent-signal layer. Read-only and credit-safe: no enrichment run, no campaign fired, nothing spent. Verified against the live workspace (1180800, workbook GTM Engine) through the browser, not the docs, then cross-checked by an independent verification pass on the config, scorer, test, spec, and ledger. Where the live build and a doc disagreed, the live build was treated as ground truth and the exact formula text was read from the column editor.

Internal working document. Numbers here are operational, never prospect-facing.

---

## BLUF

This is a genuinely strong head start, and it is not yet at "work of art / status-solidifying," because one real defect and two structural gaps sit between where it is and where it needs to be. The engine's spine is sound: the self-cleaning behavior is real and demoable (a contract at 4.0 zeroes out and drops), the scoring is config-driven, auto-run is off so nothing is charging, the send path is gated, and the provenance discipline holds (no Intradiem-verified numbers are anywhere near the intent layer). That is a credible foundation and most people at week one do not have it.

The three things standing between here and status-solidifying:

1. **A customer can leak into the motion right now.** The live `intent_score` formula self-cleans only on `overall_star_2026 >= 4`. It does not gate on `customer_flag`. Humana, UnitedHealth, and CVS, all active customers, all sub-4.0, are sitting at `intent_score` 15 to 35 with `intent_status = in_motion` in the live table today. The exclusion is a scoping convention, not a formula invariant, and the whole point of the build is that the team runs it without you in the loop. Conventions decay when the person who knows them steps out. This is the one must-fix before any intent-to-outreach wire is built.

2. **The demo thesis is only about 40% true in the live build.** "Real-time signals trigger automated action, and the list self-cleans" is half-built: self-clean is real, but 2 of 5 signals are wired, there is no decay in the live formula (only in the reference scorer), auto-run is off, and there is no signal-to-outreach automation. That is fine as a head start and it is exactly how it should be framed. It is not fine if it gets framed as finished, because a skeptical CRO poke lands directly on the unbuilt half.

3. **There is no closed loop, so there are no receipts.** Today the layer goes signals to intent and stops. Nothing carries intent to outreach to reply to meeting to pipeline, and the ledger tracks credits spent but computes no cost-per-qualified-signal. At renewal or mid-burn, "what did the credits buy" answers in enrichment counts, not qualified replies. Closing that loop is the single highest-leverage upgrade for the exec story.

Fix #1 this week. Reframe #2 honestly (the memory rules already say to). Spec and start #3. Do those and this moves from "impressive scaffolding" to "he runs GTM the way our product runs operations, and here are the receipts."

---

## Update — fixes applied Jul 12 (same day)

The audit findings below are preserved as written. This section records what was fixed the same day. Everything here was done at 0 credits, auto-run left Manual, Save-and-don't-run throughout.

**Applied live in Clay (verified):**

- **R1 (the customer leak) — closed.** `intent_score` and `intent_status` now gate on `(overall_star_2026 >= 4 || customer_flag == "TRUE")`. Verified live: every customer row (Humana, UnitedHealth, CVS) moved from intent 15-35 / in_motion to **0 / excluded**; eligible fallers stay in_motion; eligible-no-signal rows read dormant. The list now has four clean states: excluded, graduated, in_motion, dormant.
- **R3 — hiring corrected** from `> 0` to `>= 3` on the keyword-filtered count.
- **R4 — vestigial columns hidden** (`sig_leadership`, `sig_hiring`, `sig_backlog`).
- **R1 part 2 — run condition** `new_logo_eligible == "TRUE"` added to the Job Openings enrichment so paid runs can never touch a customer. (Leadership Claygent run-condition deferred: applying it required a prompt regenerate that risked altering the tightened prompt; the customer gate already makes its output inert on customers.)

**Applied in the repo (reference side, verified green):**

- **R5 — doc drift fixed**: leadership is 10 everywhere now (config, live formula, spec, test), and demoted to Tier 2. Ledger carries a dated correction (append-only).
- **R6/R7 — scorer reconciled to the live build** (customer gate, new_faller base, motion filter, aligned status labels) and tests expanded from 17 to **37 checks**, now including per-signal point contribution and customer exclusion. All green.
- **I1 — `claims_backlog` moved to the back-office motion.** **I2 — `measure_slippage`** (free, first-party CMS movement) added as the replacement Stars signal. **I5 — leadership demoted to Tier 2.** **U3 — decay** reframed as reference-only + live refresh-expiry. **U4 — motion dimension** added to config + scorer.
- Credit cadence corrected to parent grain (~260/sweep, ~520/mo steady state) in the ledger and config.

**Specced and held (0 credits to build; the one paid step waits on your go):**

- **R8 (parent-grain helper), U1 (closed loop), U4 Clay-side (back-office fork)** — turnkey build steps in `18_L2_NextBuild_Spec_Jul12.md`. The only credit-spending action anywhere is the first parent-grain sweep, pre-estimated at ~260, held for explicit go.

**Ran live Jul 12 (your go):** the first signal sweep on the eligible-only set. The view was filtered to `new_logo_eligible == "TRUE"` (44 accounts, belt to the run-condition) and Job Openings run on "empty or out-of-date rows" so already-enriched rows did not re-charge. Result: the engine produced a live, self-cleaning ranked list on real data. Customers resolve to 0/excluded; eligible accounts resolve to in_motion (e.g. 20/25/15) or dormant (genuine, no current quality-hiring cluster), with named leadership hits (Michael Carson, Halima McRoy, Heather Thiltgen, Gary Culp). Verified spend from Clay's own Usage page: GTM Engine is at **343 credits month-to-date** of the 5,000 allocation (~7%), below the ledger's earlier ~418 estimate. `measure_slippage` is now **built and wired live** (Dallas uploaded the 2025 Star Ratings Data Tables): a `CMS_Star_Movement_25v26` table joins 2025 domain stars (HD5 Customer Service, HD3 Member Experience) + Summary Overall to the 2026 universe by contract_id, a Lookup Single Row + `sig_measure_slippage` formula surfaces the 22/98 that slipped with a QO-addressable soft spot, and a +20 term now fires in intent_score (verified: Clover 20->40 grade_lift, Centene 15->35; customers still 0/excluded). It is the first FREE Tier-1 signal and cost 0 credits. The closed-loop attribution columns stay specced (launch-gated) rather than built empty.

Net: the live build is now correct, safe, clean, and producing a real hot-list. What remains is credit-efficiency (parent helper), the closed-loop receipts (launch-gated), and outreach launch itself (OAuth + approvals).

---

## Errors and risks (must-fix, ranked by severity)

### R1. Customer leak: intent formula does not exclude customers (Critical)

**What I saw.** The live `intent_score` formula on Accounts (Master):

```
Number({{overall_star_2026}}) >= 4 ? 0 :
Math.min(100, ({{new_faller}} == "TRUE" ? 20 : 0)
  + ({{sig_sec_filing}} ? 30 : 0)
  + ({{sig_earnings}} ? 25 : 0)
  + (({{Use AI result}} && String({{Use AI result}}).toLowerCase().indexOf("yes") == 0) ? 10 : 0)
  + (Number({{Job Openings}}) > 0 ? 15 : 0)
  + ({{sig_backlog}} ? 10 : 0))
```

The only kill switch is `overall_star_2026 >= 4`. `customer_flag` and `new_logo_eligible` are never referenced. In the live table, Humana rows (customer_flag TRUE) show `intent_score` 15 to 25 and `in_motion`; a UnitedHealth row shows 35 and `in_motion`; CVS rows show 15 and `in_motion`. These are the exact parents on the Jul 8 customer-exclusion list, sitting live in the motion.

**Why it matters.** The Jul 8 gate from Naveen was customer-exclusion absolute. Today the leak is latent because no wire pushes `in_motion` accounts into outreach yet. The moment that wire is built, by you or by a seller running the engine self-serve, any filter on `intent_status == "in_motion"` or `intent_score > 0` without a parallel `customer_flag` filter sends a Stars-cliff email to a live customer. The failure is invisible until it fires in front of exactly the wrong person.

**Exact fix.** Fold the exclusion into the kill switch so it is a property of the score, not a convention downstream:

```
(Number({{overall_star_2026}}) >= 4 || {{customer_flag}} == "TRUE") ? 0 : Math.min(100, ...)
```

Do the same in `intent_status` (a customer resolves to `graduated`/`excluded`/`dormant`, never `in_motion`). Then also scope every paid enrichment column with a run condition `{{new_logo_eligible}} == "TRUE"` so credits never fire on a customer row in the first place. Belt and suspenders: the formula makes a leaked customer score 0, the run condition stops paying to enrich them. Zero credits to change a formula.

### R2. Paid enrichment already fired on customer rows (High)

**What I saw.** Humana rows carry `Job Openings = 4652` and a leadership "yes Aaron Martin" result. Those are customers. The enrichment did not fully respect the "26 eligible non-customer parents" scope, at minimum the 10-row samples hit customer rows, and the values are now stale sample-era data feeding the live score.

**Why it matters.** Two harms. Credits were spent enriching accounts that can never convert (small in absolute terms so far, but it is the pattern that scales badly). And those stale values are what light up the R1 leak. The Humana `4652` is the pre-keyword, unfiltered total from the sample run, not a quality-role count.

**Exact fix.** After R1's run-condition scoping is in place, clear or re-run the enrichment on the customer rows so they hold no signal values, and confirm no customer row shows a non-blank `Job Openings` or `Use AI result`. Net cost to clear: 0 (blanking is free; only re-enriching the eligible set costs).

### R3. Hiring signal fires on `> 0`, not the specified `>= 3` cluster, and reads the raw total (High)

**What I saw.** The formula uses `Number({{Job Openings}}) > 0 ? 15`. The config and spec define this signal as "count >= 3 relevant reqs in trailing 30 days" and name it `quality_hiring_cluster`. So a single opening fires the full 15 points, and on the stale customer rows it fires off the unfiltered all-roles total (4652), not the keyword-filtered quality count.

**Why it matters.** The signal labeled "cluster" is implemented as "any." It is noisier than specified, and on stale rows it is firing off the wrong column entirely. Under scrutiny, "why does one job posting equal a hiring cluster" is an easy hit.

**Exact fix.** Change the threshold to `>= 3` to match the config, and point the term at the keyword-filtered count column, not the raw `Job Openings` total. If you want to keep a lower bar deliberately, change the config and the label to match reality (`quality_hiring_signal`, `>= 1`), so the name, the config, and the formula all agree. Config edit plus one formula edit, 0 credits.

### R4. Two signal inputs are vestigial and will confuse a live demo (Medium)

**What I saw.** `intent_score` shows "Referenced columns (7)" and reads `{{Use AI result}}` for leadership and `{{Job Openings}}` for hiring. The `sig_leadership` and `sig_hiring` checkbox columns are not referenced by the formula at all. They are dead inputs. Meanwhile `sig_sec_filing`, `sig_earnings`, and `sig_backlog` are still live manual checkboxes. So the input model is mixed: three manual checkboxes plus two enrichment columns, plus two orphaned checkboxes that do nothing.

**Why it matters.** In a live walkthrough, "what does this sig_leadership checkbox do" has no clean answer, and mixed input models are a maintainability tax on a self-serve engine. A seller toggling `sig_hiring` expecting it to change the score will be confused when it does not.

**Exact fix.** Hide or delete `sig_leadership` and `sig_hiring` (the formula ignores them). Add a one-line column description on `intent_score` stating which columns are the live inputs per signal. Pick one input model per signal and document it. 0 credits.

### R5. Documentation drift: leadership weight, in three places, is stale at 20 (Medium)

**What I saw.** The config sets `quality_leadership_change = 10` (dropped from 20 on Jul 11, with the reason noted in-file). The live formula correctly uses `10`. But the spec `16_L2_Signal_Monitoring_Spec` table still says `20`, the Jul 11 ledger entry says "+20", and the test's cap comment reads "30+25+20+15+10 = 100" which assumes 20 (the true sum at 10 is 90). The live build is right; the paper trail is wrong.

**Why it matters.** Config-over-code is a house rule and the config is correct, so the engine behaves right. But three artifacts that a reviewer might read disagree with the running system. In a high-scrutiny role, a reviewer who reads the spec and then the table will think the build is wrong when it is the doc that is stale.

**Exact fix.** Update the spec table to 10, correct the ledger note (append a correction line, do not rewrite; the ledger is append-only), and fix the test comment. Add one assertion that actually checks leadership contributes 10, since right now nothing does (see R6). 0 credits.

### R6. The test does not actually cover the leadership weight or customer exclusion (Medium)

**What I saw.** `test_l2_intent_scorer.py` passes 17/17, but the cap test passes via an appended duplicate `sec_filing` regardless of leadership's value, so changing leadership 20 to 10 fails zero assertions. There is also no test for customer exclusion, because the scorer has no customer logic to test.

**Why it matters.** Green tests are giving false comfort on exactly the two values that matter most for correctness and for the R1 leak. A silent config change to a point value would not be caught.

**Exact fix.** Add an assertion that isolates each signal's point contribution (one signal fired, assert the exact score), and, once the scorer mirrors the live customer gate (see R7), add a customer-exclusion assertion. 0 credits.

### R7. Reference scorer and live build have diverged (Medium)

**What I saw.** The Python scorer is supposed to mirror the live Clay column, but three things differ: the scorer has no `new_faller +20` base (the live formula does), the scorer applies recency decay (the live formula does not), and the scorer has no customer gate (neither does the live formula, but once R1 is fixed the live one will and the scorer still will not). The status vocabularies also differ (scorer emits active/dormant/graduated; the live column emits graduated/grade_lift/in_motion/dormant).

**Why it matters.** The scorer is the thing you demo when you say "here is the logic, proven before the paid columns are live." If it computes a different number than the live table for the same account, the proof is undermined the moment someone checks both.

**Exact fix.** Reconcile the scorer to the live formula: add the `new_faller` base, add the customer gate, align the status labels, and either add decay to the live build or drop it from the scorer (see U-note on decay in Upgrades). Keep the config as the single source both read. 0 credits.

### R8. Contract-grain scoring double-pays for parent-level facts (High, credit)

**What I saw.** Accounts (Master) is 98 contracts across 26 parents. Every L2 signal (SEC filing, earnings, leadership, hiring, backlog) is a parent-level fact, but the enrichment runs per contract row. Humana's job-openings number is fetched and paid for on each Humana contract, not once for Humana. The ledger already caught the smaller version of this ("est assumed 26 parents, table is contract-grain, actual came in ~40% over").

**Why it matters, with the math.** Using the config's own per-account estimates (sec 3, earnings 3, leadership 2, hiring 2, backlog 2 = 12 credits for the full 5-signal sweep):

- Contract grain, 98 rows: 98 x 12 = **1,176 credits per full sweep**
- Parent grain, 26 rows: 26 x 12 = **312 credits per full sweep**
- The ratified monthly-full estimate in the ledger and config: **~400**

The ~400 estimate is only consistent with parent grain. Run the monthly sweep as the table stands and it costs roughly 1,176, about 3x the plan, and the headline "~800 per month steady state" is optimistic by roughly 2x. Still inside 5,000, but the number you are quoting Naveen is wrong against the live table.

**Exact fix.** Build a 26-row parent-grain helper table (one row per `parent_key`), run the paid signal enrichments there once, and lookup the result back onto the 98 contract rows (Clay-internal lookups are free). This cuts the parent-level signal spend by roughly 70% and makes the ~400 estimate true. It also fixes the "same parent enriched N times" waste permanently and scales cleanly to more contracts.

---

## Improvements (should-do, ranked by effort vs impact)

### I1. Replace `claims_backlog` in the Stars motion with a Stars-native signal (low effort, high impact)

`sig_backlog` (claims backlog) is a back-office operational signal. The config itself labels it "back-office adjacency." It does not belong in the Star Ratings cliff intent score: a claims backlog does not make a Medicare plan a better Stars-cliff target, it makes it a better back-office target. Move it to the back-office motion's intent config (where it is the right signal) and replace it here with something that actually predicts Stars movement. Config edit, 0 credits.

### I2. Add the signal you already own and are not using: CMS measure-level movement (low effort, highest signal value)

The strongest, cheapest, most deterministic Stars signal is the tiered CMS file you already hold. Measure-level movement (a plan slipping on CAHPS, complaints, or the call-center measures QO touches) is free, first-party, and directly on-thesis, yet the intent layer spends credits on directional AI leadership guesses and ignores it. Add a `sig_measure_slippage` term computed from your own data. This is the single highest-value calibration change and it costs nothing to run.

### I3. Add a WFM/CCaaS tech-stack-change signal (medium effort, high impact)

A plan switching or expanding Verint, NICE, Calabrio, or Genesys is a direct QO-adjacent buying trigger, arguably stronger than an SEC filing. Clay's Website Techstack enrichment is ~2 credits per row and would slot in as a native column. It also feeds the competitive-intel play. Add as a Tier 2 signal.

### I4. Rebalance the point weights (low effort, medium impact)

SEC filing (30) and earnings (25) together own 55 of the point budget, but they only apply to public parents (Humana, CVS, Centene, Elevance, Molina, Clover, Alignment). Most of the 26 eligible parents are Blues and provider-sponsored plans that will never trip a public-company signal, so their achievable ceiling is capped at the smaller signals plus the faller base. Lower the SEC/earnings weights or add a "public parent" flag so the score is comparable across the universe rather than structurally favoring the handful of public names.

### I5. Demote or hard-verify the AI leadership signal (low effort, medium impact)

The leadership signal is AI web research and known to over-call recency (the live table shows "yes Aaron Martin" for Humana, and Aaron Martin reads more like an existing growth exec than a dated new quality appointment, which is the exact over-call the config note warns about). It is currently Tier 1, meaning a directional AI guess can fire an account into outreach. Either demote it to Tier 2 (raises priority, does not fire) or require a human verify before an account it fired enters outreach. The prompt tightening helps but does not make an LLM date-check reliable.

### I6. Fix the contacts-lookup errors feeding grade (low effort, data integrity)

Several parents (cloverhealth, elevance, cambiahealth, vnshealth) show "Error: We were unable to..." on the Lookup Multiple Rows column, which drops `decision_maker_found` to FALSE and grades them C. Worth a look: are those genuinely uncovered, or is the join key mismatching. If it is a key mismatch, real targets are being under-graded.

---

## Upgrades and work-of-art moves (could-do, ranked by C-suite narrative impact)

### U1. Close the loop: intent to outreach to reply to meeting to pipeline, with attribution (highest)

This is the biggest gap and the biggest prize. Today the layer stops at intent. The work-of-art version wires: `intent_status = in_motion` (and the R1 customer gate) tiers which contacts get sequenced; the sequencer's reply and meeting events write back onto the account as realized outcomes; and a rollup computes cost-per-qualified-signal per motion. That single addition turns the whole build from "a smart list" into "a measurable revenue engine," and it is the exact thing that lets you answer "what did the credits buy" in replies and meetings instead of enrichment counts. It also directly instantiates the Intradiem thesis: a signal triggers an action, the outcome is measured, the measurement tunes the next action.

### U2. Self-improving signal governance (high)

Once U1 exists, you can measure which signals actually predicted replies. Feed that back into the config: signals whose cost-per-qualified-reply runs worse than 3x the portfolio average for two weeks get downgraded to sampled use or killed (the credit-steward kill criterion). Now the intent model tunes itself on outcomes, which is a story no one else at week one is telling.

### U3. Make "self-cleaning" airtight and visible, and make the decay claim honest (high, cheap)

The self-clean is the strongest live proof you have, so make it bulletproof and put it on screen. Add the customer gate (R1) so it self-cleans on both graduation and customer status. And resolve the decay mismatch: the live build has no decay, so either add a lightweight staleness mechanism, or reframe the live claim as "refresh expiry" (a signal stays hot only while the monthly re-run still returns it) and reserve the linear-decay model for the reference scorer. Right now "it decays" is a claim the live build cannot demonstrate, and a CRO who asks "show me" should get a yes, not "that part is in the Python version."

### U4. Give the layer a motion dimension before back-office (medium, prevents a rebuild)

The config is single-motion (Stars). The back-office motion (Mandate 3, the Scott Kemme ICP work) needs its own signal set, where `claims_backlog` is central and Stars signals are irrelevant. Add a `motion` key to the config now so the same scorer serves both from one file, rather than forking the whole thing later. This is the difference between scaling by adding a config block and scaling by rebuilding.

---

## Punch-list (ordered, with credit estimates)

Everything below that spends is flagged. Nothing here was run during the audit.

1. **Add the customer gate to `intent_score` and `intent_status`** (R1). Formula edit. **0 credits.** Do this first, before any intent-to-outreach wire exists.
2. **Add run condition `new_logo_eligible == "TRUE"` to every paid enrichment column** (R1/R2). **0 credits** to configure; caps future spend.
3. **Blank the stale enrichment values on customer rows** and confirm no customer row carries a signal value (R2). **0 credits.**
4. **Change hiring term to `>= 3` and point it at the keyword-filtered count** (R3). Formula edit. **0 credits.**
5. **Hide/delete `sig_leadership` and `sig_hiring`; document live inputs on `intent_score`** (R4). **0 credits.**
6. **Fix the leadership-weight drift in spec, ledger (append correction), and test comment** (R5). **0 credits.**
7. **Add per-signal contribution assertions and a customer-exclusion assertion to the test** (R6). **0 credits.**
8. **Reconcile the reference scorer to the live formula** (new_faller base, customer gate, status labels, decay decision) (R7). **0 credits.**
9. **Build the 26-row parent-grain helper table and lookup back to contracts** (R8). Free lookups. **First real parent-grain full sweep estimate: ~312 credits** (26 parents x 12), versus ~1,176 at contract grain. Pre-estimate and log before running; held for explicit go.
10. **Swap `claims_backlog` out of Stars into back-office; add `sig_measure_slippage` from your own CMS file** (I1/I2). Config edit. **0 credits** (first-party data).
11. **Delete the stray empty draft campaign I created during the audit** (named "2026-07-12 New campaign"; it is Draft with no leads and cannot send, but it is clutter I introduced). **0 credits.** Flagged in full disclosure below.
12. **Re-verify the two Stars QBP Wave 1 campaigns are Draft and unlaunched before any launch day**, as a standing pre-flight (the send path is gated and auto-run is off; this is a habit, not a fix). **0 credits.**
13. **Spec the closed loop (U1)** and add the `motion` key to config (U4). Design work. **0 credits** until the sequencer writeback runs.

Sequencing note: 1 through 8 are free formula/config/test hygiene and should land before the next paid run. 9 is the first spend and it should wait for explicit go, pre-estimated at ~312 for a full parent-grain sweep. Steady-state at parent grain lands near the ratified ~800/month; at contract grain it does not, which is why 9 comes before any recurring cadence is switched on.

---

## The status read

The plan being stress-tested: this Clay build plus L2 layer is what gets the C-suite (the Jul 16 Norton room, Tom Russell, Chris Busbee, and Naveen behind them) seeing a long-term future with you. Here is the honest pre-mortem on that.

**Failure most likely to actually happen: a customer email goes out.** Six months from now, the engine is running self-serve the way it is supposed to. A seller, or you on a fast day, builds the obvious wire: sequence the `in_motion` accounts. Because the exclusion lives in a scoping convention and not in the score itself, the `customer_flag` filter gets left off one time, and a Stars-cliff email lands in a Humana or UnitedHealth inbox, an active account. The thing that made the build impressive, that the team runs it without you, is the thing that fires the failure, because the guardrail was in your head and the runbook, not in the formula. Naveen's one hard condition from Jul 8 was customer-exclusion absolute. This is the failure that does real damage, and R1 closes it for zero credits. Do it before anything downstream reads intent.

**Failure that quietly caps the upside: the demo gets oversold and the poke lands on the gap.** The thesis is compelling and half-built, which is the correct state for week one. The risk is not the state, it is the framing. If the Jul 16 room hears "it is built" and then Chris or a skeptical CMO asks "show me a signal firing and triggering the action," the honest answer today is "that half is staged." The self-clean demos beautifully; the automated-action half does not exist yet. Framed as a head start with a visible roadmap, that is a strength and it reads as momentum. Framed as finished, the gap becomes the story and the credibility cost is real. The memory rules already say never to use finished-product framing; this is the meeting where that rule earns its keep.

**Failure that shows up at renewal: no receipts.** The credit story is currently "spent, tracked, disciplined," which is good stewardship, but when Naveen asks "what did the credits buy," the ledger answers in enrichment counts and a free-text yield note, not in qualified replies and meetings, because the loop from intent to outcome is not wired and there is no cost-per-qualified-signal. Stewardship without receipts is a weaker renewal ask than it should be. U1 is what converts it.

**Red team on the defenses.** The current defense against the leak is discipline and a runbook, and it will not hold, because the explicit design goal is to take you out of the loop, and a convention only survives while the person who holds it is in the loop. The tell, watch for it, is the first time anyone builds a view or a sync that filters on intent without also filtering on `new_logo_eligible`. The current defense against oversell is your own instinct and the memory rules, which do hold as long as you carry them into the room; the tell is any slide or sentence that says "built" or "live" about the automated half. The current defense against the receipts gap is the ledger, which is honest but measures inputs; the tell is the first readout where the strongest number you can quote is credits spent rather than meetings sourced.

**Uncontrollable risk.** Whether October's CMS release moves parents out of your universe is not yours to control; a third of the prior seed already graduated on the 2026 ratings. You cannot solve it, you can only build the re-pull into the cadence so the list is current the day it matters and never argue a stale universe in front of the room.

**If you do nothing else this week:** ship R1, the customer gate in the two formulas. It is the one defect that can cause real harm, it is the one Naveen explicitly asked you to guarantee, and it costs zero credits. Everything else on the punch-list improves the build; R1 protects it.

**Confidence: Moderate, trending High.** The foundation is real and most of the fixes are free formula and config hygiene you can land fast. What tips it from Moderate to High is not more building, it is closing the loop (U1) so the story is measured, and holding the head-start framing in the Norton room so the half that is staged reads as roadmap, not as gap. Do the punch-list in order and this becomes the build that solidifies your standing rather than the one that exposes it.

---

## Full disclosure on the audit itself

During the campaign-status check I clicked "Create Clay email campaign," which created a new empty draft named "2026-07-12 New campaign" (Draft, no leads, no sender, cannot launch). It is harmless but it is clutter I introduced, so it is on the punch-list to delete (item 11). I did not delete it myself because it counts as data removal in the workspace and that is your call, not mine. Auto-run remained Manual on both tables throughout, and no enrichment or campaign was run. The existing send path is gated (send_ready HOLD, human_approved unchecked) per the build record; item 12 is a habit to re-verify that on launch day, not a defect found.

**Lenses applied:** cognitive-calibration (build/strategy mode, show-the-math on credits, ruthless single-signal choice, no empathetic softening of hard findings), strategic-premortem (the status read above), clay-credit-steward (contract vs parent grain math, cost-per-qualified-signal gap, kill criteria for U2), intradiem-verified-metrics (confirmed the L2 layer carries no Intradiem-verified numbers; QBP figures are labeled public-CMS analysis; keep intent-driven outreach routed through the send-gate verified-claims critic), intradiem-backoffice-icp (claims_backlog belongs to the back-office motion; the config needs a motion dimension before that motion stands up). Independent verification subagent confirmed all nine file-level drift claims against the actual files and the passing test.
