# Strike Room Kit (green-kit PDF pipeline)
Proven on Cardinal Health v2, Blue Shield of CA, Aflac (Jul 2026).

Usage in a fresh cloud session:
1. Stage this folder via device_stage_files, copy to a working dir (uploads is read-only).
2. Put the finished packet md in the same dir. Edit build_pdf_TEMPLATE.py per its header comments.
3. curl the logo if logo.svg is missing: https://intradiem.com/wp-content/themes/intradiem/src/img/logo.svg
4. Run: python3 build_pdf_TEMPLATE.py && python3 render.py
5. Merge + page numbers (pypdf + reportlab), counting the cover as page 1:

from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io
cov, bod = PdfReader('cover.pdf'), PdfReader('body.pdf')
total = len(cov.pages) + len(bod.pages)
buf = io.BytesIO(); c = canvas.Canvas(buf, pagesize=letter)
for i in range(len(bod.pages)):
    c.setFont('Courier', 6.5); c.setFillColorRGB(0.48,0.53,0.49)
    c.drawString(42, 16, 'INTRADIEM . GTM ENGINEERING - [ACCOUNT] STRIKE ROOM')
    c.drawRightString(570, 16, f'PAGE {i+2} OF {total}'); c.showPage()
c.save(); buf.seek(0)
overlay = PdfReader(buf); w = PdfWriter(); w.add_page(cov.pages[0])
for i, pg in enumerate(bod.pages):
    pg.merge_page(overlay.pages[i]); w.add_page(pg)
with open('[Account]_StrikeRoom_Sequence_v1.pdf','wb') as f: w.write(f)

Key mechanics baked in: cover renders at 6.375in x 8.25in (the print zoom 1.333333 trick makes that exactly Letter); body pages flow naturally (no fixed heights; page-break-inside:avoid on touch cards gives each contact an entry-week + escalation spread). The md must follow the section structure of the two v1 reference packets at project root (--- separators; "**Touch N (Day X) — Channel**" lines).
