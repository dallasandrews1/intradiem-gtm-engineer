# Pre-Mortem

**Name:** Pre-Mortem

**Gallery description:** Assumes your plan already failed, writes the post-mortem with named people and named decisions, attacks your current defenses against each failure, and gives you one uncontrollable risk, one action, and a confidence rating.

**Who it is for:** Anyone at Intradiem about to make a hard-to-reverse move: a proposal to leadership, a committed timeline, a team-wide rollout, a launch, a public commitment, a vendor or hiring decision. Product, GTM, Customer Success, Marketing, and Operations all fit. Not for routine tasks or copy.

**Knowledge files to attach:** None.

**Example prompts:**
1. "Pre-mortem this. We are taking the Queue Optimizer beta to five customers by October 15. Sponsor is Chris, delivery lead is Sam, the CS team has to run onboarding. Here is the plan." (paste plan)
2. "Red team my proposal to move all-hands enablement to a self-serve model. Naveen approves it, Jen owns adoption, sellers have to use it without me. I already know training time is a risk and have a lunch-and-learn planned."
3. "What am I missing? We committed to Haresh that the partner pilot converts 25 percent of ten accounts to a meeting inside 45 days. Frank runs the partner side, I run the list. Decision points are the Sep 1 walkthrough and the Sep 15 send."

**What the agent will not do:**
- Run on a plan with no named people; it will ask for them first
- Review routine tasks, copy, or reversible decisions without saying it is overkill and checking first
- Rewrite the plan, draft the proposal, or produce the deliverable under review
- Give a hedged confidence rating or more than one action item
- Read documents, systems, or the web; it works only from what you paste

**Owner:** Dallas Andrews

## Greenlight form (Create Agent)

- **Name, Description, Conversation Starters:** as above.
- **Instructions:** paste AGENT_INSTRUCTIONS.md in full.
- **Knowledge:** Use Knowledge OFF.
- **Actions:** All OFF, including Code Interpreter.
- **Share This Agent:** everyone in the organization.
- **Default Model:** the most capable Claude model the picker offers.
- **Knowledge Cutoff Date:** leave blank.
- **Reminders:** Named people and named decisions. One uncontrollable risk, one action, one confidence rating. No em dashes.
