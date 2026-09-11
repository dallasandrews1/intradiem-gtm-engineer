#!/usr/bin/env python3
"""
Re-sync the narration booth and the narration script page from cues.json.

    python3 sync_narration.py [--video Intradiem_AllHands_Demo_v3_Sep9.mp4] [--date "9 September 2026"]

cues.json is the source of truth for every line and its timing. This rewrites the CUES
block in Narration_Booth.html, the read table and the counters in the script page
(../Narration_Script_<tag>.html, derived from the Sep 7 page), and the picture filename
both pages point at. Run it after any change to cues.json or to the cut's length.
"""
import json, re, html, os, argparse, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument("--video", default="Intradiem_AllHands_Demo_v3_Sep9.mp4")
ap.add_argument("--date", default="9 September 2026")
ap.add_argument("--tag", default="Sep9")
a = ap.parse_args()

cues = json.load(open(os.path.join(HERE, "cues.json")))
vid = os.path.expanduser("~/Desktop/" + a.video)
total = cues[-1]["end"]
if os.path.exists(vid):
    total = float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration",
                                  "-of","csv=p=0",vid],capture_output=True,text=True).stdout.strip())
def fmt(t): return f"{int(t)//60}:{int(t)%60:02d}"
words  = sum(0 if c["line"].startswith("[") else len(c["line"].split()) for c in cues)
spoken = sum(c["end"]-c["t"] for c in cues if not c["line"].startswith("["))
holds  = sum(1 for c in cues if c["line"].startswith("["))
wps    = round(words/spoken, 2)

# booth
p = os.path.join(HERE, "Narration_Booth.html"); s = open(p).read()
s = re.sub(r"const CUES = \[.*?\];", "const CUES = " + json.dumps(cues) + ";", s, count=1, flags=re.S)
s = re.sub(r"Intradiem_AllHands_Demo_v\d_Sep\d+\.mp4", a.video, s)
s = re.sub(r"/ \d+:\d\d\.\d", f"/ {fmt(total)}.{int((total%1)*10)}", s)
s = re.sub(r"1 / \d+", f"1 / {len(cues)}", s)
open(p, "w").write(s)

# script page
src = open(os.path.join(HERE, "..", "Narration_Script_Sep7.html")).read()
rows = "".join(f"<tr><td class='mono'>{fmt(c['t'])}</td><td>{html.escape(c['act'])}</td><td>{html.escape(c['line'])}</td>"
               f"<td class='mono'>{round(c['end']-c['t'])}s</td><td class='mono'>{0 if c['line'].startswith('[') else len(c['line'].split())}</td></tr>" for c in cues)
s = re.sub(r"(<tr><th>At</th><th>Where</th><th>Say</th><th>Room</th><th>Words</th></tr>).*?(</table>)", lambda m: m.group(1)+rows+m.group(2), src, flags=re.S)
s = re.sub(r"Intradiem_AllHands_Demo_v\d_Sep\d+\.mp4", a.video, s)
s = re.sub(r"<b>[\d:]+</b><span>picture locked</span>", f"<b>{fmt(total)}</b><span>picture locked</span>", s)
s = re.sub(r"<b>\d+</b><span>words in the read</span>", f"<b>{words}</b><span>words in the read</span>", s)
s = re.sub(r"<b>[\d.]+</b><span>words per second</span>", f"<b>{wps}</b><span>words per second</span>", s)
s = re.sub(r"<b>\d+</b><span>lines</span>", f"<b>{len(cues)}</b><span>lines</span>", s)
s = re.sub(r"<b>\d+</b><span>held silences</span>", f"<b>{holds}</b><span>held silences</span>", s)
s = s.replace("7 September 2026", a.date).replace("(Sep 7)", f"({a.tag[:3]} {a.tag[3:]})").replace("4:38", fmt(total))
s = s.replace('<div class="gate"><p><b>The new scenes read themselves.</b>',
  '<div class="gate"><p><b>New since Sep 7, both from Naveen:</b> a flow scene after the title card (six sources feeding one AI engine, the gate, the sequencer, meetings and Salesforce, then a pulse runs the whole path) and the AI named out loud on every line where it does the work. <b>The scenes read themselves.</b>')
out = os.path.join(HERE, "..", f"Narration_Script_{a.tag}.html")
open(out, "w").write(s)
print(f"{len(cues)} lines, {words} words, {wps} w/s, {holds} holds, picture {fmt(total)}  -> booth + {os.path.basename(out)}")
