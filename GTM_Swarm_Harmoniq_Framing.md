# The GTM engine, told in Harmoniq's own vocabulary

Internal reference for Dallas. Use when explaining the GTM swarm to Naveen, Product, Engineering, or leadership. This is prep material, never a send. Tone when it leaves this doc: peer-level, showcase not seller, head start plus ongoing build.

## The one-liner

The GTM engine runs on the same architecture Harmoniq runs on: triggers, conditions, actions. Harmoniq evaluates real-time ACD/WFM telemetry and acts on the workforce; this evaluates market and pipeline signals and acts on outreach. We run GTM the way our product runs operations.

## The layer map

| Harmoniq layer | What Harmoniq does | GTM swarm equivalent |
|---|---|---|
| **Providers** | Five9, Twilio Flex, Avaya poll or stream stats on a defined frequency, normalized to common statistic names before the rules layer sees them | 15 scheduled launchd jobs (war room 7:15 weekdays, watchers weekly, credit check Thursdays) plus the lemlist relay. Each writes a normalized, dated log to `automation/logs/` before anything downstream reads it |
| **Triggers** | Agent State Changed, Time-in-State Threshold Met, VTO Approved, schedule/frequency events | War-room signal taxonomy (Tier 1-4: earnings language, leadership changes, outages, M&A, hiring clusters, stack moves), CMS Stars release watch, reply arrival, meeting transcript landing |
| **Conditions** | Metrics that must be true before a trigger fires an action: queue depth, AHT, net staffing, service level, AND/OR logic | The gates: verified-claims gate, current-customer exclusion, deliverability gate, credit flag, suppression/routing rules. Deterministic checks run BEFORE any model acts, so a noisy event never spends an expensive run |
| **Actions** | Change agent state, send a message, create a case, update a WFM schedule | Draft the outreach, build the wedge brief, stage the signal, append the proposal. Everything lands in HOLD; Dallas is the only actuator (nobody-but-Dallas rule) |
| **Rule audit trail** | Rule execution history: which trigger fired, which conditions passed, what action resulted | The causal-chain log convention (`automation/LOG_CONVENTION.md`): every log item mints an `evt:` id, every downstream action cites its `chain:`, so any draft or brief replays back to the signal that fired it |

## Where the analogy is deliberately broken

These are choices, not gaps. Worth saying out loud because they preempt the "why not a real event bus" question:

- **No streaming broker.** Harmoniq needs 15-second polling because agent states change in seconds. GTM signals (filings, CMS releases, news, hiring) change in days. Scheduled sweeps are the correct latency, and a broker between a scheduled poll and its handler adds moving parts without adding information.
- **One consolidated ping.** Harmoniq acts per-event; the swarm consolidates everything into one morning brief (single-morning-brief rule) because the consumer is one human, not a floor of agents.
- **Human actuator.** Harmoniq closes the loop automatically; the swarm stops at HOLD by design. Send gates flip only on an explicit ask.

## The boundary line

The swarm reads public and GTM-tool signals only. The moment any of this would read real customer ACD/WFM telemetry or feed a customer-facing decision, it becomes a Product/Engineering conversation, not a laptop job. That boundary is already encoded (read-only agents, no install-base scanning in the war room) and is worth stating proactively when telling this story.

## Framing guardrails when this leaves the doc

- Head start plus ongoing build, never finished-product framing.
- The Claude layer is self-serve skills the team runs themselves; Dallas maintains tools, never ghostwrites in the loop.
- No domain explainers to Naveen. The layer map is for Dallas's prep; with Naveen, lead with the parallel itself and the thread to shape together, not a walkthrough.
