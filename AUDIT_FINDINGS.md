# Audit Findings, pre-Bitbucket move
Date: 2026-07-01. Auditor: Claude Code. Scope: full workspace audit per 10-step checklist before the Jul 6 Bitbucket import.

Severity key: BLOCKER (must fix before move), FIX-APPLIED (mechanical fix done, diff logged), DECISION-NEEDED (changes meaning, targeting, or a number Naveen sees; owner must decide), NOTE (informational).

---

## Step 1: repo map
- NOTE: CLAUDE.md created earlier this session (2026-07-01), maps engines, cohesion layer, hosted platform, skills, and the verified-claims discipline.
- NOTE: No canonical/ folder exists; all canonical CSVs and docs live in the workspace root. The audit prompt allowed either location.

## Step 2: test suites
- PASS: tam-outbound-engine/test_account_engine.py: 21/21 (matches expected count, trigger tests included).
- PASS: intradiem-signal-engine/test_signal_processor.py: 14/14.
- NOTE: No test suite exists for gtm-cohesion-layer (conductor.py) or impact/. pytest is not installed on this machine; both suites are standalone scripts and were run with python3 directly (Python 3.9.6).

## Step 3: conductor preflight
- VERDICT: NOT READY with 4 blockers: attribution_ratified, baseline_set, deliverability_green, security_audit_current.
- DECISION-NEEDED: The audit spec expected exactly 3 reds, but preflight shows a 4th: security_audit_current (permission audit + log sanitization + least-privilege review). _START_HERE_Index.md line 19 explicitly lists all FOUR of these as the expected pre-access blockers, so the workspace docs and the audit expectation disagree. The fix is not mechanical: clearing it means actually running the first permission audit and setting the three security flags in engine_state.json, which only the owner can truthfully do. Decide: either accept 4 reds as the known pre-Jul-6 state (consistent with _START_HERE_Index.md) or run the security audit now to get to 3.
- All other preflight checks PASS (state structure, owner identity, all three engine contracts, WIP, approval attribution, spec present).

## Step 4: seed files and TimePhased CSV integrity
- PASS: All 8 seed inputs named in Clay_Day1_Build_Order.md exist on disk (TimePhased csv, Tiered csv, PersonaPull Runbook + RunConfig, Earnings Signals csv, Targeting Flags md, MessageGen prompt, triggers.json).
- FIX-APPLIED: StarRatings_Universe_2026_TimePhased.csv carried the five time-phased columns TWICE (header had 22 columns; addr_2028_musd, addr_2029plus_musd, pct_2028, pct_2029plus, wavg_2026 appeared at positions 13-17 and again at 18-22). Verified the two blocks were byte-identical in all 307 data rows, then dropped the second block. File is now 17 columns by 307 rows. The file was locked read-only (400); it was unlocked for the fix and re-locked after. No values changed. A duplicate header block would have broken a Clay CSV import or produced ambiguous column mapping.
- PASS: 307 data rows confirmed (after fix, and before).
- PASS: Tiered csv: Tier A = 34, Tier A+B = 98 contracts, 32 distinct parents, A+B addr_2028 total = $2,511.2M. All match expected.
- PASS: Humana Tier A+B on addr_2028 = $1,082.8M (rounds to the expected $1,083M).
- PASS: Horizon absent from both the TimePhased universe and the Tiered csv.
- PASS: H0104 tier = Unscored.
- PASS: Clay_MessageGen_SystemPrompt_v2.md is v2.1 (header line 1, patch note dated Jul 1 2026: window beat, payment-year clause, time-stamped UHC line, addr_2028 lead for Persona 2).
- PASS: PersonaPull RunConfig: 32 parents, tier_ab_addr2028_musd sums to $2,511.2M, consistent with the Tiered csv.

