---
name: alex-five-accounts-build-sep14
description: "Sep 14 2026: Alex Bauer's five new customer maps (Synchrony, Citi, JPMorganChase, PNC, AT&T) built as set alex2; /alex/ is now an index over /alex/elevance/ and /alex/financial-services/; Citi is a Prospect in SF, not a customer"
metadata:
  type: project
---

**Trigger:** Alex shared five Sales Nav relationship maps Sep 14 (Synchrony 26, Citi 18, AT&T 15, JPMorganChase 12, PNC 8; 79 cards) after loving the Elevance maps + expansion room. Dallas screenshotted them; transcribed to `automation/inbox/salesnav/alex/transcribed_fs/map_02..06.csv` (a SEPARATE inbox from `transcribed/`, which keeps map_01 Elevance so set `alex` rebuilds byte-identical).

**Built (set `alex2`, sets/alex2.json):** sweeps `sweeps/alex2/_run_sweeps.py` (FS + telecom lanes, CAP=3000 per lane, "managing director" REMOVED from the exec lane because it is a rank at Citi/JPMC and never terminates) -> 19,813 people, 0 credits. Known layer 2,579 SF contacts (JPMC 886, Citi 555, AT&T 502, PNC 441, Synchrony 195) via `_alex2_known.py` + `_alex2_people.py`. Gates -> 1,957 -> selection 146 -> live check -> **86 people on 5 maps** (Synchrony 20, PNC 19, Citi 18, JPMC 18, AT&T 11). check_all 0 FAIL, 11 advisory notes (floating cards, no single top officer).

**Two pipeline extensions made (both opt-in, no other set changes behaviour):**
1. `bo_gates.py` now honours `spec["_exclude_extra_rx"]`, compiled from `accounts[<acct>].exclude_extra` in the set JSON. The shared gates are healthcare-shaped; at banks they let corporate finance, treasury, markets/securities, custody, HR, procurement and wholesale credit onto the maps. **Anything that re-gates must compile `_exclude_extra_rx` itself** - `filter_sweep.py` does, and `_alex2_apply_bridge.py` had to be patched to do the same (the extra gates silently no-opped for a whole cycle).
2. Map-card names are trimmed out of candidates automatically by generating `trim` entries from the roster's `KNOWN_do_not_touch` rows, so no new map duplicates a card on Alex's own map. Note the filter_sweep "kept" counts print BEFORE trim is applied.

**Bridge = live check, and it is free.** Clay MCP `find-and-enrich-list-of-contacts` returns LinkedIn URL + latest_experience_company/title/start_date at 0 credits (balance unchanged across 127 lookups), max 20 contacts per call. Company identifier must resolve: `synchrony.com` and `pnc.com` work, AT&T needs `linkedin.com/company/att`, Citi `linkedin.com/company/citi`, JPMC `linkedin.com/company/jpmorganchase` (`att.com` and `linkedin.com/company/pnc` both return zero). Strip credentials from names first ("Aicha Gillespie, PhD" -> "Aicha Gillespie").

**Why the live check is non-negotiable:** sweep titles at AT&T were badly stale. Daniel McSparran's "Chief Operating Officer" is of **AT&T Veterans**, an employee resource group; Claudia Coleman is at Thomson Reuters; Jenn Kurtz left for Dauphin Borough; Kristi Parrott moved to Compliance & Audit; Michael Schuler is a Customer Engineer III; Allen Jackson shows EVP with a 1971 start; Jennifer Bergen (Synchrony) reads Retired; Jim Miller (JPMC) is an SRE manager; Alex Benitez-Kotsikas moved to Chase Travel. Dual profiles found for Jeffrey Velarde, Exa Whiteman, Jeanie Lutterbei (one reads Retired), David Beck (three), Elizabeth Flynn, Paul Peddicord.

**Salesforce facts (0-credit Audiences read, Sep 14):** Synchrony `001V5000006bHrIIAU` Account Type **Customer**, ACD **Avaya** read 2026-08-02, intent tag "Back Office Intent - FS & HC / Hot (New)". JPMorgan Chase `001V5000006b9J7IAI` Customer. PNC Financial `001V5000006b9JNIAY` Customer. AT&T Entertainment Group `001V5000006b9J6IAI` Customer, but **"AT&T Services - Backoffice" is its own record and reads Prospect**. **Citi is a Prospect on all five of its records**, so back-office work there is net-new, not expansion.

**Pages live (Sep 14):** `/alex/` is now an INDEX over both sets (built by `build_alex_index.py` -> `account_maps/alex_index.html`), Elevance moved to `/alex/elevance/` unchanged, the five at `/alex/financial-services/`. Alex's original link still works. Deploy folder `~/Desktop/Intradiem Deliverables/deploy-backoffice-maps/`.

**Still owed:** mobile numbers and work emails on the final 86 via "Enrich Person and Find Contact Details" (12.4 cr/row, ~1,070 credits) - Dallas approved verify-first, buy contact details after the maps are clean. AT&T sits at 11 because nine identical "Director Billing Operations" siblings trim to representatives per [[feedback-org-chart-density]]. Related: [[alex-elevance-bo-maps-sep11]], [[bo-map-pipeline-rep-sets-aug31]], [[feedback-no-draft-copy-to-ams]].
