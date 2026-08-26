# New Motion Build Runbook
**How to build a new motion workbook in Clay to the house standard, without reinventing it each time. Open this each time you start a motion.** Build order for the next three: Cost-Mandate, then WFM-Adjacency, then Install-Base.

## Structure law (ratified 2026-07-15)
1. **One motion = one Clay workbook.** Create `<Motion> Motion` as its own workbook before building anything (Back Office Motion is the precedent). Universe, contacts segment, MessageGen + critic, campaigns all live in it. Shared static assets (Verified Metrics, Product-Angle Map, ICP Rubric, customer exclusion file) come in by Lookup if cross-workbook lookups work, small seeded copies if not; verify in the UI first. Cross-motion unity = `source_motion` tags + ledger + readouts, never table adjacency.
2. **The engine stays centralized and thin.** One `triggers.json` / `personas.json` / `proof.json` / L2 config with per-motion overrides (the BO fork pattern), plus the reference scorer and its tests. It decides and proves the logic; it never re-implements what Clay runs. Clay is federated per motion; the engine is one brain with motion switches. That asymmetry is deliberate.
3. **Files first, Clay once.** Every formula, prompt, critic, and sequence is drafted as a project-root file, tested against the scorer/config where logic is involved, then transcribed into Clay in one pass and verified live. No fresh logic decisions inside a Clay column editor.
4. **Migration note (Cost-Mandate):** the `Cost-Mandate Universe (x-vert)` table was built inside the GTM Engine workbook on 2026-07-15 (pre-ratification). First step of the next build session: create the `Cost-Mandate Motion` workbook and move the table into it (table menu → Move table), then build L3/L4 there.

## The artifact stack (what each file is for)
- **`Clay_Golden_Standard.md`** = the rules (architecture, wiring, personalization, copy, gates, gotchas). The build thread reads it so you don't have to.
- **`Motion_Roadmap_Next3_2026-07-15.md`** = what to build and in what order, with each motion's engine and Clay spec.
- **`Clay_Build_Prompt_<Motion>.md`** = the start button you paste into a fresh thread.
- **`Clay_MessageGen_SystemPrompt_v2.md`** = the live v2.2.3 copy template you adapt per motion.

## The loop (per motion)
1. Open a fresh thread in this project and paste the motion's build prompt. It reads the standards, sweeps live Clay, and mirrors the Stars pattern.
2. Answer the two decisions it asks for (universe source and persona key; both resolved below).
3. It builds L0 to L4 (universe, signals, contacts segment, MessageGen plus critic) and reuses L5 to L8 (Send Queue, Sync, Reply/Attribution, Worklist) by tagging `source_motion`.
4. It adapts the v2.2.3 MessageGen prompt to the motion (core position, persona routing, number rule, proof).
5. You hold the gates: built via Chrome, proven on a 10-row slice, credit estimate plus ledger row before any paid run, everything Draft plus critic PASS plus your approval, nothing sends.
6. Verify against the Golden Standard and the gotchas before launch. Repeat for the next motion.

## Decision 1: where the universe is sourced from
**Rule: if the motion has an authoritative list that defines its universe, use it. If it is defined by a fit-profile plus a trigger and has no list, you generate it, signal-first, then broaden firmographically later.** You are not expected to have a list sitting ready. For a why-now motion the trigger is the source: the accounts currently showing the signal define the universe.

**Source once, process in waves (Golden Standard §16).** Whatever the source, load the FULL applicable universe into the table at kickoff — sourcing is cheap and discovery is never redone. Waves apply to the expensive layers only (enrichment, MessageGen, campaign load, sync), sliced 30 to 50 contacts at a time via `wave_number`/`wave_status` columns. Later waves pull from the standing table; they never go back out hunting. No new wave until the prior wave's reply data is read, and a wave is not "launched" until the next-wave check is on the calendar.

