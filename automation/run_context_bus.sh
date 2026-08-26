#!/bin/zsh
# context-bus publisher (personal Mac). Launched by com.dallasandrews.gtm.contextbus.
#
# Stages the day's memory delta, changed assets, and distilled session skeletons into
# ~/context-bus, has Claude write the digests and rewrite INBOX.md, then commits and
# pushes to the private GitHub repo the work Mac pulls from.
#
# Registry rules held: this job NEVER DMs Dallas (rule 2/4). It writes
# automation/logs/context-bus-<date>.md and the daily rundown reads it.
set -uo pipefail

ENGINE="/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer"
BUS="$HOME/context-bus"
TODAY=$(date +%Y-%m-%d)
OUT="$ENGINE/automation/logs/_run_context_bus.out"
LOG="$ENGINE/automation/logs/context-bus-$TODAY.md"

cd "$ENGINE" || exit 1
echo "=== context-bus run $(date) ===" >> "$OUT"

# 1. Stage. If nothing changed, stop before spending a Claude call.
COUNTS=$(python3 "$ENGINE/automation/context_bus_stage.py" 2>>"$OUT")
STAGE_RC=$?
echo "stage rc=$STAGE_RC counts=$COUNTS" >> "$OUT"
if [ $STAGE_RC -ne 0 ]; then
  { echo "# context-bus $TODAY"; echo; echo "STAGE FAILED (rc=$STAGE_RC). Nothing published today."
    echo "See _run_context_bus.out."; echo; echo "evt: context-bus-$TODAY#stage-failed"; } > "$LOG"
  exit 1
fi

SESSIONS=$(echo "$COUNTS" | python3 -c 'import sys,json;print(json.load(sys.stdin)["sessions"])' 2>/dev/null || echo 0)
MEMNEW=$(echo "$COUNTS" | python3 -c 'import sys,json;print(json.load(sys.stdin)["memory_new"])' 2>/dev/null || echo 0)
ASSETS=$(echo "$COUNTS" | python3 -c 'import sys,json;print(json.load(sys.stdin)["assets"])' 2>/dev/null || echo 0)

if [ "$SESSIONS" -eq 0 ] && [ "$MEMNEW" -eq 0 ] && [ "$ASSETS" -eq 0 ]; then
  { echo "# context-bus $TODAY"; echo; echo "Nothing changed since the last publish. No push, no Claude call."; } > "$LOG"
  exit 0
fi

# 2. Digest. Claude turns the skeletons into readable digests and rewrites INBOX.md.
export CONTEXT_BUS_LOG="$LOG"
"/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/lib/claude_net.sh" --model claude-sonnet-5 -p "$(cat <<'PROMPT'
Unattended scheduled run: context-bus publisher. Nobody is watching live. You are preparing
the context handoff that Dallas's WORK MacBook (Intradiem Enterprise Claude account) will pull
and read to catch up on what happened on the personal machine.

Ground rules for this run only:
- Do not message, DM, post, or email anyone. This job never notifies. It writes files.
- Work ONLY inside $HOME/context-bus and the one log file named at the end. Touch nothing else.
- Do not read the raw transcripts in ~/.claude/projects. The staged skeletons are your source.
- Write paths using the {{HOME}} token exactly as the staged files already do. Never write a
  literal /Users/dallasandrews path into any file. The work Mac is /Users/IntradiemDA and the
  token is what makes the handoff portable.

Do this:

1. Read $HOME/context-bus/.staging/stage_manifest.json to see what was staged.

