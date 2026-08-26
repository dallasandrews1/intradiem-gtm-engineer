---
name: mem0-enterprise-compliance-flag-jul17
description: "Jason Jones (not Jason Dowden) posted in #ai Jul 17 flagging Mem0 as third-party-cloud and pointing to his own local alternative (Total-Recall/Claude-mem); not yet sanctioned, but relevant to whether Mem0 belongs on the Intradiem Enterprise Claude account"
metadata:
  type: project
---

**Two different Jasons at Intradiem** — don't conflate them in memory: **Jason Dowden** (VP, Technology) is the AI Enablement contact from [[jason-ai-enablement-jul9]]. **Jason Jones** is a separate person, active in #ai on Greenlight engineering/updates, who created the channel's Claude/AI tooling posts.

**Jason Jones's post, #ai channel, Jul 17 2026 1:28pm CDT:** flagged that Mem0 (the memory plugin Dallas runs on this machine, see [[mem0-shared-memory-live]]) routes everything it "remembers" through a third-party cloud provider. He shared his own local alternative, built on Claude-mem: [github.com/Thejjones/Total-Recall](https://github.com/Thejjones/Total-Recall) — keeps memory on-device, no external server. Two caveats he stated himself: (1) **not yet sanctioned** — his words: "I will have to ask permission before I add it to our plugins," so this is a personal tool shared informally, not an IT-approved integration; (2) **known bug** — running ~6 agents 24/7 without a restart for 3+ weeks can wedge a Claude-mem hook worker, squatting on a port until restarted. He hasn't tested it on Kiro; expects it to work on Claude Code CLI/Desktop/VS Code. He closed with a general compliance reminder: check that any plugin/extension isn't sending chat sessions somewhere external and unapproved.

**Decision (Jul 17):** don't touch Mem0 on this personal machine — established, working, no compliance question on a personal account. For the work MacBook / Intradiem Enterprise Claude Code install (see [[vscode-work-macbook-account-split]]), hold off on enabling Mem0 until confirmed cleared for Enterprise use; Total-Recall is the safer local-only default to evaluate in the meantime, with the restart-hygiene caveat noted going in.

**Open:** confirm with Jason Jones and/or Jason Dowden whether Mem0 (or any third-party-cloud memory tool) is cleared for the Enterprise account before relying on it there.
