---
name: rep-index-pages-sep20
description: "Sep 20 2026: one working-page index shape for every rep (AE Keegan live; AM Alex and Inger, partner Frank live); shared builder build_rep_index.py; hostname rename recommended, not done"
metadata:
  type: project
---

**Shape (live for Keegan, staged for the rest):** per account the next dated move by owner with the rep first, computed in the browser from the room's own plan source so it cannot go stale; the gate line; one button to the room; text links. Plan-less page shelves sit on one line under the cards. Standard: [[feedback-seller-pages-no-fluff]].

**Builders:** Keegan `motions/back_office_expansion/build_keegan_index.py`; everyone else `motions/shared/execution_kit/build_rep_index.py [alex inger frank]`, which reads Alex's `plans.py`, the Elevance and Cleveland Clinic comms plan JSON, and parses Assurant's plan out of `build_room.py` with ast. Adding a rep = one entry in `reps()`.

**Objective changes the page:** AM expansion and partner indexes carry the sales kits line; the save index (Inger) carries nothing commercial and tags the renewal month. The Sales Navigator build is filtered out of the rep's moves (`NOT_THE_REPS`).

**State Sep 20 2026 evening:** all four rep indexes LIVE on backoffice-maps (alex, inger, frank deployed f9241b30; `/inger/` is new). Alex's six rooms are rebuilt and STAGED, not deployed, with the Sales Navigator build moved to a new GTM Engineering lane at the source (`plans.py` ENG lane, Elevance comms plan JSON edited as text to keep its formatting); `link_shelf.py` rerun; the staged Alex index was rebuilt after that and differs from live, so it deploys with the rooms.

**Hostname, corrected Sep 20 2026 late:** the decided name `account-plans` did NOT get its hostname. `account-plans.pages.dev` belongs to someone outside the account; our project of that name got `account-plans-7kb.pages.dev` and sits empty, not deleted. The fallback project `intradiem-accounts` got the clean `intradiem-accounts.pages.dev` and is the migration target, layout /<rep>/ index, /<rep>/<account>/ room and its tails, /<rep>/<account>/map/ map. `backoffice-maps` and `save-rooms` keep serving and are never deleted. Phase one is additive; redirects are a separate phase two on Dallas's explicit go, path-preserving, 302. See [[wrangler-pages-force-delegation-trap]] before any wrangler call.

**Links in the wild (Sep 20 2026):** Jen Lee holds backoffice-maps.pages.dev/ (root), save-rooms.pages.dev/cleveland-clinic/inger/, icp-committees, gtm-partner-pilot, webinar-invite-list, plus Keegan's 16 package URLs from the Sep 18 04:22 email; Keegan holds the same 16 in Slack. Registry: `automation/config/shared_links_manifest.json`, swept in full Sep 20 (43 holder entries, 65 URLs; gate `automation/check_shared_links.py`, see [[shared-links-gate-sep20]]). Any migration or rebuild must pass that file as a gate: old hostnames keep serving, never deleted, redirects path-preserving and 302 first. Add every newly sent link to it.

**Leadership holds these links too (Sep 20 2026 assessment):** the no-fluff rebuild did not remove anything Jen's email claims (maps with every person checked current, room with routes and who does what by week, sourced brief, one-pager all still there; Cleveland Clinic save room untouched). Two things changed for a leadership reader: the 122 counter is off Keegan's index (rooms still sum to 122 people; validated emails now sum to 112, not the 113 in the email, because Dakota Pelletier left and came off the map), and the pages are now date-driven, so a plan whose dates lapse will read as stale to anyone opening the link later. Recommendation given: one version for everyone, never a frozen showcase copy; keep plans current through their last dated move.

**DEPLOYED Sep 20 2026 late (Dallas ran `automation/deploy_rep_pages.sh` from his own terminal; this session's deploy was blocked, see [[claude-code-auto-mode-blocks-deploys]]):** backoffice-maps 8853c6ec, save-rooms cb4680fa, intradiem-accounts 2d103c00 (phase one, 211 files, layout /<rep>/, /<rep>/<account>/, /<rep>/<account>/map/). Live now: Alex's six rooms, Inger's Cleveland Clinic room, Frank's Assurant room and 13 shelf indexes in the no-fluff shape; AM roadmap fit on seven rooms (never on Inger's); Keegan's live-state wording fix and provenance line; Nate's two restored pages. Gate 97 of 97; Jen's 21 links intact and newest, plain and cache-busted. No redirects exist; phase two needs Dallas's explicit go. STANDING RULE: three hosts now, so every rep-page deploy is `maps`, `rooms`, then `plans` (the new tree is assembled from the two old folders; skip it and the new host goes stale). Builders read base URLs from `motions/shared/site_config.py`. Thread log: `automation/logs/rep-pages-thread-2026-09-20.md`.

**Open:** the en dashes in Salesforce-recorded titles on Alex's rooms are FIXED and live (clean() in both builders). Verification note: right after a Pages deploy the first cache-busted samples can still return the prior page; re-sample before calling it a mismatch.

Related: [[keegan-package-refresh-sep20]], [[department-shelves-sep18]].


**Sep 21 2026:** Frank's index gained a call-order card (`order` list plus `room`) for accounts with a call plan but no dated room, and `brief` links on pages-only shelves. The old `build_frank_index.py` overwrote this page once during the QuickStart build; it is retired for Frank.


**Sep 23 2026 redesign:** all four indexes now share `motions/shared/rep_index_theme.py` (hero with the rep's own moves for this week and next, date rail with relative-week chips, card anchors). Any look change goes in the theme, never in one builder. Headless Chrome's minimum window is 500px; check phone width with a 390px iframe, not a 400px screenshot. Log: `automation/logs/rep-pages-thread-2026-09-23.md`.
