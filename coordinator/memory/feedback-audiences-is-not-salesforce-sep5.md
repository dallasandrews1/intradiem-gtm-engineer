---
name: feedback-audiences-is-not-salesforce-sep5
description: "Sep 5 2026 - never call a Clay Audiences upsert a \"write back\"; it reads as Salesforce writeback. Nothing in the workspace writes to Salesforce, and the enrich-to-lemlist chain is the whole purpose."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 574f852d-d5f3-4f7f-9b4e-74b72861ddc9
  modified: 2026-09-05T03:25:24.082Z
---

Dallas read the phrase "write back to Audiences" in the Sep 5 tech-stack UI sheet as Claude building Salesforce writeback, and pushed back: the purpose of the workflows is to enrich accounts and contacts alongside the tables, then push them into lemlist for outreach, nothing more.

Facts confirmed Sep 5: the workflow node `wfn_0tkv9yhGxkgZqn3vidR` in `wf_0tkv9u0BKvNYsV4NsQx` uses Clay's `upsert-audiences-record` action (package b1ab3d5d-b0db-4b30-9251-3f32d8b103c1), entityType ACCOUNT, lookup on domain. Audiences is Clay's own store, synced one way IN from Salesforce. No Salesforce write action exists anywhere in the workspace.

**Why:** "write back" is CRM vocabulary and makes a Clay-internal stamp sound like a CRM integration, which is scope Dallas has not asked for and which would need an SF user with API write access plus an ops-approved field schema.

**How to apply:** say "stamp the field on the Clay company record" or "onto the Audiences record", never "write back". When explaining why enrichment lands on the Audiences record rather than staying in a motion table, give the real reason: it is the credit cache and the segment layer, so one company read serves every motion and the lemlist bridge reads from the same place. Salesforce stamping stays a separate, unrequested ask. Related: [[lemlist-bridge-sep3]], [[audiences-known-layer-pattern-aug25]], [[clay-audiences-live-cli-capability-aug20]].
