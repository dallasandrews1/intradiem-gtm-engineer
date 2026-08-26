---
name: cloudflare-pages-edge-propagation
description: "Cloudflare Pages serves old and new builds from different edges for minutes after deploy; verify with batched samples, never consecutive ones"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 70497397-25f3-4c4f-af31-d8a2961a3267
  modified: 2026-08-07T03:40:26.612Z
---

After `wrangler pages deploy`, the project root (e.g. `icp-committees.pages.dev`) serves a **mix** of the old and new build for several minutes. Different requests hit different edge nodes, so verification is probabilistic, not a single yes/no.

The trap: an `until` loop that stops after N *consecutive* matching samples gives false confidence. On 6 Aug 2026 a "6 consecutive samples" check passed, and the very next request returned the previous build. Consecutive runs of new-version hits happen easily while old-version edges are still live.

**Verify like this instead:** batch 12 samples per round, count new versus old, and only call it propagated when `old == 0` in a full round.

```bash
L=$(shasum -a 256 index.html | cut -d' ' -f1)
for round in $(seq 1 12); do
  new=0; old=0
  for i in $(seq 1 12); do
    s=$(curl -s -H 'Cache-Control: no-cache' https://<proj>.pages.dev/ | shasum -a 256 | cut -d' ' -f1)
    [ "$s" = "$L" ] && new=$((new+1)) || old=$((old+1))
  done
  echo "round $round: new=$new old=$old"
  [ $old -eq 0 ] && break
  sleep 20
done
```

Two related points. The **deployment-specific URL** (`https://<hash>.<proj>.pages.dev`) is deterministic and correct immediately, so use it to prove the upload itself was complete and separate a propagation lag from a genuinely bad deploy. And when sweeping asset URLs, do **not** append a query string to bust cache: `?x=1` changes the cache key and returns 404s on Pages that clean URLs return 200 for, which looks exactly like missing files.

Finish by diffing the downloaded page against local (`curl -s <url> -o live.html; diff -q index.html live.html`) rather than trusting a hash comparison done in a separate request.
