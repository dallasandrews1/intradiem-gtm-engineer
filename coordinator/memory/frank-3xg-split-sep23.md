---
name: frank-3xg-split-sep23
description: "Sep 23 2026: Frank asked to split Assurant off the QuickStart pair (3xG is not the partner on Assurant); a 3xG-only index at backoffice-maps.pages.dev/frank/3xg/ is STAGED, call plans repointed, Five9 line off the shared PennyMac plan; deploy and reply pending"
metadata:
  type: project
---

Frank Ciccone emailed Sep 23 2026: "3XG is not our partner on Assurant. Is it possible to split this one off from Highmark and Pennymac?" He is setting up time with Jeremy Roderick (3xG). Assurant's partner is SagesS3 ([[frank-assurant-package-sep16]]).

**Built, staged, NOT deployed, reply NOT sent:**
- New page `backoffice-maps.pages.dev/frank/3xg/`: Highmark and PennyMac only. No Assurant, no shelf row (Ally, Maximus, Fidelity, AmeriHealth, BCD, partner sellers), no sales kits, no Five9 registration sentence. Built by `build_rep_index.py 3xg`, which DERIVES the entry from Frank's own "frank" entry (`three_xg()` at the end of the file, added at the end so a parallel session editing the frank gates would not collide), so the two never drift; `dest` key serves it nested under frank/. Frank's own `/frank/` page is unchanged and keeps Assurant.
- The two call plans (shared by Frank and 3xG) now carry `QuickStart index -> /frank/3xg/` in the set nav instead of `Frank's index -> /frank/`, so a 3xG reader cannot walk to Assurant. The PennyMac "Four things to know" item about Five9's registration (another partner's deal registration on the pre-pipeline report) was replaced with the verified $60 million July cost line (pm_60). Both edits in `motions/partner_channel/frank_quickstart/build_quickstart.py`.
- Registered in `shared_links_manifest.json` as not sent. Snapshot `_staged_pre_job6` refreshed for the three files this work changed.
- Render checked once (downscaled), clean.

**Left on the shared pages on purpose:** the "Held until a source is in hand" section listing 3xG brief lines that did not confirm (neutral wording, protects callers from wrong facts on a dial); the "Built before the Salesforce record was read" stamp; the Highmark hold line that says "Ask Naveen and the Optum account team" (from the parallel session's Sep 23 gate rewrite).

**Trap:** a parallel Claude session was editing `build_rep_index.py` and `rep_index_theme.py` the same minute (Frank gate rewrite, 18:47). Read mtime and diff before any further edit to that file; `deploy_rep_pages.sh maps` ships everything staged under frank/, including that session's Frank index.

**How to apply:** when a partner sponsor asks for one account off a shared page, split the INDEX and repoint the sub-pages' nav; never delete the account from the rep's own page. Check every sub-page for a link back to the rep root and for other partners' deal-registration lines before handing a link to a partner.
