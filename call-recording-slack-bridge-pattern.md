# Call Recording → Slack Bridge Pattern
### Portable Architecture Reference | No CRM-native connector required

---

## The Problem This Solves

Your call recording tool captured the call. Your CRM needs to know what happened. But there's no direct write path between them.

The bridge: **the recording tool posts a structured summary into Slack, and Slack becomes the operational record layer** that humans and downstream tools read from.

This pattern works anywhere you have:
- A call recording / conversation intelligence tool (Momentum, Gong, Chorus, Fathom, etc.)
- A Slack workspace
- A CRM (Salesforce, HubSpot, etc.)
- Reps who live in Slack between calls

---

## Channel Architecture

Two channel types carry the load. You need both.

### 1. Master Aggregator Channel(s)
**Purpose:** Org-wide feed of every processed call, regardless of account or team.

| Channel | Scope |
|---|---|
| `#[tool]-sales-call-summaries` | All new business / AE calls |
| `#[tool]-acctmanagement-callsummaries` | All post-sale / AM calls |
| `#[tool]-partner-call-summaries` | Partner / channel calls |

Every call from any rep posts here automatically. No action required by the rep. This is your audit trail and leadership visibility layer.

### 2. Account Opportunity Channels
**Format:** `#opportunity-[account-name]`

**Purpose:** Deal-specific room. The recording tool posts the call summary here *in addition to* the master channel when it can match the call to a CRM opportunity. The full deal team — AE, SE, AE manager, CSM, exec sponsor — lives in this channel.

**How matching works:** The tool reads calendar invites or attendee email domains, matches to a Salesforce Account or Opportunity record, and routes accordingly. If no match is found, the post lands only in the master channel with `Opportunity: N/A`.

---

## Data Flow: End to End

```
Call happens (Zoom, Teams, Google Meet)
        ↓
Recording tool captures audio + transcript
        ↓
AI processing: summary, next steps, sentiment, MEDDIC signals (5–10 min latency)
        ↓
Tool looks up: is there a Salesforce Opportunity linked to this meeting?
        ↓
    YES → posts to:                    NO → posts to:
    - Master channel                   - Master channel only
    - Account opp channel              - Summary format only, no SF links
        ↓
Thread reply 1: Next Steps (auto-extracted)
Thread reply 2: MEDDIC / Data Insights (structured field-by-field scoring)
        ↓
Human reads it in Slack
        ↓
[MANUAL GAP — see below]
        ↓
Rep copies key fields into Salesforce manually
   OR
Downstream automation reads the Slack post and writes to Salesforce
```

---

## Message Structure: Exact Fields

Every Momentum post follows this format. Other tools (Gong, Chorus) produce nearly identical structures — the field labels differ but the information taxonomy is the same.

### Parent Message (posted in channel)

```
📞 [Meeting Title Link → momentum.io/meeting/ID] has been analyzed 📝 🔥

👥 Internal Attendees:
   [Name] (Host)
   [Name]

👥 External Attendees:
   [Name]
   [Name]
   + N more

☁️ Opportunity: [SF Opportunity Name + Link] (Stage: [SF Stage])
   — OR —
☁️ Opportunity: N/A

🏢 Account: [SF Account Name + Link]

📅 Date: MM-DD-YYYY

🕐 Time: [local time] ([duration] mins)

📓 Call Summary

[SECTION HEADERS VARY BY CALL TYPE — see below]

Use 🤖 AskMomentum to explore detailed insights in the 🧵 below
```

### Summary Section Headers (vary by call type)

| Call Type | Section Headers Used |
|---|---|
| Discovery / Qualification | 🔍 Call Context & Qualification Focus · 💎 Solution Fit & Value Drivers · 👥 Decision Makers, Budget & Timing · 💡 Customer Reaction & Sentiment |
| First meeting / exploratory | 🎯 Call Context & First Impressions · 🔥 Business Context & Pain · 👥 Stakeholders & Organization |
| Operational / project sync | 🎯 Call Context & First Impressions · 🔥 Business Context & Pain · ✅ Key Points · ✍️ External Next Steps · ✍️ Internal Next Steps |
| Scheduling / admin call | [Abbreviated — just context + next steps, no pain/stakeholder sections] |

