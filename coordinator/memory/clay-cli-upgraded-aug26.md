---
name: clay-cli-upgraded-aug26
description: "Aug 26 2026: Clay plugin updated 2.6.0 to 2.13.0, pinned CLI 0.5.0 to 0.12.0 (the API had started rejecting 0.5.0 with upgrade_required); PATH shim repoints after a Claude Code restart; cohort_cutter and heat_list_scorer wrappers now resolve the newest plugin bin via ls -td; Audiences records CLI (search-count/search-ids/get) works and the SF Cold-Outbound Exclusion segment is audseg_0tk324emMVGAwsna7g4 (127 companies), Current Customers audseg_0tk31v7TVNZnw5yRnVf (86)"
metadata:
  type: project
---

- Upgrade path is the plugin, not the binary: `claude plugin marketplace update clay-plugins` then `claude plugin update clay@clay-plugins`; the shim in `~/.claude/plugins/cache/clay-plugins/clay/<ver>/bin/clay` downloads the pinned CLI on first use. Until Claude Code restarts, PATH still points at the 2.6.0 shim; call the 2.13.0 shim by full path in the meantime.
- Automation: `run_credit_check.sh` already resolves newest by `ls -t`; `run_cohort_cutter.sh` and `run_heat_list_scorer.sh` had `2.6.0` hard-pinned in PATH and were changed Aug 26 to `$(ls -td .../clay/*/bin | head -1)`.
- Live customer union from the CLI, 0 credits: `clay audiences records search-ids --entity-type companies --audience-id audseg_0tk324emMVGAwsna7g4 --limit 200` then `records get --ids` in batches of 100; fields `org_name`, `normalized_domain`, Account Type `audf_0timw0xX6CfUdJXJznM`. The Clay MCP `query-objects` still needs a Salesforce User sync and errors.
- Supersedes the "0.5.0 pinned" note in [[clay-audiences-live-cli-capability-aug20]].
