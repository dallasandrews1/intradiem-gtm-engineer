# Momentum Architecture Deep Dive + DIY Implementation Guide
### How it works, how it's configured, how it writes to Salesforce, and how to replicate it without it

---

## Part 1: How Momentum Actually Works Under the Hood

### The Bot Join Mechanism

Momentum isn't an API connector or a webhook listener sitting passively. It operates as a **meeting bot** — a literal participant that joins your calls.

How it knows which calls to join:
- Each rep connects their **Google Calendar** (or Outlook) to Momentum via OAuth in their personal 1:1 Slack channel with the bot (`/configure integrations`)
- Momentum reads the calendar continuously, identifies upcoming meetings with external attendees, and queues the bot to join
- The bot joins the conference platform as a named participant ("Momentum Notetaker" or similar)
- On **League-hosted Zoom**: bot runs invisibly in the background, no admit required
- On **Google Meet or Teams** (hosted by anyone): bot appears in the waiting room, host must admit it
- On **externally hosted calls**: same — bot waits, host admits

This is the single biggest Day 1 failure point at new orgs. If reps don't connect their calendar, the bot never shows. Nothing else in the system works.

### The Transcript-to-Summary Pipeline

Once admitted, Momentum:

1. **Records audio** in real time (with consent disclosure handled at the org level)
2. **Transcribes** the audio using ASR (Automatic Speech Recognition) — speaker-separated, attributed by display name or phone number
3. **Enriches the transcript with CRM context** — before the AI runs, Momentum has already pulled the Salesforce Opportunity and Account data linked to the meeting invite (matched by attendee email domains against SFDC Contact records)
4. **Runs the transcript + CRM context through a large language model** (GPT-4o for most tasks; Claude for tone and ambiguity-heavy workflows per their public docs) using a configured prompt template
5. **Structures the output** into the predetermined sections (call context, pain, stakeholders, next steps, MEDDIC fields) — not free-form text, but a defined schema
6. **Posts to Slack** via webhook (5–10 minute latency post-call end)
7. **Writes to Salesforce** via their native Salesforce connector

The key thing the public documentation calls out explicitly: it's **not a one-pass LLM call on raw transcript**. It runs transcript + speaker IDs + Salesforce object metadata together. That's what produces the source attribution ("Laura O'Riordan, on call"), the deal stage awareness, and the structured MEDDIC scoring — not just text summarization.

---

## Part 2: How the Templates Are Configured

### The Admin Configuration Layer

Everything configurable lives in the **Momentum web app** (`app.momentum.io`). There is no Okta tile — reps access it directly. Admins (like Brieann at League) configure it org-wide; individual reps can adjust personal preferences within limits.

The summary configuration has three sections:

**Section 1: Trigger Conditions**
Defines which calls get processed and which template fires. Conditions can be based on:
- Salesforce Opportunity Stage (this is how stage-based summaries work)
- Account ARR or tier
- Internal vs. external attendees
- Whether a Salesforce Opportunity exists at all

This is how League's stage-based system is built: there's a separate summary workflow for each pipeline stage, each with its own AI prompt and section structure.

**Section 2: Content Configuration**
What the AI extracts and surfaces. Two modes:

*Default Prompt:* Momentum's standard summary format (the generic version — what you see on calls with `Opportunity: N/A`)

*Custom Prompt:* Admin writes the AI extraction instruction directly. This is what drives the MEDDIC scoring, the section headers, the classification taxonomy (FRAGMENTED, FIRM TIMING, etc.), and the source attribution format. The prompt is standard natural language instruction to the LLM.

League's stage-based prompts (from Brieann's Slack post, May 2026):
- **Introductory:** Stated pain points and qualification gaps
- **Stage 2 – Discovery:** Decision framework — who decides, how, against what criteria
- **Stage 3 – Qualification & Validation:** Which capabilities resonated vs. were challenged; what business value connected
- **Stage 4 – Solution Alignment:** Confirmation status of scope, budget process, commercial terms, contracting readiness
- **Stage 5 – Scoping & Planning:** Mutual close plan; deal risks to path-to-signature
- **Stage 6 – Commercials:** Pricing agreement status, scope/timeline, legal review progress
- **Stage 7 – Contracting:** Legal review completion, signatures, PO processing status

