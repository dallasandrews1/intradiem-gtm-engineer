# Competitive Intel

**Name:** Competitive Intel

**Gallery description:** Paste a call note, email, or RFP passage where a competitor comes up and get an internal brief with the operational wedge, the reframe, questions to plant, and talking points for the next call.

**Who it is for:** Account executives, account managers, and sales engineers in a live deal where Verint, NICE, Calabrio, Genesys, Assembled, Playvox, an in-house build, or "we're evaluating options" has been named. Also useful to marketing and product marketing when drafting competitive positioning.

**Knowledge files to attach:**
- Intradiem_Value_Repository.md (required; without it the agent produces no numbers)
- Customer_Value_Registry.md (optional; internal-only figures, never quoted in a brief)

**Example prompts:**
1. "Centene, Healthcare, contact center and claims. On today's call the VP of Care Ops said they already have Verint and are 'waiting for the automation module.' Here's the transcript excerpt: [paste]. Build the brief."
2. "Regions Bank, Financial Services, back office. RFP section 4.2 lists NICE and an internal RPA program as alternatives: [paste]. What's the wedge and what should we ask them to ask NICE?"
3. "Prospect at a utility said 'our supervisors handle intraday, we're just looking at vendors.' No competitor named. Give me the status-quo brief and four questions to plant."

**What the agent will not do:**
- Look anything up. It has no web access and no account database; it works only from what you paste.
- Quote a number that is not in the attached Value Repository, or strengthen a customer claim beyond its source.
- Disparage a competitor with a claim it cannot support. Inferences are labeled as inferences.
- Write prospect-facing copy. Every brief is internal-only; the seller adapts it in their own words.
- Position WFM vendors as head-to-head replacements. Intradiem acts on top of the WFM the customer already owns.
- Answer with a partial brief when the competitor, account, vertical, or raw material is missing. It asks for all of it in one message first.

**Owner:** Dallas Andrews

## Greenlight form (Create Agent)

- **Name, Description, Conversation Starters:** as above.
- **Instructions:** paste AGENT_INSTRUCTIONS.md in full.
- **Knowledge:** Use Knowledge ON: Intradiem_Value_Repository.md (required).
- **Actions:** All OFF for v1. (v2 option: Web Search ON, with one added instruction line saying what it may search for.)
- **Share This Agent:** everyone in the organization.
- **Default Model:** the most capable Claude model the picker offers.
- **Knowledge Cutoff Date:** leave blank.
- **Reminders:** Internal brief only. Label inferences as inferences. Any figure not in the attached repository is [UNVERIFIED]. No em dashes.
