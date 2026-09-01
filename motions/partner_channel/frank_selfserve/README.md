# Frank self-serve path (Sep 1 2026)

Two lanes so Frank runs briefs daily without Dallas in the loop.

## Lane A: shared Claude Project (today, no build)
Frank uses Cowork daily; in Claude Enterprise the shareable unit is a Project on claude.ai (a Cowork session itself cannot be shared). Setup, Dallas's hands, about 5 minutes:
1. claude.ai > Projects > New project: "Partner Account Briefs".
2. Paste `Project_Instructions_Partner_Briefs.md` into the project instructions.
3. Add to project knowledge: the partner-safe Ally and Maximus briefs (html or the text), and the pilot design page text. Nothing with 3xG seat counts, nothing from the internal versions.
4. Share the project with Frank (and Matt/Nigel when ready).
Frank then types "brief Christus Health" in Cowork inside that project and gets the structured brief with web research. He can paste the canvas version straight into a Slack canvas.

What Lane A deliberately cannot do: Clay contact sourcing, the customer/partner gate against Salesforce, the branded two-version pages, deploys. Those stay on the engine so credits and gates never depend on Frank's prompt discipline.

## Built after the Sep 1 call (Frank approved the direction on the spot)
- `skills/partner-account-brief/` and `skills/partner-followup-onepager/`: the two skills Frank asked for. Skill 1 runs the brief (single account or pasted rep list, 5 per sitting). Skill 2 is the "what if they say yes" follow-up: a one-page DWO piece built from the brief's specific findings, approved claims only, Intradiem brand tokens and logo baked into the skill. Zips staged in the Desktop folder under Skills for Frank.
- Delivery per the call: Dallas creates the "Partner Account Briefs" project in Cowork, flips visibility to Intradiem (the sharing option Dallas found live on the call), shares to Frank, and walks him through skill install on the afternoon follow-up call. Frank tries one account, then the new C1 rep's list (Frost Bank, Integris, Cognizant and others) is the first real account-mapping run.
- Skill 3 (branded document builder for the polished one-pagers) waits until Dallas settles the visual format; Frank also owes Dallas his current partner-facing materials to seed the bank.

## Lane B: the request loop (engine-grade briefs on demand)
Frank posts an account name in a #gtm-partner-briefs Slack thread (or a shared canvas list). A scheduled watcher picks up new names, runs the full pipeline (gate, researcher fan-out, free-path contacts, two pages, deploy of the partner-safe copy), and replies in thread with the links. Follows the swarm rules: writes a log the daily rundown reads, never DMs Dallas, posts only to the request thread. Not built yet; build prompt below.

## Alternative surface: Greenlight shared agent
If leadership prefers the blessed platform, the same instructions file becomes a "Partner Account Briefs" shared agent using the greenlight_agents pack pattern (register, create order, knowledge = this file plus the two partner-safe briefs). Same limits as Lane A. Say the word and the agent card gets generated.
