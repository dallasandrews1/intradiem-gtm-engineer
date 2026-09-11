#!/usr/bin/env python3
"""
Drop a narration recording onto the locked picture.

    python3 add_narration.py voice.m4a [-o out.mp4] [--offset 0.0]

Takes any audio file QuickTime, Voice Memos or a phone will produce, cleans it
(80 Hz high-pass to lose desk rumble, loudness normalised to -16 LUFS which is
where web video sits), and muxes it onto the cut without re-encoding the picture.
--offset shifts the voice; positive delays it, negative trims the head off.
Warns if the read is more than two seconds off the picture rather than silently
letting one run past the other.
"""
import subprocess, sys, os, argparse

HERE  = os.path.dirname(os.path.abspath(__file__))
VIDEO = os.path.expanduser("~/Desktop/Intradiem_AllHands_Demo_v3_Sep9.mp4")

def dur(path):
    r = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                        "-of","csv=p=0",path],capture_output=True,text=True)
    return float(r.stdout.strip())

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("voice")
    ap.add_argument("-o","--output", default=os.path.expanduser(
        "~/Desktop/Intradiem_AllHands_Demo_v3_Sep9_narrated.mp4"))
    ap.add_argument("--video", default=VIDEO)
    ap.add_argument("--offset", type=float, default=0.0)
    a = ap.parse_args()

    for p in (a.voice, a.video):
        if not os.path.exists(p):
            sys.exit(f"Not found: {p}")

    vd, ad = dur(a.video), dur(a.voice)
    print(f"picture {vd:.1f}s   voice {ad:.1f}s   difference {ad + a.offset - vd:+.1f}s")
    gap = abs(ad + a.offset - vd)
    if gap > 2.0:
        print(f"  Heads up: the read and the picture are {gap:.1f}s apart.")
        print("  Under-run leaves the closing card silent; over-run gets cut at the end.")

    af = "highpass=f=80,loudnorm=I=-16:TP=-1.5:LRA=11"
    if a.offset > 0:
        af = f"adelay={int(a.offset*1000)}|{int(a.offset*1000)},{af}"

    cmd = ["ffmpeg","-hide_banner","-loglevel","error","-y","-i",a.video]
    if a.offset < 0:
        cmd += ["-ss", str(abs(a.offset))]
    cmd += ["-i",a.voice,"-filter_complex",f"[1:a]{af},apad[a]",
            "-map","0:v:0","-map","[a]","-c:v","copy","-c:a","aac","-b:a","192k","-ar","48000","-ac","2",
            "-shortest","-movflags","+faststart",a.output]
    r = subprocess.run(cmd,capture_output=True,text=True)
    if r.returncode:
        print(r.stderr[-2000:]); sys.exit(1)
    print(f"Done: {a.output}  ({dur(a.output):.1f}s)")

if __name__ == "__main__":
    main()
