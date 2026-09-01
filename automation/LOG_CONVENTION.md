# Log convention: causal chain (evt / chain)

Adopted 2026-08-03. Applies to every job and agent that writes to `automation/logs/`. This formalizes what the logs already half-do ("staged_signals.csv row 16", "per the Jul 30 log") into anchors a machine or a human can follow backward without guessing.

## The two lines

**1. `evt:` mint an anchor when you surface something.**
Any log item another job might later act on (a signal, a finding, a flag, a proposal) ends with an event id line:

```
evt: <log-family>-<YYYY-MM-DD>#<slug>
```

- `<log-family>` matches the log filename family: `war-room`, `meeting-capture`, `competitor-displacement`, `gate-integrity`, `deliverability-watch`, `credit-check`, `swarm-health`, `agent-architect`, `stars-refresh-watch`, `action-brief`, `daily-rundown`, `pmo-actions`, `sync-publish`.
- `<slug>` is 2-4 kebab-case words, stable for the account or topic: `#elevance-cms-litigation`, `#centene-q2-earnings`, `#customer-exclude-text-bool`.
- The id is minted ONCE, at first surfacing. A signal carried forward on later days keeps its original id; the later mention cites it with `chain:` instead of minting a new one.

**2. `chain:` cite what caused you.**
Any log entry produced because of an upstream item carries:

```
chain: war-room-2026-08-03#elevance-cms-litigation
```

Multiple parents are comma-separated. If the upstream item predates this convention and has no id, cite the file: `chain: war-room-2026-07-30.md (pre-convention)`.

## Rules

- **Logs only.** Event ids never appear in the rundown Slack DM, the Naveen readout, or anything prospect-facing. They are plumbing, not prose. The rundown's full LOG FILE cites chains; its DM does not.
- **CSVs are not reshaped.** Where a staged/trigger CSV has a source or notes column, put the evt id there. Never add a column for this.
- **Proposal ledger entries** cite the evt that prompted them, so a proposal is traceable to the signal that justified it.
- **Don't over-mint.** "Accounts with no new signals" lines, run headers, and boilerplate get no id. If nothing downstream would ever cite it, it doesn't need an anchor.
- **Why this exists:** every agent action becomes replayable back to the signal that fired it. This is the audit trail for the swarm, the same role the rule-execution history plays in Harmoniq's trigger/condition/action engine (see `GTM_Swarm_Harmoniq_Framing.md` at the project root).

## Example

War room, Aug 3:

```
### 1. Elevance Health: litigation timeline independently confirmed
...
Next step: recheck Aug 4 and Aug 7. Staged to staged_signals.csv row 16.
evt: war-room-2026-08-03#elevance-cms-litigation
```

Competitor watch, Aug 7, briefing off that item:

```
## Elevance Health: displacement brief
...
chain: war-room-2026-08-03#elevance-cms-litigation
```

Rundown log, Aug 3, carrying it in WHAT FIRED OVERNIGHT:

```
- Elevance: CMS litigation timeline confirmed, hearing Aug 7. Play: Stars cliff-edge, contingent on filing content.
  chain: war-room-2026-08-03#elevance-cms-litigation
```
