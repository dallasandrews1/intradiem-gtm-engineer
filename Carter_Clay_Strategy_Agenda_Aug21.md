# Dallas / Carter, Clay (Fri Aug 21 2026, 10:00 CT, 30 min)

Carter's ask (Aug 18 DM): how Clay is being used, where we cross over, the webinar enrichment work.

## 1. His stack (2 min)
Which platform owns webinar registrations and nurture, and whether Salesforce Lead Source / Lead Status are written by it or by hand.

## 2. Webinar leads, done (8 min)
Brief: https://claude.ai/code/artifact/052807bb-8588-4935-a743-74bfc6ae8f51 · CSV: `motions/marketing/Webinar_Leads_Enriched_Routed_Aug20.csv`
- 1,016 "Webinar" registrants processed; persona, route, corrected title/domain, triage stored on each Audiences record (fields `Clay Persona Key`, `Clay Webinar Route`, `Clay Enriched Title`, `Clay Company Domain`, `Clay Triage`).
- 560 in ICP (wfm 431, cc_ops 116, back office 12, cx 1); 176 at Prospect accounts, 275 at accounts not in the SF sync, 94 at customers (flagged). 52 Director+.
- 954 of 1,016 have no Lead Status in SF.
- Workflow `wf_0tk333zvDnGg4YcikFp` is live for new registrants. 170 credits for the backlog.
- Not done: outreach; write-back to Salesforce. Both his call.
- `WebHelp Registration` (2,831) is customer help-portal signups, kept separate.

## 3. Audiences facts he needs (5 min)
- Synced from Salesforce: 140,805 people, 2,283 companies, 7,841 deals. Segments built: Current Customers (SF) 92, Prospects (SF) 1,848, Cold-Outbound Exclusion 133, Account Type Missing 300, BO Leaders customers 337 / prospects 1,541, Webinar Leads 1,016.
- Account Type is incomplete: Elevance Health and TD Bank absent; Cigna, Assurant, Farmers, McKesson, Citi, British Gas tagged Prospect; 300 blank; brand domains (syf.com, evernorth.com) don't match. Suppression on Account Type alone includes customers. Sales Ops (Genna) owns cleanup.

## 4. Carve-up (5 min)
| Lane | Owner |
|---|---|
| Inbound and marketing enrichment (webinars, content, events, 6sense pushes, MAP hygiene, ad audiences) | Carter |
| Outbound motions, gates, sending, customer-exclusion audits | Dallas |
| Shared: Audiences field naming, credit ledger (one line per run), workspace folders, the customer-flag union rule | Both |
Rules: credit estimate before any run over ~500 rows (Enrich Person 0.5/row, full contact waterfall ~13/row); every segment gets a description; no workflow writes to Salesforce until the mapping is read back once.

## 5. Decisions needed from him (5 min)
- Write-back destination for the webinar workflow: SF Lead Status, Slack, or MAP.
- Whether the 176 Prospect-account registrants go to the BDR lane, and who owns the 94 customer registrants.
- 50-row persona review: when.

## 6. Crossovers
- 6sense credits expire Aug 28-30 (Monday 13:00 touchbase): enrichment runs in 6sense on SF filters; Clay supplies target definitions and the agency LinkedIn list.
- ZoomInfo (Aug 26): if bought, it becomes a provider inside Clay waterfalls.
- Back-Office Marketing Alignment (Monday 13:30): BO Leaders segments are the prepared lists.

## Close
One item he owns by next Friday; agree the ledger line; 20 minutes on the Aug 25 GTM engineering cadence.
