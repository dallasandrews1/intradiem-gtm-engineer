const fs = require("fs");
const { Document, Packer, Paragraph, TextRun, LevelFormat, AlignmentType,
        BorderStyle, HeadingLevel } = require("docx");

const INK = "14181F";
const GREEN = "1B5E20";
const GRAY = "5A6068";

function h(text) {
  return new Paragraph({ heading: HeadingLevel.HEADING_2, spacing: { before: 240, after: 100 },
    children: [new TextRun({ text, bold: true, color: INK })] });
}
function p(runs, opts = {}) {
  return new Paragraph({ spacing: { after: 120, line: 276 }, ...opts,
    children: runs.map(r => typeof r === "string" ? new TextRun({ text: r }) : new TextRun(r)) });
}
function bullet(runs) {
  return new Paragraph({ numbering: { reference: "bullets", level: 0 }, spacing: { after: 80, line: 276 },
    children: runs.map(r => typeof r === "string" ? new TextRun({ text: r }) : new TextRun(r)) });
}

const doc = new Document({
  numbering: { config: [
    { reference: "bullets", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•",
      alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 540, hanging: 260 } } } }] }
  ]},
  styles: {
    default: { document: { run: { font: "Calibri", size: 22, color: INK } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal",
        run: { size: 32, bold: true, font: "Calibri", color: INK },
        paragraph: { spacing: { before: 0, after: 60 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal",
        run: { size: 24, bold: true, font: "Calibri", color: GREEN },
        paragraph: { spacing: { before: 240, after: 100 }, outlineLevel: 1 } },
    ]
  },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 },
      margin: { top: 1080, right: 1440, bottom: 1080, left: 1440 } } },
    children: [
      new Paragraph({ heading: HeadingLevel.HEADING_1,
        children: [new TextRun("Access Request: Claude Enterprise Seat")] }),
      new Paragraph({ spacing: { after: 240 }, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: GREEN, space: 4 } },
        children: [new TextRun({ text: "To: Jason Dowden, VP Technology   ·   From: Naveen Thilagan   ·   July 2026", size: 21, color: GRAY })] }),

      h("Request"),
      p(["One seat in our existing Claude Enterprise workspace for ", { text: "Dallas Andrews, GTM Engineer", bold: true }, " (reports to me). Access approval only; no new procurement."]),

      h("Business need"),
      p(["Dallas was hired for a specialist skill set: engineering go-to-market systems on AI platforms. In his first week he designed and stood up our account-scoring engine, a gated outreach pipeline where nothing sends without a human approval, and the verification and audit layers around both. Claude Enterprise is the platform he builds and operates that system on, the same way an engineer needs the company IDE rather than a personal one. The system he is building carries our Q3 commitments: 15 sales meetings, a 10x lift in outbound throughput, and 200-plus qualified back-office contacts. Provisioning the seat equips the expertise we hired and puts his work under company identity and controls from the start of the role."]),

      h("Data in scope"),
      bullet([{ text: "Will touch: ", bold: true }, "public CMS Star Ratings data, prospect and contact records from our licensed GTM tools (Clay, Salesforce, Sales Navigator), and internal GTM strategy documents."]),
      bullet([{ text: "Will not touch: ", bold: true }, "PHI, member data, customer production data, or anything from the product environment."]),
      bullet([{ text: "Enterprise workspace protections apply: ", bold: true }, "inputs and outputs excluded from model training by default, activity covered by workspace audit logs, account under Intradiem SSO with standard provisioning and offboarding."]),

      h("Controls already in place"),
      p(["Dallas designed the function to be auditable from day one: nothing reaches a prospect without an automated claims check plus a named human approval, every claim traces to a verified-claims repository he maintains, and all tool spend is logged in an append-only ledger. Happy to have him walk your team through it, audit trail included, if useful."]),

      h("Action requested"),
      p(["Provision one Claude Enterprise seat for Dallas under his Intradiem account (domain capture or direct invite, whichever your team prefers). I approve as his manager."]),
    ]
  }]
});

Packer.toBuffer(doc).then(b => { fs.writeFileSync(process.argv[2] || "out.docx", b); console.log("written"); });
