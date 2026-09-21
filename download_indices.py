"""
Download full historical daily Total Return Index (TRI) levels for the NSE
indices used here (NIFTY 50, NIFTY NEXT 50, NIFTY MIDCAP 150), from the start
of each TRI series to date, using the jugaad-data library (which talks to
NSE Indices' TRI history API).

TRI, not the price index: a Growth-option fund keeps dividends inside the
fund, so the fair benchmark for one is the index with dividends reinvested.
This is the gross TRI (the API's "TotalReturnsIndex"), the series SEBI uses
for fund benchmarking; the net-of-tax "NTR_Value" is not used.

Usage:
    .venv/bin/python download_indices.py
"""

import csv
from datetime import date, datetime
from pathlib import Path

import jugaad_data.nse as nse

OUT_DIR = Path(__file__).parent / "data" / "indices"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Ask from well before any TRI series starts; the API returns what exists.
START = date(1990, 1, 1)
INDICES = ["NIFTY 50", "NIFTY NEXT 50", "NIFTY MIDCAP 150"]


def fetch_tri(index_name: str):
    raw = nse.ih.index_tri_raw(index_name, index_name, START, date.today())
    rows = {}
    for r in raw:
        d = datetime.strptime(r["Date"], "%d %b %Y").date().isoformat()
        rows[d] = float(r["TotalReturnsIndex"])
    return sorted(rows.items())


def main():
    for name in INDICES:
        print(f"=== {name} TRI ===")
        rows = fetch_tri(name)
        if not rows:
            print("  No data fetched!")
            continue
        label = f"{name} TRI"
        path = OUT_DIR / (name.lower().replace(" ", "_") + "_tri.csv")
        with open(path, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["Date", "Open", "High", "Low", "Close", "Index"])
            for d, level in rows:
                w.writerow([d, "", "", "", level, label])
        print(f"  Saved {len(rows)} rows -> {path} ({rows[0][0]} to {rows[-1][0]})")


if __name__ == "__main__":
    main()
