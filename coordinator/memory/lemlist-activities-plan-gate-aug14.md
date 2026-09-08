---
name: lemlist-activities-plan-gate-aug14
description: "Lemlist /api/activities plan-gate (402, emailPro-only) from 2026-08-14 was CLEARED by 2026-08-30 — REST activities and campaigns routes are open again; the relay is now MCP-primary with REST as a working fallback"
metadata: 
  node_type: memory
  type: project
  originSessionId: 896ac857-2e46-4c92-ad41-a83545bdb792
  modified: 2026-09-08T07:14:15.066Z
---

As of the 2026-08-14 16:37 PDT hourly run, `GET https://api.lemlist.com/api/activities?limit=100` (workspace key `tea_h82tSpLDH9vt59tkJ`) returned HTTP 402 with body `"route is available starting emailPro plan"`. This was the trigger for redesigning the hourly lemlist-to-Slack relay job as MCP-primary (get_inbox_conversations, get_campaigns_stats) with REST as a legacy fallback.

**UPDATE 2026-08-30:** the gate is gone. On the 15:20 CDT run, the lemlist MCP connector itself was unauthenticated/unavailable (a separate, connector-level outage, not a plan gate), so the job fell back to REST per protocol — and both `/api/activities?limit=100` and `/api/campaigns` returned real 200 data, not the 402 string. So the underlying Lemlist plan restriction from Aug 14 has cleared at some point in the last two weeks (upgrade or trial renewal happened without a note here). Caveat: `/api/campaigns/{id}/stats` (the only REST stats sub-route found) returns sent/delivered/opened/clicked/replied counts only — not the bounced/unsubscribed/meetingBooked/linkedinInvitationAccepted shape the MCP campaign-stats step and `.lemlist-relay-stats.json` track, so that specific comparison still can't be done over REST; the activities feed diff covers all actionable types on its own, so this doesn't lose event coverage, just the redundant stats-count cross-check.

**Why:** matters for two separate things going forward — (1) don't assume a future 402 log entry means the same Aug 14 trial-lapse cause; check current billing state fresh, and (2) if the lemlist MCP connector (claude.ai lemlist) goes unauthenticated again, REST is now confirmed as a genuine working fallback for activities/tasks/campaigns, not just a theoretical one.

**How to apply:** if a relay log entry says REST fallback was used, that's normal degraded-but-working operation now, not a "Dallas must fix billing" flag — check the lemlist MCP connector's auth state (claude.ai connector settings) first, since that's what's actually breaking, not the Lemlist plan. Related but distinct from [[lemlist-relay-campaign-map-gap-aug7]] (a routing-config gap, not an API outage).

**UPDATE 2026-09-08 (02:13 CDT run):** MCP tools weren't findable via ToolSearch at all this run (not an auth failure, just absent from the deferred-tool registry). REST fallback confirmed still working — `/api/activities?limit=100` and `/api/tasks` both returned real 200 data. Found a real cross-surface dedup gap while diffing: the MCP-path stats-diff dedups via `.lemlist-relay-stats.json` and never writes to `seen_activity_ids`, so an event already relayed under MCP still reads as "new" to a REST-fallback run checking `seen_activity_ids` — caught one duplicate bounce (Jim Moore/Humana, cam_N92Tgg29ncHWnYAD9) that was about to get re-posted to #gtm-outbound-nathan a day after it already went out. Closed by back-filling `seen_activity_ids` with the REST batch's ids. If this recurs, the fix is to check both dedup stores whenever the surface used differs from the prior run's.
