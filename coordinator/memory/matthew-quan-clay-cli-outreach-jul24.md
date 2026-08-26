---
name: matthew-quan-clay-cli-outreach-jul24
description: Clay's product lead for CLI/API reached out unprompted over Dallas's 600k+ API calls; call scheduled Jul 29 to give feedback in exchange for 3k credits
metadata:
  type: project
---

Matthew Quan (matthew.quan@clay.com), product lead for Clay's CLI/API, emailed Dallas Fri Jul 24 2026 after noticing 600k+ API pings. Offered a 20-min feedback call + 3k Clay credits as compensation. Dallas accepted same day. Call booked via Vimcal: Wed Jul 29 2026, 10:30am CDT / 11:30am EDT, "Matthew Quan <> Dallas Andrews: API/CLI Feedback."

**Why:** unprompted outreach from Clay's own product team = leverage to ask for capability unlocks, not just give feedback. Verified live via `clay --help` (not memory) on 2026-07-24 that `workflows` is the only fully CRUD-able CLI surface (create/get/runs/snapshots); `tables`, `functions`, `workbooks` are read-only (list/get only, no create/edit/delete). That confirms the real ceiling behind most "Dallas has to click this by hand" moments logged across [[clay-motion-self-serve-path]] and [[table-hygiene-agent-jul20]].

**How to apply:** Prep list for the call, ranked by leverage:
1. Table creation via CLI/API (biggest unlock — currently every new motion needs a hand-clicked "Duplicate table")
2. Column create/edit/delete via CLI/API (table-hygiene sweeps find dead columns constantly but there's no delete API — confirmed, not assumed)
3. AI column creation via API (currently 100% UI-only wall, see [[clay-motion-selfserve-path]])
4. Bug report: `clay_table` trigger snapshot pinned to `"latest"` silently stops creating runs, no error — see [[clay-table-trigger-snapshot-pin]]
5. Bug report: `validate_workflow` misses two real runtime failures (agent nodes hang without `automapInputs=false`; `clay_function` tool nodes stall runs) — see [[clay-workflow-execution-gotchas-jul20]]
6. Logistics: how the 3k credits get applied, and whether it's renewable for ongoing bug reports
7. Any roadmap for multichannel steps (LinkedIn, call) inside Campaigns/the native sequencer — currently email-only
8. Confirm/deny: can a Claygent (built via Sculptor/Builder) be invoked from inside a Workflow node, or is Table/Audience really the only deploy target? (Docs only show table/Audience; worth a direct answer rather than inferring)

**Jul 26 addendum:** `clay tables list` now returns `auth_forbidden` — "the public observability API is not enabled for this workspace (available on Enterprise plans)." Worth asking Matthew what exactly sits behind that Enterprise gate versus what's a plain auth/login issue, since it blocks a basic read-only CLI list command.

DROPPED: Clay Audiences ask. Dallas confirmed Jul 24 it's an Enterprise-tier feature, not a workspace toggle — not solvable in this conversation. See correction in [[clay-mcp-audiences-disabled]]. Dallas's real angle: get more of Clay's CLI/API opened up to build/prove ROI faster, which becomes his case to his ELT for the Enterprise-tier spend.

Pre-call email sent to Matthew Jul 24, kept to 2 items (table/column CRUD + snapshot-pin bug) per Dallas's instruction to keep it terse and not over-explain.

Do NOT re-ask for anything already shipped — CLI surface reverified live 2026-07-24, don't rely on stale assumptions going into the call.
