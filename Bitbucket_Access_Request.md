# Bitbucket Access: What I Need It For

Short version: I'm bringing working GTM tooling with me, and it needs to live in Intradiem's version control rather than on my machine. Three Python engines (an install-base signal engine, a TAM outbound engine, and the cohesion layer that ties them to one state file), plus the Clay build pack and configs that document the table architecture. Putting them in Bitbucket gets us history, review, and the ability for anyone on the squad to run or extend them. This is the start of an ongoing build, so I also want CI on the test suite so changes stay verified as the engines evolve.

Access list:

- **New repo (or repos), write access:** signal engine, TAM engine, cohesion layer, configs, and the Clay build pack. I'll follow whatever repo structure Engineering prefers.
- **CI runner access:** the engines ship with a test suite; I want it running on every commit.
- **Read access:** any Engineering repos that touch GTM-relevant data: Salesforce integration code, data pipelines or exports for account and usage telemetry, and anything feeding the systems Genna manages. Read-only is fine; I need to see schemas and flows to wire signals correctly, not to change them.
- **Not requesting:** write access to product or platform code, or anything customer-facing.
