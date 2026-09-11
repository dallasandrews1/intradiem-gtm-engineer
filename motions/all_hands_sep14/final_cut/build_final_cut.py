#!/usr/bin/env python3
"""
Final-cut assembler for the all-hands demo (v2 takes, 5 Sep 2026).

Every source is a silent screen capture at one of three window sizes. This script
conforms each one to 1920x1080 / 30fps, trims it to the slot the recording script
gives it, drops the nine brand cards in at the act boundaries, and cross-dissolves
the whole thing into one file.

Trim points are chosen to keep unrendered template tokens and product warning
banners out of frame. See FINAL_CUT_NOTES.md for what each window excludes.
"""
import subprocess, sys, os, shutil

DL   = os.path.expanduser("~/Downloads")
HERE = os.path.dirname(os.path.abspath(__file__))
CARDS= os.path.join(HERE, "..", "title_cards")
SCENES= os.path.join(HERE, "..", "scenes", "out")
WORK = os.path.join(HERE, "work")
OUT  = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser(
        "~/Desktop/Intradiem_AllHands_Demo_v3_Sep9.mp4")

PAD  = "0xF5F4F2"          # brand --sidebar; matches every page background in shot
XF   = 0.4                 # cross-dissolve length
V    = "-c:v libx264 -preset slow -crf 17 -pix_fmt yuv420p -r 30 -g 60".split()

C = {
 "claude": "Claude - 5 September 2026.mp4",                 # 1722x1080  Act 1, Cowork
 "mercury":"Google Chrome - 5 September 2026.mp4",          # 2164x1080  Coda, one-pager
 "ally":   "Google Chrome - 5 September 2026 (1).mp4",      # 2164x1080  Coda, partner brief
 "icp":    "Google Chrome - 5 September 2026 (2).mp4",      # 2164x1080  Act 2, committees
 "maps":   "Google Chrome - 5 September 2026 (3).mp4",      # 2164x1080  Act 2, back-office maps
 "lemlist":"Google Chrome - 5 September 2026 (4).mp4",      # 1602x1080  Act 3, sequence
 "aud":    "Google Chrome - 5 September 2026 (5).mp4",      # 2164x1080  Act 2, Audiences
 "clay":   "Google Chrome - 5 September 2026 (6).mp4",      # 2164x1080  Act 2, enrichment
}

# Geometry per source window. Pads are centred and filled with the brand sidebar
# tone so the letterbox reads as page margin rather than a black bar. Two sources
# get a pre-crop: the Audiences take carries Chrome's hover-URL bar along the
# bottom edge, and the lemlist take carries the product's support-chat launcher in
# the bottom-right corner. Both are cropped away rather than left in frame.
CENTRE   = f"pad=1920:1080:(ow-iw)/2:(oh-ih)/2:{PAD}"
FIT_2164 = f"scale=1920:-2:flags=lanczos,{CENTRE}"
FIT_1722 = CENTRE
FIT_1602 = CENTRE
FIT_AUD  = f"crop=2164:1040:0:0,scale=1920:-2:flags=lanczos,{CENTRE}"
FIT_LEM  = f"crop=1512:990:0:0,{CENTRE}"
FIT = {"claude":FIT_1722, "lemlist":FIT_LEM, "aud":FIT_AUD}

# name, kind, source, start, duration, speed
#
# Built to Naveen's 7 September notes: the retitled opener, a system scene that
# walks the engine before any tool appears, a scene in front of each act that
# states the problem, what we do and where the AI is, and the partner brief
# framed by two slides instead of read off the page.
#
# Speeds are pacing, not effect. The Act 1 window is a continuous hand-scroll so
# it is eased only to 0.75. The lemlist window is pixel-frozen from 2.7s to
# 15.9s, so its middle is stretched to 0.6 with nothing moving to slow down.
EDL = [
 ("01_open",   "card",  "00_open.png",  None,  4.0, 1.0),
 ("02_flow",   "scene", "flow.mp4",     None, None, 1.0),   # every source, one engine (Naveen, 9 Sep)
 ("02_system", "scene", "system.mp4",   None, 16.0, 1.0),   # one engine, three acts on it
 ("03_act1",   "scene", "act1.mp4",     None,  7.8, 1.0),   # problem / what we do / where the AI is
 ("04_plan",   "clip",  "claude",        0.0, 19.5, 0.75),  # thesis, dated signals, committee
 ("05_object", "clip",  "claude",       70.0,  9.0, 1.0),   # objection handles + skills panel
 ("06_out1",   "card",  "10_out1.png",  None,  2.8, 1.0),
 ("07_act2",   "scene", "act2.mp4",     None,  7.9, 1.0),
 ("08_aud",    "clip",  "aud",           2.0, 31.0, 1.0),   # 140,993 -> saved segment -> 312
 ("09_clay",   "clip",  "clay",          3.0, 36.0, 1.0),   # enrichment running, columns filling
 ("10_maps",   "clip",  "maps",          8.0, 33.0, 1.0),   # hero -> MetLife map
 ("11_icp",    "clip",  "icp",          28.0, 20.0, 1.0),   # ring -> State Farm -> how to read it
                                                            # hard stop: beta terms and early-adopter
                                                            # pricing enter this page at 48.5s
 ("12_out2",   "card",  "20_out2.png",  None,  2.8, 1.0),
 ("13_act3",   "scene", "act3.mp4",     None,  7.8, 1.0),
 ("14_lem_a",  "clip",  "lemlist",       0.0,  3.0, 1.0),   # settle on the rendered email
 ("15_lem_b",  "clip",  "lemlist",       3.0, 12.5, 0.6),   # the hold, eased out
 ("16_lem_c",  "clip",  "lemlist",      15.5,  4.0, 1.0),   # down to the first branch
 ("17_out3",   "card",  "30_out3.png",  None,  2.8, 1.0),
 ("18_coda1",  "scene", "coda1.mp4",    None,  6.0, 1.0),   # the ask, what came back, who runs it
 ("19_ally",   "clip",  "ally",          2.0, 14.0, 1.0),   # the real brief, so it is not just slides
 ("20_coda2",  "scene", "coda2.mp4",    None,  6.0, 1.0),   # sourced, dated, partner-safe
 ("21_ally_b", "clip",  "ally",         40.0, 12.0, 1.0),   # who to talk to, the people table
 ("22_merc",   "clip",  "mercury",      14.0, 10.0, 1.0),   # follow-up one-pager
 ("23_end",    "card",  "40_end.png",   None,  4.5, 1.0),
]

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(" ".join(cmd)); print(r.stderr[-3000:]); sys.exit(1)

