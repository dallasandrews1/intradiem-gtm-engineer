---
name: lemlist-relay-slack-mcp-instability-aug30
description: "Slack MCP connector failed twice in one lemlist-relay run cycle on Aug 30 2026 (channel_not_found, then timeout/closed-socket) - a new, different failure mode from the known launchd job crash pattern"
metadata: 
  node_type: memory
  type: project
  originSessionId: ae2e89a4-e3f9-4827-90d4-3df4e6ef7353
  modified: 2026-08-30T08:54:03.261Z
---

On 2026-08-30, the hourly lemlist-to-Slack relay job hit two separate Slack MCP read failures on the same two rep channels (#gtm-outbound-nathan C0BM9V6KGSG, #gtm-outbound-jack C0BN0JT9D6U) within a few hours: `channel_not_found` at 01:29 CDT (resolved by 02:14 CDT), then a 931s timeout plus immediate closed-socket errors at 03:43 CDT. Logged with evt anchors `lemlist-relay-2026-08-30#slack-channel-access-lost` and `lemlist-relay-2026-08-30#slack-timeout-recurrence` in automation/logs/lemlist-relay-2026-08-30.md and brief-thread-ingest-2026-08-30.md.

**Why:** This is distinct from [[war-room-recurring-api-crash]] (whole job dies mid-response, no log) - here the job survived and logged the blocker correctly, but the Slack MCP connector itself is intermittently unreliable (two different error shapes in one day: permission-looking error, then transport-looking error). No actual harm yet because neither rep channel has ever had a "Daily Action Brief" message posted (tied to the [[rundown-job-outage-since-aug11]] outage), so there's nothing in-thread to miss - but if the rundown job starts firing again and reps start replying DONE/SKIP/HOLD, this same instability would make thread-ingest silently blind on whichever runs it hits.

**How to apply:** If Slack MCP reads keep failing across other scheduled jobs (not just this relay), treat it as an infra-level Slack connector issue, not a per-job bug - check whether it clusters with other Slack MCP tool calls in the same time window before assuming it's specific to the lemlist relay's channel IDs or scopes.
