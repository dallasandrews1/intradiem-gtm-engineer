#!/bin/bash
# sync_work_mac.sh : the work Mac's half of the two-machine loop. Pure git + sync.sh, no Claude call.
#
#   sync_work_mac.sh start   SessionStart hook: fast-forward main from origin, install the coordinator.
#   sync_work_mac.sh end     SessionEnd hook: sweep memory written here back into the snapshot
#                            (with paths rewritten to the publishing home), commit everything this
#                            machine changed, rebase if origin moved, push.
#
# Standing rules kept: the work Mac never runs `sync.sh export` (it would snapshot this machine's
# rewritten paths and its work-only skills over the personal Mac's), never loads launchd jobs,
# never messages anyone. Everything lands in automation/logs/sync-work-mac-<date>.md (gitignored).
# Throttled to one run per mode per 10 minutes. Exits 0 always so a session is never blocked.
set -uo pipefail

MODE="${1:-}"
ENGINE="$HOME/Claude/Projects/Intradiem GTM Engineer"
LOGDIR="$ENGINE/automation/logs"
TODAY=$(date +%Y-%m-%d); NOW=$(date +%H:%M)
LOG="$LOGDIR/sync-work-mac-$TODAY.md"
STAMP="$LOGDIR/.sync-work-mac-$MODE-last"
FORCE=0; for a in "$@"; do [ "$a" = "--force" ] && FORCE=1; done
# stdin (hook JSON) is intentionally not read: reading it blocks when stdin is a terminal

mkdir -p "$LOGDIR"
[ -f "$LOG" ] || printf '# sync-work-mac %s\n\n' "$TODAY" > "$LOG"
say() { printf '%s\n' "$*" >> "$LOG"; }

case "$MODE" in start|end) ;; *) echo "usage: sync_work_mac.sh start|end [--force]"; exit 0;; esac
if [ $FORCE -eq 0 ] && [ -f "$STAMP" ]; then
  last=$(cat "$STAMP" 2>/dev/null || echo 0); if [ $(( $(date +%s) - last )) -lt 600 ]; then exit 0; fi
fi
date +%s > "$STAMP"

cd "$ENGINE" || { say "$NOW  repo not found"; exit 0; }
branch=$(git branch --show-current 2>/dev/null || echo "?")
[ "$branch" = "main" ] || { say "$NOW  on '$branch', not main; skipped (needs a human)"; exit 0; }

if [ "$MODE" = "start" ]; then
  git fetch -q origin main 2>/dev/null || { say "$NOW  start: fetch failed (offline?)"; exit 0; }
  behind=$(git rev-list --count main..origin/main 2>/dev/null || echo 0)
  if [ "$behind" -gt 0 ]; then
    if git pull -q --ff-only origin main 2>/dev/null; then
      say "$NOW  start: pulled $behind commit(s), now $(git rev-parse --short HEAD)"
      bash coordinator/sync.sh install >/dev/null 2>&1 && say "$NOW  start: coordinator installed" || say "$NOW  start: install FAILED, run sync.sh install by hand"
    else
      say "$NOW  start: pull --ff-only failed (local commits or conflicting edits); needs a human"
    fi
  else
    say "$NOW  start: already at origin/main ($(git rev-parse --short HEAD))"
  fi
  exit 0
fi

# end
swept=$(bash coordinator/sync.sh export-memory 2>/dev/null | tail -1)
say "$NOW  end: $swept"
n=$(git status --porcelain | wc -l | tr -d ' ')
if [ "$n" -gt 300 ]; then say "$NOW  end: $n changed files is more than a session's worth; not committing; needs a human"; exit 0; fi
if [ "$n" -gt 0 ]; then
  git add -A >/dev/null 2>&1
  git commit -q -m "Work Mac session $TODAY $NOW (auto: sync_work_mac)" >/dev/null 2>&1 && say "$NOW  end: committed $n change(s)"
fi
git fetch -q origin main 2>/dev/null || { say "$NOW  end: fetch failed (offline?); commit kept locally, push next time"; exit 0; }
ahead=$(git rev-list --count origin/main..main 2>/dev/null || echo 0)
behind=$(git rev-list --count main..origin/main 2>/dev/null || echo 0)
if [ "$behind" -gt 0 ] && [ "$ahead" -gt 0 ]; then
  if git rebase -q origin/main >/dev/null 2>&1; then say "$NOW  end: rebased onto $behind from origin"; else git rebase --abort >/dev/null 2>&1; say "$NOW  end: DIVERGED, rebase conflict aborted; needs a human"; exit 0; fi
elif [ "$behind" -gt 0 ]; then
  git pull -q --ff-only origin main 2>/dev/null && say "$NOW  end: pulled $behind from origin"
fi
ahead=$(git rev-list --count origin/main..main 2>/dev/null || echo 0)
if [ "$ahead" -gt 0 ]; then
  git push -q origin main 2>/dev/null && say "$NOW  end: pushed $ahead commit(s); origin/main = $(git rev-parse --short origin/main)" || say "$NOW  end: push FAILED; needs a human"
else
  say "$NOW  end: nothing to push"
fi
exit 0
