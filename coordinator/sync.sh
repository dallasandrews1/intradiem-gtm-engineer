#!/bin/bash
# coordinator/sync.sh : carry Dallas's Claude coordinator (instruction set, skills, agents,
# workflows, memory) between machines through this repo.
#
#   sync.sh export    personal Mac. Snapshot ~/.claude + ~/coordinator into coordinator/ here,
#                     after sweeping harness-path memory back into ~/coordinator/memory
#                     (the Jul 20 2026 consolidation rule). Run before every push.
#   sync.sh install   any machine after clone/pull. Place the snapshot into ~/.claude and
#                     ~/coordinator, rewrite /Users/dallasandrews to this home, and point the
#                     harness memory dir for this repo at ~/coordinator/memory.
#   sync.sh status    show what differs between the live machine and the snapshot.
#
# Personal material never enters the snapshot (see EXCLUDE_* below). No secrets live in any
# of these folders; settings.json (which may carry keys) is deliberately not carried.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
REPO="$(cd "$HERE/.." && pwd)"
COORD="$HOME/coordinator"
SRC_HOME="/Users/dallasandrews"           # the publishing machine's home, rewritten on install
merge_idx() { python3 "$HERE/merge_index.py" "$@"; }

EXCLUDE_SKILLS="dallas-brand health-outcomes"
EXCLUDE_MEMORY="intradiem-interview-status.md dallas-tais-profile.md sustain-vocal-app.md brazen-recruits-system-map.md MEMORY.md.bak-jul31"

slug() { printf '%s' "$1" | sed 's#[/ ]#-#g'; }   # harness project key: path with / and space as -
HARNESS_MEM="$HOME/.claude/projects/$(slug "$REPO")/memory"

excluded_mem() { for x in $EXCLUDE_MEMORY; do [ "$1" = "$x" ] && return 0; done; return 1; }

