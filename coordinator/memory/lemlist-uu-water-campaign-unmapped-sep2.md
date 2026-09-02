---
name: lemlist-uu-water-campaign-unmapped-sep2
description: "New lemlist campaign cam_wPHsdosLdeT5t5Kct (UU Water / United Utilities, Jack's) is missing from campaign_channel_map as of 2026-09-02, same recurring gap pattern as lemlist-relay-campaign-map-gap-aug7"
metadata: 
  node_type: memory
  type: project
  originSessionId: 7cf4d204-2c76-46d1-ac71-e44fbd82eb72
  modified: 2026-09-02T17:12:57.011Z
---

As of the 2026-09-02 11:54 CDT hourly lemlist-relay run, campaign `cam_wPHsdosLdeT5t5Kct` ("UU Water", United Utilities, sent by Jack Ohagan per activity records) is live and generating activity (`conditionChosen` events on 5 leads: Dean Cunningham, Mike Gauterin, Stephanie Linforth, Lisa Young, Andrea Burke) but has no entry in `campaign_channel_map` in `automation/config/lemlist_channels.json`. No harm yet — `conditionChosen` isn't an actionable event type the relay routes — but if this campaign starts producing replies, bounces, or LinkedIn accepts, those will silently drop to the log instead of reaching Jack's channel, same failure mode as [[lemlist-relay-campaign-map-gap-aug7]].

**Why:** campaign_channel_map is populated by hand at campaign-build time and keeps drifting behind new campaign launches — this is the second time in a month a live campaign shipped without a map entry.

**How to apply:** add `"cam_wPHsdosLdeT5t5Kct": "jack"` to campaign_channel_map next time this file is touched. Worth flagging to Dallas as a process gap: consider wiring campaign_channel_map updates into whatever step launches a new lemlist campaign, so this stops recurring.
