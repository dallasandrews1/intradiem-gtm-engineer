# Work MacBook bootstrap (IntradiemDA)

Goal: the Intradiem-issued MacBook (`/Users/IntradiemDA`, Claude Enterprise account) runs Claude Code with the same instruction set, skills, agents, and memory as the personal Mac, against a git clone of this repo instead of a Jul 20 AirDrop copy.

Standing decisions this respects: the work laptop is never a second scheduling home (registry decision Jul 27 2026, no launchd jobs there), Mem0 stays off on the Enterprise account until cleared, and the context bus stays pull-only from that machine.

Every command block below is single physical lines, no backslash continuations, per the Jul 20 transfer lessons.

---

## Step 0, personal Mac: publish (staged, not run)

Everything is committed on `main`; nothing is pushed and no remote is set. Pick one target and run it here:

**A. Private GitHub repo under the same account the context bus uses (fastest, works today):**

```
cd "$HOME/Claude/Projects/Intradiem GTM Engineer" && gh repo create dallasandrews1/intradiem-gtm-engineer --private --source=. --remote=origin --push
git -C "$HOME/Claude/Projects/Intradiem GTM Engineer" push origin agents/vs-code-agents-window-usage agents/claude-agent-integration
```

**B. Intradiem Bitbucket (if the access request in `Bitbucket_Access_Request.md` has been granted):**

```
git -C "$HOME/Claude/Projects/Intradiem GTM Engineer" remote add origin https://bitbucket.org/<workspace>/<repo>.git
git -C "$HOME/Claude/Projects/Intradiem GTM Engineer" push -u origin main
```

After any later change on the personal Mac: `coordinator/sync.sh export`, commit, push. That is the whole refresh loop.

Reminder for the clone target: `coordinator/` holds 286 memory files and the full skill library; the repo is about 75 MB including the DWO deck and strike-room PDFs.

---

## Step 1, work Mac: preserve anything done in the Jul 20 copy

The Jul 20 AirDrop placed a copy at `~/Claude/Projects/Intradiem GTM Engineer`. Before replacing it, see whether anything was changed there since:

```
cd "$HOME/Claude/Projects/Intradiem GTM Engineer" && git status --short | head -40 && git log --oneline -3
```

If `git status` shows modified or untracked files that matter (anything under `motions/`, `automation/`, or a UI sheet you wrote there), copy them to `~/Desktop/jul20-copy-changes/` first. Then move the old copy aside:

```
mv "$HOME/Claude/Projects/Intradiem GTM Engineer" "$HOME/Claude/Projects/Intradiem GTM Engineer.jul20"
```

## Step 2, work Mac: clone to the same path

The path matters: the harness derives the memory-directory key from the absolute project path, and every memory file and agent references `~/Claude/Projects/Intradiem GTM Engineer`.

```
mkdir -p "$HOME/Claude/Projects" && git clone https://github.com/dallasandrews1/intradiem-gtm-engineer.git "$HOME/Claude/Projects/Intradiem GTM Engineer"
```

(Bitbucket target: swap the URL.) `gh auth login` first if the clone prompts; the repo is private.

## Step 3, work Mac: install the coordinator

```
"$HOME/Claude/Projects/Intradiem GTM Engineer/coordinator/sync.sh" install
```

What it does: writes `~/.claude/CLAUDE.md`, `~/.claude/skills/`, `~/.claude/agents/`, `~/coordinator/{CLAUDE.md,AGENT_REGISTRY.md,memory,.claude/workflows}`, rewrites `/Users/dallasandrews` to `/Users/IntradiemDA` in text files, backs up whatever it replaced, and links `~/.claude/projects/-Users-IntradiemDA-Claude-Projects-Intradiem-GTM-Engineer/memory` to `~/coordinator/memory`. Confirm with:

```
"$HOME/Claude/Projects/Intradiem GTM Engineer/coordinator/sync.sh" status
```

Expect no skill or agent diffs, and the harness memory dir reported as a symlink.

## Step 4, work Mac: Claude Code settings

Open `~/.claude/settings.json` and confirm, without copying the personal Mac's file:

