"""
Download full historical daily NAV data for a curated set of large,
long-running Multi Asset Allocation funds (Direct Plan, Growth Option),
using the free api.mfapi.in NAV history API.

These are actively managed hybrid funds that hold equity, debt, and a third
asset (typically gold/silver, sometimes REITs/InvITs) -- a different mix
from a Balanced Advantage Fund's equity+debt. Kept separate from data/baf/
for the same reason: not index trackers, and each is its own strategy.

Only funds with NAV history back to the 2013 Direct-plan era are included
here; the multi-asset category is mostly much younger (2020-2024 launches)
-- see docs_src/concepts/multi-asset-funds.rst for which funds this covers
and, just as importantly, which it doesn't.

Usage:
    .venv/bin/python download_multiasset_data.py
"""

import csv
import json
import urllib.request
from pathlib import Path

OUT_DIR = Path(__file__).parent / "data" / "multiasset"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# mfapi.in scheme codes for Direct Plan - Growth Option, confirmed via
# https://api.mfapi.in/mf/search?q=<name> and cross-checked for NAV history
# reaching back to the 2013 Direct-plan era.
FUNDS = {
    "HDFC Multi Asset Allocation Fund": 119131,
    "Axis Multi Asset Allocation Fund": 120524,
    "ICICI Prudential Multi Asset Allocation Fund": 120334,
    "UTI Multi Asset Allocation Fund": 120760,
    "Quant Multi Asset Allocation Fund": 120821,
    "SBI Multi Asset Allocation Fund": 119843,
}


def fetch(scheme_code: int):
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    with urllib.request.urlopen(url, timeout=60) as resp:
        return json.load(resp)


def clean_rows(data):
    rows = []
    for point in data:
        nav = float(point["nav"])
        if nav <= 0:
            continue  # mfapi has a handful of bad zero-NAV entries (e.g. Axis, 07-04-2013, a Sunday)
        d, m, y = point["date"].split("-")
        rows.append((f"{y}-{m}-{d}", nav))
    rows.sort(key=lambda r: r[0])
    return drop_spike_reverts(rows)


def drop_spike_reverts(rows):
    """Drop an isolated point that jumps >25% from its neighbor and reverts the
    next day (a data glitch, not a real move -- a real move doesn't snap back).
    e.g. Quant Multi Asset Allocation Fund, 23-09-2014: 27.40 -> 49.66 -> 27.41."""
    out = []
    n = len(rows)
    for i, (d, v) in enumerate(rows):
        if 0 < i < n - 1:
            up = v / rows[i - 1][1] - 1
            down = rows[i + 1][1] / v - 1
            if abs(up) > 0.25 and abs(down) > 0.2 and (up > 0) != (down > 0):
                print(f"  dropping likely data glitch: {d} = {v} (neighbors {rows[i-1][1]}, {rows[i+1][1]})")
                continue
        out.append((d, v))
    return out


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
