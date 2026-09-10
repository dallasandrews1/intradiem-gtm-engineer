#!/usr/bin/env python3
"""Build the Sep 1 list-review page for the call with Frank from the intake outputs.

Reads review_sep1/3xg_candidates_ranked.csv, 3xg_extended_pool.csv, 3xg_intake_report.md and writes
List_Review_Frank_Sep1.src.html; then run build_page.py to assemble the kit page.

The page is a working screen for the call: filter by bucket, mark each account cohort / holdout / skip,
picks persist in the browser, and "Copy picks" puts the decision on the clipboard. Local file only:
the list is 3xG's data and does not get a public URL.
"""
import csv
import datetime as dt
import html
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
REV = HERE / "review_sep1"

BUCKET_LABEL = {
    "operational_visualizer": ("Operational visualizer", "A first Verint back-office deployment, then nothing. Frank's priority."),
    "backoffice_deployment": ("Back-office deployment", "Verint Work Manager in place."),
    "dpa_deployed": ("Desktop analytics deployed", "DPA seats in place; the rest of the seat count is the whitespace."),
    "verint_no_dpa": ("Verint, no desktop analytics", "Front-office footprint only."),
}
ORDER = ["operational_visualizer", "backoffice_deployment", "dpa_deployed", "verint_no_dpa"]
SHORT = {"operational_visualizer": "Op. visualizer", "backoffice_deployment": "Back office", "dpa_deployed": "DPA deployed", "verint_no_dpa": "No DPA"}


def esc(s):
    return html.escape(str(s if s is not None else ""))


def short_flags(f: str):
    out = []
    for part in [p.strip() for p in f.split(";") if p.strip()]:
        if part.startswith("HOLD"):
            out.append(("hold", part))
        elif part.startswith("CHECK"):
            out.append(("check", "Near-name to confirm: " + part.split("'")[1] if "'" in part else part))
        elif part == "in TAM list":
            out.append(("go", "TAM list"))
        elif part == "Frank priority":
            out.append(("go", "Priority"))
        elif "also an Intradiem partner" in part:
            out.append(("now", "Reseller is an Intradiem partner"))
        elif part.startswith("sold "):
            out.append(("hold", "Verint direct"))
        elif part == "also on the partner sheet":
            out.append(("hold", "Also on partner sheet"))
    return out


def main():
    rows = list(csv.DictReader((REV / "3xg_candidates_ranked.csv").open(encoding="utf-8")))
    ext = list(csv.DictReader((REV / "3xg_extended_pool.csv").open(encoding="utf-8")))
    ranked = [r for r in rows if r["rank"]]
    held = [r for r in rows if not r["rank"]]
    counts = {b: sum(1 for r in ranked if r["bucket"] == b) for b in ORDER}
    stamp = dt.date.today().strftime("%b %-d %Y")

    def row_html(r):
        fl = short_flags(r["flags"])
        pills = " ".join(f'<span class="pill {c}">{esc(t)}</span>' for c, t in fl if c != "hold" or t in ("Verint direct", "Also on partner sheet"))
        bo = r["back_office_product"] or ""
        bid = f"r{r['rank']}"
        notes = ('<div class="nt">' + pills + '</div>') if pills else ""
        prod = ("<small>" + esc(bo) + "</small>") if bo else ""
        return (f'<tr class="cand" data-b="{r["bucket"]}" data-id="{bid}" data-name="{esc(r["account"])}">'
                f'<td class="st">{r["rank"]}</td>'
                f'<td class="who">{esc(r["account"])}{prod}{notes}</td>'
                f'<td class="pick"><button data-p="cohort">Cohort</button><button data-p="holdout">Holdout</button><button data-p="skip">Skip</button></td>'
                f'<td><span class="bk {r["bucket"]}">{SHORT[r["bucket"]]}</span></td>'
                f'<td class="num">{esc(r["verint_seats"])}</td><td class="num">{esc(r["dpa_seats"])}</td>'
                f'<td class="st">{esc(r["wfm_in_footprint"]).replace("not on matrix sheet", "n/a")}</td><td class="st">{esc(r["vertical_alignment_as_given"])}</td>'
                f'<td class="rs">{esc(r["reseller_of_record"])}</td>'
                f'</tr>')

    table = "\n".join(row_html(r) for r in ranked)

    held_rows = "\n".join(
        f'<tr><td class="who">{esc(r["account"])}</td><td><span class="bk {r["bucket"]}">{BUCKET_LABEL[r["bucket"]][0]}</span></td>'
        f'<td class="num">{esc(r["verint_seats"])}</td><td>{esc(r["flags"].split(";")[0].replace("HOLD: ", ""))}</td></tr>'
        for r in held)
    checks = [r for r in ranked if "CHECK" in r["flags"]]
    check_rows = "\n".join(
        f'<tr><td class="who">{esc(r["account"])}</td><td><span class="bk {r["bucket"]}">{BUCKET_LABEL[r["bucket"]][0]}</span></td>'
        f'<td class="num">{esc(r["verint_seats"])}</td><td>{esc(r["flags"].split(";")[0].replace("CHECK near-name: ", ""))}</td></tr>'
        for r in checks)

    ext_ok = [r for r in ext if not r["flags"].startswith("HOLD")][:25]
    ext_rows = "\n".join(
        f'<tr><td class="who">{esc(r["account"])}</td><td class="num">{esc(r["verint_seats"])}</td><td class="num">{esc(r["dpa_seats"])}</td>'
        f'<td class="st">{esc(r["wfm_in_footprint"])}</td><td class="rs">{esc(r["reseller_of_record"])}</td><td class="fl">{esc(r["flags"])}</td></tr>'
        for r in ext_ok)

    bucket_cards = "\n".join(
        f'<div class="card rv" style="--i:{i}"><span class="tag {"now" if b == "operational_visualizer" else "go" if b != "verint_no_dpa" else "hold"}">{counts[b]} account{"s" if counts[b] != 1 else ""}</span>'
        f'<h4>{BUCKET_LABEL[b][0]}</h4><p>{BUCKET_LABEL[b][1]}</p></div>'
        for i, b in enumerate(ORDER))

    page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>3xG List Review</title>
