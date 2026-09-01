# Greenlight agents register

Shared Greenlight agents packaged from the GTM Engineering skill library, so anyone at Intradiem without Claude access gets the same output. Each folder holds `AGENT_INSTRUCTIONS.md` (paste into the agent's instructions field, self-contained, no local tooling) and `AGENT_CARD.md` (name, gallery description, who it is for, knowledge files, conversation starters, what it will not do).

Greenlight is powered by Claude. Agents there carry an instructions field, attached knowledge files, optional Actions (Salesforce read, Confluence, Slack), and conversation starters. Owner shows as the creator's email.

## The agents

| # | Agent | Folder | For | Nearest existing Greenlight agent | Knowledge files |
|---|---|---|---|---|---|
| 1 | Prototype builder | `prototype-builder/` (instructions in `../pm_kit/PROJECT_INSTRUCTIONS.md`) | Product managers | MikeG_PRD_HelperAgent answers questions about a PRD; this one builds the screen from it. Complementary. | `pm_kit/DS_Tokens.md`, `pm_kit/Prototype_Brief_Template.docx` |
| 2 | Reply handler | `reply-handler/` | Sales reps, BDRs | Roleplay Agent is practice; this drafts the reply to a real objection. No overlap. | Value Repository (required), Customer Value Registry (optional) |
| 3 | Competitive Intel | `competitive-intel/` | AEs, AMs, SEs, product marketing | None. | Value Repository (required) |
| 4 | Business Case Builder | `business-case/` | AEs, SCs, CS leads before an Economic Buyer meeting | Customer Call Insights Assistant and ConvoIQ summarize a call; this turns the numbers in it into the one-page economic case. Complementary: paste their summary in. | Value Repository (required), Customer Value Registry (optional) |
| 5 | Signal to Play | `signal-to-play/` | Sellers, AMs, demand gen | Earnings Call Analyzer surfaces the signal; this turns one signal into the campaign brief, the alert, and the outreach draft. Complementary. | Value Repository (required) |
| 6 | Outreach Writer | `outreach-writer/` | Sellers, SDRs, AMs | VITO Messaging Assistant (Josh Wilkins) researches a company and writes VITO messages. This one drafts from what you paste, runs the verified-claims gate, and enforces the house CTA style. Talk to Josh before publishing so the two are positioned, not competing. | Value Repository (required), Customer Value Registry (optional) |
| 7 | Content Repurposer | `content-repurposer/` | Marketing, content, enablement | 12-40-30 (messaging alignment) is a voice guide; this produces the channel set from one asset. Complementary. | Value Repository (required) |
| 8 | Pre-Mortem | `pre-mortem/` | Anyone before a hard-to-reverse move | None. | None |

## Create order

1. Prototype builder (Product goal, first PM pairing depends on it).
2. Pre-Mortem (no knowledge file, no gate dependency, useful to everyone, safe to publish today).
3. Competitive Intel and Reply handler (highest seller pull; internal-only or draft-only output).
4. Business Case Builder and Signal to Play.
5. Outreach Writer (after the VITO conversation with Josh) and Content Repurposer.

## Before the seller-facing agents ship

The verified-claims gate in agents 2 to 7 points at the attached `Intradiem_Value_Repository.md`. The current file (`~/Claude/Intradiem-GTM-Master/04-value-repository/`, 6 KB, June 2026) was built from public sources and most entries carry the CONFIRM tier. The mechanism is right; the content needs Intradiem's internal value materials (Tom Russell's proof points, approved customer stories) swapped in as the knowledge file. Until then the agents produce correctly gated output with few verified numbers, which is the honest state.

## What each agent will not do, in one line

Send, post, schedule, or save anything; look anything up on the web or in a system; use a figure that is not in the attached repository; strengthen a customer claim beyond its source; frame Intradiem as a call-center tool; position WFM vendors as competitors.

## Maintaining

The source of truth for behaviour stays the skill library (`~/.claude/skills/`). When a skill changes, re-run the packaging pass for its Greenlight twin and paste the new instructions into the agent. Owner: Dallas Andrews.