Toggle-able features per workflow:
- Follow-up email drafts
- Action buttons in Slack (interactive elements reps can click to trigger SF writes)
- Next Steps extraction as a separate thread reply
- MEDDIC/Data Insights as a second thread reply

**Section 3: Delivery Configuration**
Where the post goes. Options:
- Static Slack channel (the master aggregator channels)
- Dynamic lookup — route to the channel owned by the Opportunity's AE (this is how it lands in `#opportunity-[account]` channels)
- 1:1 DM to the call host
- Email (rarely used)
- All of the above simultaneously

### What "Highly Configurable" Actually Means in Practice

Brieann's message to the team during rollout: *"Summaries are highly configurable — your feedback will directly improve output."*

In practice, this means:
- The first 30 days are tuning. Bad sections get flagged, the admin adjusts the prompt, and the next call reflects the change.
- The main slack summary message is **static and cannot be edited by reps** after posting
- MEDDIC/Data Insights thread fields **are editable** — reps click into the thread, edit the field, and saving pushes the update directly to Salesforce
- The Momentum webapp allows reps to edit summaries there, but not via Slack

---

## Part 3: How It Writes to Salesforce

### What Actually Gets Written, Automatically vs. With a Click

**Fully automatic (no rep action required):**
- **Activity log** — Momentum creates a Salesforce Activity (Task/Event record) on both the Account *and* the Opportunity page for every processed call. This is the call log. It contains the full call summary as the activity body.
- **Contact Intelligence fields** — "Area of Responsibility" and "Deal Involvement" fields on Contact records, populated from what people say they own during the call. Matched by email.
- **Next Call Date** — pushed to the Opportunity page
- **Current Tech Landscape** — pushed to the Account page (configurable whether Account or Opp)

**With a two-click action (Slack button → Salesforce write):**
- **Next Steps - Sales field** on the Opportunity — the Slack message contains an action button; clicking it pre-populates a modal with the extracted next steps, rep confirms, it writes to SF
- **SQO (Sales Qualified Opportunity) status** — one of the interactive buttons in the Slack thread; pressing it pushes the stage change to Salesforce
- **Custom MEDDIC fields** — the editable thread fields; saving pushes to whichever Salesforce field they're mapped to

**What does NOT get written automatically:**
- Free-form call notes beyond the structured activity body
- Opportunity stage changes (must be triggered by a rep via button or manually)
- MEDDIC fields that aren't mapped to a specific SF field in the admin config

### The Salesforce Matching Logic

Momentum matches calls to Salesforce objects via this priority order:
1. Meeting invite attendee emails → matched against SFDC Contact records
2. Contact record → linked to an Account
3. Account → linked to open Opportunities
4. Writes the activity to the matched Opportunity (and Account)

If no match: posts to master channel only, labels `Opportunity: N/A`, no SF write.

If duplicates exist: Momentum uses whichever Contact record has Momentum data as the source of truth. This is the "Duplicate Contact Fix" Brieann flagged — the duplicate without Momentum data is stale.

### The Bidirectional Reality

Chris Lyon in the growth team thread: *"So the question, is Slack and Momentum now becoming a headless front end for SFDC?"*

Brieann's answer: *"To an extent, yes. The 2-click SQO and next step update is the next step in that direction."*

This is the actual architecture: Salesforce is the database, Slack is the UI, Momentum is the middleware that reads from SF on the front end (to pull deal context into the Slack post) and writes back on the back end (when reps take action in Slack). The goal is zero reason to open Salesforce during a rep's day.

---

## Part 4: Implementing This Without Momentum

You run Salesforce + Slack. The new org runs Salesforce + Slack. But either Momentum isn't available, it's too expensive, or you want to understand the underlying pattern well enough to build it yourself or evaluate alternatives.

Here's what you're actually building and what each piece costs.

### The Four Functional Layers

| Layer | What it does | Momentum does this | DIY option |
|---|---|---|---|
| 1. Capture | Bot joins call, records audio | Native | Fireflies.ai, Otter AI, Fathom, Read.ai |
| 2. Intelligence | Transcript + CRM context → structured output | Native + GPT-4o/Claude | Claude API + your prompt |
| 3. Distribution | Post to Slack channels | Native | Slack API webhook |
| 4. CRM write-back | Push structured fields to Salesforce | Native + Slack buttons | Salesforce REST API or Make/Zapier |

