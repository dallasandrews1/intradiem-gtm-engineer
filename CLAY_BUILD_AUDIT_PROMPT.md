# Prompt — Full audit of the Intradiem Clay build + L2 intent signals

Paste everything below the line into a **new thread inside the "Intradiem GTM Engineer" project**.

---

You are auditing my live Clay GTM build and its L2 intent-signal layer, end to end. Run this as an adversarial red-team by a principal GTM engineer, not a friendly review. My standing at Intradiem rides on this being genuinely excellent, so surface every real weakness. I would rather hear the hard truth now than discover it in front of the C-suite. Flattery here costs me my credibility later.

## Orient against ground truth first (do not skip)
1. Read these before touching anything — they are the source of truth for what exists and why:
   - `CLAUDE.md` (repo conventions: config-over-code, dry-run-by-default, verified-claims discipline, credit discipline).
   - Your memory index (`MEMORY.md`) and the linked files, especially: the L2 intent build, the Clay credit ledger, the customer-exclusion history, and the feedback memories (no AI-isms, no finished-product framing, self-serve-not-Dallas-in-the-loop, Naveen/exec-facing posture, exec-deliverables-present-state-only).
   - `Clay_Credit_Ledger.md`, `intradiem-signal-engine/config/l2_intent_signals.json`, `intradiem-signal-engine/l2_intent_scorer.py` and its test, and `greenlight-pack/16_L2_Signal_Monitoring_Spec_Jul11.md`.
2. Then inspect the **live** Clay build through the Claude-in-Chrome extension. Do not trust the docs — verify against the actual workspace. Workspace `1180800`, workbook "GTM Engine". Key tables: **Accounts (Master)** `t_0thuumoUcu6wAAhovti` (the L2 intent layer lives here), **Contacts (Buying Committee)** `t_0thtm73HHxyiupTuepK`, and the two **Stars QBP Wave 1** campaigns.
3. This audit is **read-only and credit-safe**. Do not run any enrichment or fire any campaign. If an audit step would cost credits, estimate it and move it into the recommendations — never spend during the audit. Auto-run is OFF on Accounts (Master); leave it off.

## What the build currently is (verify each claim; some may already be stale)
- Accounts (Master): ~98 Medicare contracts across ~26 parents, the sub-4.0 Star Ratings universe. It carries firmographics + star fields; exclusion fields (`customer_flag`, `new_logo_eligible`); existing formula columns (`fit_star`, `grade`, `motion_exclude`, `new_faller`, `parent_key`); and a new **L2 intent layer**:
  - 5 signal columns: `sig_sec_filing`, `sig_earnings`, `sig_leadership`, `sig_hiring`, `sig_backlog` (originally checkbox placeholders; some now superseded by real enrichments).
  - `intent_score` (formula): self-cleans to 0 at `overall_star_2026` >= 4.0; otherwise `min(100, new_faller 20 + sec_filing 30 + earnings 25 + leadership[AI "yes"] 10 + hiring[Job Openings > 0] 15 + backlog 10)`.
  - `intent_status` (formula): graduated / grade_lift (>=40) / in_motion / dormant.
  - Two live paid signals: a native **Company Job Openings** enrichment keyword-filtered to quality/CAHPS/WFM roles (wired to the hiring term), and a **Use AI (Claygent) web-research** column detecting a recent quality-leadership appointment (wired to the leadership term, weight +10, prompt tightened to require a dated last-12-months appointment plus a role-specific remit).
- ~418 of the 5,000 **monthly** Clay credits spent (see ledger). SEC-filing and earnings signals are NOT yet built.

## Audit across these dimensions — be specific and cite what you actually see
1. **Errors & risks (must-fix).** Formula correctness and edge cases: nulls, text-vs-number coercion, the star self-clean threshold, the AI "yes" string match, the cap logic. Customer-exclusion integrity — can a customer leak into any outreach path? The known stale artifact: ~10 sample-era customer rows still show pre-keyword Job Openings totals — assess real impact. Vestigial/confusing columns (the manual `sig_*` checkboxes now that real signals are wired; any orphaned sync columns). Contract-grain vs parent-grain double-counting.
2. **Credit efficiency.** Where are credits wasted (e.g., enriching the same parent across multiple contract rows)? Should signals dedup to parent grain before enriching? Is the ratified cadence (monthly full + weekly delta, ~800/mo steady state) right against the 5,000 monthly budget? Is the ledger accurate, and does it compute cost-per-qualified-signal?
3. **Signal quality & calibration.** Is this the RIGHT signal set for the Star-Ratings cliff motion, or are there better/cheaper signals missing (WFM/CCaaS tech-stack moves — Verint/NICE/Calabrio/Genesys; CMS measure-level movement from data I already own; complaints/appeals trends; web/search intent)? Is `sig_backlog` (claims backlog) even the right signal for THIS motion versus the back-office motion? Are the point weights defensible? Is the AI leadership signal reliable enough, and is the tightened prompt actually tight enough? Is the self-cleaning logic complete?
4. **Architecture & scalability.** Is it config-driven, maintainable, and self-serve (the team runs it; I maintain it — never "only works if Dallas")? Does the Clay build stay in sync with the repo engine architecture? Is the refresh set as a native Clay schedule? Will it scale to the back-office motion and more parents without a rebuild?
5. **Data integrity & provenance.** Is every figure traceable and honest? Does it hold the verified-claims line (no unverified Intradiem numbers anywhere near a prospect-facing path)? Does it keep "surfaced/estimated" separate from "realized"?
6. **The closed loop (check this hard — likely the biggest gap).** Today: signals -> intent. Is there any path from intent -> outreach -> reply -> meeting -> pipeline, with attribution? If not, spec it — it is probably the single highest-leverage upgrade for the exec story.
7. **Exec-demo & narrative readiness.** Would this survive a skeptical CRO/CMO poking at it live? Is the thesis — "we run GTM the way our product runs operations: real-time signals trigger automated action, and the list self-cleans when the problem is solved" — visible and airtight in the actual build? Flag anything cosmetic that would undermine credibility under scrutiny.

## Deliver
One prioritized audit report saved to `greenlight-pack/17_Clay_Build_Audit_[date].md`, structured as:
- **BLUF** — one honest paragraph: how close is this to "work of art / status-solidifying," and the top 3 things standing between here and there.
- **Errors & risks** — must-fix, ranked by severity, each with the exact fix.
- **Improvements** — should-do, ranked by effort vs. impact.
- **Upgrades / work-of-art moves** — could-do, ranked by impact on the C-suite narrative (closed-loop measurement, signal-to-play automation, self-improving signal governance, etc.).
- **Punch-list** — the concrete, ordered steps I personally need to take, with credit estimates for anything that spends.
- **The status read** — a straight assessment of whether this build, once the punch-list is done, actually gets the C-suite seeing a long-term future with me, and precisely what would move them.

## Standards
Hold the house rules from `CLAUDE.md` and memory: credit discipline (estimate before any spend; never spend during the audit), verified-claims discipline, no AI-isms and no em dashes, no finished-product framing (head-start plus ongoing engineering), self-serve framing, and the exec-facing posture (peer-level, present-state, showcase-not-seller). Invoke the skills that sharpen the audit — `strategic-premortem`, `cognitive-calibration`, `clay-credit-steward`, `intradiem-verified-metrics`, `intradiem-backoffice-icp`. Use a verification subagent for anything high-stakes. Be brutally honest.
