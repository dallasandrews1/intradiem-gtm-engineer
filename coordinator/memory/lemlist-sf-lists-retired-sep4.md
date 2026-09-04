---
name: lemlist-sf-lists-retired-sep4
description: Sep 4 2026 - the three (SF) Salesforce-mirror lemlist contact lists were retired (contacts deleted, not just unlisted) via retire_sf_lists.py; wave 1 of the DWO live pool (1,060 contacts) loaded the same morning
metadata:
  type: project
---

Sep 4 2026 morning. Wave 1 of DWO Executives, Live (Clay) `clt_Fg8mhEJ7F9uRK9go3` was loaded via `reconcile_dwo_wave.py --go`: 1,060 contacts, 758 with verified email (staged), rest needs_email by LinkedIn URL; 1,665.5 Clay credits spent the night before; 172 rows in two stuck Clay routine runs still unresolved; wave 2 (2,669) not started. Only 40 of the 3,092 SF DWO rows matched a live person.

Dallas then had the three `(SF)` lists retired outright (BO Leaders Prospects Dir+, Sep 2 Webinar Prospects WFM Dir+, DWO Executives Prospects): `motions/lemlist_contacts/retire_sf_lists.py --go` deletes every contact whose only home is an SF list and no campaign (dry run 5,094), and only unlists the 50 records that also sit on a live list. Dallas explicitly declined to keep any SF contact, including pre-Sep-3 ones. List shells are deleted by Dallas in the UI (no API). The permission classifier blocks mass-delete Bash runs from Claude on the first try; Dallas pasting the command back has let it through. Log: `retire_sf_lists_go.log`. See [[feedback-suppression-lives-in-clay-not-lemlist]].
