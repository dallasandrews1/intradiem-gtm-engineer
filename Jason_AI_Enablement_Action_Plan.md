# Jason (Manager, AI Enablement) call, Jul 9 2026: action plan

Source: full 24-min transcript. Jason = Speaker 1. Everything below is either something he said he does, something he offered, or something he explicitly asked for.

---

## 1. VS Code moves (what he does that you should adopt)

**1. Make Claude Code in VS Code your daily driver.**
He moved completely to VS Code, even for normal non-code work. Reason: full control over skills, instruction sets, and CLAUDE.md files without the desktop harness. You committed on the call ("I'm gonna start transferring over"). Your repo already has a CLAUDE.md and skills structure, so the switch cost is low.

**2. Build the coordinator-folder architecture.**
His pattern: one central "coordinator" folder holds his memory and core instruction sets. He opens multi-root workspaces in VS Code (coordinator + whatever project he's working on), so memory and context ride along no matter which repo or terminal he's in. Your equivalent: a `coordinator/` repo containing your memory store, master CLAUDE.md, and skills, opened alongside the Intradiem GTM Engineer project.

**3. Install the memory layer (this is the "memory brain" he mentioned: Mem0, said as "Mem Zero").**
What it does for him: Claude constantly updates its own memory after everything it does, never forgets across sessions, windows, or terminals. He built a large memory architecture on top of it.
Use the official Mem0 plugin for Claude Code (verified Jul 2026): MCP server + lifecycle hooks + SDK skill. The hooks auto-load memories at session start, search relevant memories before each message, and store summaries at session end and before compaction. Free tier is 10,000 memories / 1,000 retrievals per month. Exact install steps in the setup guide below.
Docs: [Mem0 Claude Code integration](https://docs.mem0.ai/integrations/claude-code).

**4. Use the CLI-as-connector pattern.**
When Cowork/desktop lacks a connector, he has Claude Code download and drive the vendor CLI directly (his example: Azure App CLI, same day as the call). For you: Salesforce CLI (`sf`) for read-only pulls once access lands, Azure CLI for anything he hosts for you, `gh` for repos.

**5. Auto-accept mode for long builds.**
You raised it yourself on the call: half the work runs unattended in auto mode. Use it for table builds, doc generation, and refactors where the plan is already approved.

**6. Build-for-hosting discipline.**
His hard rule: he cannot host anything that calls Claude at runtime ("you built it to utilize Claude inside your dashboard, so no"). Anything you want hosted for the team must run standalone. Your engines and static dashboards already fit this; keep it that way.

---

## 2. Greenlight approval package (send to Jason)

Timing is on your side: he just shipped document creation, and **skill attachment is the next Greenlight release**, then agents assigned to workflows (orchestrator + sub-agents, e.g. a Salesforce sub-agent with MCP-optimized instructions). He watched JD spend six hours writing one skill, so pre-built skills are a direct pain reliever. He said on the call you can send ideas over and they'll pick and choose.

**Wave 1: sales-team skills (low risk, high demand)**
1. intradiem-objection-handler
2. intradiem-competitive-intel
3. intradiem-roi-business-case
4. intradiem-first-draft-engine + intradiem-copy-sharpener (ship as a pair)
5. intradiem-verified-metrics (prerequisite: this is the claims gate the copy skills depend on; send it first and say so)

**Wave 2: motion/marketing skills**
6. intradiem-signal-to-play
7. intradiem-strike-sequence
8. intradiem-content-engine
9. intradiem-daily-war-room
10. intradiem-launch-kit
11. intradiem-backoffice-icp

**Universal (you demoed both to him on the call and he tracked immediately)**
12. cognitive-calibration
13. strategic-premortem

Keep local, do not send: dallas-brand, naveen-weekly-readout, clay-credit-steward (personal or manager-facing).

**Packaging for each skill:** SKILL.md + one-paragraph plain-language description of what it does for the seller + a sample output. Note in the cover message that every outbound-copy skill carries the verified-claims gate, since unverified numbers in team hands is the obvious objection.

---

## 3. The feature list he explicitly asked for

Direct quote: "if there are certain features that we need to steal from Anthropic to put internal, just let me know. I usually ask people that and I never hear from them again." Sending this within a day or two is a free trust win nobody else delivers on. Suggested list:

1. Projects as agents (scoped instruction sets per workstream; he already uses this pattern himself)
2. Skills attachment (already his next release; offer your skill library as launch content)
3. Persistent memory (the Mem0 pattern, per-user memory in Greenlight)
4. Scheduled tasks (recurring runs: daily war room, Friday readouts)
5. Live artifacts (dashboards that re-pull data on open, without calling Claude at runtime)
6. Sub-agent orchestration (he already plans this; endorse the Salesforce sub-agent idea and offer your engine MCPs as sub-agent backends)
7. Connector catalog with an "ask before you build" flow (mirrors his "do we have a connection to that?" offer)

---

## 4. Requests to route through Jason

**Data connections**
- Ask for access to the **Zuar MCP connection** (beta). Zuar already pulls in Salesforce, ChurnZero, and 6sense into one database, and he pings that instead of fighting Salesforce API limits. This may solve your Salesforce read-only need faster than direct SF access.
- Standing habit he offered: before building any data pull, ask him "do we have a connection to X?"
- Microsoft Graph API MCP is planned (direct login). SharePoint/Confluence are coming later; when they land, scope queries to roughly the last six months because both are full of stale data (his words: five terabytes of garbage).

**Hosting (goes through him: simple browser things → Microsoft Power Apps; involved things → Azure Apps)**
1. gtm-hosted-platform brain (FastAPI container, no Claude at runtime, fits Azure Apps)
2. Static dashboards: control_tower, attribution_dashboard, approval_queue, variant_tracker, deliverability_monitor (Power Apps candidates)
3. clay-build explainer site + function roadmap site (currently on personal Cloudflare/local; moving them internal removes the "lives on Dallas's laptop" risk)
4. Norton pre-read page (after the meeting, if it becomes a standing asset)

**Process**
- Use his **intake form** for every scoping request once it exists. He built it specifically because requests come at him ad hoc; being its first disciplined user makes you easy to help.

---

## 5. Adjacent items you didn't ask about but should do

1. **Enterprise migration prep now, not later.** You described the plan yourself on the call: compartmentalize memory, artifacts, and docs into a zip with a markdown onboarding file, then load it into an Enterprise project on day one of the license. Pre-stage that zip this week so license day is a one-hour ramp, not a rebuild. (Naveen said after Jason dropped: "very close to getting your license.")
2. **Jason relationship cadence.** He ended with "any VS Code questions, let me know." Naveen called the relationship "very important" and GTM engineering formally sits under the AI Enablement initiative (from Jen, board-level). A short recurring sync or async thread with Jason is justified structurally, not just socially.
3. **Naveen's Claude organization.** You promised to help him projectize his threads and markdown files ("can I take some help from you on that sometime?" "Yeah"). Small, fast favor, do it before he asks twice.
4. **Greenlight document creation for exec assets.** He says internal branded doc creation "blows Claude out of the water." Test it for the Norton one-pager or future branded collateral; using his tool on a visible deliverable is another cheap alliance-builder.

---

## Setup guide: step by step

### Already built for you (sitting in this project folder)

- `coordinator/` : the full coordinator folder, Jason's pattern. Contains `CLAUDE.md` (your master instruction set: memory protocol, house style, working conventions), `ONBOARD.md` (the bootstrap prompt), `memory/` (all 34 memory files exported from the Cowork environment, including the index), and `.claude/skills/` (18 skills: all 12 intradiem skills plus cognitive-calibration, strategic-premortem, clay-credit-steward, naveen-weekly-readout, dallas-brand, health-outcomes).
- `coordinator/dallas.code-workspace` : a VS Code workspace file that opens coordinator + this repo side by side with auto-accept edits on by default.
- `greenlight-pack/skills-wave1/` : the six Wave 1 skills plus a README cover note written for Jason. Zip the folder and send it.
- `Enterprise_Migration_Pack.zip` (93 files) : the coordinator zipped for license day. Upload to a new Enterprise project, paste the ONBOARD.md prompt, done.

### Steps on your Mac (about 20 minutes)

**Step 1. Move the coordinator to your home folder** so it lives outside any one project, exactly like Jason's:

```bash
mv "/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer/coordinator" ~/coordinator
```

**Step 2. Install the Claude Code CLI** (the extension bundles its own copy for the chat panel, but you want `claude` in the terminal too):

```bash
curl -fsSL https://claude.ai/install.sh | bash
claude --version
```

**Step 3. Install the VS Code extension.** In VS Code: Cmd+Shift+X, search "Claude Code", Install (needs VS Code 1.98+). Click the spark icon, sign in with your Claude account in the browser. Your personal Max account works now; swap to the Enterprise login when the license lands.

**Step 4. Make the skills and instruction set global** so every workspace gets them, not just the coordinator:

```bash
mkdir -p ~/.claude/skills
cp -r ~/coordinator/.claude/skills/. ~/.claude/skills/
cp ~/coordinator/CLAUDE.md ~/.claude/CLAUDE.md
```

**Step 5. Open the workspace.** File > Open Workspace from File > `~/coordinator/dallas.code-workspace`. That gives you coordinator + the Intradiem repo in one window, permission mode already set to auto-accept edits.

**Step 6. Install Mem0.** Sign up at [app.mem0.ai](https://app.mem0.ai), copy your API key (starts with `m0-`), then:

```bash
echo 'export MEM0_API_KEY="m0-your-key"' >> ~/.zshrc
source ~/.zshrc
```

In the Claude Code panel, run these two commands, then restart the session:

```
/plugin marketplace add mem0ai/mem0
/plugin install mem0@mem0-plugins
```

New session, then run `/mem0:onboard`. The wizard verifies the connection and imports your CLAUDE.md automatically. From then on the lifecycle hooks capture and recall memory on their own; this is the "never forgets" behavior Jason described.

**Step 7. The first prompt** (this is the "prompt to give VS Code"): open `~/coordinator/ONBOARD.md`, paste its contents as your first message. It makes Claude read the master instructions and memory index, confirm what it knows, and flag gaps. After that one message, VS Code Claude has the same brain as this environment.

**Step 8. CLIs for the connector pattern:**

```bash
brew install azure-cli gh
```

Salesforce CLI when read access lands: `npm install -g @salesforce/cli`.

**Step 9. Sanity check.** Ask it: "What are my three Q3 mandates and what's currently gated?" If it answers from memory (15 meetings, 10x throughput, 200 back-office contacts; Wave 1 HOLD pending the customer-exclusion file), you're fully migrated.

### Then the Jason sends

1. Feature list (Section 3): drop it in Slack or email today.
2. Wave 1 skills: `cd "~/Claude/Projects/Intradiem GTM Engineer/greenlight-pack" && zip -r skills-wave1.zip skills-wave1` and send with a two-line note pointing at the README.
3. Ask for Zuar MCP access in the same message.
