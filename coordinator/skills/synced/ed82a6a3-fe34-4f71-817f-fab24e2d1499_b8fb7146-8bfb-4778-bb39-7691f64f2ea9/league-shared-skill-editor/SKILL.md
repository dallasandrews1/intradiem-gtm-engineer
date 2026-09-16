---
name: league-shared-skill-editor
version: 1.0.0
description: >
  Guides any League employee through improving or editing an existing org
  skill from workspace-agents. Covers how to install the skill locally,
  manage the enterprise vs personal priority conflict, iterate safely, and
  submit a PR back to the org. Trigger when someone says: improve a skill,
  edit a skill, update a skill, fix a skill, change a skill, the skill isn't
  working right, I want to make a skill better, or iterate on a skill.
  Load proactively when someone is working with a skill file and mentions
  wanting to change it.
allowed-tools: Read, Glob
---

# League Skill Editor

You are helping a League employee improve an existing org skill from
`LeagueInternal/workspace-agents`. Your job is to explain the local
iteration workflow, help them make the improvement, and guide them through
submitting it back to the org.

## Important context: the enterprise priority problem

League org skills are provisioned at the **enterprise** level in Claude.ai
and Claude Code. The priority order is: enterprise > personal > project.

This means if a developer copies an org skill to `~/.claude/skills/` under
the same name, the enterprise version wins and their local copy is ignored.

There are two ways to work around this.

## Option A — Toggle and replace (recommended for significant changes)

This gives the developer a clean test environment with no interference from
the live org version.

1. Go to **Settings → Capabilities → Skills** in Claude.ai.
2. Find the skill and toggle it **off**.
3. Copy the skill folder from `.claude/skills/league/[skill-name]/` to
   `~/.claude/skills/[skill-name]/`.
4. Edit the SKILL.md in `~/.claude/skills/[skill-name]/`.
5. Test by starting a new Claude Code session or Claude.ai chat and
   triggering the skill.
6. Iterate until satisfied.
7. When ready, open a PR to `workspace-agents` with your changes.
8. Once the updated org skill is deployed by IT, toggle the org version
   back **on** and delete your local copy.

## Option B — Draft name (recommended for quick experiments)

This lets the developer test without disabling the live version, so they can
compare the two side by side.

1. Copy the skill folder to `~/.claude/skills/[skill-name]-draft/`.
2. Edit the draft version.
3. Test by invoking `/[skill-name]-draft` directly in Claude Code.
4. When satisfied, open a PR to `workspace-agents` using the draft as the
   proposed change.
5. Once the updated org skill is deployed, delete the draft folder.

## Finding the existing skill file

All org skills live in the `workspace-agents` repo:
**https://github.com/LeagueInternal/workspace-agents**

First, ask the contributor: **"Are you comfortable using GitHub, or would
you prefer IT to handle submitting your changes?"**

If they are comfortable with GitHub, the skill they want to edit is at:
```
skills/[function]/[skill-name]/SKILL.md
```
They can browse to it directly in the GitHub UI without installing anything.

If they are not comfortable with GitHub, skip the local iteration steps
below and go straight to the "Submitting without GitHub" section at the
end of this skill.

## What to check before editing

Read the existing SKILL.md carefully. Identify:
- What version it currently is (in the frontmatter)
- What rules exist and whether they use Must/Should/Never correctly
- Whether the description is specific enough about triggers
- Whether `allowed-tools` is properly scoped

## Making the edit

Help the contributor make their change. Common improvements:

**Improving trigger coverage** — The description should over-specify
triggers. If the skill isn't firing when expected, the description is
probably too narrow. Add more trigger phrases and scenarios.

**Adding or clarifying rules** — Each rule must be one sentence with no
ambiguity. If a rule is vague, rewrite it as a concrete Must/Should/Never
statement.

**Adding examples** — Every skill should have at least one ✅ compliant and
one ❌ non-compliant example. If they're missing, help the contributor write
them.

**Scoping allowed-tools** — If the skill has `Bash(*)`, flag this as a
problem. Help narrow it to the specific commands actually needed.

## Bumping the version

After any edit, the version field in frontmatter must be bumped:
- **Patch** (1.0.0 → 1.0.1): fixing a typo, clarifying wording, adding
  examples — no behaviour change
- **Minor** (1.0.0 → 1.1.0): adding new rules or triggers — backwards
  compatible
- **Major** (1.0.0 → 2.0.0): removing rules, changing Must to Should, or
  narrowing triggers — breaking change that may affect users who relied on
  the old behaviour

For major version bumps, remind the contributor to add a `CHANGELOG.md`
entry explaining what changed and why.

## Submitting the changes

### If they are comfortable with GitHub

1. Go to the `workspace-agents` repo:
   **https://github.com/LeagueInternal/workspace-agents**
2. Navigate to `skills/[function]/[skill-name]/SKILL.md` and click the
   pencil icon to edit the file directly in the browser.
3. Make your changes and click **"Propose changes"** to open a pull request.
4. Add a brief description of what you changed and why.
5. The team responsible for that folder will review and approve it.
6. Once merged, post in **#it-support-requests** asking IT to redeploy the
   updated skill. IT will re-upload the ZIP to org settings.
7. After redeployment, if using Option A: toggle the org skill back on and
   delete your local copy.

### Submitting without GitHub

That's completely fine — most people at League don't use GitHub day-to-day.
There are two easy options:

**Option 1 — IT help desk (recommended):**
Submit a request at the IT Service Desk:
**https://everlong.atlassian.net/servicedesk/customer/portal/13**
Paste the updated SKILL.md content into the request, explain what you
changed and why, and ask IT to submit it to the workspace-agents repo.
IT will handle the GitHub steps for you.

**Option 2 — Slack:**
Post in **#it-support-requests** with the updated content and a note
explaining what changed. IT will get it into the repo.

### A note on what a "pull request" is

For contributors who aren't familiar with GitHub: a pull request (PR) is
just a way of proposing a change and asking someone to review it before it
goes live. Think of it like tracked changes in a Word document — someone
reviews your suggestion and either approves it or asks for tweaks. No
technical knowledge required to submit one through the GitHub website.

## Reminders

- Confluence is auto-generated from this repo — never edit Confluence
  directly. The `sync-confluence.yml` workflow updates it on merge.
- Service repos in EverlongProject pin the workspace-agents submodule to a
  git tag. For major version bumps, announce the change in
  **#ai-coding-tools** so teams know to update their submodule pin.
