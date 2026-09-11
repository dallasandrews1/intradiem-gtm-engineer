#!/bin/zsh
# rep-campaign-hook: pre-send hook for rep-built lemlist campaigns (built Sep 4 2026 after
# Jack's hand-loaded ST Water campaign bounced 4 of 6). Runs hourly at :25, after the relay (:10).
#
# Step 1 (python, deterministic): discover campaign ids not in the relay map, add them to the
#   map routed by sender, check every lead for a Clay Audiences record, write the DRY-RUN
#   credit estimate for the Work Email + ZeroBounce workflow, stage the inputs. Never runs it.
# Step 2 (Claude, only when step 1 found something): lemlist-lead-integrity sweep on the new
#   campaign(s) plus the free Clay bridge (0 credits) on the no-record leads, appended to the
#   same dated log. Read-only: no lead edits, no campaign state changes, no workflow runs.
#
# Silence on empty: no new campaign means no Claude session and no dated log; the quiet line
# lands in _run_rep_campaign_hook.out only. Never DMs anyone; the daily rundown reads the log.
set -uo pipefail
cd "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"
export LATE_RETRY=1  # log-only job: safe to resume a late-crashed run (see lib/claude_net.sh)
export GUARD_JOB="run_rep_campaign_hook.sh"
OUT="automation/logs/_run_rep_campaign_hook.out"
HANDOFF="automation/staging/rep_hook/_handoff.txt"
PY_ARGS=("$@")   # pass-through: --campaign cam_x (on demand), --no-map-write, --no-clay

STEP1="$(python3 automation/rep_campaign_hook.py "${PY_ARGS[@]}" 2>>"$OUT")"
rc=$?
print -r -- "[$(date '+%Y-%m-%d %H:%M:%S')] step1 rc=${rc} ${STEP1}" >> "$OUT"

if [[ $rc -ne 0 ]]; then
  print -r -- "[$(date '+%Y-%m-%d %H:%M:%S')] step1 FAILED rc=${rc}; step 2 not launched. New rep campaigns are UNWATCHED this run." >> "$OUT"
  exit $rc
fi

# Step 1 writes the handoff itself (id|name|rep|staged|evt per line) and truncates it every run,
# so the shell never parses JSON. A quoting bug here used to turn a real finding into a silent
# "nothing new", which is the exact invisible failure this whole hook exists to prevent.
if [[ ! -s "$HANDOFF" ]]; then
  exit 0
fi
NEW_IDS="$(tr '\n' ' ' < "$HANDOFF")"

"/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/claude_net.sh" --model claude-sonnet-5 -p "$(cat <<PROMPT
Unattended scheduled run: rep-campaign-hook step 2. Nobody is watching live.

Step 1 (automation/rep_campaign_hook.py) just discovered these lemlist campaigns that were built outside the engine (by a rep, by hand) and wrote their discovery, relay-map, Clay-record and DRY-RUN credit-estimate sections to automation/logs/rep-campaign-hook-<today>.md. Each entry is id|name|rep|staged-inputs-file|evt:
${NEW_IDS}

Do exactly this, appending to that same dated log file (figure out today's date yourself; never create a second log):

1. INTEGRITY SWEEP. Follow the lemlist-lead-integrity agent definition at /Users/dallasandrews/.claude/agents/lemlist-lead-integrity.md exactly, scoped to ONLY the campaign ids above. Append a "## Integrity sweep (step 2)" section per campaign with the PASS / FLAG / UNVERIFIED verdict, exact lead ids, stored vs expected values, and a "chain:" line citing that campaign's evt id from step 1. Pay particular attention to email pattern drift inside one domain (reversed name order, collapsed hyphens, a .com where colleagues are .co.uk), TEST rows, unrendered {{variables}} (preview at least one real lead per email step), and leads at the wrong company for the campaign. If the lemlist MCP tools are not available in this session, fall back to curl with the API key in automation/config/lemlist.env (export: GET https://api.lemlist.com/api/campaigns/{id}/export/leads?state=all&format=json; sequences: GET /api/campaigns/{id}/sequences).

2. FREE BRIDGE (0 credits) on the no-record leads. For every campaign with a staged-inputs file (the 4th field, not "-"), read that JSONL and run ToolSearch with query "select:mcp__claude_ai_Clay__find-and-enrich-list-of-contacts". If it loads: call it with contactName = full_name and companyIdentifier = company_domain for the rows (max 20 per call, NO dataPoints, that is what keeps it free) and append a "## Free bridge (step 2)" table per campaign: lead, found or not found, current company and title returned, LinkedIn URL returned, and a one-word read (current / moved / not found). A lead whose returned company differs from the campaign's account is a stop-the-line flag. If the tool does NOT load, append one line: "BRIDGE UNAVAILABLE headless this run; run attended with the paste-back line in step 1." Never request data points, never call any enrich, workflow, or routine.

3. Close with a "## Next action" block per campaign: exactly what Dallas or the rep should do before this campaign sends (remove TEST rows, verify N addresses attended via the paste-back line, fix a placeholder, nothing needed). Keep it to the facts.

Hard rules for this run: read-only everywhere. Never run wf_0tk4jo5z7RjGKo3rvR8 or any Clay workflow, routine, or enrichment. Never edit, add, remove, pause, or resume a lead, step, or campaign. Never post to Slack, never DM anyone (the daily rundown reads this log). Do not modify any file except automation/logs/rep-campaign-hook-<today>.md. No em dashes in anything you write. Mint no new evt ids; cite the step-1 ones with chain:.
PROMPT
)
$(cat "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/log_resilience.txt")" --dangerously-skip-permissions >> "$OUT" 2>&1
