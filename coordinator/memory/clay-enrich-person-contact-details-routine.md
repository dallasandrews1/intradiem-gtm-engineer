---
name: clay-enrich-person-contact-details-routine
description: "The reliable Clay path for committee contact detail: managed routine Enrich Person and Find Contact Details, LinkedIn URL in, work email + mobile out, ~8 credits per person"
metadata:
  type: reference
---

Confirmed working Sep 22 2026 on 21 people across two accounts, 21 of 21 complete.

```
clay routines runs start function:t_0thx4ojyQd6uNhDf44G --input items.json
clay routines runs get <routineRunId>
```

`items.json` is `{"items":[{"id":"<slug>","inputs":{"Social Profile URL":"<linkedin url>"}}]}`, 1 to 100 entries. Returns `Work Email`, `Mobile Phone`, and a full `Enrich person` block with title, dated experience history, education and summary. Roughly **8 credits per person**. Runs async, about 60 to 90 seconds for 13 rows. Encode `®` in a LinkedIn slug as `%C2%AE`.

Use this instead of hand-assembling contact detail. It gets the mobile, which Apollo's bulk_match does not without a separate phone reveal, and mobiles are what a cold-calling rep actually needs.

**Two traps.**
1. **The email waterfall can return a personal address.** It returned `@umich.edu` alumni addresses for two BCBSM directors. Always check the returned domain against the company domain before treating it as a work email; a wrong-but-deliverable address never bounces.
2. **A surname change may not have reached the mailbox.** Leilah Mack returns `leilah_krohn@vanguard.com`. Use what it returns; do not "correct" it to the current surname.

**What was NOT working that day:** `clay search query-mode run` returned HTTP 504 on every page across three separate searches, so the roster had to come from Apollo. `clay search query-mode create` worked; only the run/page leg failed. The Clay MCP `run_subroutine_direct` and `slack_create_canvas` also returned internal errors. The CLI routines path was the one that held.

Related: [[strikerooms-bcbsm-vanguard-sep22]], [[enrichment-doctrine-clay-not-lemlist]], [[clay-spend-posture-aggressive]]
