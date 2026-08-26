---
name: sep2-webinar-invite-lists-aug21
description: "Sep 2 2026 webinar (Operationalizing AI for Business Outcomes, Jennifer Lee + Donna Fluss/DMG, reg bit.ly/4yzs95x): Clay invite pool built Aug 21 from Salesforce-synced Audiences at 0 credits, six tiered segments (WFM 1,428 customers / 6,578 prospects; CC ops+BO 4,392 customers / 26,119 prospects), CSVs + brief in motions/marketing; marketing sends via Pardot; suppression list and send owner still open"
metadata:
  type: project
---

Context: Naveen (Aug 6-7) asked Dallas to use Clay to drive attendance to the DMG webinar; Melissa (marketing lead, Aug 6 GTM action plan call) proposed it as the Clay test run starting with additional contacts at existing customers, noting marketing's own email promotion underperforms. Webinar: Wed Sep 2 2026, 12:00-1:00 PM, Jennifer Lee (co-CEO) with Donna Fluss (DMG Consulting), registration bit.ly/4yzs95x (Aug 7 Intradiem LinkedIn post).

Built 2026-08-21 (CLI, 0 credits): six Audiences segments (ids in `Clay_Build_State_Registry.md`): T1 WFM titles (customers 1,428 / prospects 6,578 / prospect Director+ 1,262), T2 contact-center ops + back office (customers 4,392 / prospects 26,119 / prospect Director+ 17,558), email present, existing webinar leads excluded. Exports: `motions/marketing/Sep2_Webinar_Invite_T1_WFM_Aug21.csv` (8,004) and `Sep2_Webinar_Invite_T2_CustomerOps_Aug21.csv` (4,392) with SF ids, brand-domain customer corrections (Optum/UHC/Cigna/Anthem/TD tagged Prospect in SF), stale-title flags. Brief: `Sep2_Webinar_Invite_Brief_Aug21.html` + artifact. Lead Source values include `pardot` = marketing's MAP.

**Why:** the invite pool already lives in Salesforce; selection and cleanup, not enrichment, was the job. Net-new sourcing outside SF is phase 2 (credits).

**How to apply:** for any event-attendance ask, start from Audiences segments by title x Account Type, export SF-keyed CSVs for Pardot, offer rep one-liners for Director+ at prospects, then source net-new only if volume is short. Open: who sends, dates, registrant suppression list, UTM, net-new go/no-go. Related: [[carter-webinar-lead-engine-aug20]], [[clay-audiences-live-cli-capability-aug20]].

**Net-new pool built Aug 21 (Dallas: "use credits to find people who AREN'T in Salesforce"):** 2,015 WFM + contact-center people sourced free via `clay search query-mode` at 345 registrant-producing accounts; email waterfall workflow `wf_0tk4jo5z7RjGKo3rvR8` (Work Email fn + ZeroBounce) via bulk routine; **3,005.6 credits (1.49/row, over the 1.3 test rate and ~180 over the ceiling), 1,165 net-new verified emails, 309 Director+**; 363 late-flagged as already in SF; 419 runs failed (retry candidates). Dallas approved option A explicitly after the 20-row test; the warn-before-large-spend rule came from this thread. Deliverables `Sep2_NetNew_Contacts_Verified_Aug21.csv` + `Sep2_Webinar_Attendance_Plan_Aug21.html` (artifact https://claude.ai/code/artifact/35c958ef-5542-49fa-834e-67ae4feed880).

**Aug 21 ~11:00 CT: sent to Naveen** (artifact v3, the simplified "invite list, built in Clay" page, same URL). Dallas's DM framing: built the invite lists for marketing's Sep 2 webinar in Clay incl. ~1,200 net-new contacts not in Salesforce; talk next steps Tuesday (Aug 25 GTM engineering cadence). Open with marketing: sender + dates, Pardot import of net-new (Lead Source "Clay, Sep 2 webinar"), current registrant list for suppression, UTM per list. 419 errored email rows are retry candidates if volume is wanted.
