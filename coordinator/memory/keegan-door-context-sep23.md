---
name: keegan-door-context-sep23
description: Keegan maps, rooms and alumni page now carry the read behind "worked at a customer" (overlap with Intradiem, success manager, outreach rule, suggested use); staged Sep 23 2026, not deployed
metadata:
  type: project
---

Sep 23 2026 evening. Dallas: a bare "worked at MetLife" pill in an orange box does nothing for anyone. Replaced across Keegan's three account maps, the three rooms and the 135-person alumni page.

- Source of the read: `motions/keegan/accounts/customer_context.py`, built programmatically from the active customer report (customer since), the Customer Value Registry (success manager, maturity, STALLED) and marketing's stories registry (story, cleared name, EXCLUSIONS). Never hand-typed.
- Per spell: overlapped / before / former / unknown, a verdict line, the outreach rule, a suggested-use line. alumni.py is importable now (CUST, SN_PAST, CTX); alumni.json and the CSV carry the new fields.
- The finding: of 37 spells, 21 ended before Intradiem arrived at that customer and only 12 overlapped. The old pill read all 37 as warm.
- Staged to deploy-backoffice-maps and deploy-save-rooms; deploy order maps, rooms, plans (auto mode denies wrangler, see [[claude-code-auto-mode-blocks-deploys]]). Rooms build with --allow-stale while the Vanguard record is unread ([[sf-freshness-gate-sep21]]).
- Log: automation/logs/keegan-door-context-2026-09-23.md.

**Why:** a fact with no consequence attached (worked at X) reads as a warm door when most were not; the rep needs overlap, the internal route and what may go in writing.
**How to apply:** any future "worked at a customer" surface (Alex, Frank, Inger maps, alumni-champion-watch) reads alumni.json / customer_context.py rather than printing the employer name. Same pattern for any signal: attach the consequence, not the fact.
