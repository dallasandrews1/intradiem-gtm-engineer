#!/usr/bin/env python3
"""
embed_outfit_fonts.py

Post-processes a PPTX file to embed Outfit SemiBold and Outfit Regular,
so headlines render correctly on any machine without Outfit installed.

Usage:
    python embed_outfit_fonts.py input.pptx [output.pptx]

If output path is omitted, overwrites input in-place.
"""

import sys
import shutil
import zipfile
import os
import re
from pathlib import Path

FONTS = [
    {
        "ttf_path": "assets/Outfit-SemiBold.ttf",
        "typeface": "Outfit SemiBold",
        "zip_name": "Outfit-SemiBold.ttf",
        "rel_id": "rIdOutfitSemiBold",
    },
    {
        "ttf_path": "assets/Outfit-Regular.ttf",
        "typeface": "Outfit",
        "zip_name": "Outfit-Regular.ttf",
        "rel_id": "rIdOutfitRegular",
    },
]

CONTENT_TYPE = "application/x-fontdata"
FONT_REL_TYPE = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/font"


def patch_content_types(content: str) -> str:
    """Ensure .ttf has a Default entry in [Content_Types].xml."""
    if 'Extension="ttf"' not in content:
        insert = f'<Default Extension="ttf" ContentType="{CONTENT_TYPE}"/>'
        content = content.replace("</Types>", f"  {insert}\n</Types>")
    return content


def patch_font_table(content: str) -> str:
    """Add <a:font> entries for each Outfit variant in fontTable.xml."""
    for font in FONTS:
        if font["typeface"] in content:
            continue  # already present
        entry = (
            f'  <a:font typeface="{font["typeface"]}">\n'
            f'    <a:font typeface="{font["typeface"]}" r:id="{font["rel_id"]}"/>\n'
            f'  </a:font>\n'
        )
        content = content.replace("</a:fontTbl>", entry + "</a:fontTbl>")
    return content


def patch_font_rels(content: str) -> str:
    """Add Relationship entries in fontTable.xml.rels."""
    for font in FONTS:
        if font["rel_id"] in content:
            continue
        rel = (
            f'<Relationship Id="{font["rel_id"]}"\n'
            f'  Type="{FONT_REL_TYPE}"\n'
            f'  Target="../fonts/{font["zip_name"]}"/>'
        )
        content = content.replace("</Relationships>", f"  {rel}\n</Relationships>")
    return content


def embed_fonts(input_path: str, output_path: str):
    input_path = Path(input_path)
    output_path = Path(output_path)

    tmp = output_path.with_suffix(".tmp.pptx")

    with zipfile.ZipFile(input_path, "r") as zin, \
         zipfile.ZipFile(tmp, "w", compression=zipfile.ZIP_DEFLATED) as zout:

        names = zin.namelist()

        for name in names:
            data = zin.read(name)

            if name == "[Content_Types].xml":
                text = data.decode("utf-8")
                text = patch_content_types(text)
                data = text.encode("utf-8")

            elif name == "ppt/fontTable.xml":
                text = data.decode("utf-8")
                text = patch_font_table(text)
                data = text.encode("utf-8")

            elif name == "ppt/_rels/fontTable.xml.rels":
                text = data.decode("utf-8")
                text = patch_font_rels(text)
                data = text.encode("utf-8")

            zout.writestr(name, data)

        # If fontTable.xml.rels didn't exist, create it
        if "ppt/_rels/fontTable.xml.rels" not in names:
            rels_content = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">\n</Relationships>'
            rels_content = patch_font_rels(rels_content)
            zout.writestr("ppt/_rels/fontTable.xml.rels", rels_content.encode("utf-8"))

        # Embed the actual TTF files
        for font in FONTS:
            zip_entry = f"ppt/fonts/{font['zip_name']}"
            if zip_entry not in names:
                with open(font["ttf_path"], "rb") as f:
                    zout.writestr(zip_entry, f.read())
                print(f"  + Embedded {font['zip_name']}")
            else:
                print(f"  ~ {font['zip_name']} already present, skipping")

    tmp.replace(output_path)
    print(f"\n✅ Done: {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python embed_outfit_fonts.py input.pptx [output.pptx]")
        sys.exit(1)

    input_pptx = sys.argv[1]
    output_pptx = sys.argv[2] if len(sys.argv) > 2 else input_pptx

    print(f"Embedding Outfit fonts into: {input_pptx}")
    embed_fonts(input_pptx, output_pptx)
