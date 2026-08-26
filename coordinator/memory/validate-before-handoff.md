---
name: validate-before-handoff
description: FEEDBACK - never hand Dallas a command, config, or file to paste/run that hasn't been validated; giving him knowably-broken steps wastes his time and breaks trust
metadata:
  type: feedback
---

FEEDBACK (Jul 19 2026, given sharply): "stop giving me things to do in ways that you already know are not correct. incredibly frustrating and wasted time."

**Trigger incident:** handed Dallas a JSONC block with `//` comments to paste into ~/.claude/settings.json. JSON has no comments, so it broke the parse and took his whole global config out of effect. The block was knowably invalid before he ever pasted it.

**Why:** anything Dallas has to paste or run is a handoff of MY work into HIS hands. If it's wrong, he pays the cost, not me. A knowably-broken step is worse than no step.

**How to apply:**
- Before handing any config/command/file: validate it. JSON through `python3 -m json.tool`, commands dry-checked, files written to scratchpad and parsed there FIRST, then give him a one-liner to install the already-validated artifact. Never hand raw pseudo-code with placeholder comments.
- Never annotate a paste-target with `//` or `#` comments unless the target file format allows them.
- When the classifier blocks ME from writing a protected file (settings.json etc.), the fix is: I produce + validate the full file in scratchpad, he runs ONE `cp` in HIS OWN terminal (not the chat, where it routes back to me and re-hits the block). See [[classifier-blocks-unattended-automation]].
- Verify claims against reality before passing them on (the runs=0 false alarm, [[agent-registry-and-architect]]) — same principle, applied to findings not just commands.
