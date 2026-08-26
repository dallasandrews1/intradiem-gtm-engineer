#!/usr/bin/env python3
"""Merge memory index files (MEMORY.md) without duplicating pointers.

usage: merge_index.py BASE.md [OTHER.md ...] --out OUT.md [--exclude name.md ...] [--label "text"]

Keeps BASE verbatim, then appends every pointer line from the OTHER files whose link
target is not already present in BASE (and not excluded). One line per memory, no content.
"""
import re, sys, argparse

LINK = re.compile(r"\]\(([^)]+)\)")

def pointers(path):
    out = []
    try:
        lines = open(path, encoding="utf-8").read().splitlines()
    except FileNotFoundError:
        return out
    for ln in lines:
        if ln.lstrip().startswith("- ") and LINK.search(ln):
            out.append((LINK.search(ln).group(1).split("/")[-1], ln.rstrip()))
    return out

ap = argparse.ArgumentParser()
ap.add_argument("base"); ap.add_argument("others", nargs="*")
ap.add_argument("--out", required=True); ap.add_argument("--exclude", nargs="*", default=[])
ap.add_argument("--label", default="Swept from harness memory stores")
a = ap.parse_args()

excluded = set(a.exclude)
base_text = open(a.base, encoding="utf-8").read().rstrip("\n") if a.base and a.base != "-" else "# Memory index"
seen = {t for t, _ in pointers(a.base)} if a.base != "-" else set()
# drop excluded pointers from the base copy too
base_lines = [ln for ln in base_text.splitlines()
              if not (LINK.search(ln) and LINK.search(ln).group(1).split("/")[-1] in excluded)]
added = []
for other in a.others:
    for target, line in pointers(other):
        if target in seen or target in excluded:
            continue
        seen.add(target); added.append(line)
with open(a.out, "w", encoding="utf-8") as f:
    f.write("\n".join(base_lines).rstrip("\n") + "\n")
    if added:
        f.write(f"\n## {a.label}\n")
        f.write("\n".join(added) + "\n")
print(f"index: {len(seen)} pointers, {len(added)} added, {len(excluded)} excluded")
