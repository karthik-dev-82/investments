"""
Builds the NIFTY Index Terminal dashboard from source data + template.

Reads:
  - data/indices/*.csv           (daily OHLC per index, from download_indices.py)
  - data/index_funds_india.csv   (per-fund expense ratio / AUM, gathered by hand/research)
  - web/index_terminal.template.html  (the actual page: HTML/CSS/JS, with two
    placeholders — /*__DATA__*/ for index price data, /*__FUNDS_DATA__*/ for
    the funds comparison table)

Writes:
  - web/index_terminal.html   (dev copy)
  - docs/index.html           (published copy, served by GitHub Pages)

Re-run this after editing the template, or after data/*.csv changes (e.g. a
fresh download_indices.py run, or new rows in index_funds_india.csv).

The Funds tab applies the project's fund-selection rules (see
docs_src/concepts/choosing-a-fund.rst and the "project_overarching_directive"
memory) at build time, not by hand-curating a separate list:
  - Direct plan only (index_funds_india.csv only has Direct TER to begin with)
  - excludes ELSS / tax-saver variants (3-year lock-in)
  - excludes funds with no expense-ratio data at all
  - sorted by AUM descending within each index
"""

import csv
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
EPOCH = date(1990, 1, 1)

INDICES = {
    "NIFTY 50": ROOT / "data/indices/nifty_50.csv",
    "NIFTY NEXT 50": ROOT / "data/indices/nifty_next_50.csv",
    "NIFTY MIDCAP 150": ROOT / "data/indices/nifty_midcap_150.csv",
}


def build_index_data():
    out = {}
    for name, path in INDICES.items():
        with open(path, newline="") as f:
            rows = list(csv.DictReader(f))
        rows.sort(key=lambda r: r["Date"])
        days, closes = [], []
        for r in rows:
            y, m, d = (int(x) for x in r["Date"].split("-"))
            days.append((date(y, m, d) - EPOCH).days)
            closes.append(round(float(r["Close"]), 2))
        out[name] = {"d": days, "c": closes}
    return out


def is_lockin(name: str) -> bool:
    return bool(re.search(r"\belss\b|tax saver", name, re.I))


def build_funds_data():
    with open(ROOT / "data/index_funds_india.csv", newline="") as f:
        rows = list(csv.DictReader(f))

    out = {"NIFTY 50": [], "NIFTY NEXT 50": [], "NIFTY MIDCAP 150": []}
    for r in rows:
        if is_lockin(r["fund_name"]):
            continue
        if not r["direct_ter_pct"]:
            continue
        out[r["index"]].append(
            {
                "name": r["fund_name"],
                "ter": float(r["direct_ter_pct"]),
                "aum": int(r["aum_cr"]) if r["aum_cr"] else None,
                "src": "amfi" if r["amfi_scheme_name"] else "web",
            }
        )
    for cat in out:
        out[cat].sort(key=lambda x: -(x["aum"] or 0))
    return out


def main():
    template = (ROOT / "web/index_terminal.template.html").read_text(encoding="utf-8")

    index_json = json.dumps(build_index_data(), separators=(",", ":"))
    funds_json = json.dumps(build_funds_data(), separators=(",", ":"))

    final = template.replace("/*__DATA__*/", "window.__INDEX_DATA__ = " + index_json + ";")
    final = final.replace("/*__FUNDS_DATA__*/", funds_json)

    assert "__DATA__" not in final and "__FUNDS_DATA__" not in final, "placeholder left unreplaced"

    (ROOT / "web/index_terminal.html").write_text(final, encoding="utf-8")
    (ROOT / "docs/index.html").write_text(final, encoding="utf-8")
    print(f"Built web/index_terminal.html and docs/index.html ({len(final):,} bytes)")


if __name__ == "__main__":
    main()
