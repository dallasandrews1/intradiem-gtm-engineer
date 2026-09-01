---
name: clay-sf-audiences-integration-jul23
description: Clay Audiences is live-synced to Salesforce (import-only/read-only) as of Jul 23 2026; write-back spec'd but held pending Eric sign-off
metadata:
  type: project
---

As of 2026-07-23, Clay **Audiences** (the CRM-connected account layer, separate from Clay tables) is live-connected to Intradiem's Salesforce via the Client Credentials integration (connected app; My Domain intradiem2023.my.salesforce.com). Eric Ebeling is Senior Salesforce Admin and owns the SF side.

**Import (live, read-only):** All four objects imported, all exports OFF. Accounts ~2.3K, Contacts ~125.3K, Leads ~16.3K, Opportunities ~7.8K (~152K total; Tasks 177.4K and Events 5.8K deliberately left OFF to protect the record ceiling). Record matching: Companies matched on domain→SF Website. Plan tier / Audiences record ceiling still `[UNVERIFIED]`.

**Intended use (per strategy this session):** Audiences is the live top-of-funnel (sourcing + segmentation + customer-exclusion + signals) that FEEDS the existing Clay motion tables. It does NOT replace the send machinery. First two audiences: (1) Current Customers exclusion segment (Type=Customer OR won Opportunity) to retire the fragile `customer_exclude` text hack in the tables, (2) Star Ratings universe from StarRatings_CliffEdge_Target_List.xlsx via CSV import.

**Write-back (SPEC'D, HELD):** Decisions locked — net-new people created as **Contacts under the Account** (ABM); **Clay owns campaign membership + status** (Clay's own sequencer via Outlook is the only system that knows send/reply state). Spec at `Desktop/Intradiem Deliverables/Clay_SF_WriteBack_Spec.pdf (source: Intradiem GTM Engineer/Clay_SF_WriteBack_Spec.html)`. Guardrails: account-level customer-exclusion gates record CREATION (not just sending), dedup across Contacts+Leads on email, real-row validation first. Clay SF write-back is IRREVERSIBLE (no undo), so nothing enabled until Eric signs off. Open for Eric/Sales-ops: contact ownership on create (cold contacts appearing on AE accounts = change-mgmt), campaign naming/ownership, whether Einstein Activity Capture already covers Outlook activity.

Related: [[steps-in-dependency-correct-order]] [[verify-dont-theorize]] [[orchestrator-not-manual-directive]]
