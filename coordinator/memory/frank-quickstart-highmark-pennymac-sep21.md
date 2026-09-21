---
name: frank-quickstart-highmark-pennymac-sep21
description: "Sep 21 2026: Frank's 3xG Back Office QuickStart pair (Highmark, PennyMac): org charts from the executive office to front-line supervisors plus cold call talking points; staged not deployed; Clay live check stalled; method and traps"
metadata:
  type: project
---

Frank Ciccone emailed Naveen and Dallas (cc Haresh, Kevin Jolliffe) at 4:30pm Sep 21 2026 with two 3xG research briefs (Jeremy Roderick) and asked for the org chart "from VITO on down to front line managers" and cold call talking points per executive. "Back Office QuickStart Program" is defined nowhere readable (Outlook, Slack, Teams, Otter, SharePoint); Frank owns what it offers.

**Built, staged, nothing deployed or sent:** maps at deploy-backoffice-maps/frank/{highmark,pennymac}/ (86 and 87 people across six and five maps), call plans at .../<slug>/call-plan/, Frank's index at three accounts, Desktop folder "Frank Back Office QuickStart - Sep 21". Builders: motions/back_office_expansion/ (sweeps/frank_quickstart/_run_sweeps.py, frank_qs_filter.py, frank_qs_trees.py, build_frank_quickstart_sheets.py, frank_qs_resolve.py, frank_qs_contacts.py, finalize_frank_quickstart.sh, sets/frank_highmark.json, sets/frank_pennymac.json) and motions/partner_channel/frank_quickstart/ (talk_tracks.py, build_quickstart.py). Log: automation/logs/frank-quickstart-2026-09-21.md.

**Depth below Director is new:** the shared gates stop at Director on purpose; frank_qs_filter.py adds managers and supervisors by title plus an operations vocabulary. build_bo_map_artifact.py gained two opt-in flags, hide_salesnav_status and hide_hero_stats (Assurant page proven byte-identical).

**Traps found:**
- highmark.com misses about 40 percent of Highmark people in Clay find-and-enrich, including the COO; retry under the company page linkedin.com/company/highmark-health. enGen (goengen.com) runs health plan operations for Highmark and needs its own sweep.
- Clay's index showed Tom Doran as health plan COO; he is leaving and Gustavo Giraldo was named president Aug 24 2026. Executive cards follow company releases, never the index.
- Clay's Enrich Person live refresh stalled for hours (1 of 418 items). frank_qs_resolve.py and frank_qs_contacts.py now have --submit and --collect so a slow queue never blocks a build; pages state the live-check count truthfully.
- Back Office Optimizer is BETA in Q4 2026. Talk tracks must follow marketing's V04 framework (BOO_Industry_Outreach_Messaging_Framework_V04.pdf): recovered productive time is what both customer results measured; the capacity and service-risk read is the newer half; automated re-skilling is roadmap and is never claimed. No compliance promise, integration specifics wait for a technical session, lead with service and cost, never monitoring.
- Blinded registry figures on a CALL are inside the Sep 18 ruling (sequences carry call steps); the reviewer first read the V04 tier as email and LinkedIn only.
- About a third of the 3xG brief's checkable claims did not confirm at a primary source; the held list is on each call plan. Blue KC's 1 million members and about $3 billion DID confirm (Highmark release May 28 2026; close Apr 1 2026).

**Open:** run finalize_frank_quickstart.sh when Clay clears; PennyMac's Five9 record (Register Lead since Jan 30 2026) is unread, so pages carry the allow-stale stamp; Cianfrocco's dial is held for a warm route via the Optum relationship; 3xG must write its own "why is 3xG calling" lines.

Related: [[frank-assurant-package-sep16]], [[keegan-three-account-package-sep17]], [[bo-map-pipeline-rep-sets-aug31]], [[feedback-talking-points-defend-before-delivery]].