## Step 5: stale-reference sweep
- PASS: `StarRatings_Universe_2026_Canonical.csv` is referenced only once outside itself, in Clay_Day1_Build_Order.md line 10, and that reference is the supersession note itself ("Supersedes ... use the TimePhased file"). No tool, config, or artifact still reads the Canonical file.
- PASS: No live `addressable_pct == 0` exclusion rule anywhere in the tree. The only match is Clay_Day1_Build_Order.md line 29, which correctly forbids it in favor of `pct_2028 == 0 AND pct_2029plus == 0`. The Fable_Prompt_* files use addressable_pct only as a computed column definition, not an exclusion.
- FIX-APPLIED: UHC $190M time-stamp. Three mentions lacked the required "under the prior rules" framing (per StarRatings_Targeting_Flags_2026.md line 21). Fixed:
  1. StarRatings_Earnings_Signals_2026.csv row 7 (UnitedHealth angle_line): added "under the prior rules" after "bonus payments". This angle_line feeds why_now copy in Clay, so it was the highest-exposure miss.
  2. Fable_Prompts_Portable_Deliverables.md line 43: added "under the prior rules", noted the measure is retired for 2028 Stars, and added the never-imply-still-earns-bonus guard.
  3. Devoted_WholeParent_StrikePlan.md line 45: same treatment.
  Already compliant, no change: Clay_MessageGen_SystemPrompt_v2.md (v2.1 lines 80-88) and StarRatings_Targeting_Flags_2026.md (the rule source).
- DECISION-NEEDED: `StarRatings_Motion_Clay_Seed.csv` is a superseded-era seed that violates two current rules: (a) its play_text in roughly 20 rows says "Lead with QO for C32/D01 secret-shopper measures (binary pass-fail; one half-star to full QBP)", which presents the retired call-center measures as live QBP levers, and (b) it contains Horizon (H0885 Braven Health), which exited the motion. `StarRatings_Accounts_Clay_Seed.csv` also carries a Horizon target row ($26.2M) on the old pre-time-phased data model. Neither file is referenced by Clay_Day1_Build_Order.md (only by the historical Fable_Context_Bridge_Prompt.md). Recommendation: move both to _archive/ before the Bitbucket import. Not done automatically because they are data files you built by hand; say the word and I will archive them.
- PASS: No occurrence of the stale totals $2,359M or $872M anywhere in the tree (md, html, json, csv, py).
- PASS: HTML artifacts contain no C32/D01-live claims, no $190M mentions, and no stale dollar totals.

## Step 6: triggers.json and persona keys
- PASS: `qbp_earnings_pressure` present, weight 22, route_personas [finance, cc_ops].
- PASS: `quality_identity_gap` present, weight 15, route_personas [cx, cc_ops].
- PASS: Persona keys are exactly cc_ops, wfm, cx, finance in personas.json and across every route_personas entry. No stray keys anywhere.
- BLOCKER (DECISION-NEEDED on the fix): The Molina line-exit suppression is NOT wired anywhere in code or config. triggers.json has no suppression on qbp_earnings_pressure; the only suppression logic in either engine is the generic 14-day time window in signal_processor.py. Meanwhile StarRatings_Targeting_Flags_2026.md line 9 claims "This is wired into the signal engine: qbp_earnings_pressure suppresses for contracts flagged for divestiture/line-exit", which is not true of the code on disk. Clay_Day1_Build_Order.md delta 4 does plan the Molina-MAPD exclusion as a Clay motion_exclude column, so the Clay-side rule is documented but the engine-side suppression the flags doc claims does not exist. Options: (a) add a suppression field to the trigger and honor it in account_engine.py (changes ranking logic, so your call), or (b) soften the flags doc line to say the suppression is a Clay motion_exclude rule, not engine wiring. Not fixed automatically because both paths change either ranking logic or a claim's meaning.
- DECISION-NEEDED (deferred to owner): Both new trigger plays still list call-center among the movable measures. qbp_earnings_pressure play: "sits in the CAHPS/complaints/call-center measures our platform acts on". quality_identity_gap play: "sitting almost entirely in the CAHPS, complaints, and call-center measures". Under the CY2027 final rule the call-center measures are retired for 2028 Stars, and the v2.1 MessageGen patch moved the live money to "Complaints, Appeals, Customer Service, and the CAHPS experience core". Suggested rewording for both: "CAHPS, complaints, appeals, and customer-service measures". Not changed automatically because this is prospect-facing copy meaning.

