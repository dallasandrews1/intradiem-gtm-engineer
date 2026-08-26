export const meta = {
  name: 'gate-integrity-fanout',
  description: 'Fan-out, adversarial-verify upgrade of the gate-integrity-auditor subagent: one agent per live Clay motion table checks customer-exclusion + shared-gate integrity on REAL rows, any leak found gets independently re-verified before it is ever reported.',
  whenToUse: 'Before any wave load, as a weekly backstop, or on demand when Dallas wants deeper/faster coverage than the serial gate-integrity-auditor subagent. Read-only throughout: never edits a Function, gate, or row, never runs a wave, never spends credits beyond the cost of a live-row read.',
  phases: [
    { title: 'Discover Tables' },
    { title: 'Audit' },
    { title: 'Verify' },
    { title: 'Report' },
  ],
}

// READ-ONLY, real-rows-only, mirrors gate-integrity-auditor.md's hard rule:
// never validate gate semantics with synthetic --input, and an honest
// "couldn't read it" beats a fabricated all-clear.

const ROOT = '/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer'

const DISCOVERY_SCHEMA = {
  type: 'object',
  properties: {
    motions: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          motion_key: { type: 'string', description: 'e.g. stars, back_office, cost_mandate, wfm_adjacency' },
          motion_label: { type: 'string' },
          table_id: { type: ['string', 'null'], description: 'the live send-readiness/contacts table this motion gates on, or null if unresolved' },
          table_name: { type: ['string', 'null'] },
          customer_exclude_column: { type: ['string', 'null'], description: 'exact column name holding the exclusion flag, and how it is stored (text vs boolean) if determinable' },
          id_confidence: { type: 'string', enum: ['live_confirmed', 'doc_only', 'unresolved'], description: 'live_confirmed = table.schema call succeeded on this id; doc_only = found in docs but not live-checked; unresolved = no confident id found, do not guess' },
          notes: { type: 'string' },
        },
        required: ['motion_key', 'motion_label', 'table_id', 'id_confidence', 'notes'],
      },
    },
  },
  required: ['motions'],
}

const AUDIT_SCHEMA = {
  type: 'object',
  properties: {
    motion_key: { type: 'string' },
    table_id: { type: 'string' },
    verdict: { type: 'string', enum: ['PASS', 'FLAG', 'UNVERIFIED'] },
    leak_found: { type: 'boolean' },
    evidence: { type: 'string', description: 'the exact row(s) and stored value(s) behind any FLAG, or why this is UNVERIFIED' },
    rows_checked_summary: { type: 'string' },
  },
  required: ['motion_key', 'table_id', 'verdict', 'leak_found', 'evidence'],
}

const VERIFY_SCHEMA = {
  type: 'object',
  properties: {
    leak_confirmed: { type: 'boolean' },
    reasoning: { type: 'string' },
  },
  required: ['leak_confirmed', 'reasoning'],
}

phase('Discover Tables')
const discovery = await agent(
  `You're locating the live Clay tables each Intradiem GTM motion gates customer-exclusion on, as ground truth for a real-row leak audit. Root: ${ROOT}.

Step 1: Read ${ROOT}/Clay_Build_State_Registry.md for the current motion list and any table/workbook IDs it already names (note its own header: this registry can be stale, verify don't trust).

Step 2: For each of these 4 motions — Stars (Star Ratings), Back Office, Cost-Mandate, WFM-Adjacency — grep the repo (*.md files) for that motion's live send-readiness or contacts table id (pattern like t_0t[A-Za-z0-9]+, near the motion's name, build-pack, or run-sheet docs). There is also a shared master accounts table referenced elsewhere as Accounts(Master), id t_0thuumoUcu6wAAhovti, carrying a "Customer Flag" column many motions' Universe Lookups read from — check whether each motion's gate consumes that shared source or its own copy.

Step 3: For every candidate table id you find, call the Clay MCP \`table\` tool with mode="schema" on that id to LIVE-confirm it exists and to find the exact column name that stores the customer-exclusion flag, and whether it looks like it's stored as text or boolean (this matters: a known live trap is a flag stored as the TEXT string "TRUE" but consumed as if it were a real boolean, which lets a customer slip through the type mismatch). If the schema call succeeds, mark id_confidence="live_confirmed". If you found an id in docs but the schema call fails or you're not confident it's current, mark "doc_only" or "unresolved" honestly, do not guess an id and do not report unconfirmed as verified.

Return one entry per motion. An honest "unresolved, couldn't confirm a live table id for this motion" is the correct and expected answer if you can't find one, not a failure.`,
  { schema: DISCOVERY_SCHEMA, label: 'discover-tables' }
)

const motions = (discovery && discovery.motions) || []
const resolvable = motions.filter((m) => m.table_id && m.id_confidence !== 'unresolved')
const unresolvedMotions = motions.filter((m) => !m.table_id || m.id_confidence === 'unresolved')
log(`${resolvable.length}/${motions.length} motion tables resolved to a live id; ${unresolvedMotions.length} unresolved`)

