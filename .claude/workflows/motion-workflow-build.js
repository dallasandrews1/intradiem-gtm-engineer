export const meta = {
  name: 'motion-workflow-build',
  description: 'Build and adversarially test a new motion\'s Clay send-readiness Workflow (Alpha) + MessageGen prompt, per Clay_Motion_Scaffold_SOP_v1.md and Motion_Workflow_Build_Prompt_TEMPLATE_v1.md',
  whenToUse: 'After the golden-scaffold table (L0-L4) has been duplicated by hand into a new <Motion> Motion workbook, and the runbook\'s two decisions (universe source, persona key) are resolved. Pass the motion name via args.motion, e.g. {motion: "WFM-Adjacency"}. Never creates Clay tables, never sends, never syncs, never spends live-wave credits — those stay human-gated.',
  phases: [
    { title: 'Scope' },
    { title: 'Credit Check' },
    { title: 'Draft & Build' },
    { title: 'Critique' },
    { title: 'Report' },
  ],
}

const ROOT = '/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer'

const SCOPE_SCHEMA = {
  type: 'object',
  properties: {
    motion_key: { type: 'string', description: 'source_motion tag, e.g. wfm_adjacency' },
    persona_keys: { type: 'array', items: { type: 'string' }, description: 'the full canonical 6-key ICP rubric, constant across motions' },
    universe_source_summary: { type: 'string' },
    number_rule: { type: 'string', description: 'the H1 number-window rule node 4 of the workflow will enforce' },
    first_wave_estimate: { type: 'string' },
    open_decisions: { type: 'array', items: { type: 'string' }, description: 'anything the runbook says is Dallas\'s call, not to be guessed' },
  },
  required: ['motion_key', 'persona_keys', 'number_rule', 'open_decisions'],
}

const CREDIT_SCHEMA = {
  type: 'object',
  properties: {
    ledger_remaining_summary: { type: 'string' },
    fixture_test_cost_estimate: { type: 'string', description: 'cost of the 2-row fixture test this pipeline runs, should be near-zero' },
    live_wave_cost_estimate: { type: 'string', description: 'informational only, this pipeline does not spend this' },
    recommendation: { type: 'string' },
  },
  required: ['recommendation'],
}

const BUILD_SCHEMA = {
  type: 'object',
  properties: {
    messagegen_file_path: { type: 'string' },
    workflow_id: { type: 'string' },
    workflow_name: { type: 'string' },
    known_good_result: { type: 'string' },
    known_bad_result: { type: 'string' },
    self_reported_status: { type: 'string', enum: ['GREEN', 'NEEDS_TIGHTENING', 'BLOCKED'] },
    issues: { type: 'array', items: { type: 'string' } },
  },
  required: ['messagegen_file_path', 'workflow_id', 'known_good_result', 'known_bad_result', 'self_reported_status'],
}

const CRITIC_SCHEMA = {
  type: 'object',
  properties: {
    verdict: { type: 'string', enum: ['PASS', 'FAIL'] },
    reasoning: { type: 'string' },
    violations: { type: 'array', items: { type: 'string' } },
  },
  required: ['verdict', 'reasoning'],
}

if (!args || !args.motion) {
  throw new Error('Pass args.motion, e.g. Workflow({name: "motion-workflow-build", args: {motion: "WFM-Adjacency"}})')
}
const MOTION = args.motion

phase('Scope')
log(`Scoping ${MOTION} against the runbook and roadmap`)
const scope = await agent(
  `Read these files at absolute paths, root ${ROOT}:
- New_Motion_Build_Runbook.md
- Motion_Roadmap_Next3_2026-07-15.md
- Clay_Golden_Standard.md (persona rubric section, and section 16 on waves)
- Clay_Motion_Scaffold_SOP_v1.md

Find the entry for the motion "${MOTION}". Extract:
- motion_key: its source_motion tag (e.g. cost_mandate, wfm_adjacency)
- persona_keys: the FULL canonical 6-key ICP rubric (coo_finance, cc_ops, wfm, cx, bo_claims, bo_shared) — this is constant across all motions per Motion_Workflow_Build_Prompt_TEMPLATE_v1.md, not this motion's target subset
- universe_source_summary: one sentence on where this motion's universe comes from per the runbook's Decision 1
- number_rule: the H1 number-window rule this motion's node 4 must enforce (what number, if any, this motion may cite and under what freshness/attribution condition — mirror the Cost-Mandate pattern of "prospect's own disclosed figure, source url populated, dated within N days")
- first_wave_estimate: the runbook's credit estimate range for this motion's first wave
- open_decisions: anything the runbook or roadmap explicitly marks as unresolved or "ask Dallas" for this motion — do not guess these, list them

Do not invent a number_rule if the docs don't specify one for this motion; in that case propose one that mirrors the Cost-Mandate pattern (block-on-empty, prospect's own disclosed figure only) and add "number_rule was inferred, not sourced from a doc — confirm" to open_decisions.`,
  { schema: SCOPE_SCHEMA, label: 'scope' }
)
log(`Scope: motion_key=${scope.motion_key}, ${scope.open_decisions.length} open decision(s) flagged`)

