# GTM Impact Scorecard

One number for ELT: the opportunity this system has put on the table, the activity
behind it, and the results realized so far. It reads the outputs of both engines, so
there is nothing new to maintain.

## Run it

```bash
python3 impact_engine.py                 # print the scorecard
python3 impact_engine.py --output impact.json   # feed the dashboard Impact tab
```

## What it reads

- `../intradiem-signal-engine/data/signals.json` install-base expansion and risk signals
- `../tam-outbound-engine/data/tam_plays.json` net-new strike plans (carry the ROI)
- `./outcomes.csv` realized results you append to: `date, account, type, value, note` where type is `meeting`, `pipeline`, or `won`

## The two numbers, kept separate

**Opportunity surfaced** is estimated recoverable customer cost the system put in
front of a rep. It is large and immediate, but it is not booked revenue. Present it
as what the system found.

**Realized** (meetings, pipeline, won) comes only from `outcomes.csv` and is the
number that grows as deals move. Present it as what closed. Never blend the two.

## Where it shows

The dashboard Impact tab renders this scorecard, refreshed beside the page by the
daily run. As real activity flows into `outcomes.csv` and the engines point at real
data, the same scorecard becomes your live proof of the system's ROI.
