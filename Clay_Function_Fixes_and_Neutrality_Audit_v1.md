# Clay Function Fixes + Motion-Neutrality Audit v1
**Confirmed live in workspace 1180800 on 2026-07-17 via direct read of the function editors (page-verbatim). Companion to the scaffold/stamping system. Both fixes are Clay-UI edits — Functions are not CLI/MCP-writable.**

## Why this matters beyond Cost-Mandate
These are your **shared** Functions — the reuse layer every motion stamps on top of. A bug here isn't a Cost-Mandate bug; it's a bug in the foundation of the whole stamping system. Two confirmed leaks below prove the "7 Functions = universal reuse layer" doctrine has motion-specific assumptions baked in. Fix these, then run the neutrality audit on all 7 before WFM-Adjacency.

---

## Confirmed findings (verbatim)

### Bug 1 — `fn_tokens_ready` hardcodes `install_base`
Live formula, last clause:
```
&& {{Function inputs}}?.["Universe"] == "install_base"
```
Every non-install-base row (all of Cost-Mandate, WFM-Adjacency, Stars) fails this AND → `tokens_ready = false` → exits node 5 `HOLD_incomplete`. This clause is Back Office logic (BO is the only motion where every row IS install_base). It leaked into a shared function.

### Bug 2 — `fn_draft_critic` is blind to the disclosed figure
The "Draft Audit" AI prompt binds subject, body, signal_evidence, top_signal, vertical to real inputs, but leaves three fields as literal text:
```
disclosed_figure: (none)
disclosed_figure_source: (none)
product_angle: (none)
```
The critic never receives the figure it is supposed to verify or its source, so it cannot discriminate a real cited number from a fabricated one — its stated core job. It still emits PASS/FAIL from body-vs-signal, which is why it ran "over-strict" (false FAILs) in session 4: with no figure context it can't confirm a legitimately disclosed number.

### Suspected Bug 3 — Cost-Mandate system prompt in a "shared" critic
The critic's System Prompt begins "You audit one cold email drafted for Intradiem's Cost-…". Its own description says "shared across all motions." **Read the full system prompt** — if it is Cost-Mandate-specific, a stamped WFM/Install-Base motion inherits the wrong audit framing. (Flagged, not confirmed in full — verify.)

---

