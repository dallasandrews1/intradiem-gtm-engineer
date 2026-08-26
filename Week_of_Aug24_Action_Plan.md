# Week of Aug 24, 2026: action plan

Built Fri Aug 21 from the seven Otter recordings of Aug 17-21 (Jack 1:1, AI Champion handoff, Side Quest kickoff, Naveen/Nate/Jack/Carter tooling call, Jen/Nate/Jack AI sales goals, AI Champions standup, Carter marketing-ops sync) plus the project memory.

## The week in one line

Lemlist payment is the single blocker in front of four motions. The Sep 2 webinar sends must leave this week. The 6sense credits expire Aug 31. Everything else is follow-through on promises I made out loud this week, and every one of those gets closed by Monday EOD.

## Five priorities, in order

1. **Unblock Lemlist payment and go live.** Get Luis's written invoice, hand it to Chris for Ramp, confirm paid, then mailboxes/subdomain, Nate's number, Jack's white-glove setup, team "we're live" note. Six campaigns are staged; nothing launches until this clears.
2. **Put Sep 2 webinar invites in flight.** Lists are built (8,004 WFM + 4,392 customer ops + 1,165 net-new verified). Tuesday with Naveen: lock sender, dates, Pardot import, suppression list, UTMs. Invites leave no later than Wed Aug 26.
3. **Close every open promise from this week** (list below). This is the credibility lever: things I said I'd send, sent.
4. **6sense Monday: walk in with three specific asks**, not complaints. 216K credits, ~2K used, expiring Aug 31. Decide in the room what the last-sprint use is, and leave with the contract term/renewal date.
5. **Set up the AI Champion seat properly** (Monday.com access + accurate goal language + Friday update) and stage the Side Quest dashboard scope before the Derek working session.

## Open promises from this week (close Monday)

| Promised to | What I said | Status / action |
|---|---|---|
| Jack (Aug 18) | "I finished the thing, I'll send it over" (VodafoneThree ops-layer build) | Confirm sent. If not, send Monday AM. |
| Jack (Aug 17) | Share the LinkedIn workflows doc/link | Send Monday AM. |
| Carter (Aug 21) | Send the webinar Clay workflow + contact list, then a Clay walkthrough session | Lists and brief already built (`motions/marketing/Sep2_*`, `Webinar_Leads_Brief_Aug21.html`). Send Monday AM with a 30-min walkthrough invite for Wed or Thu. |
| Carter / Naveen (Aug 18) | Add Carter to the Clay account | Verify the invite he mentioned landed and he can log in. |
| Jen, Nate, Jack (Aug 20) | Update on how Chris pays Lemlist | Send the moment Chris confirms. If still stuck Tuesday, say so plainly with the next step, never silence. |
| Naveen, Nate, Jack (Aug 18) | Follow up with Chris + Luis: payment received, Nate's phone number setup | Monday AM email to Luis (invoice + number provisioning), forward to Chris. |
| Naveen (Aug 18) | Notify the team when Lemlist is confirmed ready | Fires the day access lands. |
| Naveen (Aug 18) | Coordinate with Sierra + marketing on Clay for the webinar | Done in substance (lists sent to Naveen Aug 21). Tuesday is the decision meeting. |
| Jack + Naveen (Aug 18) | Co-author Jack's workflow-builder use-case list (event-driven automations) for Naveen to take to Chris | Draft my half Monday, send to Jack to merge. Keep "already doable today" and "needs a tool" as two columns so the ask is honest. |
| Jen (Aug 20) | Add a 6sense workflows/intent-signals segment to the Aug 24 rep meeting | Ask Sierra/Carter Monday first thing who owns the agenda and add it. |
| Side Quest team (Aug 18) | Lead dashboards/tracking; share at check-ins | Draft the scope this week (below). |
| AI Champions (Aug 21) | Send Luis's written invoice to Chris for Ramp; route future AI tool requests through the contracts team | Invoice: Monday. Contracts routing: note it in the Lemlist thread so it's on record. |

## Pre-built Sunday Aug 23 (status)
- DONE: State Farm + Centene committee pages staged (gate clear on both, render verified, deploy command staged NOT run; see `~/Desktop/Intradiem Deliverables/deploy-icp-committees/STATE_FARM_CENTENE_REFRESH_Aug23.md`). Open gap: State Farm contact-center/QO lane needs a sourcing pull.
- DONE: BO Insurance Titles segments live in Clay Audiences (Customers 15 / Prospects 68, all Director+, 0 credits, balance 67,861.8). Registry updated.
- DONE: `verint_backoffice` trigger in the TAM engine config, tests 21/21. Follow-up: engine has no back-office persona key yet.
- DONE: back-office ICP skill updated with the Aug 18 insurance intel. Ask Naveen for his written CNI department map.
- DONE: messaging-study intake (`motions/messaging-study/`) and `Workflow_Builder_UseCases_Draft_for_Jack.md`.

## Day by day

