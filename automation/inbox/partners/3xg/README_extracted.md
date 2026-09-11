# Verint Partner Account Whitespace 2024, extracted copy

Source: Outlook forward from Frank Ciccone, Aug 31 2026 15:32 CT, original sender Jeremy Roderick (3xG Consulting). Attachment name: `Intradiem Work -Verint Partner Account Whitespace 2024.xlsx`.

How this was captured: the Microsoft 365 connector returns spreadsheet attachments as extracted, tab-delimited text per sheet, not as the original file. These CSVs are a faithful line-for-line transcription of that extraction (every line kept, every tab split into a cell, nothing dropped or reordered). The original .xlsx (formulas, formatting, hidden columns, merged cells) was NOT saved to disk. Read-only intake; nothing was sent and no mailbox item was modified.

## Sheets

| Sheet (as named in the workbook) | CSV | Lines in CSV | Header row (1-based CSV line) | Data rows after header | Non-empty data rows |
|---|---|---|---|---|---|
| Quantified Whitespac No SSA-IRS | whitespace_2024__quantified_whitespac_no_ssa_irs.csv | 1306 | 7 | 1299 | 1298 (1,297 account rows + 1 footer row of x marks) |
| Verint Partner Only 2024 | whitespace_2024__verint_partner_only_2024.csv | 84 | 1 | 83 | 83 (74 in header layout + 9 in the bottom block) |

### Sheet 1: Quantified Whitespac No SSA-IRS

CSV lines 1 to 6 are the workbook's preamble above the header (a Prereq's / 150 min. note whose cell text wrapped across lines 2 to 4 in the extraction, a List Price row for the opportunity columns, and a Totals / Total Opportunity row). The column header is CSV line 7. Columns 4, 27 and 28 have blank header cells in the source (column 4 carries an "x" flag on some rows; 27 and 28 are spacer columns).

Header (38 columns):
1. Bill To Name
2. Account Name
3. Bucket
4. ''
5. Max License
6. Type    (WFE)
7. EDM-Rec
8. Rec
9. Encrp
10. QM
11. AQM
12. DPA
13. WFM
14. WFMPro
15. PM
16. Speech
17. RTAA
18. IQ
19. CF
20. XM
21. VFC
22. community
23. RecPubSafe
24. ChAuto
25. KMEnt
26. KMPro
27. ''
28. ''
29. Workflex
30. Quality Bot
31. Trans Bot
32. Wrap Up 624+128
33. Voice Capture
34. RT Coach w Trans
35. Redaction
36. Speech 480+120
37. Encryption
38. Total

Note: every row after the header has the full 38-column width. CSV lines 8 to 1304 are the 1,297 account rows of the main table (Bill To Name through Total). CSV line 1305 is a footer row of "x" marks under the opportunity columns and line 1306 is empty; both are kept as extracted.

### Sheet 2: Verint Partner Only 2024

Header is CSV line 1. Column 4 has a blank header cell in the source (an "x" flag). CSV lines 2 to 75 are the 74 partner-account rows in the header's layout. CSV lines 76 to 84 are a second block of 9 rows in a different layout that the workbook holds below the table: Partner (Direct or TTEC), Account, three blank cells, a Verint back-office product name (Operations Manager, Operations Visualizer, Operations Productivity, eg Work Manager) in the Model column position, and a seat count in the DPA Seats column position. Kept exactly as extracted.

Header (9 columns):
1. Partner
2. Account
3. Max Verint
4. ''
5. Max Verint license
6. Model
7. DPA Seats
8. Vertical Alignment
9. DPA-Max Licence

## Provenance
Extracted Sep 1 2026 via the claude.ai Microsoft 365 connector (read_resource on the message attachment). Converter kept in the session scratchpad only; regenerate by re-reading the attachment if needed.
