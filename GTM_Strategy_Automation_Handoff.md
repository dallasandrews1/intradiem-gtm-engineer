# GTM Strategy and Automation Handoff
Date: 2026-07-18

This document is a durable handoff for the next Claude Code session. It captures what was decided, what was built, what is live, what is still planned, and what remains open. Anything unverified is marked [UNVERIFIED]. The posture here is head start plus ongoing build, not finished-product framing.

---

## 1. GTM STRATEGY

### 1.1 Core strategy

The working strategy in this thread is to treat the Intradiem GTM Engineering workspace as the operating brain for motion build, orchestration, and state visibility, while keeping Clay work grounded in the live tool and in repo-owned source documents.

The core operating posture is:
- use repo docs as the source-of-truth for plans, state, and build order
- use the live Clay tool for actual workbook/workflow state
- keep sends and outbound volume gated until the build is verified
- keep surfaced and realized outcomes separate
- never present seeded or stale data as if it were live fact

### 1.2 Decisions made in this thread

These decisions were made or reinforced in this thread:

1. Control tower as a read-and-render layer
- The control tower is a read-only render layer over existing source files, not a new engine or a new source of truth.
- The intended spine is the existing engine state plus impact, credit ledger, Clay build registry, account plays, and the readout log.
- The tower should surface trust state explicitly rather than silently rendering seeded or stale values as live truth.

2. Clay build discipline
- One motion per workbook is the operating pattern.
- The repo is the spec layer; the live Clay workbook is the authoritative build surface.
- The golden scaffold pattern is the preferred starting point for motion stamping.
- Shared Functions and Claygents are UI-bound work; workflow logic is the local Claude Code lane when the environment supports it.

3. Capability boundary for this environment
- Claude Code CLI is the right place for repo-based prep, local workflow drafting, and planning.
- Cowork MCP is useful for coordination and context, but it is not a full enterprise Clay execution surface.
- Any step requiring higher-access Clay capabilities should be treated as manual Clay UI work or a blocked step rather than assumed to be available.

4. No-send posture while the system is still in build
- The current operating posture is build-first, not launch-first.
- Sends remain at zero by design while the system is still being verified.

5. Verified-claims discipline
- Only verified figures should be used in prospect-facing or leadership-facing claims.
- Unverified or placeholder values should be marked [UNVERIFIED] or surfaced as seeded/stale.

### 1.3 What is decided vs still open

Decided in this thread:
- the control tower should be built as a read-only snapshot renderer over existing files
- the control tower should badge trust state and expose seeded/stale values clearly
- the Clay workbook handoff should be explicit about CLI vs MCP vs UI vs blocked steps
- the strategy agent should help route work from repo docs into the correct execution lane

Still open:
- whether the control tower will stay as a static snapshot or later evolve into a more frequent live refresh model
- whether enterprise Clay access will be available for fuller workbook administration and live UI execution
- whether the open parser bugs in the control tower will be fixed in the next session
- whether the current motion build states should be re-verified live in Clay before the tower is trusted more heavily

### 1.4 Why these choices were made

These choices were made because the workspace already had a strong repo of strategy and build artifacts, but the live build surface and the operating state were still fragmented. The purpose of this thread was to create a more durable handoff and a more honest operating view so the next session could move from planning into execution without pretending the system was already farther along than it actually was.

---

## 2. THE STRATEGY AGENT CREATED

### 2.1 Exact path
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/clay-workbook-builder/SKILL.md
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/clay-workbook-builder/STARTER_PROMPT.md
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/clay-workbook-builder/EXECUTION_MATRIX.md
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/clay-workbook-builder/USE_THIS_PROMPT.md
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/clay-workbook-builder/HANDOFF_NOTE.md

### 2.2 What it does

The strategy agent is a Clay workbook handoff layer. Its purpose is to help the operator move from build planning into the next concrete action without overclaiming what can be done in the current environment.

It is designed to:
- read the repo build-state and motion runbook before acting
- classify the next step into CLI, Cowork MCP, Clay UI, or blocked/manual
- keep the handoff specific and realistic
- avoid pretending the agent can complete enterprise-only Clay work in a non-enterprise environment

### 2.3 How to run or invoke it

