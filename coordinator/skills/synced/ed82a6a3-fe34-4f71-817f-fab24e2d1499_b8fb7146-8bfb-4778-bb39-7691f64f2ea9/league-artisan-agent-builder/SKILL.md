---
name: league-artisan-agent-builder
version: 1.0.0
description: >
  Builds two copy-paste-ready Artisan (Ava) AI sales agents per target account — Digital Engagement (CIO/CTO/VP Digital) and Health Engagement (CMO/VP Pop Health/VP Quality). Gathers intelligence from Salesforce, Slack opportunity channels, web research, and project files, populates templates, verifies metrics, runs pre-mortem, and delivers final output. Trigger on: "build artisan agents for [account]", "create agents for [account]", "artisan build", "set up outreach agents", "build ava agents", "run the artisan pipeline", or any mention of Artisan/Ava agents with an account name. Load proactively when discussing a new target account that lacks agents.
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, WebSearch, Agent
---

# Artisan Agent Builder

Build two copy-paste-ready Artisan (Ava) agent configurations for a target
account — Digital Engagement and Health Engagement — using the full 8-step
build order.

## Why two agents per account

Artisan's Ava engine uses a "Personalization Waterfall" that dynamically
selects which pain point, proof point, and CTA to assemble per email. It
does not guarantee persona-matched combinations. The two-agent architecture
solves this by ensuring every pain point within a single agent is valid for
every persona in that agent's buying committee. Digital personas (CIO, CTO,
VP Digital, VP Member Experience) share technology and experience pain
points. Health personas (CMO, VP Pop Health, VP Quality, VP Behavioral
Health) share clinical and quality measure pain points. This way, any
random combination Ava assembles is coherent regardless of which prospect
receives it.

## Why this matters for copy quality

Artisan operates in Copilot mode for Dallas's campaigns — every email is
reviewed before sending. But the agents do the heavy lifting of generating
the first draft. If the pain points, proof points, and CTAs are not
account-specific, clinically grounded, and metrically verified, the
Copilot review becomes a rewrite instead of an approval. The quality of
what goes INTO Artisan determines the quality of what comes OUT.

## Reference files

These files are your source material. Read them before starting any build.

- **Templates:** `Growth Enablement Manager Campaign/Artisan_Account_Level_Templates.md`
  The reusable template with placeholder fields for both Digital and Health agents.
  Contains the full coaching point stack (subject lines, message body, LinkedIn)
  which is PORTABLE — copy exactly as written, only adjusting persona-specific
  references and account-specific system names in Points 2, 3, and 8.

- **Golden example — Digital:** `Growth Enablement Manager Campaign/Artisan_BCBSNC_Digital_Engagement_Agent.md`
  BCBS NC's Digital agent. Study the tone, specificity level, pain point
  construction, and how account intelligence maps to template fields.

- **Golden example — Health:** `Growth Enablement Manager Campaign/Artisan_BCBSNC_Health_Engagement_Agent.md`
  BCBS NC's Health agent. Note how clinical language differs from digital,
  how proof points emphasize outcomes over architecture, and how CTAs
  reference clinical programs.

## The 8-step build order

Execute these steps in sequence. Do not skip steps or reorder them.

### Step 1: Intelligence gathering

Gather everything before writing anything. This is the most important step.
Thin intelligence produces generic agents that sound like every other vendor
email. Rich intelligence produces agents that make the prospect feel like
you understand their organization.

#### 1a. Salesforce
Pull the account record, all open opportunities (stage, ARR, close date),
all closed-lost opportunities (with loss reasons and dates), recent tasks
and activity notes, and all contacts with titles. Use `league-salesforce`
tools: `get_account`, `search_opportunities`, `get_opportunity`,
`get_tasks_by_account`, `search_contacts`.

Key things to extract:
- Current opportunity stage and ARR
- Account owner (AE name)
- How many times League has lost here and why
- Which contacts are already in Salesforce
- Last meaningful activity date

#### 1b. Slack opportunity channel
Search for `#opportunity-[account-name]` using Slack search tools.
Read the FULL channel history. This channel contains AE conversations,
Momentum call summaries, prospect objections, build-vs-buy discussions,
League Connect attendance, post-event follow-ups, and internal strategy
notes. The opportunity channel often contains the single most important
piece of intelligence for the entire build — things like "they tried to
build internally and it failed" or "the CTO said they want to evaluate
external platforms in Q2."

If the channel does not exist, search for variations: `#opp-[name]`,
`#deal-[name]`, or search public channels for the account name.

Also search `#team-core-sales` and `#growth-team` for mentions of the
account.

#### 1c. Web research
Run fresh searches on:
- "[Account name] leadership changes [current year]"
- "[Account name] technology investments healthcare"
- "[Account name] digital transformation OR member experience"
- "[Account name] app store ratings" (check iOS and Google Play)
- "[Account name] financial results OR earnings"
- "[Account name] regulatory OR CMS OR Star ratings"
- "[Account name] M&A OR acquisition OR partnership"
- "[Account name] job postings VP OR Director OR Chief"

