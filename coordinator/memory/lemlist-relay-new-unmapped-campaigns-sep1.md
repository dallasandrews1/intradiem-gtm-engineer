---
name: lemlist-relay-new-unmapped-campaigns-sep1
description: "Sep 1 2026 — two more Jack campaigns (Achmea, LV=) are missing from campaign_channel_map; a real emailsBounced event on LV= went unroutable"
metadata: 
  node_type: memory
  type: project
  originSessionId: 4e097bbf-7c95-4bb7-b16e-c5b78cd53e64
  modified: 2026-09-01T09:13:34.122Z
---

As of the 2026-09-01 hourly relay runs, two campaigns are live and sending but absent from `campaign_channel_map` in `automation/config/lemlist_channels.json`:
- `cam_et6gRwgXgjeeYQg4B` — "THE Achmea contact" (Jack Ohagan), first spotted 02:11 CDT (non-actionable events only so far).
- `cam_7NXbM7HgYtRvMtodm` — "THE LV= Contact" (Jack Ohagan), spotted 04:12 CDT — this one already produced a real `emailsBounced` (Phil Coole, LV=) that the relay could not route anywhere per the never-post-to-an-unlisted-channel rule. The bounce is sitting logged but invisible; list hygiene on it hasn't happened.

**Why:** same failure mode as [[lemlist-relay-campaign-map-gap-aug7]] (resolved Aug 20 for the Hartford/Citizens pair) — new campaigns Jack builds aren't getting added to the map at build time, so the relay silently drops their events to the log instead of a rep channel until someone notices.

**How to apply:** next time this file is touched, add both campaign ids to `campaign_channel_map` routed to `jack`, and have Jack check Phil Coole's bounce for list hygiene. Worth floating to whoever builds new motions: add the campaign_channel_map entry as part of campaign creation, not after the relay catches the gap.
