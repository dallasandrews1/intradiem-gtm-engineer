---
name: clay-query-live-needs-oauth
description: "clay tables query-live returns empty stdout (auth_forbidden: needs an OAuth clay login session, not the static cli key) from Claude sessions as of Sep 5 2026; find rows another way (rows get by id, Audiences search-count, or the Clay UI filter)"
metadata:
  type: reference
---

Sep 5 2026: every `clay tables query-live` attempt from a Claude Code session on t_0thtm73HHxyiupTuepK returned nothing (or "Invalid SELECT item shape" for name refs). The CLI help says query-live needs an OAuth `clay login` session, not a static cli:all key. `clay tables rows get <table> <rowId>` works (cells keyed by field id; map ids with `clay tables columns list`). For "which rows are still blank" questions, hand Dallas the UI filter instead. Related: [[clay-cli-upgraded-aug26]], [[tech-stack-verified-read-sep5]].
