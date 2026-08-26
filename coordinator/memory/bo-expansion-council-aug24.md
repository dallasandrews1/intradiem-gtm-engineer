---
name: bo-expansion-council-aug24
description: "Aug 24 2026 council call (Mary Ann, Naveen, Ellen, Savannah, Nate, Carter, AM): back-office expansion inside customers is a go, ~300 contacts in multi-channel sequences by all-hands (week of Sep 14); Mary Ann's rules (never touch the sponsor's reporting line, SVP-to-Director in back-office functions, AM clears before Nate calls, never say 'existing customer'); AMs share Sales Nav Relationship Maps with Dallas; Naveen opens a 'GTM Engineering' pipeline channel"
metadata:
  type: project
---

Decided Mon 2026-08-24 (Otter xtgffRJp6IXdeO3vi19qY5sfwdA). Strategy and three-week plan: `motions/back_office_expansion/BO_Expansion_Strategy_Aug24.md` (worktree vs-code-agents-window-usage; merge before main-repo jobs read it).

- Mary Ann's rules: (1) nobody who reports into the same leader as our current sponsor (Cigna: Jean Marie's line); targets are SVP to Director in shared services / claims / fraud / payment ops / administration; a distinct-line top officer (CAO when our people report to the COO) is fair game, "start high and get pushed down." (2) AM clears a name before Nate calls behind an email. (3) Never say "existing customer"; most customers rebrand us, only the contact center knows the name.
- Nate: email first then LinkedIn for familiarity, ~6 contacts per account, separate customer sequence beside new logo.
- Sales Nav: every customer account has a hierarchy; AMs share Relationship Maps with Dallas (same contract). Verified Aug 24: maps share to teammates, 30 leads per map, 10 maps per account, no native export, so intake is transcription by Dallas's hand.
- Marketing (Ellen): wants a project plan first; vertical-specific email + LinkedIn examples land early September (Boston this week, Genesys next, all-hands after). 6sense role open.
- Naveen: initiative is named Go-To-Market Engineering (council: Naveen, Dallas, Carter, Sierra, Nate, Jenna, David); new pipeline channel for opportunities from it, taken to pipeline council Aug 24. Target: sequences live on the 300 by all-hands. Tue Aug 25 Naveen + Nate + Dallas start the project plan; group reconvenes early-mid week of Sep 7.
- Dallas's on-record commitments: build org charts / account maps from the AMs' Sales Nav maps, guarantee no AM-known names on his lists, configure Lemlist and hand Nate (and Jack) sequence assets, draft the project plan this week, align messaging with marketing by end of next week.
- Lemlist as of Aug 24: no mailboxes provisioned, API 402 on current tier; contracting closes this week. Confirm the PO tier includes API access.

- Naveen's Slack DM ask (Aug 24, 2:13 pm CDT): an "operational process" for the alignment, replicable for future outbound: marketing gives industry- AND role-specific messaging options, AMs sign off per account ("this type of messaging will/will not work"), then we trigger the sequence; "super important to be scientific about this." Dallas committed to review something with him Tue Aug 25. Built: `motions/back_office_expansion/BackOffice_Outbound_Operating_Process_Aug25.html` (seven steps, AM sign-off sheet, role x vertical messaging matrix, six decisions), artifact https://claude.ai/code/artifact/7572fab6-f3e8-4e45-bcab-ba83c3634265, copy in ~/Desktop/Intradiem Deliverables/.

- Dallas, Aug 24 evening: each AM owns the sign-off sheet and prospect list for their own accounts (Savannah is one AM, not the pool owner); Mary Ann (SVP) wants process and progress at a high level, a weekly one-line-per-account rollup; the Sales Nav org-chart mapping is the most important step after the Clay lists themselves. Facilitation split in the strategy file section 3b.

- Known-contact sources check (Aug 24): Savannah's 214-row seed (SF report export `report1784825852835.csv`, had Account Owner) is NOT on disk and the `Existing_BO_Campaign_Seed` Clay table does not exist among the 20 live tables; the Jul 27 dedup of the 285 against it was done by hand. Audiences people carries SF `Lead Source`, `Lead Status`, `Owner ID` (0 credits) as a broad known-to-Intradiem proxy. The sponsor reporting line only comes from each AM's contact list or Relationship Map; no Sales Nav map gets built or shared to an AM before that AM's list is in.

**Why:** this is Naveen's priority 2 (back office existing customers) with an executive sponsor (Mary Ann) and a dated target; the "hands slapped" risk is the design constraint, not an afterthought.

**How to apply:** the Back Office Account Map per account (known layer / conflict zone / net-new with clearance state) is the clearance mechanism; `owner_cleared` on t_0ti4jj1hfZyEWcfirfU is the state column. Wave 1 = the existing 15 accounts only, six per account, no new sourcing until the maps land. Related: [[week-aug24-commitments]], [[sunday-aug23-tuesday-package]], [[lemlist-approval-status]], [[feedback-no-failure-talk-leadership]].
