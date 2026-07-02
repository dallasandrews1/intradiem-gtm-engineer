# Intradiem GTM Signal Engine

A config-driven engine that reads account usage data, computes expansion and risk
signals, and routes each to AE or CSM. One source of truth feeds two surfaces:
the MCP (query signals inside Claude/Cowork) and the dashboard (a shared web view).

Swap the sample CSV for a real Intradiem reporting export and everything recomputes.
Nothing here is hardcoded in HTML or in code: data lives in `data/accounts.csv`,
thresholds live in `config/thresholds.json`.

## Folder layout

```
intradiem-signal-engine/
  config/thresholds.json        all thresholds, routes, suppression window
  data/accounts.csv             raw account metrics (the swap-in point)
  data/signals.json             generated output the dashboard reads
  data/suppression_state.json   created on --suppress runs, tracks last-fired
  signal_processor.py           the engine
  intradiem_mcp_server.py       MCP wrapper (reads the same data + config)
  test_signal_processor.py      asserts known routing outcomes
  README.md
```

## Run it

```bash
python3 signal_processor.py                      # summary of all accounts
python3 signal_processor.py --domain centene.com # one account as JSON
python3 signal_processor.py --output data/signals.json   # feed the dashboard
python3 signal_processor.py --suppress           # apply the 14-day window
python3 test_signal_processor.py                 # 14 checks, should all pass
```

## The six signals

| Signal | Type | Fires when | Routes to |
|---|---|---|---|
| seat_utilization | expansion | active seats >= 85% of contract | AE |
| coaching_coverage | expansion | coaching reaches < 60% of agents, 20+ sessions/day | CSM |
| rule_engine_active | expansion | active rules < 35% of available | CSM |
| crm_not_connected | expansion | WFM live 90+ days, CRM not connected | AE |
| automation_volume_drop | risk | volume down 20%+ MoM for 2 straight months | CSM |
| champion_job_change | risk | champion left, within 90 days of renewal | AE+CSM |

Routing priority is AE, then CSM, then HOLD. An account that fires both an AE and
a CSM signal routes AE with the CSM motion noted (see Centene in the sample).

## Swapping in real data (day one in the role)

Replace `data/accounts.csv` with an export that has these columns. The CSV holds
pre-aggregated 30-day rolling values, which matches a nightly reporting export
rather than a live event stream.

```
domain, company, licensed_seats, active_seats, total_agents, agents_coached,
coaching_sessions_per_day, available_rules, active_rules, wfm_connected,
crm_connected, wfm_days_active, automation_vol_current, automation_vol_prev1,
automation_vol_prev2, champion_changed, days_to_renewal
```

Booleans are `true`/`false`. Add as many rows as you monitor. To change a
threshold, edit `config/thresholds.json`, never the code. Re-run the processor and
both surfaces update.

## Wiring the MCP (query signals inside Claude)

Install the dependency, then point Claude Desktop at the server.

```bash
pip install mcp
```

`claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "intradiem-signals": {
      "command": "python3",
      "args": ["/ABSOLUTE/PATH/intradiem-signal-engine/intradiem_mcp_server.py"]
    }
  }
}
```

Tools exposed: `get_expansion_signals(domain)`, `list_monitored_accounts()`,
`score_all()`, `add_monitored_account(...)`. The team can ask Claude for live
signals on any account in the CSV without opening the page.

## Feeding the dashboard

The dashboard's Signal Queue tab is the live install-base view, driven by the
engine. Refresh it in two steps:

```bash
python3 signal_processor.py --output data/signals.json
python3 build_dashboard.py --html /path/to/intradiem-deploy/index.html
```

`build_dashboard.py` injects the data straight into the page, so it works even
opened from disk with no server. If you also copy `data/signals.json` next to
`index.html` on deploy, the page fetches it on load and shows the freshest run,
falling back to the injected copy otherwise. Either way the page, the MCP, and
the processor read the same numbers and never disagree.

## Routing signals to the owner (Slack / email)

`notifier.py` takes each firing signal, looks up who owns the account in
`data/owners.csv`, and routes it to that AE or CSM. It is dry-run by default: it
prints exactly what it would send and to whom, and sends nothing.

```bash
python3 notifier.py                     # dry-run, preview every message
python3 notifier.py --channel slack     # preview only the Slack DMs
python3 notifier.py --send --channel slack   # go live (needs SLACK_BOT_TOKEN)
```

`owners.csv` is the swap-in point, same idea as `accounts.csv`. Today it holds
sample owners. In the role you replace it with a Salesforce owner export (domain,
AE name/email/Slack, CSM name/email/Slack) and routing becomes real.

A signal routed `AE+CSM` goes to both owners. The suppression window in
`thresholds.json` plus `notified_state.json` stop the same signal pinging the same
owner twice inside the window, which is what keeps reps from muting it.

Going live: set `SLACK_BOT_TOKEN` (bot scopes `chat:write`, `users:read.email`)
for Slack, or `SMTP_HOST/PORT/USER/PASS/FROM` for email. Always validate in
dry-run first, and start with one rep on one signal before turning it on for the team.

## Run it every morning (scheduler)

`run_daily.sh` does the whole loop in one shot: score every account, inject fresh
data into the dashboard, copy `signals.json` next to it, and write the notifier
dry-run to a dated digest in `logs/`. Run it by hand any time:

```bash
bash run_daily.sh
```

To have it run itself every morning at 7am, use the included launchd agent (the
native macOS scheduler):

```bash
cp "com.intradiem.signals.daily.plist" ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.intradiem.signals.daily.plist
launchctl start com.intradiem.signals.daily   # optional: run once now to test
```

Check `logs/launchd.out.log` and the newest `logs/digest_YYYY-MM-DD.txt`.

- Reschedule: edit `Hour`/`Minute` in the plist, then `launchctl unload` and `load` it again.
- Stop it: `launchctl unload ~/Library/LaunchAgents/com.intradiem.signals.daily.plist`
- If the Mac is asleep at 7am, launchd runs the job at the next wake, so you do not miss a day.

Prefer cron? `crontab -e` and add one line:

```
0 7 * * * /bin/bash "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/intradiem-signal-engine/run_daily.sh" >> "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/intradiem-signal-engine/logs/cron.log" 2>&1
```

The daily run is a dry run by design. When the signals have earned trust, change
the notifier line in `run_daily.sh` to `notifier.py --send --channel slack` and it
delivers for real on the same schedule. Deploying the refreshed page to Cloudflare
stays a manual step, since that needs your account.

## Who uses what

- Nathan / AEs: `list_monitored_accounts` and `score_all` to see what is firing and where it routes, before opening Salesforce.
- Sales ops: `config/thresholds.json` to govern what fires and how often (suppression), with no code change.
- You: swap the data source, add accounts, tune thresholds, regenerate both surfaces.
