NIFTY Index Terminal — Notes
============================

Reference notes for the metrics shown in the `NIFTY Index Terminal
<../index.html>`_ — what each chart measures, the formula behind it, and
how to read it without getting misled. Every worked example below uses the
real NIFTY 50 Total Return Index series, not placeholder numbers.

.. list-table::
   :header-rows: 1
   :widths: 22 45 33

   * - Concept
     - What it measures
     - Key terms
   * - :doc:`concepts/index-levels`
     - Raw level vs. "Growth of ₹100", and why total return
     - rebasing, log scale, TRI
   * - :doc:`concepts/base-dates`
     - Where each TRI series starts, and what's back-tested
     - launch date, base date, back-tested history
   * - :doc:`concepts/drawdown`
     - Fall from the last all-time high
     - running peak, recovery time
   * - :doc:`concepts/rolling-returns`
     - Annualized return over a trailing N years
     - CAGR, sequence-of-returns risk
   * - :doc:`concepts/volatility`
     - How much daily returns swing, annualized
     - std. deviation, √252
   * - :doc:`concepts/calendar-returns`
     - Simple year-by-year return
     - YTD, partial year
   * - :doc:`concepts/choosing-a-fund`
     - Which actual fund to buy, and why
     - Direct, Growth, lock-in, NRO→NRE
   * - :doc:`concepts/lumpsum-and-balanced-advantage`
     - A lump sum's timing risk, and funds built to manage it
     - sequence-of-returns risk, dynamic asset allocation
   * - :doc:`concepts/risk-adjusted-metrics`
     - Beta, alpha, Sharpe/Sortino, Calmar, capture ratios — and what's good or bad
     - risk-adjusted return, capture spread
   * - :doc:`concepts/multi-asset-funds`
     - Equity + debt + gold funds, and how they compare to NIFTY 50 and BAFs
     - multi asset allocation, gold

.. toctree::
   :maxdepth: 2
   :hidden:

   concepts/index-levels
   concepts/base-dates
   concepts/drawdown
   concepts/rolling-returns
   concepts/volatility
   concepts/calendar-returns
   concepts/choosing-a-fund
   concepts/lumpsum-and-balanced-advantage
   concepts/risk-adjusted-metrics
   concepts/multi-asset-funds
