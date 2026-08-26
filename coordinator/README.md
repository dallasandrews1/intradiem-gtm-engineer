# coordinator/ : the Claude working context, versioned with the repo

This folder is a snapshot of everything that makes a Claude Code session on any machine behave like Dallas's: the global instruction set, the Intradiem skill library, the agent definitions, the workflow scripts, and the file-based memory with its index. It exists so the work MacBook gets the whole context on `git clone` instead of by AirDrop, and so every later `git pull` carries the delta.

Source of truth stays on the personal Mac: `~/.claude/CLAUDE.md`, `~/.claude/skills`, `~/.claude/agents`, and `~/coordinator/memory` (the durable memory store per the Jul 20 2026 consolidation rule). This folder is a copy, refreshed by `sync.sh export` before each push.

| Path | What | Source on the personal Mac |
|---|---|---|
| `CLAUDE.md` | master instruction set (global) | `~/.claude/CLAUDE.md` (identical to `~/coordinator/CLAUDE.md`) |
| `AGENT_REGISTRY.md` | swarm registry and governing rules | `~/coordinator/AGENT_REGISTRY.md` |
| `skills/` | 19 Intradiem work skills (`dallas-brand` and `health-outcomes` are personal and stay out) | `~/.claude/skills/` |
| `agents/` | 17 subagent definitions | `~/.claude/agents/` |
| `workflows/` | orchestration scripts | `~/coordinator/.claude/workflows/` |
| `memory/` | file-based memory, one fact per file, plus `MEMORY.md` index | `~/coordinator/memory/` after sweeping the harness stores |
| `manifest.json` | when and where the snapshot was taken, with counts | written by `sync.sh export` |
| `sync.sh`, `merge_index.py` | the carrier | this folder |

## Commands

```
coordinator/sync.sh export    personal Mac, before every push
coordinator/sync.sh install   work Mac (or any fresh machine), after clone or pull
coordinator/sync.sh status    what differs between the live machine and the snapshot
```

`export` first sweeps memory the harness wrote outside `~/coordinator/memory` (the `~/.claude/projects/<slug>/memory` stores) back into it, merges the indexes without duplicate pointers, then snapshots. It refuses to write the snapshot if a personal file or a secret pattern shows up.

`install` places everything, rewrites `/Users/dallasandrews` to the receiving machine's home in text files, backs up anything it replaces under `~/.claude/backups/coordinator-install-<stamp>/`, and points the harness memory dir for this repo at `~/coordinator/memory` with a symlink so the two stores cannot drift on that machine.

## What never goes in here

- Personal material: interview-era notes, the TAIS profile, personal side projects, `dallas-brand`. The exclude lists are at the top of `sync.sh`.
- `~/.claude/settings.json` (can carry keys; each machine keeps its own).
- Mem0 configuration. Mem0 is not cleared for the Intradiem Enterprise account (Jason Jones, #ai, Jul 17 2026). File memory works without it.

## Relationship to the context bus

The context bus (`~/context-bus`, private repo `dallasandrews1/context-bus`, three drops a day from the personal Mac) keeps carrying the daily memory delta and session digests. This folder is the full baseline the bus assumes is already in place; run `sync.sh install` first, then `~/context-bus/bin/ingest.sh` as usual.
