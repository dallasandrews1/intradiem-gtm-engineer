# SalesNav intake folder

Drop hand-pulled Sales Navigator CSV/list exports here, then ask Claude to "ingest the SalesNav export" (or name the file). The `salesnav-csv-intake` agent reconciles it against the owning live roster, fills named gaps, dedups, enforces the existing gates (Director+ for back-office), writes the roster diff, and logs the coverage delta into `automation/logs/pipeline-receipts-*.md` for the daily rundown.

It never touches SalesNav itself and never loads anything into Clay or lemlist. Processed files are tracked in `.intake-state`.
