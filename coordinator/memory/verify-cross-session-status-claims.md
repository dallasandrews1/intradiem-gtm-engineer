---
name: verify-cross-session-status-claims
description: "FEEDBACK: when a different session/tool hands off a status claim (e.g. a Cowork reconciliation prompt saying a system is 'proven end-to-end'), verify it against direct evidence before treating it as ground truth"
metadata:
  node_type: memory
  type: feedback
  originSessionId: catchup-jul17-2026
---

On 2026-07-17 night, a parallel Cowork session (running the golden-scaffold clone/stamp work in a separate browser tab) produced a handoff prompt asserting "the golden-scaffold clone-and-stamp system is PROVEN end-to-end." A VS Code Claude Code session working the same motion at the same time had direct, first-hand contradicting evidence: the sourcing/company-import step was actively broken (bulk company search returning duplicates for some domains and zero results for others, confirmed by testing Clay's raw search API directly), and the credit-gated sample that would have proven the signal-research formulas against real data had never run. Dallas was about to paste the other session's summary into a third session as ground truth.

**Why this matters:** sessions that haven't witnessed the same work firsthand tend to summarize optimistically or go stale, especially under a deadline. A status claim from one session ("X is proven/done/working") is not verified just because it reads confidently — it's a claim like any other, and it can directly contradict what another session watched happen in real time.

**How to apply:** before treating a handoff prompt, another session's summary, or a "here's what exists" status block as ground truth to build on, check it against direct evidence you actually have (memory of what you watched happen, live tool state, direct verification) rather than passing it through unchecked. If it contradicts what you know firsthand, say so plainly before the user acts on it — don't let a rosier secondhand claim override eyewitness reality. Ties to [[wfm-adjacency-and-belfield-continuation]] for the specific incident.
