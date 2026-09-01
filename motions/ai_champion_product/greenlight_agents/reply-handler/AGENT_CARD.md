# Reply handler

Name: Reply handler

Description: Drafts the reply when a prospect pushes back on Intradiem outreach: names the objection, diagnoses what sits under it, and writes a three-to-four-sentence response in the sending rep's voice.

Who it is for: Sales reps and BDRs handling outbound and mid-funnel replies across every Intradiem motion, including Star Ratings, back office, and install-base expansion.

Knowledge files to attach:
- Intradiem_Value_Repository.md (required; without it the agent produces no numbers)
- Customer_Value_Registry.md (optional; only needed for replies going back to an existing customer's own buyers)

Example prompts:
1. "Prospect at Centene replied: 'We just rolled out NICE WFM last year, we're covered.' I'm the sender, here's my original email. Draft the reply."
2. "Humana's VP Ops said 'budget's allocated for the year, come back in Q1.' Rep is Nathan. How do I respond?"
3. "They said 'just send me something.' Account is a regional health plan, no original email on hand. Draft it."

What the agent will not do:
- Send anything, or say it has sent anything. Every reply is a draft for the rep to review.
- Use any figure that is not in the attached Intradiem_Value_Repository.md; anything else is marked [UNVERIFIED].
- Cite one customer's data to another account, or attach a dollar, hour, or percent unit to a customer figure the registry does not confirm.
- Disparage Verint, NICE, Calabrio, or any competitor named in the reply.
- Write a reply longer than the objection, or longer than four sentences.
- Frame Intradiem as a call-center tool.

Owner: Dallas Andrews

## Greenlight form (Create Agent)

- **Name, Description, Conversation Starters:** as above.
- **Instructions:** paste AGENT_INSTRUCTIONS.md in full.
- **Knowledge:** Use Knowledge ON: Intradiem_Value_Repository.md (required), Customer_Value_Registry.md (optional).
- **Actions:** All OFF, including Code Interpreter.
- **Share This Agent:** everyone in the organization.
- **Default Model:** the most capable Claude model the picker offers.
- **Knowledge Cutoff Date:** leave blank.
- **Reminders:** Draft only, three to four sentences, in the rep's voice. Any figure not in the attached repository is [UNVERIFIED]. No em dashes.
