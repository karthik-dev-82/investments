Base Dates & Back-tested History
==================================

The simple explanation
-----------------------

Every NSE index has a few distinct dates that are easy to conflate:

- **Launch date** — when the index actually started being calculated and
  published in real time.
- **Base date** — the date NSE Indices chose to set the index to 1,000. This
  is often *earlier* than the launch date, because once an index's
  methodology (which stocks, what weighting) is defined, NSE can apply that
  methodology backward using historical constituent prices to produce a
  continuous back-tested series — even for days before anyone was actually
  quoting the index.

The Terminal shows each index as a **Total Return Index (TRI)** (see
:doc:`index-levels`), and a TRI series begins on its own date, which is neither
the launch date nor the price index's base date. The table shows all three.

.. list-table::
   :header-rows: 1
   :widths: 25 20 25 30

   * - Index
     - Launched
     - Price index base date (=1000)
     - TRI series starts in the Terminal
   * - NIFTY 50
     - 22 Apr 1996
     - 3 Nov 1995
     - 30 Jun 1999 (1,256.38)
   * - NIFTY Next 50
     - 1 Jan 1997
     - 3 Nov 1996
     - 8 Nov 2002 (1,360.04)
   * - NIFTY Midcap 150
     - Apr 2016
     - 1 Apr 2005
     - 1 Apr 2005 (1,000.00)

Why it matters
---------------

- Data before an index's **launch date** is a retroactive reconstruction —
  real historical stock prices run through today's index methodology, not
  a series that was actually published and tradeable at the time. It's
  generally trustworthy as a research approximation, but it wasn't something
  you could have bought or benchmarked against at the time.
- Of the three, only the **NIFTY Midcap 150 TRI** reaches back before its
  launch date: it is a relatively new index construct (2016) whose series
  starts in 2005, so its 2005–2016 stretch is built from a stock universe
  definition that didn't formally exist yet. The NIFTY 50 and NIFTY Next 50
  TRI series both begin after their launch dates.
- Because each index starts from a different value on a different date, their
  **raw levels are not comparable** — see :doc:`index-levels` for the fix
  (rebasing).

How to read it on the chart
-----------------------------

There's no visual marker distinguishing back-tested history from live
history on the Growth tab — both are drawn identically. Treat the NIFTY
Midcap 150 TRI before April 2016 as directionally informative but not as
precise as the live-quoted era.
