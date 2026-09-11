# AI Change Management Side Quest: measurement layer

Dallas's lane on the side quest (Joey Fogle PM, Kathryn Anderson change management and legal, Dallas dashboards and telemetry). Sponsor Derek Eck, point person Jen East, Greenlight stakeholder Jason Dowden. Due Dec 31 2026. Charter deliverables: internal pilot completed, executive presentation delivered, change management intervention framework, telemetry tracking built.

## What is here

| Path | What |
|---|---|
| `adoption_engine/adoption_engine.py` | Computes every Success Metrics Framework v1.0 signal from a usage log plus roster, fires the four triggers, writes `data/adoption_state.json`. Never sends anything. |
| `adoption_engine/config/signals.json` | Every threshold ([X]/[Y] in the framework). Config over code. |
| `adoption_engine/config/interventions.json` | Trigger to playbook action, owner role, response window. Playbook text is Joey and Kathryn's. |
| `adoption_engine/make_sample.py` | Deterministic SAMPLE telemetry (40 synthetic users, 4 teams, 8 weeks). No real people. |
| `adoption_engine/test_adoption_engine.py` | 31 checks on hand-built fixtures. |
| `Adoption_Dashboard.src.html` | The telemetry dashboard on the GTM Engineering page system; threshold panel recomputes in the browser (verified equal to the engine with node). Present mode for the Derek session. |
| `Greenlight_Data_Contract.src.html` | One sheet for the Greenlight reporting review: three feeds, CSA Section B2 grid, six questions. |
| `build_pages.py` | Assembles `.html` from `.src.html`, inlines the state JSON. `--check` fails on em dashes and leftover placeholders. |

## Run

```
cd adoption_engine
python3 make_sample.py                                  # only to regenerate the sample
python3 adoption_engine.py --output data/adoption_state.json
python3 test_adoption_engine.py
cd .. && python3 build_pages.py --check
```

## Swap in real data

Replace the four sample files in `adoption_engine/data/` with the Greenlight export in the same columns (`roster_sample.csv`, `usage_sample.csv`, `manager_views_sample.csv`, `responses_sample.csv`), set `window` in `config/signals.json`, rerun the engine and the build. Set `sample_data` handling: the engine writes `"sample_data": true` today; flip it in `score()` when the feed is real so the dashboard banner comes off.

## Source documents

Kathryn's drafts (Aug 18 2026, shared in the group DM Sep 9): `AI Change Management Success Metrics Framework.docx` and `AI Change Management Current State Assessment.docx` on her OneDrive. PDFs in `~/Downloads` the day they were shared.

## Open with the team (Sep 9 2026)

Sustained-use threshold; Greenlight telemetry answers (Joey with Jason Dowden); pilot team; productivity baseline with Finance; qualitative methods; hosting; stage vocabulary for the productised version (Kathryn). The Derek working session has not happened yet.

## Live

- Dashboard: https://adoption-telemetry.pages.dev (noindex)
- Data contract: https://adoption-telemetry.pages.dev/contract/

Deploy folder `~/Desktop/Intradiem Deliverables/deploy-adoption-telemetry/` (index.html, contract/index.html, _headers, 404.html; the dashboard's contract link is rewritten to `contract/` there). Redeploy after a rebuild:

```
cp Adoption_Dashboard.html "$D/index.html"; cp Greenlight_Data_Contract.html "$D/contract/index.html"
sed -i '' 's|href="Greenlight_Data_Contract.html"|href="contract/"|' "$D/index.html"
cd "$D" && CLOUDFLARE_ACCOUNT_ID=37eeacfb7a4767c44ee8f40243b62c96 npx wrangler pages deploy . --project-name=adoption-telemetry --commit-dirty=true --branch=main
```
