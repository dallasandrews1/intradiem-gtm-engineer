# Intradiem GTM Platform: one brain, many surfaces

The control principle, made real: **you own the brain, sellers get a thin surface.**
The engine, the configs, the data, and Clay all live in one hosted service that only
you (and anyone you authorize, like Naveen or Genna) can change. Sellers ask in plain
language from Slack or Claude and get a plan back. They cannot see or alter anything.

```
   Slack app  ─┐
   Claude plugin ┼──>  GTM BRAIN (hosted, yours)  ──>  the two engines + impact
   Salesforce (v2) ┘        auth + request log              configs, data, Clay
```

Every request is logged in `brain/logs/requests.jsonl` with who called and what.
That log is both your audit trail and your adoption metric for ELT.

## 1. Deploy the brain

It is a FastAPI service. Any Python host works (Render, Fly, Railway, a VM, or your
own box). Docker is included.

```bash
# from the project root (so the engine folders are in build context)
docker build -f gtm-hosted-platform/brain/Dockerfile -t intradiem-gtm-brain .
docker run -p 8000:8000 -e GTM_API_KEYS="slack:SLACK_KEY,claude:CLAUDE_KEY" intradiem-gtm-brain
```

Or without Docker:

```bash
cd gtm-hosted-platform/brain
pip install -r requirements.txt
GTM_API_KEYS="slack:SLACK_KEY,claude:CLAUDE_KEY" uvicorn app:app --host 0.0.0.0 --port 8000
```

`GTM_API_KEYS` is a comma list of `label:key` pairs. Give each surface its own key so
the log tells you which surface drove which usage. Without it set, the service runs
open in dev mode. Put it behind your SSO or IP allowlist for production.

Endpoints: `/v1/strike`, `/v1/strike/{domain}`, `/v1/signals`, `/v1/signals/{domain}`,
`/v1/impact`. All require `X-API-Key`.

## 2. Slack app (sellers self-serve where they already are)

Create a Slack app (api.slack.com/apps), enable Socket Mode, add a slash command
`/strikeplan`, and grant `commands` + `chat:write`. Then:

```bash
cd gtm-hosted-platform/slack
pip install -r requirements.txt
SLACK_BOT_TOKEN=xoxb-... SLACK_APP_TOKEN=xapp-... \
BRAIN_URL=https://your-brain-host BRAIN_API_KEY=SLACK_KEY \
python slack_app.py
```

A seller types `/strikeplan amerihealth.com` and gets the snapshot, why-now, and a
first touch per persona, posted just to them. `/strikeplan` alone returns the list.

## 3. Claude plugin (plain-language, plug and play)

The plugin lives in `plugin/intradiem-gtm`. Edit `.claude-plugin/plugin.json` to set
`BRAIN_URL` and the `claude` key, then distribute it (zip the folder, or host it in a
plugin marketplace). On install, a seller asks in natural language: "strike plan for
AmeriHealth," "what's hot today," "any expansion risk on Centene." The bundled MCP
client calls your brain; no engine or data ships to the seller.

The plugin includes a skill that teaches Claude when to use the tools and always
carries the verify-before-send guardrail.

## Governance, the part that protects you

- **One brain, you own it.** Surfaces are swappable clients. The value and control sit in the brain.
- **Per-surface keys + request log.** You see exactly who used what. That is your audit trail and your adoption number for ELT.
- **Verify before send.** Every output is marked a draft on sample data; the benchmark and peer claims must be verified against real Intradiem proof before anything goes out. Nothing auto-sends.
- **Only the owner changes the brain.** Sellers cannot touch thresholds, triggers, data, or copy. Config changes route to you, or to a leader with the authority, like Naveen or Genna.

## Salesforce (v2, later)

A button on the Account record that calls `/v1/strike/{domain}` and renders the plan
in CRM. Same brain, one more thin surface. Deferred until the Slack and Claude
surfaces have proven adoption.
