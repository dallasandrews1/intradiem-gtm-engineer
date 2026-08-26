# BOO Demo Script + Interactive Artifact Spec (v0)

## Demo narrative (10 minutes, mirrors the Norton demo grammar)

1. **The report lag (2 min).** Show a back-office queue dashboard as the buyer knows it: yesterday's aging, this morning's backlog count. Ask the room: what changed since this printed? Nobody knows. That gap is the product.
2. **The live surface (3 min).** Same queues, live: aging accelerating in appeals, an idle window opening in enrollment, an SLA clock at risk in disputes. The point is not the visibility, it is what happens next without a human deciding.
3. **The action beat (3 min).** BOO reassigns work into the idle window, triggers a micro-training for the under-utilized pod, rebalances the disputes load. Before/after on the SLA clock. One rule shown being edited (config, not code — the buyer's team owns the logic).
4. **The gates beat (2 min).** Nothing acts outside the rules the ops leader set; every action logged and reversible. Same fail-closed grammar the GTM engine demos: automation with a human-owned rulebook. Close on the found-capacity line.

**Claims discipline in the room:** live demo shows mechanism only. If asked for ROI: "the published figures are on our site; for your numbers we'd model your own queues, and you'll know your picture far better than we do."

## Interactive artifact spec (the send-instead-of-a-deck asset)

**Working name:** Back-Office Found-Capacity Calculator (single self-contained HTML page, current Intradiem brand kit, Roboto system: forest #014637, green #2DB56E, orange #F58220 as the action accent only, official inline SVG logo).

- **Inputs (5 sliders):** back-office FTEs in scope · avg fully-loaded hourly cost · observed idle % (default conservatively low) · weekly backlog overtime hours · SLA penalty exposure per quarter (optional).
- **Output:** annualized found-capacity hours and dollars, labeled **"your inputs, your math — an estimate, not an Intradiem claim"**. No Intradiem ROI multipliers anywhere in the math; the calculator only rearranges the prospect's own numbers.
- **Beat 2:** a live-queue vignette (animated aging bar vs a rebalanced one) illustrating the mechanism, no numbers.
- **Footer:** verified-claims note + a single soft CTA (15 minutes).
- Ships via `send_info` replies (Reply Engine v1 routes it) and as the Touch-4 asset in the coo_finance lane.

**Build gate:** artifact copy passes copy-sharpener; the math passes a Dallas review; nothing implies a verified outcome.
