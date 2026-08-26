#!/usr/bin/env python3
"""Merge cover.pdf + body.pdf and stamp page numbers, counting the cover as page 1.
RUN: python3 merge_and_stamp.py "ACCOUNT NAME" Output_File_v1.pdf"""
import sys, io, warnings; warnings.filterwarnings('ignore')
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

account = sys.argv[1] if len(sys.argv) > 1 else 'ACCOUNT'
out     = sys.argv[2] if len(sys.argv) > 2 else 'StrikeRoom_v1.pdf'
cov, bod = PdfReader('cover.pdf'), PdfReader('body.pdf')
total = len(cov.pages) + len(bod.pages)
buf = io.BytesIO(); c = canvas.Canvas(buf, pagesize=letter)
for i in range(len(bod.pages)):
    c.setFont('Courier', 6.5); c.setFillColorRGB(0.48, 0.53, 0.49)
    c.drawString(42, 16, f'INTRADIEM . GTM ENGINEERING - {account.upper()} STRIKE ROOM')
    c.drawRightString(570, 16, f'PAGE {i+2} OF {total}'); c.showPage()
c.save(); buf.seek(0)
ov = PdfReader(buf); w = PdfWriter(); w.add_page(cov.pages[0])
for i, pg in enumerate(bod.pages):
    pg.merge_page(ov.pages[i]); w.add_page(pg)
with open(out, 'wb') as f: w.write(f)
print(f'{out}: {total} pages')