phase('Credit Check')
const creditCheck = await agent(
  `Follow the clay-credit-steward skill's logic. Read ${ROOT}/Clay_Credit_Ledger.md for current balance and burn.
This pipeline only runs 2 synthetic test fixtures through a Clay Workflow (Alpha) — no live universe enrichment, no real contacts. Confirm that cost is near-zero and state the current ledger remaining balance for context.
Separately, state the first-wave live cost estimate for "${MOTION}" from the runbook for informational purposes only — make explicit that this pipeline does NOT spend it and that sourcing the real wave is a separate credit GO requiring Dallas's explicit approval.
Motion scope for reference: ${JSON.stringify(scope)}`,
  { schema: CREDIT_SCHEMA, label: 'credit-check' }
)
log(`Credit check: ${creditCheck.recommendation}`)

let round = 0
let build = null
let critiqueNotes = ''
const MAX_ROUNDS = 3
const critics = []

while (round < MAX_ROUNDS) {
  phase('Draft & Build')
  log(`Round ${round + 1}/${MAX_ROUNDS}: drafting MessageGen prompt and building the Workflow (Alpha)`)

  build = await agent(
    `You have the Clay agent-plugin connected, authenticated to workspace 1180800. Root: ${ROOT}.

STEP A — Draft the MessageGen system prompt. Read ${ROOT}/Clay_MessageGen_SystemPrompt_v2.md as the base template and ${ROOT}/Clay_MessageGen_SystemPrompt_CostMandate_v1.md as a worked example of adapting it to a motion. Adapt it for "${MOTION}" (motion_key: ${scope.motion_key}). It must have: a token/column map, persona routing across ${scope.persona_keys.join(', ')}, a core position, number discipline per this rule: "${scope.number_rule}" (block-on-empty, never an Intradiem-computed figure — only the prospect's own disclosed figure or a verified-repository stat per ${ROOT}/04-value-repository/Intradiem_Value_Repository.md), no em dashes, contractions always, brand-light, 2 worked examples. Apply the intradiem-first-draft-engine and intradiem-copy-sharpener skills' rules. Write it to ${ROOT}/Clay_MessageGen_SystemPrompt_${MOTION.replace(/[^A-Za-z0-9]/g, '')}_v1.md.
${critiqueNotes ? `\nPrior round's critic feedback to address in this draft:\n${critiqueNotes}\n` : ''}

STEP B — Build the Workflow (Alpha). Follow ${ROOT}/Motion_Workflow_Build_Prompt_TEMPLATE_v1.md exactly, using ${ROOT}/CostMandate_Workflow_Alpha_Blueprint_v1.md as the structural reference (the same 9-node fail-closed graph). Fill the 5 blanks: MOTION_NAME="${MOTION}", MOTION_KEY="${scope.motion_key}", PERSONA_KEYS="${scope.persona_keys.join(', ')}", MSGGEN_FILE the file you just wrote in Step A, NUMBER_RULE="${scope.number_rule}".
1. Run \`clay workflows create --name "${MOTION} Send-Readiness (Alpha)"\`.
2. Read the created workflow graph first to learn the live node schema before editing — do not hand-author JSON blind.
3. Add nodes 1-9 exactly as specified in the template (eligibility kill switch, persona routing, email verify, number-source gate, tokens ready, MessageGen Email 1, malformed guard, figure-integrity critic, send-ready gate), every gate fail-closed.
4. Add NO send, sync, or launch node.
5. Save the KNOWN-GOOD and KNOWN-BAD test fixtures per the template (known-bad = fabricated number with attribution phrase but BLANK source url) and run \`clay workflows runs test\` on both.
6. If the known-bad fixture does NOT fail at node 8, do not treat that as done — report self_reported_status="NEEDS_TIGHTENING" and explain why in issues.
7. Do not run this on real rows, do not load any campaign, do not touch the sender webhook.

Report messagegen_file_path, workflow_id, workflow_name, known_good_result, known_bad_result, self_reported_status, and any issues.`,
    { schema: BUILD_SCHEMA, label: `build:r${round}` }
  )

  if (build.self_reported_status === 'BLOCKED') {
    log(`Round ${round + 1}: build reported BLOCKED — stopping before critique. Issues: ${(build.issues || []).join('; ')}`)
    break
  }

  phase('Critique')
  log(`Round ${round + 1}: running the critic panel`)
  const roundCritics = await parallel([
    () => agent(
      `Adversarially re-verify a Clay Workflow (Alpha) build. Do NOT trust the builder's self-report. Root: ${ROOT}. Workflow id: ${build.workflow_id}.
Use the Clay MCP read tool to independently pull the live workflow graph. Confirm against ${ROOT}/Motion_Workflow_Build_Prompt_TEMPLATE_v1.md: all 9 nodes present in order, every gate genuinely fail-closed (a failed gate exits and never reaches send_ready=READY), NO send/sync/launch node exists anywhere in the graph, human_approved defaults FALSE. FAIL if any of these don't hold, citing the specific node.`,
      { schema: CRITIC_SCHEMA, label: 'critic:structure', phase: 'Critique' }
    ),
    () => agent(
      `Verified-claims audit. Read ${build.messagegen_file_path} and ${ROOT}/04-value-repository/Intradiem_Value_Repository.md. Apply the intradiem-verified-metrics skill's gate: FAIL if any figure in the worked examples or copy is not either (a) explicitly the prospect's own disclosed figure, attributed and dated, or (b) confirmed present in the Value Repository and correctly attributed. FAIL any Intradiem-computed savings/ROI/recovered-capacity/idle-percent number. FAIL anything unverified that isn't marked [UNVERIFIED].`,
      { schema: CRITIC_SCHEMA, label: 'critic:verified-claims', phase: 'Critique' }
    ),
    () => agent(
      `Copy-quality audit. Read ${build.messagegen_file_path}. Apply the intradiem-copy-sharpener skill's rules: no em dashes, contractions always ("I'd" not "I would"), brand-light, banned-words list, CTA construction (prospect is hero, meeting is their idea), front-loaded/single-idea worked examples. FAIL with specific line citations if violated.`,
      { schema: CRITIC_SCHEMA, label: 'critic:copy-quality', phase: 'Critique' }
    ),
    () => agent(
      `Independently verify this claim rather than trusting it: "known_bad_result was ${build.known_bad_result}". Use the Clay MCP read/table tools to pull the actual known-bad fixture's run result for workflow ${build.workflow_id} directly from Clay. Confirm it genuinely exited at node 8 (figure-integrity critic) with a FAIL/HOLD status, not send_ready=READY and not a silent pass-through. FAIL this check if the live run data doesn't match the builder's claim, or if you cannot independently retrieve the run result.`,
      { schema: CRITIC_SCHEMA, label: 'critic:known-bad-verify', phase: 'Critique' }
    ),
  ])

  const validCritics = roundCritics.filter(Boolean)
  critics.push({ round, critics: validCritics })
  const failed = validCritics.filter(c => c.verdict === 'FAIL')

  if (failed.length === 0) {
    log(`Round ${round + 1}: all critics PASS`)
    break
  }

  critiqueNotes = failed.map(c => `- ${c.reasoning}${c.violations && c.violations.length ? ' (' + c.violations.join('; ') + ')' : ''}`).join('\n')
  log(`Round ${round + 1}: ${failed.length} critic(s) FAILed, redrafting. Notes: ${critiqueNotes}`)
  round++
}

