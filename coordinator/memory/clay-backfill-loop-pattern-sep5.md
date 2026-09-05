---
name: clay-backfill-loop-pattern-sep5
description: Sep 5 2026 - the reusable pattern for draining a Clay Audiences segment through a workflow in 10-row batches, and the three guards each failure taught
metadata:
  type: reference
---

`clay workflows runs test <wf> --audience-segment <seg> --limit N` caps N at **10**, so any backfill is a batched loop. Runner: `tam-outbound-engine/cc_platform_backfill.sh` (parameterize WF/SEG to reuse). Three guards, each earned on a failed run:

1. **Retry the kick.** Clay returns transient `server_error: Failed to generate latest snapshot: Unexpected token '<'` (an HTML error page where JSON was expected). Aborting on it killed run 1 at batch 84 of 176. Retry 6x with doubling backoff.
2. **Wait for the batch to SETTLE before the next kick.** Kicking as soon as the count moves at all re-sends rows still in flight, because read status has not been written yet so they are still segment members. Cost ~10% in duplicate reads (906 credits for 818 rows). Settle = full batch drained, or count stable across 3 consecutive polls. After the fix: 315 credits for 310 rows.
3. **A quiet batch is not fatal.** Clay's dispatch slows badly under sustained load: batches ran 22s early, 84-105s by batch 80, and one landed its runs **6 minutes** after the kick. A 5-minute stall limit aborted run 2 about a minute before the work arrived. Give each batch ~13 min and only stop after 3 consecutive zero-progress batches.

**Also:** a workflow whose first node can hard-fail (bad input) leaves the row un-stamped and therefore permanently in the queue, so the drain-based loop can deadlock at the tail. Put the status write on the failure path. Verify a run with `clay workflows runs get <wf> <run> --verbose` to see per-node inputs/outputs. Segment filters reference built-in fields the same way as custom ones: `dataPath: ["account_entity_field_values","field","normalized_domain"]`, not `["normalized_domain"]`.
