---
name: proposal-queue-zero-rule
description: "Aug 6 2026 - proposals are BUILT or KILLED, never \"queued\"; fold into jobs that already fire rather than creating new ones nobody loads"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: d3b88697-23fb-4296-865e-5eaecdcf9851
  modified: 2026-08-06T21:24:36.188Z
---

Dallas: "makes no sense to have queued proposals if they end up just sitting stale in a table." The ~30-item proposal queue was closed to zero on Aug 6 2026: 10 proposals built (all folded into agents/scripts that already run), 9 killed with reasons.

**Why:** the queue was a symptom, not a backlog. Every agent-architect run since Jul 21 throttled its own proposing because the queue was deep, while nothing drained the other end. One item (the `run_credit_check.sh` clay path fix) had been done for two weeks and nobody closed it. Five separate proposals described the same failure class from different angles. Meanwhile `tablehygiene` never ran for three days because of a missing execute bit, and every one of those five proposed watchers would have caught it, but none were built.

**How to apply, three standing rules:**
1. A proposal is BUILT or KILLED. There is no "queued." If it's worth keeping, fold it into something that already runs; if nobody will fold it in, it wasn't worth the slot.
2. Prefer extending a job that already fires over creating a new one that has to be loaded. New jobs are another thing that can silently not run.
3. The architect may not open a new proposal in a class where an unbuilt one already exists; it appends evidence to the open item instead.

**Two judgment calls worth reusing:** killing the `log_sanitization` flip because the flag has no implementation behind it (flipping it would make preflight report READY while logs still leak PII, worse than an honest warning), and killing retroactive `credit-draw-attribution` in favour of writing a ledger line at the time each run happens. Both are cases where the proposed work would have produced a false signal rather than a true one.

Related: [[enrichment-doctrine-clay-not-lemlist]]
