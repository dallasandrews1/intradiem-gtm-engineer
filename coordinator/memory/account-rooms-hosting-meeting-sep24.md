---
name: account-rooms-hosting-meeting-sep24
description: "Sep 24 2026 11:00 CT call with Sierra Jones and Carter Woods on where account rooms and one-pagers should live and how engagement gets tracked; marketing's three options, the two-need split, Paperflite is Carter's idea"
metadata:
  node_type: memory
  type: project
  originSessionId: a836b3bb-14c2-4b5e-934d-f89194ec5116
  modified: 2026-09-24T02:14:21.875Z
---

**Origin:** Sep 23 2026 noon call (Otter `fvw-559lZZg4A6fvmTSY39bOVKY`). Dallas showed the account rooms on intradiem-accounts.pages.dev and said they sit on his personal Cloudflare because Bitbucket access never came. Carter Woods (marketing ops, Boise, ran webinars and 6sense) suggested Paperflite, a PDF hosting tool he used before: per-viewer read tracking, Salesforce sync, reps send from the app, password gating. Sierra scheduled the follow-up: Sep 24 2026, 11:00 to 11:30 CT, Zoom.

**Marketing's options per Sierra's invite:** WordPress on intradiem.com (best tracking, carries 6sense and Pardot tags), Unbounce (landing page builder, still licensed, pages@intradiem.com), Pardot / Account Engagement at marketing.intradiem.com (may be replaced soon).

**State of the estate on Sep 23:** 27 Cloudflare Pages projects on Dallas's personal account, 55 links registered in other people's hands (22 with Naveen), zero engagement tracking on any page (no beacon of any kind), pages.dev URLs unauthenticated, contact-detail pages either sealed behind a passphrase or shipped as PDF per [[strike-room-guide-deployed-sep22]].

**The split to hold in the meeting:** internal rooms (org maps, save rooms, call desks, kits) need an Intradiem domain plus SSO and only usage counts; prospect-facing pieces (one-pagers, wins pages) need per-recipient engagement that lands in Salesforce. Marketing's three tools serve the second need only. Paperflite is the candidate for the second need; the first is a domain plus Cloudflare Access (free to 50 users) or an Engineering-owned deploy target.

**Rule applied:** [[feedback-marketing-tools-never-bypass-marketing]]. Lead with Sierra's options and Carter's idea; the rooms are a head start waiting on a home, never a way around the web team.

Related: [[shared-links-gate-sep20]], [[rep-index-pages-sep20]], [[lemlist-open-tracking-domain-pending-it]].
