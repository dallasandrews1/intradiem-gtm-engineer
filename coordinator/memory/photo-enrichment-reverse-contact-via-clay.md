---
name: photo-enrichment-reverse-contact-via-clay
description: "Profile photos come from Reverse Contact via Clay, never Apollo; Apollo's silhouette is a gap in Apollo, not a fact about the person"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 70497397-25f3-4c4f-af31-d8a2961a3267
  modified: 2026-08-07T03:24:26.002Z
---

**For profile photos on any deliverable, use Reverse Contact via Clay. Do not use Apollo.**

Proven 6 Aug 2026 on the ICP buying-committee site. Apollo returned its grey-silhouette placeholder for a person who demonstrably has a photo (Merrilee Matchett, MetLife). A control test settled it: Katie Oakley has a real photo, Apollo had it, and Clay's own first-party `cpj-enrich-person` still returned `picture_url_copy: null`. **Clay's first-party person enricher does not populate picture fields at all**, so a null there means nothing about the person.

Two saved Clay workflows do this now, both manual-trigger, both runnable from the CLI so output goes to disk instead of into a session's context:

- **Profile Photo Fetch** `wf_0tjdq6dDxvgdXTvYvAG` — input `linkedin_url`, action `reverse-contact-enrich-personal-linkedin-profile-v2`, **1 credit**. Photo is at `stepOutputs.result.person.photoUrl` (NOT under a `toolResult` envelope, despite what the workflows skill says).
- **Profile URL Repair** `wf_0tjdqg1qkx3VYdSpTRV` — input `linkedin_url`, action `cpj-enrich-person`, **0.5 credits**. Returns the person's CURRENT profile url even when handed a stale one.

Run them with `echo '{"linkedin_url":"..."}' | clay workflows runs test <wfId> --input -`, poll `clay workflows runs get`, then read `clay workflows runs steps`.

Why Reverse Contact wins beyond coverage: images are up to 750x750 versus Apollo's 200x200 crops, and they're hosted on Reverse Contact's own CDN (`visum-images.fra1.cdn.digitaloceanspaces.com`), so the URLs do not expire the way LinkedIn's do. Still download rather than hotlink.

**Stale LinkedIn URLs are the hidden failure.** When Reverse Contact returns no match at all (empty `firstName`), the stored URL is often a dead vanity slug the person has since changed. Five of 56 misses were this, and repairing the URL recovered the photo every time. This matters past photos: a stale URL means the "View LinkedIn profile" link on a deliverable is dead in front of an audience. Run the repair pass whenever a profile lookup misses. Datagma (`datagma-enrich-person`, 0.4 cr) was tested as a fallback provider and added nothing.

Realistic yield on a cold list: about half of people have a retrievable photo. Design for an initials fallback, don't assume full coverage. See [[apollo-credit-ceiling-and-ghost-avatars]] for why Apollo is the wrong tool here.
