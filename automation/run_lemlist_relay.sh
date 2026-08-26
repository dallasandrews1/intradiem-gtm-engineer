#!/bin/zsh
# Lemlist -> Slack relay for the rep channels (#gtm-outbound-nathan / #gtm-outbound-jack).
# Turns Lemlist prospect behavior into rep action items: reply alerts with a drafted response,
# invite-accepted alerts (the LinkedIn message task just unlocked), meeting-booked, bounce warnings,
# and a pending-task digest. DRY RUN by default: posts nothing until "live": true in
# automation/config/lemlist_channels.json (Dallas flips it at launch). Never DMs Dallas directly;
# the daily rundown reads this job's log (single-morning-brief rule).
set -uo pipefail
cd "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"

python3 automation/lemlist_pulse.py >> "automation/logs/_run_lemlist_relay.out" 2>&1 || true

"/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/claude_net.sh" --model claude-sonnet-5 -p "$(cat <<'PROMPT'
Unattended scheduled run: Lemlist-to-Slack relay for rep channels. Nobody is watching live.

Config and state: automation/config/lemlist_channels.json (channel IDs, campaign-to-channel map, seen_activity_ids, and the "live" flag). automation/config/lemlist.env has LEMLIST_API_KEY.

PLAN GATE CONTEXT (Aug 15 2026): the lemlist trial ended Aug 13 and most REST routes (including /api/activities and /api/campaigns) now return "route is available starting emailPro plan". Only /api/tasks is confirmed still open. The activity surface is therefore MCP-FIRST with REST as a legacy fallback if the plan is ever upgraded.

Do exactly this:
1. PRIMARY SURFACE (MCP): run ToolSearch with query "select:mcp__claude_ai_lemlist__get_inbox_conversations,mcp__claude_ai_lemlist__get_campaigns_stats". If the tools load:
   a. Fetch unread inbox conversations (listId: unRead) and also myConversations page 1. A conversation whose last message is FROM the lead and whose id+lastMessageDate is not in seen_activity_ids is a REPLY event.
   b. Fetch campaign stats for every campaign id in campaign_channel_map. Compare bounced / unsubscribed / meetingBooked / linkedinInvitationAccepted counts against the previous snapshot in automation/logs/.lemlist-relay-stats.json (create it if missing; write the fresh snapshot at the end of every run). A count increase is that many new events of that type.
   If the MCP tools do NOT load this run: try the legacy REST route curl -s -u ":$LEMLIST_API_KEY" "https://api.lemlist.com/api/activities?limit=100". If that returns the plan-gate string, write one loud line to the log: "BLOCKED-PLAN-GATE: no activity surface available this run (MCP absent, REST gated). Replies are UNWATCHED until this clears." with an evt: anchor, then still do the tasks step and thread ingest below before exiting. Never let the block kill the run silently.
   Always fetch open tasks via REST (still ungated): curl -s -u ":$LEMLIST_API_KEY" "https://api.lemlist.com/api/tasks?filters=%5B%5D" (the filters query param is REQUIRED and must be a URL-encoded JSON array; a bare /api/tasks call returns {"error":"Malformed filters"}. %5B%5D is the empty array, meaning no filter.) Tasks already marked done are excluded by the API.
2. Diff events against seen_activity_ids in the config (for MCP reply events use "<conversationId>|<lastMessageDate>" as the id). Actionable NEW events only: replies, linkedinInviteAccepted, meetingBooked, bounces, send failures, unsubscribes.
3. For each new actionable event, compose the rep-channel message, routed by campaign_channel_map:
   - emailsReplied: lead name, title, company, campaign, and a DRAFT response in Nathan's calm peer-level voice (2-4 sentences, contractions, acknowledge then insight pivot then soft CTA, ZERO Intradiem stats or ROI numbers, no em dashes). Label it clearly: "Draft to edit and send from your own inbox, not auto-sent." If the reply text is available in the event, tailor the draft to it; otherwise keep it category-neutral.
   - linkedinInviteAccepted: "accepted your connect" plus the reminder that the LinkedIn message task is now waiting in Lemlist Tasks (manual approve).
   - meetingBooked: short congrats line plus lead/company. This is a receipts event, flag it prominently in the log too.
   - emailsBounced / emailsSendFailed / emailsUnsubscribed: one-line warning with lead and campaign so list hygiene happens same day.
4. Task digest, RIDE-ALONG ONLY: a channel that is already receiving at least one new-event message this run may have one compact open-task digest appended to it (count plus the first few lead names). A channel with no new events this run gets NOTHING, even if that rep has open tasks. Open tasks stay open for days, so a standalone digest would repeat every hour and train the reps to ignore the channel.
5. Check "live" in the config:
   - If live is false: DO NOT post anything to Slack. Write everything you would have posted, verbatim per channel, into automation/logs/lemlist-relay-<today>.md under a "DRY RUN" header.
   - If live is true: post the composed messages to the mapped channel IDs via Slack (channels only, never DM anyone), AND write the same content to the log.
6. Update seen_activity_ids in automation/config/lemlist_channels.json (append the new activity ids, keep the rest of the file intact).
7. THREAD INGEST (closes the daily-brief DONE/SKIP/HOLD loop): for each rep channel in the config, read replies threaded under today's and yesterday's Daily Action Brief messages (the messages titled "Daily Action Brief"). Any rep reply matching a name + DONE / SKIP / HOLD gets logged to automation/logs/brief-thread-ingest-<today>.md as "<timestamp> <rep> <lead name> <verb>". A HOLD additionally gets a prominent flag block in that log ("HOLD: nothing is auto-paused, Dallas must pause the lead in Lemlist") AND a short threaded acknowledgment reply under the rep's own message ("Logged. Nothing pauses automatically, flagging Dallas to pause this lead today.") so the rep sees the loop is alive; the acknowledgment is the ONLY thread reply this job ever posts, and only when live=true. Never act on the lead itself: no pausing, no task changes. The daily rundown reads this ingest log; a HOLD there is a same-day action item for Dallas.
8. SILENCE ON EMPTY (hard rule, this job runs hourly 24/7): if a channel has no new actionable events this run, post nothing to it (a HOLD acknowledgment threaded under the rep's own reply is exempt, it is a response, not an alert). If there are zero new events across the board, post nothing anywhere, write one "no new events" line with a timestamp to the log, and exit. The log is the only place a quiet run is ever recorded. Never post a heartbeat, a status line, an "all quiet" note, or a "still monitoring" message to a rep channel.

Hard rules: never DM anyone (Dallas included; the rundown reads the log). Never post to any channel not listed in the config. Never start, pause, or edit a campaign, sequence, or lead. Never invent an Intradiem number; drafts carry no stats at all. Do not modify any file except automation/logs/* and the seen_activity_ids array in automation/config/lemlist_channels.json.
PROMPT
)" --dangerously-skip-permissions >> "automation/logs/_run_lemlist_relay.out" 2>&1