## Step 7: HTML artifacts (static checks only)
- PASS: All five cohesion-layer dashboards (control_tower, approval_queue, attribution_dashboard, deliverability_monitor, variant_tracker) fetch `engine_state.json` by relative path, which resolves correctly from gtm-cohesion-layer/ where they live. No hardcoded absolute paths, no file:// URLs, no dead references anywhere in the local HTML.
- PASS: Four of the five use empty-skeleton FALLBACK objects plus a loud red "showing PLACEHOLDER data" banner when the fetch fails, so no real numbers are baked in.
- NOTE: attribution_dashboard.html bakes a full FALLBACK snapshot (documented design: "mirrors engine_state.json so the page renders standalone"). It is 5 days behind the state file on two cosmetic fields: _meta.last_updated ("2026-06-24" vs "2026-06-29") and deliverability.overall_health ("not_started" vs "warming"). Every functional value (funnel zeros, floor thresholds 0.40/0.003/0.03, targets 15/200, ratification flags false) matches the current state exactly, and the placeholder banner fires whenever the fallback renders. No fix applied; harmless, but say the word if you want the fallback regenerated for byte-parity.
- PASS: Day1_Audit_Console_LIVE.html is self-contained sample data by design, with an explicit "Showing sample data" banner and a documented MODE flag for go-live. Not a drift risk.
- PASS: The deploy pages (GTM Engine - deploy, Star Ratings Play - deploy) are seeded-and-labeled per their own legends; no engine_state duplication.
- NOTE: The named Cowork artifacts (command-center, control-plane, star-ratings-motion, strike-room, golden-list, roi-calculator, dallas-mission-control) do not exist as files in this tree; they live in claude.ai. Only their local HTML counterparts were audited, per the static-checks-only scope.

