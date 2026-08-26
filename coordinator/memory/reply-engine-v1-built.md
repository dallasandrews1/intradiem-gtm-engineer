---
name: reply-engine-v1-built
description: "Reply Engine v1 built Jul 13-14: classifies inbound replies into 7 categories and drafts a reframe response in Nathan's voice, never sends; claiming a reply is the real-world use of the Norton-demo collision gate"
metadata:
  node_type: memory
  type: project
  originSessionId: catchup-jul17-2026
---

`reply-engine/` (README.md + SOP_Reply_Handling.md, Jul 13-14) is a Python tool that classifies an inbound prospect reply into 7 categories mirrored from [[intradiem-objection-handler]] (Bad Timing, We Have WFM, Built In-House RPA, Evaluating Competitor, No Budget, Send Info, Wait for October) and drafts a reframe response in Nathan's voice. It never sends — sending stays with Nathan after a copy-sharpener pass.

Load-bearing mechanical detail: claiming a replied row (`bdr_claimed = TRUE` in Clay Contacts) is what the live `send_ready` formula (`critic PASS && human_approved && !bdr_claimed`) uses to instantly drop a row from READY to HOLD — the same collision-gate mechanism built for the Norton demo is now doing real production work. Applies across every motion (Stars, back-office, install-base); config lives in `config/reply_categories.json` (config over code).
