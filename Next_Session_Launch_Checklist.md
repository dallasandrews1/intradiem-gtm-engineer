# Next Session Launch Checklist
Date: 2026-07-18

Use this at the start of the next Claude Code session.

## 0. Live execution state (verified 2026-07-18, read before priorities)
The registry and handoff run behind live Clay. Verified live: WFM-Adjacency L3 (t_0tic8arWbZp8bSx87Ad) holds 524 rows, not 0. MessageGen is generating drafts. The active blocker is the Draft Audit failing rows on unpopulated/snake_case tokens, most likely unresolved MessageGen input bindings (Dallas is working this directly).

Implication for priority order: the WFM-Adjacency drafts are the outbound path and sit closest to a send; the control-tower parser bugs below are instrumentation. Lead with getting the 524 to send-ready (clean drafts through Draft Audit + Voice Audit to HOLD, then rep review), then return to the tower. Do not let the stale registry drive the order. Sends still stay gated on mailbox warmup; nothing here flips a send gate.

## 1. Read these first
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/GTM_Strategy_Automation_Handoff.md
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/Clay_Build_State_Registry.md
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/Control_Tower_Build_Contract_v1.md
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/clay-workbook-builder/USE_THIS_PROMPT.md

## 2. Confirm the current state
- The control tower builder exists at /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/build_control_tower.py
- The current snapshot exists at /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/control_tower_state.json
- The latest generated HTML exists at /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/Control_Tower.html
- The current build registry is the live source of truth for Clay state

## 3. Do not overclaim
- Do not present seeded or stale values as live fact
- Do not assume enterprise Clay access is available
- Do not treat Cowork MCP as a full Clay execution surface

## 4. First action of the session
- Re-run the control tower builder and verify the current output
- Re-read the Clay registry before changing any build state
- Choose the next action lane: CLI, MCP, Clay UI, or blocked/manual

## 5. Priority actions
1. Fix the control-tower parser bugs for motion status and blockers
2. Re-verify live Clay state before trusting the tower more deeply
3. Decide the refresh cadence for the control tower
4. Use the Clay handoff prompt for any new workbook work

## 6. One-line operating rule
Treat this session as a head-start build, not a finished system: verify first, execute second, and keep the handoff specific.
