"""
Computes CAGR, volatility, max drawdown, beta, alpha, Sharpe, Sortino, Calmar,
correlation, and up/down capture ratios for each Multi Asset Allocation fund
against the NIFTY 50 Total Return Index (TRI), reusing the exact same engine
as baf_risk_stats.py (the math doesn't care what the fund's underlying
strategy is).

Only six funds are covered here -- see the FUNDS dict below and
docs_src/concepts/multi-asset-funds.rst for why: these are the only Multi
Asset Allocation funds with NAV history back to the 2013 Direct-plan era.
The category has ~20 more funds, almost all launched 2022-2024, too short
a history for this kind of comparison.

Usage:
    .venv/bin/python multiasset_risk_stats.py
"""

import sys
from pathlib import Path

from baf_risk_stats import RF_ANNUAL, WINDOWS as _  # noqa: F401 (re-exported for convenience)
from baf_risk_stats import compute

ROOT = Path(__file__).parent

FUNDS = {
    "HDFC Multi Asset Allocation Fund": ROOT / "data/multiasset/hdfc_multi_asset_allocation_fund.csv",
    "Axis Multi Asset Allocation Fund": ROOT / "data/multiasset/axis_multi_asset_allocation_fund.csv",
    "ICICI Prudential Multi Asset Allocation Fund": ROOT / "data/multiasset/icici_prudential_multi_asset_allocation_fund.csv",
    "UTI Multi Asset Allocation Fund": ROOT / "data/multiasset/uti_multi_asset_allocation_fund.csv",
    "Quant Multi Asset Allocation Fund": ROOT / "data/multiasset/quant_multi_asset_allocation_fund.csv",
    "SBI Multi Asset Allocation Fund": ROOT / "data/multiasset/sbi_multi_asset_allocation_fund.csv",
}

# All six launched their Direct plan within the Jan-Mar 2013 window; SBI (19 Mar
# 2013) is the latest, so that's the common start for an apples-to-apples window.
WINDOWS = [("2013-03-19", FUNDS)]


def main():
    for start_date, funds in WINDOWS:
        bench_stats, rows = compute(start_date, funds)
        print(
            f"\n=== from {start_date} ({bench_stats['years']:.1f}y) ===  "
            f"(Rf={RF_ANNUAL * 100:.1f}% flat assumption)"
        )
        print(
            f"NIFTY 50 TRI: CAGR {bench_stats['cagr']:.2f}%  "
            f"vol {bench_stats['vol']:.2f}%  maxDD {bench_stats['maxdd']:.2f}%"
        )
        header = (
            f"{'Fund':46s} {'Beta':>6s} {'Alpha':>7s} {'Corr':>6s} {'Sharpe':>7s} "
            f"{'Sortino':>8s} {'Calmar':>7s} {'UpCap':>7s} {'DownCap':>8s}"
        )
        print(header)
        for r in rows:
            print(
                f"{r['name'][:46]:46s} {r['beta']:6.2f} {r['alpha']:6.2f}% {r['corr']:6.2f} "
                f"{r['sharpe']:7.2f} {r['sortino']:8.2f} {r['calmar']:7.2f} "
                f"{r['upcap']:6.1f}% {r['downcap']:7.1f}%"
            )


if __name__ == "__main__":
    sys.exit(main())
