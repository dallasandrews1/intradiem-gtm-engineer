# Account briefs (partner channel)

One JSON per account in `data/`, two pages per account from `build_briefs.py`: `<Account>_Brief_Internal.html` (everything, with an internal note on the 3xG savings table) and `<Account>_Brief_Partner.html` (partner-safe: no item marked internal_only, no UNVERIFIED or EMPLOYEE SENTIMENT flag, no dollar figure anywhere, no Verint-replacement language; the build fails if any of those survive). `Compare_Briefs_<date>.html` is the side by side against Jeremy Roderick's Gemini brief on the same two accounts.

| Folder | What it holds |
|---|---|
| `data/` | The JSON the pages are built from (sections, leaders, triggers, questions, confidence, gaps, sources, deck lines). Edit here, never in the html. |
| `research/` | Raw output of the signal-researcher fan-out, one file per account, verbatim. |
| `contacts/` | Clay free-path contact pulls (0 credits) with a labeled role guess per person. Not a freshness check. |

Pipeline per account (Sep 1 2026 dry run on Ally Financial and Maximus): gate (Salesforce customer-or-partner segment, pre-pipeline overlap) → signal-researcher on Jeremy's eight-section spec, 2025 and 2026 sources first, flags kept → two Clay free-path contact pulls (executive layer, then operations / WFM / shared services / automation) → JSON → pages → checks. No credits over the free path; emails run on the picked cohort after Frank's go.

Rebuild: `python3 build_briefs.py` (all) or `python3 build_briefs.py ally`. Local files only; the internal pages carry 3xG seat data and are never deployed.
