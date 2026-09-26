---
name: dwo-exec-recut-sep26
description: "Sep 26 2026: DWO executive campaign (803 leads, paused) re-cut to the service track with the ACD in the product sentence and DWO named once; canon entry dwo-exec-service-track-sep26; review canvas F0C5JCP1F4G staged for Dallas to post; lemlist lead variables write via POST /api/leads/{id}/variables"
metadata:
  type: project
---

Applied on Dallas's ask after a review of the live copy against the week's decisions (Naveen Sep 23: ACD in the DWO sentence; Jennifer East Sep 24: service track for ops and client-service seats; Cheryl Sep 25: idle figure once, never the closing question; Sep 4 pressure standard: no "fair enough"). Records in `motions/dwo_executives/recut_sep26/` (recut.py, PLAN.json, APPLIED.json), log `automation/logs/dwo-exec-recut-2026-09-26.md`.

**How to reuse:** lead variables go through `POST /api/leads/{lead_id}/variables` with the lead `_id` from the campaign CSV export (`GET /api/campaigns/{id}/export/leads?state=all`, CSV not JSON, read it raw). Step writes need `type` in the PATCH body. Long REST loops need retries; a bare urllib call to api.lemlist.com timed out mid-run once.

**Still open:** the group's nine on ten (Dallas posts the canvas to the GTME thread himself), then Dallas's go to resume; the 346-account Salesforce match (accounts are Clay-sourced, 96 percent not in Salesforce) before results can land in Pipeline Council. Related: [[john-exec-brief-biweekly-sep26]], [[vanguard-service-message-jenn-east-sep24]], [[bo-messaging-alignment-sep25]], [[feedback-messaging-canon-is-the-source]].
