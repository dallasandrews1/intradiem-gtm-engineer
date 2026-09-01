---
name: lemlist-relay-slack-read-blocked-aug27
description: "2026-08-27 01:11 CDT lemlist-relay run: Slack MCP tools were loaded and slack_search_channels found both rep channels, but slack_read_channel returned channel_not_found on both — a new failure shape (access-denied, not tool-absence) in the same recurring pattern as lemlist-relay-session-tools-absent-aug19"
metadata: 
  node_type: memory
  type: project
  originSessionId: ac5ccb8a-37f5-4a9e-a59e-9407c379663a
  modified: 2026-08-27T06:12:55.365Z
---

The 2026-08-27 01:11 CDT hourly lemlist-to-Slack relay run (see [[lemlist-relay-campaign-map-gap-aug7]] for the job's shape) hit a Slack access gap distinct from the prior known failure mode. Unlike [[lemlist-relay-session-tools-absent-aug19]] (where Slack tools didn't load into the session at all), this run had Slack MCP tools loaded and `slack_search_channels` correctly resolved both #gtm-outbound-nathan (C0BM9V6KGSG) and #gtm-outbound-jack (C0BN0JT9D6U) with matching IDs — but `slack_read_channel` returned `channel_not_found` on both, twice, even after confirming the IDs via search. Both are private channels, so this reads as an app/session membership gap on the specific channels rather than a bad config or a fully-down connector.

Practical effect: step 7 thread ingest could not be independently verified this run. Fell back to citing the last confirmed state from the same day's earlier 00:10 CDT run (which *did* read both channels successfully and found, consistent with [[daily-action-brief-never-posted-rep-channels]], no Daily Action Brief messages and no rep replies in either). Logged to `automation/logs/lemlist-relay-2026-08-27.md` and `automation/logs/brief-thread-ingest-2026-08-27.md` (evt: lemlist-relay-2026-08-27#slack-channel-read-blocked).

**Why this matters:** the relay's Slack surface has now failed in two different shapes across separate runs (total tool absence on Aug 19, search-works-but-read-fails on Aug 27) with hours of clean runs in between both times. That's consistent with session-to-session flakiness in how the claude.ai Slack connector's app membership/auth resolves for these two private channels specifically, not a one-off fluke.

**How to apply:** if a third distinct failure shape shows up, stop treating each as isolated — flag to Dallas directly that the Slack MCP connector's access to #gtm-outbound-nathan/#gtm-outbound-jack is unreliable across sessions and needs a fix at the app-membership level (adding the Slack app to both channels explicitly, or checking why it drops), rather than continuing to log-and-move-on each time.
