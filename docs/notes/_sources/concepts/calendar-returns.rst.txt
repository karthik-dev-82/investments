Calendar-Year Returns
=======================

The simple explanation
-----------------------

The most intuitive way anyone actually thinks about performance: "how did
the index do in 2023?" A calendar-year return compares the index's closing
value on the last trading day of a year to its closing value on the last
trading day of the *previous* year.

.. code-block:: text

   calendar_return[year] = ( close[year-end] / close[previous year-end] − 1 ) × 100

Two edge cases are marked explicitly in the Calendar Returns table:

- **†  (partial year)** — an index's very first year of data has no "previous
  year-end" to compare against, so that year's return is measured from the
  index's first available data point instead. It's a real return, just over
  a shorter-than-12-month stretch.
- **(YTD)** — the current year is still in progress, so its return runs from
  the prior year-end through the *latest* trading day in the dataset, not a
  full year.

Worked examples
------------------

The NIFTY 50 TRI's best full calendar year in the Terminal's data (which starts
in 1999) is **2009 (+77.6%)** — the sharp rebound after the 2008 global
financial crisis. Its worst is **2008 (−51.3%)** — the crisis itself. Seeing both in the same table, one row
apart, is a useful reminder that the depth of a crash and the strength of
the recovery are often two sides of the same event.

Why it matters
---------------

- Calendar years are how most people already track investments mentally,
  how many fund fact-sheets report performance, and (loosely) how India's
  own financial year (April–March) is structured — though note the
  Terminal uses the *Jan–Dec* calendar year, not the Apr–Mar financial
  year, so figures won't line up exactly with a mutual fund factsheet's
  "FY24" return.
- A table of individual years exposes **consistency** in a way a single
  long-run CAGR cannot — an index that returned 10% every year for a decade
  and one that returned −40% then +60% can have similar 10-year CAGRs while
  being completely different experiences to hold.
- Reading down one column shows an index's full history of good and bad
  years at a glance; reading across one row compares how all three indices
  handled the *same* macro event.

How to read it on the chart
-----------------------------

Rows are sorted most-recent-first. Cell shading is proportional to the
size of the return — deeper green for stronger gains, deeper red for
larger losses — capped at ±60% so that one extreme year (like 2009's
+77.6%) doesn't wash out every other cell's shading.

Because these are total returns, they include reinvested dividends, so they
read a little higher than headline "price return" figures for the same index
— and they are the like-for-like comparison for a Growth-option fund's
calendar-year return.