### Thread Reply 1: Next Steps

Posted as a separate reply immediately after the parent message.

```
➡️ Next Steps & Open Items
- [Action] (Owner: [Name], [Timeframe])
- [Action] (Owner: [Name])
Open items: [Unresolved questions or gaps flagged explicitly]
```

### Thread Reply 2: Data Insights / MEDDIC Scoring

Posted as a second reply. This is the MEDDIC layer.

```
🔍 Data Insights
Opportunity

Decision Criteria:
[CLASSIFICATION] | [FORMALITY] | [PRIORITY LEVEL] | [Detailed finding] | [Source: who said it, on what call]

Decision Process:
[CLASSIFICATION] | [Process detail] | [Risk flags] | [Finding] | [Source]

Competition Eliminated:
[STATUS] | [Competitor names] | [Finding]

Timing Identified:
[FIRMNESS] | [Type of event] | [Urgency] | [Finding] | [Source]

Economic Buyer:
[EB STATUS] | [Named person or gap] | [Champion status] | [Buying committee map]

Money budgeted:
[BUDGET STATUS] | [Sufficiency] | [Amount detail or gap] | [Deal type] | [Approval status] | [Source]

Risk:
[RISK TYPE] | [SEVERITY] | [IMPACT LABEL] | [Named person raising risk] | [Specific risk detail]

Benefit Agreed:
[ALIGNMENT LEVEL] | [Qualifier] | [Qualifier] | [Finding] | [Source]

Identified Pain:
[PAIN TYPE] | [CATEGORY] | [CONNECTION TO SOLUTION] | [URGENCY] | [Source + quote summary]

Competition Eliminated: [repeat field with status update]
```

**Classification taxonomy observed:**

- Decision Process: `FRAGMENTED`, `CLEAR`, `APPROVAL FRAGMENT ONLY`
- EB Status: `COACH IDENTIFIED NOT CHAMPION`, `EB CONFIRMED`, `EB UNKNOWN`
- Risk: `BENEFIT NOT AGREED`, `DECISION PROCESS UNVALIDATED`, `TIMELINE RISK`
- Timing: `FIRM TIMING`, `BOARD/GOVERNANCE EVENT`, `VAGUE/UNQUANTIFIED`
- Budget: `BUDGET AWARENESS`, `SUFFICIENCY UNKNOWN`, `CONDITIONAL APPROVAL`

### Deal Room Initialization Post (first post in opp channel)

When a new opportunity channel is created or a new deal is first matched, Momentum posts a "Deal Room" summary pulled from Salesforce:

```
Welcome to the Deal Room for ☁️ [Opportunity Name]:
Opportunity Details
Stage: [SF Stage]
Committed ARR: $[amount]
Anticipated SQO Date: [date]
Next Steps - Sales: [pulled from SF next steps field]
Account Executive: @[AE Slack handle]

📞 Contacts
⭐ 👤 [Name] ([Title]): email | phone
```

---

## The Manual Gap: Where the Automation Stops

### What gets automated (no human required):
- Call is recorded → processed → posted to Slack
- Meeting-to-opportunity matching via SF lookup
- Summary generation (context, pain, stakeholders, next steps)
- MEDDIC field scoring with source attribution
- Routing to the correct channel(s)

### What does NOT get automated (manual step remains):

**The Salesforce write-back.**

The tool reads from Salesforce to match and link. It does not write back to Salesforce. The MEDDIC scores, next steps, and call context stay in Slack. They do not appear in the Salesforce activity log, opportunity fields, or MEDDIC fields unless a human copies them there.

**The actual manual workflow observed:**
1. Rep gets paged in the opp channel when the post lands
2. Rep reads the summary in Slack (or AskMomentum in the thread)
3. Rep manually logs a Salesforce Activity ("Call — [date]") with their own paraphrase
4. Rep manually updates MEDDIC fields in SF (or skips it)
5. AE manager reads the Slack post directly for deal intel instead of going to Salesforce

