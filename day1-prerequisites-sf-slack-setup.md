# Day 1 Prerequisites: What Needs to Exist Before Any of It Works
### The stuff nobody tells you until something breaks

---

## The Honest Problem with the Previous Two Docs

The architecture doc explains what to build. The Momentum deep-dive explains how it's configured. Both assume certain things already exist: clean Salesforce data, a properly connected Salesforce-Slack integration, custom fields that match your extraction prompts, and a person with admin access who knows where the buttons are.

At a new org, none of that is guaranteed. This doc covers everything that needs to be in place — or audited on Day 1 — before the intelligence layer has anything to work with.

---

## Part 1: The Salesforce-Slack Native Connector (The Foundation)

This is a separate thing from Momentum. It's Salesforce's own first-party Slack app, and it's what allows tools like Momentum to route to opportunity channels, what allows reps to edit SF fields from Slack, and what enables the alert logic that drives deal rooms. If this isn't set up, nothing routes correctly.

### What it requires — both sides have to act

**On the Slack side (Slack Admin):**
- Go to workspace Settings → Tools & Settings → Manage Salesforce Organizations
- Enter the Salesforce org's My Domain URL (format: `[orgname].my.salesforce.com`)
- Choose account mapping method: **Email** if no SSO, **SAML NameID** if the org uses single sign-on/Okta
- Submit the connection request — this puts it in "Waiting for Approval" status

**On the Salesforce side (SF Admin):**
- Go to Setup → search "Manage Slack Connection"
- Find the pending request, select the same mapping field (Email or SAML Federation ID)
- Agree to terms and Approve
- Back in Slack: activate the pending connection

**Then each rep authenticates individually:**
- The Salesforce app appears in their Slack sidebar once connected
- They run `/salesforce connect` or authenticate via the banner prompt
- Without this individual step, alerts don't reach them personally and field edits don't write back under their user credentials

### What to configure after connection is live

**Salesforce Channels for Records** — this is the native deal room feature. It's what creates a Slack channel that's tied to a specific SF Opportunity or Account record:
- In Salesforce Setup → Quick Find: "Slack Channels for Records"
- Click + Add Objects → add Opportunity, Account (and any other objects you want channelized)
- Set default privacy: Public means anyone can join, Limited Access mirrors the SF record's sharing settings
- Channel names pull from whichever field you configure — Account Name is typical for opp channels

Once this is configured, creating an Opportunity in SF can automatically spin up a corresponding Slack channel. That's the native version of the `#opportunity-[account]` channel pattern — no manual channel creation needed.

