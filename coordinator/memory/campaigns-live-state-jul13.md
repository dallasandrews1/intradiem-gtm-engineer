---
name: campaigns-live-state-jul13
description: "Live Clay Campaigns state Jul 13: 2 persona campaigns loaded, curated to 33 addressable leads, all Draft; real send gate is Draft status + Nathan's review, NOT the send_ready column"
metadata:
  node_type: memory
  type: project
  originSessionId: aa8ceb79-626e-4543-8aa3-e0e0309a2e5d
---

Jul 13 2026, live Clay Campaigns check after Nathan finished mailbox setup. Five campaigns exist, ALL in Draft (nothing sends until someone clicks Launch): Persona 1 (Stars/Quality), Persona 2 (Finance), a redundant GATED Tier-A committee campaign (0 leads by design, superseded by the two persona campaigns), and two of Naveen's empty junk test campaigns (flagged for Dallas to delete).

**Key architecture finding:** the two persona campaigns pull leads from Contacts WITHOUT respecting the `send_ready` gate — a HOLD row still synced in. The real send gate is **Draft status + Nathan's per-lead review**, not `send_ready` (which is decorative for this sync path).

**Changes made live:** pruned the 4 clinical-gap parents (see [[stars-wave1-sequences-jul13]]) out of both campaigns → Persona 1 = 15 leads, Persona 2 = 18, all addressable, no customer domains present. Later same day, confirmed emails were already ZeroBounce-validated end-to-end (a stale manual "Email Status" column had wrongly suggested otherwise) and removed 2 known-invalid leads from Persona 2 → 16 leads.

**Expansion mechanism mapped but not yet executed:** Persona 2 pulls from an old static 23-row list, not live Contacts — inconsistent with Persona 1 which pulls from Contacts directly. Fix recipe specced (filtered views on Contacts, repoint each campaign's source) but not run. Nathan's next steps: attach his warmed mailbox, review both campaigns' leads/rendered emails, launch Batch 1 first at the deliverability ceiling. Ties to [[contacts-list-finalized-jul13]], [[clay-build-audit-jul12]].
