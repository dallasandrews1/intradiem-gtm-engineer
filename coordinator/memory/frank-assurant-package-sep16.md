---
name: frank-assurant-package-sep16
description: Frank's Assurant package; re-centered Sep 21 2026 on Gary Mann (VP Back Office Operations) after Frank said the live deal was not prominent
metadata:
  type: project
---

Frank's Assurant package (map, room, brief, one-pager) hangs off intradiem-accounts.pages.dev/frank. Assurant is Inger's customer with a SagesS3 registration (Tony Rotondi partner AE, Don Cousineau partner RVP), not Accenture.

Sep 21 2026: Frank DM'd that the recent activity was not prominent in the notes and strategy. He was right. The room was a cold multi-door plan that scheduled a 12-minute and 40-minute for October, when both had already happened (Sep 2 and Sep 14) with Gary Mann, and the pre-pipeline record (a0dV500000O4LCvIAN) sat at "Scheduling 2nd Customer Meet", next action Sep 25, est ACV $500K on 2,000 agents. The map had Gary as "President, APAC"; Frank's notes say VP of Back Office Operations.

What Gary confirmed: insurance tracking 1,200 agents plus 550 in loss draft on a homegrown platform; NICE IEX WFM; homegrown "DPA" activity tracker; loss draft under a different chain, mid-migration to Guidewire. He has dashboards; the gap is acting in the moment. Blockers are integration effort and data security ("juice worth the squeeze"), not the value case. Josh owes integration paths from Product. Frank owes Gary a meeting summary and a discovery-question list. Gary offered intros into Connected Living and raised corporate comms to CSRs. Competitive watch: on-prem Cisco moving to cloud, NICE WFM stays (room only, never in the brief or to the account).

Rebuilt Sep 21: rooms/assurant_frank/build_room.py (Gary Mann route first, 7 routes, 14 moves), roadmap_fit_am.py Assurant entry, frank_assurant/build_brief.py. Staged to deploy-save-rooms, deploy-intradiem-accounts and deploy-partner-pilot; gate PASS. Dallas deployed all four Sep 21 2026 (backoffice-maps 95361294, save-rooms 674b5ccc, intradiem-accounts a198133a, gtm-partner-pilot 9cb7cb9b); live content verified by curl. Backups are .bak_sep21a.

Map, same day: Gary Mann added at the top of BO_Map_Build_Sheets_Frank_Assurant.csv (31 rows), linkedin.com/in/gary-mann-8841a313, paid Clay Enrich Person run_0tlpwq3RmqmGzsANpfx (0.5 credit): current at Assurant. His LinkedIn still reads "President, APAC", which is where the wrong title came from; Frank's title stands. Title corrected in Inger's transcribed map_01.csv and Frank's roster; Inger's own map pages pick it up on their next rebuild. _frank_assurant_changes.md carries the ADD for the Sales Navigator map, which is Dallas's hand.

Trap found: check_plans_site.py compares deploy-save-rooms and deploy-backoffice-maps to the frozen _staged_pre_job6 snapshot, so ANY intended edit to a room or map makes `deploy_rep_pages.sh plans` stop. Refresh the named files in the snapshot (backups in ~/Desktop/Intradiem Deliverables/_snapshot_baks_sep21a), never put .bak files inside the snapshot tree. Also pages_live_diff.py reports clean-URL pages (briefs/ally.html) as "NEW, not served live"; they are live at the extensionless path.

Paste-block trap: interactive zsh does not treat # lines as comments, and an apostrophe in one ("Frank's") hangs the shell at quote>. Terminal blocks for Dallas carry no comments and no apostrophes; chain with &&.

**Why:** a package built from public research and a Sep 1 export went stale against the rep's own Salesforce notes within days.
**How to apply:** before building or refreshing any rep package, read the rep's live pre-pipeline or opportunity record notes first; the rep's record sets the plan's starting stage ([[feedback-rep-word-is-the-truth]]).
