"""
Computes beta, alpha, Sharpe, Sortino, Calmar, correlation, and up/down
capture ratios for each Balanced Advantage Fund against NIFTY 50, over the
two common windows used in docs_src/concepts/lumpsum-and-balanced-advantage.rst
(2013-2026 for the four longest-running funds, 2021-2026 for all five,
since SBI Balanced Advantage Fund only has NAV history from Sep 2021).

Beta/alpha/Sharpe/Sortino/correlation use daily returns; up/down capture
uses monthly returns (the standard convention -- compounding daily returns
over a subset of days distorts the ratio at this many data points).

Rf is a flat 6.5% annualized assumption, not the actual historical T-bill
path -- treat absolute Sharpe/Sortino/alpha values as approximate and the
ranking between funds as the more reliable signal.

Usage:
    .venv/bin/python baf_risk_stats.py
"""

import csv
import math
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
RF_ANNUAL = 0.065
RF_DAILY = (1 + RF_ANNUAL) ** (1 / 252) - 1

FUNDS_2013 = {
    "HDFC BAF": ROOT / "data/baf/hdfc_balanced_advantage_fund.csv",
    "ICICI Pru BAF": ROOT / "data/baf/icici_prudential_balanced_advantage_fund.csv",
    "Edelweiss BAF": ROOT / "data/baf/edelweiss_balanced_advantage_fund.csv",
    "Nippon India BAF": ROOT / "data/baf/nippon_india_balanced_advantage_fund.csv",
}
FUNDS_2021 = dict(FUNDS_2013, **{"SBI BAF": ROOT / "data/baf/sbi_balanced_advantage_fund.csv"})
BENCH_PATH = ROOT / "data/indices/nifty_50.csv"


def load(path):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    rows.sort(key=lambda r: r["Date"])
    return {r["Date"]: float(r["Close"]) for r in rows}


def to_returns(series, dates):
    vals = [series[d] for d in dates]
    return [vals[i] / vals[i - 1] - 1 for i in range(1, len(vals))]


def max_drawdown(dates, series):
    peak, worst = -float("inf"), 0.0
    for d in dates:
        c = series[d]
        peak = max(peak, c)
        worst = min(worst, c / peak - 1)
    return worst


def cagr(dates, series):
    d0, d1 = dates[0], dates[-1]
    y0, y1 = date(*map(int, d0.split("-"))), date(*map(int, d1.split("-")))
    years = (y1 - y0).days / 365.25
    return (series[d1] / series[d0]) ** (1 / years) - 1, years


def ann_vol(rets):
    n = len(rets)
    mean = sum(rets) / n
    return math.sqrt(sum((r - mean) ** 2 for r in rets) / n) * math.sqrt(252)


def ann_downside_dev(rets):
    n = len(rets)
    downs = [min(0, r) for r in rets]
    return math.sqrt(sum(d * d for d in downs) / n) * math.sqrt(252)


def beta_alpha(fund_rets, bench_rets):
    n = len(fund_rets)
    mf, mb = sum(fund_rets) / n, sum(bench_rets) / n
    cov = sum((fund_rets[i] - mf) * (bench_rets[i] - mb) for i in range(n)) / n
    var_b = sum((b - mb) ** 2 for b in bench_rets) / n
    beta = cov / var_b
    alpha_daily = (mf - RF_DAILY) - beta * (mb - RF_DAILY)
    return beta, alpha_daily * 252


def correlation(fund_rets, bench_rets):
    n = len(fund_rets)
    mf, mb = sum(fund_rets) / n, sum(bench_rets) / n
    cov = sum((fund_rets[i] - mf) * (bench_rets[i] - mb) for i in range(n)) / n
    sf = math.sqrt(sum((r - mf) ** 2 for r in fund_rets) / n)
    sb = math.sqrt(sum((r - mb) ** 2 for r in bench_rets) / n)
    return cov / (sf * sb)


def month_end_series(series, dates_sorted):
    out = {}
    for d in dates_sorted:
        out[d[:7]] = d
    return [series[d] for _, d in sorted(out.items())]


def monthly_returns(series, dates_sorted):
    vals = month_end_series(series, dates_sorted)
    return [vals[i] / vals[i - 1] - 1 for i in range(1, len(vals))]


def capture_ratios(fund_m, bench_m):
    up_f = up_b = down_f = down_b = 1.0
    for f, b in zip(fund_m, bench_m):
        if b > 0:
            up_f *= 1 + f
            up_b *= 1 + b
        elif b < 0:
            down_f *= 1 + f
            down_b *= 1 + b
    return (up_f - 1) / (up_b - 1) * 100, (down_f - 1) / (down_b - 1) * 100


def analyze(label, start_date, fund_paths):
    bench = load(BENCH_PATH)
    bench_dates = sorted(d for d in bench if d >= start_date)
    print(f"\n=== {label} ===  (Rf={RF_ANNUAL * 100:.1f}% flat assumption)")
    header = f"{'Fund':22s} {'Beta':>6s} {'Alpha':>7s} {'Corr':>6s} {'Sharpe':>7s} {'Sortino':>8s} {'Calmar':>7s} {'UpCap':>7s} {'DownCap':>8s}"
    print(header)
    for name, path in fund_paths.items():
        fund = load(path)
        dates = sorted(set(bench_dates) & set(fund.keys()))
        f_rets, b_rets = to_returns(fund, dates), to_returns(bench, dates)
        f_cagr, _ = cagr(dates, fund)
        vol = ann_vol(f_rets)
        dd = max_drawdown(dates, fund)
        downside = ann_downside_dev(f_rets)
        beta, alpha = beta_alpha(f_rets, b_rets)
        corr = correlation(f_rets, b_rets)
        sharpe = (f_cagr - RF_ANNUAL) / vol
        sortino = (f_cagr - RF_ANNUAL) / downside if downside > 0 else float("nan")
        calmar = f_cagr / abs(dd) if dd < 0 else float("nan")
        f_m, b_m = monthly_returns(fund, dates), monthly_returns(bench, dates)
        n = min(len(f_m), len(b_m))
        up_cap, down_cap = capture_ratios(f_m[-n:], b_m[-n:])
        print(
            f"{name:22s} {beta:6.2f} {alpha * 100:6.2f}% {corr:6.2f} {sharpe:7.2f} "
            f"{sortino:8.2f} {calmar:7.2f} {up_cap:6.1f}% {down_cap:7.1f}%"
        )


def main():
    analyze("2013-2026 (13.6y)", "2013-01-22", FUNDS_2013)
    analyze("2021-2026 (5.0y)", "2021-09-07", FUNDS_2021)


if __name__ == "__main__":
    main()
