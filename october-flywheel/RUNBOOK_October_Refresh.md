# October CMS Refresh — Runbook (v0 skeleton, Jul 14 2026)

The Stars motion is built to re-grade itself from one input: the October CMS Star Ratings release. October = re-import, re-grade, new fallers enter, graduates self-clean. This runbook is the ordered checklist; `refresh_oct_release.py` is the script that does the mechanical middle.

## Release week, in order

1. **Download the ZIP** the morning CMS publishes (expected early-to-mid Oct 2026 for the 2027 ratings). Do not unzip-and-eyeball in Excel first; Excel mangles the cp1252 and the leading-zero contract IDs.
2. **Wire the member map** — the one real TODO in the script. CMS renames files every cycle; run `python3 refresh_oct_release.py --zip <file> --dry-run`, read the printed member list, and fill `ingest_zip()`'s member/column mapping (summary table + HD3/HD5 domain stars).
3. **Dry-run** until the drift report reads sane (faller/graduate counts in plausible range; a zero-faller October means the mapping is wrong, not that nobody fell).
4. **Full run** → four outputs: movement 26v27, refreshed universe, engine swap-in CSV, drift report.
5. **Engine swap** (data swap, never logic): drop `l2_accounts_stars_2027.csv` over `intradiem-signal-engine/data/l2_accounts_stars.csv`, run `test_l2_intent_scorer.py` (must stay green), run the scorer, confirm graduates now show `graduated` and new fallers surface at base 20.
6. **Clay re-import** at PARENT grain (the contract-grain cost mistake stays dead): refresh the universe table, let the L2 helper re-run, verify intent scores move the way the drift report says. Credit pre-check with clay-credit-steward before any paid sweep; meter is the authority.
7. **The revenue beat:** every account that ever said "wait for October" gets their own published movement in their inbox within 48 hours (reply-engine `wait_for_october` follow-up promised exactly this). New fallers route into Wave-entry per the standing gates (critic, approval, deliverability, owner rules).
8. **Log it:** drift report to the war room + Friday readout; ledger rows for any credits; Mem0 + memory update.

## Guardrails

- cp1252 everywhere; contract_id is the only join key; parent aliases maintained by hand in the script.
- Economics carry forward flagged `stale_econ_carryforward` until QBP re-modeling runs — never present old dollars as new.
- Graduates are a SUCCESS story for list honesty (self-cleaning is the demo line), not a loss.
- Nothing in this refresh sends anything; it re-scores. Sends stay behind the human gate.
