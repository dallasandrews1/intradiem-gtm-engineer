# Intradiem GTM Engineer Interview — Full Context Handoff
*Read this completely before responding. This is a context transfer document for a new Claude session.*

---

## The Situation

Dallas Andrews has an interview tomorrow — **June 11, 2026 at 12:00 PM** — for the **GTM Engineer role at Intradiem**. Interviewers: **Naveen Thilagan** (Director Product Strategy, 3 months in role, posted the job himself) and **Cheryl Eckel** (Lead Product Marketing Manager).

Dallas has spent the last 24+ hours building a full interview package from scratch. Everything described below is real, built, and working.

---

## What Dallas Built (All Live)

### 1. PLG Signal Processor (`~/signal_processor.py`)
Python script that processes Intradiem product event data and routes expansion signals. Three hardcoded accounts as demo data: Synchrony Financial (synchrony.com), Centene Corporation (centene.com), CareSource (caresource.com). Produces JSON output with signals_fired, primary_routing (AE/CSM/HOLD), and signal details.

### 2. GTM Signal Engine HTML Artifact
Live interactive dashboard at `/Users/dallasandrews/Library/Application Support/Claude/local-agent-mode-sessions/.../outputs/intradiem-gtm-signal-engine.html` and deployed to Cloudflare. Shows PQL routing logic, ICP scoring model, expansion signals for the three accounts. Sent to Scarlett Caputa (recruiter) before the interview.

### 3. Custom Intradiem MCP Server (`~/intradiem-mcp-server.py`)
Python MCP server built with FastMCP that wraps the signal processor. Exposes two tools:
- `get_expansion_signals(domain)` — returns expansion signal status for any monitored account
- `list_monitored_accounts()` — lists all monitored accounts

**Status: LIVE AND WORKING.** Connected to Claude Desktop via `claude_desktop_config.json`. Runs using venv Python at `~/.venvs/intradiem/bin/python`. The tools are callable right now — `mcp__intradiem-signals__get_expansion_signals` and `mcp__intradiem-signals__list_monitored_accounts`.

**To run manually:** `~/.venvs/intradiem/bin/python ~/intradiem-mcp-server.py stdio`

**Claude Desktop config location:** `~/Library/Application Support/Claude/claude_desktop_config.json`
The mcpServers entry is already written and working.

### 4. ICP Clay Table (`/outputs/intradiem-icp-clay-table.csv`)
20 target accounts pre-enriched with ICP scores, ACD systems, employee count, tier classifications. Built using Apollo MCP during the session.

### 5. Clay Table Setup Guide (`/outputs/clay-table-setup-guide.md`)
Step-by-step guide for building the 3-table Clay architecture at Intradiem.

---

## Files in Working Folder (`/outputs/`)

- `interview-prep-naveen.md` — primary interview prep document (MOST IMPORTANT)
- `clay-mastery-intradiem.md` — complete Clay reference for this role
- `intradiem-teardown.md` — company intelligence, product gaps, GTM weaknesses
- `signal_processor.py` — the Python signal processing logic
- `intradiem-gtm-signal-engine.html` — the live artifact
- `intradiem-icp-clay-table.csv` — 20 enriched ICP accounts
- `clay-table-setup-guide.md` — Clay build instructions
- `scarlett-email.md` — the email sent to recruiter (already sent)

---

## Clay Architecture (Critical to Know)

### Three-Table Structure
**Table 1 — ICP Accounts:** The core scoring model. Columns: Company ID group (name, domain, HQ, employee count, revenue, industry), Contact Center Infrastructure (ACD system via BuiltWith/Claygent, WFM system, cloud provider), Pain Signals (WFM job postings, intent, recent news), ICP Scoring (formula columns: tech stack score 0-25, pain score 0-25, size score 0-25, timing score 0-25, total 0-100, tier label). THIS IS essentially what Dallas built as the prototype — add domain column and ACD/WFM columns to the existing scoring model.

**Table 2 — Contacts:** Separate table. Decision makers per account. Lookup column back to Table 1 via domain. Columns: name, title, email (waterfall: Apollo→Lusha→Hunter→Kaspr), phone, LinkedIn URL, recent post.

**Table 3 — Expansion Signals:** Fed by Intradiem's product event stream. Lookup to Table 1 via domain for account context, Lookup to Table 2 for AE owner. This is where the signal processor output eventually lands.

