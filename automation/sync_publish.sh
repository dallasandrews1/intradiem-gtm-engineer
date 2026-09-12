#!/bin/bash
# sync_publish.sh : personal-Mac publisher for the two-machine loop. Pure git + sync.sh, no Claude call.
#
# Runs at the end of every Claude Code session (SessionEnd hook in ~/.claude/settings.json) and
# nightly at 21:30 (com.dallasandrews.gtm.syncpublish) as a backstop. Does, in order:
#   1. coordinator/sync.sh export   (snapshot skills, agents, workflows, memory into coordinator/)
#   2. commit coordinator/ if anything beyond manifest.json changed
#   3. fast-forward from origin if it moved; rebase only when the tree is clean; never force
#   4. push main if it is ahead
#   5. report work that is NOT committed (main checkout + every worktree) to
#      automation/logs/sync-publish-<date>.md so the daily rundown surfaces "unpushed work"
#
# Guardrails: only touches coordinator/ with git add; never `git add -A` on the repo (other
# sessions' half-finished edits stay theirs); never resolves a conflict; exits 0 always so a
# session close is never blocked. Throttled to one run per 10 minutes unless --force.
set -uo pipefail

ENGINE="/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"
LOGDIR="$ENGINE/automation/logs"
STAMP="$LOGDIR/.sync-publish-last"
LOCK="$LOGDIR/.sync-publish.lock"
TODAY=$(date +%Y-%m-%d)
NOW=$(date +%H:%M)
LOG="$LOGDIR/sync-publish-$TODAY.md"
FORCE=0; HOOK=0
for a in "$@"; do case "$a" in --force) FORCE=1;; --hook) HOOK=1;; esac; done
# stdin (hook JSON) is intentionally not read: reading it blocks when stdin is a terminal

mkdir -p "$LOGDIR"
[ -f "$LOG" ] || printf '# sync-publish %s\n\n' "$TODAY" > "$LOG"
say() { printf '%s\n' "$*" >> "$LOG"; }

# throttle (hooks fire for every session, including the swarm's headless ones)
if [ $FORCE -eq 0 ] && [ -f "$STAMP" ]; then
  last=$(cat "$STAMP" 2>/dev/null || echo 0); nowsec=$(date +%s)
  if [ $((nowsec - last)) -lt 600 ]; then exit 0; fi
fi
if ! mkdir "$LOCK" 2>/dev/null; then exit 0; fi
trap 'rmdir "$LOCK" 2>/dev/null' EXIT
date +%s > "$STAMP"

cd "$ENGINE" || { say "$NOW  repo not found, nothing done"; exit 0; }
branch=$(git branch --show-current 2>/dev/null || echo "?")
if [ "$branch" != "main" ]; then say "$NOW  main checkout is on '$branch', not main; skipped (needs a human)"; exit 0; fi

# 1. export
if ! out=$(bash coordinator/sync.sh export 2>&1); then
  say "$NOW  export FAILED: $(printf '%s' "$out" | tail -3 | tr '\n' ' ')"
fi

# 2. commit coordinator/ when more than the manifest changed
changed=$(git status --porcelain -- coordinator | grep -v ' coordinator/manifest.json$' | wc -l | tr -d ' ')
if [ "$changed" -gt 0 ]; then
  git add coordinator >/dev/null 2>&1
  git commit -q -m "coordinator export $TODAY $NOW (auto: sync_publish)" >/dev/null 2>&1 && say "$NOW  committed coordinator export ($changed files)"
else
  git checkout -q -- coordinator/manifest.json 2>/dev/null || true
fi

# 3. reconcile with origin
git fetch -q origin main 2>/dev/null || { say "$NOW  fetch failed (offline?); nothing pushed"; exit 0; }
ahead=$(git rev-list --count origin/main..main 2>/dev/null || echo 0)
behind=$(git rev-list --count main..origin/main 2>/dev/null || echo 0)
dirty=$(git status --porcelain --untracked-files=no | wc -l | tr -d ' ')
if [ "$behind" -gt 0 ]; then
  if [ "$ahead" -eq 0 ]; then
    git pull -q --ff-only origin main 2>/dev/null && say "$NOW  pulled $behind commit(s) from origin (work Mac pushed)" || say "$NOW  pull --ff-only failed; needs a human"
  elif [ "$dirty" -eq 0 ]; then
    if git rebase -q origin/main >/dev/null 2>&1; then say "$NOW  rebased $ahead local commit(s) onto $behind from origin"; else git rebase --abort >/dev/null 2>&1; say "$NOW  DIVERGED: rebase conflict, aborted; needs a human"; say "evt: sync-publish-$TODAY#diverged"; exit 0; fi
  else
    say "$NOW  DIVERGED with a dirty tree ($ahead ahead, $behind behind, $dirty modified); not rebasing; needs a human"; say "evt: sync-publish-$TODAY#diverged"; exit 0
  fi
fi

# 4. push
ahead=$(git rev-list --count origin/main..main 2>/dev/null || echo 0)
if [ "$ahead" -gt 0 ]; then
  if git push -q origin main 2>/dev/null; then say "$NOW  pushed $ahead commit(s); origin/main = $(git rev-parse --short origin/main)"; else say "$NOW  push FAILED; needs a human"; fi
