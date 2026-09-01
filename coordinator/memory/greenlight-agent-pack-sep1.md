---
name: greenlight-agent-pack-sep1
description: "Sep 1 2026: Dallas wants every Claude skill that can run without local tooling published as a shared Greenlight agent (Jason Jones pushes Greenlight adoption; 41 agents exist); eight packaged in motions/ai_champion_product/greenlight_agents/ with a register, create order, neighbour notes, and the Value Repository caveat"
metadata:
  type: project
---

Greenlight is Intradiem's internal Claude-powered tool (Jason Jones owns it): agents with an instructions field, knowledge files, optional Actions (Salesforce read, Confluence, Slack), conversation starters; Projects too; downloadable single-file HTML artifacts confirmed Sep 1 2026. About 41 agents existed on Sep 1 (Confluence Assistant, Salesforce Agent, VITO Messaging Assistant by Josh Wilkins, Earnings Call Analyzer by Ben Goodenough, MikeG_PRD_HelperAgent, Customer Call Insights, ConvoIQ, Roleplay Agent, Channel Catalyst by Frank Ciccone, 12-40-30, Coaching Solution SME, Slackbot, others). Jason had asked the champions which business-unit Slack channels could host a Greenlight agent and which Claude work Greenlight could replicate for people without Claude access.

Dallas's direction Sep 1: "shared agent anywhere and anytime we can", make the GTM Engineering work visible in Greenlight. Packaged the same day in `motions/ai_champion_product/greenlight_agents/<slug>/` (AGENT_INSTRUCTIONS.md self-contained, AGENT_CARD.md with description, starters, knowledge files): prototype-builder (instructions = pm_kit/PROJECT_INSTRUCTIONS.md), reply-handler, competitive-intel, business-case, signal-to-play, outreach-writer (first-draft + copy-sharpener merged, two-pass), content-repurposer, pre-mortem. README.md there is the register with neighbour notes and create order (Prototype builder, Pre-Mortem, Competitive Intel + Reply handler, Business Case + Signal to Play, Outreach Writer after a word with Josh about VITO overlap, Content Repurposer).

Not packagable (local tooling): strike-sequence, motion-stamp, war-room, daily-rundown, naveen-readout, interactive-enablement, backoffice-icp, launch-kit partly.

Caveat: the Value Repository the gate points at (~/Claude/Intradiem-GTM-Master/04-value-repository/Intradiem_Value_Repository.md) is 6 KB, public-sourced June 2026, mostly CONFIRM tier; internal value materials need to replace it as the knowledge file before seller-facing agents ship.

**Why:** Greenlight is the surface people without Claude already have, and Jason's adoption push makes it the place GTM Engineering's work gets seen.

**How to apply:** when a skill changes, repackage its Greenlight twin (packaging rules: no Claude Code, skills, paths, Clay, engines; "the attached <file>" for knowledge; verified-claims gate and six-vertical scope kept verbatim; no em dashes; inputs and output shape sections). Next: a GTM agent with the Salesforce Action once the text-only ones are up. Related: [[pm-kit-greenlight-coldrun-sep1]], [[ai-champion-product-role-aug17]], [[feedback-orchestrator-not-clay]].
