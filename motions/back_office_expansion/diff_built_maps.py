#!/usr/bin/env python3
"""Diff the current build sheet against the snapshot Dallas built from, for maps already created in Sales Nav."""
import csv,os,sys,json
HERE=os.path.dirname(os.path.abspath(__file__))
BUILT=["Assurant","Cleveland Clinic","Cox Communications","DIRECTV"]
SNAP=os.path.join(HERE,"_built_snapshot.csv")
cur=[r for r in csv.DictReader(open(os.path.join(HERE,"BO_Map_Build_Sheets_Inger.csv"))) if r["account"] in BUILT]
if len(sys.argv)>1 and sys.argv[1]=="snapshot":
    with open(SNAP,"w",newline="") as fh:
        w=csv.DictWriter(fh,fieldnames=list(cur[0].keys())); w.writeheader(); w.writerows(cur)
    print("snapshot taken:",len(cur),"rows"); sys.exit()
old=list(csv.DictReader(open(SNAP)))
o={(r["account"],r["full_name"]):r for r in old}; c={(r["account"],r["full_name"]):r for r in cur}
out=["# Changes to maps already built in Sales Nav\n"]
any_change=False
for a in BUILT:
    adds=[k for k in c if k[0]==a and k not in o]; rems=[k for k in o if k[0]==a and k not in c]
    moves=[k for k in c if k[0]==a and k in o and c[k]["reports_up_to"]!=o[k]["reports_up_to"]]
    if not (adds or rems or moves): out.append(f"\n## {a}: no change\n"); continue
    any_change=True; out.append(f"\n## {a}\n")
    for k in adds: out.append(f"- ADD {k[1]} ({c[k]['title'][:50]}) under {c[k]['reports_up_to']}")
    for k in rems: out.append(f"- REMOVE {k[1]} ({o[k]['title'][:50]})")
    for k in moves: out.append(f"- MOVE {k[1]}: {o[k]['reports_up_to']} -> {c[k]['reports_up_to']}")
open(os.path.join(HERE,"BO_Map_Changes_Built.md"),"w").write("\n".join(out)+"\n")
print("\n".join(out)); print("\nANY CHANGE:",any_change)
