---
name: jw-four-canadian-accounts-sep9
description: "Sep 9 2026: JW MacDonald (james.macdonald@intradiem.com, Canadian enterprise seller) asked for back-office maps on four Canadian prospects (Bell Canada, BMO, Telus, Canada Life); BUILT same day as set jw on the Nate pipeline, 98 people, live at backoffice-maps.pages.dev/jw/, 52.5 Clay + 39 Apollo credits; next is the JW + Nate + Dallas review, then the lemlist sequence"
metadata: 
  node_type: memory
  type: project
  originSessionId: f3e4ae31-1369-4c15-aec2-254bc06182d8
  modified: 2026-09-09T16:48:53.573Z
---

**The ask (Otter nuYxKpBq2snvYNwvjXLjKZYa1Ts, Sep 9 2026 08:31, Naveen + JW + Dallas):** JW gave four accounts on the spot, "different industries, all Canadian": Bell Canada, Bank of Montreal, Telus, Canada Life. He has not "cracked the nut" at any of them; Telus and Bell have "insanely complicated, layered hierarchies" with street title vs internal title confusion. Wants who to talk to, LinkedIn-active people prioritized, no Salesforce duplicates. After the build: a three-way review with JW and Nate ("consume it together as a team"; JW is not meeting Nate all-hands week, may squeeze one in or do it in person), then Dallas + Nate build the multi-channel lemlist sequence. JW will add up to six accounts later. Naveen's framing: automate "peppering" the back office via lemlist while JW works the front-office core group.

**Account facts (Audiences read Sep 9, 0 credits), all four PROSPECTS, all owned by SF user 005V5000004XWIAIA4 (JW):**
- Bell Canada, SF 001V5000006b9K0IAI, 44,610 employees, 280 known people, Consideration / Moderate / Warm, ACD reads Amazon Connect + Genesys Cloud + NICE CXone (Jul-Aug 2026)
- BMO, SF 001V5000006b9JGIAY, 46,722, 275 known, Consideration / Strong / Warm, Amazon Connect (Apr 2026)
- Telus Corporation, SF 001V5000006bGwGIAU, 108,500, only 31 known, Decision / Weak / Cold, Verint WFM (Aug 2025) + NICE CXone + Five9 + RingCentral + Amazon Connect
- Canada Life, SF 001V5000006b7jmIAA, 11,275, 81 known, Consideration / Weak / Cold, Calabrio WFM (Dec 2025) + Amazon Connect
- Telus International (SF 001V5000006b9JHIAY, BPO, 554 known) is a separate account and is OUT of the Telus map.

**What shipped Sep 9:** set `motions/back_office_expansion/sets/jw.json`; 98 people on four maps (BMO 30, Canada Life 30, Telus 20, Bell 18), check_all clean, page `account_maps/jw_backoffice_maps.html` deployed to https://backoffice-maps.pages.dev/jw/ and copied to `~/Desktop/Intradiem Deliverables/Back Office Maps - JW MacDonald (Sep 9).html`; build sheet `BO_Map_Build_Sheets_JW.md` for the Sales Nav map build (map name convention `<Account> - Back Office`). Nothing built in Sales Nav yet; `built` is empty.

**Data lessons (reusable):**
- Bell people list their employer as plain "Bell" (358 of 991 rows); the Bell anchor is `company_name = "Bell"` with `location_country = "Canada"` at the PERSON level, not inside experiences.any.
- Clay's free contacts bridge maps bmo.com to the "BMO U.S." entity; the Canadian bank is `https://www.linkedin.com/company/bank-of-montreal` (bmo.ca also resolves). That identifier lifted BMO from 29 found to 92.
- New config gate flag `assoc_director_ok` (bo_gates.py) because Associate Director is a management tier at Bell, Telus and BMO.
- Apollo people/bulk_match as the paid fallback for free-bridge misses: 1 Apollo credit per match, ~55% match rate, about half of matches usable, the rest confirmed leavers. Worth it only on VP+ and on the thinnest account's director layer.
- The SF known layer at all four is largely stale (Ares left BMO, Kristjanson left Canada Life, Fedorchuk left Canada Life Jun 2025, Michael Jones retired Apr 2026, Zoppi left Telus, Gendron and Frappier changed roles at Bell).
- Telus has two back offices: telecom (billing, revenue assurance, service delivery) and TELUS Health (employer operations, benefits administration, disability management). Hesham Fahmy is EVP COO & CIO since Feb 2026. Mona Malone is BMO CAO since Jul 2025; Brady Aarssen is Canada Life SVP Canada Operations since Oct 2025.

Related: [[nate-six-accounts-bo-maps-aug31]], [[bo-map-pipeline-rep-sets-aug31]], [[feedback-linkedin-active-takes-precedence]], [[feedback-sf-presence-is-info-not-exclusion]], [[naveen-call-sep2-demo-three-acts]].
