---
name: lemlist-api-campaign-defaults-sep2
description: Sep 2 2026: campaigns created by the lemlist API get a Europe/Paris 09:00-18:00 default schedule, no sender, and no label; every API-built campaign needs a schedule PATCH to America/New_York plus sender and label before launch
metadata:
  type: project
---

Found Sep 2 2026 while finishing the five back-office campaigns: `POST /api/campaigns` attaches a "Default schedule" in **Europe/Paris**, 09:00-18:00 Mon-Fri, 20-minute gap. Nathan's running campaigns use America/New_York. Left alone, the BO campaigns would have sent between 3 a.m. and noon Eastern. Fix by API: `GET /api/campaigns/{id}/schedules` for the skd_ id, then `PATCH /api/schedules/{skd}` with `{"timezone":"America/New_York"}`. Also true of API-built campaigns: senders come back empty (fixable now with the lemlist MCP `set_campaign_senders`, Nathan is usr_9rxD82ZfapeZBGSoz) and labels are not exposed anywhere in the API (UI only). Step edits by API need `type` in the PATCH body.

**How to apply:** add "schedule timezone, sender, label" to the post-create checklist for any campaign shell built by API (motion-stamp, BO builds, Jack's UK campaigns). Verify with `get_campaign_details` + the schedules GET before calling a campaign ready. Related: [[bo-lemlist-shells-built-sep2]], [[bo-netnew-package-sep2]], [[lemlist-api-sequence-step-limits-aug31]].