**Why this gap exists:**
The call recording tool was procured for conversation intelligence, not CRM hygiene. The Slack integration was the path of least resistance — it required no Salesforce admin configuration, no field mapping, no permission setup. The tool POSTed to Slack via webhook in hours. A true Salesforce write-back would require custom field mapping, activity object creation, sandbox testing, and security review. The Slack bridge is faster to ship than the CRM integration is to approve.

### Where downstream automation could close the gap:

A secondary tool (or custom Slack bot) could watch the master channel for new Momentum posts, parse the structured message format, and write to Salesforce automatically. The message structure is consistent enough to parse reliably. This is the gap you can offer to close on Day 1 at a new company.

---

## Day 1 Diagnostic: Do You Have This Gap?

Ask these questions to map whether the same pattern exists:

| Question | Signals gap exists | Signals gap is closed |
|---|---|---|
| Does your call recording tool post to Slack? | Yes | No (writes to CRM directly) |
| Are Salesforce activity logs up to date? | No / inconsistent | Yes / automated |
| Do managers read Slack for deal intel instead of SF? | Yes | No |
| Is there a Slack-to-SF automation running? | No | Yes (Zapier, Make, custom bot) |
| Do MEDDIC fields in SF match what was discussed on calls? | No | Yes |

If you get 3+ "signals gap exists" answers: the pattern is live, the bridge is missing, and you can build it.

---

## Build Checklist: Replicating This Bridge

**What you need at the new company:**

- [ ] Call recording tool with Slack webhook capability (Momentum, Gong, Chorus, Fathom — all support this)
- [ ] Slack workspace with ability to create channels and add the tool as a bot
- [ ] Salesforce with Opportunity and Account objects accessible via API or SOQL
- [ ] Channel naming convention agreed on (standardize early — retrofitting is painful)

**Channel setup:**
- [ ] Master channel(s) created and bot added
- [ ] Opp channel naming convention defined (`#opportunity-[accountname]`)
- [ ] Bot granted access to private channels where deal rooms will live

**Optional: close the write-back gap**
- [ ] Slack event listener watching the master channel for new Momentum posts
- [ ] Parser that extracts: meeting title, SF opportunity URL (already embedded in the post), next steps, MEDDIC fields
- [ ] Salesforce Activity write via REST API on each parsed post
- [ ] Error alerting when match fails (N/A opportunity = no write attempted)

---

## Reference: Real Post Examples

All examples pulled from production Slack. Account names and prospect names are visible in the original posts — sanitize before sharing externally.

**Example 1 — Master channel, discovery call with linked opportunity:**
`#momentum-sales-call-summaries` | Dean Wood // Laura O'Riordan | Doctor Care Anywhere | Stage: Qualification & Validation | Full MEDDIC thread with EB gap flagged, pricing risk identified, LOI timing noted.

**Example 2 — Master channel, new business exploratory, no SF opportunity yet:**
`#momentum-sales-call-summaries` | Naomi Adams // Telstra Health | Stage: N/A | Stakeholder map, pain identified, no CRM record created yet.

**Example 3 — Master channel, internal/partner sync:**
`#momentum-sales-call-summaries` | Brett Whitley // Deloitte Canada | Stage: N/A | Account updates, no opportunity linked.

**Example 4 — Opportunity channel, mid-funnel discovery call:**
`#opportunity-bcbs-nc` | Andrea Puckett // Rammesh Rajagopal | Stage: Interested | Full summary + next steps. Human commentary posted by AE immediately after, supplementing the Momentum post with her own read of the call.

**Example 5 — AM channel, post-sale implementation sync:**
`#momentum-acctmanagement-callsummaries` | Geisinger Member Portal Modernization | Stage: Qualification & Validation | Project status, blockers, roadmap priorities, budget timing pressure.

---

*Pattern documented: June 2026. Source: production Slack posts from Momentum bot across multiple channel types. Portable — does not reference company-specific systems beyond what's visible in the message format itself.*
