#!/usr/bin/env python3
"""
Render the motion scenes Naveen asked for on 7 September.

Each scene is one HTML page that draws its own state from a ?k= keyframe index,
so the build-on animation is deterministic: render k=0..N as stills, then
cross-dissolve them on a per-keyframe hold. That gives motion that reads as
designed rather than as a slideshow, without a frame-by-frame render.

    python3 build_scenes.py            builds every scene to ./out/<name>.mp4
    python3 build_scenes.py system     builds one
"""
import subprocess, sys, os, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.join(HERE, "out")
WORK = os.path.join(HERE, "work")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
V = "-c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p -r 30 -g 60".split()

# name: (page, [hold seconds per keyframe], dissolve between keyframes)
SCENES = {
 # title, then the six steps one at a time, then what runs itself, then the
 # checkpoints, then the three act lanes laid over the same rail.
 "system": ("system.html",
            [2.2, 1.0,1.0,1.0,1.0,1.0,1.0, 1.7,1.7, 1.6,1.6,1.6, 2.0], 0.20),
 # act title, then problem, then what we do, then where the AI is.
 # every source, one engine: title, six sources, the engine, the gate, the
 # sequencer and AM clearance, meetings and Salesforce, the loop, then a dot
 # travels the whole path (rendered as frames, not keyframes) and a hold.
 "flow":   ("flow.html",
            [2.2, 0.7,0.7,0.7,0.7,0.7, 1.6, 2.0, 2.0, 1.8, 1.6], 0.20),
 "act1":   ("act1.html", [1.7, 2.0, 2.3, 2.6], 0.25),
 "act2":   ("act2.html", [1.7, 2.0, 2.4, 2.6], 0.25),
 "act3":   ("act3.html", [1.7, 2.0, 2.3, 2.6], 0.25),
 "coda1":  ("coda1.html", [1.4, 1.7, 1.7, 1.9], 0.25),
 "coda2":  ("coda2.html", [1.4, 1.7, 1.7, 1.9], 0.25),
}

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(" ".join(str(c) for c in cmd)); print(r.stderr[-2500:]); sys.exit(1)

# name: (keyframe to hold the diagram on, seconds the dot travels, capture fps, hold after)
PULSE = {"flow": (10, 5.0, 12, 1.4)}

def build(name):
    page, holds, xf = SCENES[name]
    holds = list(holds)
    wd = os.path.join(WORK, name)
    shutil.rmtree(wd, ignore_errors=True); os.makedirs(wd)
    stills = []
    for k in range(len(holds)):
        png = os.path.join(wd, f"k{k:02d}.png")
        run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
             "--force-device-scale-factor=1", "--window-size=1920,1080",
             f"--screenshot={png}", f"file://{HERE}/{page}?k={k}"])
        stills.append(png)

    segs = []
    for k, (png, hold) in enumerate(zip(stills, holds)):
        mp4 = os.path.join(wd, f"s{k:02d}.mp4")
        run(["ffmpeg","-hide_banner","-loglevel","error","-y","-loop","1","-t",str(hold),
             "-i",png,"-vf","scale=1920:1080,setsar=1,fps=30,format=yuv420p","-an",*V,mp4])
        segs.append(mp4)

    if name in PULSE:
        kk, secs, fps, tail = PULSE[name]
        n = int(secs * fps)
        for i in range(n + 1):
            png = os.path.join(wd, f"p{i:03d}.png")
            run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                 "--force-device-scale-factor=1", "--window-size=1920,1080",
                 f"--screenshot={png}", f"file://{HERE}/{page}?k={kk}&p={i/n:.4f}"])
        mp4 = os.path.join(wd, "pulse.mp4")
        run(["ffmpeg","-hide_banner","-loglevel","error","-y","-framerate",str(fps),
             "-i",os.path.join(wd,"p%03d.png"),
             "-vf","scale=1920:1080,setsar=1,minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:vsbmc=1,format=yuv420p",
             "-an",*V,mp4])
        segs.append(mp4); holds.append((n + 1) / fps)
        mp4 = os.path.join(wd, "tail.mp4")
        run(["ffmpeg","-hide_banner","-loglevel","error","-y","-loop","1","-t",str(tail),
             "-i",os.path.join(wd,f"p{n:03d}.png"),"-vf","scale=1920:1080,setsar=1,fps=30,format=yuv420p","-an",*V,mp4])
        segs.append(mp4); holds.append(tail)

    ins, fc, cur, off = [], [], "[0:v]", 0.0
    for m in segs: ins += ["-i", m]
    for i in range(1, len(segs)):
        off = (off + holds[i-1] - xf) if i > 1 else (holds[0] - xf)
        nxt = f"[v{i}]" if i < len(segs)-1 else "[vout]"
        fc.append(f"{cur}[{i}:v]xfade=transition=fade:duration={xf}:offset={off:.3f}{nxt}")
        cur = nxt
    dst = os.path.join(OUT, name + ".mp4")
    run(["ffmpeg","-hide_banner","-loglevel","error","-y",*ins,
         "-filter_complex",";".join(fc),"-map","[vout]",*V,dst])
    d = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                        "-of","csv=p=0",dst],capture_output=True,text=True).stdout.strip()
    print(f"  {name:<8} {len(holds)} keyframes  {float(d):5.2f}s  -> {dst}")

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    names = sys.argv[1:] or list(SCENES)
    print("Rendering scenes...")
    for n in names: build(n)
