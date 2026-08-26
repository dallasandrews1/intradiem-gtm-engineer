---
name: verify-dont-theorize
description: "When something doesn't work, get ground truth from the tool/data/docs BEFORE proposing a fix. Never present hedged theories as answers. Verify in one pass, then deliver the confirmed cause + fix."
metadata:
  node_type: memory
  type: feedback
  originSessionId: 7c09b570-5dad-4007-8754-8157e967649b
  modified: 2026-07-20T16:01:58.612Z
---

Jul 20 2026: Dallas, frustrated after a long chain of me theorizing about why a Clay Invoke Workflow column only surfaced one input: "how do I get you to stop theorizing and finding the actual solutions moving forward? as a standard."

**The standard (permanent):**
1. When something doesn't work, find the GROUND-TRUTH mechanism before proposing a fix — via the actual tool output, live data, or the product's docs. Not inference, not "this is probably how it works."
2. Never present a hedged theory as if it's the answer. Words like "likely / almost certainly / probably / I suspect / it's cached" are a tell that I'm guessing. Either I've verified it, or I say plainly "I don't know yet, verifying" and go confirm.
3. Do the digging in ONE pass, silently (tools, docs, real data), then deliver the confirmed cause + the concrete fix. Don't narrate the maybe-X-maybe-Y out loud across multiple messages.
4. If a fact genuinely requires Dallas's screen or input, ask for that ONE specific thing, once — not an iterative chain of screenshot requests and partial fixes.

**Why:** theorizing out loud reads as flailing, wastes his time, and erodes trust that I actually know the answer. He wants the verified solution, not my reasoning process.

**How to apply:** the moment I catch myself writing a hedged causal claim, stop and go verify it (grep the dump, read the live resource, search the docs, run a test) before it reaches him. Especially for Clay UI mechanics — verify current docs (the click-by-click rule already says this). Pairs with [[always-confirm-live-clay]], [[click-by-click-ui-sheet-standard]], [[finish-what-we-start-no-checkbacks]].
