#!/bin/zsh
# Unattended weekly Clay credit ledger check + reconciliation. Launched by com.dallasandrews.gtm.creditcheck (see ~/Library/LaunchAgents).
set -uo pipefail
cd "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"
export LATE_RETRY=1  # log-only job: safe to resume a late-crashed run (see lib/claude_net.sh)

TODAY="$(date +%Y-%m-%d)"
RECON="automation/logs/credit_reconciliation.log"

# --- deterministic anchor: capture the LIVE balance verbatim so it is never eyeballed or skipped ---
# clay lives in the plugin cache (version-pinned dir), so resolve it: PATH first, then newest cache version.
CLAY_BIN="$(command -v clay 2>/dev/null || ls -t /Users/dallasandrews/.claude/plugins/cache/clay-plugins/clay/*/bin/clay 2>/dev/null | head -1)"
{
  echo "===== ${TODAY} ====="
  echo "clay credits (live, authoritative):"
  "${CLAY_BIN:-clay}" credits 2>&1
} >> "${RECON}" 2>&1 || echo "[${TODAY}] clay credits UNREACHABLE" >> "${RECON}"

"/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/claude_net.sh" --model claude-sonnet-5 -p "$(cat <<'PROMPT'
/clay-credit-steward

Unattended weekly credit reconciliation ahead of Friday's readout. Ground rules for this run only:
- Read-only. Do not run enrichment, do not spend credits, do not modify any ledger file. Reconcile and report only; Dallas merges ledger updates himself.
- Message nobody. The daily rundown reads your log.
- ANCHOR on the live balance: the authoritative current balance is the most recent "clay credits (live)" capture in automation/logs/credit_reconciliation.log (captured deterministically just now, in the file's latest dated block). Use THAT number as truth, not any ledger figure. Budget framing: the original ~72K was the ONE-TIME proof budget, and on 2026-07-31 Clay's product lead topped the account up with ~12K additional credits (confirmed by Dallas 2026-08-03, see that date's entry in credit_reconciliation.log). Keep the two separate: % consumed is computed against total credits made available (original budget + top-up), but the renewal receipts story stays anchored on the original purchased proof budget. The old "5,000 monthly allocation" framing is stale, do not use it, and do not treat the balance as monthly-refreshing.
- Reconcile the live balance against the last recorded balance in all THREE ledger files: Clay_Credit_Ledger.md (canonical, meter-verified history), clay_credit_ledger.csv, and "../Clay Builds and Strategy/Clay_Credit_Ledger.md" (a known duplicate that should NOT diverge). Compute drift = live minus each ledger's last number. Flag any drift over ~50 credits, and flag LOUDLY if the duplicate ledger disagrees with the canonical one.
- Figure out today's date, then write to automation/logs/credit-check-<todays-date>.md: the ONE reconciled number (live balance = truth), consumed-to-date and % of total credits made available (original ~72K budget + the Jul 31 ~12K top-up), drift vs each ledger with which file needs Dallas to sync, burn by motion, and cost-per-qualified-reply. If everything agrees, say "no drift, all three ledgers agree with live" in one line so silence never hides a problem.
PROMPT
)
$(cat "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/log_resilience.txt")" --dangerously-skip-permissions >> "automation/logs/_run_credit_check.out" 2>&1
