# Clay Golden Standard
**The transferable engine standard for every Intradiem GTM motion. Dallas Andrews, GTM Engineer.**

## How to use this
This is the canonical, version-stable standard for how a motion is built in Clay. Start here before building any new motion or opening any build thread, so nothing here gets reinvented per thread. It captures what transfers across every motion: the architecture, the wiring, the rules, the discipline, and the hard-won gotchas. What it deliberately does NOT contain: the aspects unique to each motion (universe source, persona pains, product angle, proof, and the exact MessageGen prompt text), which are worked per motion in that motion's own build prompt.

Two source-of-truth rules that override this doc where they conflict:
- The live Clay workspace is ground truth for any live column, formula, or count. This doc describes the pattern; the workspace is the instance.
- The MessageGen system prompt is a separate maintained artifact (`Clay_MessageGen_SystemPrompt_v2.md`; the live Clay column is canonical). This doc states the rules a MessageGen prompt must follow, never a frozen copy of its text or version.

---

## 1. Operating model
- **One motion = one workbook (ratified 2026-07-15).** Every motion gets its own Clay workbook (`Back Office Motion` is the precedent; `Cost-Mandate Motion` follows). Its universe, contacts segment, MessageGen + critic columns, and campaigns live there. Shared, static assets (Verified Metrics, Product-Angle Map, ICP Rubric, the customer exclusion file) are referenced by Lookup where cross-workbook lookups work, or seeded as small copies where they don't (verify in the current UI, never assume). The closed loop stays unified through `source_motion` tags, the ledger, and the readouts, never through table adjacency. Rationale: a clean room per motion beats reuse-by-proximity; the critic/gate/campaign wiring is a copy-paste pattern, not shared infrastructure.
- **The repo engine is config + reference scorer + tests ONLY, never a parallel build.** Points, tiers, thresholds, triggers, persona routes, and proof rules are decided once in the engine's config (with per-motion overrides, the Back Office fork pattern) and proven by the reference scorer's tests. Clay formulas, prompts, and critics are transcriptions of that ratified config, not fresh decisions made in a column editor. Do not maintain a second implementation of contacts, campaigns, or enrichment logic in the repo; that is where drift is born (the v2.2.1/v2.2.3 MessageGen split is the documented cost).
- **Files first, Clay once.** Draft every formula, MessageGen prompt, critic, and sequence as a file at the project root, then transcribe into Clay in one pass and verify live. The Clay UI is the most expensive surface to iterate on; a logic bug caught in the scorer or a file costs seconds, the same bug caught in a live column costs a sandbox round-trip (the 2026-07-15 intent_status bug is the reference case).
- **Native Clay tables are the engine.** The living, auto-updating motion (tables writing into tables, conditional runs, scheduled refreshes) exists only as native tables built in the Clay UI. That is where the motion runs and where reps consume it.
- **The Clay MCP is a complement, not a builder.** It does find/enrich/read for ad-hoc work. It cannot create tables, and Audiences is disabled on this workspace, so it cannot read the built tables either. Build and read the live tables via Chrome. Never invent a number from a table the MCP cannot actually see.
- **CSV import is a one-time seed,** to stand a native table up from an external file. After the seed the native table owns the data and keeps it fresh. Re-exporting CSVs as a way of working produces snapshots that die when the market moves, the exact thing the engine exists to beat.
- **Verify the current Clay UI before any click-by-click.** Clay's UI and per-provider pricing change. Do not instruct steps from memory. (Example that already moved: row-moves are "Send Table Data" under the table Actions menu, not a "Write to Table" column.)

---

## 1.5 The build labor map (agent vs. human)
Every motion build divides into three tiers by who can own the work. Know the tier before you start so no one rediscovers the Clay ceiling per motion. The standing goal is to push work UP into Tier 1 and shrink Tier 3 to its irreducible minimum, never to automate Tier 3's clicks. This section makes the division an explicit rule; it is not per-motion tribal knowledge.

