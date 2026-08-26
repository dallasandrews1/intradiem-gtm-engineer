---
name: headless-render-workaround
description: "How to actually SEE/screenshot HTML builds in the sandbox so design work isn't done blind"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 08961b83-9830-4e80-9df7-23be56983c25
---

The sandbox CAN render HTML headlessly — use this to self-verify any visual/design build instead of guessing from the user's screenshots (the blind-build loop caused many near-miss design iterations Jun 25 2026).

**Setup (one-time per session):** Playwright chromium is already at `~/.cache/ms-playwright/chromium-1223/chrome-linux/chrome`. It fails only on a missing lib `libXdamage.so.1`. Pull it without root:
```
cd /sessions/<id> && mkdir -p libs && cd libs && apt-get download libxdamage1 && dpkg -x *.deb .
export LD_LIBRARY_PATH=/sessions/<id>/libs/usr/lib/aarch64-linux-gnu
```
Then `pip install playwright --break-system-packages` (package only; browser already downloaded). Launch with `args=["--no-sandbox","--disable-gpu"]`, `device_scale_factor=2`. Open the file via `pathlib.Path("index.html").resolve().as_uri()`.

**Updates verified Jul 2 2026:** (a) if the browser binary is missing, install with `PLAYWRIGHT_SKIP_VALIDATE_HOST_REQUIREMENTS=true python3 -m playwright install chromium` (plain install fails host validation; `--with-deps` fails, no root). (b) A shell `export LD_LIBRARY_PATH=...` does NOT reach the launched browser — pass it explicitly: `p.chromium.launch(env={**os.environ, "LD_LIBRARY_PATH": "/tmp/xd/usr/lib/aarch64-linux-gnu"})`. (c) Sandbox is aarch64, so the extracted lib path is `aarch64-linux-gnu`, never `x86_64`.

**Gotchas:** the page uses `.rv` scroll-reveal (opacity:0 until in view) — before screenshotting, run `document.querySelectorAll('.rv').forEach(e=>e.classList.add('in'))` and wait ~700ms or content shows faded. Section scroll-to is approximate; use `getBoundingClientRect().top+pageYOffset`. Save PNGs to the outputs dir (`/sessions/<id>/mnt/outputs/`) then Read them on the HOST path (`/Users/.../local_.../outputs/v_*.png`).

**Updates verified Jul 5 2026:** fresh sandboxes may have NO browser cached (`~/.cache/ms-playwright` absent) and no playwright pip package. Full cold-start that worked: `pip install playwright --break-system-packages`, then `python3 -m playwright install chromium --only-shell` (headless shell only, ~130MB, finishes in ~35s vs several stalled minutes for full chromium; run via nohup + poll `du -sh ~/.cache/ms-playwright` to see progress since the log buffers to 0 bytes). libxdamage1 fix same as above (aarch64 path). This run a plain shell `export LD_LIBRARY_PATH` before `python3` DID work with the headless shell (no explicit env= needed), but passing env= explicitly remains the safe default.

**For matching Naveen's site:** render mine headlessly AND load his live site in the connected Chrome extension; compare region by region. Deploying mine to a URL also lets both load in the same Chrome. See [[intradiem-official-brand]].