2. For EACH skeleton in $HOME/context-bus/.staging/skeletons/*.md, write one digest to
   $HOME/context-bus/digests/<the session's date>-<3-5 word kebab slug>.md with this shape:

   # <plain title of what this session was>
   when: <date and time from the skeleton header>
   where: <cwd from the skeleton header>

   ## What we were doing
   Two or three sentences. The actual task, in plain language.

   ## Decisions made
   Bullets. Only real decisions, the kind that would be wrong to re-litigate. If none, say "None."

   ## What got built or changed
   Bullets naming the real files (token paths). Skip scratchpad churn.

   ## Still open
   Bullets. What was unfinished, blocked, or waiting on Dallas. If nothing, say "Nothing open."

   Skip a session entirely if it produced no decisions and no file changes worth carrying.
   If a digest for that session already exists, overwrite it (later runs know more).

3. Rewrite $HOME/context-bus/INBOX.md completely. This is the ONE file the work machine reads
   first, so it has to stand alone. Shape:

   # INBOX
   published: <today's date> from the personal Mac

   ## Read me first
   One short paragraph: what changed since the last drop and what the work machine should know
   before it does anything. Lead with anything that would cause wrong work if missed.

   ## Sessions in this drop
   One line per digest: date, title, and the single most important thing from it, with the
   digest filename in parentheses.

   ## Memory files new or changed
   One line each: filename plus the hook from its own description frontmatter. Read the actual
   files in $HOME/context-bus/memory/ for these. Group as NEW vs CHANGED using the manifest.

   ## Assets changed
   Grouped by kind (skills, agents, automation, workflows), token paths, one line each.

   ## Open threads carried forward
   Everything still open across the last 7 days of digests, not just today's. Read the other
   files in $HOME/context-bus/digests/ to carry these forward. This section is the point of
   the whole file: it is what stops the work machine from redoing or contradicting work.

   Keep INBOX.md under 400 lines. If a drop is huge, summarize harder rather than truncating a
   section away.

4. House style applies: no em dashes, no AI-isms, no self-narration, contractions fine.
   Never render an unverified Intradiem figure as fact; mark it [UNVERIFIED] if it appears.

5. Last, write the run log to the file named in the CONTEXT_BUS_LOG environment variable
   (create it): a short "# context-bus <date>" report with counts of sessions digested, memory
   files, and assets, the digest filenames written, and anything that looked wrong. Per
   LOG_CONVENTION.md, mint "evt: context-bus-<date>#<slug>" on any item another job might act
   on (a blocked thread, a failed stage). Do NOT DM anyone. The daily rundown reads this log.
PROMPT
)" --dangerously-skip-permissions >> "$OUT" 2>&1
CLAUDE_RC=$?
echo "claude rc=$CLAUDE_RC" >> "$OUT"

# 3. Token sweep on GENERATED payload only. The digest step is told to use {{HOME}}, but a
#    single literal path that slips through would land broken on /Users/IntradiemDA.
#    README.md and bin/ are excluded: they name both real paths on purpose, as prose.
cd "$BUS" || exit 1
for f in $(grep -rl "/Users/dallasandrews" memory digests assets INBOX.md MANIFEST.json 2>/dev/null); do
  LC_ALL=C sed -i '' 's#/Users/dallasandrews#{{HOME}}#g' "$f"
  echo "token-swept $f" >> "$OUT"
done

# 4. Commit and push. The work Mac only ever pulls, so this side owns history.
git add -A >> "$OUT" 2>&1
if git diff --cached --quiet; then
  echo "nothing to commit" >> "$OUT"
else
  git commit -q -m "context drop $TODAY: ${SESSIONS} sessions, ${MEMNEW} memory, ${ASSETS} assets" >> "$OUT" 2>&1
fi
PUSH_MSG=$(git push origin HEAD 2>&1)
PUSH_RC=$?
echo "push rc=$PUSH_RC $PUSH_MSG" >> "$OUT"

# 5. Only advance the watermark on a successful push, so a failed run re-publishes
#    the same delta tomorrow instead of silently dropping it.
if [ $PUSH_RC -eq 0 ]; then
  python3 -c "
import json, datetime, pathlib
p = pathlib.Path.home() / '.context-bus-state.json'
p.write_text(json.dumps({'last_publish': datetime.datetime.now(datetime.timezone.utc).isoformat()}, indent=2))
" >> "$OUT" 2>&1
else
  { echo; echo "## Push failed"; echo "The drop was staged and committed but did not reach GitHub."
    echo "Watermark NOT advanced, so tomorrow's run republishes this same delta."
    echo "git said: $PUSH_MSG"; echo; echo "evt: context-bus-$TODAY#push-failed"; } >> "$LOG"
fi

exit 0
