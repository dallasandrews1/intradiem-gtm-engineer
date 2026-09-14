# Polar sheets

> Polar-ready sheets for UI-only steps. Each one is a numbered task to paste into Polar, with stop-and-hand-back lines, a report-back folder, and the Claude Code read that closes it. Plan: gtm-polar-plan.pages.dev.

## Open

- [WFM L3 customer lookup re-bind](wfm-l3/) · Clay · slug `wfm-l3-lookup-rebind` · open since Aug 20 2026
- [Stars - Resurrection STRAY step deletes](stray-steps/) · lemlist · slug `stars-resurrection-stray-steps`

## How a sheet closes

1. Paste the task block into a new Polar task with the target tab open. Polar pauses on every stop line.
2. Polar ends with a REPORT block in its final message (it has no access to this Mac; screenshots stay in its workspace behind download links).
3. Paste the REPORT block back to Claude Code. The intake logs it as a claim (`polar_intake.py --paste <slug>`), then the verifier read named in the sheet runs. The registry status in `automation/config/polar_tasks.json` moves to verified only on that read.
