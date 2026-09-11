#!/usr/bin/env python3
"""rep-campaign-hook, step 1 (deterministic).

Why this exists (Sep 4 2026): Jack built ST Water by hand in the lemlist UI, six guessed
addresses went out from his mailbox, four bounced. Nothing in the pipeline sees a rep-built
campaign before it sends: the Clay verify path only covers what the engine pushes, and the
relay only reports bounces after the fact. This hook closes that gap.

What it does, every run:
  1. Lists lemlist campaigns (REST) and diffs against campaign_channel_map in
     config/lemlist_channels.json plus this job's own seen list.
  2. For every campaign it has not seen: resolves the owning rep (campaign sender, then
     creator, then a "(Jack)" / "(Nate)" name hint) and ADDS the id to the relay map under that
     rep. This is the one write the hook makes outside its own log and state (Dallas's ask,
     Sep 4 2026: "add it to the map routed by sender"). Unresolvable campaigns are logged as
     UNROUTABLE and left unmapped.
  3. Pulls the campaign's leads (export endpoint) and checks each one against Clay Audiences
     by email, then by LinkedIn URL. A lead with neither is "no Clay record": nobody verified it.
  4. Writes a DRY-RUN credit estimate for running wf_0tk4jo5z7RjGKo3rvR8 (Work Email waterfall
     + ZeroBounce) on the no-record leads, against the 200-credit warn-first line, and stages
     the workflow inputs as JSONL under automation/staging/rep_hook/. It never runs the
     workflow, never edits a lead, never touches campaign state.
  5. Appends to automation/logs/rep-campaign-hook-<date>.md (evt anchors per
     automation/LOG_CONVENTION.md) and prints a JSON line the wrapper uses to decide whether
     to launch step 2 (the lemlist-lead-integrity sweep plus the free Clay bridge).

Silence on empty: when nothing is new it writes nothing to the dated log (the rundown reads
"no log today" as "no new rep campaigns"); the quiet line goes to the wrapper's .out file.

Flags:
  --campaign cam_x   sweep this campaign even if it is already mapped or seen (on demand)
  --no-map-write     discovery + checks only, do not touch lemlist_channels.json
  --no-clay          skip the Audiences lookups (network-free smoke test)
"""
import argparse
import glob
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
API = "https://api.lemlist.com/api"
CHANNELS = os.path.join(HERE, "config", "lemlist_channels.json")
STATE = os.path.join(HERE, "config", "rep_campaign_hook.json")
LOG_DIR = os.path.join(HERE, "logs")
STAGE_DIR = os.path.join(HERE, "staging", "rep_hook")
HANDOFF = os.path.join(STAGE_DIR, "_handoff.txt")
WORKFLOW = "wf_0tk4jo5z7RjGKo3rvR8"
PLAN_GATE = "route is available starting"
TEST_MARK = "TEST-DELETE-BEFORE-LAUNCH"


# ---------- helpers ----------

def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def today():
    return datetime.now().strftime("%Y-%m-%d")


def load_key():
    with open(os.path.join(HERE, "config", "lemlist.env")) as f:
        for line in f:
            if line.startswith("LEMLIST_API_KEY="):
                return line.split("=", 1)[1].strip()
    sys.exit("LEMLIST_API_KEY not found in config/lemlist.env")


def lem_get(key, path):
    out = subprocess.run(["curl", "-s", "-u", f":{key}", f"{API}{path}"],
                         capture_output=True, text=True, timeout=90)
    try:
        return json.loads(out.stdout)
    except json.JSONDecodeError:
        return {"_error": out.stdout[:300]}


def clay_bin():
    found = shutil.which("clay")
    if found:
        return found
    cands = sorted(glob.glob(os.path.expanduser("~/.claude/plugins/cache/clay-plugins/clay/*/bin/clay")),
                   key=os.path.getmtime, reverse=True)
    return cands[0] if cands else None


def audiences_count(clay, field, operator, value):
    """Count Audiences people matching one field. Returns int, or None on error."""
    flt = {"type": "GroupOp", "combinationMode": "And", "entityType": "CONTACT", "items": [
        {"type": "BinOp", "entityType": "CONTACT", "key": field,
         "dataPath": ["contact_entity_field_values", "field", field],
         "operator": operator, "value": value}]}
    try:
        out = subprocess.run([clay, "audiences", "records", "search-count", "--entity-type", "people",
                              "--filter", json.dumps(flt)], capture_output=True, text=True, timeout=60)
        d = json.loads(out.stdout or "{}")
        return d.get("count") if "count" in d else None
    except Exception:
        return None


