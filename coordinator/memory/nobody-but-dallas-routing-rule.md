---
name: nobody-but-dallas-routing-rule
description: STANDING RULE (Jul 19 2026) — nothing in the autonomous swarm messages/routes/DMs/emails/posts to anyone but Dallas; external send paths stay dry-run until he lifts it
metadata:
  type: feedback
---

Standing as of Jul 19 2026. Nothing in Dallas's autonomous swarm may message, route, DM, email, or post to anyone but Dallas himself. No AE, CSM, prospect, rep, or third party.

**Why:** Dallas wants full control of who hears from the machine right now; no automated external contact while the engine is still proving out.

**How to apply:** Any job with an external send path stays dry-run / preview-only until Dallas explicitly lifts this. Concrete live case: the signal engine `intradiem-signal-engine/run_daily.sh` runs `notifier.py` as a DRY-RUN (writes a digest, sends nothing) and the job is unloaded; do NOT flip that line to `notifier.py --send --channel slack`. Any new agent or proposal that would notify a third party is dead on arrival. This is stricter than and sits alongside the single-morning-brief rule (which governs pings TO Dallas). Recorded as Rule 1 in [[agent-registry-and-architect]] (AGENT_REGISTRY.md). Distinct from the Mem0 catch-up cloud routine, which DMs Dallas (allowed, it's him).