Job postings are a leading indicator of strategic priorities. A posting for
"VP Digital Health" means they are investing in digital. A posting for
"Director Star Ratings" means they are worried about quality measures.

#### 1d. Project files
Check the workspace for:
- Daily signal scans mentioning this account
- Warm path reports
- Prior roadmaps or strike packets
- Master account list entry
- Any prior Artisan agents already built for this account

#### 1e. App store audit (optional)
If the account has a consumer-facing mobile app, pull iOS and Google Play
ratings. Extract 1-star and 2-star complaint themes. This feeds directly
into Digital agent pain points.

### Step 2: Map the buying committee

Split all identified contacts into two buckets:

**Digital Engagement** — CIO, CTO, CDO, SVP/COO, VP Digital Health,
VP Member Experience, VP Digital Strategy, Director Digital Transformation,
Director Strategic Portfolio Management, Head of Digital Products

**Health Engagement** — CMO, Chief Medical Officer, VP Population Health,
VP Clinical Operations, VP Quality, VP Behavioral Health, Medical Director,
Director Utilization Management, Director Care Management, Director Health
Programs, Chief Nursing Officer, VP/SVP Government Programs, Director Star
Ratings

Target 3-5 contacts per agent. If you have fewer than 3 for one agent,
supplement with web research (LinkedIn, press releases, organizational
charts).

Flag any contacts with warm signals: League event attendance, LinkedIn
engagement, inbound inquiries, or recent Salesforce activity.

### Step 3: AE coordination check

Identify the account owner from Salesforce (Andrea Puckett or Phil).
Note in the output which contacts are in active AE dialogue based on
Salesforce tasks and Slack channel activity. These contacts MUST be
EXCLUDED from Artisan campaigns to avoid cold outreach colliding with
warm engagement.

Mark excluded contacts clearly: "[EXCLUDED — active AE dialogue as of
[date]]"

### Step 4: Populate both templates

Read the template file and fill in every placeholder field using the
intelligence gathered in Steps 1-3.

For each agent, write:

**One Sentence Offering Description** — Customize with the account's
actual admin system (Facets, QNXT, HealthEdge, Epic), named apps or
portals, and core systems.

**Features (4-5 pain points)** — Each pain point must:
- Name specific systems, programs, populations, or events at THIS account
- Be valid for EVERY persona in that agent's buying committee
- Follow the 2-4 sentence structure: what is happening, why it hurts, what
  the cost of inaction is
- Connect to a solution with verified metrics (numbers AND timelines)

**Proof Points (7-9)** — Select from the League Value Repository based on
which metrics resonate most with this account's specific pains. Every proof
point must include a number AND a timeline. Source from verified metrics
skill.

**CTAs (10-14)** — 8-11 portable CTAs from the template plus 2-3
account-specific CTAs that reference named programs, populations, or
situations unique to this account.

**Coaching Points** — Copy the portable coaching points from the template.
Adjust Points 2, 3, and 8 in each section to reference this account's
specific systems, metrics, and clinical programs.

### Step 5: Verify metrics

Invoke the `league-verified-metrics` skill (read its SKILL.md). Every
number cited in pain points, solutions, proof points, and CTAs must be
traceable to the League Value Repository Q1 2026. Check:

- 1:1 vs 1:many approval tiers — if a metric is approved only for 1:1
  conversations, it cannot appear in a mass outreach agent
- Named vs. blinded customers — only SCAN, Santa Clara, and Baptist
  Health are logo-approved. All others must be blinded as "one comparable
  plan" or "a [plan type] plan"
- No fabricated or blended metrics — if you cannot find a specific number
  in the repository, do not use it

### Step 6: Combinatorial coherence check

For each agent, mentally test every combination:
- Each pain point × each proof point × each CTA
- For each combination, ask: "If this fires for Persona X, does it make
  sense?" Run through at least 2 personas per agent.

Flag any combinations that produce incoherent or mismatched emails. If
more than 30% of combinations are problematic, the pain points are too
narrow. Either broaden them or reduce to 3-4 pain points.

### Step 7: Pre-mortem

Run the `strategic-premortem` skill on both agents together. Check for:

1. **Random assembly mismatches** — combinations that produce embarrassing
   or incoherent emails
2. **Unverified metrics** — numbers that slipped through Step 5
3. **Persona coverage gaps** — pain points that only work for 1-2 personas
   out of the 4-5 in the buying committee
4. **Closed-lost antibodies** — if League has lost at this account before,
   the agents must acknowledge and work around the likely objections
5. **AE conflict risk** — warm contacts accidentally included in cold
   outreach
6. **Artisan platform mechanics** — coaching points that assume behaviors
   Ava does not actually support

### Step 8: Resolve and finalize