def li_slug(url):
    if not url:
        return ""
    m = re.search(r"linkedin\.com/(in/[^/?#]+)", url, re.I)
    return m.group(1).rstrip("/") if m else ""


def norm(s):
    """Lowercase, strip accents-ish and punctuation, for comparing a name to an email local part."""
    return re.sub(r"[^a-z]", "", (s or "").lower())


def pattern_flags(rows):
    """The ST Water class of defect: an address that does not match the person's own name, or
    two addresses for one person. Catches reversed name order (cawley.stephanie), a collapsed
    hyphen (martinrerrie), and a misspelled local part (johnathan for Jonathan). Pure string
    work on rows we already have; no network, no credits."""
    flags, by_person = [], {}
    for r in rows:
        email, first, last = r.get("email", ""), r.get("first_name", ""), r.get("last_name", "")
        if not email or "@" not in email:
            continue
        local = email.split("@", 1)[0]
        lo, f, l = norm(local), norm(first), norm(last)
        if f and l:
            # Compare on TOKENS, not raw substrings: "hunt" is a substring of "phil.hunter"
            # but not the same surname, and a wrong surname is exactly what has to be caught.
            toks = [norm(t) for t in re.split(r"[._\-]", local) if norm(t)]
            first_tok = toks[0] if toks else ""
            surname_ok = (l in toks
                          or "".join(toks[1:]) == l          # multi-word surname split across tokens
                          or "".join(toks) == f + l)          # whole name run together, no separator
            # Nickname tolerance on the FIRST name only (Philip -> phil, Daniel -> dan).
            # Jonathan -> johnathan is not a prefix either way, so it still surfaces.
            first_ok = (f in toks
                        or (len(first_tok) >= 3 and (f.startswith(first_tok) or first_tok.startswith(f))))
            if lo.startswith(l) and lo.endswith(f) and lo != f + l:
                flags.append(f"{r['who']} <{email}>: reversed name order, expected {first}.{last} shape")
            elif not first_ok or not surname_ok:
                missing = "first name" if not first_ok else "surname"
                flags.append(f"{r['who']} <{email}>: local part does not match the {missing} (misspelled, a different person, or a name change)")
        # A HYPHEN in the surname makes two addresses plausible (martin-rerrie and martinrerrie
        # both look right), so a guess is a coin flip. This is the exact Deborah Martin-Rerrie
        # bounce. Only the COLLAPSED form is ambiguous: an address that keeps a separator
        # between the parts is explicit and needs no flag. Apostrophes are excluded on purpose,
        # since O'Sullivan is collapsed to osullivan by convention, not by guesswork.
        parts = [p for p in (last or "").split("-") if p]
        if len(parts) > 1:
            a, b = parts[0].lower(), parts[1].lower()
            low = local.lower()
            if re.search(a + r"[-._]" + b, low) is None and (a + b) in re.sub(r"[^a-z]", "", low):
                dom = email.split("@", 1)[1]
                alt = f"{first}.{'-'.join(parts)}".lower()
                flags.append(f"{r['who']} <{email}>: hyphenated surname loaded collapsed; "
                             f"{alt}@{dom} is equally plausible, verify rather than guess")

        key = (f, l)
        if key != ("", ""):
            by_person.setdefault(key, set()).add(email)
    for (f, l), emails in by_person.items():
        if len(emails) > 1:
            flags.append(f"{f} {l}: {len(emails)} different addresses loaded ({', '.join(sorted(emails))}); at most one is right")
    return flags


def slugify(name):
    s = re.sub(r"[^a-z0-9]+", "-", (name or "").lower()).strip("-")
    return "-".join(s.split("-")[:4]) or "campaign"


def load_json(path, default):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        return default


def save_json(path, data):
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    os.replace(tmp, path)


# ---------- rep resolution ----------

