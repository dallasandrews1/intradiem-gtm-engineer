---
name: signal-researcher-agents-cannot-write
description: The signal-researcher agent type has no Write tool, so its files come back inside its final message; extract them from the transcript rather than re-typing
metadata:
  type: project
---

Sep 25 2026: three signal-researcher passes (BofA, Centene, TD) each ended "BLOCKED ON FILE WRITE" and returned both markdown files inline. The fix that worked: parse the agent's JSONL transcript in the tasks folder for the longest string, split on the FILE markers, write to disk with em dashes replaced. Script: scratchpad extract_research.py (three marker formats seen: fenced ```markdown blocks, "FILE n: name\n===" plain blocks, and "=== FILE n START ===\nFILENAME:" blocks).

**How to apply:** when a research pass must land on disk, either use a general-purpose agent with Write, or brief the researcher to end with the two files delimited by a fixed marker and extract. Never re-emit the content by hand.
