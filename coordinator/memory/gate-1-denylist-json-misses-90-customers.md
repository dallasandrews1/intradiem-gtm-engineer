---
name: gate-1-denylist-json-misses-90-customers
description: customer_denylist.json holds only 1 domain + 10 aliases but the real customer list is 101 accounts; screen against the CSV
metadata: 
  node_type: memory
  type: project
  originSessionId: 526d8dd8-98ee-4387-9c92-b5cdef3423c8
  modified: 2026-08-06T21:17:39.768Z
---

`tam-outbound-engine/config/customer_denylist.json` contains **1 domain** (`hcsc.com`) and **10 name aliases** (hcsc, health care service, humana, unitedhealth, uhc, cvs health, aetna, molina, elevance, anthem). It points at `greenlight-pack/Active_Customers_SF_Jul10.csv`, which holds **101 accounts**.

**Any exclusion screen run against the JSON aliases alone passes roughly 90 current customers as cold-eligible.** The JSON is a hand-maintained overlay for brand/legal-name gaps, not the source of truth; its own `_source` note says Nate's SF report is. Always screen against the 101-row CSV.

**Why:** at low sourcing volume this stayed invisible. It surfaced while sizing the Aug 2026 6sense sourcing sprint ([[sixsense-si-credits-expire-aug30]]), where tens of thousands of contacts would run through the screen at once and a customer leak becomes a wave rather than a single email. Compounds the known `customer_exclude` text-`"TRUE"`-vs-boolean bug.

**How to apply:** before any cold sourcing or wave load, screen against `Active_Customers_SF_Jul10.csv` (refresh it from Nate first, it goes stale fast). Never treat the JSON as the full list. Validate gate semantics on real rows, never synthetic `--input`.
