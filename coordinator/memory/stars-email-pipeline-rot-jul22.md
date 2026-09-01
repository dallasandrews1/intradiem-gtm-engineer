---
name: stars-email-pipeline-rot-jul22
description: Jul 22 — Stars Contacts table email waterfall was deleted; current 46 survive on SalesNav+lookup+ZeroBounce; Proofpoint false-negative handling; queued waterfall rebuild + orphan cleanup
metadata:
  type: project
---

Jul 22 2026: diagnosed a rotted email pipeline on the Stars Contacts table (t_0thtm73HHxyiupTuepK) while unblocking the 46-lead re-send.

ROOT CAUSE: an entire enrichment/email-finding WATERFALL column family was deleted (the `f_0thvsf...` block: f_0thvsf9, f_0thvsfd, f_0thvsfg, f_0thvsfk, f_0thvsfn, f_0thvsfr). Its deletion cascaded: the "Email" column (f_0thtm75SRgJxZBohRZm) lost its source and got repointed to SalesNav Full Name (showing NAMES not emails); email_final only had the lookup; Status couldn't populate (no address to validate); the workflow's 3g Existing-email gate errored "missing required inputs: email_status" on the rows with no email. Snapshot confirms NO find-email/waterfall action columns survive (only "Get professional posts" + "Send table data"); 6 orphan {{f_0thvsf...}} refs + New Column (2)-(11) formula deps remain.

FIX APPLIED (Dallas, Jul 22): email_final coalesce = `{{Lookup Single Row in Other Table (2)}}?.record?.Email || {{Rows from: SalesNav Staging (Persona Pull)}}?.["Email"] || ""`; "Email" column repointed to SalesNav `?.["Email"]`. The real emails survive live in TWO places: the SalesNav Staging source object (`?.["Email"]` + `?.["Email Status"]`) and the lookup (Other Table 2 `record.Email`). ZeroBounce (Validate Email -> Status) is intact and is the authoritative validation the gate reads. Validate Email is a manual button action (run_as_button), so Status only fills after it's run. Gate stays STRICT (email_status required) — no hardening (Dallas's call).

DECISION — Proofpoint/security-gateway false-negatives: ZeroBounce marks Proofpoint/Mimecast-protected mailboxes "invalid / mailbox_not_found" because the gateway blocks the SMTP probe (classic false-negative). centene.com is Proofpoint, so the whole Centene cohort may read invalid. STANDING CALL: keep the automated gate strict (protects automated sends), but for MANUAL Nate send docs INCLUDE security-gateway invalids (proofpoint/mimecast + mailbox_not_found) FLAGGED ("ZeroBounce couldn't verify through the gateway; delivered in wave 1; your call"), since they already received wave 1 and Nate sends individually. Genuine invalids on normal providers = exclude.

NOT a blocker for the 46 (emails sourced from surviving columns). But NET-NEW email SOURCING is gone until rebuilt.

QUEUED (after the send, own task): (1) rebuild the email-finding waterfall and bake it into the golden scaffold so a column delete can't sever the email chain again; (2) hygiene pass to clean the 6 orphan f_0thvsf refs + New Column (N) deps (table-hygiene agent's safe-delete/repoint plan). Ties to [[stars-messagegen-v24-nate-feedback-jul22]] and the row-actions-use-filters + always-confirm-live-clay rules.
