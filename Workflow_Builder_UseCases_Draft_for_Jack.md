# Workflow builder use cases: my half of the draft (for Jack to merge)

Jack: Naveen asked you (Aug 18) for a list of event-driven automations to justify a workflow builder. Here's my half. Merge yours, cut what you don't like, and send it to Naveen as one list from both of us. I kept it honest with two columns, because the case is stronger when we're clear about what a new tool actually adds versus what I can already run today.

## Column A: doable today (no new purchase, I can build these now)
1. Meeting booked → Slack notification to the AE + channel, prospect agenda email drafted, meeting brief compiled from Clay + account notes.
2. New Clay-sourced contact matches an ICP persona → routed to the right campaign list with persona + message variant pre-assigned.
3. Webinar registrant lands → enriched, triaged (customer / competitor / prospect), routed to BDR review or nurture, stamped back onto the shared record. (This one is already live for the Sep 2 webinar.)
4. Reply lands from any campaign → classified (objection type / positive / referral), draft response prepared in the rep's voice for review.
5. Daily digest: what fired overnight across campaigns, replies to handle first, no inbox archaeology.
6. Call transcript lands → outcomes, next steps, and buyer data extracted; follow-up drafted; flag if a meeting has no post-meeting record.

## Column B: where a dedicated workflow tool (n8n-class) genuinely adds
1. Event listeners on systems I can't poll from my side: Salesforce field changes, Pardot form fills, calendar events, inbound webhook triggers from Lemlist at the moment they happen rather than on a schedule.
2. Team-owned automations: you, Nate, and Memory Blue able to build and edit flows yourselves in a visual editor without me in the loop, which is the real unlock for the UK.
3. Cross-tool chains with retries, error queues, and an audit log that IT can inspect (matters for anything touching Salesforce writes).
4. Long-running stateful flows: multi-day waits ("if no reply in 4 business days, then..."), branching on CRM state at execution time.
5. A shared library of templates across sales AND marketing, so Carter's team reuses the same flows instead of rebuilding.

## The honest framing for Naveen/Chris
Column A proves the demand is real because it's already happening. Column B is what we're actually buying: team self-service, native event triggers, and auditability. Suggested pilot: two Column B flows (Salesforce-triggered meeting prep + no-reply branching), 60 days, success = hours saved per week per rep, measured.

Add your UK day-to-day list and the Memory Blue tasks, and it's ready to send.