## Step 8: engine_state.json vs canonical CSVs
engine_state.json is explicitly SEEDED (_meta.status: "SEEDED, pre-access placeholders"), so most values are declared placeholders rather than claims. Fields that intersect the canonical CSVs and disagree:
- DECISION-NEEDED: `list_health.accounts_by_motion.star_ratings` = 38, but the canonical universe is 307 contracts (Tier A+B = 98, Tier A = 34). The 38 is the pre-TimePhased motion count that Clay_Day1_Build_Order.md delta 1 explicitly supersedes ("do not load 38 + 157"). Decide which number this field should carry pre-build (98 is the Tier A+B build target; 307 is the universe) and I will set it. Not changed automatically because engine_state.json is the declared source of truth for the dashboards.
- NOTE: `impact` block ($41.6M opportunity, $180K pipeline, 6 strike plans) derives from the seeded tam/signal sample data, not the Star Ratings CSVs. Consistent with its declared sources (the two engines' sample outputs) and already flagged as seeded by VERIFICATION_AUDIT.md. No CSV disagreement, but never present these numbers.
- NOTE: `north_star.approved_claims` is empty. The live-wire checklist (cohesion README) requires seeding it with the verified figures before go-live so the critic can allow them. Known to-do, not a new finding.
- PASS: All other state fields either match their documented sources or are structural placeholders (nulls, zeros, false flags) that preflight already gates on.

## Step 9: repo hygiene for the Bitbucket move
- PASS: Secrets scan clean. Grepped for Slack tokens (xoxb/xapp), OpenAI-style keys, AWS AKIA keys, bearer tokens, private key blocks, and hardcoded api_key assignments across py/json/md/html/sh/csv/txt/plist. Zero hits. The plugin manifest carries the placeholder "SET_THE_CLAUDE_KEY_HERE"; the brain and the stdio client read keys from env vars only. No .env files exist.
- FIX-APPLIED: Created .gitignore covering OS junk (.DS_Store, .~lock files, *.tmp, _wtest.txt), __pycache__/*.pyc, node_modules/, env and key files, logs/ plus the brain request log, transient engine state (suppression_state.json, notified_state.json), .claude/settings.local.json, *.zip bundles, one unnamed junk zip (_archive/zi7Zjxcl), and a clearly-labeled personal/interview-era section.
- DECISION-NEEDED: Personal files excluded from git pending your call. The .gitignore keeps [redacted-personal-file], [redacted-personal-file], both resume files, [redacted-personal-file], [redacted-personal-file], [redacted-personal-file], [redacted-personal-file], [redacted-personal-file], [redacted-personal-file], [redacted-personal-file], and [redacted-personal-file] OUT of the repo. These are your private documents and should not enter Intradiem's Bitbucket; if any belongs in, remove its line deliberately. They remain on disk untouched.
- NOTE: [redacted-personal-file] IS tracked (it is the interview demo one-pager, an artifact rather than private material). Drop it from the archive commit if you want zero interview-era files in company history.
- FIX-APPLIED: git init (branch main) plus 12 commits, one per logical unit: foundation, signal engine, TAM engine, impact, cohesion layer, hosted platform, Star Ratings motion data, agent skills, operating plan docs, HTML surfaces and handoffs, portable prompts, reference material. Working tree clean. Nothing pushed anywhere.

## Step 10: summary

| # | Check | Result |
|---|---|---|
| 1 | Repo map / CLAUDE.md | DONE (CLAUDE.md created this session) |
| 2 | Test suites | PASS: tam 21/21, signal 14/14; no suites exist for cohesion layer or impact |
| 3 | Conductor preflight | NOT READY as expected, but 4 reds vs the expected 3 (extra: security_audit_current) |
| 4 | Seed files + TimePhased integrity | PASS after 1 fix (duplicate column block); all counts and totals verified |
| 5 | Stale-reference sweep | 3 fixes applied (UHC time-stamps); 2 superseded seed CSVs flagged; no stale totals |
| 6 | triggers.json + personas | Triggers and persona keys PASS; Molina suppression MISSING (blocker); call-center wording flagged |
| 7 | HTML artifacts | PASS; one cosmetic fallback staleness noted |
| 8 | engine_state consistency | 1 disagreement (star_ratings 38 vs canonical 307/98); rest seeded-by-design |
| 9 | Hygiene / git | Secrets clean; .gitignore created; 12 logical commits on main; no push |

### Fixes applied (files touched)
1. StarRatings_Universe_2026_TimePhased.csv: removed duplicated 5-column block (22 to 17 columns, 307 rows unchanged, re-locked read-only).
2. StarRatings_Earnings_Signals_2026.csv row 7: UHC angle_line now says "under the prior rules".
3. Fable_Prompts_Portable_Deliverables.md line 43: UHC proof line time-stamped, retirement noted.
4. Devoted_WholeParent_StrikePlan.md line 45: same UHC time-stamp treatment.
5. .gitignore: created.
6. Git repository initialized with 12 logical commits.

### DECISION-NEEDED list (your calls, in priority order)
1. Molina line-exit suppression does not exist in code despite StarRatings_Targeting_Flags_2026.md claiming it is "wired into the signal engine". Pick: (a) wire a suppression flag into triggers.json + account_engine.py, or (b) correct the flags doc to say the rule lives in Clay motion_exclude. (Step 6, blocker.)
2. Fourth preflight red (security_audit_current): accept as known pre-Jul-6 state per _START_HERE_Index.md, or run the first permission audit now to get to the expected 3. (Step 3.)
3. Trigger play copy in triggers.json still lists "call-center" among movable measures in both qbp_earnings_pressure and quality_identity_gap. Suggested: "CAHPS, complaints, appeals, and customer-service measures". (Step 6.)
4. engine_state.json list_health.accounts_by_motion.star_ratings = 38 vs canonical 307-universe / 98 Tier A+B. Tell me which number and I will set it. (Step 8.)
5. Archive or keep StarRatings_Motion_Clay_Seed.csv and StarRatings_Accounts_Clay_Seed.csv (superseded era: C32/D01-live play text, Horizon rows). Recommend moving to _archive/. (Step 5.)
6. Confirm the personal-file exclusions in .gitignore are the right set before the Bitbucket import; also decide on [redacted-personal-file] which is currently tracked. (Step 9.)

---

## Resolutions (owner decisions, applied 2026-07-01)

All six DECISION-NEEDED items were decided by the owner and applied as follows. After every change: tam 21/21, signal 14/14, preflight unchanged (NOT READY, the four expected people-gated reds), and both edited JSON files parse clean.

1. RESOLVED (flags doc corrected): StarRatings_Targeting_Flags_2026.md line 9 no longer claims engine wiring. It now states the Molina rule lives in Clay's motion_exclude column (Build Order delta 4) plus the persona-pull step-0 product-line check, and that engine-level line-exit suppression is a post-start enhancement. No engine code changed.
2. RESOLVED (accepted as-is): security_audit_current stays red as the expected fourth blocker. Owner runs the permission audit on Day 1 with company access. No change.
3. RESOLVED (copy fixed): tam-outbound-engine/config/triggers.json. Both plays now read "CAHPS, complaints, appeals, and customer-service measures"; call center no longer appears as a movable measure anywhere prospect-facing. 21/21 tests still pass.
4. RESOLVED (state updated): gtm-cohesion-layer/engine_state.json list_health.accounts_by_motion now carries star_ratings: 98 (Tier A+B working set), star_ratings_tier_ab: 98, star_ratings_universe_total: 307, and a _note explaining both figures shrink after the Day-1 non-customer filter. Verified no code or dashboard iterates accounts_by_motion, so the added fields are inert to consumers.
5. RESOLVED (archived): StarRatings_Motion_Clay_Seed.csv and StarRatings_Accounts_Clay_Seed.csv moved to _archive/ via git mv, each with a one-line "# SUPERSEDED 2026-07-01" note prepended naming the replacement files.
6. RESOLVED (history rewritten): the tracked interview-era HTML artifact was removed from all git history via filter-branch (nothing was ever pushed), backup refs deleted, reflog expired, gc run. The file remains on disk and is gitignored. All 13 personal files were verified excluded via git check-ignore; the names are intentionally not listed here (see the redaction addendum below).

## Addendum (2026-07-01, post-resolution): interview-era files relocated
All 13 files on the exclusion list above were MOVED out of this workspace to ~/Documents/job-search-archive/ (the resumes and offer docs are the only copies). A filename-pattern sweep (interview/offer/panel/resume/salary/negotiat) found no additional matches beyond the 13. _START_HERE_Index.md's superseded section now points at the new location; the .gitignore personal section was replaced with generic guard patterns so no personal filename is listed in the repo going forward. Residual, CLOSED (owner-approved rewrite, 2026-07-01): the personal filenames were scrubbed from every commit via a second filter-branch pass over .gitignore, this findings file, and _START_HERE_Index.md, each occurrence replaced with a [redacted-personal-file] token. Backup refs deleted, reflog expired, gc run. Verified afterward: zero occurrences of any personal filename in any blob of any commit; the only remaining "Busbee" mentions are Chris Busbee (SVP Product), a work stakeholder in business docs, which is in scope for the company repo. The files themselves live in ~/Documents/job-search-archive/.

## DWO Positioning Audit (2026-07-05, night before Day 1)
Scope: the three eyes-only HTMLs, all 12 skills, 3 engines + configs, 8 live artifacts, 3 scheduled task prompts, message seeds, and reference docs. Standard: Dynamic Workforce Orchestration positioning per Naveen's onboarding site (contact center AND back office, six verticals, three pillars: Goal Advisor / Decision Intelligence / Workforce Orchestration; WFM = the layer we sit on, never a rival; never cap the platform at idle-time recovery or call-center scope).

Findings and resolutions:
1. RESOLVED (artifact updated): roi-calculator subtitle read "Recoverable idle-labor capacity on a contact-center floor," the only scope-describing copy in any artifact that omitted the back office. Rescoped to "across contact centers and back offices"; manifest description updated; no logic changes. The other seven artifacts audited CLEAN (control-plane and mission-control explicitly carry back-office scope; command-center's "Back Office out of scope this cycle" line is WIP-of-one discipline, not positioning).
2. RESOLVED (doc updated): intradiem-context-handoff.md described the company as "real-time workforce automation to contact centers (500+ agents)... acts in the idle seconds between scheduled events." Rewritten to full DWO scope with the three pillars; idle-seconds recovery reframed as the entry wedge, never the whole story. The moat one-liner broadened the same way.
3. RESOLVED (rule sharpened): Grand Plan "rules I never break" #9 capped the mechanism at "we act in the idle time between." Now reads: WFM plans the day, DWO orchestrates what happens inside it (idle-time actions, coaching/training delivery, back-office work), and the competitive wedge targets the module and the contact-center-only scope, never the WFM layer itself.
4. RESOLVED (constraint added): intradiem-competitive-intel gains "the module, never the layer" as an explicit constraint, so wedge briefs against Verint/NICE/Calabrio can never drift into disparaging the layer we integrate with. The skill's body was already correctly framed (augment-not-replace, honest strengths, back-office scope wedge).
5. RESOLVED (copy hygiene): Message_Variant_Starter_Pack.md carried six em dashes in prospect-facing copy and two forbidden "compare notes" CTAs. All fixed; CTAs now name the topic per the sharpener's rules.
6. CLEAN, verified no action: all "call center" occurrences in Stars assets (MessageGen prompt, variant pack, Devoted plan, one-pagers) are CMS measure terminology or retired-measure history, used correctly with the retirement caveat. Wave-2 skills, war-room play mapping ("we sit ON the stack they just bought"), objection-handler's We-Have-WFM reframe, scheduled task prompts, and tam-outbound-engine configs (call-center wording already removed in the 2026-07-01 audit) all carry the positioning correctly.
7. NOTED, no fix (archived): _archive/_live-preview-grouped-nav.html labels Verint/Calabrio as "competitor" and uses idle-time-only pitch language. In-archive per policy; if that mockup is ever resurrected, its positioning must be rebuilt to this standard first.
8. NOTED (accepted for targeting, superseded for pitching): Naveen_Send_Note.md ties the wedge to "call-center measures Queue Optimizer moves." The addressability cut (target plans whose gap sits in measures QO touches) remains valid targeting logic. But Naveen's Jun 27 email explicitly widened the pitch: "Queue optimizer might not be the only product we pitch. We are looking to get them to buy into our Dynamic workforce orchestration platform vision with a suite of products moving various metrics that will eventually give them what pure human and pure AI investments have failed them on." Rule going forward: QO defines WHO we target in the Stars motion; DWO defines WHAT we sell them. No new asset anchors the pitch to QO alone. The "pure human / pure AI have both failed them" articulation was added to competitive-intel's reframe and first-draft-engine's one-idea families the same night.

Addendum (same audit, email reconciliation): Naveen's full email corpus was cross-checked against the portfolio. Confirmed aligned: co-shape posture, Clay exhaust-credits-then-decide strategy (clay-credit-steward encodes it), his two signal ideas (earnings calls, QBP lost-revenue filings) live in the war room and earnings CSV, MessageGen v2.1 aimed at exactly the "system prompt needs fine tuning" gap he named, Genna best-privileges arrangement, Bitbucket outline. Deltas captured: persona-pull runbook now carries his Jun 9 persona spec verbatim as provenance plus wave-2 personas 3 and 4; sequencing decision of record is Clay's native sequencer first (Dallas's proposal, unchallenged), so the attribution loop spec must wire to Clay's sequencer, not a hypothetical external tool; Naveen is OOO until Jul 7, so the first 1:1 and all Naveen-gated asks land Jul 7+, and the promised who-does-what/system-ownership doc has NOT yet arrived, so no asset may assume org-ownership facts beyond his emails.
