export const meta = {
  name: 'gtm-proposal-sweep',
  description: 'Fan out strategist lenses over the current GTM state, dedup, and return ranked improvement proposals for the proposal ledger. Read-only; proposes, never mutates.',
  whenToUse: 'On demand when Dallas wants a deeper strategy pass than the daily rundown ideas block. This is the embryo of the phase-2 supervised orchestrator: it only PROPOSES; guardrail edits still need Dallas.',
  phases: [
    { title: 'Read state' },
    { title: 'Lenses' },
    { title: 'Synthesize' },
  ],
}

// This workflow is READ-ONLY. It surfaces proposals; it never edits skills,
// system prompts, send gates, or live Clay/Apollo data. Guardrail-layer changes
// remain Dallas's one-tap approval per the supervised-loop decision.

const PROPOSAL_SCHEMA = {
  type: 'object',
  properties: {
    proposals: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          title: { type: 'string' },
          why_now: { type: 'string', description: 'what in the current state prompts it' },
          first_move: { type: 'string', description: 'smallest next step' },
          touches_guardrail: { type: 'boolean', description: 'true if it would edit a skill, system prompt, or send gate' },
          impact: { type: 'string', enum: ['high', 'medium', 'low'] },
        },
        required: ['title', 'why_now', 'first_move', 'touches_guardrail', 'impact'],
      },
    },
  },
  required: ['proposals'],
}

phase('Read state')
const REPO = '/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer'
const STATE_FILES = [
  'control_tower_state.json',
  'Clay_Build_State_Registry.md',
  'gtm-cohesion-layer/engine_state.json',
  'impact/impact.json',
  'automation/logs/proposal_ledger.md',
].map((p) => `${REPO}/${p}`)
const stateDigest = await agent(
  `Read these files under the Intradiem GTM Engineer repo and return a tight factual digest of the current GTM state (gates, per-motion build+funnel, open blockers, credit posture, what is already in the proposal ledger so we do not repeat it): ${STATE_FILES.join(', ')}. Facts only, no recommendations yet.`,
  { label: 'read-state', phase: 'Read state', model: 'claude-haiku-4-5-20251001' }
)

// Diverse strategist lenses. Each is blind to the others; diversity beats
// redundancy for surfacing non-obvious moves.
const LENSES = [
  { key: 'unblock', prompt: 'the fastest path to a first real send: what single change moves the closest-to-send motion forward' },
  { key: 'leverage', prompt: 'reuse and leverage: where an existing workflow/skill/motion could be extended instead of building new' },
  { key: 'signal', prompt: 'signal-to-action: which fresh market signal is under-exploited and what play it unlocks' },
  { key: 'instrumentation', prompt: 'measurement gaps: what the control tower or state files under-report, blinding decisions' },
  { key: 'risk', prompt: 'risk and drift: what is quietly degrading (stale data, an open blocker, a guardrail gap) and should be caught now' },
]

phase('Lenses')
const lensResults = await parallel(
  LENSES.map((lens) => () =>
    agent(
      `You are a GTM strategist for Intradiem. Current state digest:\n\n${stateDigest}\n\nThrough ONE lens only — ${lens.prompt} — propose 1 to 3 concrete improvements. Prefer extending existing assets over net-new. Each proposal: title, why_now (tie to the digest), first_move (smallest step), touches_guardrail (does it edit a skill/system-prompt/send-gate?), impact. Do not repeat anything already in the proposal ledger.`,
      { label: `lens:${lens.key}`, phase: 'Lenses', schema: PROPOSAL_SCHEMA }
    )
  )
)

const allProposals = lensResults.filter(Boolean).flatMap((r) => r.proposals || [])

phase('Synthesize')
const synthesis = await agent(
  `Here are ${allProposals.length} raw proposals from five strategist lenses over Intradiem's GTM state:\n\n${JSON.stringify(allProposals, null, 2)}\n\nDedup overlapping ones, drop anything weak or already-known, and return the final ranked set most-impactful first. Flag which touch the guardrail layer (those become one-tap approvals for Dallas, never auto-applied). Keep it honest: if only two are worth his time, return two.`,
  { label: 'synthesize', phase: 'Synthesize', schema: PROPOSAL_SCHEMA }
)

return synthesis
