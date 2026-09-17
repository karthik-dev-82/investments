Base Dates & Back-tested History
==================================

The simple explanation
-----------------------

Every NSE index has two distinct dates that are easy to conflate:

- **Launch date** — when the index actually started being calculated and
  published in real time.
- **Base date** — the date NSE Indices chose to set the index to 1,000. This
  is often *earlier* than the launch date, because once an index's
  methodology (which stocks, what weighting) is defined, NSE can apply that
  methodology backward using historical constituent prices to produce a
  continuous back-tested series — even for days before anyone was actually
  quoting the index.

The Terminal's charts default to showing the **full back-tested history**,
which is why NIFTY 50 data starts in **July 1990** even though the index
wasn't launched until **22 April 1996** (base date 3 Nov 1995).

.. list-table::
   :header-rows: 1
   :widths: 30 25 25 30

   * - Index
     - Launched
     - Base date (=1000)
     - Earliest chart data
   * - NIFTY 50
     - 22 Apr 1996
     - 3 Nov 1995
     - 3 Jul 1990
   * - NIFTY Next 50
     - 1 Jan 1997
     - 3 Nov 1996
     - 4 Nov 1996
   * - NIFTY Midcap 150
     - Apr 2016
     - 1 Apr 2005
     - 1 Apr 2005

Why it matters
---------------

- Data before an index's **launch date** is a retroactive reconstruction —
  real historical stock prices run through today's index methodology, not
  a series that was actually published and tradeable at the time. It's
  generally trustworthy as a research approximation, but it wasn't something
  you could have bought or benchmarked against in, say, 1992.
- Because each index has a different base date, their **raw levels are not
  comparable** — see :doc:`index-levels` for the fix (rebasing).
- NIFTY Midcap 150 in particular is a relatively new index construct (2016)
  wearing an older base date (2005) — its pre-2016 history is the most
  "synthetic" of the three in this Terminal, built from a stock universe
  definition that didn't formally exist yet at the time.

How to read it on the chart
-----------------------------

There's no visual marker distinguishing back-tested history from live
history on the Price tab — both are drawn identically. Treat everything
before the launch dates above as directionally informative but not as
precise as the live-quoted era.
