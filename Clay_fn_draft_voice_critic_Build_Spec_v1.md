# Clay Function Build Spec — `fn_draft_voice_critic` (v1.0, Jul 17 2026)

The 8th shared Function. Extracts the Voice Audit (cadence) gate out of every motion's table into **one** callable definition, so Stars, Cost-Mandate, and Back Office can never again drift to different voice versions. Companion to `Clay_Functions_Build_Pack_v1.md` (this is the voice sibling of F1 `fn_draft_critic`). Carries Voice Fix **v2** (fails STACKED and CHOPPED).

---

## 0. Why voice is the cleanest shared Function you own

`fn_draft_critic` (F1) had a structural leak: it referenced fields (`disclosed_figure`, `product_angle`) that were hardcoded literals, not real inputs, and its system prompt is Cost-Mandate-specific. It can't be truly motion-neutral without work.

`fn_draft_voice_critic` has the opposite property. It judges **cadence only** — never facts, numbers, claims, or motion angle — so it has **zero motion-specific inputs**. Its only input is the draft text. That makes it structurally impossible for it to leak one motion's logic into another. It is the ideal shared gate: build once, reference everywhere, nothing per-motion to keep in sync.

This is the fix for the "did I update the voice column in Cost-Mandate or Back Office?" question. After this, there is no per-motion voice column to update — there is one Function.

---

## 1. Function definition

- **Name:** `fn_draft_voice_critic`
- **Inputs (the only things that change per row/table):**
  - `draft_body` (text, required) — the MessageGen email body being judged
  - `draft_subject` (text, optional; Required-to-run OFF) — included for completeness; the cadence judgment is about the body
- **Internal steps:**
  1. **AI column** — strong reasoning model (Anthropic Claude Sonnet or an OpenAI o-series). **NOT GPT-4o** — the same model lesson as the s4 `fn_draft_critic` swap; GPT-4o under-discriminates on cadence. System prompt = §2 below, verbatim.
  2. **Parse formula** — extract the four JSON fields from the AI output into typed outputs (§3).
- **Outputs:**
  - `voice_verdict` (PASS / FAIL) — the gate field
  - `voice_reason` (text, one sentence)
  - `voice_failure_mode` (STACKED / CHOPPED / NONE)
  - `voice_worst_line` (text; empty when PASS)

Credits: the Function costs nothing; the one AI action inside it bills exactly as the current per-motion `voice_audit` column does. This is consistency + fix-once, not credit savings (same as every other Function).

---

## 2. AI system prompt — paste verbatim into the Function's AI step

```text
You audit one cold email for VOICE only. You do not check facts, numbers, or claims. You judge one thing: does this read like one person explaining something to another, or like AI generated it? Return a verdict and one line of reason.

There are two AI failure modes. You fail BOTH.

FAIL, STACKED (too dense) if:
- The opening sentence packs two or more facts as comma-separated phrases before the main verb (appositive stacking). Example: "X sits at 3.0 stars this cycle, a full star under the bonus line, with no contract in the mix."
- Any sentence is a pile of comma-separated facts with no connecting logic (nothing like because / so / which / though tying the parts together).

FAIL, CHOPPED (too robotic) if:
- Three or more short, flat sentences in a row with no connectors, each a bare subject-verb-object. Example: "X is at 3.0. That's under the line. No contract is close. It's multi-year."
- The sentences don't hand off to each other; the email reads as a list of facts rather than one connected thought with an arc.

FAIL, either mode also if:
- It uses a decorative metaphor or filler phrase for color ("the climb", "sequencing", "cliff-edge" in prose, "spark", "north star", or a flourish sentence that adds no new fact).

PASS only if: the sentences connect with real logic and build a through-line (situation, then what it means, then why now, then what it's worth, then the ask); the rhythm varies, mostly medium connected sentences with at most one short sentence used as a deliberate beat; the words are plain and spoken; and it reads like a sharp person wrote it to a peer in one sitting. Length is fine when it comes from connected clauses; short sentences are fine as spice, not as the default.

Return exactly: { "verdict": "PASS" or "FAIL", "reason": "one sentence", "failure_mode": "STACKED" or "CHOPPED" or "NONE", "worst_line": "the single worst sentence, or empty if PASS" }
```

---

## 3. Parse formula (AI JSON → the four outputs)

