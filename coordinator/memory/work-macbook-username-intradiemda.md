---
name: work-macbook-username-intradiemda
description: Work MacBook home is /Users/IntradiemDA, not /Users/dallasandrews. Every folder transfer to it needs a path-rewrite pass.
metadata:
  type: reference
---

The work MacBook (Intradiem Claude Enterprise account) runs under username **IntradiemDA**, home `/Users/IntradiemDA`. The personal Mac is `dallasandrews`, home `/Users/dallasandrews`.

Because the coordinator folder, the engine repo (`Claude/Projects/Intradiem GTM Engineer`), the automation scripts, the `.plist` scheduled jobs, `.claude/settings.json`, and `.claude/agents` all contain hardcoded `/Users/dallasandrews/...` paths, **any airdrop/transfer to the work Mac requires a path-rewrite pass** before things work.

The rewrite (run on the work Mac after placing files):
```bash
for d in ~/coordinator "$HOME/Claude/Projects/Intradiem GTM Engineer" "$HOME/Claude/Projects/Clay Builds and Strategy" ~/.claude/agents; do
  grep -rlI '/Users/dallasandrews' "$d" 2>/dev/null | while IFS= read -r f; do
    LC_ALL=C sed -i '' 's#/Users/dallasandrews#/Users/IntradiemDA#g' "$f"
  done
done
sed -i '' 's#/Users/dallasandrews#/Users/IntradiemDA#g' ~/.claude/CLAUDE.md
```
`grep -rlI` skips binaries so the gif/pdf/docx are safe.

Full standing runbook lives at `~/Desktop/WORK_MACBOOK_SETUP.md` (regenerate anytime). On the work Mac the harness project slug becomes `-Users-IntradiemDA-coordinator`; keep writing file memory into `~/coordinator/memory/` regardless. Related: [[vscode-work-macbook-account-split]], [[memory-store-consolidation-jul20]], [[mem0-enterprise-compliance-flag-jul17]].
