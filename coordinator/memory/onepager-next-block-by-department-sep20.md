---
name: onepager-next-block-by-department-sep20
description: "Sep 20 2026: the twelve-then-forty meeting ladder is the partner channel's only (Haresh's funnel); AE and AM one-pagers now swap the closing Next block by department via shelf.with_next and a required REP[\"next\"] key; rooms, plans.py and the AE self-serve skills still carry 12/40"
metadata:
  type: feedback
---

The "12-minute intro, then 40-minute working session" ladder belongs to the partner channel (Haresh's funnel, see [[partner-pilot-haresh-frank-aug31]]). It leaked into every AE and AM one-pager because all builders read Frank's locked template, where the "What happens next" block is hard-coded. Dallas called it a mistake on Sep 20 2026.

**Why:** partner requirements are not the sales org's. An AE or AM page that promises a partner meeting format misstates how that rep works.

**How to apply:** never edit the partner template to fix this. `motions/keegan/accounts/shelf.py` holds `NEXT` and `with_next(html, kind)`; `build_shelf_generic.py` requires `REP["next"]` (ae, am_expansion, am_save, partner) and refuses to build without it, so the partner ladder is never inherited by default. Blocks chosen Sep 20:
- ae (Keegan): Fifteen minutes (the house ask), then a working session on one unit they pick, with their numbers.
- am_expansion (Alex): a short conversation in back-office wording, then one team with their numbers. No clock, the reader came through an introduction.
- am_save (Inger, all three accounts): a short conversation where they walk us through their day, then "a closer look, if it's useful". Nothing sized, nothing commercial.
- partner (Frank): template unchanged.

66 pages rebuilt and staged (25 Keegan, 30 Alex, 11 Inger), each still one Letter page, diff-verified as Next-block-only; Frank's 15 untouched. Also fixed: the AE page-builder template and example in `keegan/selfserve/skills/ae-page-builder/`, the selector notes in `shelf_alex.py`, `build_kit.py` and `export_library.py`.

**Carried through Keegan's package the same evening (Sep 20 2026), staged, not deployed:** `plans.py` (owner lines and dated moves now read "the fifteen-minute intro" and "the working session"), the three rooms and Keegan's index page rebuilt (diffs were the wording only, shelf links survived, `link_shelf.py` not needed), the three knowledge libraries and `Approved_Claims_and_Proof.md` re-exported, `ae-call-prep`, `ae-reply-handler`, `Project_Instructions_AE.md`, `Walkthrough_One_Page.md`. Trap fixed: `selfserve/export_library.py` re-copied Frank's template into `ae-page-builder` on every run and asserted the 12/40 text; it now writes the template through `shelf.with_next(..., "ae")`. Keegan's Claude project needs knowledge/ and the three skills re-uploaded by hand.

**Deploy state:** `deploy_rep_pages.sh rooms` stopped at the pre-gate on a transient handshake timeout (gtm-operating-map, 200 on recheck); nothing shipped. Order is maps, rooms, plans. `check_plans_site.py` fails until `_staged_pre_job6` is refreshed, because 142 staged files now differ from that snapshot on purpose (138 one-pager and shelf files, 3 Keegan rooms, Keegan's index; classified, nothing else). The only 12/40 left in any staging folder is Frank's and the partner pilot's, which is correct.

Related: [[department-shelves-sep18]], [[keegan-execution-kit-sep18]], [[ae-selfserve-project-sep18]].