do_export() {
  echo "== export from $HOME into $HERE"
  [ -d "$COORD/memory" ] || { echo "no $COORD/memory on this machine; export runs on the personal Mac"; exit 1; }

  # 1. sweep: harness-path memory stores back into ~/coordinator/memory (additive, newer wins)
  swept=0
  for store in "$HARNESS_MEM" "$HOME/.claude/projects/$(slug "$HOME")/memory" "$HOME/.claude/projects/$(slug "$COORD")/memory"; do
    [ -d "$store" ] || continue
    [ "$store" -ef "$COORD/memory" ] && continue
    for f in "$store"/*.md; do
      n="$(basename "$f")"; [ "$n" = "MEMORY.md" ] && continue; excluded_mem "$n" && continue
      if [ ! -e "$COORD/memory/$n" ] || [ "$f" -nt "$COORD/memory/$n" ]; then cp -p "$f" "$COORD/memory/$n"; swept=$((swept+1)); fi
    done
    merge_idx "$COORD/memory/MEMORY.md" "$store/MEMORY.md" --out "$COORD/memory/MEMORY.md.new" --exclude $EXCLUDE_MEMORY --label "Swept from $(basename "$(dirname "$store")") on $(date +%Y-%m-%d)" >/dev/null
    mv "$COORD/memory/MEMORY.md.new" "$COORD/memory/MEMORY.md"
  done
  echo "swept $swept harness memory files into $COORD/memory"

  # 2. snapshot
  rm -rf "$HERE/skills" "$HERE/agents" "$HERE/workflows" "$HERE/memory"
  mkdir -p "$HERE/skills" "$HERE/agents" "$HERE/workflows" "$HERE/memory"
  cp "$HOME/.claude/CLAUDE.md" "$HERE/CLAUDE.md"
  [ -f "$COORD/AGENT_REGISTRY.md" ] && cp "$COORD/AGENT_REGISTRY.md" "$HERE/AGENT_REGISTRY.md"
  for s in "$HOME/.claude/skills"/*/; do
    n="$(basename "$s")"; case " $EXCLUDE_SKILLS " in *" $n "*) continue;; esac
    rsync -a --exclude '.DS_Store' "$s" "$HERE/skills/$n/"
  done
  rsync -a --exclude '.DS_Store' "$HOME/.claude/agents/" "$HERE/agents/"
  [ -d "$COORD/.claude/workflows" ] && rsync -a --exclude '.DS_Store' "$COORD/.claude/workflows/" "$HERE/workflows/"
  for f in "$COORD/memory"/*.md; do n="$(basename "$f")"; excluded_mem "$n" && continue; cp -p "$f" "$HERE/memory/$n"; done
  # index: drop excluded pointers
  merge_idx "$COORD/memory/MEMORY.md" --out "$HERE/memory/MEMORY.md" --exclude $EXCLUDE_MEMORY

  # 3. guard: nothing personal, nothing secret
  bad=0
  for x in $EXCLUDE_MEMORY; do [ -e "$HERE/memory/$x" ] && { echo "EXCLUDED FILE PRESENT: $x"; bad=1; }; done
  if grep -rlE 'xox[abpsr]-[A-Za-z0-9-]{10,}|sk-ant-[A-Za-z0-9_-]{20,}|LEMLIST_API_KEY=[A-Za-z0-9]|-----BEGIN [A-Z ]*PRIVATE KEY' "$HERE" --include='*.md' --include='*.js' --include='*.json' --include='*.sh' >/dev/null 2>&1; then
    echo "SECRET PATTERN FOUND in snapshot, aborting"; grep -rlE 'xox[abpsr]-|sk-ant-|LEMLIST_API_KEY=|PRIVATE KEY' "$HERE"; bad=1
  fi
  [ $bad -eq 0 ] || exit 2

  cat > "$HERE/manifest.json" <<JSON
{
  "exported_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "exported_from": "$(hostname -s) ($HOME)",
  "skills": $(ls -d "$HERE"/skills/*/ | wc -l | tr -d ' '),
  "agents": $(ls "$HERE"/agents/*.md | wc -l | tr -d ' '),
  "workflows": $(ls "$HERE"/workflows/*.js 2>/dev/null | wc -l | tr -d ' '),
  "memory_files": $(ls "$HERE"/memory/*.md | grep -vc 'MEMORY.md'),
  "index_pointers": $(grep -c '^- \[' "$HERE/memory/MEMORY.md")
}
JSON
  cat "$HERE/manifest.json"
}

rewrite_paths() {  # $1 dir : replace the publishing home with this machine's home, text files only
  [ "$HOME" = "$SRC_HOME" ] && return 0
  # grep exits 1 when a target holds no publishing-home path; under pipefail that would abort the whole install
  # (seen on the work Mac 2026-08-31: install stopped after the index merge, before the symlink). Tolerate it.
  { grep -rlI "$SRC_HOME" "$1" 2>/dev/null || true; } | while IFS= read -r f; do LC_ALL=C sed -i '' "s#$SRC_HOME#$HOME#g" "$f"; done
}

do_install() {
  echo "== install from $HERE into $HOME"
  [ -f "$HERE/manifest.json" ] || { echo "no snapshot here; run 'sync.sh export' on the personal Mac first"; exit 1; }
  ts="$(date +%Y%m%d-%H%M%S)"; bak="$HOME/.claude/backups/coordinator-install-$ts"; mkdir -p "$bak" "$HOME/.claude/skills" "$HOME/.claude/agents" "$COORD/memory" "$COORD/.claude/workflows"

  [ -f "$HOME/.claude/CLAUDE.md" ] && cp "$HOME/.claude/CLAUDE.md" "$bak/CLAUDE.md"
  cp "$HERE/CLAUDE.md" "$HOME/.claude/CLAUDE.md"; cp "$HERE/CLAUDE.md" "$COORD/CLAUDE.md"
  [ -f "$HERE/AGENT_REGISTRY.md" ] && cp "$HERE/AGENT_REGISTRY.md" "$COORD/AGENT_REGISTRY.md"
  rsync -a --backup --backup-dir="$bak/skills" "$HERE/skills/" "$HOME/.claude/skills/"
  rsync -a --backup --backup-dir="$bak/skills" "$HERE/skills/" "$COORD/.claude/skills/"
  rsync -a --backup --backup-dir="$bak/agents" "$HERE/agents/" "$HOME/.claude/agents/"
  rsync -a --backup --backup-dir="$bak/agents" "$HERE/agents/" "$COORD/.claude/agents/"
  rsync -a "$HERE/workflows/" "$COORD/.claude/workflows/" 2>/dev/null || true
  rsync -a --update --exclude 'MEMORY.md' --backup --backup-dir="$bak/memory" "$HERE/memory/" "$COORD/memory/"
  if [ -f "$COORD/memory/MEMORY.md" ]; then
    merge_idx "$COORD/memory/MEMORY.md" "$HERE/memory/MEMORY.md" --out "$COORD/memory/MEMORY.md.new" --label "Installed from repo snapshot $(date +%Y-%m-%d)"
    mv "$COORD/memory/MEMORY.md.new" "$COORD/memory/MEMORY.md"
  else
    cp "$HERE/memory/MEMORY.md" "$COORD/memory/MEMORY.md"
  fi
  rewrite_paths "$HOME/.claude/CLAUDE.md"; rewrite_paths "$COORD"; rewrite_paths "$HOME/.claude/skills"; rewrite_paths "$HOME/.claude/agents"

  # harness memory dir for this repo: symlink to the canonical store so the two never drift
  mkdir -p "$(dirname "$HARNESS_MEM")"
  if [ -L "$HARNESS_MEM" ]; then
    echo "harness memory already linked: $HARNESS_MEM -> $(readlink "$HARNESS_MEM")"
  elif [ -d "$HARNESS_MEM" ] && [ -n "$(ls -A "$HARNESS_MEM")" ]; then
    echo "harness memory dir exists with content, merging it into $COORD/memory then linking"
    rsync -a --update --exclude 'MEMORY.md' "$HARNESS_MEM/" "$COORD/memory/"
    merge_idx "$COORD/memory/MEMORY.md" "$HARNESS_MEM/MEMORY.md" --out "$COORD/memory/MEMORY.md.new" --label "Merged from harness store $(date +%Y-%m-%d)"; mv "$COORD/memory/MEMORY.md.new" "$COORD/memory/MEMORY.md"
    mv "$HARNESS_MEM" "$bak/harness-memory"; ln -s "$COORD/memory" "$HARNESS_MEM"
  else
    rm -rf "$HARNESS_MEM"; ln -s "$COORD/memory" "$HARNESS_MEM"
  fi
  echo "harness memory: $HARNESS_MEM -> $COORD/memory"
  echo "backups of anything replaced: $bak"
  echo "installed: $(ls -d "$HOME"/.claude/skills/*/ | wc -l | tr -d ' ') skills, $(ls "$HOME"/.claude/agents/*.md | wc -l | tr -d ' ') agents, $(ls "$COORD"/memory/*.md | wc -l | tr -d ' ') memory files"
}

do_status() {
  echo "== snapshot vs this machine"
  [ -f "$HERE/manifest.json" ] && cat "$HERE/manifest.json"
  echo "-- skills"; diff -rq "$HERE/skills" "$HOME/.claude/skills" 2>/dev/null | grep -v -e dallas-brand -e health-outcomes || true
  echo "-- agents"; diff -rq "$HERE/agents" "$HOME/.claude/agents" 2>/dev/null || true
  echo "-- memory (files only in one place)"; comm -3 <(ls "$HERE/memory" | sort) <(ls "$COORD/memory" 2>/dev/null | sort) | head -40
  echo "-- harness memory dir: $HARNESS_MEM $( [ -L "$HARNESS_MEM" ] && echo '(symlink)' || echo '(real dir, can drift)')"
}

case "${1:-}" in
  export) do_export;; install) do_install;; status) do_status;;
  *) sed -n 2,15p "$0"; exit 1;;
esac
