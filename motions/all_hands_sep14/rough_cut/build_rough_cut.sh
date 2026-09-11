#!/bin/bash
# Rough-cut assembler for the all-hands demo.
# Normalises every source clip to 1920x1080 / 30fps CFR / silent AAC, trims each to
# its script slot, drops the title cards and the two gap slates in at the act
# boundaries, and concatenates. Narration is deliberately stripped: this cut exists
# to validate story order, coverage and pacing before the takes are re-recorded.
set -euo pipefail

DL="$HOME/Downloads"
HERE="$(cd "$(dirname "$0")" && pwd)"
CARDS="$HERE/../title_cards"
WORK="$HERE/work"
OUT="${1:-$HOME/Desktop/AllHands_Demo_RoughCut_Sep5.mp4}"
mkdir -p "$WORK"

V="-c:v libx264 -preset veryfast -crf 20 -pix_fmt yuv420p -r 30 -g 60"
A="-f lavfi -i anullsrc=channel_layout=stereo:sample_rate=48000 -c:a aac -b:a 128k -shortest"

# clip <name> <file> <start> <duration> <pad_expr>
clip () {
  local n="$1" f="$2" ss="$3" t="$4" vf="$5"
  ffmpeg -hide_banner -loglevel error -y \
    -ss "$ss" -t "$t" -i "$DL/$f" $A \
    -vf "$vf,setsar=1,fps=30" -map 0:v:0 -map 1:a:0 $V "$WORK/$n.mp4"
  echo "  built $n ($t s)"
}

# card <name> <png> <duration>
card () {
  ffmpeg -hide_banner -loglevel error -y \
    -loop 1 -t "$3" -i "$2" $A \
    -vf "scale=1920:1080,setsar=1,fps=30" -map 0:v:0 -map 1:a:0 $V "$WORK/$1.mp4"
  echo "  built $1 ($3 s)"
}

FULL="crop=1920:958:0:60,pad=1920:1080:0:61:black"          # the four Loom browser takes
ACT1A="pad=1920:1080:101:1:black"                            # 1718x1078 Cowork window
ACT1B="crop=1668:1044:0:34,pad=1920:1080:126:18:black"       # 1668x1078 Cowork window

echo "Normalising..."
card c1 "$CARDS/01_act1.png" 3.5
clip a1a "Loom _ Free Screen & Video Recording Software _ Loom - 5 September 2026.mp4"        22 20 "$ACT1A"
clip a1b "Loom _ Free Screen & Video Recording Software _ Loom - 5 September 2026 (1).mp4"     5 45 "$ACT1B"
card c2 "$CARDS/02_act2.png" 3.5
card g2 "$HERE/gap_screen2.png" 3.0
clip a2clay "Contacts (Buying Committee) _ Star Ratings _ Clay - 5 September 2026.mp4"         2 50 "$FULL"
clip a2maps "Back Office Maps, Inger's Twelve - 5 September 2026.mp4"                          2 35 "$FULL"
clip a2icp  "ICP Buying Committees · Queue Optimizer, Back Office Optimizer and Engagement Hub - 5 September 2026.mp4" 2 35 "$FULL"
card c3 "$CARDS/03_act3.png" 3.5
clip a3lem  "lemlist • DWO Executives - Live Pool (Nate) - 5 September 2026.mp4"               78 42 "$FULL"
card c4 "$CARDS/04_coda.png" 3.5
card gc "$HERE/gap_coda.png" 3.0

printf "file '%s'\n" \
  "$WORK/c1.mp4" "$WORK/a1a.mp4" "$WORK/a1b.mp4" \
  "$WORK/c2.mp4" "$WORK/g2.mp4" "$WORK/a2clay.mp4" "$WORK/a2maps.mp4" "$WORK/a2icp.mp4" \
  "$WORK/c3.mp4" "$WORK/a3lem.mp4" \
  "$WORK/c4.mp4" "$WORK/gc.mp4" > "$WORK/concat.txt"

echo "Concatenating..."
ffmpeg -hide_banner -loglevel error -y -f concat -safe 0 -i "$WORK/concat.txt" -c copy "$OUT"
echo "Done: $OUT"
ffprobe -v error -show_entries format=duration -of csv=p=0 "$OUT" | awk '{printf "Runtime: %d:%02d\n", $1/60, $1%60}'
