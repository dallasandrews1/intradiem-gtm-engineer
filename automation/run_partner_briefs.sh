#!/bin/zsh
# Partner-brief request loop for #gtm-partner-briefs (Frank Ciccone, partner channel).
# A partner-team member posts an account name in the channel; this job returns routing context
# (who registered it, what stage, which AE to loop in, customer status) and the branded brief. DRY RUN by default: replies to
# nothing and deploys nothing until "live": true in automation/config/partner_briefs.json.
# Never DMs Dallas; the daily rundown reads automation/logs/partner-briefs-<date>.md.
# Runs every 5 minutes; launchd will not start a second instance while a build is still running,
# so a long build simply delays the next poll.
set -uo pipefail
cd "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"

# Business-hours guard: no Claude session outside 07:00-18:59 CT weekdays. Requests posted
# off-hours are simply picked up by the first morning poll. Costs nothing to skip.
H=$(date +%H); DOW=$(date +%u)
if [ "$DOW" -gt 5 ] || [ "$H" -lt 7 ] || [ "$H" -gt 18 ]; then exit 0; fi

"/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/claude_net.sh" --model claude-sonnet-5 -p "$(cat <<'PROMPT'
Unattended scheduled run: partner-brief request loop. Nobody is watching live.

Config and state: automation/config/partner_briefs.json (channel_name, channel_id, live flag, seen_request_ts). Log: append to automation/logs/partner-briefs-<today>.md, incremental as you go (never one write at the end), evt anchors per LOG_CONVENTION.md for anything another job might act on.

Do exactly this:
1. Resolve the channel: if channel_id is empty, load the Slack MCP tools (ToolSearch "select:mcp__claude_ai_Slack__slack_search_channels,mcp__claude_ai_Slack__slack_read_channel,mcp__claude_ai_Slack__slack_send_message") and search for channel_name. Not found: write one log line "channel not created yet, exiting" and exit. Found: write the id into the config.
2. Read the channel's last 50 messages. A REQUEST is a top-level human message naming one or more companies (an account name alone, or "brief: X", "run X", a short list). Ignore bot messages, thread replies, and anything in seen_request_ts. No new requests: one quiet log line, exit. Never post a heartbeat or an all-quiet message.
3. ACK FAST: the moment a new request is recognized and live=true, reply in its thread BEFORE any research: "On it. Gate check first, then the full brief; links land in this thread in about 15 minutes." (live=false: write the would-be ack to the log instead.) Then, per new request, per account (cap 5 accounts per run; queue the rest in the log for next run):
   a. ROUTING CONTEXT first, from local files, read-only. This is a routing desk, not a bouncer: the pre-pipeline is the partner team's own work queue, so an account being registered is a reason to COORDINATE, never a reason to stop. Read the newest ref/sf_customer_partner_segment_*.csv under motions/partner_channel/, the newest run under automation/inbox/partners/sf_prepipeline/, and tam-outbound-engine/config/customer_denylist.json, then classify:
      - REGISTERED (in the pre-pipeline): report every matching record with partner, stage, created date and age in days, Intradiem AE, partner AE, category and priority. Say plainly that it is a live registered lead and name the Intradiem AE to loop in. A record at Register Lead or CAM to AE Intro older than 45 days is exactly what the pilot exists to accelerate: say so. A Disqualified record is history, not a block: give the date and note it can be reworked with fresh context. A Converted to Opportunity record means an opp is live: coordinate with the AE, no cold outreach. Build the brief in every one of these cases.
      - PARTNER-CONFLICT NOTE (the one real caution): when a partner other than the one being worked has the registration, the outreach must not name the working partner. State it in one line: "registered by <partner>, so do not name <other partner> in outreach on this account."
      - CUSTOMER (SF segment, denylist, or install base): this one does stop cold new-logo outreach. Report it and say it routes to the account manager for expansion, not to a cold sequence. Still build the brief; the AM can use it.
      - CLEAR: nothing found in any source; say so in one line.
      Near-name matches are reported as CHECK with both names, never as a hard claim. Every classification carries an evt anchor in the log.
   b. Clear accounts: run the briefing engine exactly as motions/partner_channel/briefs/README.md describes: signal-researcher subagent on the eight-section spec (2025-2026 sources first, flags kept), two Clay free-path contact pulls via mcp__claude_ai_Clay__find-and-enrich-contacts-at-company (title filters, NO dataPoints, 0 credits), author briefs/data/<slug>.json following ally.json as the pattern (internal_only / partner_only / flag fields drive the partner-safe filter), then python3 motions/partner_channel/build_briefs.py <slug>. The build MUST exit 0; a partner-safe check failure means no deploy, log the failure loudly, and the thread reply says the brief needs a manual pass before it can be shared.
   c. Deploy PARTNER-SAFE ONLY: copy the *_Brief_Partner.html to ~/Desktop/Intradiem\ Deliverables/deploy-partner-pilot/briefs/<slug>.html, add the account to the briefs index list, wrangler pages deploy per motions/partner_channel/README.md. Internal pages never leave the repo. Verify the deployed URL returns 200 and contains no 3xG seat figures before replying.
   d. Reply IN THREAD on the request message: the routing context first (registered/customer/clear plus who to loop in), then the partner-safe link, then one line that the internal version and verified contacts come through GTM Engineering. Keep it to five lines, no emoji storms, no em dashes.
4. live=false: do steps 1-3 fully EXCEPT the thread reply and the deploy; write the would-be reply and the built file paths to the log under a DRY RUN header.
5. Update seen_request_ts in the config (append processed message timestamps, keep the file otherwise intact).
6. Spend guard: 0 Clay credits beyond the free path (no dataPoints, no Claygent, no email waterfall). Email/phone enrichment is never run by this job.

Hard rules: never DM anyone. Never post outside the configured channel. Never send outreach, never touch lemlist, never edit a gate or a Function. Do not modify files except automation/logs/*, automation/config/partner_briefs.json, motions/partner_channel/briefs/**, and the deploy folder. Verified-claims discipline everywhere: no dollar estimates on anything deployed, only Value Repository 1:many lines as Intradiem claims.
PROMPT
)" >> "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/logs/_run_partner_briefs.out" 2>&1