phase('Report')
const finalCritics = critics.length ? critics[critics.length - 1].critics : []
const allPassed = finalCritics.length > 0 && finalCritics.every(c => c.verdict === 'PASS')

const report = await agent(
  `Write the human-approval gate packet for "${MOTION}"'s send-readiness workflow build. This is what Dallas reads to decide go/no-go — be concrete, not celebratory.

Scope: ${JSON.stringify(scope)}
Credit check: ${JSON.stringify(creditCheck)}
Final build result: ${JSON.stringify(build)}
Rounds needed to converge: ${round + 1} of ${MAX_ROUNDS}
Final critic verdicts: ${JSON.stringify(finalCritics)}
All critics passed: ${allPassed}

Structure the report as:
1. What was built (MessageGen file path, workflow id/name, node count)
2. Test results (known-good, known-bad, independently re-verified)
3. Critic verdicts, each one line
4. Open decisions that are Dallas's call, not decided here (from scope.open_decisions)
5. Explicit statement: no Clay table was created or duplicated, no send/sync node exists, sender webhook untouched, nothing sent, the live-wave universe was not sourced or enriched
6. A single GO / NO-GO / NEEDS-DALLAS recommendation with the one-sentence reason

House style: no em dashes, no self-narration, peer-level tone.`,
  { label: 'report' }
)

log(allPassed ? `${MOTION}: converged, all critics PASS after ${round + 1} round(s)` : `${MOTION}: did not fully converge after ${MAX_ROUNDS} round(s) — report flags what's outstanding`)

return { motion: MOTION, scope, creditCheck, build, rounds: round + 1, allCriticsPassed: allPassed, critics, report }
