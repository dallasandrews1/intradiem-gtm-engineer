---
name: lemlist-relay-dual-surface-staleness-sep15
description: "The lemlist-relay hourly job's MCP stats snapshot can go stale when a run falls back to REST, causing false-positive diffs on the next MCP run"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4ff8ae38-9be7-4cb8-b2ba-c6bcb6264d67
  modified: 2026-09-15T14:18:01.564Z
---

The lemlist-to-Slack relay job (`automation/config/lemlist_channels.json` + `automation/logs/.lemlist-relay-stats.json`) has two independent activity surfaces: MCP (`get_campaigns_stats`, diffed against the `.lemlist-relay-stats.json` snapshot) and a REST fallback (`/api/activities`, no equivalent stats-snapshot mechanism). Confirmed live on 2026-09-15: a run that fell back to REST (MCP tools not loaded that hour) correctly found and posted a new bounce to #gtm-outbound-jack and added its activity id to `seen_activity_ids`, but had no way to refresh `.lemlist-relay-stats.json` since REST doesn't expose the same campaign-stats aggregate. The next run, back on MCP, diffed against the stale snapshot and saw the same bounce as "new" again.

**Why:** the two surfaces track state independently — `seen_activity_ids` is the single source of truth for what's been posted, `.lemlist-relay-stats.json` is only a diffing optimization for the MCP path and isn't updated by REST-only runs.

**How to apply:** before ever posting a bounce/unsub/meeting/LI-accept event that the MCP stats diff flags as new, cross-check whether its lead/activity id (or the campaign+lead+date synthetic id) is already in `seen_activity_ids` — if so, it's a stale-snapshot false positive, not a real new event. Never repost; just refresh the stats snapshot silently and log the reconciliation.
