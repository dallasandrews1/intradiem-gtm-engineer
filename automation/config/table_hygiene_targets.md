# Table-hygiene sweep targets

One table per line: `name | table_id | workbook/notes`. `table-hygiene` sweeps each daily. Clay's list endpoint is Enterprise-gated, so this list is maintained by hand — add a line when you build a new table, remove one when a table is retired. Function tables (fn_*) can be listed too; they hold logic, not data, but still accrue redundancy.

## Live data tables
- WFM-Adjacency L3 (contacts) | t_0tic8arWbZp8bSx87Ad | WFM-Adjacency Motion
- WFM-Adjacency L1 (clean, 28 accounts) | t_0tict25TSXgTgdJgtZZ | WFM-Adjacency Motion
- Stars MessageGen (working reference) | t_0thtm73HHxyiupTuepK | Stars

## Known cruft to confirm/remove (flag on sweep)

## Add the rest (IDs Dallas fills in)
- Stars L1 / L2 / L3 | <id> |
- Contacts (Buying Committee) | <id> |
- Back Office motion tables | BO_People_Master = t_0tingaqoNzymfmSpEZh, workbook wb_0ti4jh8ATmjiCowc7JM | Existing_BO_Campaign_Seed ID still unknown, get it next time it's open
- Cost-Mandate motion tables | <id> |