### Monday Aug 24
- **8:00** Email Luis: written invoice, Nate's phone-number provisioning, mailbox/subdomain purchase path, confirm the data-deletion-on-cancel language in writing (Jason Jones's open condition from Aug 13). Forward invoice to Chris with one line: "Ready for Ramp; let me know when it's through and I'll have the team live that day."
- **8:30** Send the Monday-AM batch: Jack (ops-layer build + LinkedIn workflows doc), Carter (webinar workflow + lists + walkthrough invite), Jen/Nate/Jack (Lemlist status, one paragraph).
- **6sense rep meeting.** Three asks: (1) exact mechanics to spend the remaining credits on contact records at our named accounts without overwriting Salesforce fields (Jenna's question, my concern); (2) what the "audience workflows" Sierra built actually produce and whether any output can feed Clay; (3) contract term and renewal date, in writing. Do not argue Clay vs 6sense in the room. Carter is the bridge for that conversation; he's already a Clay user.
- **PM** Monday.com: confirm access to the Operational Excellence workspace and the AI Initiatives boards; if blocked, ping Randy. Reword the product-team AI goals so they read as automation and scale, not "AI" as a label. Sales-side goal language already agreed with Jen: AI SDR goal Done with "change of direction, would require purchasing a toolkit, revisit Q2 2027"; Medicare Star Ratings GTM Done.
- **PM** Start the messaging-study intake: a folder and a rubric ready before Nate's emails and the Memory Blue (Aidan, Tyler) examples arrive. Reply/no-reply, channel, persona, pattern, so the analysis turns around in a day, not a week.

### Tuesday Aug 25 (GTM engineering cadence with Naveen)
Bring, in this order:
1. Lemlist status in one sentence and the go-live day.
2. Sep 2 webinar decisions: sender, send dates (two touches, Aug 26 and Aug 31), Pardot import of the 1,165 net-new with Lead Source "Clay, Sep 2 webinar", registrant suppression list, UTM per list. Offer the 419 errored rows as a retry if he wants volume.
3. Naveen's stated priority stack, read back: 1 Star Ratings, 2 back office existing customers, 3 back office new logo, 4 webinar registrations. Confirm nothing moved.
4. ABM test he asked for: State Farm and Centene, ten buying groups x ten message angles. Bring the buying-committee pages for both (the ICP committee builder does this) so the test design is concrete, not hypothetical.
5. Insurance back-office titles from his CNI contact (Chief Administrative Officer, SVP Administration, Claims Shared Services, Actuarial) folded into the back-office ICP and the Clay segments, plus "Verint back office in use" as a fit signal. Show it's done, ask if the department map he wrote down can be shared.
6. Messaging study: intake is ready, waiting on Nate's and Jack's exports.
7. One question: does he want me to take the John/KJ "AI SDR" framing conversation directly, as offered Aug 20.

### Wednesday Aug 26
- Webinar touch 1 goes out (if Tuesday locked it). Confirm Pardot import landed and suppression applied before send.
- Carter Clay walkthrough (30 min). Agenda: the live webinar workflow, Audiences segments, Clay Gens, what "campaign ideas" he's bringing back. Leave with two concrete marketing campaigns to build.
- Lemlist: if paid, provision mailboxes and start warmup the same day (warmup is the timing variable). Configure Jack's account first, Nate's second, with a short written setup sheet Jack can run himself.
- Side Quest: draft the dashboard/tracking scope (Greenlight usage: who, how often, which agents, trend; intervention triggers; a current-state assessment view). Check with Krishnan so my metrics and his Aug 31 adoption baseline are the same numbers, not two sets.

### Thursday Aug 27
- Jack's n8n/workflow-builder use-case list: finalize with Jack and send to Naveen.
- Messaging study: if inputs are in, run the pattern analysis and write the "what worked" one-pager; pipe findings into the MessageGen prompts and Lemlist A/B variants.
- Lemlist: load the first Star Ratings follow-up campaign for Nate in draft (dry run, human sign-off, no AI voice, per Jason Jones's pilot conditions). Do not send until warmup is green.
- Derek working session if scheduled: bring the dashboard scope and ask the three open questions (how he wants updates, his vision for the deliverable, productization vs internal framework weight).

### Friday Aug 28 (AI Champions standup, 7:00 PT)
Update, 60 seconds, peer-level, nothing about failures or holdups: Lemlist status; AI-enabled prospecting complete; interactive sales enablement 25% with the next milestone named; webinar lists built in Clay incl. ~1,200 net-new, invites in flight; Side Quest scope drafted. Ask Jen whether she wants me in the John conversation on AI SDR framing.
- Friday readout for Naveen (standard).
- Update Monday.com percent-complete so the company scorecard reads correctly before month end.

## Watch list (no action required yet, but know them cold)
- **Adam's BOO/UHG pilot Sep 23.** The Back Office Optimizer launch kit should be ready before that date; ask Adam next week what GTM needs to have in hand.
- **Crayon purchased for competitive intel; Kayla departing.** Ask who inherits it; the competitive-intel skill should consume Crayon output, not duplicate it.
- **Tyler Vogley, new Director of AI Enablement, starts within 30 days.** Catherine meets him day one about the Side Quest. Have the GTM Engine page and the self-serve skills story ready for an intro.
- **Einstein Activity Capture** is why Jen can't track booked meetings. Any "AI SDR" conversation should name that as the prerequisite, not a tool gap.
- **Gong / call recording.** Naveen ranked pipeline above conversion; keep a one-page Gong vs Otter comparison ready, don't push it.
- **Clay enterprise upgrade.** Jack and Jenna both want it; the webinar result is the proof point. Raise after the webinar numbers land, not before.

## Tone rules for the week
No failure or holdup language anywhere leadership sees it. Head start, ongoing build. Contractions. Automation-first with judgment checkpoints. Credit mindful, and any Clay spend over ~100 credits gets a test and an estimate first.
