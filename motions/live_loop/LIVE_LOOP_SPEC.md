# Live loop for the strike universe

Spec, Sep 11 2026. Source for the HTML page on the Desktop. Builds in dry-run first.

## The problem it fixes

The engine's inputs are hand-maintained files, so the loop that already runs every day (war
room scans, heat-list scoring, Audiences syncing from Salesforce, lemlist replies) stops at a
staging file and waits for a person to merge. The brain then serves whatever was last merged.
Today's swap replaced one static file with a better static file. This spec moves the inputs onto
the systems that already update, without giving up the sourced-only gate.

## Design in one paragraph

Accounts come from a saved Audiences segment at build time (0 credits, Dallas shapes the
filter in Clay). Employee counts and tech reads come from the Audiences record; sourced facts
from research overlay them from a ledger the weekly refresh job writes. War-room signals enter
the snapshot the morning they are staged, labelled unreviewed, visible in strike_list but never
scoring and never in copy. Dallas approves or denies by replying in the rundown thread, the
existing listener records the decision, and the next build turns an approved signal into a cited
trigger that scores and reaches copy. The nightly sync publishes the snapshot instead of staging
it, once the deploy flag is on.

## Four components

### 1. Accounts from Audiences at build time

- `tam-outbound-engine/config/universe.json`: `source` (`audiences` or `csv`), the segment id,
  the industry map, the agent-ratio table and the freshness rule for facts. Config, not code.
- Saved segment "TAM Strike Universe (engine)" on companies, created once from the CLI, edited
  by Dallas in the Clay UI whenever the universe should change. Starting filter: Salesforce
  Account Type = Prospect, employee_count >= 1000, industry in the ICP set, and at least one of
  a contact-centre platform read, 6sense 6QA, or heat lane rep/cohort. Counts on Sep 11: 1,057
  ICP prospects over 1,000 employees; 422 with a platform read; 169 6QA.
- `tam-outbound-engine/universe_from_audiences.py` reads the segment (search-ids + get, 0
  credits), maps each record to the engine's row shape and writes `data/tam_accounts.csv` as a
  build artifact. Provenance per row: employees cite the Audiences record and its read date;
  a fact in `data/account_facts.json` (SEC filing, annual report, newsroom) overrides it and
  cites its own URL. agent_count is the public figure from the ledger when one exists, else the
  banded ESTIMATE with ratio and band sensitivity spelled out in `source`. Tech reads come from
  the CC Platform fields with their observed dates. Owners come from `config/sf_owners.json`
  (Salesforce owner id to seller), which Dallas fills once.
- Customer exclusion is unchanged: the denylist runs on every row, and Account Type = Customer
  never enters the segment.
- Failure mode: if Clay is unreachable the generator keeps the last written CSV and records
  `universe: stale` in the snapshot errors so the brain says so.

### 2. Staged war-room signals as unreviewed triggers, approve or deny in the rundown thread

- `automation/signal_review.py` ingests `automation/logs/staged_signals.csv` into
  `automation/config/signal_reviews.json`. Each signal gets a stable id (`sig-YYYYMMDD-slug`), a
  resolved domain (heat domain cache, then Audiences by name, 0 credits), a trigger family
  mapped from the source type and angle line, a date, the verbatim quote and the URL. State is
  `unreviewed`, `approved` or `denied`. Signals whose org is a customer or has no domain are
  parked with a reason, never served.
- Generator: approved signals are appended to `data/triggers.csv` by id (idempotent) and become
  cited triggers, so they score and can reach copy. Unreviewed signals ride the strike row as
  `unreviewed_signals`: quote, URL, family, date, id. They do not enter the engine, do not
  score, and no copy is written from them. The brain serves them labelled "unreviewed, approve in
  the rundown thread". Denied signals are dropped and remembered so they never resurface.
- Slack, no new scopes: the rundown DM gains one line, "N signals awaiting review", from a new
  log the rundown reads (`automation/logs/signal-review-<date>.md`, one line per signal with its
  id, family, one-line quote and URL). Dallas replies in the thread `APPROVE sig-...` or
  `DENY sig-...` (several per reply is fine). The existing thread listener records the decision
  in `signal_reviews.json` and confirms in-thread. The Slackbot app stays single-scope
  mcp:connect and the admin install request stands as written.
- The war room keeps staging, never merging. Its staging columns gain `trigger_type` and
  `domain` when it knows them; the ingester tolerates the current shape.

### 3. Nightly deploy

- `automation/config/brain_publish.json` holds `deploy`. Off by default. When on, the nightly
  sync runs the publish script with `--deploy`, and the brain picks the new snapshot up within
  its 300 second cache. The generator's own validation still refuses an empty or non-fresh
  snapshot before anything leaves the machine.
- Order inside the nightly run: ingest signals, build the universe, generate, validate, deploy,
  log with an event anchor.

### 4. Weekly account-facts refresh

- `automation/run_account_facts_refresh.sh` (launchd Sunday 06:00, plist written, NOT loaded
  until Dallas says so). Selects universe domains whose facts are missing or older than 90 days,
  fans out the signal-researcher prompt used on Sep 11 (three accounts per agent, strongest
  model), and writes one JSON per agent to `automation/inbox/account_facts/<date>/`.
- `automation/account_facts_merge.py` validates every fact (URL and verbatim quote present,
  aggregator domains rejected, dates parse) and merges into `data/account_facts.json` with
  `facts_updated`. Runs `--dry-run` (prints the diff, writes nothing) until the flag in
  `automation/config/account_facts.json` is on. Writes a log the rundown reads.

## What changes for the reader of the brain

- strike_list rows carry `unreviewed_signals` next to `triggers`. Cited triggers score; unreviewed
  ones are context with a quote and a link.
- A row's `source` says where employees came from (Audiences read or a filing) and whether the
  agent count is public or an estimate.
- Nothing seed, nothing unsourced, nothing stale is served. Same gates as today.

## Dry-run build (this session)

Built and tested offline, nothing deployed, no credits spent, no gate flipped:

- `config/universe.json`, `universe_from_audiences.py` with a fixture test and one live 0-credit
  read to confirm the field mapping.
- `data/account_facts.json` seeded from the Sep 11 research, so the sourced rows survive.
- `automation/signal_review.py` with tests; the ledger built from the current staged file.
- Generator and contract changes with tests; a scratch snapshot generated to compare counts.
- `brain_publish.json` (deploy off), sync_publish wired to read it.
- Refresh wrapper, plist (not loaded), researcher prompt file, merge script in dry-run.
- Rundown and thread-listener wrapper prompts extended by one rule each.

## Dallas's hand, in order

1. Fill `config/sf_owners.json` for the owner ids listed in the generator log.
2. Shape the "TAM Strike Universe (engine)" segment filter in Clay if the starting filter is not
   the universe you want.
3. Flip `deploy` in `automation/config/brain_publish.json` when the first dry-run snapshot
   looks right.
4. Load the weekly refresh plist when you want facts refreshing on their own.
