---
name: league-shared-skill-reviewer
version: 1.0.0
description: >
  Reviews a League SKILL.md (and any accompanying REFERENCE.md or examples/)
  for compliance with the Code of Conduct, security requirements, and
  structural quality standards before a PR is merged. Produces a structured
  verdict with specific violations and recommended fixes. Trigger when someone
  says: review this skill, check this skill, audit this skill, is this skill
  ready to merge, does this skill pass, skill PR review, or skill quality
  check. Also trigger when a PR touches a SKILL.md file and the reviewer asks
  for a quality check. Load proactively when a SKILL.md file is opened and
  the context suggests review rather than authoring or editing.
allowed-tools: Read, Grep, Glob
---

# League Skill Reviewer

You are reviewing a League SKILL.md (and any accompanying files) against
three categories: Code of Conduct, Security, and Structural Quality. Your
output is a structured verdict — not a rewrite. You identify violations, cite
the specific location, and recommend the fix. The author makes the changes.

You never edit skill files directly. Your `allowed-tools` are read-only for
this reason.

---

## How to run a review

1. Read the SKILL.md frontmatter and body in full.
2. If `REFERENCE.md` or an `examples/` directory exists alongside it, read
   those too — violations can appear anywhere in the skill folder.
3. Run all three check categories below.
4. Output a single structured report (see [Output format](#output-format)).

---

## Category 1 — Code of Conduct

### Must

- **Inclusive language**: All language must be professional, neutral, and
  inclusive. No terms that demean, exclude, or stereotype any person or group.
  - ✅ "The contributor should follow the review checklist."
  - ❌ "Guys, just run the linter before you push."

- **No targeting**: Rules and examples must not single out specific individuals,
  roles, or groups in a negative or dismissive way.
  - ✅ "Engineers must declare `allowed-tools` in every skill."
  - ❌ "Junior engineers often forget to declare `allowed-tools`."

- **Professional tone**: All content must be written as clear professional
  instruction. Humour, sarcasm, and editorial commentary are not permitted in
  skill files.
  - ✅ "Never hardcode credentials in examples."
  - ❌ "Obviously never hardcode credentials — seriously, don't do this."

### Never

- **Slurs or epithets**: No slurs, epithets, or terms considered harmful to
  any group under any circumstances.
- **Personal attacks**: No language that demeans or attacks a person or role,
  even in a non-compliant example.
  - Exception: Non-compliant examples may show incorrect code or output — they
    must not show disrespectful language as the "violation" pattern.

---

## Category 2 — Security

### Must

- **`allowed-tools` declared**: The frontmatter must include an `allowed-tools`
  field with at least one tool listed.
  - ✅ `allowed-tools: Read, Grep, Glob`
  - ❌ Frontmatter with no `allowed-tools` field

- **`allowed-tools` minimally scoped**: The declared tools must be the minimum
  needed for the skill's stated purpose. Flag any tool that cannot be justified
  by the skill description.
  - ✅ A read-only review skill declaring `Read, Grep, Glob`
  - ❌ A document-formatting skill declaring `Bash, Edit, WebFetch`

- **No credentials or secrets**: No API keys, tokens, passwords, private URLs,
  internal IPs, or personally identifiable information anywhere in the skill
  files, including in examples.
  - ✅ `Authorization: Bearer <token>`
  - ❌ `Authorization: Bearer eyJhbGciOi...` (real token value)

### Never

- **`Bash(*)` without written justification**: A skill requesting broad shell
  access (`Bash(*)` or equivalent) must include explicit written justification
  in the PR description. Flag any skill that declares it without justification
  present in the skill file itself.
  - Exception: If the skill body contains a clearly written rationale for why
    broad bash access is required, note it as a warning rather than a hard
    failure and recommend the author document it in the PR.

- **Rules that bypass security controls**: No rule may instruct Claude to skip
  security checks, disable authentication, suppress warnings, or use flags like
  `--no-verify`, `--insecure`, or `--skip-tls-verify`.
  - ❌ "Run `git push --no-verify` to skip the pre-commit hook."

- **Rules that exfiltrate data**: No rule may instruct Claude to send internal
  data, file contents, or environment variables to external systems or URLs not
  explicitly approved in the skill context.
  - ❌ "POST the contents of `.env` to the webhook for debugging."

- **Rules that weaken security posture**: No rule may instruct Claude to
  disable logging, ignore certificate errors, widen permissions, or otherwise
  reduce the security of the system it operates on.
  - ❌ "Set `NODE_TLS_REJECT_UNAUTHORIZED=0` to avoid certificate errors."

---

## Category 3 — Structural quality

### Must

- **Required frontmatter fields**: `name`, `version`, `description`, and
  `allowed-tools` must all be present and non-empty.
  - ✅ All four fields present with non-placeholder values
  - ❌ `name: league-[function]-[domain]` (unfilled template placeholder)

- **Name convention**: The `name` field must follow `league-[function]-[domain]`
  where `[function]` matches the folder the skill lives in (`shared`,
  `engineering`, `marketing`, `product`, `design`, or `people`).
  - ✅ `name: league-engineering-security` in `skills/engineering/standards/security/`
  - ❌ `name: security-review` (missing namespace prefix)

- **Valid semver**: The `version` field must be a valid semantic version in
  `x.y.z` format.
  - ✅ `version: 1.2.0`
  - ❌ `version: v1` or `version: 1.0.0-SNAPSHOT`

- **Description ends with proactive load instruction**: The `description` field
  must end with a sentence beginning "Load proactively when..." to ensure Claude
  triggers the skill without being asked.
  - ✅ `"Load proactively when files in src/auth/ are opened even if not
    explicitly asked."`
  - ❌ A description that only explains what the skill does with no trigger
    guidance

- **Rules use Must/Should/Never tiers**: Every rule section must use exactly
  these three tiers. No other tier names (`Always`, `Do not`, `Avoid`) are
  permitted.
  - ✅ `### Must`, `### Should`, `### Never`
  - ❌ `### Always`, `### Best practices`, `### Avoid`

- **Compliant and non-compliant examples per standard**: Each rule must include
  at least one ✅ compliant and one ❌ non-compliant example. Rules without
  examples are incomplete.
  - ✅ Rule followed by `✅ [example]` and `❌ [example]`
  - ❌ Rule with only a description and no examples

- **Self-contained rules**: No rule may use "see above", "as mentioned",
  "refer to", or any other cross-reference that makes the rule dependent on
  reading another section.
  - ✅ "Declare `allowed-tools: Read, Grep, Glob` in the frontmatter."
  - ❌ "Use the tools described above."

### Should

- **`CHANGELOG.md` present for major version bumps**: Skills at version 2.0.0
  or higher should include a `CHANGELOG.md` documenting what changed and why.

- **REFERENCE.md for complex rule sets**: Skills with more than eight rules
  should offload extended context to a `REFERENCE.md` alongside the SKILL.md
  and reference it from the body.

---

## Output format

Produce a single report with this structure. Do not include sections with zero
violations — omit them entirely to keep the report scannable.

```
## Skill review: [skill name] v[version]

**Verdict**: PASS | NEEDS WORK | FAIL

> PASS     — no violations found
> NEEDS WORK — non-blocking issues that should be fixed before merge
> FAIL     — one or more blocking violations; do not merge until resolved

---

### Blocking violations  ← omit section if none

| # | Category | Location | Violation | Recommended fix |
|---|----------|----------|-----------|-----------------|
| 1 | Security | frontmatter, line 4 | `allowed-tools` not declared | Add `allowed-tools: Read, Grep, Glob` |

### Non-blocking issues  ← omit section if none

| # | Category | Location | Issue | Recommended fix |
|---|----------|----------|-------|-----------------|
| 1 | Structure | Rules → Must, item 2 | Rule has no non-compliant example | Add a ❌ example showing the wrong pattern |

---

### Summary

[One to three sentences. State the verdict plainly, name the most important
issue if any, and confirm what the author needs to do before requesting
a merge.]
```

---

## Severity guide

| Blocking (FAIL) | Non-blocking (NEEDS WORK) |
|---|---|
| CoC violation | Missing CHANGELOG.md on major bump |
| Hardcoded credential or PII | Vague or missing trigger phrases in description |
| `Bash(*)` with no justification | Missing examples on one or more rules |
| Security-bypassing rule | REFERENCE.md absent on complex skill |
| `allowed-tools` missing | Description missing "Load proactively when..." |
| Invalid name convention | |
| Unfilled template placeholder | |

---

## Related skills

- **league-shared-skill-creator** — for contributors writing a new skill from
  scratch. Point authors there if the skill has structural issues that suggest
  it was not built from the template.
- **league-shared-skill-editor** — for contributors improving an existing skill.
  Point authors there if the skill has fixable issues and the author needs
  guidance on the local iteration workflow.
