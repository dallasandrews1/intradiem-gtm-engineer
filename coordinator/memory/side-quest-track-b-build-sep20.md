---
name: side-quest-track-b-build-sep20
description: "Sep 20 2026: side quest Track B built on sample data in motions/ai_adoption_sidequest/: sources/ adapter pattern (Greenlight + Microsoft 365 Copilot), Delivery_Contract spec page, Kathryn's CSA v1.0 as a self-scoring intake page, offer sheet with price blanks for Derek; 31 + 33 + 25 checks green; NOT deployed, uncommitted on main"
metadata:
  type: project
---

Built Sep 20 2026 after Kathryn rescinded the no-commercial-product ruling (see [[side-quest-productized-offer-thinking-sep20]]). All in `motions/ai_adoption_sidequest/`, sample data only, nothing deployed, changes uncommitted on main.

1. **Adapters.** `adoption_engine/sources/` + `config/sources.json`. Engine now runs `--source NAME` or `--all` (writes one state per tool plus `data/portfolio_state.json`, which never blends tools into one rate because units differ). Greenlight state verified identical to pre-refactor. Microsoft 365 Copilot adapter is modeled on Microsoft's real report (headers checked against Microsoft Learn Sep 20): the report is a daily SNAPSHOT of last-activity date per app, not a usage log, so the unit is active app-days, pulls must be daily, and user names arrive concealed by default (adapter refuses with the fix). Loader refuses any non `@sample.invalid` roster id while a source's `sample` flag is true; that flag in sources.json is now the only live/sample switch (replaces the old "flip it in score()" step).
2. **Delivery_Contract.src.html.** Spec only: record out, receipt back (maps onto the responses feed the engine already reads), three targets (manager card, enablement queue, in the flow of work), six questions for Product. Makes no claim about what the Intradiem platform can take in.
3. **Current_State_Assessment.src.html.** CSA as `config/csa.json` (Kathryn's wording verbatim) + `csa_scoring.js` (same file inlined in the page and run under node). Three items marked PROPOSED for Kathryn: plain-word stage labels replacing ADKAR terms, 5/3/1 status-to-rating conversion for Sections B, E, A2, per-dimension risk bands. One parenthetical naming two ADKAR stages was cut from her High Risk rollout text. Overall score is withheld until all nine dimensions score. Answers stay in localStorage; page sends nothing.
4. **Adoption_Offer_Sheet.src.html.** For Derek: Assess / Run / Orchestrate, price a literal blank per tier, no Greenlight mention, durations marked proposed.

**Why:** proves "all their AI tools" with a second real-shaped adapter instead of a slide, and gives Joey, Kathryn, Product and Derek each one concrete thing to react to.

**How to apply:** next moves are human, not build: group DM confirming the scope change, the Derek session, Kathryn's review of the three proposed items, Product's six answers (Chris Busbee). Not yet done: dashboard does not show the second tool or the portfolio roll-up; no deploy (auto mode blocks wrangler, and customer data must never sit on the personal Cloudflare account). Mem0 quota was exhausted Sep 20 (resets Oct 1), so this exists in files only. Related: [[side-quest-measurement-layer-sep9]].
