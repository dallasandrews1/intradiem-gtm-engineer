# Control Tower

## What it is

The GTM Control Tower is a read-only render layer over the existing GTM state files. It does not write back to any source and does not send anything.

## Inputs

The assembler reads the following source files:
- gtm-cohesion-layer/engine_state.json
- impact/impact.json
- clay_credit_ledger.csv
- Clay_Build_State_Registry.md
- tam-outbound-engine/account_plays.json
- Readout_Log.md

## How to run

From the repo root:

```bash
python3 build_control_tower.py
```

This writes the snapshot to:
- control_tower_state.json

## How to view it

Open the HTML file directly in a browser:
- Control_Tower.html

The HTML reads the snapshot file and renders the panels.

## How to add a source

1. Add the source path to build_control_tower.py.
2. Parse it into a structured value.
3. Add a field to control_tower_state.json.
4. Render it in Control_Tower.html.
