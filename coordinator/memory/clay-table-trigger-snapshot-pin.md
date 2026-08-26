---
name: clay-table-trigger-snapshot-pin
description: HARD RULE from the Jul 23 Stars launch block - clay_table triggers must pin a CONCRETE snapshot (never "latest"), re-pin after every workflow edit, and diagnose "column errors" from the runs list before touching the graph
metadata:
  type: feedback
---

FEEDBACK (Jul 23 2026, from the Stars Invoke-Workflow launch block Dallas had to debug three rounds with me): three rules, all learned the hard way in one incident on `wf_0tiegzuo3PzJ4UtUGFA` / table `t_0thtm73HHxyiupTuepK`.

**1. Never set a clay_table trigger's snapshotId to "latest".** The Sculptor API accepts it and reads it back fine, but the table's Invoke-Workflow path then silently stops creating runs AT ALL: cells show an error, `clay workflows runs list` shows zero new runs from that trigger. Manual triggers handle "latest" fine; clay_table triggers are UI-managed and resolve only concrete `wfs_` ids. I set "latest" trying to keep table runs fresh and it broke the column-to-trigger handshake for hours while the graph itself was healthy.

**2. After ANY workflow edit, the LAST step of the edit routine is re-pinning the clay_table trigger to a fresh concrete snapshot.** Snapshots are auto-captured before every node edit and at run start, so the newest capture after a passing test IS the current graph. Routine: edit nodes -> smoke test via the manual trigger -> pin the clay_table trigger to the newest verified capture (grep its content for the edit, or use the capture a passing run executed). If this step is skipped, table runs keep executing the old prompt; if "latest" is used instead, table runs stop happening entirely.

**3. When an Invoke-Workflow column "errors", check `clay workflows runs list` FIRST.** Zero new runs from the table trigger = the failure is upstream of the workflow (trigger handshake or a stale cached cell error from an earlier attempt); editing the graph again is wasted motion. Cells display the LAST attempt's error text until force re-run, so "still the same error" can mean "nothing fired," not "same bug."

**Why:** I burned three rounds of Dallas's launch window fixing the (already-fixed) graph while the real breakage was the trigger pin I myself had changed, and the "error" he kept seeing was partly a cached cell.

**How to apply:** any Clay workflow wired to a table column: pin concrete, re-pin after edits as a standing final step, and start every "it errors" diagnosis at the runs list, not the graph.

Bonus rule from the same incident: node inputSchema `required` fields crash the WHOLE run when a real row has that cell blank, and synthetic `--input` tests (all keys filled) mask this completely. Keep `required` only where absence must stop the row (customer_exclude); everything else optional so gates fail-soft to their HOLD exits. This is the workflow-side twin of the real-rows-vs-synthetic gate rule in [[clay-input-rule-refined]].

Related: [[clay-workflow-execution-gotchas-jul20]] [[invoke-workflow-trigger-inputschema-jul20]] [[stars-dwo-messagegen-refresh-jul23]]