- **Tier 1 — Agent-owned, fully (the files).** Config (points, tiers, thresholds, persona routes, proof rules), the fit and intent formulas, the MessageGen prompt, the companion critic, the scaffold re-point spec, and the full build pack. All authored as files at the project root, then transcribed to Clay in one pass ("files first, Clay once," Section 1). This is roughly 80 percent of a motion and has no platform ceiling. If a decision is being made in a Clay column editor instead of a file, it is in the wrong tier: move it to a file, ratify it, then transcribe.
- **Tier 2 — Agent-buildable via API / MCP, with caveats.** The logic graph: Clay workflows and the shared Functions. Proven live, not aspirational: the Cost-Mandate workflow was built through the API (`wf_0tiane7qgXQ6PH9UdBA`) and the seven shared Functions are MCP-callable from Cowork. The caveats that keep this out of Tier 1 are real and documented: agent-nodes derive their required inputs from `{{token}}` text rather than an input schema, so their pins must be bound in the UI (the node-6 blocker); and `snapshots restore` re-IDs every node and breaks `inputRef`s, so recovery is always fix-forward on the live graph, never restore. Agents get the graph most of the way; a human finishes the UI-only bindings.
- **Tier 3 — Human-only residue (the platform wall).** Clay has no create-table API, so agents cannot create tables, and with Audiences disabled the MCP cannot even read the built ones. Also human-only: pin-binding agent-node inputs, flipping any send or sync gate, and verifying live counts and `Sent At`. This tier is irreducible. Do not spend agent turns fighting the API to do it; the five failed `edit_node` pin attempts are the documented cost of trying.

**How the tiers collapse a motion to minutes of human Clay work.** Tier 3's table-creation wall is beaten by reuse, not automation: keep one canonical golden scaffold per motion-family (structure, never data), have the agent fill it via the build pack, and a human Duplicate-tables it and re-points the few motion-specific things. The mechanism and its SOP already exist: `Clay_Motion_Scaffold_SOP_v1.md` (structure) plus `Motion_Workflow_Build_Prompt_TEMPLATE_v1.md` (logic). The governing rule this encodes: **agents produce the complete, correct build; the human does only what the platform reserves for a human** — duplicate the scaffold, bind the agent-node pins, verify live, approve the send.

---

## 2. The 8-layer architecture (L0 to L8)
Every motion is these layers. Build the rails once; most layers are reused across motions, only the front half is motion-specific.

```
L0  SOURCES        CMS / Install-Base / Signal feeds        [motion-specific]
L1  ACCOUNTS       Accounts Master (fit + intent + grade)   [motion-specific rows, shared table]
L2  SIGNALS        Intent layer, writes back to Accounts    [motion-specific signals]
L3  CONTACTS       Buying Committee (persona + valid email) [motion-specific segment, shared table]
L4  MESSAGING      Message Gen + companion critic           [motion-specific prompt, shared pattern]
L5  QA / APPROVAL  Send Queue (critic gate + human approve) [SHARED infra, reuse]
L6  DELIVERY       Outreach Sync + Deliverability gate      [SHARED infra, reuse]
L7  CLOSED LOOP    Reply & Meeting Sync -> Attribution       [SHARED infra, reuse]
L8  REP HANDOFF    AE Assignment -> AE Worklist              [SHARED infra, reuse]
Reference tables:  Verified Metrics · Product-Angle Map · ICP Rubric · Variant Library  [SHARED, build once]
```

The rule this encodes: a new motion builds L0 to L4 (its sources, its scored accounts, its signals, its contacts segment, its message prompt + critic) and REUSES L5 to L8 and the reference tables by tagging rows with `source_motion`. Do not rebuild the egress, deliverability, attribution, or worklist per motion.

---

## 3. Wiring mechanics (the only three connective column types)
- **Send Table Data** (formerly "Write to Other Table"): under the table's **Actions** menu, not the Add Column list. Sends rows one table into another (create/append). "Send row" per row, or "Flatten Lists" to split a list into one row each. Filter the source view first to control which rows go. Flow is linear (A to B to C, no loops back); any write-back to source goes through the CRM or a webhook, not a Clay table pointing at itself.
- **Lookup**: reads a value from another table by a join key. This is how reference tables and write-backs work.
- **Conditional run + only-run-if-empty**: gates every enrichment so credits never fire on out-of-window, out-of-ICP, already-filled, or customer rows. This is what makes the engine cheap enough to run continuously.

