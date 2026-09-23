---
name: customer-leak-scan-sep23
description: Sep 23 2026 lemlist customer scan; BO Expansion lanes are customers by design, Citizens blitz sync-reverted to ADT, paused WFM/DWO/Genesys campaigns hold true customers
metadata:
  type: project
---

Sep 23 2026, from Keegan's flag in #gtm-outbound-nathan (C0BM9V6KGSG). Full scan of every lemlist campaign through automation/customer_gate.py; log automation/logs/customer-leak-scan-2026-09-23.md.

- BO Expansion FS / Payer v2 / Insurance v2 / BPO v2 are the install-base customer lane ON PURPOSE (Nathan confirmed, Aug 24 strategy). Do not treat those hits as leaks. AM clearance filter was dropped Sep 2; the open question is AM awareness, not exclusion.
- Blitz - Citizens reverted a third time (Bartolazo to adt.com, a customer; Weaver to voya.com) while running. Restored Sep 23 by update_lead; will revert until Salesforce is corrected. See [[lemlist-salesforce-sync-overwrites-lead-fixes]].
- Paused WFM Tool Users, DWO Executives Live Pool and Genesys No WFM Tool hold true customers (Cigna/Express Scripts/Evernorth, Duke Energy, BT, McKesson). Pull before any resume.
- customer_gate.py matches loosely: Capital Group, Progressive Leasing, US Bancorp and Amex GBT produce false hits; read the hit before acting.
