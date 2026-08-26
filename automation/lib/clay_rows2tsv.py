import json,sys
# usage: rows2tsv.py <fieldId>... ; reads CLI JSON (may contain raw control chars) on stdin, prints id + values TSV, and the cursor on the last line as "#CURSOR <cursor>"
fields=sys.argv[1:]
raw=sys.stdin.read()
d=json.loads(raw, strict=False)
for r in d.get("data",[]):
    cells=r.get("cells",{})
    vals=[]
    for f in fields:
        c=cells.get(f,{}) or {}
        v=c.get("value")
        s="" if v is None else (json.dumps(v) if isinstance(v,(dict,list)) else str(v))
        vals.append(s.replace("\t"," ").replace("\n"," ").replace("\r"," "))
    print("\t".join([r["id"]]+vals))
print("#CURSOR "+(d.get("cursor") or ""))
