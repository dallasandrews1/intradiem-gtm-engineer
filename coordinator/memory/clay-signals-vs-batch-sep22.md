---
name: clay-signals-vs-batch-sep22
description: Clay Audiences Signals are UI-only on this build (no CLI/API); audience_signal triggers need a pre-existing sig_ id. Batch pull and native signal are complementary, not alternatives
metadata:
  type: project
---

Sep 22 2026. Dallas asked how the hand-built exec-hire workflow differs from using Clay's own Signals section. Verified answer: the workflow is a PULL, a batch snapshot over a domain list. A signal is a PUSH, Clay watching and firing on change.

**They are complementary and both are needed.** A signal only reports changes from the day it is switched on, so it would never have surfaced the 9 accounts whose leader arrived up to twelve months ago. The batch is the backfill and the re-run tool; the signal keeps it current.

**Signals have NO CLI or API surface on this build.** `clay --help` has no signals command, and the audiences skill states signal commands exist only in an experimental CLI, otherwise use the Clay app. The `audience_signal` workflow trigger requires `signalId` (a `sig_...`) plus `entityType`, and that id must already exist. So creating a signal is always UI work here.

Valid workflow trigger types in this workspace: `manual`, `webhook`, `audience_segment`, `audience_scheduled`, `audience_signal`, `scheduled`, `clay_table`, `csv_upload`, `action_source_scheduled`.

**Built to the edge of what the CLI allows:** company field `audf_0tlsbdrbpahu6VJmYoJ` "Signal Watch"; upsert workflow `wf_0tlsbeggeEMV5A2Jht3` which stamped all 72 Stars domains (only 16 already existed as company records, 56 were created); audience `audseg_0tlsbjxHmH2259r5rHx` "Signal Watch: Stars scored accounts". UI sheet at `motions/shared/polar_sheets/Clay_Sheet_Stars_NewHire_Signal_Sep22.md`, registered in polar_tasks.json as `stars-newhire-signal`.

**Precedent that already existed:** audience `audseg_0tkbpyip5Kkvyok7wdd` "JC Watch: customer WFM leaders with LinkedIn (test roster)" is a staged job-change roster on the CUSTOMER side, never switched on. The new one is its prospect-side counterpart.

**upsert-audiences-record field shape** (copied from the Heat Stamp node `wf_0tkbgk0UytzkPQWmakX`, not guessed): keys are PIPE-DELIMITED, not nested objects. `lookupFields|selectedLookupFields` static array, `lookupFields|domain` reference, `recordFields|selectedRecordFields` static array of field ids, one `recordFields|<fieldId>` per value, plus `recordFields|removeNullValues`.

**Defect found:** Audiences holds 76 company records for 72 distinct domains. caloptima.org 2, chpw.org 3, essencehealthcare.com 2. Pre-existing duplicates; a signal firing on one could double-count.

**polar_tasks.json gotcha:** `tasks` is a DICT keyed by task slug, not a list. An `.append` silently no-ops. Related: [[clay-exec-hire-signal-sep22]], [[signal-scoring-model-sep22]].
