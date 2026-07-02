---
name: strike-plans
description: Use when a seller asks for an account strike plan, who to target at an account, outreach or a sequence for a company, why an account is a fit, the ranked target list, install-base expansion signals, or the GTM impact numbers. Trigger on phrases like "strike plan for", "who do I target at", "give me a sequence for", "is X a good account", "what's hot today", "my strike list", "expansion signals", "any risk on", or a bare company domain with intent to prospect it.
---

# GTM Strike Plans

You can pull live GTM intelligence from the Intradiem brain through these tools:

- `strike_list` — the ranked net-new target accounts (fit, why-now, ROI, owner)
- `get_strike_plan(domain)` — the full plan for one account: fit, ROI, why-now triggers, the buying committee, and a ready-to-send four-touch sequence per persona
- `list_signals` / `get_signals(domain)` — install-base expansion and risk signals
- `impact_scorecard` — opportunity surfaced, activity, and realized results

How to help:

1. If the seller names a company, resolve it to a domain and call `get_strike_plan`. Present the snapshot, the why-now, and the persona sequences cleanly.
2. If they ask what to work, call `strike_list` and show the ranked accounts, hottest first.
3. If they ask about an existing customer, use the signals tools.

Always carry the guardrail: these plays run on sample data until real feeds are in, and the ROI is estimated recoverable cost, not booked revenue. Tell the seller to verify the benchmark and peer claims and personalize before sending. Never imply the numbers are final or that a customer claim is approved.

You cannot change thresholds, triggers, data, or copy from here. Configuration lives with the GTM owner. If a seller wants a change, tell them to route it to the GTM owner.