## STATUS (updated 2026-07-17, live in workspace 1180800)
- **Fix 1 (`fn_tokens_ready`): DONE — applied and verified live.** The `&& Universe == "install_base"` clause was removed; the published formula now ends at `== "valid"`. Confirmed on the live (non-edit) function + Clay "All changes successfully published." Every non-install-base row now clears node 5.
- **Fix 2 (`fn_draft_critic`): NOT applied — bigger than a bind, deliberately not guessed.** Live inspection showed the three figure fields are **not declared inputs** AND **not present in the Record object** (its 27 keys don't include them). So there's nothing to bind to — the fix needs upstream schema + wiring across two sources. IMPORTANT: the critic is **not** a safety hole — it gets the disclosed number via `signal_evidence` (Cost Signal Research) and fails CLOSED; the real cost is over-strict FALSE-FAILs on legitimate `product_angle` proof stats (a yield tax, not a leak). Not urgent. See revised Fix 2.
- **`fn_eligible`: audited — clean.** Formula `!{{...}}["Install Base Lookup BO Universe"] && {{...}}["Customer Flag"] != true`. Parameterized (install-base + customer as inputs), no hardcoded motion value. Note: it's the *new-logo* exclusion; install-base motions need an inverted variant.
- Bug 3 (CM-specific critic system prompt): confirmed real, NOT auto-changed (policy decision).

## Fix 1 — `fn_tokens_ready` (make it motion-neutral) — ✅ DONE
1. Functions → `fn_tokens_ready` → click **Edit function** (top-right) to enter edit mode (column configs only save in edit mode).
2. Open the `tokens_ready` column formula.
3. **Delete** the trailing `&& {{Function inputs}}?.["Universe"] == "install_base"`. Recommended over patching: `tokens_ready` should only check token completeness (name, title, company, persona ≠ out_of_icp, email valid). Universe/population belongs in node 1 (`fn_eligible`), which already excludes install-base for new-logo motions and is the inverted gate for install-base motions. The universe check here is both wrong and redundant.
   - If you want to keep a population guard, do NOT hardcode a value — either make it presence-only (`{{Function inputs}}?.["Universe"] != ""`) or promote it to a function **input** so each motion supplies its own expected population. Hardcoding any single value re-creates the leak.
4. **Save changes.** Then re-open the column and re-read the formula to confirm it persisted (Clay's silent input-pin/config persistence bug — never trust the first save).

## Fix 2 — `fn_draft_critic` (REVISED after live inspection — this is structural, do it deliberately)
Live finding: the critic's declared inputs are **only** `Subject`, `Body`, `Record`, `Top Signal`, `Vertical`. In the prompt, `signal_evidence` binds to the `Record` object; `top_signal`/`vertical` bind to their own inputs. `disclosed_figure`, `disclosed_figure_source`, `product_angle` are literal `(none)` **and are not inputs anywhere** — so there is no chip to bind them to yet. The fix depends on one question:

**RESOLVED by live Record inspection (Jul 17):** the `Record` object's 27 keys do NOT include `disclosed_figure`, `disclosed_figure_source`, or `product_angle`. The disclosed number lives inside `Cost Signal Research (AI)` as free text (e.g. "…eliminating 56 jobs…"), which is exactly what `signal_evidence` binds to. So it's the bigger branch: those three fields don't exist to bind to.

**Severity is lower and safer than "blind," though — important:** the critic DOES receive the disclosed number, because `signal_evidence` (= `Cost Signal Research (AI)`, in the Record) carries it, and the Source Figure Law explicitly permits "a number literally present in signal_evidence." So:
- It CANNOT falsely pass a fabricated number — any number not present in `signal_evidence` (and `disclosed_figure`/`product_angle` are `(none)`) is disallowed → FAIL. **The gate fails CLOSED. It is not a safety hole.**
- Its real gap is `product_angle` (the verified-repository proof stat, e.g. the Humana webinar claim): with `product_angle: (none)`, the critic can't see it and will **FALSE-FAIL a legitimate proof stat**. This is the "over-strict" behavior from session 4 — a yield tax (rejects good drafts), not a leak (passes bad ones).

**So the fix is a deliberate design change, not urgent:** to let the critic validate branch-(b) proof stats (and enforce the source URL at the critic layer), add discrete `disclosed_figure` / `disclosed_figure_source` / `product_angle` fields to the upstream Record (they don't exist as columns today) and wire them in **both** sources (the "CFO, SVP & VP Operations…" persona table AND the workflow node 8), then bind in the prompt. That means deciding where those values come from — a verified-claims-policy decision, yours to make. Until then the critic is safe (fails closed) but occasionally over-rejects legitimate verified proof stats.

Why I did not auto-apply: confirmed the fields don't exist to bind, so any fix requires upstream schema + wiring changes across two consumers of the verified-claims gate — a design decision, not a mechanical edit.

After the bind: **Bug 3** — the system prompt opens "You audit one cold email drafted for Intradiem's Cost-Mandate motion" with a CM-specific "SOURCE FIGURE LAW." If this critic is to stay shared, genericize that framing or make the motion a passed input. This is your verified-claims policy, so it's your call, not an auto-edit.

Validate: re-run on real rows and confirm a real sourced figure PASSes and a blank-`source_url` figure FAILs — for the right reason (missing source), not lack of context.

## Then, and only then: run the H2 test
With both functions fixed, run the two fixtures on **real deliverable rows** (use 1–2 of the already-enriched hardened Cost-Mandate rows so email verify doesn't re-charge; doctor one copy into the known-bad with a fabricated number + blank source_url). Ledger the small MessageGen+critic spend. This is the test that was blocked at node 3 — it can only be meaningful after the critic can actually see the figure.

---

## Motion-Neutrality Audit — all 7 Functions (do before WFM-Adjacency)
The rule: **a shared Function must not hardcode any value that is true for one motion and false for another** — no literal `install_base`/`cost_mandate`, no single persona key, no single vertical, no customer name, no motion-specific system prompt. Open each, read the formula/prompt, flag any motion-specific literal.

| Function | Status | What to check |
|---|---|---|
| `fn_tokens_ready` | **LEAK — confirmed** | `install_base` hardcode (Fix 1) |
| `fn_draft_critic` | **LEAK — confirmed** | 3 unbound figure fields (Fix 2) + verify system prompt isn't Cost-Mandate-specific |
| `fn_persona_key` | **audited — CLEAN (+coverage note)** | Live formula returns bo_claims / bo_shared / coo_finance / **cc_ops** / out_of_icp — the earlier cc_ops gap is ALREADY FIXED. Rubric-key only, no motion literal. Coverage gap: NO `wfm` or `cx` branch (WFM/cx titles fall to out_of_icp). Add a `wfm` branch before WFM-Adjacency launch. Fine for Cost-Mandate. |
| `fn_send_ready` | **audited — CLEAN, fully hardened** | Verbatim: `Msg1 Critic Status=="PASS" && Human Approved && !Bdr Claimed && !Customer Exclude && Draft Clean && Email Status=="valid" ? "READY":"HOLD"`. All six conditions present (incl draft_clean + email_status — blueprint pre-req confirmed done). No motion literal. |
| `fn_eligible` | **audited — CLEAN** | Formula `!InstallBaseLookup && CustomerFlag != true`. Parameterized (install-base + customer as inputs), no hardcoded motion value. Correct new-logo kill switch. Archetype note: implements the *standard* (new-logo) exclusion only; an install-base motion needs an inverted eligibility variant. No fix needed for new-logo motions. |
| `fn_email_verified` | **audited — CLEAN (neutral by nature)** | Provider waterfall (Find Work Email → … → ZeroBounce) keyed on Full Name + Company Domain; email lookup can't carry a motion assumption. Heaviest credit line (23.1/row) — keep gated (only-if-empty + eligibility run-condition). |
| `fn_draft_clean` | **audited — CLEAN** | Verbatim: `!!Body && !Body.trim().startsWith("{") && !Body.includes('"subject"')`. Pure malformation guard, no motion literal. |

**Audit verdict (all 7 read live):** Only ONE true hardcoded-motion leak existed — `fn_tokens_ready` (fixed). `fn_draft_critic` is a structural/coverage gap, not a leak, and fails closed (safe). Everything else is clean. Two forward coverage items for later motions: add a `wfm` branch to `fn_persona_key` before WFM-Adjacency, and an inverted `fn_eligible` variant for install-base motions. The reuse layer is sound.

Log each result. Any function that passes clean is genuinely reusable; any leak found is one the stamping system would have silently inherited into motion #2.

## Bottom line
The fail-closed workflow did its job: it surfaced two foundation bugs (and a suspected third) before a single row was sent. Fix the two Functions in the UI, verify persistence, read the critic's system prompt, run the neutrality audit on the other five, then re-run the H2 test on real rows. Until the critic can see the figure, no send-readiness verdict from this pipeline is trustworthy.
