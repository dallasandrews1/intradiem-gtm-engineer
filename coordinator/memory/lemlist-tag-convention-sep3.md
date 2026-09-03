---
name: lemlist-tag-convention-sep3
description: Sep 3 2026: lemlist campaign tags (labels) are two hyphenated tags per campaign, gtm-engineering on everything the engine builds plus a motion tag (gtm-engineering-stars, -blitz, -bo, -uk); tags are UI-only and not readable by API, automation keys on campaign ids
metadata:
  type: project
---

Decided Sep 3 2026 with Dallas. Every lemlist campaign the GTM engine builds carries two tags, set in the campaign's Settings gear, General, "Add tags" (lemlist calls labels tags; docs: help.lemlist.com/en/articles/5071155): `gtm-engineering` (the channel roll-up for the pipeline council's cost-per-meeting view in Reports) plus one motion tag, hyphenated: `gtm-engineering-stars`, `gtm-engineering-blitz`, `gtm-engineering-bo`, `gtm-engineering-uk` (Jack). Spaces are allowed in lemlist tags but the hyphen form is the standard because the first tag was created that way. Tags are not exposed by the lemlist API, so the relay map (automation/config/lemlist_channels.json), the receipts tracker and the integrity sweep key on campaign ids; every new campaign gets its id added to those maps at build time and the tags applied in the UI.

**How to apply:** when a new campaign is built by API, the post-create checklist is schedule timezone, sender, and the two tags (UI), plus the campaign id in the relay map. Related: [[lemlist-api-campaign-defaults-sep2]], [[bo-netnew-package-sep2]], [[pipeline-council-context-aug24]].