You can replicate all four with existing tools or lightweight code.

---

### Layer 1: Call Capture — Choose Your Recorder

The recorder's only job: get a transcript with speaker attribution into a place you can read it.

**Fireflies.ai** — closest Momentum analog for smaller orgs. Bot joins via calendar. Posts summaries to Slack. Has Salesforce integration. Does not do MEDDIC scoring natively, but has custom AI prompt support. ~$10–19/user/month.

**Otter AI** — League already has this for non-sales use cases. Has calendar integration, Slack posting. Less sales-specific. No native SF write.

**Fathom** — popular with individual reps, free tier. Posts to Slack. No native Salesforce integration. Good transcript quality.

**Read.ai** — strong enterprise option. Has Salesforce, Slack, HubSpot integrations. More expensive.

**Gong** — if the org already has it, Momentum has a native Gong integration. Gong provides the transcript, Momentum wraps it with the intelligence and routing layer.

**Minimum viable:** Any tool that can output a transcript (even as a text file or API endpoint) and post to Slack.

---

### Layer 2: Intelligence — The Prompt Is the Product

This is the part that looks like magic but is actually just a well-engineered prompt running on top of a transcript. You can replicate it entirely with the Claude API.

**The core input to your LLM call:**
```
1. Full transcript text (speaker-attributed)
2. Salesforce Opportunity context: stage, ARR, account name, existing next steps
3. Salesforce Account context: industry, tech landscape if known
4. Stage-specific extraction prompt (varies by deal stage)
```

