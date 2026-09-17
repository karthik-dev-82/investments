"""
Download full historical daily OHLC data for Indian NSE indices
(NIFTY 50, NIFTY NEXT 50, NIFTY MIDCAP 150) from inception to date,
using the jugaad-data library (which talks to NSE's index history API).

Usage:
    .venv/bin/python download_indices.py
"""

import time
from datetime import date, timedelta
from pathlib import Path

import pandas as pd
import jugaad_data.nse as nse

OUT_DIR = Path(__file__).parent / "data" / "indices"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Start a bit before each index's known base/inception date so we don't
# accidentally clip early back-tested history.
INDICES = {
    "NIFTY 50": date(1990, 1, 1),
    "NIFTY NEXT 50": date(1996, 1, 1),
    "NIFTY MIDCAP 150": date(2005, 1, 1),
}

END_DATE = date.today()
CHUNK_YEARS = 3
MAX_RETRIES = 4


def daterange_chunks(start: date, end: date, years: int):
    cur = start
    while cur < end:
        nxt = min(date(cur.year + years, cur.month, cur.day), end)
        yield cur, nxt
        cur = nxt + timedelta(days=1)


def fetch_index(symbol: str, start: date, end: date) -> pd.DataFrame:
    frames = []
    for chunk_start, chunk_end in daterange_chunks(start, end, CHUNK_YEARS):
        for attempt in range(1, MAX_RETRIES + 1):
            try:
                print(f"  {symbol}: {chunk_start} -> {chunk_end} (attempt {attempt})")
                df = nse.index_df(symbol, chunk_start, chunk_end)
                frames.append(df)
                break
            except Exception as e:
                print(f"    failed: {e}")
                if attempt == MAX_RETRIES:
                    print(f"    giving up on chunk {chunk_start}-{chunk_end}")
                else:
                    time.sleep(3 * attempt)
        time.sleep(1)  # be polite between chunks
    if not frames:
        return pd.DataFrame()
    full = pd.concat(frames, ignore_index=True)
    return full


def clean(df: pd.DataFrame, symbol: str) -> pd.DataFrame:
    df = df.copy()
    df["HistoricalDate"] = pd.to_datetime(df["HistoricalDate"])
    df = df.drop_duplicates(subset="HistoricalDate").sort_values("HistoricalDate")
    df = df.rename(
        columns={
            "HistoricalDate": "Date",
            "OPEN": "Open",
            "HIGH": "High",
            "LOW": "Low",
            "CLOSE": "Close",
        }
    )
    df["Index"] = symbol
    df = df[["Date", "Open", "High", "Low", "Close", "Index"]]
    return df.reset_index(drop=True)


def main():
    for symbol, start in INDICES.items():
        print(f"\n=== {symbol} ===")
        raw = fetch_index(symbol, start, END_DATE)
        if raw.empty:
            print(f"  No data fetched for {symbol}!")
            continue
        cleaned = clean(raw, symbol)
        fname = symbol.lower().replace(" ", "_") + ".csv"
        out_path = OUT_DIR / fname
        cleaned.to_csv(out_path, index=False)
        print(
            f"  Saved {len(cleaned)} rows -> {out_path} "
            f"({cleaned['Date'].min().date()} to {cleaned['Date'].max().date()})"
        )


if __name__ == "__main__":
    main()
