---
name: lemlist-campaigns-stats-batch-limit-sep22
description: "mcp__claude_ai_lemlist__get_campaigns_stats errors on large campaignIds batches (~20) with a proxy \"Invalid content from server\" error; batches of 8 or fewer work reliably"
metadata: 
  node_type: memory
  type: project
  originSessionId: 42e015cc-90ae-4b94-8c5c-f09e870995f6
  modified: 2026-09-22T07:14:11.716Z
---

Observed 2026-09-22 during a scheduled lemlist-relay run: calling `get_campaigns_stats` with the full 39-campaign `campaignIds` list (and a 20-campaign sub-batch) failed with `Streamable HTTP error: ... "Anthropic Proxy: Invalid content from server"`. A single-campaign call succeeded immediately, and batches of 8 campaigns each also succeeded cleanly (39 campaigns split into 1+8+8+8+8+7).

**Why:** the tool's declared `maxItems` is 100, but the response payload for ~20+ campaigns (each with full leadMetrics/messageMetrics/perChannel/steps detail) appears to exceed something the Anthropic proxy will pass through, causing a hard error rather than a partial/truncated response.

**How to apply:** for the lemlist-relay hourly job (or any other caller of this tool covering the full 39-campaign `campaign_channel_map`), batch `campaignIds` into groups of ~8 rather than sending the full list in one call. This avoids the error entirely and costs a few extra round-trips, not a redesign. Related: [[mem0-search-quota-exhausted-sep22]] was hit the same run, unrelated cause.
