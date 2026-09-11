#!/usr/bin/env python3
"""The snapshot contract shared by the generator and the brain.

Why this file exists
--------------------
The brain used to `import account_engine` and read the CSVs sitting next to it in the
container. The Dockerfile copies those CSVs in at build time, so the data the brain served
was frozen at the last deploy and there was no path to refresh it short of a rebuild. On
2026-09-05 that produced a strike plan for Centene at fit 43 Tier 3 with no agent count and
no triggers, against a local engine that had the same account at 88 Tier 1 with three
sourced triggers, and copy reading "On ~0 agents that's about $0 a year" under a subject
line about a seven-figure number.

The fix has three parts and they all live here so the two sides cannot disagree:

  1. PROVENANCE IS PER ROW. Every record carries `source` and `seed`. A row with no
     citation is seed data, whatever the engine-level tag says.
  2. AGE IS ALWAYS ON THE RESPONSE. Every payload carries `generated_at`, `age_hours` and
     `freshness`. A caller can no longer fail to notice that an answer is two months old.
  3. STALE MEANS REDACTED, NOT WRONG. Past the age threshold, and on any seed row, the
     confident fields (fit, tier, ROI, agent count, generated copy) are REMOVED and
     replaced by a warning. A missing number forces a question. A stale number gets quoted.

That last rule is the point. The Centene incident did not happen because the brain was
silent; it happened because the brain was confident.
"""
import datetime

SCHEMA_VERSION = 2

# Past this age a payload is redacted (see redact_row). The generator runs nightly at 21:30
# off automation/sync_publish.sh, so 36h leaves a full missed run of headroom before the
# brain starts stripping numbers.
DEFAULT_MAX_AGE_HOURS = 36.0

# Past this age the payload is refused outright. A week-old strike universe is not a
# degraded answer, it is a different company.
DEFAULT_HARD_MAX_AGE_HOURS = 168.0

# The fields that assert something. Identity (domain, company, industry, seller) survives
# redaction so a caller still knows which account it asked about; everything that is a
# number, a score, or generated prospect-facing copy does not.
CONFIDENT_FIELDS = {
    "strike": ("icp_total", "tier", "dims", "roi_annual", "roi_label", "roi_per_agent",
               "roi_per_agent_label", "agent_count", "committee", "why_now_raw", "fresh"),
    "signal": ("signals", "signals_fired", "primary_routing"),
}


def utcnow():
    return datetime.datetime.now(datetime.timezone.utc)


def iso(dt):
    return dt.replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_iso(s):
    """Accept the Z suffix and naive stamps; treat a naive stamp as UTC."""
    if not s:
        return None
    try:
        dt = datetime.datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except ValueError:
        return None
    return dt.replace(tzinfo=datetime.timezone.utc) if dt.tzinfo is None else dt


def age_hours(generated_at, now=None):
    dt = parse_iso(generated_at)
    if dt is None:
        return None
    return round(((now or utcnow()) - dt).total_seconds() / 3600.0, 2)


def freshness(age, max_age=DEFAULT_MAX_AGE_HOURS, hard_max=DEFAULT_HARD_MAX_AGE_HOURS):
    """'fresh' | 'stale' | 'expired' | 'unknown'.

    An unreadable or absent timestamp is 'unknown' and is treated as stale everywhere,
    never as fresh. A snapshot dated in the future is the same class of defect as a
    trigger dated in the future (see account_engine.recency_factor) and is not trusted.
    """
    if age is None:
        return "unknown"
    if age < 0:
        return "unknown"
    if age > hard_max:
        return "expired"
    return "fresh" if age <= max_age else "stale"


def redact_row(row, kind, reason):
    """Strip the asserting fields from one record and say what was removed and why."""
    out = {k: v for k, v in row.items() if k not in CONFIDENT_FIELDS.get(kind, ())}
    removed = sorted(k for k in CONFIDENT_FIELDS.get(kind, ()) if k in row)
    out["redacted"] = removed
    out["redaction_reason"] = reason
    return out


def seed_reason(row):
    """Why this row is seed, in the words the CLI already uses, or None if it is cited."""
    if not row.get("seed"):
        return None
    return ("No `source` on this row, so it is demonstration data. It scores, but nothing "
            "on it may reach a prospect, a seller, a slide or a recording.")


# The prose on a trigger IS the claim: `detail`, `play` and `stakes` are what the sequence
# copy is written from. A trigger with no citation must not carry them, whatever the rest of
# the row looks like.
TRIGGER_PROSE = ("label", "detail", "play", "stakes")


def scrub_triggers(row, stale):
    """Drop the prose from any trigger that is uncited, or from all of them when stale.

    Kept deliberately separate from redact_row: a row can be seed purely because its
    agent_count is missing while its triggers are properly sourced, and throwing away real
    why-now signal in that case would be its own kind of wrong.
    """
    trigs = row.get("triggers")
    if not isinstance(trigs, list):
        return row
    out = []
    for t in trigs:
        if not isinstance(t, dict):
            continue
        if stale or not (t.get("source") or "").strip():
            kept = {k: v for k, v in t.items() if k not in TRIGGER_PROSE}
            kept["redacted"] = [k for k in TRIGGER_PROSE if k in t]
            kept["redaction_reason"] = ("Snapshot is not fresh." if stale
                                        else "This trigger carries no source.")
            out.append(kept)
        else:
            out.append(dict(t))
    return {**row, "triggers": out}


def apply_gates(rows, kind, fresh_state, age):
    """Redact per row: stale/unknown snapshot redacts everything, seed redacts that row."""
    stale_reason = None
    if fresh_state == "stale":
        stale_reason = (f"Snapshot is {age}h old, past the {DEFAULT_MAX_AGE_HOURS}h freshness "
                        "threshold. Figures withheld rather than served at an unknown age. "
                        "Re-run the snapshot generator.")
    elif fresh_state == "unknown":
        stale_reason = ("Snapshot carries no usable `generated_at`, so its age cannot be "
                        "established. Figures withheld.")
    out = []
    for r in rows:
        reason = stale_reason or seed_reason(r)
        row = redact_row(r, kind, reason) if reason else dict(r)
        out.append(scrub_triggers(row, bool(stale_reason)))
    return out


def envelope(state, now=None, max_age=DEFAULT_MAX_AGE_HOURS, hard_max=DEFAULT_HARD_MAX_AGE_HOURS):
    """The freshness header stamped onto every brain response."""
    gen = state.get("generated_at")
    a = age_hours(gen, now)
    f = freshness(a, max_age, hard_max)
    env = {
        "generated_at": gen,
        "age_hours": a,
        "freshness": f,
        "schema_version": state.get("schema_version"),
    }
    if f == "stale":
        env["warning"] = (f"This snapshot is {a}h old (threshold {max_age}h). Scores, ROI and "
                          "generated copy have been withheld. Do not quote anything from it.")
    elif f == "unknown":
        env["warning"] = ("This snapshot has no usable timestamp. Scores, ROI and generated "
                          "copy have been withheld.")
    return env
