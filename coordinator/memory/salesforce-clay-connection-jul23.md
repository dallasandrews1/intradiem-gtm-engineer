---
name: salesforce-clay-connection-jul23
description: Salesforce-to-Clay connection approved Jul 23 2026; intended job is to make the customer-exclusion gate live instead of Nate's static Jul 10 export
metadata:
  type: project
---

Jul 23 2026: Dallas got the Salesforce -> Clay connection approved. Primary intended use is to make the `customer_exclude` gate LIVE (24h auto-resync) instead of running off Nate's static Jul 10 SF export (101 accounts, see [[customer-file-landed-jul10]]). Enrichment (account owner, open opps) and write-back are secondary; write-back stays OFF until Dallas explicitly says so (dry-run default + [[nobody-but-dallas-routing-rule]]).

How the connection works (for future instructing):
- It is a ONE-WAY PULL: Clay reaches into Salesforce and reads. There is NO Clay panel/button inside the Salesforce UI. You never "use Clay from inside Salesforce."
- The REPORT lives in Salesforce (Accounts object, tabular, max 2,000 rows, must include Account ID + Name). Everything else is configured in Clay.
- Clay entry point: open a table -> **Tools -> Import** -> search Salesforce (the `+ Add` "workbook button" is just the small tab-style `+` at bottom-left next to table tabs; Dallas couldn't find it, Tools -> Import is the unambiguous path).
- Clay import settings: SF account (OAuth) / import type = Report / pick report / Uniqueness field = Account ID (dedupe) / columns / sync 24h default / Import to NEW table.

Safe rollout (ordering trap): import SF customer list as a NEW isolated table FIRST, reconcile against the 101 (find new-customers-since-Jul-10 = the real leak risk), and only THEN repoint the `customer_exclude` gate (col f_0thzalcNJ5VDtBRUcri on Accounts(Master) t_0thuumoUcu6wAAhovti). The gate repoint runs on REAL rows (never synthetic --input) and is Dallas's hand. Write-back, when eventually enabled, = Update record keyed on Record ID (never Create) with "Ignore blank values" on.

Reuse Nate's existing report/filter that produced the Jul 10 101-account export rather than rebuilding the customer definition.

**RESOLVED Jul 26:** Dallas confirmed the SF OAuth handshake is complete — done in a separate session working directly in Clay. The "still blocked" claim from the other Claude Chat session was stale/wrong. Status of the downstream steps (new isolated table, reconciliation vs the 101, gate repoint) not yet reconfirmed as of this note — check current state before assuming the full rollout (not just OAuth) is finished.
