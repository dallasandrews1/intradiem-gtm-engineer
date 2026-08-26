---
name: salesnav-access-aug7
description: "Dallas got LinkedIn Sales Navigator access Aug 7 2026; no API and ToS bars automation, so the swarm reaches it only via Outlook alert emails, manual CSV exports, and Clay's SalesNav source; architect proposals logged in proposal_ledger.md"
metadata: 
  node_type: memory
  type: project
  originSessionId: fdd6b514-c851-45c3-bbef-12bd9f3b9d8a
  modified: 2026-08-07T18:17:25.041Z
---

Dallas received Sales Navigator access on Aug 7 2026. Governing constraint: individual seats have NO public API and LinkedIn ToS prohibits scraping or browser automation, so no agent ever drives SalesNav directly. The only machine-readable surfaces are (a) SalesNav alert emails landing in Outlook via the Microsoft 365 MCP (auth VERIFIED working interactively Aug 7 2026 by a live outlook_email_search; the Jul 21 failure record in mcp-audit-email-jul21.md is stale; headless launchd availability still unproven until the first Tuesday alumni-watch run logs either alerts scanned or BLOCKED), (b) CSVs Dallas exports by hand, (c) Clay's Sales Navigator source (doctrine holds: SalesNav sources, Clay enriches, lemlist executes).

Agent-architect review ran same day; spec table and BUILT dispositions in `Intradiem GTM Engineer/automation/logs/proposal_ledger.md` under "SalesNav Access Review — 2026-08-07". All three BUILT Aug 7 2026: (1) `salesnav-alert-triage` shipped as an in-place upgrade of alumni-champion-watch (alert emails primary, WebSearch fallback, cross-matches ALL rosters; runtime gated on M365 re-auth, Dallas's hand-made saved-search alerts, and the Keegan alumni CSV); (2) `salesnav-csv-intake` net-new on-demand agent with intake folder `automation/inbox/salesnav/` (first targets: Bradley Tan's missing LinkedIn URL in [[uk-named-accounts-lane-aug6]], Mandate 3's 200+ back-office Director+ contacts); (3) committee-coverage-gap rank shipped as step 4 of stars-refresh-watcher (Mon 6:40), queueing the 27 of 32 uncovered Star Ratings parents by forgone QBP for manual pulls. Agent defs mirrored in `~/.claude/agents/` and `coordinator/.claude/agents/`; registry updated; session restart needed before salesnav-csv-intake is invocable.

Explicitly rejected as agents: anything polling or puppeting SalesNav, auto-InMail, a second job-change watcher parallel to alumni-champion-watch.