**Salesforce Alerts** — three types:
- **My Alerts:** DM to the record owner when their record changes (stage moves, field updates)
- **Channel Alerts:** Post to a specific channel when a single record changes
- **Bulk Alerts:** Post to a channel whenever any record of a given type changes (e.g., all new Closed Won opportunities → #wins)

To set up a Channel Alert from Slack: click the `+` in the message field → "Add/edit alerts for a channel" → add the record → select which field changes trigger the alert.

To set up from Salesforce: open any record → click the Slack Alerts button → choose channel.

**Record unfurling** — when a SF record URL is pasted into Slack, it previews the record inline. Configurable under the Salesforce Org settings in Slack: choose how much detail to show (full fields, name + object only, or off). All channel members see the preview regardless of their individual SF permissions — worth knowing for security-sensitive orgs.

### The user mapping problem — audit this on Day 1

The single most common reason Momentum posts land without routing to the right rep, or alerts don't fire to the right channel, is **broken user mapping between Slack and Salesforce.** The system matches by email. If a rep's Slack email is their work alias and their Salesforce email is their direct address, or if either was set up before the other existed, the match fails silently.

Ask the SF admin to run a quick report: pull all active SF users, export email addresses, cross-reference against the Slack member list. Any mismatch = a rep whose activity will route to `N/A` in Momentum and whose SF alerts won't reach them.

---

## Part 2: The Salesforce Object Layer — What Needs to Exist for the AI to Write to

Momentum (or your DIY equivalent) writes to Salesforce fields. If those fields don't exist, or aren't mapped in the tool's config, the write fails silently and nobody knows until they check SF and find it empty.

### Opportunity object — what you need as custom fields

The standard SF Opportunity object gives you: Name, Stage, Close Date, Amount, Account, Owner. That's it. Everything else is custom. Here's what to audit or build:

**Core activity fields (needed for call log write-back):**
- `Next_Steps__c` — Long Text Area — where extracted next steps land
- `Last_Call_Date__c` — Date — auto-populated from the call record
- `Next_Call_Date__c` — Date — Momentum writes this automatically
- `Current_Tech_Landscape__c` — Long Text Area — what the prospect currently runs

**MEDDIC/MEDDPICC fields (needed for structured scoring):**

Two-layer approach is best practice:
- A **picklist field** per element using a shared Global Value Set: `Red / Yellow / Green` (or `Gap / Moderate / Strong`) — gives the traffic light for pipeline reviews
- A **Long Text Area notes field** per element for the actual extracted content — this is what Claude writes to, what managers read during coaching

| Field | API Name | Type |
|---|---|---|
| Metrics | `MEDDIC_Metrics_Score__c` | Picklist (Global Value Set) |
| Metrics Notes | `MEDDIC_Metrics_Notes__c` | Long Text Area |
| Economic Buyer | `MEDDIC_EB_Score__c` | Picklist |
| Economic Buyer Notes | `MEDDIC_EB_Notes__c` | Long Text Area |
| Decision Criteria | `MEDDIC_DC_Score__c` | Picklist |
| Decision Criteria Notes | `MEDDIC_DC_Notes__c` | Long Text Area |
| Decision Process | `MEDDIC_DP_Score__c` | Picklist |
| Decision Process Notes | `MEDDIC_DP_Notes__c` | Long Text Area |
| Identified Pain | `MEDDIC_Pain_Score__c` | Picklist |
| Identified Pain Notes | `MEDDIC_Pain_Notes__c` | Long Text Area |
| Champion | `MEDDIC_Champion_Score__c` | Picklist |
| Champion Notes | `MEDDIC_Champion_Notes__c` | Long Text Area |
| MEDDIC Composite Score | `MEDDIC_Composite__c` | Formula (rolls up the picklists) |

**Global Value Set tip:** Create one value set called `Qualification_Score` with values Red/Yellow/Green (or 1/2/3/4/5 if you want numeric), apply it to all picklist score fields. One place to update if the scale ever changes.

**Validation rules (optional but high-value):** Prevent opportunities from advancing past a stage without minimum field completion. Example: can't move to Stage 4 without at least four MEDDIC score fields set to Yellow or Green. This is the enforcement layer. Without it, reps treat the fields as optional and data quality collapses within 90 days.

### Contact object — what Contact Intelligence writes to

Momentum's Contact Intelligence feature writes two fields to Contact records automatically. If these fields don't exist, the write silently fails:
- `Area_of_Responsibility__c` — Long Text Area — what the contact said they own
- `Deal_Involvement__c` — Long Text Area — their role in the buying process

These are simple to create. Add them to the Contact page layout so they're visible when reps open a contact record.

### Opportunity Contact Roles — the hidden dependency

This is the thing most orgs skip and then regret. Opportunity Contact Roles are how Salesforce associates specific contacts to a specific opportunity with a role label (Champion, Economic Buyer, Technical Evaluator, etc.). Momentum uses contact records linked to meetings to match calls to opportunities. If contact roles aren't populated, that matching gets fuzzy.

What to audit:
- Are Contact Roles enabled on the Opportunity object? (Setup → Object Manager → Opportunity → Fields & Relationships → confirm `Contact Roles` is present)
- Is there a validation rule or required field ensuring at least one Primary Contact Role per opportunity before advancing past Stage 2?
- Are your role picklist values aligned with MEDDIC labels? If they're generic ("User", "Other") they're useless for multi-threading context.

---

## Part 3: Contact Data Hygiene — The Input Quality Problem

Every doc so far assumes clean contact data. The reality at most orgs: it isn't. And dirty contact data means Momentum's email-matching logic fails, calls route to `N/A`, and the write-back fires on the wrong record or not at all.

### The three most common contact data problems

**Duplicate contacts:** Same person, two records — one created by a rep manually, one imported from marketing. Momentum's instruction (per Brieann's Slack post): the contact with Momentum data is the source of truth. But if duplicates exist before Momentum, the tool picks whichever it finds first.

