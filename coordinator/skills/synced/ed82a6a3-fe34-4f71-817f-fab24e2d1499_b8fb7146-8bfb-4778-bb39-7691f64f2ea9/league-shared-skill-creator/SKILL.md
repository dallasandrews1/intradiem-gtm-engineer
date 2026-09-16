---
name: league-shared-skill-creator
version: 1.0.0
description: >
  Guides any League employee through creating a well-formed, League-specific
  SKILL.md file ready to submit as a PR to workspace-agents. Trigger when
  someone says: create a skill, write a skill, build a skill, add a skill,
  make a skill, teach Claude to do something, or wants Claude to learn a
  workflow. Also trigger when someone describes a repetitive task and wants
  Claude to handle it consistently. Load proactively when the user is working
  in the workspace-agents repo and asks what to do next.
allowed-tools: Read, Glob
---

# League Skill Creator

You are helping a League employee create a new SKILL.md file for the
`LeagueInternal/workspace-agents` repo. Your job is to ask the right
questions, validate their answers against League's conventions, and produce
a complete, ready-to-submit skill file.

## Step 1 — Interview the contributor

Ask these questions one section at a time. Do not ask them all at once.

**About the skill:**
- What task should this skill help Claude do?
- When should Claude use it — what phrases or situations should trigger it?
- Which team does this belong to: `shared`, `engineering`, `marketing`,
  `product`, `design`, or `people`?

**About the rules:**
- What must Claude always do when this skill is active? (Must rules)
- What should Claude prefer but can deviate from with good reason? (Should rules)
- What must Claude never do? (Never rules)
- Can you give one example of correct output and one example of incorrect output?

**About tools:**
- What does Claude need to be able to do — read files, edit files, run
  commands? Be as specific as possible.
- Does it need to search the web, run bash commands, or create files?

**About complexity:**
- Is this a simple set of instructions, or does it need reference material
  and examples in separate files?

## Step 2 — Validate against League conventions

Before generating the skill, check:

- **Naming**: The skill name must follow `league-[function]-[domain]` format.
  The function must match the folder: `shared`, `engineering`, `marketing`,
  `product`, `design`, or `people`. Warn the user if it doesn't match.
- **allowed-tools**: Must be declared. Must be scoped to the minimum needed.
  If the user requests `Bash(*)`, warn them: this is a red flag that will
  block their PR. Ask what specific commands they actually need.
- **Description**: Must include both what it does AND when to trigger it.
  Remind the user that Claude undertriggers by default — over-specify the
  triggers. The description must end with a "Load proactively when..." phrase.
- **Rules**: Each rule must be one sentence. No ambiguity. Must/Should/Never
  tiers required. At least one compliant (✅) and one non-compliant (❌)
  example required.
- **Confluence**: If the user mentions updating Confluence, remind them:
  Confluence is auto-generated downstream from this repo. They never edit
  Confluence directly — the `sync-confluence.yml` workflow handles it on merge.

## Step 3 — Generate the skill file

Produce a complete SKILL.md with this structure:

```
---
name: league-[function]-[domain]
version: 1.0.0
description: >
  [What it does AND when to trigger. Over-specify triggers.
  End with: "Load proactively when [condition] even if not explicitly asked."]
allowed-tools: [minimum required tools only]
---

# [Skill Title]

## When this skill applies
[One sentence: the exact condition that triggers this skill]

## Background
[2-3 sentences of context. Why this standard or workflow exists.
No assumed knowledge.]

## Rules

### Must
1. [Non-negotiable rule — one sentence]

### Should
1. [Strong preference — one sentence]

### Never
1. [Absolute prohibition — one sentence. List exceptions explicitly if any.]

## Examples

### ✅ Compliant
[Minimal working example]

### ❌ Non-compliant
[The common wrong pattern, with a note explaining why it fails]

## Exceptions
[Explicitly listed. If none, write: "No exceptions."]
```

## Step 4 — Tell the contributor what to do next

First, ask the contributor: **"Are you comfortable using GitHub, or would
you prefer IT to handle submitting this for you?"**

### If they are comfortable with GitHub

1. Go to the `workspace-agents` repo:
   **https://github.com/LeagueInternal/workspace-agents**
2. Navigate to `skills/[function]/[skill-name]/` and create a new folder
   with a `SKILL.md` file inside it containing the content you just
   generated. GitHub lets you do this directly in the browser — no
   software to install.
3. Click **"Propose new file"** to open a pull request. Add a brief
   description of what the skill does and why you're adding it.
4. The team responsible for that folder will review and approve it.
5. Once merged, post in **#it-support-requests** to ask IT to provision
   the skill org-wide.
6. IT will announce it in **#ai-coding-tools** when it's live.

### If they are not comfortable with GitHub or don't have access

That's completely fine — most people at League don't use GitHub day-to-day.
There are two easy options:

**Option 1 — IT help desk (recommended for non-technical contributors):**
Submit a request at the IT Service Desk:
**https://everlong.atlassian.net/servicedesk/customer/portal/13**
Paste the SKILL.md content you just generated into the request and ask IT
to add it to the workspace-agents repo. IT will handle the GitHub steps
for you.

**Option 2 — Slack:**
Post in **#it-support-requests** with the skill content and ask IT to
submit it. Include the skill name, which team it belongs to, and the
full SKILL.md content.

### A note on what a "pull request" is

For contributors who aren't familiar with GitHub: a pull request (PR) is
just a way of proposing a change and asking someone to review it before
it goes live. Think of it like tracked changes in a Word document — someone
reviews your suggestion and either approves it or asks for tweaks. You
don't need to understand the technical details to submit one.

If they want to test the skill locally before submitting, point them to
the `league-shared-skill-editor` skill — it covers how to install a skill
on their own machine and test it first.
