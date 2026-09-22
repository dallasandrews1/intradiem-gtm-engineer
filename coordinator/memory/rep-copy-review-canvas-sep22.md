---
name: rep-copy-review-canvas-sep22
description: "Sep 22 2026: a Slack canvas is the working way to hand a rep copy for review, since wrangler deploys are blocked in auto mode and a canvas needs none"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: eb7aa043-b846-44a2-9ee2-93981bef4bc7
  modified: 2026-09-22T18:04:13.708Z
---

Sep 22 2026, handing Nathan Belfield seven rendered Email 1s for the Stars relaunch. Dallas's usual pattern with Nate is a pages.dev link, the way the back-office and front-office map sets went over on Sep 4. That path needs a wrangler deploy, which the permission classifier refuses in auto mode ([[claude-code-auto-mode-blocks-deploys]]), so it costs Dallas a manual step before he can even send the note.

A standalone Slack canvas solves it: created through the Slack connector with no deploy, invisible to the rep until Dallas shares the link, and the rep can comment inline on individual emails. Canvas created: https://intradiem.slack.com/docs/T02FUS29E/F0C3HKH1ZBM

**Why:** Nate reviews copy item by item and answers per item ("The Insurance messaging is great IMO. Would not change that one. Hits the mark," Sep 4). A canvas matches how he already works and skips the deploy gate entirely.

**How to apply:** for rep-facing copy review, default to a canvas, not a page. Keep it seller-facing per [[feedback-seller-pages-no-fluff]]: what changes, what stays the same, the copy, the flags the rep needs, and the one question back. Leave out the research method, the claim lanes and the gates, which are Dallas's side of the work. Reserve pages.dev for things that need to live at a URL or be re-shared. A canvas is not a deployed page, so it does not go in the shared links manifest. Related: [[stars-relaunch-mined-lines-sep22]].
