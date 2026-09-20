---
name: lemlist-salesforce-sync-overwrites-lead-fixes
description: "Sep 20 2026: lemlist's Salesforce CRM sync overwrites lead corrections on any lead linked to a Salesforce Contact; the Sep 18 Keegan blitz fixes were reverted within a day; fix Salesforce first or the lemlist fix does not hold"
metadata:
  type: project
---

**What happened:** the Sep 18 2026 corrections to the Citizens blitz leads (Bartolazo adt.com, Weaver voya.com, Foss switchboard) landed, then were overwritten in one batch on Sep 19 2026 at about 07:40 to 07:46 UTC with no activity logged. Hartford lost three corrections the same way (Lyon, Beausoleil, Batman), and Higgins's phone at Citizens. Re-applied to the three Citizens leads Sep 20 and proven by re-read.

**Cause (LIKELY, strong):** the lemlist team is connected to Salesforce with a bi-sync flag. The reverted leads carry `salesforceContactId` and `isSyncBetweenLemlistAndCrm: true`; untouched leads carry neither. The Salesforce Contacts still hold the stale values (Salesforce-known titles and emails on these accounts are mostly stale, see [[keegan-three-account-package-sep17]]). Sync logs, direction and field mapping are not readable through the connector.

**How to apply:**
- Before correcting any lemlist lead, check for `salesforceContactId`. If present, the Salesforce Contact must be corrected first (or sync unlinked for that lead), otherwise the fix lasts until the next sync.
- A lemlist-lead-integrity PASS on a Salesforce-linked lead is a point-in-time read, never a standing state. Re-read right before any wave or before anyone clears a task queue.
- Wrong-company emails are the dangerous case (they deliver and never bounce); phones and titles are lower severity.
- Blitz - Citizens was left PAUSED on Sep 20 2026 for this reason; resume is Dallas's call.

Related: [[keegan-package-refresh-sep20]], [[keegan-execution-kit-sep18]], [[enrichment-doctrine-clay-not-lemlist]].
