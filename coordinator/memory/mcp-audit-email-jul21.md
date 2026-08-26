---
name: mcp-audit-email-jul21
description: The two custom MCP servers submitted to Intradiem IT for approval (Jul 21) and the audit-intake format Jason Jones defined; memory stays local, not submitted
metadata:
  type: project
---

Jul 21 2026: Drafted the email that kicks off IT's MCP audit process so Dallas's custom connectors can attach to the work Claude Enterprise account. Goes to Jason Jones (jason.jones@intradiem.com) and JD / Jason Dowden (jason.dowden@intradiem.com, VP Technology). Jason's required intake format per his Jul 17 DM: for each connector state **what it is / what it does / why you need it**, and that kicks off the audit.

The two custom MCP servers (both local Python FastMCP stdio servers, read local files only, no external calls, which is the fast-approval story):
- **`intradiem-tam`** — TAM Outbound Engine, `Intradiem GTM Engineer/tam-outbound-engine/tam_mcp_server.py`. Tools: list_strike_accounts, get_strike_plan, accounts_for_seller, add_strike_account.
- **`intradiem-signals`** — GTM Signal Engine, `Intradiem GTM Engineer/intradiem-signal-engine/intradiem_mcp_server.py`. Tools: get_expansion_signals, list_monitored_accounts, score_all, add_monitored_account.

Decisions Dallas made shaping the draft: **Memory is NOT an audit item and is not mentioned at all** — Dallas caught that giving local memory the what-is/does/why breakdown reads like a submission, and since Jason already said no to mem0, referencing memory only reopens a closed negative topic; the local repo speaks for itself. See [[mem0-enterprise-compliance-flag-jul17]].

**Share method: sanitized ZIP attachment, NOT personal GitHub.** The GTM Engineer repo has no git remote and the engine `data/` CSVs carry real customer flags (customer_flag/install_base on Humana, Capita, etc.) + internal rep emails; putting that on personal GitHub during a data-governance audit is bad optics. Built `~/Desktop/Intradiem_MCP_Connectors_Review.zip` (56K): both engine folders, code + config + README + tests, every data CSV stripped to header-only, generated JSON outputs removed, AmeriHealth example dropped. Dallas then said NO prospect names at all: so all three test_*.py files were REMOVED (they named AmeriHealth/HCSC/Centene/Synchrony/CareSource/Molina/Ally and couldn't pass without data anyway), and leftover usage-example domains in READMEs/docstrings swapped to `example.com`. Final zip = 49K, code + config + README + header-only data; word-boundary scan confirmed zero prospect names; only domains left are intradiem.com/slack.com/example.com. Env-based SLACK_BOT_TOKEN reads left in (good security signal). Email includes deploy footprint inline: Python 3.10+, `pip install mcp`, per-connector `command`/`args` MCP registration JSON. Offer to push to Intradiem Bitbucket (sanctioned) if they want a repo.

Outlook MCP (Microsoft 365 connector) was NOT authorized this session — `outlook_create_draft` returned "tool not available," so the draft could not be placed programmatically; Dallas pastes the body into Outlook manually + attaches the Desktop zip. To enable next time: authorize Microsoft 365 in claude.ai connector settings. gh CLI authed to personal `dallasandrews1` (unused — chose zip over GitHub). See [[work-machine-operational-jul20]] (other MCPs await IT).
