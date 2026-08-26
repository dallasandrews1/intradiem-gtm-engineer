---
name: lemlist-relay-session-tools-absent-aug19
description: "One hourly lemlist relay run on 2026-08-19 (18th run of the day) had neither the lemlist MCP tools nor any Slack tool loaded, unlike all 17 prior runs that day — a session-level gap distinct from the standing Aug 15 plan-gate issue"
metadata: 
  node_type: memory
  type: project
  originSessionId: 5e4e40c2-a57a-44ad-82c2-c998c9e199b5
  modified: 2026-08-20T01:20:26.749Z
---

On 2026-08-19, the 18th hourly run of the `lemlist-to-Slack relay` job (see [[lemlist-relay-campaign-map-gap-aug7]] for the job's shape) found neither the lemlist MCP tools (`get_inbox_conversations`, `get_campaigns_stats`) nor any Slack tool available via ToolSearch, after three separate query attempts. Every other run that day (17 of them) had both surfaces working normally. This is separate from the standing lemlist plan-gate issue (REST `/api/activities` gated since Aug 13, MCP-first fallback built Aug 15, evt: swarm-2026-08-15#relay-mcp-first) — that gate blocks lemlist REST specifically; this gap blocked lemlist MCP AND Slack MCP simultaneously, which the runbook doesn't anticipate (it only has a documented fallback for the lemlist side).

Practical effect: campaign-stats snapshot (`.lemlist-relay-stats.json`) could not be refreshed and was left at its last real value; Step 7 thread ingest could not read either rep channel at all, so that hour is an unconfirmed coverage gap rather than a confirmed-empty check. Logged to `automation/logs/lemlist-relay-2026-08-19.md` (evt: lemlist-relay-2026-08-19#session-tools-absent) and `automation/logs/brief-thread-ingest-2026-08-19.md`.

**Why this matters:** it happened once, so it may be a transient session/ToolSearch hiccup rather than a real outage — but if it recurs on a future run, the relay is fully blind that hour (not just plan-gated), and that's worth surfacing to Dallas directly rather than letting it blend into the routine "no new events" pattern.

**How to apply:** if a future lemlist-relay run also finds both surfaces absent, treat it as a pattern (not a fluke) and flag it prominently rather than logging it as another routine "blocked" entry — check whether it correlates with anything (time of day, other jobs also missing tools) similar to how [[swarm-blackout-fixed-guarded-shim-aug15]] was root-caused.
