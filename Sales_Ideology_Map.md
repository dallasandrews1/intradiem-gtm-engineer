# Sales Ideology → GTM Systems Map

Source: Dallas's 10-fact sales belief set (Nate Nasralla / Fluint "Selling With" lineage), shared 2026-07-22.
Purpose: a standing lens on the engine. Each fact maps to the skill/engine it should shape, with current state and the change it drives.
Status keys: **BUILT** (change made), **PROPOSED** (awaiting greenlight), **ALREADY HOLDS** (engine already reflects it).

---

## The 10 facts, mapped

**1. Deal reviews compress to <60 seconds / one page.**
Home: no skill owns this yet. Adjacent to `naveen-weekly-readout` (already compresses) and the daily rundown.
Change, **PROPOSED**: a lightweight `deal-review-onepager` skill: account in, one page out (situation, priority, committee, next step, gap, ask), forced to fit a 60-second read. Doubles as champion-enablement (see #3, #9).

**2. Building the business case *is* the sales process.**
Home: `intradiem-roi-business-case`.
State: **ALREADY HOLDS** in framing ("the business case is the deal"), now reinforced by the #6 edit. The deeper move (every other activity rolls up into the case) is an orchestration idea, not a single skill. **PROPOSED**: have the strike-sequence and signal-to-play outputs each reference/feed the account's business-case doc so the case is the spine, not a sibling artifact.

**3. Deals close in conversations about you, without you.** *(Dallas's most-interesting pick)*
Home: every asset-producing skill (roi-business-case, strike-sequence, content-engine, signal-to-play).
Insight: the unit of work is the artifact that travels without the rep. Optimize what survives the internal forward.
Change, **PROPOSED**: (a) instrument a "did the artifact survive the forward" signal (reply/meeting attribution back to a specific asset) into impact.json + the readouts; (b) a "forwardable by design" check in copy-sharpener (would this survive being pasted into the buyer's own deck with our name stripped?).

**4. Efficiency = less activity, more influence.**
Home: the whole motion-factory posture + `clay-credit-steward`.
State: **ALREADY HOLDS**. Credit-per-qualified-reply and the receipts story already reward influence over volume. Reinforce in `naveen-weekly-readout`: lead the efficiency line with influence-per-touch, not touch count.

**5. Writing is discovery, not documentation.**
Home: `intradiem-first-draft-engine` (prospect-first cognition before rules).
State: **ALREADY HOLDS** in spirit. **PROPOSED**: add an explicit "what don't we know yet" gap-surface step so drafting exposes discovery gaps, not just produces copy.

**6. Buyers don't trust your ROI; numbers ratify a story they already believe.**
Home: `intradiem-roi-business-case`.
Change, **BUILT (2026-07-22)**: new step 3.5 "Anchor to the executive priority," new "Executive Priority" output section above Current State, constraint that numbers ratify a story and never open on cold math. Reconciled with the exec present-state rule (neutral stakes, never a diagnosis of the buyer's team).

**7. Two problems: math and drama; drama is why math goes unsolved.**
Home: roi-business-case (math) + first-draft-engine / copy skills (drama).
State: partially covered by the #6 edit. **PROPOSED**: name "the drama" explicitly in discovery capture (meeting-capture / the case), the political or career tension that keeps the costly problem unsolved, distinct from the cost itself.

**8. Selling priorities > solving problems.**
Home: roi-business-case (#3.5) and the war-room play-mapping.
Change, **BUILT (2026-07-22)** inside the #6 edit: the case now leads with the exec-level priority, and flags a missing priority as the top "Ask on Next Call." **PROPOSED**: war-room play mapping tags each signal with the exec priority it ladders to, not just the operational pain.

**9. You build champions (IKEA), you don't find them.**
Home: `intradiem-strike-sequence` (buying-committee sequencing).
State: sequences *reach* the committee but don't yet *co-create* with a champion. **PROPOSED**: a champion-enablement asset in the sequence (a forwardable one-pager the champion can present as their own), transferring ownership over touches. Ties to #1 and #3.

**10. Multithreading = a minimally-viable committee, not more contacts.**
Home: `intradiem-strike-sequence` contact selection + Clay Contacts (buying committee).
Insight: more contacts = more dysfunction; build a minimal committee as a social safety net around the champion.
Change, **PROPOSED**: a committee-shaping rule in strike-sequence (economic buyer + champion + one blocker-neutralizer + one user-voice, capped) instead of maximizing addressable contacts.

---

## Three facts the shortlist missed (my adds)

**A. "Why now" is the buyer's own clock, not urgency you install.** Fit: highest. Already wired into `intradiem-daily-war-room` + `intradiem-signal-to-play` (Stars cliff, CMS release, WFM renewal). Make it an explicit named principle so every motion asks "whose clock, and what's the deadline they already live by."

**B. The real competitor is "no decision" / status quo, not Verint or NICE.** Fit: high. `intradiem-competitive-intel` over-indexes on named rivals; add a status-quo wedge as a first-class competitor profile.

**C. The best pipeline is already inside the install base.** Fit: high for NRR. The shortlist is all net-new; the install-base expansion/risk motion and the renewal-receipts tracker are where this lives. Elevate to a named strategic pillar, not just motion #4.

---

## Decision log
- 2026-07-22: roi-business-case edited for #6/#8 (both mirror copies).
- 2026-07-22: Dallas supplied the Kellogg exec-blog top-10, the SCR exec-summary framework, and the Miro S1/S2 exit-criteria (all Nasralla lineage) and greenlit building "all skills we need." Built this session:
  - `Exec_Grade_Sales_Doctrine.md` (this folder): canonical reference housing Kellogg 10, SCR, and the S1/S2 exit criteria. Skills cite it.
  - `intradiem-problem-statement` skill (S1): co-created current-state problem + consequences, attached to an exec priority. NEW.
  - `intradiem-exec-summary` skill (S2): the 1-page SCR business case; composes roi-business-case (numbers) + verified-metrics (proof). NEW. This is the customer-facing "1-page business case," distinct from the internal deal-review one-pager proposed under fact #1.
  - `intradiem-deal-review` skill (internal): <60s deal compressor + exit-criteria qualification + calibrated probabilistic forecast (Kellogg 1, 2, 9). NEW. This supersedes the fact-#1 `deal-review-onepager` proposal (that item is now BUILT under this name).
  - `intradiem-copy-sharpener`: added the Kellogg-10 recognition test to the Send-Ready checklist (person, problem recognized in the first sentence).
  - All new/edited skills mirrored to coordinator and ~/.claude; em-dash swept clean.
- FLAG for Dallas: brand-palette conflict between sources. Coordinator CLAUDE.md says official Intradiem brand is "green-forward, Playfair Display + DM Sans"; the repo's `intradiem-brand-kit.md` (stated source of truth) says Orange #FE5000 / Ink #14181F / Paper #FAF8F6. New skills now defer to the brand source rather than assert a palette. Needs a one-line ruling on which is canonical.
- Open follow-up: Dallas offered a Fluint framework/write-up on fact #3; incorporate when it lands. Dallas will also locate more relevant docs.
