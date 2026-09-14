#!/bin/zsh
cd "$(dirname "$0")"
clay credits > balance_before.json 2>&1
clay routines runs start function:t_0thx4ovuPGp8sjH2hPP --input "$(cat input.json)" > start.json 2>&1
RID=$(python3 -c "import json;d=json.load(open('start.json'));print(d.get('runId') or d.get('id') or d.get('run',{}).get('id',''))")
echo "run $RID"
for i in 1 2 3 4 5 6; do
  clay routines runs get "$RID" --wait 60 --limit 100 > result.json 2>&1
  python3 -c "import json,sys;d=json.load(open('result.json'));items=d.get('data',[]);done=all(x.get('status') in ('complete','error','failed') for x in items) and len(items)>=8;print('items',len(items),'done',done);sys.exit(0 if done else 1)" && break
  sleep 15
done
clay credits > balance_after.json 2>&1
python3 -c "
import json
d=json.load(open('result.json'))
for x in d.get('data',[]): print(x['id'], x.get('status'), (x.get('result') or {}).get('Work Email'))
b=json.load(open('balance_before.json'))['balance']; a=json.load(open('balance_after.json'))['balance']; print('credits', b, '->', a, 'spent', round(b-a,1))"