**Lookup columns** are the connection mechanism between tables — "find row in Table X where domain matches, return field value." Domain is the shared key across all three tables.

### Clay MCP — CRITICAL DIRECTION
Clay built itself as an **MCP SERVER**. Claude/ChatGPT are the **clients**. Connecting Claude Desktop to Clay gives Claude access to all 150+ enrichment providers as callable tools. This is NOT Claygent calling a custom server — it's Claude calling Clay.

**The three-MCP distinction for the interview:**
1. **Apollo MCP** — used to BUILD the prototype (Claude called Apollo during construction)
2. **Clay MCP** — Claude can call Clay's entire enrichment stack from any conversation (connected in Clay Settings → MCP → Connect next to Claude)
3. **Custom Intradiem MCP** (`intradiem-mcp-server.py`) — wraps Intradiem's product event stream so Claude/Clay can query live expansion signals as a tool call

All three use the same protocol. Three different servers, three different layers, three different problems.

### Waterfall Enrichment
Sequential provider chain — Apollo→Lusha→Hunter→Kaspr. Stops at first valid result. Apply to every email/phone column. Never run providers simultaneously on the same column (pays twice for one result).

### Day-1 Tool Stack
Must have: Apollo (firmographics + contacts + sequences), BuiltWith (ACD/WFM tech stack detection)
Push for: LinkedIn Sales Nav, Bombora intent data
Nice to have: ZoomInfo (as waterfall fallback if already owned)

---

## About the Role and Company

**Intradiem** — 30-year-old Atlanta enterprise software company. Sells real-time workforce automation to contact centers (500+ agents). Core product: Dynamic Workforce Orchestration. Sits between ACD (Genesys, Five9, Avaya) and WFM (Verint, NICE, Calabrio), acts in the idle seconds between scheduled events.

**Key numbers to know cold:** 114% NRR, NPS 71, eNPS 79, <1% churn, 7x ROI/3-month payback, record net new bookings 2024 AND 2025, 250,000+ agents on platform.

**Why GTM Engineer NOW:** Platform modernized in 2025 (data architecture now supports signal routing). Two consecutive record years create scaling pressure. Naveen 3 months into Director mandate that blocks on this hire. 250,000+ agents generating product data daily with NO systematic expansion motion.

**WFM and ACD are prerequisites, not competitors.** Verint/NICE/Calabrio = WFM (scheduling layer). Genesys/Five9/Avaya = ACD (call routing layer). Intradiem acts in the gap between them. Never position them as competitive.

**The moat in one sentence:** "WFM systems tell you what agents should be doing. Intradiem acts on agents in the idle seconds between scheduled events — the gap WFM never addresses."

---

## Interview Prep — Key Points for Naveen

**Naveen thinks like a PM:** instrumentation, activation events, funnel stages, product signals. Not AE routing. Engage him as a peer. Ask what he ran into when instrumenting PLG in his Sr PM role.

**The three questions he'll ask:**
1. "How would you actually get the data?" → CSV export + Python cron job is day-1 honest answer. 90-day state is live API. Don't claim live API exists on day one.
2. "What does success look like at 60 days?" → Two signals instrumented with baselines, one AE has actioned one signal in pipeline, clear data map of what's natively available vs. what needs building.
3. "How do you think about free trial / self-serve?" → Completely different architecture (Segment/Mixpanel). Expansion motion uses existing event stream. These are two separate workstreams with different milestones. Ask which Naveen is prioritizing.

**The 60-day milestone made concrete:** "Day 45 is one validated signal in the pipeline. Day 60 is that same signal firing automatically every morning and landing in the AE's workspace before they open Salesforce. That's the difference between a proof of concept and an operating motion."

**What Not to Say:**
- Don't say "I used MCP" without specifying which of the three servers
- Don't say Verint/NICE are competitors
- Don't claim live API access on day one
- Don't say "figure out" the data sourcing — say "map it in the first two weeks"

---

## Interview Prep — Key Points for Cheryl

Cheryl is NOT a culture screen. She's evaluating whether Dallas can bridge product and marketing without her translating.

**Key answer for her:** "Every expansion signal that fires is a proof point. Synchrony hitting 88% seat utilization means the product worked so well they ran out of room. That's a case study seed, not just a sales alert. If I'm routing that signal to an AE, I'm also flagging it to marketing as a 'this customer is achieving the outcome we promise.' The best GTM engineering feeds both the sales pipeline and the proof point library at the same time."

