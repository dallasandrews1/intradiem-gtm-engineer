---
name: feedback-enrich-in-clay-never-lemlist
description: "Sep 3 2026 rule from Dallas: never enrich on lemlist (no findEmail, verifyEmail, findPhone, linkedinEnrichment, enrich_lead); Clay is the only enrichment surface, lemlist is the sequencer"
metadata:
  type: feedback
---

Sep 3 2026, after a lead add with verifyEmail on turned out to be a no-op (lemlist credits at zero): "never try to enrich on lemlist we have Clay for all enrichment needs."

**Why:** lemlist enrichment spends a separate, unmanaged credit pool that reads zero, gives no result field back on the lead, and splits the audit trail. Every enrichment dollar and every verification result is supposed to live in Clay, where the ledger, the ZeroBounce status and the two-source email rule already exist.

**How to apply:** on add_leads_to_campaign and import, leave findEmail, verifyEmail, findPhone and linkedinEnrichment off, always. Never call enrich_lead, bulk_enrich_data or the /enrich endpoints. Emails, phones, LinkedIn URLs and freshness come from Clay (work-email workflow wf_0tk4jo5z7RjGKo3rvR8, Enrich Person, the free bridge) before the load; lemlist receives finished rows only. Related: [[lemlist-enrichment-credits-zero-sep3]], [[quality-fresh-pull-sep3]], [[clay-free-sourcing-path]].
