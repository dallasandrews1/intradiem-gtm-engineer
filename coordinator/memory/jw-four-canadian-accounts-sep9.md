---
name: jw-four-canadian-accounts-sep9
description: "Sep 9 2026: JW MacDonald (james.macdonald@intradiem.com, Canadian enterprise seller) asked for back-office maps on four Canadian prospects (Bell Canada, BMO, Telus, Canada Life) after Naveen's intro call; built on the Nate net-new pipeline as set jw; review is JW + Nate + Dallas, possibly in person all-hands week"
metadata: 
  node_type: memory
  type: project
  originSessionId: f3e4ae31-1369-4c15-aec2-254bc06182d8
  modified: 2026-09-09T16:15:23.218Z
---

**The ask (Otter nuYxKpBq2snvYNwvjXLjKZYa1Ts, Sep 9 2026 08:31, Naveen + JW + Dallas):** JW gave four accounts on the spot, "different industries, all Canadian": Bell Canada, Bank of Montreal, Telus, Canada Life. He has not "cracked the nut" at any of them; Telus and Bell have "insanely complicated, layered hierarchies" with street title vs internal title confusion (60K to 100K employees). Wants who to talk to, LinkedIn-active people prioritized, no Salesforce duplicates. After the build: a three-way review with JW and Nate ("consume it together as a team"), then Dallas + Nate build the multi-channel lemlist sequence. JW will add up to six accounts later. Naveen's framing: automate "peppering" the back office via lemlist while JW works the front-office core group.

**Account facts (Audiences read Sep 9, 0 credits), all four are PROSPECTS, all owned by SF user 005V5000004XWIAIA4 (JW):**
- Bell Canada, SF 001V5000006b9K0IAI, bell.ca, 44,610 employees, 280 known people, Consideration / Moderate / Warm, ACD reads Amazon Connect + Genesys Cloud + NICE CXone (Jul-Aug 2026)
- BMO, SF 001V5000006b9JGIAY, bmo.com, 46,722, 275 known, Consideration / Strong / Warm, Amazon Connect (Apr 2026)
- Telus Corporation, SF 001V5000006bGwGIAU, telus.com, 108,500, only 31 known, Decision / Weak / Cold, Verint WFM (Aug 2025) + NICE CXone + Five9 + RingCentral + Amazon Connect
- Canada Life, SF 001V5000006b7jmIAA, canadalife.com, 11,275, 81 known, Consideration / Weak / Cold, Calabrio WFM (Dec 2025) + Amazon Connect
- Telus International (SF 001V5000006b9JHIAY, BPO, 554 known) is a separate account and is OUT of the Telus map.

**Build notes:** set `motions/back_office_expansion/sets/jw.json`; sweeps in `sweeps/jw/` via `_run_sweeps.py` (seven lanes per account, 0 credits). Bell people list their company as plain "Bell" (358 of 991), so the Bell anchor is `company_name = "Bell"` with `location_country = "Canada"` at the PERSON level, not inside experiences.any. New config gate flag `assoc_director_ok` (bo_gates.py) because Associate Director is a management tier at Bell, Telus and BMO. The SF known layer at all four is largely stale (Ares left BMO, Kristjanson left Canada Life, Zoppi left Telus); sweep recall against it is not a sweep defect.

Related: [[nate-six-accounts-bo-maps-aug31]], [[bo-map-pipeline-rep-sets-aug31]], [[feedback-linkedin-active-takes-precedence]], [[feedback-sf-presence-is-info-not-exclusion]].
