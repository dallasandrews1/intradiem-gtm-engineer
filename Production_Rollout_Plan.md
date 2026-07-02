# GTM System: Production Rollout Plan

From a working prototype to a team-wide motion, once access is granted.

## Where it stands today

- Two engines, net-new strike plans and install-base expansion signals, plus an impact scorecard. All config-driven and tested.
- A hosted brain: one API, key-based access per surface, every request logged. Already live.
- A Claude plugin wired to the brain, install-free for sellers. A Slack `/strikeplan` command proven end to end in a test workspace.
- Everything runs on sample data behind clear banners. The ROI benchmark and peer claims are flagged to verify.

Production does not require new construction. It requires four things: real data, a real Slack workspace, always-on hosting, and verified claims. Each is a swap or an approval, not a rebuild.

## Rollout, in order

**Phase 1, access and validation (first week).** Pull a recurring product-usage export from product analytics or data engineering, and a Salesforce owner and renewal export from RevOps. Drop them into `accounts.csv`, `triggers.csv`, and `owners.csv`. Validate the signals against what a CSM or AE already knows about those accounts and tune the thresholds. Verify the idle-time benchmark and any peer claim against real Intradiem proof points. Nothing sends in this phase.

**Phase 2, harden hosting.** Move the brain from the free instance to a Starter instance so it stays warm. Confirm a separate key per surface and lock access behind SSO or an allowlist. Deploy the Slack listener as an always-on Background Worker. Register the app in Intradiem's real Slack workspace, which needs admin approval.

**Phase 3, pilot.** One or two reps. Install the plugin, which needs no setup on their end, and turn on `/strikeplan` for the pilot group. Have a rep work one play by hand and book one real meeting before any automation. Flip the notifier from dry-run to live for a single signal and a single rep.

**Phase 4, team rollout and measure.** Distribute the plugin, announce the Slack command, and expand the notifier signal by signal. The impact scorecard plus the request log become the adoption and ROI number for leadership. A Salesforce action on the Account record is v2.

## Governance, non-negotiable

One brain, owned by GTM Engineering. Sellers self-serve a surface they cannot configure. Every output is a draft to verify before send, and nothing auto-sends. Only the owner and an authorized leader can change thresholds, triggers, data, or copy.

## Cost

About fourteen dollars a month for two always-on instances, the brain and the Slack worker, plus enrichment (Apollo, Clay) and data access. Trivial against the pipeline the system surfaces.

## What I need from the org

A recurring product-usage export (product analytics or data engineering), a Salesforce owner and renewal export (RevOps), Slack admin approval to install the app, and sign-off on which claims are verified for external use.

## Risks and how they are handled

- Unverified claims: the verify-before-send guardrail, plus a validation step before any real send.
- Noisy signals: validate against reality before automating anything.
- Adoption: lead with Slack, which needs zero install, and the plugin for power users.
- Data delays: start with whatever fields exist, since the engine works on partial data.

## Bottom line

The system is built and proven. Production is access, validation, and two small hosting steps, not new construction. The pilot can be live within the first few weeks of access.