- `enabledPlugins`: `clay@clay-plugins` on. Leave `mem0@mem0-plugins` off (compliance hold). `gitkraken-hooks` and `cloudflare` are optional.
- `permissions.additionalDirectories`: add `~/coordinator` and `~/Claude/Projects/Clay Builds and Strategy` if that folder exists there.
- Model: whatever the Enterprise seat allows.

Sign into Claude Code with the Intradiem Enterprise account, not the personal one (VS Code Settings Sync can stay on the personal account; the two logins are independent).

## Step 5, work Mac: connectors and CLIs

Connectors are per Claude account, so nothing from the personal Mac carries over. On the Enterprise account each one is an admin allowlist item, so request them as a batch. In priority order for the first build (Salesforce attribution loop):

| Need | How | Status to expect |
|---|---|---|
| Salesforce | `sf` CLI, SSO login (below) | new on this machine |
| Clay | plugin CLI, `clay login` to the Enterprise workspace | done Jul 20; re-run `clay whoami` |
| Slack | claude.ai connector | awaiting IT approval as of Jul 20 |
| Microsoft 365 (Outlook, Teams, SharePoint) | claude.ai connector | request |
| Otter | claude.ai connector | awaiting IT approval as of Jul 20 |
| Monday.com | claude.ai connector | request (AI Champion boards) |
| lemlist | claude.ai connector, or `LEMLIST_API_KEY` in a local `automation/config/lemlist.env` (gitignored, never committed) | request |
| Apollo | claude.ai connector | request |
| 6sense | web login only, Dallas has his own | no connector exists |
| Gmail, Google Drive | personal; do not connect on the work account | skip |

Clay CLI:

```
clay whoami || clay login
clay workflows list | head
```

Salesforce CLI (this is the reason the work laptop exists in this plan):

```
npm install -g @salesforce/cli && sf --version
sf org login web --alias intradiem
sf org display --target-org intradiem
sf data query --target-org intradiem --query "SELECT Id, Name FROM Lead LIMIT 3"
```

If `npm` is missing, install Node from nodejs.org first. The web login goes through Intradiem SSO in the browser; no password is stored by Claude.

## Step 6, work Mac: context bus stays the daily carrier

```
[ -d "$HOME/context-bus/.git" ] || git clone https://github.com/dallasandrews1/context-bus.git "$HOME/context-bus"
"$HOME/context-bus/bin/ingest.sh"
```

Then paste the block from `~/context-bus/INGEST.md` into Claude Code. Do this at the start of any work-Mac session; the repo clone is the baseline, the bus is the delta. Reverse direction is `~/context-bus/bin/handoff.sh` (no Claude call, works when Enterprise usage is exhausted).

## Step 7, work Mac: first message in Claude Code

Open `~/Claude/Projects/Intradiem GTM Engineer` in VS Code and paste:

```
You're picking up on the work MacBook. Read CLAUDE.md here and ~/.claude/CLAUDE.md, then memory/MEMORY.md through the harness memory dir, and confirm in one short paragraph: who I am, what week it is, the priority stack (Star Ratings, back office existing customers, back office new logo, webinar), what's gated and why, and the house style rules. Then read coordinator/BOOTSTRAP_WORK_LAPTOP.md and tell me which connectors and CLIs you can actually reach from this session so we know what the first Salesforce build can use.
```

## Refresh loop after today

- Personal Mac: work as usual; before pushing, `coordinator/sync.sh export && git add coordinator && git commit -m "coordinator snapshot" && git push`.
- Work Mac: `git pull && coordinator/sync.sh install`, then `~/context-bus/bin/ingest.sh` for anything since the last push.
- Memory written on the work Mac lands in `~/coordinator/memory` (the symlink guarantees it). Bring it back with `handoff.sh` or by committing it under `coordinator/memory` on a branch and pushing; `sync.sh export` on the personal Mac will not overwrite newer files.

## Known traps

1. Placing `~/coordinator` is the load-bearing step; `sync.sh install` does it, but if you ever hand-copy, do the coordinator first.
2. Never paste multi-line `unzip` or backslash-continued blocks; every block here is single lines.
3. The work Mac's newest `~/.claude/projects/*/*.jsonl` is genuinely the interactive session (no swarm jobs there), which is what `handoff.sh` relies on.
4. `automation/` is in the repo for reference and for on-demand runs only. Do not `launchctl load` any plist on the work Mac.
