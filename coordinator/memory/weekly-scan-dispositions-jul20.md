---
name: weekly-scan-dispositions-jul20
description: Dispositions on the Jul 20 weekly automation-scan top 3 (Stars clone HELD, credit reconciliation BUILT, war-room auto-merge pending Dallas's gate choice)
metadata:
  type: project
---

The Jul 20 morning DM (weekly automation scan) proposed 3. Dallas said action on them. Dispositions after grounding each against live state:

1. **Clone Send-Readiness onto Stars — HELD, do not action as written.** Two stale/wrong premises: (a) a Stars send-readiness workflow ALREADY exists — "Star Ratings 5-Touch Send-Readiness (Alpha)" `wf_0tiegzuo3PzJ4UtUGFA` (built Jul 19); the proposal's "no workflow yet" is stale. (b) The WFM 57-node workflow it calls "proven" is NOT proven — mid-fix on its trigger Inputs (the 16-key `$.customer_flag undefined` bug, see [[wfm-sendready-runbook-jul20]]). Cloning now clones the broken trigger wiring. Same "claimed proven when firsthand evidence says otherwise" pattern as [[verify-cross-session-status-claims]]. CORRECTED PLAN: prove WFM first (6 contacts run clean), then apply the same 16-key Inputs mapping + Stars MessageGen prompt to the EXISTING Stars workflow. Verify-and-fix, not a half-day clone.

2. **Credit ledger auto-reconciliation — BUILT Jul 20.** Extended `run_credit_check.sh`: a deterministic pre-step captures live `clay credits` verbatim into `automation/logs/credit_reconciliation.log` (append-only history) so the number is never eyeballed or skipped; the clay-credit-steward step then anchors on that live number as truth and diffs all THREE ledger files (canonical Clay_Credit_Ledger.md, clay_credit_ledger.csv, and the Clay Builds and Strategy duplicate), flags drift >~50 and any duplicate-ledger disagreement, writes ONE reconciled number. Also killed the stale "5,000 allocation" framing (real = ~72K proof budget). In-place edit to the already-loaded creditcheck job → no reload; effect next Thursday 7:00. Note: there are THREE ledger files, not two — the Clay Builds and Strategy duplicate is the known-problem parallel ([[clay-builds-strategy-duplicate-ledger-jul17]]).

3. **Auto-merge staged war-room signals — PENDING Dallas's gate choice.** staged_signals.csv → StarRatings_Earnings_Signals_2026.csv is a deliberate human review gate. Offered 3: auto-merge+audit (recommended), dedupe-only, full-auto-silent (steer off). Build against war-room-fanout.js once Dallas picks. Low real risk (signals affect scoring/targeting not sends; Nathan reviews all sends) but it's his live pipeline.
