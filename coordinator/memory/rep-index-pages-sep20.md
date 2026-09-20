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

**Open:** en dashes inside Salesforce-recorded titles on four live Alex rooms (pre-existing; Alex's builder has no clean() normaliser). Verification note: right after a Pages deploy the first cache-busted samples can still return the prior page; re-sample before calling it a mismatch.

Related: [[keegan-package-refresh-sep20]], [[department-shelves-sep18]].