Per motion:
- **Cost-Mandate: no authoritative list** (unlike Stars, which had the CMS file). Generate signal-first, a Clay company search or war-room sweep across the six verticals for companies showing a live cost or efficiency signal (recent RIF or layoff news, earnings cost-takeout language, a hiring freeze, open RTA or intraday reqs). Roughly 150 to 200 accounts for the first wave. Broaden later with an Apollo or Sales Navigator firmographic pull on the ICP if you need volume.
- **WFM-Adjacency: also net-new, signal-first,** but the signal is technographic plus hiring. Source via a Clay technographic search (who runs Verint, NICE, Calabrio, Genesys, Amazon Connect) plus RTA and intraday job postings. It overlaps the Cost-Mandate accounts, so it can run as an overlay on that table rather than a separate pull.
- **Install-Base: the list already exists.** The universe is the customer file (the 101-account install base), inverted so customers are in scope. No generation needed.

The pattern to remember: Stars had CMS, Install-Base has the customer file, Cost-Mandate and WFM have neither, so they get generated from their trigger.

## Decision 2: which persona key is canonical
**You do not discover this, you designate it.** Canonical is the **ICP Persona Rubric** (`ref_ICP_Persona_Rubric.csv`): `coo_finance`, `cc_ops`, `wfm`, `cx`, `bo_claims`, `bo_shared`. It is the deliberate taxonomy the Back Office motion already uses. Anything using a different key (for example `triggers.json` says `finance`) is drift to normalize to the rubric. Same principle as the Value Repository for claims: one source of truth, everything else matches it.

Per motion (all drawn from the rubric):
- **Cost-Mandate:** `coo_finance` primary; `cc_ops`, `bo_shared` / `bo_claims` secondary.
- **WFM-Adjacency:** `wfm` entry; routed up to `cc_ops`, `coo_finance`.
- **Install-Base:** `bo_claims` / `bo_shared` or `cc_ops` (owner of the dark workforce), plus `coo_finance` for multi-BU.

Standing normalization: DONE 2026-07-15. `finance` was standardized to `coo_finance` across the engine config (personas.json, triggers.json, generated plays) and the tests (25/25 green). Canonical keys: `coo_finance`, `cc_ops`, `wfm`, `cx`, `bo_claims`, `bo_shared`. The Clay `persona_key` column is a separate motion-label layer (`stars_quality`, `medicare_finance`) and was correctly left alone.

## Gates and discipline (every motion, non-negotiable)
- Build in Clay via Chrome (the MCP cannot create tables). Verify the current UI before any click-by-click.
- Prove on a 10-row slice before volume.
- Credit estimate plus ledger row before any paid enrichment. Tier it: firmographics broad, waterfall or technographic only on fit-cleared rows. Sample 10 rows to confirm any unknown per-provider cost.
- Everything ships gate-fed: Draft, critic PASS, your approval. Sender webhook OFF until deliverability is green. Nothing sends.
- Watch the gotchas: read `Sent At` after a sync, never click Create Claygent, keep optional inputs Required-to-run OFF, reconcile account data or the critic will correctly refuse.
- Wave discipline: full universe sourced once at kickoff; enrichment/MessageGen/sync run per 30-50 contact wave; stamp the MessageGen prompt version on each wave; never re-run sync over campaign-side per-lead overrides; schedule the next-wave check before calling a wave launched.

## Quick reference

| Motion | Key | Universe source | Primary persona | Lead proof | First-wave credit est. |
|---|---|---|---|---|---|
| Cost-Mandate | `cost_mandate_xvert` | Signal-first across 6 verticals | `coo_finance` | Humana (healthcare) + by-vertical public | ~350 to 500 cr |
| WFM-Adjacency | `wfm_adjacency` | Technographic + RTA hiring (overlay on Cost-Mandate) | `wfm` | Idle-time-on-top-of-WFM + Humana occupancy/AHT | ~150 to 300 cr |
| Install-Base | `installbase_expansion` | Customer file (inverted) | `bo_claims`/`bo_shared`/`cc_ops` + `coo_finance` | Humana land-and-expand arc + the customer's own results | ~50 to 150 cr |

**Definition of done per motion:** a live self-cleaning list (fit plus intent, customers excluded inside the score), a MessageGen prompt built to the v2.2.3 contract with only prospect-own or verified numbers, a critic gating sync on PASS, personalized 5-touch two-lane sequences in Draft, and reply/attribution tags wired. Nothing sent. If any layer is thinner than its Stars equivalent, it is not done.