---

## The Behavioral Story — "Built From Scratch Under Pressure"

**PRIMARY STORY: The League Cowork Build.** NOT the Intradiem artifact.

WHAT DIDN'T EXIST: League had no AI-native GTM infrastructure. Research was manual, cold email was written from scratch, call transcripts processed by hand, MEDDPICC hygiene was a Slack thread.

WHAT YOU BUILT: A complete GTM operating system in Cowork — 30+ skills covering the full AE workflow end to end:
- Intelligence layer: daily war room (24-72hr signal scan), tech radar (weekly infra sweep), app audit (iOS/Google Play review mining), AE briefing (strike packet with forcing function + hidden fear)
- Pre-call layer: AE initializer (session constraints), pre-call planner (full disco prep with L1/L2/L3 pain maps for 8+ C-suite personas)
- Outreach layer: first-draft-engine → copy-sharpener → cold-call-playbook → holistic-roadmap (full buying committee, 10-16 contacts) → full-pipeline (7-phase autonomous orchestrator)
- Post-call layer: ae-call-transcript (produces MEDDIC scorecard + SF activity + follow-up in one run), post-discovery, meddpicc hygiene pass
- Deal layer: CFO business case, Accord MAP, objection handler, deal desk
- Quality/meta layer: cognitive-calibration (pre-execution failure scan from 50+ documented failures), verified-metrics, skill creator/editor/reviewer (self-replication layer)

WHAT BROKE: [Dallas fills in — name the real thing that failed]
WHAT SHIPPED: Full League AE Deal Accelerator, live, team uses it daily, Apollo MCP connected for live enrichment
OUTCOME: [Dallas fills in — specific number]

The Intradiem artifact is a SECOND story or a close: "I had 48 hours, no brief, no existing infrastructure. I built a PLG signal processor, an ICP scoring model, a custom MCP server, and a live enrichment run. That's what day 30 looks like if you give me a starting point."

---

## Dallas's No-Brainer Argument

The sell is that Dallas has already built three types of agentic behavior working together in production at League:
1. **Autonomous scheduled agents** — daily war room, tech radar fire on cron without any user trigger
2. **Orchestration agents** — full-pipeline runs 7 phases sequentially, multi-tool, user-triggered but fully agentic
3. **MCP-connected agents** — Apollo MCP for live enrichment called mid-workflow

Most GTM Engineer candidates describe these things. Dallas has shipped them, the team uses them daily, and he has outcome numbers. The custom Intradiem MCP server (built last night) is the 90-day architecture already prototyped. No other candidate walks in having already built that.

**The Claude/Cowork pitch for the interview:** "The reason Cowork matters for this role is that it's the difference between GTM engineering as a project and GTM engineering as an operating system. A project is something you build and hand off. An operating system runs continuously, updates when data changes, and makes the team faster every week without additional headcount."

---

## The 90-Second Opening (If They Haven't Seen the Artifact)

"Before we dive in — I put together a live GTM Signal Engine specifically for Intradiem before this conversation. It's a PLG signal routing framework for expansion signals across the existing install base, plus an ICP scoring model for net-new targets. I can pull it up on screen if it's useful context, or I can describe what I built and we can go from there. Either way, I want to make sure the conversation is grounded in something concrete, not just what I'd do in theory."

---

## The Close Question

"You've been inside the product for four years and you're now taking Dynamic Workforce Orchestration to market as the core positioning. What's the gap in the current GTM motion that this role is designed to close — is it the expansion signal infrastructure, the net-new pipeline instrumentation, or something else I haven't accounted for?"

---

## GitHub

Dallas has 9 repos built in ~1 month. When asked: this is a velocity signal, not an inexperience gap. "Joined last month" + 9 repos = builder who ships. Don't volunteer the timeline. If asked, frame it as: "I started building publicly when I started building seriously."

---

## What's Still TODO Before 12pm

- [ ] Fill in WHAT BROKE and OUTCOME fields in the behavioral story (you know the real answers)
- [ ] Read interview-prep-naveen.md, clay-mastery-intradiem.md, intradiem-teardown.md
- [ ] Have the artifact URL ready to share on screen
- [ ] Be prepared to demo the MCP server live: "list my monitored accounts" → "get expansion signals for synchrony.com"
