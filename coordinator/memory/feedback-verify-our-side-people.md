---
name: feedback-verify-our-side-people
description: Sep 23 2026 - Ted Lango (left Intradiem Dec 2024) shipped on seller pages and a live call script as Intradiem's SVP; every Intradiem person named on rep-facing material is verified against a dated roster, gate in check_our_side_people.py
metadata:
  type: feedback
---

Dallas, Sep 23 2026: "you must be more diligent with ensuring accurate data in these builds for our sellers. Ted Lango hasn't worked at Intradiem for 2-1/2 years... shows very clearly in his linkedin."

**What happened:** an Aug 3 note ("Foss knows Ted Lango") was carried forward for seven weeks and hardened into "Intradiem's SVP of Business Enablement, confirmed" without anyone checking Ted's profile. It reached Keegan's index, room and brief, the Citizens self-serve library, the memoryBlue call card and Nathan's live lemlist voicemail hook. Clay settled it in one call: Ted left Dec 2024 and is a VP at Amex GBT, a customer. The "Charter years" tie was also wrong (Foss's overlap with Ted was MetLife 2018 to 2019).

**Why:** the Sep 17 live-check covered prospects only. Intradiem-side people, partners and "mutual contact" claims were never on any check, and "confirmed" in a doc is not a source.

**How to apply:** any Intradiem person, partner contact or mutual-contact claim on rep-facing material gets the same treatment as a prospect: Clay Enrich Person or a dated first-party source, named in the data with the date. Roster: `automation/config/intradiem_people.json` (current, unverified, former). Gate: `motions/shared/check_our_side_people.py`, fail closed, run before rep-page and call-desk deploys. A name in the unverified block never ships. Related: [[feedback-clay-is-contact-source-of-truth]], [[feedback-no-unresolved-contacts-spend-credits]], [[keegan-first-strike-citizens-hartford-aug3]].