Chain them for depth: Accounts (write if grade >= C) to Contacts (write if email valid) to Send Queue (write if approved) to Outreach Sync (reverse webhook) to Contacts.reply_status (lookup) to Attribution.

---

## 4. Account + intent layer standard
- **Fit score then grade.** `fit_score` (0 to 100) is a per-motion formula; `grade` buckets it with intent: A = fit and intent both high, B = fit high, C = mid, D = drop. Weights live in config, confirmed with the owner, never hardcoded.
- **Intent is a point-scored signal set.** Each signal is one column that outputs its point value when it fires. Tiers: **Tier 1 fires outreach**, **Tier 2 raises priority within the fired set**, **Tier 3 is context only** (lifts grade, no auto-fire). `intent_score` sums the fired points (cap 100); `top_signal` names the freshest.
- **The customer-exclusion kill switch lives inside the score itself,** not just as a downstream convention: `intent_score` and `intent_status` both zero/exclude when `customer_flag == TRUE` (or the motion's graduation condition). Belt and suspenders: also put a `<eligible> == TRUE` run-condition on every paid signal column so credits never touch an excluded row. A self-cleaning list stays honest without manual pruning.
- **Cost control is parent-grain.** Run paid signals once on a parent helper table and look the result back onto contracts/rows (Clay-internal lookups are free). Contract-grain paid runs cost roughly 3x. Staleness is approximated by refresh-expiry (a signal stays hot only while the scheduled re-run still returns it), not in-formula decay.
- **Config over formula.** Points, tiers, thresholds, and the active-motion switch live in a JSON config, never in the Clay formula text.

---

## 5. Contacts + attribution standard
- **ICP-filtered find-people,** limited N per account, with a `persona_match` AI column (Primary / Secondary / Out) and a drop-out-of-ICP conditional so credits stop on Out rows.
- **Email waterfall with a hard reject:** provider A, then B only-if-empty, then pattern+verify only-if-empty, then `email_status`; reject the row if not valid before any send.
- **The three attribution tags are set at creation and read-only after:** `gtm_engine_sourced`, `source_motion`, `sourced_date`. This is where the credit war is won or lost; never let a downstream step overwrite them. They also write to Salesforce on approval.
- Plus `reply_status` (the credit line, written back by the reply-sync agent) and `variant_id` (experiment tracking).

---

## 6. Messaging standard (rules only; the prompt is a separate artifact)
The exact MessageGen prompt text and its version live in `Clay_MessageGen_SystemPrompt_v2.md` and, canonically, in the live Clay column. This section is the transferable contract any MessageGen prompt must satisfy, regardless of version:
- **A token/column map:** the prompt reads named tokens fed from real columns (identity, the account's why-now, the persona routing field, an approved-claims-only `product_angle`, and a `source_motion` guardrail that errors if wrong).
- **Persona routing from job_title:** each persona leads differently (the economic buyer leads with the number as stakes; the operational buyer leads with the mechanism, number late).
- **A core position never violated:** the one idea the motion sells, and what it deliberately concedes to stay credible.
- **Number discipline:** the only numbers allowed are the prospect's own (attributed, labeled as estimates where modeled) or a verified-repository stat with correct attribution. Never invent, round up, reassign, or split a figure. **Block-on-empty:** if the personalizing number is missing, do not fall back to a weaker or invented one; fall back to qualitative framing with no number.
- **A companion critic** audits every draft for figure integrity and FAILs on any non-source or misattributed number. The sync run-condition carries `msg1_critic == "PASS"` so a FAIL can never sync. The repeatable gate is: regen, critic audit, sync only on PASS, verify per row.
- **Reads the reference tables** (Verified Metrics, Product-Angle Map, ICP Rubric, Variant Library) so claims stay approved and the angle stays persona-correct.
- **Output format is fixed** (subject cap, body length band, no signature block, no preamble), and every copy rule in Section 8 is hard.

Motion-specific: the actual prompt text, the persona lead structures, and the number tokens are built per motion, to this contract.

---

## 7. Personalization layers (individual-level, including the LinkedIn recent-post hook)
Account-level personalization (the why-now, the fired signal, the number) makes a message relevant to the company. Individual-level personalization makes it read as written for this person, and it is the layer that lifts reply rates once the account layer is solid. The strongest and safest source of it is the prospect's own words.

Personalization hierarchy, highest priority first:
1. The prospect's own disclosure or event (earnings language, a filing, a stated target, a role change). Their own disclosure always beats our observation.
2. The account-level signal and number (the fired trigger, the why-now, the personalizing figure).
3. The individual hook: the prospect's own recent, relevant LinkedIn post or share. This is the layer that says we pay attention to the person, not just the company.

**The LinkedIn recent-post column (`li_recent_post_hook`).** A Clay enrichment ("Get a person's professional posts and shares") pulls a prospect's recent professional posts, relevance-filtered to the motion's theme, and feeds a one-line hook token into MessageGen. Rules:
- **Optional input, always.** Set the enrichment and its MessageGen chip "Required to run" to OFF. Many prospects have no recent posts; with it required, those rows hard-fail "Some inputs missing" and can wipe an existing draft on re-run. This is the single most common way the feature breaks (see gotchas).
- **Relevance filter, not recency alone.** Only surface a post genuinely tied to the motion's pain or theme (staffing, cost, service quality, a reorg, a mandate). Never reach for an off-topic post (a work anniversary, a conference selfie) to seem personal; an irrelevant reference reads worse than none.
- **Block-on-empty for the hook.** If there is no relevant post, the message runs on the account-level personalization alone. Never fabricate or paraphrase a post the prospect did not make, and never imply you read something you did not.
- **One sentence, as the opener when present.** The hook opens and hands off to the single idea; it never becomes the message. It carries every copy rule (no em dashes, contractions, no "great post" flattery).
- **Per contact, not per account.** Each person's posts differ, so this is what keeps two committee members at the same account seeing genuinely different, individually-attentive messages rather than one template with a swapped name.
- **Safe on verified-claims.** The post is the prospect's own content, so referencing it sits inside their disclosure, the same reason the why-now and earnings language are safe. It does not touch the Intradiem-number rules.

Where it lands: strongest on the LinkedIn touches (the connection request and the follow-up message, where reacting to a post is native) and on the Email 1 opener; later touches lean back on the account angle. Run the posts enrichment as a paid per-contact column, run-conditioned on the same eligibility and fit gate as the rest of the enrichment so it never fires on excluded or unscored rows.

---

## 8. Copy house-style (hard rules, every prospect-facing draft)
- **No em dashes anywhere.** Use periods, commas, colons, or restructure. (This is a banned character in the critic gate.)
- **Contractions always.** Uncontracted "I would / I am / you will / that is / do not / cannot" are AI tells and are treated as such by the gate.
- **One idea per message.** Everything supports the single idea or gets cut.
- **Front-load.** The point lands in the first sentence.
- **The prospect is the hero.** Their team closes the gap; we are the instrument. Never "we transform your...".
- **The meeting is their idea.** Never ask for time. Offer the artifact (the math, the one-pager, the breakdown). The natural-CTA pattern is "thought it might be worth ___. Have 15 min ___?".
- **Brand-light.** Intradiem appears at most once, and stays out of the first touches entirely on multi-touch sequences.
- **Banned phrases** (kept in `copy_standards.json`, edit there): "I would value" / "I'd value" / "would value connecting", "trade notes" / "compare notes" / "pick your brain", "touch base", "circle back", "deep dive", "I'd love to", "happy to", "hope you're well", "I know you're busy", "companies like yours", "leaders in your space", "I help organizations". Also banned as jargon: agentic, seamless, transform, leverage, synergy, streamline, alignment, game-changer, orchestrate (as a verb), journey, unlock, empower, revolutionize.
- **No flattery openers, no "hope you're well", no "I noticed that" filler. No self-narration.**
- **A held draft goes back through the first-draft-engine, not a one-word patch.** Samples are shown as real emails signed by the sending rep, never as a template.

---

## 9. Verified-claims discipline
- **The Value Repository is the single source of truth** for any claim that may appear in prospect copy. A claim not in it does not ship. Never cite a number from memory.
- **Three tiers:** VERIFIED (citable, source attached, approval tier noted), DRY-RUN (internal demos only), DO-NOT-SEND (known placeholder, listed so nobody reintroduces it).
- **Approval tiers:** 1:1 vs 1:many. Public/estimate figures carry the label and the humility clause ("you'll know the exact picture far better than I do").
- **The gate lives in two places with the same wording:** `config/proof.json` (repo) and the Clay critic column. They must never diverge.
- Currently the only VERIFIED customer story is Humana. Everything else customer-specific stays DO-NOT-SEND until it lands in the Repository with a source.

---

## 10. Sequence standard
- **Five-touch, multi-channel, across about nine business days** from each contact's entry: Email 1 (opener, 2 to 3 signal-assigned variants), LinkedIn connection request, Voicemail + LinkedIn message same day, Email 2 (a genuinely new angle, never a recycled Day 1), Breakup email.
- **Merge-field driven** so MessageGen personalizes per lead. **Per-touch angle shift.** **Signature discipline:** first name on the early touches, full name on the later ones.
- **Per persona lane.** Run each buyer lane as its own campaign so per-persona analytics split for free.
- **Staggered committee entry:** never fire two lanes at the same account on Day 1; enter one, the other one to two days behind. Keep the bodies and CTAs distinct per committee member so two people side by side see different angles on the same problem, not one template with a swapped name.
- **Objection quick-handles** are embedded in the sequence (We-Have-WFM, Wait-for-October, Send-Info, No-Budget, etc.).
- **Launch checklist:** warm the mailbox to green first (2 to 3 weeks), confirm the campaign's lead-email field points at the verified email column, approve a small first batch only, size to the mailbox (about 20 sends/day to start, ceiling about 40 on one mailbox, entering 2 to 3 accounts/day), keep bounce under 2 to 3 percent, read every rendered email before launch, track to qualified reply not open.

---

## 11. Gate and approval discipline (fail-closed)
- **The Send Queue is the single egress. Nothing sends from Clay directly.** Every row POSTs to the approval queue; a human approves before egress.
- **`send_ready` = critic PASS AND human_approved AND NOT claimed.** The sender webhook stays OFF until deliverability is green.
- **Dry-run is the default state of the world.** The sender is the rep, not Dallas. Anything that sends, deletes, launches, or flips a gate needs an explicit instruction in that session.
- **Never "Save" a Contacts-sourced campaign** (a stale unsaved source edit floods it with wrong rows). Expand a campaign by editing its load list, not by re-saving its source.
- **The collision/claim gate:** the instant a reply is handled, claim the contact's row (`bdr_claimed`) so `send_ready` drops READY to HOLD and no later touch fires at someone who already raised their hand.

---

## 12. Reply handling standard
The engine sources conversations; this loop keeps them alive without automation talking past a human. Positive replies ("yes, let's talk") skip straight to booking, then log.
1. **Classify** the reply into the seven objection categories (mirrors `intradiem-objection-handler`); anything unclassified or ambiguous gets read by a human before a draft.
2. **Draft** from the template as a starting point: first-draft-engine thinking if non-standard, copy-sharpener always, every figure through the verified-claims gate.
3. **Approve:** the sending rep reads the final text; their voice, their name, their call; if they edit, the edit wins.
4. **Claim the row the same minute** (`bdr_claimed`), so no later automated touch can reach them.
5. **Confirm the same-company pause** caught the account.
6. **Log the outcome twice:** the Contacts closed-loop columns, and `impact/outcomes.csv` as the realized side of the scorecard. Never blend realized outcomes with engine-surfaced estimates.
7. **Calendar the follow-up** on the category's cadence (send-info 5 days, competitor eval 30, bad timing 45, etc.). No orphan replies: every reply has a booked meeting or a named next date.

Category side-effects: Evaluating-Competitor also spins the competitive-intel wedge brief same day; We-Have-WFM logs the vendor; No-Budget logs the reforecast window to re-engage ahead of; Wait-for-October calendars the release week; Send-Info sends the one-pager or interactive artifact, never the deck.

---

## 13. Credit governance
- **No un-budgeted runs.** Every enrichment run gets a pre-estimate (rows x columns x per-provider cost), a named motion, an expected yield, and a ledger row before it fires. If a run cannot state its expected yield, it does not run.
- **Tier enrichments:** firmographics cheap-and-broad first, expensive-and-narrow (waterfall email, technographic, intent) only on rows that already cleared the fit threshold. Never run premium enrichment on an unscored list.
- **only-run-if-empty** on every enrichment (no double-spend); **conditional runs** so credits never fire out-of-window, out-of-ICP, or on a customer row; **parent-grain** the paid signals (~3x cheaper than contract-grain).
- **Sample 10 rows** to confirm any unknown per-provider cost before the full run. **Verify current Clay pricing** before instructing (providers and UI change).
- **The 60 percent flag:** at ~3,000 of 5,000 consumed, produce the mid-burn review (yield per motion, what gets killed, what earns the rest). **Kill criteria:** any enrichment whose cost-per-qualified-reply runs worse than 3x the portfolio average for two consecutive weeks gets killed or downgraded to sampled use.
- **Framing:** "allocated," never "purchased" or "monthly." The story is judgment, not thrift. The ledger (`Clay_Credit_Ledger.md`, append-only) is the renewal receipts: credits in, contacts enriched, messages sent, qualified replies, meetings, by motion.

---

## 14. Reporting and closed loop
- **`reply_status`** (none / reply / qualified reply / meeting), set same-day, upgrade-forward only; funnel counts filter this column.
- **Attribution is set at creation.** The funnel is enriched to sent to reply to qualified reply to meeting; engine-sourced credit is counted at the qualified-reply line; sourced is kept separate from any existing motion.
- **No opens.** Campaigns send plain text on purpose; HTML tracking costs cold-outbound deliverability. Never promise opens in reporting. The line is "plain text on purpose; pixels cost deliverability and opens are unreliable; we measure replies, which are real."
- **Native analytics are free per persona** because each campaign is one persona lane (Analytics + Replies tabs split automatically).
- **Opportunity surfaced (estimate) and realized (from `outcomes.csv`) are never blended into one number.** Weekly readout goes to the inbox plus a council view; nothing new to log into.

---

## 15. What does NOT work (hard-won gotchas, from the live red-team audits)
- **Sync clicks miss silently.** Always re-select the cell and read the fresh `Sent At`; the grid "Sent" tick alone proves nothing.
- **Full MessageGen re-rolls are non-deterministic and reintroduce figure errors.** Fix drafts in place via per-lead campaign overrides, not a source re-run. Caveat: campaign-side overrides revert if the sync is re-run before launch; making a fix permanent at source is a separate task.
- **The run-condition preview grid shows "Will not run" for valid rows.** It is a static UI artifact; verify against the real column values, don't trust the preview.
- **The Claygent trap.** Never click "Create Claygent" or the top-right panel icons near it. A stray click binds the column to an auto-created agent template with unmapped inputs, producing unresolved-token garbage and wasted credits. Fix: click the x on the "Agent template being used" banner in the column editor to detach and restore the inline config, then Save and re-run.
- **The stray-campaign trap.** Clicking "Create Clay email campaign" during a sweep auto-creates a draft campaign AND a second sync column with Auto-run ON and no run condition, which pushes real leads into the draft. Don't click it exploring; if you did, turn that column's Auto-run OFF and delete both the column and the draft.
- **Optional enrichment inputs must have "Required to run" OFF.** With it on, any row missing that input hard-fails "Some inputs missing" and can wipe an existing cell on re-run. The LinkedIn recent-post hook is the common case (see Personalization layers).
- **Account data must reconcile before copy can pass.** If a contact-level figure disagrees with the account-master figure, the critic correctly refuses. That is a DATA fix, not a copy fix; do not force-pass it.
- **CSV import quirks.** Some CMS files are cp1252-encoded; the file_upload path needs the file in a connected/outputs folder targeting the type=file input.
- **The MCP cannot see your tables** (Audiences disabled) and cannot create tables. Build and read live state via Chrome; never report a count or status from anything but the live page.

---

## 16. Build order and governing rules
1. Core five first: the source imports, Accounts (identity to fit), Contacts, Send Queue. Prove on a 10-row slice.
2. Reference tables (Verified Metrics, Product-Angle Map, ICP Rubric, Variant Library): small, static, build once.
3. Signals (Tier 1 first, then Tier 2), wired to write back into Accounts.
4. Message Gen reading the reference tables, plus the companion critic.
5. Deliverability monitor and Outreach Sync, sender webhook OFF.
6. Reply Sync and Attribution.
7. AE Assignment and Worklist.
8. Automations last, and only on motions already proven on a slice.

Governing rules, everywhere: **measurement before volume, ICP before sourcing, human before send, fail-closed, config over code, source once / process in waves.** Ratify scoring weights, ICP, and baseline with the owner before removing the test-slice limit.

### Universe and wave standard (source once, process in waves)
Split sourcing from processing. They have different economics and different failure modes, so they get different rules.

- **Source the full applicable universe ONCE, at motion kickoff, at the table level.** Find, dedupe, and tag every applicable account and contact into the standing universe/Contacts tables up front (attribution tags set at creation, per Section 5). Sourcing is cheap and discovery is never redone — later waves PULL from the standing universe, they never go back out hunting. For signal-defined motions the universe stays alive: new accounts enter as their signal fires (the intent layer already does this); that is refresh, not re-sourcing.
- **Gate the expensive, fragile layers in waves:** paid enrichment, MessageGen + critic, campaign load, and sync run only on the active wave slice. These are the layers the census/critic gates police, and the observed defect rate justifies it: Stars waves ran roughly 10 to 18 percent broken (3/38 census FAILs, 4 drafts needing per-lead overrides). At 30 to 50 contacts that is an afternoon of surgical fixes; at full-universe scale it is 30 to 50 broken drafts and an unmanageable pile of campaign-side overrides that a single sync re-run wipes (Section 15).
- **Wave mechanics:** a `wave_number` column on Contacts assigns the slice; `wave_status` (staged / enriched / drafted / launched / done) tracks it. Wave size 30 to 50. Every wave runs the same runbook: credit estimate + ledger row, enrich (only-run-if-empty), MessageGen + critic, census, fix FAILs, load, sync, verify `Sent At`, launch on approval.
- **No new wave until the prior wave's reply data has been read.** Waves exist so the MessageGen prompt and targeting improve between batches; stamp the prompt version (e.g. v2.2.3) on each wave so quality is traceable per batch. Filling a campaign with the whole universe freezes today's prompt across everything and spends credits ahead of proof.
- **Kill the "remember to go back" failure by process, not by batching:** the last step of every wave launch is scheduling the next-wave check (a scheduled task or a dated runbook entry tied to the sequence's end date, ~9 business days out). A wave is not "launched" until its successor is on the calendar.

---

## 17. Repo and Clay relationship (and how to keep them honest)
- The repo engine is the **brain and spec**: pattern-first, config over code, swappable universes, so a new motion is a config change, not a rebuild. It scores fixtures and proves the logic (both engines currently carry `data_source: "mock"`).
- Clay is the **live running surface** and the **source of truth for any live column text**. A motion is only "built" when both layers exist and stay in sync.
- **Known drift to reconcile (separate task):** the MessageGen system prompt is live at v2.2.3 in Clay while the repo file `Clay_MessageGen_SystemPrompt_v2.md` trails at v2.2.1. The live column is canonical; capturing its current text back into the repo file is its own reconciliation task, tracked separately from this standard.

---

## 18. Maintaining this doc
Update this standard when a transferable pattern, rule, or gotcha changes, not for per-motion specifics. The motion-unique elements (universe source, persona pains, product angle, proof, exact prompt text) belong in that motion's own build prompt, which should open by pointing back here so the shared standard is never rebuilt from scratch.
