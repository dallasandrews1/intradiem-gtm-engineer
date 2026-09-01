#!/usr/bin/env python3
"""Rep-set config loader for the back-office map pipeline.
A set is one rep's batch of accounts: sets/<name>.json holds the rep, the files, the built list, and the hand-curated
placements (drop / priority / manual_under / title_override / dual / verify / phrases / collision). Scripts take
`--set <name>` (default inger, or env BO_SET) and never hardcode a rep."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))

def load_set(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    name = os.environ.get("BO_SET", "inger")
    rest = []
    i = 0
    while i < len(argv):
        if argv[i] == "--set" and i + 1 < len(argv): name = argv[i + 1]; i += 2; continue
        if argv[i].startswith("--set="): name = argv[i].split("=", 1)[1]; i += 1; continue
        rest.append(argv[i]); i += 1
    p = os.path.join(HERE, "sets", f"{name}.json")
    if not os.path.exists(p): sys.exit(f"no such set: {p}")
    cfg = json.load(open(p))
    cfg["_name"] = name; cfg["_args"] = rest
    f = cfg["files"]
    cfg["_paths"] = {k: (os.path.join(HERE, v) if v else "") for k, v in f.items()}
    # tuple-keyed views of the curated lists
    cfg["_drop"] = set(cfg.get("drop", []))
    cfg["_priority"] = {tuple(x) for x in cfg.get("priority", [])} | {(m["account"], m["full_name"]) for m in cfg.get("manual_add", [])}   # researched executives always fill a slot
    cfg["_manual_under"] = {(a, n): m for a, n, m in cfg.get("manual_under", [])}
    cfg["_title_override"] = {(a, n): t for a, n, t in cfg.get("title_override", [])}
    cfg["_dual"] = {tuple(x) for x in cfg.get("dual", [])}
    cfg["_verify"] = {tuple(x) for x in cfg.get("verify", [])}
    cfg["_band_override"] = {(a, n): b for a, n, b in cfg.get("band_override", [])}
    cfg["_confirm"] = {(a, n): note for a, n, note in cfg.get("confirm", [])}   # stays on the map with a confirm badge (VERIFY benches)
    cfg["_root_exclude"] = {tuple(x) for x in cfg.get("root_exclude", [])}   # real officers of a subsidiary or plan: a top card, never the inferred manager of corporate functions
    cfg["_collision"] = {(a, n): why for a, d in cfg.get("collision", {}).items() for n, why in d.items()}
    return cfg
