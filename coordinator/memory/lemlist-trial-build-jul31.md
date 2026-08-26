---
name: lemlist-trial-build-jul31
description: Jul 31 Lemlist build state - 3 adaptive Stars campaigns live in Draft (IDs inside), behavior-branching sequences, hand-check passed with zero customer hits, what still blocks lead load (Nate channels, Wave 1 export, flag rulings)
metadata:
  type: project
---

Executed the [[lemlist-trial-gameplan-jul31]] build on Jul 31 2026 evening. Full review package (all copy, verified lists, flags, action order): `Intradiem GTM Engineer/motions/star_ratings/Lemlist_Trial_Build_Review_Jul31.md`.

**Live in Lemlist (all Draft, zero leads, weekdays 9-18 ET, clicks OFF, reply/meeting = stop lead + stop company):**
- Stars - Resurrection (Nate) = cam_sh3JCJoxtEHyjGrsw
- Stars - Fresh Pool / Quality (Nate) = cam_viEbB6HkYsCPtxKbi
- Stars - Fresh Pool / Finance (Nate) = cam_2gy9hmEvMjYEuPZ8A

Sequences are ADAPTIVE trees, not linear: invite-accepted branches (LinkedIn thread vs phone/email path), hasPhoneNumber branches (no junk call tasks), and on Resurrection an emailsOpened branch (warm vs cold breakup). All LinkedIn sends/invites manual-approve. Copy = Jul 13 Wave 1 send-ready set adapted + new Resurrection copy, zero Intradiem stats.

**Hand-check PASSED:** all 94 fresh-pool candidates (63 Quality incl cc_ops, 31 Finance) hand-compared against the full 101-account SF customer file with alias traps (HCSC, 12 Kaisers, SCAN, Molina, Elevance, BCBS NC, Aetna/CVS/UHC cluster, Medica-FL-vs-MN). Zero customer hits. Clay's 6-name allowlist gap (missing kaiser/scan) confirmed harmless for this table today.

**Flag rulings (Dallas, Jul 31 evening): all recommendations approved.** Cut 13 clinical-gap rows (CareFirst/Lumeris/MGB/GuideWell), hold 2 Excellus email rows, cut 5 wrong-persona cc_ops rows; cc_ops fold-in stays (18 rows, shown as own block at final gate); qbp_avg from Accounts (Master) where it exists, otherwise the lead runs the 1B opener. Post-cut, pre-dedup counts: Quality 50, Finance 24.

**Blocks lead load (in order):** (1) Nate's Lemlist ACTIVATION EMAIL is blocked by the corporate mail filter (DM + Randy Brown thread Jul 31); Randy requires a case emailed to internalsupport@intradiem.com before IT will allow lemlist.com senders; Outlook write tools are permission-blocked in coordinator sessions so Dallas sends the case himself (paste-ready text delivered in chat). Until the case clears, Nate can't even create his account, let alone connect mailbox/LinkedIn; (2) Resurrection cohort + fresh-pool de-dupe need Dallas's export of the Wave 1 Persona 1/2 campaign Leads tabs (sent/replied) - Clay campaign objects are unreachable by any API path (Enterprise observability gate, reconfirmed); (3) Dallas rules on cut flags: 13 rows at do-not-send clinical-gap parents (CareFirst/Lumeris/MGB/GuideWell), 2 Excellus email-holds, 5 wrong-persona cc_ops rows, cc_ops human_approved=false wholesale, qbp_avg source (no such column; cs_star is NOT it; pull from Accounts or use 1B variant).

**Also built:** `automation/lemlist_pulse.py` + run_lemlist_pulse.sh (validated live) writing lemlist-pulse-DATE.md logs for the rundown; API key in automation/config/lemlist.env. Webhooks deliberately NOT used (no listener endpoint exists; polling covers receipts).

**Gotchas learned:** Lemlist MCP create-campaign can get classifier-blocked then succeed later on identical calls (build state must be re-checked live, never assumed from errors); create response says status "running" but campaigns actually land in draft; add_sequence_step with type=conditional returns YES/NO branch sequenceIds and branch steps are added into those; manual/phone steps hold a lead until completed or skipped.
