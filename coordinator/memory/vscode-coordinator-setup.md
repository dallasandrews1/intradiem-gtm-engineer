---
name: vscode-coordinator-setup
description: "Jul 9-10 2026: coordinator folder built and fully migrated to ~/coordinator (VS Code + Claude Code + Mem0 plugin); the coordinator memory copy is a snapshot that goes stale unless re-synced"
metadata:
  node_type: memory
  type: project
  originSessionId: edfe77c7-6120-4e44-b06f-69692e43ccbd
---

Built Jul 9 2026 in the Intradiem GTM Engineer project folder, following [[jason-ai-enablement-jul9]], then migrated Jul 9-10 to its permanent home `~/coordinator` (now outside Cowork's connected folders): CLAUDE.md master instruction set, ONBOARD.md bootstrap prompt, `memory/` (full export of the Cowork memory corpus as of the migration date), `.claude/skills/` (18 skills global), `dallas.code-workspace`. Mem0 plugin v0.2.12 installed user-scope, onboarded (user_id=dallasandrews, project_id=coordinator).

Dallas ruled: nobody cares about local vs hosted memory tier, move fast — Mem0 cloud plugin is the standing choice, no local/OpenMemory hedge.

**Gotcha solved:** Dock-launched VS Code doesn't source `.zshrc`, so `MEM0_API_KEY` lives in the env block of `~/.claude/settings.json` (if the key is ever rotated, update both places).

**Maintenance rule:** the coordinator `memory/` folder is a snapshot, not a live mirror. Whichever surface (Cowork or VS Code) does substantive work must sync it back — see [[surface-split-rule]] and [[mem0-sync-gap-jul17]] for what happens when that discipline lapses (a full week, Jul 11-17, went uncaptured).

**Jul 17 addendum:** same snapshot problem applies to any new machine, not just Cowork/VS Code sync — the folder has to be physically copied (AirDrop/git) to a second computer, account login alone doesn't carry it. See [[vscode-work-macbook-account-split]] for the work-MacBook case, including the personal-vs-Enterprise Claude account split.
