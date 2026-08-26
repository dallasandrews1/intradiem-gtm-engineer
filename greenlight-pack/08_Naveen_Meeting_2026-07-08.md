# Naveen Strategy Meeting, Jul 8 2026 (transcript processed same day)

Source: Otter transcript "Customer Strategy Planning Meeting." Recording cuts off mid-thread while Naveen is setting up the John Norton presentation idea; anything after that point is unrecorded.

## The one change that touches the build

**New-logo Stars motion excludes existing customers.** Naveen's verbal list: UnitedHealthcare, Humana, CVS/Aetna, Kaiser, Elevance, Molina, and Scan Health ("I believe" a customer). Confirmed NOT customers: Centene ("a big one, we have to include them"), HCSC, and everybody else on the universe. He is sending the Star Ratings file with current customers flagged; that file, then Salesforce read access, becomes the source of truth. Do not rebuild anything from memory of the call.

What this means in the workbook:
- Accounts (Master) needs a `customer_exclude` dimension wired into motion_exclude once the flagged file lands. Free formula work, no credits.
- The 22 Contacts skew heavily to Humana / UHC / CVS, which are now existing-customer lane, not Wave 1 targets. Contacts stay (attribution intact); they move to the expansion motion bucket. Centene and Medica contacts remain Wave 1 eligible.
- **Wave 1 approvals HOLD until the flagged file lands.** Nothing was sent, no human_approved box was ever checked, so the gate did exactly what it was built to do. The 10 pre-gate draft leads were already slated for purge; the purge now also drops existing-customer leads.
- The Humana re-grade demo (contacts land, account flips A) stays valid as a demo. Wave 1 targeting shifts to non-customer parents.

**Two motions, cleanly separated (Naveen's framing):** Stars new-logo motion serves the new-logo sales team first. Back-office expansion (Queue Optimizer + the upcoming launch) sells into existing customers through the account-manager lane (Mary Ann and Rachel). Both stay in scope; new-logo goes first.

## Ratified (no correction offered)

- **Zero-credit build discipline and the gate design.** He walked the workbook live: "this looks good," "that's phenomenal," "mind blowing." No pushback on grading basis (307 scored / 98 Tier A+B), the waterfall table structure, or the native sequencer.
- **The credit story, verbally ratified.** Worst-case quarter spend for the main motion ~3,000 credits: Tier A+B committee expansion 1,150 to 1,500; back-office pull 1,000 to 1,400; ~40% headroom under the review flag; Claude alerts at 3,500. Naveen's reaction: leadership had assumed they would burn through credits ("they came to sell us 80k worth"); the efficiency story lands as a renewal-negotiation asset. Matches 02_Credit_Spend_Plan.md; no spend authorized, per-run pre-estimate + explicit go unchanged.
- **Portfolio positioning:** position Intradiem as a whole, the entire portfolio moving star ratings, consistent with the DWO platform email of Jun 27.
- Naveen knows Star Ratings cold from a prior role. Drop the explainers in his direction permanently; he said so directly.

## Open questions he raised (not settled)

- **Contract-specific vs company-level messaging** when a leader maps to a particular contract. He flagged it as a discussion to have. Bring a recommendation, not a question.
- Attribution definition and the 15/10x/200 shaping did not come up. Still owed from the Week 1 plan.
- Scott Kemme / back-office ICP conversation not mentioned; back-office pull stays gated on it.

## His commitments

1. Send the flagged current-customer file (the Star Ratings sheet, colors or flags per row).
2. Claude Enterprise access: "give me a couple of days," actively fighting for it. Bottleneck is approval, not Chris; path runs through Jason Dowden (VP of Technology / AI enablement) and a second Jason (AI engineer, runs internal projects).
3. Intro to Jason (AI engineer) on Friday.
4. Raise Salesforce read-only access at the Thursday 12pm meeting with Nate and Genna.
5. Go through the workbook tables plus the clay-build site, come back with pointed questions, set a follow-up meeting.

## What Dallas owes

1. Nothing sent, approvals held, until the customer file lands (see above).
2. Function roadmap site made live (committed on the call; currently local only).
3. Thursday 12pm with Nate and Genna: Salesforce read-only ask framed as nomenclature + report-pull access, nothing write-level. Also the first real look at Nate's current manual motion.
4. Friday: Jason intro. Thirty-second competence read happens here; the access approval likely follows it.
5. Salesforce MCP connector once Claude Enterprise access lands (read-only, replaces manual lookups).
6. Probable: the engine presentation for John Norton (CRO, more technically savvy than the CMO). Naveen's framing: marketing would get "a shock," play it politically, route through Norton first. Transcript cut before the ask was finished; confirm scope with Naveen before building.

## New cast (add to stakeholder map)

- **Mary Ann** and **Rachel**: existing-customer account managers, strong at expansion selling; the lane back-office motion eventually feeds.
- **Jason Dowden**: VP of Technology / AI enablement; Claude Enterprise approval path.
- **Jason (second, surname unknown)**: AI engineer, runs internal AI projects; Friday intro.
- **John Norton**: CRO; target audience for the engine presentation.
- **Greenlight**: internal Claude-based assistant wired to Salesforce, Q&A only, no Cowork. Posture stated on the call and worth keeping verbatim: Dallas builds skills FOR Greenlight (the company AI mandate); he does not work IN Greenlight. Interim: usable to learn Salesforce field nomenclature.

## Political context (current GTM motion, Naveen's own words)

Marketing hands MQLs plus event-booth contacts to Nate; Nate manually drafts messages with Claude day in day out; meetings route to ~25 salespeople; 2 BDRs total. Naveen called the system archaic unprompted. The engine replaces exactly this, which is why the Norton-first routing matters: marketing sees it as a shock, the CRO sees it as throughput.

## Discipline notes

- "5k a month" was said conversationally on the call. Keep the ledger discipline: 5,000 allocated to this motion, workspace credits are the larger pool with the May 2027 expiry. Say "allocated," never monthly entitlement, in anything written.
- Transcript garbles to watch: "Sentinel" = Centene, "11th"/"elements" = Elevance, "HSPC" = HCSC, "QVP" = QBP, "Greenlight/green light" = the internal tool, not the exec go-ahead.
