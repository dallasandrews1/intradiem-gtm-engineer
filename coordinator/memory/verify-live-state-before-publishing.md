---
name: verify-live-state-before-publishing
description: Re-pull live state on EVERY redeploy of a page that asserts numbers, not just on the first build; the Engine Room shipped "zero sent" while two campaigns were sending
metadata:
  type: feedback
---

10 Aug 2026. The Engine Room page went live on 7 Aug asserting "Zero sends is a choice, not a stall. Eight campaigns are built and sitting in draft" and "eight in draft, zero sent." Both blitz campaigns had flipped to `running` that same day and were sending. The claim stayed wrong on a leadership-facing URL through **three full revision passes** (framing, then voice, then brand), because each pass edited copy and never re-checked the facts underneath it.

**The rule:** any page that asserts live numbers gets a live re-pull on every redeploy, not only on the first build. Treat the facts as an input that expires, the same way [[clay-credit-steward]] treats the credit balance. Verifying the render is not verifying the content.

**The specific trap:** a revision brief that sounds purely editorial ("make it stronger", "make it sound like me", "check the brand") reads as permission to touch only prose. It isn't. If the artifact states facts, the facts are in scope every time.

**Cheap check before any redeploy of an outbound-facing page:** `lemlist-pulse-<date>.md` in `automation/logs/` lists every campaign and its status, and `get_campaigns_stats` gives verified lifetime sent/delivered/bounced/replied per campaign id. Both are seconds of work.

This is the same failure class the page is about: a claim that reads cleanly and is wrong, invisible to every check that only looks at rendering. Related: [[engine-room-deliverable-aug7]], [[engine-room-voice-brand-fix-aug10]], [[deliverable-strength-framing]].