Fix: Run the SF Duplicate Management report before going live. Merge or delete duplicates. Set up a Duplicate Rule on the Contact object going forward so new dupes get flagged on creation.

**Missing or wrong email addresses:** Momentum matches meeting attendees to SF Contacts by email. If the contact record has the wrong email (old job, typo, personal address), no match.

Fix: Before rollout, pull a Contact report filtered to your target accounts, sort by email domain, flag anything that doesn't match the expected corporate domain.

**Contacts not linked to opportunities:** A contact can exist on an Account without being associated to any Opportunity. If they're not an Opportunity Contact Role, Momentum won't write to the Opportunity when they're on a call — it writes to the Account level only, which is less useful.

Fix: Make it a habit (or a validation rule) that every new contact added from a prospect meeting gets added as a Contact Role on the relevant Opportunity immediately.

---

## Part 4: The Tools That Sit Alongside the Core Stack

Things that came up at League that aren't Momentum but are part of how the full system operates:

### Accord (Mutual Action Plans)
Doug Tipsword raised this directly in `#growth-enablement`: *"If we're going to continue to leverage Accord and Momentum, I would be keen to better understand how we can plug these things into Claude. Getting call recordings from Momentum into Claude, paired with account plans/mutual success plans would be huge."*

What Accord does: it's a shared workspace with the prospect — a mutual action plan (MAP) that both sides can see and update. Tracks milestones, owners, and deadlines on the path to contract. Connects to Salesforce to pull/push opportunity data.

Why it matters for the bridge: Accord is where the deal's forward-looking plan lives. Momentum captures what happened on calls. The two together give you a complete picture — past (call history) + future (MAP). The gap Tipsword identified is that these two data sources aren't yet being fed into Claude together.

At a new org, ask: do you have a MAP tool? If yes (Accord, Mutual Action, Dealhub, Notion templates, even a Google Sheet), figure out whether it connects to Salesforce and whether call summaries are being cross-referenced with it.

### Artisan (AI Outbound Agent)
League runs Artisan as its AI outbound agent for BDRs. It connects to Salesforce for account/contact data, sequences outreach, and has its own Slack notifications. It's separate from Momentum but uses the same SF contact data as its input.

What this means for Day 1: if the new org has any AI outbound tool (Artisan, Ava, 11x, Clay sequences), its data quality depends entirely on the same clean SF contact data you're auditing for Momentum. Fix the data once, and all tools benefit.

### Rattle (or equivalent Slack-SF workflow tool)
Worth knowing about even if League doesn't heavily use it. Rattle is a lightweight tool that does one thing well: it watches for SF field changes and posts alerts to Slack, and lets reps update SF fields from inside Slack messages without leaving the thread.

It's the lightweight alternative to Momentum's write-back buttons if you're building a DIY stack. Two-way SF-Slack field sync in about 10 minutes of setup. Free tier covers three workflows. Useful bridge while waiting for a more full-featured tool to be approved through procurement.

### Claude in Slack (the layer League added on top of everything)
League's IT team built a custom Salesforce MCP connector for Claude (read-only, per the `#growth-team` post from Marissa Thiel). The use case Brieann posted: paste a Momentum summary into Claude, ask it to draft the next steps for Salesforce, copy-paste into the field.

The reason this matters: even without write access, Claude as a Slack-native layer on top of Momentum posts closes the cognitive gap between "here's what the call said" and "here's what I should do with it." The Forcing Function is already this, but at a new org where Momentum is the only tool, Claude in Slack is the low-lift way to start getting AI into the workflow immediately.

At a new org ask: is Claude available in Slack? If not, can you get it approved? It's a one-line install for any Slack workspace owner and it doesn't require IT engineering time.

---

## Part 5: The Security and Permissions Layer — Where Things Get Blocked

The things that got blocked at League and will get blocked at a new org:

**The Google Drive / Salesforce conflict:** Michele Oliveto noted in `#claude-cowork` that IT had to disable Claude's Google Drive connection for any user who also had Salesforce access, due to security concerns about data crossing boundaries. This is a real policy consideration — expect it at any security-conscious org (especially healthcare/HIPAA environments). You may need to choose which connection you prioritize, or work with IT to get a carve-out.

