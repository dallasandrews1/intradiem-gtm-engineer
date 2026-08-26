#!/bin/zsh
# ONE-OFF structural smoke test for the Lemlist -> Slack rep-channel relay.
#
# What it proves: that an unattended `claude -p` run can compose the rep-channel alerts
# and actually POST them to Slack through the connector.
# What it does NOT prove: that a real Lemlist wave will fire correctly. The events are
# SYNTHETIC (automation/config/relay_smoketest_fixture.json). Never present this run as
# proof that a live wave will behave.
#
# Blast radius: posts ONLY to the test channel ID passed as $1. Never touches
# automation/config/lemlist_channels.json, never touches #gtm-outbound-nathan or
# #gtm-outbound-jack, never calls the Lemlist API at all.
#
# Usage: ./run_relay_smoketest.sh C0XXXXXXXXX
set -uo pipefail
cd "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"

TEST_CHANNEL="${1:-}"
if [[ -z "$TEST_CHANNEL" ]]; then
  echo "ERROR: pass the test channel ID as the first argument (e.g. C0XXXXXXXXX)" >&2
  exit 1
fi
if [[ "$TEST_CHANNEL" == "C0BM9V6KGSG" || "$TEST_CHANNEL" == "C0BN0JT9D6U" ]]; then
  echo "ERROR: refusing to smoke-test into a live rep channel." >&2
  exit 1
fi

"/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/claude_net.sh" --model claude-sonnet-5 -p "$(cat <<PROMPT
Unattended run: STRUCTURAL SMOKE TEST of the Lemlist-to-Slack rep-channel relay. Nobody is watching live.

The events are SYNTHETIC. Read them from automation/config/relay_smoketest_fixture.json. Do NOT call the Lemlist API. Do NOT read or write automation/config/lemlist_channels.json.

Target channel for every post: ${TEST_CHANNEL}. This is a private test channel with only Dallas in it. Post to NOTHING else. Never DM anyone.

Do exactly this:
1. Read the fixture. Treat every activity in it as a new actionable event.
2. Compose one Slack message per event, exactly the way the real relay would (same rules as automation/run_lemlist_relay.sh):
   - emailsReplied: lead name, title, company, campaign, the reply text, and a DRAFT response in Nathan Belfield's calm peer-level voice (2-4 sentences, contractions, acknowledge then insight pivot then soft CTA, ZERO Intradiem stats or ROI numbers, no em dashes). Label it clearly: "Draft to edit and send from your own inbox, not auto-sent."
   - linkedinInviteAccepted: "accepted your connect" plus the reminder that the LinkedIn message task is now waiting in Lemlist Tasks for manual approval.
   - emailsBounced: one-line warning with lead and campaign so list hygiene happens same day.
3. Prefix the FIRST message with a bold line: "*SMOKE TEST, synthetic data, not real prospects.*" so nothing here can ever be mistaken for a live event.
4. Post each composed message to ${TEST_CHANNEL} via Slack.
5. Write everything you posted, verbatim, to automation/logs/relay-smoketest-<today>.md, and record at the top whether the Slack posts SUCCEEDED or FAILED and the exact error text if they failed. This is the actual finding of the test, so be precise about it.

Hard rules: post only to ${TEST_CHANNEL}. Never DM anyone including Dallas. Never touch a campaign, sequence, lead, or any config file. Never invent an Intradiem number; the drafts carry no stats at all. The only file you may write is automation/logs/relay-smoketest-<today>.md.
PROMPT
)" --dangerously-skip-permissions
