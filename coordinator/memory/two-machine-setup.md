---
name: two-machine-setup
description: "Dallas runs the scheduled swarm on his personal Max laptop for usage headroom; this enterprise machine is for interactive work, be usage/credit-conscious here"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4e012640-7a78-497b-94f5-caa1a5b90cad
  modified: 2026-08-06T15:14:13.231Z
---

Confirmed by Dallas Aug 6 2026. Dallas operates across two machines:

- **Personal Max laptop:** runs the scheduled automation swarm (daily rundown, war room, deliverability watch, credit check, gate integrity, meeting capture, etc.). He runs it there because his personal Claude Max account has much higher usage limits than the enterprise account. This is deliberate, to avoid burning enterprise Claude usage on the recurring agent runs.
- **This enterprise machine** (`/Users/dallasandrews`, project at `~/Claude/Projects/Intradiem GTM Engineer`): interactive / strategy work. Holds a MIGRATED SNAPSHOT of the project; its `automation/logs` stop 2026-07-20 and no `gtm` launchd jobs are installed here (verified: nothing in `~/Library/LaunchAgents`, none in launchctl). This is NOT a bug and NOT dark; the live swarm lives on the personal laptop.

**How to apply:**
- Do NOT propose installing, loading, or duplicating the launchd swarm on this enterprise machine. That would double-run jobs and burn enterprise usage. If a session flags "the swarm is dark," it is only looking at this snapshot machine.
- Be usage-conscious on this machine: don't spawn unnecessary background agents or heavy runs just because it's convenient here. Reserve heavy recurring/agent work for the personal-laptop swarm.
- Dated rows sourced from THIS machine's logs are stale snapshots, not live state. For live swarm output, the source of truth is the personal laptop (and Mem0 / the coordinator memory that syncs between them).
- Reading the live Clay credit balance (`clay credits`) is read-only and does not burn Clay credits; that number (Intradiem's shared Clay workspace) is valid from either machine.

Related: [[initiatives-board]], the repo CLAUDE.md Mem0 sync discipline note (coordinator memory + Mem0 keep the two machines consistent).