**Bot approval for Slack:** Creating a new Slack bot or app requires Slack admin approval. If you're building a DIY call summary bot, factor in procurement/IT review time. This is not a same-day ask at any org with proper governance. At League, even Momentum required IT admin approval to join as a bot participant in the workspace.

**Salesforce API access:** Your DIY write-back needs a Salesforce user with API access enabled. Not all SF user licenses include this — it depends on license type. A Salesforce Admin or Platform license includes API access; a basic Salesforce license may not. Confirm this before you write a single line of Python that hits the SF REST API.

**OAuth and token stability:** The Atlassian MCP situation (Dmitri's note in `#ai`) is a preview of a recurring problem: OAuth tokens expire, users get logged out of integrations, and nobody notices until something stops posting. Design for this: build monitoring into any automation that catches auth failures and alerts someone, rather than silently dropping calls.

---

## Part 6: Day 1 Audit Checklist

Walk into the new org, get Salesforce access, run these checks before you build anything:

**Salesforce-Slack connection:**
- [ ] Native Salesforce app installed in Slack workspace?
- [ ] Salesforce org connected and activated?
- [ ] Your personal account mapped (Email matches between SF and Slack)?
- [ ] Salesforce Channels for Records enabled for Opportunity and Account objects?
- [ ] Channel naming field configured (Account Name field)?

**Salesforce object readiness:**
- [ ] Opportunity stages defined and match your sales methodology?
- [ ] `Next_Steps__c` field exists on Opportunity?
- [ ] MEDDIC or qualification framework fields exist (or is someone building them)?
- [ ] Contact Roles enabled on Opportunity?
- [ ] Contact Role picklist values align with your qualification language?
- [ ] `Area_of_Responsibility__c` and `Deal_Involvement__c` on Contact (if using Momentum)?

**Contact data quality:**
- [ ] Duplicate contacts audited for your target accounts?
- [ ] Email addresses present and correct on key contacts?
- [ ] Key prospect contacts linked as Opportunity Contact Roles, not just Account contacts?
- [ ] Field History tracking enabled on Opportunity (so you can see what changed and when)?

**Recording and bot setup:**
- [ ] Call recording tool identified and approved?
- [ ] Bot approved to join Slack workspace?
- [ ] Rep calendar connections established (the most skipped step)?
- [ ] Bot tested on a live call before any rep relies on it for deal intel?

**Intelligence layer:**
- [ ] Stage-based prompts written and ready to configure?
- [ ] Slack channels created: master aggregator + naming convention agreed for opp channels?
- [ ] SF field mapping confirmed between extraction output and actual SF field API names?
- [ ] Test call run and output reviewed before full rollout?

**Security:**
- [ ] Salesforce API access confirmed for the integration user/service account?
- [ ] IT approval obtained for any new bots or connected apps?
- [ ] Data handling reviewed for any PHI or HIPAA considerations if healthcare org?

---

## The One Thing That Will Kill the Rollout If You Skip It

Rep calendar connections.

Everything downstream depends on the bot knowing which calls to join. The bot only knows which calls to join if it reads each rep's calendar. If reps don't connect their calendar — which they won't do unless someone walks them through it live, on a call, with screen-sharing — the bot sits idle. No joins, no transcripts, no summaries, no SF activity logs, no MEDDIC scoring.

At League, Brieann's rollout sequence was: enablement call → welcome email sent the same day → calendar connection as the first and most urgent action item → then Salesforce connection → then actual call recording.

The second thing: clean your contact email addresses before you connect anything. That five-hour data cleanup session before launch will save forty hours of debugging why calls keep routing to `N/A`.

---

*Documented June 2026. Sources: League Slack (Brieann Geddes in #momentum-feedback, #growth-team; Michele Oliveto in #claude-cowork; Doug Tipsword in #growth-enablement; Marissa Thiel in #growth-team); Slack help docs (slack.com/help); Salesforce admin resources (salesforceben.com, salesmethods.com, coffee.ai). Portable — applies to any Salesforce + Slack org regardless of call recording tool or industry.*