phase('Audit')
const auditResults = await parallel(
  resolvable.map((m) => () =>
    agent(
      `You are auditing ONE live Clay motion table for customer-leak and gate-integrity risk, on REAL rows only. Never use synthetic --input. Motion: ${m.motion_label} (${m.motion_key}). Table id: ${m.table_id}${m.customer_exclude_column ? `. Exclusion column found in discovery: ${m.customer_exclude_column}` : ''}.

Use the Clay MCP \`table\` tool, mode="query", on table id "${m.table_id}" to pull real rows and check three things, the same checklist gate-integrity-auditor runs:
1. Customer exclusion: for every row that is (or should be, per the shared exclusion source) a current customer, confirm it is actually gated OUT of any cold campaign. Check the ACTUAL stored value and how the gate consumes it (text vs boolean), not just the column label. One customer reachable by a cold send is a critical finding, leak_found=true.
2. Shared-Function integrity: look for hardcoded literals where a per-row value belongs (the class of bug where e.g. install_base was once hardcoded into a shared Function).
3. Send-gate coherence: rows that should be HOLD are actually HOLD; nothing reads send-ready that shouldn't.

If you cannot read real rows for this table (access limited, schema mismatch, empty/unreachable), say so and return verdict="UNVERIFIED" with leak_found=false rather than guessing a pass. Return the exact row id(s) and stored value(s) as evidence for any FLAG so this doesn't need re-deriving.`,
      { schema: AUDIT_SCHEMA, label: `audit:${m.motion_key}`, phase: 'Audit' }
    )
  )
)

const audits = auditResults.filter(Boolean)
const flagged = audits.filter((a) => a.leak_found)
log(`${audits.length} motions audited, ${flagged.length} flagged for independent verification`)

phase('Verify')
const verifyResults = await parallel(
  flagged.map((a) => () =>
    agent(
      `Independently re-verify a customer-leak finding. Do NOT trust the first auditor's claim, re-derive it yourself. Motion: ${a.motion_key}. Table id: ${a.table_id}. The first pass reported: leak_found=true, evidence: "${a.evidence}".

Use the Clay MCP \`table\` tool, mode="query", to independently re-pull the SAME row(s) directly from Clay. Confirm for yourself whether the exclusion flag's actual stored value really does let this row reach a cold send, don't just restate the first auditor's conclusion. leak_confirmed=true only if your own independent read of the live data supports it. If your read disagrees with the first pass, or the row now reads differently, or you cannot reproduce the finding, set leak_confirmed=false and say exactly why in reasoning, that disagreement is itself useful signal.`,
      { schema: VERIFY_SCHEMA, label: `verify:${a.motion_key}`, phase: 'Verify' }
    ).then((v) => ({ ...a, verify: v }))
  )
)

// Plain-code reduce, no agent needed to sort findings into buckets.
// Exhaustive by construction: every audit result lands in exactly one bucket,
// with an uncategorized catch-all so a future schema drift can never silently
// vanish a finding the way a verdict=FLAG/leak_found=false combo once did.
const verified = verifyResults.filter(Boolean)
const confirmedLeaks = verified.filter((v) => v.verify && v.verify.leak_confirmed)
const disputedLeaks = verified.filter((v) => v.verify && !v.verify.leak_confirmed)
const passed = audits.filter((a) => !a.leak_found && a.verdict === 'PASS')
const flaggedNonLeak = audits.filter((a) => !a.leak_found && a.verdict === 'FLAG')
const unverified = audits
  .filter((a) => a.verdict === 'UNVERIFIED')
  .concat(unresolvedMotions.map((m) => ({ motion_key: m.motion_key, table_id: m.table_id || 'unresolved', verdict: 'UNVERIFIED', evidence: m.notes || 'no live table id could be confidently resolved for this motion' })))
const categorized = new Set([...flagged, ...passed, ...flaggedNonLeak, ...audits.filter((a) => a.verdict === 'UNVERIFIED')])
const uncategorized = audits.filter((a) => !categorized.has(a))
if (uncategorized.length) log(`WARNING: ${uncategorized.length} audit result(s) didn't match any known bucket, surfacing raw so nothing gets silently dropped`)

phase('Report')
const report = await agent(
  `Write the gate-integrity report for Dallas. This is a stop-the-line document if anything is confirmed, be concrete not celebratory.

Confirmed leaks (independently re-verified, real): ${JSON.stringify(confirmedLeaks)}
Disputed findings (first pass flagged it, independent re-check couldn't confirm, needs a human look): ${JSON.stringify(disputedLeaks)}
Flagged but not a customer-exclusion leak (a real defect worth fixing, e.g. a broken shared Function, but nothing reachable by a cold send today): ${JSON.stringify(flaggedNonLeak)}
Clean (PASS on real rows): ${JSON.stringify(passed)}
Unverified (couldn't read real rows or couldn't resolve a live table id): ${JSON.stringify(unverified)}
Uncategorized (didn't match any bucket, should be empty, investigate the workflow's own reduce logic if not): ${JSON.stringify(uncategorized)}

Structure:
1. Any CONFIRMED leak first and loudest, one line per finding, exact row/value evidence, this is a stop-the-line finding
2. Any DISPUTED finding next, flagged for Dallas to eyeball himself since two independent reads disagreed
3. Any FLAGGED-BUT-NOT-A-LEAK finding next, one line each, real defect worth fixing but not itself a customer-exclusion path
4. PASS list, one line each
5. UNVERIFIED list, one line each, with why (unresolved table id vs unreadable rows)
6. If uncategorized is non-empty, list it too and say plainly that the workflow's own bucket logic missed these, don't drop them
7. One-sentence overall verdict: CLEAR / STOP-THE-LINE / NEEDS-DALLAS

House style: no em dashes, no self-narration, peer-level tone.`,
  { label: 'report' }
)

log(confirmedLeaks.length > 0 ? `STOP THE LINE: ${confirmedLeaks.length} confirmed leak(s)` : `No confirmed leaks. ${disputedLeaks.length} disputed, ${flaggedNonLeak.length} flagged-non-leak, ${passed.length} clean, ${unverified.length} unverified`)

return { confirmedLeaks, disputedLeaks, flaggedNonLeak, passed, unverified, uncategorized, report }
