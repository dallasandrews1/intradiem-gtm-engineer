---
name: motionstatus-not-a-lemlist-gate-sep4
description: Sep 4 2026 - the Clay-stamped motionStatus variable (held / staged / sf_stale) is NOT a lemlist send gate; lemlist readiness returns ready with those leads loaded, so flagged rows must be pulled by hand before a campaign starts
metadata:
  type: project
---

Found by the Sep 4 2026 pre-send integrity sweep on the five BO campaigns (log `automation/logs/lemlist-integrity-2026-09-04.md`). `motionStatus` is a custom variable the Clay bridge writes; lemlist does not read it, and `validate_campaign_readiness` said ready for campaigns holding `sf_stale` and `held` leads. Two wrong-company leads (a Barclays mailbox tagged Wells Fargo in FS, a Freedom Mortgage mailbox tagged Truist in Net-New) were already stamped `sf_stale` and would still have sent. Karoline Kane was removed via the allow-listed helper Sep 4; Joel Davis's removal was blocked by the classifier and handed to Dallas.

**Why:** the Patrick Savage pattern repeats whenever a Salesforce address is trusted over a live person match, and no downstream gate catches it.

**How to apply:** before any campaign starts, list leads whose motionStatus is not in_sequence and pull or fix them by hand; treat a stale-stamped lead as a wrong-company lead until proven otherwise. Longer fix: have the bridge skip lemlist entirely for anything not `staged` or `in_sequence`. See [[lemlist-linkedin-backfill-pattern-aug31]].
