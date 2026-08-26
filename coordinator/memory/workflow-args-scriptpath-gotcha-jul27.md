---
name: workflow-args-scriptpath-gotcha-jul27
description: FEEDBACK - passing args to Workflow() via scriptPath didn't propagate; war-room-fanout ran the full 137-account universe instead of the scoped "strategic" filter, burning 3.6M subagent tokens on what was meant to be a small smoke test
metadata:
  type: feedback
---

2026-07-27: invoked `Workflow({scriptPath: ".../war-room-fanout.js", args: {"universe": "strategic"}})` intending a cheap, narrowly-scoped smoke test after a model-tiering edit. The script reads `const universe = (args && args.universe) || 'all'`. The actual run came back `"universe":"all"`, scanning all 137 accounts across 139 agents, 3.6M subagent tokens, ~17 minutes, instead of the handful of named strategic accounts intended.

**Why:** not fully confirmed, but empirically the `args` value didn't reach the script's `args` global when invoked via `scriptPath`, even though the tool accepts `args` alongside `scriptPath` in its signature. Invoking by registered `name` (as done successfully for `gtm-proposal-sweep`) may behave differently; untested whether that path threads `args` correctly either.

**How to apply:** before trusting a scoped/filtered Workflow run to stay small, either (a) invoke by name instead of scriptPath when args matter and confirm the scope logs as expected, or (b) add a cheap `log(\`args=${JSON.stringify(args)}\`)` as literally the first line of the script and check that log line before letting a large fan-out proceed. Never assume a passed `args` filter took effect just because the call didn't error, expensive fan-out workflows should self-report their effective scope immediately so a wrong-scope run gets caught in seconds, not after 3.6M tokens.

Related: [[usage-optimization-config-jul24]], [[graph-engineering-audit-jul27]].
