# Prototype builder

**Name:** Prototype builder

**Description (gallery):** Turns a one-page brief or an existing PRD into a working single-file HTML prototype on the Intradiem design system, with the acceptance checks tested inside the file. Download, open, click through in the review.

**For:** Product managers. Also design and engineering when they want to see a screen before it is built.

**Instructions:** paste `motions/ai_champion_product/pm_kit/PROJECT_INSTRUCTIONS.md` in full.

**Knowledge files to attach:**
- `pm_kit/DS_Tokens.md` (DS v1 per the Skills Editor PRD; replace with design's current sheet when they send one)
- `pm_kit/Prototype_Brief_Template.docx` (so the agent can hand a PM the blank brief on request)

**Conversation starters:**
1. Build the prototype from the attached brief.
2. Build the prototype for Screen [number or name] from the attached PRD. Draft the brief first and show it to me before building.
3. Check [number] fails: [paste the line from the Checks panel]. Fix that and keep everything else the same.
4. Give me the blank prototype brief and tell me which two sections matter most.

**What it will not do:** fetch anything from the web or SharePoint, invent chrome outside the token sheet, ship a control that does nothing, fill in the decision record (section 8 is the PM's), or claim a check passes that it did not compute.

**Worked examples:** pm-builder.pages.dev/prototype/ (Skills Editor PRD v2.0) and pm-builder.pages.dev/prototype-2/ (Scheduling Service PRD v1.0, Screen 7, built from these instructions alone).

**Owner:** Dallas Andrews, AI champion, Product.

## Greenlight form (Create Agent)

- **Name, Description, Conversation Starters:** as above.
- **Instructions:** paste ../pm_kit/PROJECT_INSTRUCTIONS.md in full.
- **Knowledge:** Use Knowledge ON: DS_Tokens.md, Prototype_Brief_Template.docx.
- **Actions:** Code Interpreter ON (it produces the downloadable index.html). Everything else OFF.
- **Share This Agent:** everyone in the organization.
- **Default Model:** the most capable Claude model the picker offers (this agent writes working code; the strongest model matters most here).
- **Knowledge Cutoff Date:** leave blank.
- **Reminders:** Return the whole index.html as one downloadable file, never a snippet. Lead the handover with the N pass, N fail, N manual line. No em dashes.
