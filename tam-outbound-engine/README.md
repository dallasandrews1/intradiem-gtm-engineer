# Intradiem TAM Outbound Engine

Account to action. For every net-new target account it scores ICP fit, scores
"why now" from live triggers, estimates the recoverable labor cost (ROI), maps the
buying committee the triggers point to, and renders a persona-specific, multi-touch
sequence the owning seller can action the same day.

It runs on external data you can get on day one (firmographics, tech stack, job
postings, news). It does not wait on internal product access, which is why it is
the fastest path to visible pipeline.

## Why this matters

Intradiem has no tool that does sequencing today. This is not a sender, it
generates the play (committee, trigger hook, ROI, drafted cadence) and drops it
into whatever sender the team already uses. The moat is the trigger logic: a daily
play only gets opened if the "why now" is real.

## Run it

```bash
python3 account_engine.py                          # ranked action list
python3 account_engine.py --plan amerihealthcaritas.com   # full strike plan
python3 account_engine.py --top 3                  # just the top N
python3 account_engine.py --output account_plays.json     # feed other surfaces
python3 test_account_engine.py                     # 13 checks
```

## What you swap (the data layer)

- `data/tam_accounts.csv` firmographics + contact-center infra: `domain, company, industry, employees, agent_count, acd, wfm`
- `data/triggers.csv` detected buying triggers: `domain, trigger_type, detail, date` (filled by Apollo, Clay, news, and job scrapers in the role)
- `data/sellers.csv` ownership: `domain, seller_name, seller_email, seller_slack`

## What you tune (the config layer)

- `config/icp_weights.json` fit scoring, four dimensions, 25 points each
- `config/triggers.json` the trigger taxonomy: weight, the Intradiem play, and which personas each routes to. This is the moat, spend your thinking here.
- `config/personas.json` the buying committee and the message blocks each cadence renders
- `config/sequences.json` the 4-touch cadence (Email, LinkedIn, Call, Email)
- `config/roi_model.json` recoverable-cost math: `agents * (idle_min/60) * productive_hours * loaded_cost`

## How scoring works

Fit (0-100) = industry + contact-center scale + tech stack + pain, where pain is
derived from the strength and freshness of the account's triggers. Triggers decay
with age: full weight inside 30 days, down to a floor past 120. Accounts with a
fresh trigger and Tier 1 or 2 fit are the "work today" list. ROI is computed per
account from agent count, so every play carries a dollar figure into the
conversation.

## The honest line

The accounts are real companies; the trigger details and ROI assumptions are
sample inputs to demonstrate the engine. Swap the three CSVs for real enrichment
output and the plays are real. Keep the ROI assumptions in `roi_model.json`
conservative and defensible, since that number goes in front of a buyer.

## Surfaces (built)

**Dashboard.** The Strike List tab on the dashboard (now the default tab) lists
today's ranked accounts and expands each into the full committee and sequences. It
reads a small inlined seed for instant render and fetches `tam_plays.json` (placed
next to `index.html`) for the full sequences on the live site.

**MCP, pull a plan inside Claude.** `tam_mcp_server.py` exposes
`list_strike_accounts`, `get_strike_plan(domain)`, and `accounts_for_seller(email)`.

```json
"intradiem-tam": {
  "command": "python3",
  "args": ["/ABSOLUTE/PATH/tam-outbound-engine/tam_mcp_server.py"]
}
```

**Notifier, each seller's morning strike list.** `tam_notifier.py` prints (dry run)
or sends each seller their ranked accounts with why-now and ROI.

```bash
python3 tam_notifier.py                      # dry-run
python3 tam_notifier.py --send --channel slack   # live (needs SLACK_BOT_TOKEN)
```

**Scheduler.** The signal engine's `run_daily.sh` also scores this engine each
morning, refreshes `tam_plays.json` next to the page, and writes each seller's
strike digest to `logs/`. Same launchd job, nothing extra to install.

## Day-one swap

Replace `data/tam_accounts.csv` (firmographics) and `data/triggers.csv` (real
Apollo, Clay, news, and job-posting signals) with live enrichment, and the plays
are real. Verify everything in `config/proof.json` against real Intradiem proof
points before any send.
