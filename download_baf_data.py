"""
Download full historical daily NAV data for a curated set of large,
long-running Balanced Advantage / Dynamic Asset Allocation funds
(Direct Plan, Growth Option), using the free api.mfapi.in NAV history API.

These are actively managed hybrid funds, not index trackers -- they're kept
separate from data/indices/ and plotted as extra comparison series so their
drawdown/volatility can be read against the NIFTY indices, for evaluating
whether a dynamically-allocated fund cushions a lump-sum entry better than
going straight into an equity index.

Usage:
    .venv/bin/python download_baf_data.py
"""

import csv
import json
import urllib.request
from pathlib import Path

OUT_DIR = Path(__file__).parent / "data" / "baf"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# mfapi.in scheme codes for Direct Plan - Growth Option, picked for AMC size /
# category tenure. Confirmed via https://api.mfapi.in/mf/search?q=<name>.
FUNDS = {
    "HDFC Balanced Advantage Fund": 118968,
    "ICICI Prudential Balanced Advantage Fund": 120377,
    "Edelweiss Balanced Advantage Fund": 118615,
    "Nippon India Balanced Advantage Fund": 118736,
    "SBI Balanced Advantage Fund": 149134,
}


def fetch(scheme_code: int):
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    with urllib.request.urlopen(url, timeout=30) as resp:
        return json.load(resp)


def clean_rows(data):
    # mfapi returns newest-first as {"date": "DD-MM-YYYY", "nav": "123.45"}
    rows = []
    for point in data:
        d, m, y = point["date"].split("-")
        rows.append((f"{y}-{m}-{d}", float(point["nav"])))
    rows.sort(key=lambda r: r[0])
    return rows


def main():
    for name, code in FUNDS.items():
        print(f"=== {name} (scheme {code}) ===")
        payload = fetch(code)
        rows = clean_rows(payload["data"])
        fname = name.lower().replace(" ", "_") + ".csv"
        out_path = OUT_DIR / fname
        with open(out_path, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["Date", "Open", "High", "Low", "Close", "Index"])
            for d, nav in rows:
                w.writerow([d, "", "", "", nav, name])
        print(f"  Saved {len(rows)} rows -> {out_path} ({rows[0][0]} to {rows[-1][0]})")


if __name__ == "__main__":
    main()
