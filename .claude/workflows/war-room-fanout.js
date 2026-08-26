export const meta = {
  name: 'war-room-fanout',
  description: 'Parallel per-account signal sweep across the outbound universes, ranked and mapped to plays — the fan-out version of the daily war room skill',
  whenToUse: 'Run by name ("run the war-room-fanout workflow") when you want deeper or faster coverage than the sequential /intradiem-daily-war-room skill run — e.g. before a big outbound week, after a market event, or when the daily cron log looks thin. Pass a universe filter via args (e.g. {universe: "stars"} or {universe: "backoffice"} or {universe: "all"}); defaults to "all".',
  phases: [
    { title: 'Load Universe' },
    { title: 'Scan' },
    { title: 'Synthesize' },
  ],
}

const ROOT = '/Users/dallasandrews/Claude/Projects/Intradiem GTM Engineer'
const universe = (args && args.universe) || 'all'

phase('Load Universe')
const loaded = await agent(
  `Read the account universes in ${ROOT}. Load: the 32 Tier A+B Star Ratings parents (StarRatings_Universe_2026_TimePhased.csv or its current successor — check Clay_Build_State_Registry.md if the filename has moved), the back-office target list (BackOffice_Target_Universe_v1.csv), and any named strategic accounts flagged in memory or project docs (e.g. Norton/Cardinal Health/Aflac/Blue Shield CA strike-room accounts). Filter to universe="${universe}" (all/stars/backoffice/strategic). Return each account with: name, tier/priority bucket, and 1-2 lines of existing context (why it's on the list, prior signals already logged) so scanners aren't starting cold.`,
  {
    phase: 'Load Universe',
    schema: {
      type: 'object',
      properties: {
        accounts: {
          type: 'array',
          items: {
            type: 'object',
            properties: {
              name: { type: 'string' },
              universe: { type: 'string' },
              tier: { type: 'string' },
              context: { type: 'string' },
            },
            required: ['name', 'universe'],
          },
        },
      },
      required: ['accounts'],
    },
  }
)

const accounts = (loaded && loaded.accounts) || []
log(`Loaded ${accounts.length} accounts for universe="${universe}"`)

phase('Scan')
const scanned = await parallel(
  accounts.map((acct) => async () => {
    const result = await agent(
      `Sweep the last 24-72 hours of public signal for "${acct.name}" (${acct.universe} universe, tier ${acct.tier || 'unspecified'}). Context: ${acct.context || 'none on file'}. Look for: market events (earnings mentions, Stars/CMS language in filings, CMS releases), plan-level or leadership signals (quality leadership changes, hiring clusters), operational signals (outages, backlog news, cost mandates, BPO/vendor changes), and tech-stack moves (WFM/ACD/CCaaS: Verint, NICE, Calabrio, Genesys, Amazon Connect). Only report things that actually happened in the window — say "nothing new" if that's the truth, don't manufacture a signal to have something to report.`,
      {
        phase: 'Scan',
        label: `scan:${acct.name}`,
        model: 'claude-haiku-4-5-20251001',
        schema: {
          type: 'object',
          properties: {
            account: { type: 'string' },
            has_signal: { type: 'boolean' },
            signal_summary: { type: 'string' },
            signal_type: { type: 'string', description: 'market/plan-level/operational/tech-stack/none' },
          },
          required: ['account', 'has_signal'],
        },
      }
    )
    return result
  })
)

const withSignal = scanned.filter(Boolean).filter((s) => s.has_signal)
log(`${withSignal.length} of ${accounts.length} accounts returned a fresh signal`)

phase('Synthesize')
const synthesis = await agent(
  `You are ranking fresh account signals for Dallas Andrews's daily war room, Intradiem GTM. Here are this run's raw findings: ${JSON.stringify(withSignal)}. Rank Priority 1-4 (1 = act today, 4 = log and move on), map each to the Intradiem play it triggers (Star Ratings cliff-edge, Cost-Mandate, WFM-Adjacency, Install-Base, Back Office, or competitive displacement), and flag anything that should hand off to the intradiem-signal-to-play or intradiem-competitive-intel skills. Figure out today's date yourself, then write the full ranked report to automation/logs/war-room-fanout-<todays-date>.md in ${ROOT} (create the file). Do not write to, append to, or modify any other file in the repo — not StarRatings_Earnings_Signals_2026.csv or any other live pipeline file, even if a signal would normally get logged there. If something belongs in a live file, append it instead to automation/logs/staged_signals.csv (create with a header row if missing) and note in the report that it's staged for Dallas's review, not merged. Do not send or post anything to anyone — this is a write-to-log-only run.`,
  { phase: 'Synthesize' }
)

return { universe, accounts_scanned: accounts.length, signals_found: withSignal.length, synthesis }
