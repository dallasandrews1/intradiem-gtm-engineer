---
name: lemlist-salesforce-create-on-sync-off-sep23
description: "Sep 23 2026 evening: Dallas turned off lemlist's create-in-Salesforce-on-sync; verified by canary (new contacts no longer carry isSyncBetweenLemlistAndCrm); the 108-person Keegan former-customer roster is now a lemlist list, clt_zfPgevBcfyawwpP8L, no campaign"
metadata:
  type: project
---

**What changed:** on Sep 23 2026 Dallas changed the lemlist Salesforce integration so new lemlist contacts no longer create Salesforce leads. The API exposes no toggle; `crmType` still reads salesforce and the `crmBiSyncOnCreateCrmOnUpdate` beta flag still shows, so neither is evidence either way.

**How it was verified:** the per-contact marker. Contacts created before the change (Brian Parrish, 14:40 UTC) carry `isSyncBetweenLemlistAndCrm: true`; a canary created after it (Bryan Takvorian, 23:35 UTC) carries no sync flag and no Salesforce id. Read a fresh contact's raw record with GET /api/contacts/{id} to re-check before any future bulk load.

**What was loaded:** "Keegan's TAM - former customer alumni (verified Sep 23)", list clt_zfPgevBcfyawwpP8L, 108 contacts (84 employer-domain emails, 9 personal addresses left blank, 24 LinkedIn + mobile only), custom fields parentAccount and motion. Not in any campaign, nothing sent. Dallas's morning 31-person list of the same name is superseded and left in place.

**Still true:** leads already linked to a Salesforce Contact still bi-sync and still revert fixes ([[lemlist-salesforce-sync-overwrites-lead-fixes]]).

Related: [[keegan-call-asks-built-sep23]], [[feedback-never-send-as-dallas]].
