---
name: dwo-shell-load-plan-sep4
description: Sep 4 2026, DWO Executives shell LOADED on Dallas's go (690 leads in cam_SiD4KmWcRuhiF6uhL, draft, never launched), Email 1 A/B on per-lead angle variables, 64 leads without URL flagged unconfirmed, sender still the main mailbox
metadata:
  type: project
---
DWO Executives - Live Pool (Nate) cam_SiD4KmWcRuhiF6uhL: `motions/dwo_executives/load_dwo_shell.py <scratch>` (dry run; `--go` loads leads, never launches). Sep 4 plan: 700 loadable of 1,135 wave 1 rows at 285 accounts; holds: 368 no verified email, 52 title filter (chief of staff, deputy, associate, assistant, chief nursing, chief medical, specialist, analyst, office of), 9 moved company, 4 already in BO Net-New (Elwood, D. Clark, S. Smith, Malee), 1 disputed (mm@fidelity.com), 1 account/company disagree. Rule A new-in-role 76; angles core 450 / customer 160 / transformation 90 (182 family swaps so no two people at an account share an angle); 32 provider-unit COOs flagged for Nate.

**Why:** Email 1 in lemlist hard-codes the core angle, so the family swap only works if the three middle paragraphs become per-lead variables (`angleIdea`, `angleProof`, `angleAsk`); the loader already fills them. Lead fields also carry `cohortId` / `cohortArm` for the Lane B pilot ([[lane-b-pilot-dwo-cohort-sep4]]).

**How to apply:** order on go: (1) edit E1 A and B templates to the variables while the campaign has zero leads, (2) `--go`, (3) integrity sweep + three previews. Sender stays the intradiem.com main until lemwarm clears nathan.belfield@intradiemhq.com (active, DNS 100/100, lemwarm state not readable by API). Nate read page: Desktop/Intradiem Deliverables/DWO_Executives_Nate_Read_Sep4.html.


**Update Sep 4 late morning:** loaded on Dallas's go. Email 1 A and B edited to {{angleIdea}}/{{angleProof}}/{{angleAsk}} first, then 699 loaded, then the free bridge on the 85 email-only rows exposed six movers/noise plus three account mismatches (Fincik, George mapped to AAA Texas; Mastrean now FIS): removed via ~/.local/bin/lemlist-lead-remove. 690 leads, test 336 / holdout 354, 94 possessives patched (loader now uses poss()). Lesson: a verified email without a LinkedIn URL is not proof of a current seat; the bridge found 6 of 13 resolvable email-only DWO rows had moved.


**Update Sep 4 afternoon:** after the delegated spend pass the campaign holds 804 leads at 346 accounts (test 399 / holdout 405), 36 without a URL, 36 provider-unit COOs flagged; still DRAFT on the main mailbox.


**Copy check Sep 4 afternoon:** Email 1 was 139-167 words as first loaded; a trimmed Email 1 was loaded and REVERTED on Dallas's word (copy stands as the Sep 4 doc wrote it, median 128 words); NAME_MAP for long account names and the possessive rule kept. Email 2 no longer dates the 12,000 VTO hours. Nate page live at https://dwo-exec-read.pages.dev; Nate has not reviewed DWO copy yet. Campaign 803 after Vega's removal.