The AI step returns a JSON object. Parse each field defensively (uppercase the verdict/mode, trim). Reference the AI column as `{{voice_ai}}` (rename to your AI step's actual column name):

- `voice_verdict` = `{{voice_ai.verdict}}?.toString()?.trim()?.toUpperCase()` — expect `PASS` / `FAIL`
- `voice_reason` = `{{voice_ai.reason}}?.toString()?.trim()`
- `voice_failure_mode` = `{{voice_ai.failure_mode}}?.toString()?.trim()?.toUpperCase()` — expect `STACKED` / `CHOPPED` / `NONE`
- `voice_worst_line` = `{{voice_ai.worst_line}}?.toString()?.trim()`

**Fail-closed rule:** if the AI output does not parse to a clean `PASS`, treat `voice_verdict` as `FAIL`. A garbled critic output must never read as a pass.

---

## 4. Baked-in test fixtures (anti-rubber-stamp — do this before Publish)

Same discipline as F1's H2 fixtures. Save these three rows as the Function's test inputs. **Any future edit must still produce these exact verdicts before Publish** — that is what stops a silently-passing voice gate.

| # | `draft_body` (test input) | Must return |
|---|---|---|
| **PASS** | "CalOptima OneCare is sitting at 3.0 stars right now, which puts it a full star under the 4.0 bonus line. None of the contracts are close enough to clear that in a single cycle, so realistically this is a multi-year effort rather than a one-cycle push. What makes the timing worth a note is where CMS is steering the rating: through 2029 it keeps shifting weight onto the CAHPS experience measures, so the service side is increasingly what decides whether you get over the line. And it's not a one-time number. It's roughly $9.6M a year in addressable QBP for every year the contract stays under 4.0. I've put the contract-level math on a single page. Worth 15 minutes to talk through how you're approaching the next couple of cycles?" | `verdict: PASS`, `failure_mode: NONE` |
| **FAIL-STACKED** | "CalOptima OneCare sits at 3.0 stars this cycle, a full star under the 4.0 bonus line, with no cliff-edge contract in the mix, so the climb has to be multi-year. CMS keeps concentrating the rating into the CAHPS experience core through 2029, so the service measures your team can move only get more decisive from here." | `verdict: FAIL`, `failure_mode: STACKED` |
| **FAIL-CHOPPED** | "CalOptima OneCare is at 3.0 stars. That's under the 4.0 line. No contract is close. So it's a multi-year fix. The service side matters most. CMS is shifting weight there. Your team can move it." | `verdict: FAIL`, `failure_mode: CHOPPED` |

If any fixture returns the wrong verdict after an edit, the edit is wrong, not the fixture. Do not Publish until all three are green.

---

## 5. Build steps (current Clay UI)

Fastest path reuses the hardened Cost-Mandate column per the extraction doctrine ("extract from Cost-Mandate, not the older Stars columns").

1. **First make Cost-Mandate's `voice_audit` column v2** (paste §2 above into it) so the extraction source is correct. If it's already v2, skip.
2. On the Cost-Mandate contacts table (`t_0ti8tdqQAXiWMkx76Jj`), Cmd-click the `voice_audit` AI column header (and its parse formula column if separate) → right-click → **Save as function**.
3. In the dialog: name `fn_draft_voice_critic`; set **inputs** = `draft_body` (+ optional `draft_subject`); set **outputs** = `voice_verdict`, `voice_reason`, `voice_failure_mode`, `voice_worst_line`. Leave **"Replace columns with function" unchecked** on the first build (keep the originals until proven). → **Create**.
   - *Alternative if Save-as-function is awkward:* **Functions** sidebar → **+ New Function** → one AI step (paste §2) → parse formulas (§3) → same inputs/outputs.
4. **Functions** sidebar → `fn_draft_voice_critic` → **Edit function** → **Add test inputs** → paste the three §4 fixtures → confirm PASS/NONE, FAIL/STACKED, FAIL/CHOPPED → **Review Changes** → **Publish Changes**.

---

## 6. Wiring — point every motion's send gate at the Function

Replace each motion's per-column voice reference with the Function output, then retire the local `voice_audit` columns once proven in ≥2 motions.

- **Cost-Mandate** `send_ready`: change `... && {{voice_audit}}=="PASS" && ...` → `... && {{fn_draft_voice_critic.voice_verdict}}=="PASS" && ...`
- **Back Office** sync run-condition: change `&& voice_audit_bo == "PASS"` → `&& {{fn_draft_voice_critic.voice_verdict}} == "PASS"`
- **Stars** both sync run-conditions ("Sync leads to campaign (2)" and "(3)"): change `{{Voice Audit.voice_verdict}} == "PASS"` → `{{fn_draft_voice_critic.voice_verdict}} == "PASS"`
- Map the Function's `draft_body` input to each table's MessageGen body column (`MessageGen Email 1`, `MessageGen Email 1 (BO)`, etc.).

**Prove before relying:** run the Function on a 10-row slice per motion, confirm the three fixtures still discriminate after Publish, and confirm every `send_ready` / sync condition still reads HOLD. A voice gate that silently passes is worse than the per-motion column it replaces.

---

## 7. Definition of done

`fn_draft_voice_critic` published with the v2 STACKED/CHOPPED prompt and the three §4 fixtures saved and green; called from Cost-Mandate, Back Office, and Stars via `voice_verdict`; the per-motion `voice_audit` / `voice_audit_bo` columns retired once proven in ≥2 motions; every send gate still fail-closed to HOLD. Nothing sent. This is the doctrine target from `messagegen-voice-gate-gap` closed: one voice gate, every motion inherits it.
```
