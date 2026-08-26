---
name: lemlist-relay-campaign-map-gap-aug7
description: "RESOLVED 2026-08-20 — campaign_channel_map gap for the two Hartford/Citizens campaigns is closed; both route to nathan"
metadata: 
  node_type: memory
  type: project
  originSessionId: 252ca487-00b8-4542-8bc2-8b601e67da10
  modified: 2026-08-20T15:15:33.814Z
---

RESOLVED as of the 2026-08-20 10:13 CDT relay run: `campaign_channel_map` in `automation/config/lemlist_channels.json` now has entries for both `cam_fYp7Nh9wB72gfMke6` (Blitz - The Hartford, Nate) and `cam_yWefPqaDhNNv4RyQK` (Blitz - Citizens, Nate), both routed to `nathan`. Also confirmed the config is out of canary mode — `live=true` with real channel ids (`nathan` → C0BM9V6KGSG, `jack` → C0BN0JT9D6U), not the old #relay-test placeholder. Original gap description below for history.

`automation/config/lemlist_channels.json`'s `campaign_channel_map` has no entry for `cam_fYp7Nh9wB72gfMke6` (Blitz - The Hartford, Nate) or `cam_yWefPqaDhNNv4RyQK` (Blitz - Citizens, Nate). Both campaigns are actively sending (confirmed live activity through Aug 7). On 2026-08-07 15:12:54 CDT the hourly lemlist-to-Slack relay job caught an `emailsBounced` event on the Hartford campaign (lead Dakota Pelletier) that it could not route to any Slack channel because the campaign isn't a key in the map — the bounce sat logged but invisible, and list hygiene on it hasn't happened. As of the 17:12:59 CDT run the gap is still unresolved.

**Why:** the relay's hard rule is never to invent a routing target or post to an unlisted channel — only `campaign_channel_map` entries are valid routing keys, so a missing entry means silent drop-to-log instead of misdelivery. That's the safe failure mode, but it means bounces/replies/etc. on these two campaigns won't reach a rep same-day until the map is fixed.

**How to apply:** add both campaign ids to `campaign_channel_map` (routed to whichever rep owns Hartford/Citizens — Nate, per the campaign names) next time this file is touched. Also worth noting: the config is currently in CANARY MODE (`live=true` but both `nathan` and `jack` routes point at Dallas's private #relay-test channel C0BM86CV138, not real rep channels — see the `note` field and `rep_channels_at_launch` in the same file) — restore real channel ids from `rep_channels_at_launch` at the same time as fixing the campaign map, since both are pre-launch cleanup items on this one file.