**Stage-based prompt structure (replicate League's exactly):**

```
SYSTEM: You are a sales intelligence analyst. Extract structured deal intelligence 
from this call transcript. Output must follow the exact schema below. Be specific — 
attribute every insight to the person who said it and the context in which they said it.

OPPORTUNITY CONTEXT:
Stage: {sf_stage}
Account: {account_name}
ARR: {committed_arr}
Existing Next Steps: {sf_next_steps}

TRANSCRIPT:
{transcript_text}

---

IF stage is "Discovery":
Extract:
- Call Context & First Impressions: Purpose of the call, who initiated, tone of meeting
- Business Context & Pain: Named pain points, operational problems, urgency signals
- Stakeholders & Organization: Every attendee's apparent role and influence level
- Next Steps: Specific, owned, time-bound actions for both sides
- MEDDIC Assessment: Score each field (Metrics, Economic Buyer, Decision Criteria, 
  Decision Process, Identify Pain, Champion) with: STATUS | CONFIDENCE | EVIDENCE | SOURCE

IF stage is "Qualification & Validation":
Extract:
- Call Context & Qualification Focus
- Solution Fit & Value Drivers: Which capabilities resonated, which were challenged, 
  what value language the prospect used
- Decision Makers, Budget & Timing: Named people, stated budget context, timeline drivers
- Customer Reaction & Sentiment: Emotional register, buying signals, risk flags
- Next Steps
- MEDDIC Assessment

[Continue for each stage...]

OUTPUT FORMAT: Structured JSON with named fields for each section.
Return JSON only, no preamble.
```

**What makes this work:** The stage awareness means you're not asking the LLM to do everything every time. A Stage 7 (Contracting) call gets a prompt laser-focused on legal review, signatures, and PO processing. The output is short and actionable, not a wall of text.

---

### Layer 3: Slack Distribution — Replicate the Message Format

Once you have structured JSON output from your LLM call, you format it into a Slack Block Kit message via the Slack API.

**The channel routing logic:**
```python
def route_to_channels(sf_opportunity_id, owner_slack_id):
    channels = []
    
    # Always post to master channel
    channels.append(MASTER_CHANNEL_ID)
    
    # If opportunity exists, also post to opp channel
    if sf_opportunity_id:
        opp_channel = find_channel(f"opportunity-{account_slug}")
        if opp_channel:
            channels.append(opp_channel.id)
    
    # Always DM the call host
    channels.append(owner_slack_id)
    
    return channels
```

**The thread structure:**
- Post 1 (parent): Header block + call summary sections
- Reply 1 (thread): Next Steps & Open Items
- Reply 2 (thread): MEDDIC/Data Insights with editable fields

Slack Block Kit lets you add interactive buttons to the parent message. Each button triggers a Slack webhook that you catch server-side and use to write to Salesforce.

---

### Layer 4: CRM Write-Back — Close the Loop

This is where most DIY implementations stop. Don't stop here.

**What to write to Salesforce after every call:**

1. **Activity record** (Task or Event) on the Opportunity:
```python
sf.create('Task', {
    'Subject': f'Call - {call_title} - {call_date}',
    'Description': formatted_summary,
    'WhatId': opportunity_id,  # links to Opportunity
    'WhoId': contact_id,       # links to primary Contact
    'ActivityDate': call_date,
    'Status': 'Completed',
    'Type': 'Call'
})
```

2. **Opportunity field updates** (next steps, close date signals):
```python
sf.Opportunity.update(opportunity_id, {
    'Next_Steps__c': extracted_next_steps,
    'Last_Call_Date__c': call_date
})
```

3. **Contact Intelligence fields** (from what people said on the call):
```python
sf.Contact.update(contact_id, {
    'Area_of_Responsibility__c': extracted_role_context,
    'Deal_Involvement__c': extracted_deal_role
})
```

4. **MEDDIC fields** (if your org has them as custom fields):
```python
sf.Opportunity.update(opportunity_id, {
    'MEDDIC_Economic_Buyer__c': meddic_json['economic_buyer']['finding'],
    'MEDDIC_Decision_Process__c': meddic_json['decision_process']['finding'],
    # ... etc
})
```

**Libraries:** `simple-salesforce` (Python) or `jsforce` (Node). Both handle OAuth, field mapping, and error handling cleanly.

---

### The Minimum Viable Stack (No New Budget)

If you're at a new org that has Salesforce + Slack + Zoom + some recording tool, here's the path to 80% of Momentum's value with near-zero cost:

**Step 1: Enable Zoom local recording + Otter AI** (or whatever is approved). Connect Otter to Slack. You now have transcripts posting to Slack automatically.

**Step 2: Build a Slack bot** that watches the transcript channel for new posts. When a post arrives, extract the meeting title, pull the Otter transcript via API, identify the Salesforce opportunity by keyword matching, and send the transcript to Claude API with your stage-based prompt.

**Step 3: Claude API call** returns structured JSON. Format it as a Block Kit message. Post to master channel + opp channel via Slack API.

**Step 4: Add a Zapier or Make automation** (or a simple Python webhook) that catches the "Update Salesforce" button click from the Slack message and writes the next steps to the SF Opportunity record via Salesforce REST API.

**Total new cost:** Claude API credits (pennies per call), Zapier free tier or Make free tier for the SF write trigger.

**What you've built:** Automated transcript → AI summary → Slack post → Salesforce activity log. Identical functional architecture to Momentum. Customizable prompts. Stage-aware. Routable to any channel.

---

### The Day 1 Pitch at a New Org

*"You have Salesforce, Slack, and call recording. You're probably missing the middle layer — the thing that reads the transcript, extracts the deal intelligence, routes it to the right people in Slack, and writes it back to Salesforce without the rep having to do anything. I've built this before. Here's what it looks like and what it takes to stand it up."*

If they have Momentum already: you know exactly how it's configured and can improve it.
If they don't: you know exactly what to build and can have a working prototype in two weeks.

---

## Quick Reference: What to Ask on Day 1

| Question | What the answer tells you |
|---|---|
| What call recording tool are you using? | Whether the capture layer exists |
| Does it connect to Salesforce or Slack? | Whether intelligence and distribution are active |
| How do reps update Salesforce after a call? | Whether there's a manual gap or automation |
| What fields are reps required to fill in? | What your write-back logic needs to map to |
| Who owns the call recording configuration? | Who you need to partner with to change anything |
| Do you have a MEDDIC or qualification framework? | What your extraction prompt needs to focus on |
| Do you have deal room channels in Slack? | Whether the distribution architecture exists |

---

*Documented June 2026. Sources: League internal Slack (Brieann Geddes enablement posts in #momentum-feedback, #growth-team, #team-core-sales); Momentum public documentation (docs.momentum.io, momentum.io/integration, momentum.io/better-together-salesforce). Portable — designed for use at any Salesforce + Slack org regardless of call recording tool.*
