# Account briefs (partner channel)

One JSON per account in `data/`, two pages per account from `build_briefs.py`: `<Account>_Brief_Internal.html` (everything, with an internal note on the 3xG savings table) and `<Account>_Brief_Partner.html` (partner-safe: no item marked internal_only, no UNVERIFIED or EMPLOYEE SENTIMENT flag, no dollar figure anywhere, no Verint-replacement language, no What Intradiem can say claims block, and no Likely role column on the people table; the build fails if any of the first four survive). The claims list and the committee-role read are our own working reference, so they stay on the internal version: the partner reps do their own selling and pick their own words. `Compare_Briefs_<date>.html` is the side by side against Jeremy Roderick's Gemini brief on the same two accounts.

| Folder | What it holds |
|---|---|
| `data/` | The JSON the pages are built from (sections, leaders, triggers, questions, confidence, gaps, sources, deck lines). Edit here, never in the html. |
| `research/` | Raw output of the signal-researcher fan-out, one file per account, verbatim. |
| `contacts/` | Clay free-path contact pulls (0 credits) with a labeled role guess per person. Not a freshness check. |

Pipeline per account (Sep 1 2026 dry run on Ally Financial and Maximus): gate (Salesforce customer-or-partner segment, pre-pipeline overlap) → signal-researcher on Jeremy's eight-section spec, 2025 and 2026 sources first, flags kept → two Clay free-path contact pulls (executive layer, then operations / WFM / shared services / automation) → JSON → pages → checks. No credits over the free path; emails run on the picked cohort after Frank's go.

Rebuild: `python3 build_briefs.py` (all) or `python3 build_briefs.py ally`. The internal pages carry 3xG seat data and are never deployed. The partner-safe pages and the compare page ARE deployed, under https://gtm-partner-pilot.pages.dev/briefs/ : after a rebuild copy `<Account>_Brief_Partner.html` to `ally.html` / `maximus.html` and `Compare_Briefs_<date>.html` to `compare.html` in `~/Desktop/Intradiem Deliverables/deploy-partner-pilot/briefs/`, then run the wrangler command in the motion README from `deploy-partner-pilot/`. `briefs/index.html` in that folder is the hub page and has no generator; edit it in place.
