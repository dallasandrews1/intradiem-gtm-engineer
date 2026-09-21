---
name: heat-lane-a-clay-workflow-unconnected
description: Heat list Lane A cannot post to Slack until Dallas connects Slack and lemlist accounts on the Clay workflow and publishes it; webhook 2xx is not proof of a post
metadata:
  type: project
---

On 2026-09-21 Dallas gave the explicit go (Nate approved the format) to turn on heat list Lane A. One live run POSTed centene.com and maximus.com to the Clay webhook, got 2xx, and NOTHING reached #gtm-outbound-nathan (C0BM9V6KGSG). Clay workflow `wf_0tkbgk02Xub84UtnRXS` (Heat Lane A) has `authAccountId: null` on both the Slack approval node and the lemlist add-lead node, and zero runs since it was built Aug 25. `cohort.lemlist_campaign_ids` is also empty for both reps, so Approve has no campaign to push into.

State left: `dry_run=true`, `live_lane_a=true`, `live_stamp=false`, `lane_a_live_reps=["nathan"]` in `automation/config/heat_loop.json`, so flipping `dry_run` alone turns it on. False `alerted` entries were removed.

**Why:** a Clay webhook source accepts a payload even when the workflow behind it can't run. The only proof of a Lane A post is reading the Slack channel.

**How to apply:** needs Dallas's hands in Clay (connect Slack on node 1, lemlist on node 2, publish), then set a per-rep campaign id, then flip `dry_run`, then read the channel. Same session added: review-flag holds, tool-domain exclusion, TLD rep routing (.nl/.uk/.ie to Jack), lemlist unsubscribe suppression on suggested names (Drex Fitzwater at Maximus was being suggested after unsubscribing Sep 11). Related: [[pipeline-council-oct8-doubling-ask]].
