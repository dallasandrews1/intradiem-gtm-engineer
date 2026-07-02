# Signal Engine: Day One in the Role

A short, ordered plan for making the signal engine real once you have access. The
whole system reads two files. Swap those for real data, validate, then turn things
on in order. Do not skip the validation step.

## The two files you swap

**1. `data/accounts.csv`** is the account usage data the engine scores.

Columns it needs:
`domain, company, licensed_seats, active_seats, total_agents, agents_coached,
coaching_sessions_per_day, available_rules, active_rules, wfm_connected,
crm_connected, wfm_days_active, automation_vol_current, automation_vol_prev1,
automation_vol_prev2, champion_changed, days_to_renewal`

**2. `data/owners.csv`** is who owns each account, so signals route to a person.

Columns it needs:
`domain, ae_name, ae_email, ae_slack, csm_name, csm_email, csm_slack`

## Where each piece of data comes from, and who to ask

| Data | Lives in | Ask |
|---|---|---|
| Seats active vs licensed, coaching sessions and coverage, rules active vs available, automation volume (current and prior months), WFM/CRM connected, days WFM active | Intradiem product / reporting database | Product analytics or data engineering |
| Licensed seats, total agents (contract size) | Contract / CPQ data | RevOps or Sales Ops |
| Renewal date (days_to_renewal), champion change flag | Salesforce | RevOps or Sales Ops |
| Account owner (AE), assigned CSM, their email and Slack | Salesforce + the Slack directory | RevOps for the owner export, IT or Slack admin for handles |

Day one this is a nightly CSV export or a scheduled warehouse query, not a live
API. That is fine. The engine is built for it.

## The order to turn things on

- [ ] **1. Get read access and a sample export.** Find who owns the product usage data. Ask for one export with the columns above, even if partial. Map their column names to the engine's column names. That mapping is the only integration work.
- [ ] **2. Validate the signals against reality.** Put the real export in `accounts.csv`, run the processor, and sit with a CSM or AE. Do the numbers match what they already know about those accounts? Tune the thresholds in `config/thresholds.json` until the signals are right. Wrong or noisy signals here will sink the whole thing later.
- [ ] **3. Work one signal by hand.** Have one rep open the queue and act on one signal. Confirm it led to a real conversation. You want proof before any automation.
- [ ] **4. Point the team's MCP and the page at the shared data.** The MCP and dashboard already read the same files. Put them where the team can reach them and confirm `list_monitored_accounts` returns the real set.
- [ ] **5. Run the notifier in dry-run on the schedule.** Install the daily job. Review the digests for about a week. Confirm the right owner would get the right signal, and nothing noisy.
- [ ] **6. Get Sales Ops sign-off, then flip one rep to live.** With ops approval, change the notifier to `--send` for a single rep and a single signal type. Watch how they react.
- [ ] **7. Expand gradually.** Add more signals and more reps as trust builds. Only add Salesforce write-back (auto-creating tasks) after ops explicitly approves the schema.

## Three questions to ask early

- When you modernized the data architecture in 2025, what does it now expose at the event level that the GTM motion is not using yet?
- Who owns the customer product-usage schema, and what is the approval path to surface a derived signal to a rep?
- What is your bar for putting a signal-routing layer like this in front of a customer, on data that touches their usage?

## What is already built, so you are not rebuilding

- Engine, all six signals, routing, suppression: `signal_processor.py` + `config/thresholds.json`
- Query signals inside Claude: `intradiem_mcp_server.py` (MCP)
- Live queue with actioned/snooze: the dashboard Signal Queue tab
- Owner routing to Slack or email: `notifier.py` + `data/owners.csv`
- Daily automation: `run_daily.sh` + the launchd agent

## Do not, on day one

- Auto-DM real reps before the signals are validated. One wrong blast and they mute it.
- Ship a black-box health score. Keep everything rule-based and auditable.
- Turn on all six signals at once. Prove one, earn the rest.
- Write to Salesforce without Sales Ops sign-off on the schema.