Invoke it by using the starter prompt or by referencing the Clay workbook build context in a fresh Claude Code session.

Recommended entry points:
- use the prompt in /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/clay-workbook-builder/STARTER_PROMPT.md
- use the one-line handoff prompt in /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/clay-workbook-builder/USE_THIS_PROMPT.md
- use the handoff note in /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/clay-workbook-builder/HANDOFF_NOTE.md

### 2.4 Inputs and outputs

Inputs:
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/Clay_Build_State_Registry.md
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/Clay_Golden_Standard.md
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/New_Motion_Build_Runbook.md
- the motion-specific build prompt if one exists

Outputs:
- a concise build plan
- a handoff brief for the next action
- a lane split between CLI, MCP, UI, and blocked/manual work
- a risk/constraint note before a build begins

### 2.5 Dependencies

The agent depends on the repo docs and on the current Clay registry state. It does not replace the live Clay truth; it helps interpret it.

### 2.6 Current status

The agent files exist and are ready to use. This is a head-start foundation, not a finished automation layer. It is currently documented and reusable, but it has not been converted into a fully autonomous agent workflow beyond the repo-local skill and prompts.

---

## 3. AUTOMATION ORCHESTRATION

### 3.1 Control tower automation

#### build_control_tower.py
- Path: /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/build_control_tower.py
- What it does: reads the control-tower source files, builds a snapshot, and writes control_tower_state.json
- When it runs: on demand in this session, and via the refresh script or launchd job
- Current status: verified in this session; it ran successfully and wrote /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/control_tower_state.json

#### Control_Tower.html
- Path: /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/Control_Tower.html
- What it does: renders the control-tower snapshot in a browser
- When it runs: on demand via local preview server or by opening the file directly
- Current status: verified in this session; the file exists and the preview route was reachable locally at http://127.0.0.1:8000/Control_Tower.html

#### control_tower_state.json
- Path: /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/control_tower_state.json
- What it does: snapshot payload that the HTML renderer consumes
- When it runs: generated by build_control_tower.py
- Current status: generated successfully during this session

#### .vscode/tasks.json
- Path: /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/.vscode/tasks.json
- What it does: holds VS Code tasks named Preview Control Tower and Refresh Control Tower
- When it runs: manually from VS Code
- Current status: created and present

#### scripts/preview_control_tower.sh
- Path: /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/scripts/preview_control_tower.sh
- What it does: starts a simple local preview server and opens the HTML in the browser
- When it runs: manually when previewing the control tower
- Current status: present; the preview flow was exercised in this session

#### scripts/refresh_control_tower.sh
- Path: /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/scripts/refresh_control_tower.sh
- What it does: reruns the builder and refreshes the preview view
- When it runs: manually when refreshing the control tower
- Current status: present

#### automation/run_control_tower.sh
- Path: /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/run_control_tower.sh
- What it does: wrapper for the builder used by launchd
- When it runs: as a scheduled job
- Current status: present; launchd load status [UNVERIFIED]

#### automation/com.dallasandrews.gtm.controltower.plist
- Path: /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/com.dallasandrews.gtm.controltower.plist
- What it does: launchd definition for the control-tower job
- When it runs: daily at 7:30
- Current status: file exists; launchd registration/load status [UNVERIFIED]

### 3.2 Other scheduled automation jobs

These were also part of the automation layer in this thread:
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/run_war_room.sh
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/run_credit_check.sh
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/run_friday_readout.sh
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/com.dallasandrews.gtm.warroom.plist
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/com.dallasandrews.gtm.creditcheck.plist
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/com.dallasandrews.gtm.fridayreadout.plist

What they do:
- daily war-room sweep
- weekly Clay credit check
- Friday readout draft generation

Current status:
- scripts and plist files are present in the repo
- actual launchd registration and execution status are [UNVERIFIED] in this session

### 3.3 Open control-tower parser bugs

The two open bugs called out in the thread are still relevant and should be treated as open until fixed:

1. Motion build-state reads PLANNED when the registry says BUILT
- This was observed in the generated control_tower_state.json.
- The current parser still maps the motion rows to PLANNED in the snapshot even though the Clay registry says BUILT for the live motions.
- Current status: open