def main():
    shutil.rmtree(WORK, ignore_errors=True); os.makedirs(WORK)
    print("Conforming segments...")
    durs = []
    for name, kind, src, ss, dur, speed in EDL:
        dst = os.path.join(WORK, name + ".mp4")
        if kind == "card":
            vf = "scale=1920:1080,setsar=1,fps=30,format=yuv420p"
            run(["ffmpeg","-hide_banner","-loglevel","error","-y",
                 "-loop","1","-t",str(dur),"-i",os.path.join(CARDS,src),
                 "-vf",vf,"-an",*V,dst])
        elif kind == "scene":
            # already 1920x1080/30fps out of build_scenes.py; copy the stream
            run(["ffmpeg","-hide_banner","-loglevel","error","-y",
                 "-i",os.path.join(SCENES,src),"-an","-c:v","copy",dst])
        else:
            vf = FIT.get(src, FIT_2164)
            if speed != 1.0:
                vf += f",setpts=PTS/{speed}"
            vf += ",setsar=1,fps=30,format=yuv420p"
            run(["ffmpeg","-hide_banner","-loglevel","error","-y",
                 "-ss",str(ss),"-t",str(dur),"-i",os.path.join(DL,C[src]),
                 "-vf",vf,"-an",*V,dst])
        out = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                              "-of","csv=p=0",dst],capture_output=True,text=True).stdout.strip()
        durs.append(float(out))
        print(f"  {name:<10} {durs[-1]:6.2f}s")

    print("Cross-dissolving...")
    ins, fc, cur, off = [], [], "[0:v]", 0.0
    for i,(name,*_ ) in enumerate(EDL):
        ins += ["-i", os.path.join(WORK, name + ".mp4")]
    for i in range(1, len(EDL)):
        off = (off + durs[i-1] - XF) if i > 1 else (durs[0] - XF)
        nxt = f"[v{i}]" if i < len(EDL)-1 else "[vout]"
        fc.append(f"{cur}[{i}:v]xfade=transition=fade:duration={XF}:offset={off:.3f}{nxt}")
        cur = nxt
    run(["ffmpeg","-hide_banner","-loglevel","error","-y",*ins,
         "-filter_complex",";".join(fc),"-map","[vout]",
         *V,os.path.join(WORK,"video.mp4")])

    print("Muxing silent track...")
    run(["ffmpeg","-hide_banner","-loglevel","error","-y",
         "-i",os.path.join(WORK,"video.mp4"),
         "-f","lavfi","-i","anullsrc=channel_layout=stereo:sample_rate=48000",
         "-c:v","copy","-c:a","aac","-b:a","128k","-shortest",
         "-movflags","+faststart",OUT])

    # timecodes every review page reads: [start, end, name, kind, src, dur]
    import json
    rows, t = [], 0.0
    for i,((name,kind,src,*_),d) in enumerate(zip(EDL,durs)):
        rows.append([round(t,2), round(t+d,2), name, kind, src, round(d,2)])
        t += d - XF
    json.dump(rows, open(os.path.join(HERE,"edl_timecodes.json"),"w"), indent=1)

    d = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                        "-of","csv=p=0",OUT],capture_output=True,text=True).stdout.strip()
    print(f"Done: {OUT}\nRuntime: {int(float(d))//60}:{int(float(d))%60:02d}")

if __name__ == "__main__":
    main()