<!--FONTS-->
<style>
.bk{{display:inline-block;font-family:var(--ff-mono);font-size:10px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;padding:3px 8px;border-radius:6px;white-space:nowrap}}
.bk.operational_visualizer{{background:#FDECD9;color:var(--orange-600)}}
.bk.backoffice_deployment{{background:var(--tint);color:var(--green-600)}}
.bk.dpa_deployed{{background:var(--tint-soft);color:var(--green-600)}}
.bk.verint_no_dpa{{background:var(--zebra);color:var(--ink-3);border:1px solid var(--line)}}
.who small{{display:block;font-weight:400;color:var(--ink-3);font-size:12px;margin-top:2px}}
td.num{{font-variant-numeric:tabular-nums;white-space:nowrap;text-align:right;padding-right:14px !important}}
th.num{{text-align:right;padding-right:14px}}
#cands{{font-size:13.5px;table-layout:fixed;width:100%}}
#cands th:nth-child(1){{width:30px}}#cands th:nth-child(2){{width:auto}}#cands th:nth-child(3){{width:196px}}#cands th:nth-child(4){{width:126px}}#cands th:nth-child(5){{width:70px}}#cands th:nth-child(6){{width:62px}}#cands th:nth-child(7){{width:44px}}#cands th:nth-child(8){{width:42px}}#cands th:nth-child(9){{width:120px}}
#cands td{{padding:10px 10px 10px 0}}
td.rs{{font-size:12px;color:var(--ink-3);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
td.who .nt{{margin-top:4px}} td.who .nt .pill{{margin:0 4px 3px 0}}
td.fl .pill{{margin:0 4px 4px 0}}
td.pick{{white-space:nowrap}}
td.pick button{{font-family:var(--ff-mono);font-size:9.5px;letter-spacing:.08em;text-transform:uppercase;font-weight:600;padding:5px 8px;border-radius:5px;border:1px solid var(--line);background:#fff;color:var(--ink-2);cursor:pointer;margin-right:3px}}
td.pick button:hover{{border-color:var(--green-600);color:var(--green-600)}}
tr.cand.cohort td{{background:var(--tint-soft)}}
tr.cand.holdout td{{background:#FDECD9}}
tr.cand.skip td{{opacity:.45}}
tr.cand.cohort button[data-p=cohort],tr.cand.holdout button[data-p=holdout]{{background:var(--forest);color:#fff;border-color:var(--forest)}}
tr.cand.skip button[data-p=skip]{{background:var(--ink-3);color:#fff;border-color:var(--ink-3)}}
tr.cand.hidden{{display:none}}
.bar{{position:sticky;top:0;z-index:20;background:var(--bg);border-bottom:1px solid var(--line);padding:12px 0}}
.bar .wrap{{display:flex;gap:10px;align-items:center;flex-wrap:wrap}}
.bar .f{{font-family:var(--ff-mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;font-weight:600;padding:7px 12px;border-radius:6px;border:1px solid var(--line);background:#fff;color:var(--ink-2);cursor:pointer}}
.bar .f.on{{background:var(--forest);color:#fff;border-color:var(--forest)}}
.bar .sp{{flex:1}}
.bar .cnt{{font-family:var(--ff-mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-2)}}
.bar .cnt b{{color:var(--green-600);font-size:14px}}
.bar .cnt b.h{{color:var(--orange-600)}}
.bar .btn{{padding:8px 14px;font-size:12px}}
.bar .btn.ghost{{margin-left:4px}}
.q{{list-style:none;margin-top:16px;border-top:1px solid var(--line)}}
.q li{{display:grid;grid-template-columns:34px 1fr 1.2fr;gap:16px;padding:14px 0;border-bottom:1px solid var(--line);align-items:start}}
.q li .n{{width:30px;height:30px;border-radius:6px;background:var(--forest);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:14px}}
.q li .t{{font-weight:700;color:var(--ink);font-size:15.5px}}
.q li .t small{{display:block;font-weight:400;color:var(--ink-2);font-size:13.5px;margin-top:3px;line-height:1.45}}
.q textarea{{width:100%;min-height:52px;font-family:var(--ff);font-size:14px;color:var(--ink);padding:8px 10px;border:1px solid rgba(0,0,0,.18);border-radius:6px;background:#fff;resize:vertical}}
.q textarea:focus{{outline:2px solid var(--green-300);outline-offset:1px;border-color:var(--green)}}
details{{margin-top:16px}}
summary{{cursor:pointer;font-weight:700;color:var(--ink);font-size:15px}}
.toast{{position:fixed;left:50%;bottom:28px;transform:translateX(-50%) translateY(20px);background:var(--forest);color:#fff;font-family:var(--ff-mono);font-size:11px;letter-spacing:.12em;text-transform:uppercase;padding:12px 18px;border-radius:8px;opacity:0;transition:all .3s;z-index:90;pointer-events:none}}
.toast.on{{opacity:1;transform:translateX(-50%) translateY(0)}}
@media(max-width:900px){{.q li{{grid-template-columns:34px 1fr}}.q li textarea{{grid-column:2}}}}
</style>
</head>
<body>
<!--LOGO-->
<div id="prog"></div>

<div class="sheet">
<header class="hero">
  <div class="wrap">
    <svg class="logo"><use href="#ilogo"/></svg>
    <div class="eyebrow" data-h="1">GTM Engineering &middot; Partner channel &middot; 3xG list review</div>
    <h1 data-h="2">Jeremy's list, read once. <span class="spark">Pick the cohort.</span></h1>
    <p class="sub" data-h="3">The whitespace workbook from 3xG, bucketed the way you described it, with current Intradiem customers and partners held out. Mark five to ten accounts as the cohort and a matched set as the holdout; the picks copy out at the end.</p>
    <div class="hstats" data-h="4">
      <div><b><span class="hc" data-to="{len(rows)}">0</span></b><span>accounts on the partner sheet</span></div>
      <div><b><span class="hc" data-to="{len(ranked)}">0</span></b><span>workable after the customer and partner gate</span></div>
      <div><b><span class="hc" data-to="{counts['operational_visualizer'] + counts['backoffice_deployment']}">0</span></b><span>with a Verint back-office deployment</span></div>
      <div><b><span class="hc" data-to="{len(held)}">0</span></b><span>held for the account manager</span></div>
    </div>
    <div class="meta" data-h="5">
      <div><span>For</span>Frank Ciccone</div>
      <div><span>Source</span>3xG workbook, forwarded Aug 31</div>
      <div><span>By</span>Dallas Andrews, GTM Engineering</div>
      <div><span>Today</span>Cohort, holdout, four questions</div>
    </div>
  </div>
</header>

<section>
  <div class="wrap">
    <div class="tldr">
      <div class="k">How the list was read</div>
      <ul>
        <li><b>Two sheets.</b> The partner-only sheet (74 accounts sold through a Verint reseller, plus 9 Verint-direct back-office deployments) is the universe. The 1,297-row matrix was used only to see whether WFM is in the footprint.</li>
        <li><b>What was stripped.</b> Every dollar column, list price, total and per-module license count stayed in the intake. Only account, bucket, seats, desktop-analytics seats, model, WFM yes/no and the reseller of record are on this screen.</li>
        <li><b>The gate.</b> Every account was checked against Salesforce (Customer or Partner) and the customer lists. Matches are held, listed at the bottom, and go through the account manager if anyone wants them worked.</li>
      </ul>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="eyebrow">Buckets</div>
    <h2>Four kinds of account on the list.</h2>
    <div class="grid c4">
      {bucket_cards}
    </div>
  </div>
</section>

<div class="bar" id="bar">
  <div class="wrap">
    <button class="f on" data-f="all">All</button>
    <button class="f" data-f="operational_visualizer">Op. visualizer</button>
    <button class="f" data-f="backoffice_deployment">Back office</button>
    <button class="f" data-f="dpa_deployed">Desktop analytics</button>
    <button class="f" data-f="verint_no_dpa">No DPA</button>
    <span class="sp"></span>
    <span class="cnt">Cohort <b id="nC">0</b> &nbsp; Holdout <b class="h" id="nH">0</b> &nbsp; Skip <b style="color:var(--ink-3)" id="nS">0</b></span>
    <button class="btn" id="copyBtn" type="button">Copy picks</button>
    <button class="btn ghost" id="clearBtn" type="button">Clear</button>
  </div>
</div>

<section>
  <div class="wrap">
    <div class="eyebrow">Candidates</div>
    <h2>{len(ranked)} accounts, ranked. Pick on the row.</h2>
    <p class="lede">Rank is bucket first, then seats, then the vertical alignment as Jeremy scored it, then WFM in the footprint. Seats are Verint's max license count; the desktop-analytics column is seats with DPA today.</p>
    <div class="tablewrap">
      <table id="cands">
        <thead><tr><th>#</th><th>Account</th><th>Pick</th><th>Bucket</th><th class="num">Seats</th><th class="num">DPA</th><th>WFM</th><th>Vert</th><th>Reseller</th></tr></thead>
        <tbody>
{table}
        </tbody>
      </table>
    </div>
    <div class="callout">
      <h4>Reseller of record is not 3xG</h4>
      <p>The reseller column is who sold Verint (Avaya, ConvergeOne, Cisco, AWS and others, several of them Intradiem partners too). 3xG is the consulting partner. Outreach names 3xG only where Jeremy agrees; the reseller is never named.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="eyebrow">Held</div>
    <h2>{len(held)} held for the account manager, {len(checks)} to confirm.</h2>
    <p class="lede">Held accounts matched Salesforce as a customer or a partner. Brand matches (Farmers Group to Farmers Insurance, PNC Bank to PNC Financial) are held until the account manager says otherwise. Near-names stay ranked but carry a note.</p>
    <div class="tablewrap">
      <table>
        <thead><tr><th>Account</th><th>Bucket</th><th class="num">Seats</th><th>Why</th></tr></thead>
        <tbody>
{held_rows}
{check_rows}
        </tbody>
      </table>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="eyebrow">To settle today</div>
    <h2>Four questions, then it's build.</h2>
    <ul class="q">
      <li><span class="n">1</span><div class="t">Vertical alignment scale<small>Jeremy scored accounts 1, 2, 3. If 1 means strongest fit to our six verticals, the ranking keeps it; if not, it comes out.</small></div><textarea data-q="q1" placeholder="Answer"></textarea></li>
      <li><span class="n">2</span><div class="t">Verint-direct accounts<small>Ally, Maximus, AIG, Intuit, Citibank were sold direct or through TTEC, not partner-registered. In play for a 3xG motion, and who makes the intro?</small></div><textarea data-q="q2" placeholder="Answer"></textarea></li>
      <li><span class="n">3</span><div class="t">Naming 3xG<small>Which accounts can carry 3xG's name in the first touch, and who at 3xG is the sponsor we can reference.</small></div><textarea data-q="q3" placeholder="Answer"></textarea></li>
      <li><span class="n">4</span><div class="t">Salesforce access<small>Read access to the pre-pipeline report and the Automated Health Systems record, so the day-45 read comes from the stage fields.</small></div><textarea data-q="q4" placeholder="Answer"></textarea></li>
    </ul>
    <div class="gate">
      <h4>After the call</h4>
      <p>Sep 2 to 4: buying committees sourced and briefings written for the cohort, customer-exclusion gate on every name, sequences drafted for Frank's review the week of Sep 7. The holdout stays on the current process for the same 45 days.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="eyebrow">If the cohort needs more choice</div>
    <h2>Extended pool from the matrix sheet.</h2>
    <p class="lede">Accounts with 500+ Verint seats and WFM or desktop analytics in place that are not on the partner sheet. {len(ext)} in total; the first {len(ext_ok)} not held are below. Not partner-registered, so each needs a path in.</p>
    <details>
      <summary>Show the extended pool</summary>
      <div class="tablewrap">
        <table>
          <thead><tr><th>Account</th><th class="num">Seats</th><th class="num">DPA seats</th><th>WFM</th><th>Bill-to</th><th>Notes</th></tr></thead>
          <tbody>
{ext_rows}
          </tbody>
        </table>
      </div>
    </details>
  </div>
</section>

<footer class="foot">
  <svg class="logo"><use href="#ilogo"/></svg>
  <span>Internal. GTM Engineering &middot; Partner channel &middot; 3xG list review</span>
  <span>Built {stamp} from the intake run &middot; local file, not published &middot; 3xG data, do not forward</span>
</footer>
</div>

<div class="toast" id="toast">Copied</div>
<!--PRESENT-->
<script>
(function(){{
  var KEY='3xg-list-review-sep1';
  var state={{}};
  try{{ state=JSON.parse(localStorage.getItem(KEY)||'{{}}')||{{}}; }}catch(e){{ state={{}}; }}
  var rows=[].slice.call(document.querySelectorAll('tr.cand'));
  function save(){{ try{{ localStorage.setItem(KEY,JSON.stringify(state)); }}catch(e){{}} }}
  function paint(){{
    var c=0,h=0,s=0;
    rows.forEach(function(tr){{
      var p=state[tr.dataset.id]||'';
      tr.classList.remove('cohort','holdout','skip');
      if(p){{ tr.classList.add(p); }}
      if(p==='cohort')c++; else if(p==='holdout')h++; else if(p==='skip')s++;
    }});
    document.getElementById('nC').textContent=c; document.getElementById('nH').textContent=h; document.getElementById('nS').textContent=s;
  }}
  rows.forEach(function(tr){{
    tr.querySelectorAll('td.pick button').forEach(function(b){{
      b.addEventListener('click',function(){{
        var id=tr.dataset.id, p=b.dataset.p;
        state[id]=(state[id]===p)?'':p; save(); paint();
      }});
    }});
  }});
  document.querySelectorAll('.bar .f').forEach(function(f){{
    f.addEventListener('click',function(){{
      document.querySelectorAll('.bar .f').forEach(function(x){{x.classList.remove('on');}}); f.classList.add('on');
      var v=f.dataset.f; rows.forEach(function(tr){{ tr.classList.toggle('hidden', v!=='all' && tr.dataset.b!==v); }});
    }});
  }});
  document.querySelectorAll('.q textarea').forEach(function(t){{
    t.value=state['_'+t.dataset.q]||'';
    t.addEventListener('input',function(){{ state['_'+t.dataset.q]=t.value; save(); }});
  }});
  function toast(m){{ var t=document.getElementById('toast'); t.textContent=m; t.classList.add('on'); setTimeout(function(){{t.classList.remove('on');}},1600); }}
  document.getElementById('copyBtn').addEventListener('click',function(){{
    var out=['3xG list review, '+new Date().toLocaleDateString(),''];
    ['cohort','holdout','skip'].forEach(function(p){{
      var names=rows.filter(function(tr){{return state[tr.dataset.id]===p;}}).map(function(tr){{return '- '+tr.dataset.name;}});
      if(names.length){{ out.push(p.charAt(0).toUpperCase()+p.slice(1)+' ('+names.length+')'); out=out.concat(names); out.push(''); }}
    }});
    var qs=[['q1','Vertical alignment'],['q2','Verint-direct accounts'],['q3','Naming 3xG'],['q4','Salesforce access']];
    qs.forEach(function(q){{ var v=state['_'+q[0]]; if(v){{ out.push(q[1]+': '+v); }} }});
    var txt=out.join('\\n');
    if(navigator.clipboard&&navigator.clipboard.writeText){{ navigator.clipboard.writeText(txt).then(function(){{toast('Copied');}},function(){{prompt('Copy:',txt);}}); }} else {{ prompt('Copy:',txt); }}
  }});
  document.getElementById('clearBtn').addEventListener('click',function(){{ if(confirm('Clear all picks and answers?')){{ state={{}}; save(); paint(); document.querySelectorAll('.q textarea').forEach(function(t){{t.value='';}}); }} }});
  paint();
}})();
</script>
</body>
</html>
'''
    out = HERE / "List_Review_Frank_Sep1.src.html"
    out.write_text(page)
    print(f"wrote {out.name}: {len(ranked)} ranked, {len(held)} held, {len(checks)} check, {len(ext_ok)} extended shown")


if __name__ == "__main__":
    main()
