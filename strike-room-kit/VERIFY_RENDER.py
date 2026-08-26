#!/usr/bin/env python3
"""Render pages to PNG so you can LOOK at them. Both Jul 29 bugs were invisible
in the HTML and obvious in the render. Never ship without doing this.
RUN: python3 VERIFY_RENDER.py Output_v1.pdf 1 12 16"""
import sys, pypdfium2 as p
d = p.PdfDocument(sys.argv[1])
pages = [int(x) for x in sys.argv[2:]] or [1, 2, 3]
for n in pages:
    d[n-1].render(scale=1.6).to_pil().save(f'verify_p{n}.png')
    print(f'verify_p{n}.png')
print(f'total pages: {len(d)}  <- now Read these PNGs and actually look at them')
