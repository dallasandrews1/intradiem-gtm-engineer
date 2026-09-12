# Seed fixture for test_account_engine.py

These are the Jul 1 2026 demonstration CSVs (plus the Sep 5 Centene row) that the engine tests
pin their expectations to: AmeriHealth fit 85 / ROI $7.1M / rendered copy, HCSC customer
exclusion, seed-banner behaviour. On Sep 11 2026 `data/` was swapped for the real, sourced
account universe, so the tests now run against this fixture (`eng.D` is pointed here) instead
of live data. Do not use these rows for anything prospect-facing; every row except Centene is
unsourced demonstration data.
