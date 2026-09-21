---
name: greenlight-bespoke-agent-workaround-sep21
description: Sep 21 2026 Jason Dowden offered bespoke @-mentionable Greenlight agents in Slack; candidate route to full Salesforce Notes and SharePoint docs without a connector; nothing asked or built yet
metadata: 
  node_type: memory
  type: project
  originSessionId: 6551a0aa-0fba-459f-903b-11900c01b9ed
  modified: 2026-09-21T21:08:30.093Z
---

Sep 21 2026, #ai (C0A3NPDCE3G, ts 1790022610.053799): Jason Dowden (SVP Technology) said they will build "bespoke" Greenlight agents on request, e.g. a team SharePoint site pulled in as knowledge, added to any channel and called with @GreenlightAgentName. Greenlight also shows Internal Search, Web Search, M365 MCP and Zoom MCP toggles. Greenlight's Slack search reaches back only 60 days (Iktaer asked; Jason Jones to answer).

Idea: ask for a GTM agent with the Salesforce read Action plus the GTM SharePoint folders, living in a private GTM channel. A rep or Dallas @-mentions it for a record's full Notes; the answer lands in a Slack thread, which Claude Code already reads through the Slack connector. That would replace the hand CSV export in [[sf-freshness-gate-sep21]] and give the 255-character Notes limit a way around. Zoom MCP may partly cover [[call-capture-evaluation-sep21]].

Unverified: whether a bespoke agent can carry the Salesforce Action (Jason's example was SharePoint documents only), whose Salesforce permissions it reads with, whether it returns long text in full, whether it answers a scheduled message.

**Why:** IT is pushing back on a Salesforce MCP connector; Jason's org owns both that objection and Greenlight, so the ask goes straight to him. Do NOT explain that Claude reads Slack: the Slack connector is company-installed and Jason knows it (Dallas, Sep 21). No disclaimers about not going around IT either.
**How to apply:** the ask goes to Jason Dowden as a DM in Dallas's voice, specific about fields and records, never as a public thread reply (Dallas's call, Sep 21). Private channel only, since Salesforce notes would sit in Slack. Related: [[greenlight-agent-pack-sep1]].

Slack app inventory, Sep 21 2026 (60 apps, Dallas's screenshots): Greenlight, Greenlight Slack Search (per-user authorization), Greenlight People Team, Claude (official app), Zoom (AI Companion summaries), Salesforce (Legacy only, the current Salesforce app is NOT installed), OneDrive and SharePoint, ChurnZero, Zapier, IFTTT, Microsoft Power Platform Connectors, Salesloft, G2, RB2B, boo-bot (someone's bespoke bot answering BOO, Aldus and UHG Pilot questions from a local knowledge base, a precedent), Kiro, Hypercontext. Checked the same day: RB2B was connected Oct 2024 by Sierra Jones and never posted a visitor; no G2 posts and no Zoom meeting summaries found in Slack. Zapier and Power Platform could pipe Salesforce notes to Slack but are the refused connector under another logo, so not used.

Greenlight runs us.anthropic.claude-sonnet-5 on Bedrock with about 180K tokens available per request. Dallas hit "Required 443,291, Available 179,889" on Sep 21. Greenlight searches every source unless the toggles are turned off for that chat (Jason Dowden, same day), so run record pulls in a fresh chat with Internal Search, Web, M365 and Zoom off. Keep Greenlight agent knowledge files small for the same reason.

TEST RESULT Sep 21 2026 17:49 CDT: the plain Greenlight app DM in Slack (DM channel D0C3J5RQW8H, bot U0BQVPWKB4Y) returned the Assurant pre-pipeline record with the FULL Notes field, 3,821 characters, nothing cut, plus Stage and Last Modified. No bespoke agent and no ask needed for the read; the 255-character limit is beaten. The app directory page saying "Authorization hasn't been set up" did not block it. Greenlight answers in a thread under the prompt.
OPEN GAP: the Slack connector returns Greenlight's reply with EMPTY text (read_channel, read_thread and search all show a blank body, though search matched its keywords, so Slack indexes it). Greenlight posts blocks with no plain-text fallback. Until that changes Claude can see that Greenlight replied but not what it said, so Dallas pastes the answer in. Candidate fixes: ask Jason Jones to set the top-level text field on Greenlight's Slack posts, or have Greenlight write the answer to a canvas or file the connector can read (untested).
Sep 21 later: Dallas confirmed the Greenlight Slack app cannot create a canvas or attach a file. Remaining routes to a hands-free read: Jason Jones sets the text field on Greenlight's Slack posts, or Greenlight desktop emails the result through its M365 MCP (untested, write ability unknown).
Dallas's standard (Sep 21): the Salesforce notes read has to be autonomous; paste-in is not an acceptable end state, so the text-field ask to Jason Jones is the path. Drafts to the Jasons: problem, ask, example, nothing else.