def resolve_rep(camp, senders_by_campaign, state):
    rep_users = state.get("rep_users", {})
    cid = camp["_id"]
    uid = senders_by_campaign.get(cid)
    if uid in rep_users:
        return rep_users[uid], f"sender {uid}"
    creator = camp.get("createdBy")
    if creator in rep_users:
        return rep_users[creator], f"creator {creator}"
    name = (camp.get("name") or "").lower()
    for hint, rep in state.get("name_hints", {}).items():
        if hint.lower() in name:
            return rep, f"name hint '{hint}'"
    return None, f"no rep sender (sender {uid}, creator {creator})"


# ---------- main ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--campaign", action="append", default=[], help="force-sweep this campaign id")
    ap.add_argument("--no-map-write", action="store_true")
    ap.add_argument("--no-clay", action="store_true")
    args = ap.parse_args()

    key = load_key()
    state = load_json(STATE, {})
    state.setdefault("seen_campaigns", {})
    state.setdefault("exclude_campaign_ids", {})
    rate_low = float(state.get("credit_rate_low", 0.78))
    rate_high = float(state.get("credit_rate_high", 1.6))
    line = float(state.get("warn_first_line", 200))

    channels = load_json(CHANNELS, {})
    cmap = channels.setdefault("campaign_channel_map", {})

    # 1. discover
    # The handoff file is the ONLY thing the wrapper reads to decide whether to launch step 2.
    # It is rewritten (never appended) on every run, so a stale file can never trigger a rerun.
    os.makedirs(STAGE_DIR, exist_ok=True)
    open(HANDOFF, "w").close()

    resp = lem_get(key, "/campaigns?version=v2&limit=100")
    campaigns = resp.get("campaigns", []) if isinstance(resp, dict) else resp
    if not isinstance(campaigns, list) or (not campaigns and PLAN_GATE in str(resp)):
        print(json.dumps({"blocked": True, "reason": str(resp)[:200]}))
        with open(os.path.join(LOG_DIR, f"rep-campaign-hook-{today()}.md"), "a") as f:
            f.write(f"\n- {now()} BLOCKED: /api/campaigns unavailable ({str(resp)[:160]}). New rep campaigns are UNWATCHED this run.\n"
                    f"  evt: rep-campaign-hook-{today()}#blocked\n")
        return 0
    if len(campaigns) >= 100:
        more = lem_get(key, "/campaigns?version=v2&limit=100&offset=100")
        campaigns += more.get("campaigns", []) if isinstance(more, dict) else []

    senders = lem_get(key, "/team/senders")
    senders_by_campaign = {}
    if isinstance(senders, list):
        for s in senders:
            for c in s.get("campaigns", []):
                senders_by_campaign.setdefault(c["_id"], s["userId"])

    forced = set(args.campaign)
    targets = []
    for c in campaigns:
        cid = c["_id"]
        if cid in forced:
            targets.append(c)
            continue
        if cid in state["exclude_campaign_ids"]:
            continue
        seen = state["seen_campaigns"].get(cid)
        if seen:
            # A campaign swept while it had zero leads is re-checked until leads arrive.
            # Without this, a rep loading a draft later would never be seen: the campaign is
            # already in the relay map by then, and mapping is not verification.
            if seen.get("recheck_when_loaded"):
                targets.append(c)
            continue
        if cid in cmap:
            # Already routed and never swept by this hook: an engine-built campaign that
            # went through the Clay path at load time. Record it as seen so it is not
            # re-swept every hour, and leave it alone.
            state["seen_campaigns"][cid] = {"date": today(), "rep": cmap[cid],
                                            "note": "pre-existing in relay map, engine-built, not swept"}
            continue
        targets.append(c)

    if not targets:
        print(json.dumps({"new": [], "quiet": True, "at": now()}))
        return 0

    os.makedirs(STAGE_DIR, exist_ok=True)
    log_path = os.path.join(LOG_DIR, f"rep-campaign-hook-{today()}.md")
    new_file = not os.path.exists(log_path)
    clay = None if args.no_clay else clay_bin()
    result = {"new": [], "at": now(), "log": log_path}
    lines = []
    if new_file:
        lines.append(f"# rep-campaign-hook — {today()}\n")
        lines.append("Pre-send hook for rep-built lemlist campaigns. Step 1 is deterministic (this file's discovery, map, Clay-record, estimate sections); step 2 (integrity sweep, free bridge) is appended by the Claude session the wrapper launches. DRY RUN on every credit-bearing action: nothing here runs a workflow, edits a lead, or changes campaign state.\n")
    lines.append(f"\n## Run {now()}\n")

    # Campaigns already reported as empty on an earlier run: re-checked every run, but only
    # written up once they actually have leads, so an empty draft is not hourly noise.
    already_swept_empty = {cid for cid, v in state["seen_campaigns"].items()
                           if isinstance(v, dict) and v.get("recheck_when_loaded")}

    for c in targets:
        cid, name, status = c["_id"], c.get("name", ""), c.get("status", "")
        slug = slugify(name)
        evt = f"rep-campaign-hook-{today()}#{slug}"
        rep, how = resolve_rep(c, senders_by_campaign, state)
        sec_start = len(lines)
        lines.append(f"### {name} ({cid}), status {status}\n")
        lines.append(f"- evt: {evt}")
        lines.append(f"- chain: lemlist-relay-2026-09-04#run-1011 (ST Water bounces, the failure this hook exists for)")

        # 2. map
        mapped = False
        if rep and cid not in cmap and not args.no_map_write:
            cmap[cid] = rep
            mapped = True
            lines.append(f"- Relay map: ADDED {cid} -> {rep} (resolved by {how}). Events on this campaign now reach #gtm-outbound-{rep}.")
        elif rep and cid in cmap:
            lines.append(f"- Relay map: already {cmap[cid]} (resolver says {rep} by {how}).")
        elif rep:
            lines.append(f"- Relay map: would add {cid} -> {rep} (by {how}); --no-map-write, not written.")
        else:
            lines.append(f"- Relay map: UNROUTABLE, {how}. Left unmapped; Dallas assigns the rep or adds the id to exclude_campaign_ids in config/rep_campaign_hook.json.")

        # 3. leads + Clay record check
        leads = lem_get(key, f"/campaigns/{cid}/export/leads?state=all&format=json")
        if not isinstance(leads, list):
            lines.append(f"- Leads: could not read ({str(leads)[:120]}). Clay check UNVERIFIED.")
            state["seen_campaigns"][cid] = {"date": today(), "rep": rep, "leads": None}
            result["new"].append({"id": cid, "name": name, "rep": rep, "leads": None, "no_record": None})
            continue
        n = len(leads)
        test_rows, no_record, has_record, unchecked = [], [], [], []
        for L in leads:
            email = (L.get("email") or "").strip().lower()
            url = L.get("linkedinUrl") or ""
            who = f"{L.get('firstName','')} {L.get('lastName','')}".strip() or email or url
            if TEST_MARK in json.dumps(L) or email.endswith("@gmail.com"):
                test_rows.append(who)
                continue
            if clay is None:
                unchecked.append(who)
                continue
            cnt = audiences_count(clay, "email", "Equal", email) if email else 0
            if cnt is None:
                unchecked.append(who)
                continue
            if cnt == 0 and li_slug(url):
                cnt2 = audiences_count(clay, "linkedin_url", "Contain", li_slug(url))
                cnt = cnt2 if cnt2 is not None else 0
            (has_record if cnt else no_record).append({
                "who": who, "email": email, "url": url,
                "full_name": who, "first_name": L.get("firstName", ""), "last_name": L.get("lastName", ""),
                "company_name": L.get("companyName", ""),
                "company_domain": (email.split("@", 1)[1] if "@" in email else (L.get("companyDomain") or "")),
                "title": L.get("jobTitle", "")})

        if n == 0:
            state["seen_campaigns"][cid] = {"date": today(), "rep": rep, "leads": 0, "recheck_when_loaded": True}
            if cid in already_swept_empty:
                # Silent re-check: already reported as empty on an earlier run, so saying so
                # again every hour would be noise. Drop this section entirely.
                del lines[sec_start:]
                continue
            lines.append("- Leads: none loaded yet. Nothing to check; the hook re-checks every run until leads arrive, then sweeps them.")
            result["new"].append({"id": cid, "name": name, "rep": rep, "leads": 0, "no_record": 0,
                                  "staged": None, "evt": evt})
            lines.append("")
            continue

        lines.append(f"- Leads: {n} loaded. Clay Audiences record: {len(has_record)} yes, {len(no_record)} NO, {len(test_rows)} TEST rows, {len(unchecked)} unchecked"
                     + ("" if clay else " (clay CLI not found, lookups skipped)") + ".")
        if test_rows:
            lines.append(f"- TEST rows still loaded: {', '.join(test_rows)}. Remove before launch.")

        # The ST Water tells: an address that does not match its own person, and domain drift.
        pf = pattern_flags(no_record + has_record)
        if pf:
            lines.append("- ADDRESS PATTERN FLAGS (the ST Water defect class, check these before any send):")
            lines.extend(f"  - {x}" for x in pf)
        doms = {}
        for r in no_record + has_record:
            if r["email"]:
                doms.setdefault(r["email"].split("@")[1], []).append(r["email"])
        odd = [d for d in doms if len(doms) > 1 and len(doms[d]) == 1]
        if odd:
            lines.append(f"- Domain drift inside one campaign (single-address domains, check the TLD): {', '.join(odd)}.")

        if no_record:
            shown = no_record[:10]
            more = len(no_record) - len(shown)
            lines.append("- No Clay record (nobody verified these addresses): " + "; ".join(
                f"{r['who']} <{r['email'] or 'no email'}>" for r in shown)
                + (f"; plus {more} more, all listed in the staged file below." if more > 0 else ""))

        # 4. dry-run estimate + staged inputs
        if no_record:
            est_lo, est_hi = round(len(no_record) * rate_low, 1), round(len(no_record) * rate_high, 1)
            stage = os.path.join(STAGE_DIR, f"{cid}_{today()}.jsonl")
            with open(stage, "w") as f:
                for r in no_record:
                    f.write(json.dumps({k: r[k] for k in ("full_name", "first_name", "last_name",
                                                           "company_domain", "company_name", "title")}) + "\n")
            verdict = "under the 200 line: state the estimate, log the actual" if est_hi < line else \
                "ABOVE the 200 line: 10-20 row test first, then Dallas's go"
            lines.append(f"- DRY RUN estimate for {WORKFLOW} (Work Email waterfall + ZeroBounce) on {len(no_record)} rows: "
                         f"{est_lo} to {est_hi} credits at {rate_low}-{rate_high}/row; {verdict}. NOT RUN.")
            lines.append(f"- Staged inputs: {os.path.relpath(stage, REPO)} (one JSON object per row, ready for "
                         f"`clay workflows runs test {WORKFLOW} --inputs <row>`). Free bridge first (0 credits) in step 2.")
            lines.append(f"- To run it attended, paste: \"Verify the no-record leads in {name} ({cid}) from the staged file "
                         f"{os.path.relpath(stage, REPO)}: free bridge first, then {WORKFLOW} per row, estimate {est_lo}-{est_hi}, "
                         f"then update_lead on corrected emails and lemlist-lead-remove on failures. Do not restart the campaign.\"")
        else:
            lines.append("- Every lead has a Clay record; no verification spend proposed.")

        state["seen_campaigns"][cid] = {"date": today(), "rep": rep, "leads": n, "no_record": len(no_record)}
        result["new"].append({"id": cid, "name": name, "rep": rep, "leads": n, "no_record": len(no_record),
                              "staged": (os.path.relpath(stage, REPO) if no_record else None), "evt": evt})
        lines.append("")

    # Every target turned out to be a silent re-check (still-empty drafts): nothing to report,
    # so write no dated log at all. The rundown reads a missing file as "no rep campaigns",
    # which is the truth, and an empty run header would read as a finding.
    if not result["new"]:
        if not args.no_map_write:
            save_json(CHANNELS, channels)
            save_json(STATE, state)
        print(json.dumps({"new": [], "quiet": True, "rechecked": len(targets), "at": now()}))
        return 0

    with open(log_path, "a") as f:
        f.write("\n".join(lines) + "\n")

    # Pipe-delimited handoff for the wrapper: id|name|rep|staged|evt, one per line.
    # Written by python (not parsed out of JSON in zsh) so a quoting bug can never silently
    # turn a real finding into an empty "quiet" result and skip step 2.
    with open(HANDOFF, "w") as f:
        for c in result["new"]:
            f.write("|".join([c["id"], (c["name"] or "").replace("|", "/"),
                              c.get("rep") or "UNROUTABLE", c.get("staged") or "-",
                              c.get("evt") or "-"]) + "\n")
    # --no-map-write is the look-but-do-not-touch mode: it must not mark campaigns seen either,
    # or a dry test would suppress the next real run's discovery of the same campaigns.
    if not args.no_map_write:
        save_json(CHANNELS, channels)
        save_json(STATE, state)
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