else
  say "$NOW  nothing to push (origin/main = $(git rev-parse --short origin/main))"
fi

# 4b. brain snapshot: regenerate + stage, so the hosted brain has something current to
# fetch. Log-only and non-fatal, per the swarm convention (no DM; the daily rundown reads
# this log). STAGES ONLY, never deploys: publishing is outward-facing and the snapshot
# carries seller emails and generated prospect copy, so the wrangler push stays a
# deliberate act. Added 2026-09-05 with the brain's snapshot rewrite.
BRAIN="$ENGINE/gtm-hosted-platform/brain/publish_gtm_state.sh"
# 2026-09-11 live loop: the loop's inputs run first (signal ledger sync, universe rebuild from
# Audiences), then the snapshot; --deploy only when automation/config/brain_publish.json says so.
PUBCFG="$ENGINE/automation/config/brain_publish.json"
DEPLOY_FLAG=""
if [ -f "$PUBCFG" ]; then
  if python3 -c "import json,sys; sys.exit(0 if json.load(open('$PUBCFG')).get('signal_review_sync') else 1)" 2>/dev/null; then
    if sr=$(python3 "$ENGINE/automation/signal_review.py" sync 2>&1); then say "$NOW  signal review synced: $(printf '%s' "$sr" | sed -n 3p)"; else say "$NOW  signal review sync FAILED: $(printf '%s' "$sr" | tail -1)"; fi
  fi
  if python3 -c "import json,sys; sys.exit(0 if json.load(open('$PUBCFG')).get('universe_rebuild') else 1)" 2>/dev/null; then
    if ub=$(python3 "$ENGINE/tam-outbound-engine/universe_from_audiences.py" 2>&1); then say "$NOW  universe rebuilt from Audiences: $(printf '%s' "$ub" | python3 -c 'import json,sys; t=sys.stdin.read(); d=json.loads(t[:t.rfind("}")+1]); print(d["accounts"],"accounts,",d["triggers_added"],"triggers added")' 2>/dev/null)"; else say "$NOW  universe rebuild FAILED, last universe kept: $(printf '%s' "$ub" | tail -1)"; say "evt: brain-snapshot-$TODAY#universe-stale"; fi
  fi
  if python3 -c "import json,sys; sys.exit(0 if json.load(open('$PUBCFG')).get('deploy') else 1)" 2>/dev/null; then DEPLOY_FLAG="--deploy"; fi
fi
if [ -x "$BRAIN" ]; then
  if out=$("$BRAIN" $DEPLOY_FLAG 2>&1); then
    if [ -n "$DEPLOY_FLAG" ]; then say "$NOW  brain snapshot regenerated and DEPLOYED (brain_publish.json deploy=true)"; say "evt: brain-snapshot-$TODAY#deployed"; else say "$NOW  brain snapshot regenerated and staged (deploy=false)"; fi
  else
    say "$NOW  brain snapshot FAILED (hosted brain will keep serving its last one, redacted once stale): $(printf '%s' "$out" | tail -2 | tr '\n' ' ')"
    say "evt: brain-snapshot-$TODAY#stale"
  fi
fi

# 5. uncommitted work, main checkout + worktrees
unpushed=0
report_tree() {  # $1 path $2 label
  local n paths
  n=$(git -C "$1" status --porcelain 2>/dev/null | grep -v -E '^\?\? (\.wrangler/|_archive/)|(automation/config/rundown_thread_state.json|control_tower_state.json)$' | wc -l | tr -d ' ')
  if [ "$n" -gt 0 ]; then
    unpushed=$((unpushed + n))
    paths=$(git -C "$1" status --porcelain 2>/dev/null | grep -v -E '^\?\? (\.wrangler/|_archive/)|(automation/config/rundown_thread_state.json|control_tower_state.json)$' | awk '{print $2}' | cut -d/ -f1-2 | sort | uniq -c | sort -rn | head -6 | awk '{printf "%s(%s) ", $2, $1}')
    say "  - $2: $n uncommitted: $paths"
  fi
  local ah; ah=$(git -C "$1" rev-list --count "origin/$(git -C "$1" branch --show-current 2>/dev/null)..HEAD" 2>/dev/null || echo 0)
  if [ "$ah" -gt 0 ]; then unpushed=$((unpushed + ah)); say "  - $2: $ah commit(s) not on origin"; fi
}
say "$NOW  uncommitted or unpushed work:"
report_tree "$ENGINE" "main checkout"
while IFS= read -r wt; do   # process substitution, not a pipe, so $unpushed survives the loop
  [ -z "$wt" ] && continue
  [ "$wt" = "$ENGINE" ] && continue
  report_tree "$wt" "worktree $(basename "$wt") [$(git -C "$wt" branch --show-current 2>/dev/null)]"
done < <(git worktree list --porcelain | awk '/^worktree /{print substr($0,10)}')
if [ "$unpushed" -eq 0 ]; then say "  - none"; else say "evt: sync-publish-$TODAY#unpushed-work"; fi
say ""
exit 0