2. Blockers panel misses the fn_email_verified item
- The blockers panel still does not surface the relevant fn_email_verified issue from the Clay registry in the current control-tower parsing flow.
- Current status: open

---

## 4. CURRENT STATE OF THINGS TOUCHED

### 4.1 Motions and workbooks

Current state, as reflected by the repo and the control-tower build:
- Cost-Mandate motion: present in the Clay registry as BUILT; it is treated as a live motion from the registry, but the current control-tower parser still surfaces it as PLANNED in the snapshot [UNVERIFIED in output, but the registry says BUILT].
- Back Office motion: present in the Clay registry as BUILT and used as an install-base archetype.
- WFM-Adjacency motion: present in the Clay registry as BUILT and the workflow build was proven via an acceptance test run.
- Star Ratings motion: still in the build/plan lane relative to the current motion state. It is not the same as a live send-ready motion.

### 4.2 Files created or updated in this thread

Files created or updated in this thread include:
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/build_control_tower.py
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/Control_Tower.html
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/control_tower_state.json
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/.vscode/tasks.json
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/scripts/preview_control_tower.sh
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/scripts/refresh_control_tower.sh
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/run_control_tower.sh
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/com.dallasandrews.gtm.controltower.plist
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/clay-workbook-builder/SKILL.md
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/clay-workbook-builder/STARTER_PROMPT.md
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/clay-workbook-builder/EXECUTION_MATRIX.md
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/clay-workbook-builder/USE_THIS_PROMPT.md
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/clay-workbook-builder/HANDOFF_NOTE.md
- /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/GTM_Strategy_Automation_Handoff.md

### 4.3 What is live vs planned

Live in this session:
- the control tower builder ran and produced a snapshot
- the control tower HTML exists and the preview route was reachable locally
- the Clay workbook handoff docs exist and are ready to use
- the current control-tower snapshot reflects the current repo source state

Planned or not yet fully verified:
- launchd job registration for the automation jobs
- full enterprise Clay access for higher-level workbook/admin actions
- full end-to-end control-tower rendering beyond the current snapshot model
- parser bug fixes for motion status and blocker extraction

---

## 5. OPEN THREADS AND NEXT ACTIONS

### Priority 1: Fix the control-tower parser bugs
- Path: /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/build_control_tower.py
- Why it matters: the current tower does not yet reflect the live Clay registry correctly for motion build status, which undermines the whole honesty layer.
- Next action: update the parser to read the registry status accurately and ensure the blockers panel surfaces the fn_email_verified issue.

### Priority 2: Re-verify the live Clay state before trusting the tower more deeply
- Paths: /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/Clay_Build_State_Registry.md and the live Clay workbook state
- Why it matters: the tower should not over-trust the registry if the live state changed after the last sweep.
- Next action: re-run a live Clay sweep at the start of the next session and update the registry if the live state differs.

### Priority 3: Decide on the refresh cadence and ownership model
- Paths: /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/run_control_tower.sh and /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/automation/com.dallasandrews.gtm.controltower.plist
- Why it matters: the tower is useful only if it is refreshed regularly and tied to a clear schedule.
- Next action: decide whether daily refresh is enough for now, or whether a more frequent refresh model should be introduced later.

### Priority 4: Use the new handoff agent for the next Clay workbook session
- Paths: /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/clay-workbook-builder/SKILL.md and /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/clay-workbook-builder/USE_THIS_PROMPT.md
- Why it matters: the next build session will be less noisy if the handoff is explicit about the lane split.
- Next action: when a new workbook build begins, use the starter prompt and classify the work as CLI, MCP, UI, or blocked/manual before acting.

### Priority 5: Keep the no-send and verification posture intact
- Paths: /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/Clay_Golden_Standard.md and /Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/New_Motion_Build_Runbook.md
- Why it matters: this thread explicitly kept the build in a dry-run posture and that discipline should continue.
- Next action: do not flip send gates or treat seeded numbers as live results.

---

## 6. FINAL NOTE

The work in this thread produced a solid head start: a control-tower scaffold, a reusable Clay handoff framework, and a clearer operating boundary between planning, local execution, and the live Clay surface. The system is not yet finished and should be treated as an ongoing build with several open gaps, especially around parser fidelity and live-state verification.