Fix every issue the pre-mortem surfaced. Then produce two final markdown
files — one per agent — ready to copy/paste into Artisan's agent
configuration screen. Each file should be a complete, standalone document
matching the format of the BCBS NC golden examples.

Save both files to the workspace:
- `Growth Enablement Manager Campaign/Artisan_[ACCOUNT_SHORT]_Digital_Engagement_Agent.md`
- `Growth Enablement Manager Campaign/Artisan_[ACCOUNT_SHORT]_Health_Engagement_Agent.md`

## Rules

### Must

1. Read all three reference files (templates + both golden examples) before starting any build.
2. Search the Slack opportunity channel for the account — this is where the highest-value intelligence lives.
3. Verify every metric against the League Value Repository before including it in an agent.
4. Produce two separate agent files (Digital + Health) as final output.
5. Run the pre-mortem before delivering final output.
6. Exclude any contacts in active AE dialogue from the Artisan buying committee.
7. Include a number AND a timeline in every proof point and every social proof reference in coaching points.
8. Keep pain points to 4-5 per agent, and every pain point must pass the swap test (valid for every persona in that agent's committee).

### Should

1. Target 3-5 contacts per agent buying committee, supplementing with web research if Salesforce has fewer than 3.
2. Include 2-3 account-specific CTAs beyond the portable template CTAs.
3. Flag warm signals (event attendance, LinkedIn engagement, inbound inquiries) on buying committee members.
4. Note closed-lost history and how the current agents account for prior objections.
5. Run the app store audit for accounts with consumer-facing mobile apps — the complaint themes feed directly into Digital pain points.

### Never

1. Never fabricate metrics or blend two verified ranges into an unverified one (e.g., "$7-$9" and "$8-$15" do not become "$7-$12").
2. Never include a contact who is in active AE warm dialogue in the Artisan buying committee.
3. Never name a League customer in the agents unless they are logo-approved (SCAN, Santa Clara, Baptist Health only).
4. Never skip the Slack opportunity channel search — even if web research feels sufficient, the channel often contains deal-critical intelligence that exists nowhere else.
5. Never copy coaching points from the golden examples instead of the templates — the templates are the canonical source; the examples are illustrations of how they look when populated.
6. Never deliver agents without running the pre-mortem first.

## Examples

### Correct output structure

```
# [Account Name] — Digital Engagement Agent

**Account:** [Full legal name]
**Salesforce ID:** [ID]
**Owner:** [AE name]
**Open Opportunity:** [Opp name] — [Stage] — $[ARR] — Close [date]
**Last SF Activity:** [date]
**Closed-Lost History:** [count] prior opportunities ([years])
**Employees:** ~[count] | Headquarters: [city, state]

**Target personas:** CIO, CTO, VP Digital Health, VP Member Experience...

**Buying committee for this agent:**
- [Name] — [Title] ([date/context] — [why they matter to League])
- [Name] — [Title] ([date/context] — [why they matter])
...

## One Sentence Offering Description
[Account-specific, names their systems]

## Features (Pain Point / Solution Pairs)
### Feature 1: [Named, account-specific pain]
**Pain Point:** [2-4 sentences with named systems, events, metrics]
**Solution:** [2-3 sentences with verified metrics, numbers + timelines]
...

## Proof Points
### Proof Point 1
[Verified metric with number AND timeline. Source: Value Repository Q1 2026]
...

## Ava Coaching Points: Email Subject Line Coaching
[Portable from template, Points 2/3 adjusted for this account]
...

## Calls to Action
[10-14 CTAs, 2-3 account-specific]
...
```

### Common mistakes

**Too generic:** "Health plans struggle with member engagement" —
this could apply to any plan. Must name the account's specific
situation: "Blue Cross NC insourced Healthy Blue D-SNP administration
from Elevance in January 2026, expanding Medicare operations across
all 100 North Carolina counties without a digital engagement layer
for the incoming population."

**Unverified metric:** "Plans see 14x annual value from engaged
members" — this number does not exist in the Value Repository.
The verified metric is "digitally engaged members are 3x more
likely to renew."

**Persona mismatch:** A pain point about "OpenShift containerization
of 250+ applications" works for a CTO but not a VP Member Experience.
Either broaden it ("the infrastructure investment has not translated
to member-facing experience improvements") or move it to a
supplementary note outside the agent.

**Skipped opportunity channel:** Building agents from web research
alone missed that the account "tried to build internally and it
failed" — intelligence that completely changes the competitive
positioning from "why external" to "you already proved external
is the path."

## Exceptions

If the account has no Slack opportunity channel and no Salesforce record,
this is likely a net-new account with no League history. In this case:
- Skip Steps 1a and 1b
- Increase web research depth (add LinkedIn Sales Navigator scan if
  available via Chrome)
- Note in the output header: "NET-NEW ACCOUNT — no prior League
  engagement history"
- The pre-mortem should focus on cold-outreach-specific risks rather
  than closed-lost antibodies
