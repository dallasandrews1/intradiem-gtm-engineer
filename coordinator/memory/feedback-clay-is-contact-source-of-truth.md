---
name: feedback-clay-is-contact-source-of-truth
description: "Clay, not Salesforce, is the source of truth for contact data (email, employer, title, phone); settle a lemlist/Salesforce disagreement with a Clay Enrich Person read, never by asking Dallas to check Salesforce"
metadata:
  node_type: memory
  type: feedback
  originSessionId: b37fd0f6-84a0-4d6b-86e3-38bb0786240b
  modified: 2026-09-23T00:05:51.792Z
---

Sep 22 2026, after I told Dallas to check four drifted lemlist emails "in Salesforce": "salesforce isn't the source of truth, clay is."

**Why:** the drift came from the lemlist-Salesforce sync overwriting Clay-verified values. A fresh Clay Enrich Person read showed all four people still at their original employers on their original emails; one lemlist record had even moved a Molina director to a wrong Humana address, and I acted on it before checking Clay.

**How to apply:** when a lemlist or Salesforce contact field disagrees with Clay, run the Clay Enrich Person routine ([[clay-enrich-person-contact-details-routine]]) and restore Clay's value; never treat a changed lemlist email as a job change until Clay confirms it. Hand Dallas a Salesforce task only to push Clay's value into Salesforce so the sync stops reverting it. Related: [[lemlist-salesforce-sync-overwrites-lead-fixes]], [[enrichment-doctrine-clay-not-lemlist]].
