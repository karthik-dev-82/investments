"""
Builds the NIFTY Index Terminal dashboard from source data + template.

Reads:
  - data/indices/*.csv           (daily OHLC per index, from download_indices.py)
  - data/baf/*.csv                (daily NAV per Balanced Advantage fund, from
    download_baf_data.py -- plotted as extra comparison series, see BAF_FUNDS below)
  - data/index_funds_india.csv   (per-fund expense ratio / AUM, gathered by hand/research)
  - web/index_terminal.template.html  (the actual page: HTML/CSS/JS, with three
    placeholders — /*__DATA__*/ for index + BAF price data, /*__FUNDS_DATA__*/ for
    the index-fund comparison table, /*__BAF_STATS__*/ for the Balanced Advantage
    risk table, computed by baf_risk_stats.py)

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

import baf_risk_stats
import multiasset_risk_stats

ROOT = Path(__file__).parent
EPOCH = date(1990, 1, 1)

INDICES = {
    "NIFTY 50": ROOT / "data/indices/nifty_50_tri.csv",
    "NIFTY NEXT 50": ROOT / "data/indices/nifty_next_50_tri.csv",
    "NIFTY MIDCAP 150": ROOT / "data/indices/nifty_midcap_150_tri.csv",
}

# Actively managed Balanced Advantage / Dynamic Asset Allocation funds
# (Direct Plan, Growth Option) plotted as extra comparison series -- not
# index trackers, so they're kept out of INDICES / the Funds tab's
# TER-driven index-fund comparison, but they share the same date+close
# series shape and so plug straight into the same charts (Price, Drawdown,
# Rolling Return, Volatility, Calendar Returns) as the indices.
BAF_FUNDS = {
    "HDFC Balanced Advantage Fund": ROOT / "data/baf/hdfc_balanced_advantage_fund.csv",
    "ICICI Prudential Balanced Advantage Fund": ROOT / "data/baf/icici_prudential_balanced_advantage_fund.csv",
    "Edelweiss Balanced Advantage Fund": ROOT / "data/baf/edelweiss_balanced_advantage_fund.csv",
    "Nippon India Balanced Advantage Fund": ROOT / "data/baf/nippon_india_balanced_advantage_fund.csv",
    "SBI Balanced Advantage Fund": ROOT / "data/baf/sbi_balanced_advantage_fund.csv",
}

# Multi Asset Allocation funds -- equity + debt + a third asset (typically
# gold), a different strategy from BAF's equity+debt. Plotted as chart series
# same as BAF; see multiasset_risk_stats.py for why only these six.
MULTIASSET_FUNDS = {
    "HDFC Multi Asset Allocation Fund": ROOT / "data/multiasset/hdfc_multi_asset_allocation_fund.csv",
    "Axis Multi Asset Allocation Fund": ROOT / "data/multiasset/axis_multi_asset_allocation_fund.csv",
    "ICICI Prudential Multi Asset Allocation Fund": ROOT / "data/multiasset/icici_prudential_multi_asset_allocation_fund.csv",
    "UTI Multi Asset Allocation Fund": ROOT / "data/multiasset/uti_multi_asset_allocation_fund.csv",
    "Quant Multi Asset Allocation Fund": ROOT / "data/multiasset/quant_multi_asset_allocation_fund.csv",
    "SBI Multi Asset Allocation Fund": ROOT / "data/multiasset/sbi_multi_asset_allocation_fund.csv",
}


def build_price_series(paths):
    out = {}
    for name, path in paths.items():
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


def build_index_data():
    out = build_price_series(INDICES)
    out.update(build_price_series(BAF_FUNDS))
    out.update(build_price_series(MULTIASSET_FUNDS))
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


def build_fund_cost(csv_path):
    with open(csv_path, newline="") as f:
        return {
            r["fund_name"]: {
                "ber": float(r["ber_pct"]),
                "allin": float(r["all_in_pct"]),
                "aum": int(r["aum_cr"]),
                "asof": r["cost_as_of"],
            }
            for r in csv.DictReader(f)
        }


def build_baf_stats():
    cost = build_fund_cost(ROOT / "data/baf_funds_india.csv")

    def r(v, n):
        return None if v != v else round(v, n)  # NaN -> null

    windows = []
    for start_date, fund_paths in baf_risk_stats.WINDOWS:
        bench, rows = baf_risk_stats.compute(start_date, fund_paths)
        windows.append(
            {
                "start": bench["start"],
                "end": bench["end"],
                "years": round(bench["years"], 1),
                "bench": {"cagr": r(bench["cagr"], 2), "maxdd": r(bench["maxdd"], 2)},
                "funds": {
                    x["name"]: {
                        **cost[x["name"]],
                        "cagr": r(x["cagr"], 2),
                        "maxdd": r(x["maxdd"], 2),
                        "beta": r(x["beta"], 2),
                        "alpha": r(x["alpha"], 2),
                        "sharpe": r(x["sharpe"], 2),
                        "sortino": r(x["sortino"], 2),
                        "calmar": r(x["calmar"], 2),
                        "upcap": r(x["upcap"], 1),
                        "downcap": r(x["downcap"], 1),
                    }
                    for x in rows
                },
            }
        )
    return {"rf": baf_risk_stats.RF_ANNUAL * 100, "windows": windows, "cost": cost}


def build_multiasset_stats():
    cost = build_fund_cost(ROOT / "data/multiasset_funds_india.csv")

    def r(v, n):
        return None if v != v else round(v, n)

    windows = []
    for start_date, fund_paths in multiasset_risk_stats.WINDOWS:
        bench, rows = multiasset_risk_stats.compute(start_date, fund_paths)
        windows.append(
            {
                "start": bench["start"],
                "end": bench["end"],
                "years": round(bench["years"], 1),
                "bench": {"cagr": r(bench["cagr"], 2), "maxdd": r(bench["maxdd"], 2)},
                "funds": {
                    x["name"]: {
                        **cost[x["name"]],
                        "cagr": r(x["cagr"], 2),
                        "maxdd": r(x["maxdd"], 2),
                        "beta": r(x["beta"], 2),
                        "alpha": r(x["alpha"], 2),
                        "sharpe": r(x["sharpe"], 2),
                        "sortino": r(x["sortino"], 2),
                        "calmar": r(x["calmar"], 2),
                        "upcap": r(x["upcap"], 1),
                        "downcap": r(x["downcap"], 1),
                    }
                    for x in rows
                },
            }
        )
    return {"rf": multiasset_risk_stats.RF_ANNUAL * 100, "windows": windows, "cost": cost}


def main():
    template = (ROOT / "web/index_terminal.template.html").read_text(encoding="utf-8")

    index_json = json.dumps(build_index_data(), separators=(",", ":"))
    funds_json = json.dumps(build_funds_data(), separators=(",", ":"))

    final = template.replace("/*__DATA__*/", "window.__INDEX_DATA__ = " + index_json + ";")
    final = final.replace("/*__FUNDS_DATA__*/", funds_json)
    baf_json = json.dumps(build_baf_stats(), separators=(",", ":"))
    final = final.replace("/*__BAF_STATS__*/", baf_json)
    multiasset_json = json.dumps(build_multiasset_stats(), separators=(",", ":"))
    final = final.replace("/*__MULTIASSET_STATS__*/", multiasset_json)
    final = final.replace("/*__RF_ANNUAL__*/", str(baf_risk_stats.RF_ANNUAL))

    placeholders = ("__DATA__", "__FUNDS_DATA__", "__BAF_STATS__", "__MULTIASSET_STATS__", "__RF_ANNUAL__")
    assert not any(p in final for p in placeholders), "placeholder left unreplaced"

    (ROOT / "web/index_terminal.html").write_text(final, encoding="utf-8")
    (ROOT / "docs/index.html").write_text(final, encoding="utf-8")
    print(f"Built web/index_terminal.html and docs/index.html ({len(final):,} bytes)")


if __name__ == "__main__":
    main()
