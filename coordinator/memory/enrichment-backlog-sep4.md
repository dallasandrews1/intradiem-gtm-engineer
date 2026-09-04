---
name: enrichment-backlog-sep4
description: Sep 4 2026 enrichment backlog read from lemlist contact by contact, 673 gaps (85 email-only free path, 588 URL-only paid path incl. 177 DWO rows in two stuck Clay runs and 206 parked WFM rows); lemlist list endpoint hides email, per-contact GET carries it top-level
metadata:
  type: project
---
Backlog page + CSV in motions/enrichment/ (build_backlog_page.py <scratch>). Per pool (people / both keys / email-only / URL-only): DWO Live 1,058 / 686 / 83 / 289; BO Customer 296 / 238 / 2 / 56 (holds); BO Net-New 150 / 135 / 0 / 15 (holds); Stars 147 / 126 / 0 / 21; Blitz 15 complete; Cost-Mandate 5 / 4 / 0 / 1; WFM-Adjacency 206 URL-only, parked (no campaign, no spend). The two stuck Work Email runs (run_0tktg67B6g9g3PcGcmh 98/100, run_0tktgpqEnKpc4jMdnjN 71/72) cover 177 wave 1 rows, not the 172 in earlier notes.

**Why:** the rule is every sequenceable contact ends with a verified email AND a LinkedIn URL; campaign leads are complete by construction, the gaps sit on the lists.

**How to apply:** `GET /api/contacts?listId=` returns no email field; `GET /api/contacts/{id}` returns `email` top-level and custom fields under `fields` (single worker, ~0.3 s a call). Run order: A free bridge (0), B Enrich Person on misses (0.5/hit), C re-run stuck rows (~283, over the 200 line: 15-row test then Dallas's go, or cancel), D Work Email by URL on confirmed-current no_email rows (~0.8 on find), E Stars 21 (~34). Nothing above ran on Sep 4.
