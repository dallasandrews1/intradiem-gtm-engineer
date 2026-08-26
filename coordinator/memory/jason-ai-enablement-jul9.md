---
name: jason-ai-enablement-jul9
description: "Jul 9 2026 intro call with Jason (Manager, AI Enablement): Zuar data hub + MCP, hosting rules (Power Apps/Azure Apps, no Claude-at-runtime), Greenlight roadmap (doc creation shipped, skill attachment next, then agent workflows), VS Code+Mem0 pattern, his explicit asks"
metadata: 
  node_type: memory
  type: project
  originSessionId: edfe77c7-6120-4e44-b06f-69692e43ccbd
---

Intro call Jul 9 2026, set up by Naveen. Jason = Manager, AI Enablement (the "Jason #2 / AI engineer" from [[naveen-jul8-meeting]]; distinct from Jason Dowden VP Technology). Runs Greenlight and all internal AI projects. GTM engineering formally sits under the AI Enablement initiative (sponsored by "Jen," board-level). Action plan saved at Jason_AI_Enablement_Action_Plan.md in project folder.

**His stack/rules:** Zuar is the data one-stop shop (Salesforce, ChurnZero, 6sense pulled into Zuar's DB; Zuar MCP connection exists, beta; avoids Salesforce API restrictions/call limits). Standing offer: ask him "do we have a connection to X?" before building any pull. Microsoft Graph API MCP planned; SharePoint/Confluence full of stale data, scope queries to ~last 6 months. Hosting goes through him: simple browser things → Microsoft Power Apps, involved things → Azure Apps; HARD RULE: he will not host anything that calls Claude at runtime. He's building an intake form for scoping requests, use it.

**Greenlight roadmap (iterative):** document creation just shipped (branded templates, he claims it beats Claude), NEXT = skill attachment, then agents assigned to workflows (orchestrator + sub-agents, e.g. Salesforce sub-agent with MCP-optimized instructions). Greenlight will eventually clone Cowork internally ("I'm just gonna steal cowork"). JD spent ~6 hours writing one skill, so pre-built skills relieve real pain. Dallas offered his skill library; Jason accepted (they'll pick and choose).

**His explicit asks of Dallas:** (1) send him the list of Anthropic/Claude features worth cloning internally ("people never follow up," easy trust win); (2) route data-connection and hosting needs through him; (3) VS Code questions welcome anytime. He told Naveen on-call: "go get him a license."

**His VS Code pattern (Dallas committed to adopting):** moved 100% to Claude Code in VS Code even for non-code work (control over skills/CLAUDE.md without desktop harness); coordinator folder holding memory + instruction sets, opened as multi-root workspace alongside active projects; Mem0 ("Mem Zero") memory layer auto-updating after every action, "never forgets"; CLI-as-connector when no MCP exists (e.g. Azure CLI). Dallas also promised to help Naveen projectize his Claude threads (Naveen asked on-call).

**Migration note:** cross-account chat migration is impossible (Jason confirmed); Dallas's plan = zip memory/artifacts/docs + markdown onboarding file into an Enterprise project when license lands. Naveen post-call: "very close to getting your license."
