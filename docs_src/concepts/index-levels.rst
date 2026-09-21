Index Levels & Rebasing
========================

The simple explanation
-----------------------

An index level (e.g. "NIFTY 50 TRI = 35,577.90") is not a price you can buy —
it's a number calculated from its constituent stocks and scaled so that it
started from an arbitrary round-ish value on its starting date. Everything
after that is relative: 35,577.90 means the index is about 28x its starting
value of 1,256.38 (30 Jun 1999).

That scaling is exactly why you **cannot compare three indices by raw level**.
On the Terminal's Price tab, the NIFTY Next 50 TRI currently reads around
1,04,000 while the NIFTY 50 TRI is around 35,600 — that difference says nothing
about which index performed better. It mostly reflects that each index started
from a different value on a *different* date (see :doc:`base-dates`), so their
raw levels were never on the same footing to begin with.

Why total return, not the price index
--------------------------------------

Every index in the Terminal is a **Total Return Index (TRI)**. A price index
only counts changes in the constituent stocks' prices; a TRI also assumes every
dividend the companies pay is reinvested in the index on the day it's paid.

A Growth-option mutual fund does the equivalent: it keeps whatever dividends its
stocks pay inside the fund and lets the NAV compound. So a Growth fund's NAV is
directly comparable with a TRI, and *not* with the price index — comparing it
with the price index credits the fund with dividends the index never counted.
For NIFTY 50 the gap is about 1.4 percentage points a year (10.4% price return
vs. 11.8% total return, Jan 2013 to Sep 2026), which is enough to change a
conclusion. This is also the series SEBI requires funds to benchmark against.

The TRI used here is the *gross* one (dividends reinvested before any tax on
them); NSE also publishes a net version that deducts tax.

The fix: rebasing
------------------

"Growth of ₹100" (the other toggle on the Price tab) fixes this by picking one
common **base date** and dividing every point in every series by that series'
value on that date, then multiplying by 100:

.. code-block:: text

   rebased[i] = close[i] / close[base date] × 100

The base date is the left edge of whatever range you're viewing — or, if one of
the visible series launched later than that, the launch date of the latest one,
so that all lines can start together. The chart's hint line names the date.
Every line then crosses ₹100 on the same day, and the *shape* of each line
directly shows compounding growth from that day — a line that reaches 800 turned
every ₹100 into ₹800. This is the only fair way to eyeball which series
compounded faster over a given stretch, because the starting point is identical
for all of them.

Zoom to a different range and the base date moves with it, so the same series can
look very different in a 1-year view and a 10-year view. That is the point: the
chart always answers "what happened to ₹100 put in at the start of *this* window?"

Log scale
---------

Over a 27-year span, an index that compounds at a roughly constant annual
rate traces an ever-steepening curve on a normal ("linear") y-axis — the
early 2000s look flat next to 2020s moves that are numerically much larger but
proportionally similar. Flipping on **Log scale** makes equal *percentage*
moves take up equal vertical space, so a doubling in 2003 looks the same size
as a doubling in 2020. Use log scale whenever you're comparing growth *rates*
across eras; use linear when you want to see today's rupee-for-rupee moves at
their true size.

Why it matters
---------------

- Raw index level tells you almost nothing on its own — it's a function of
  an arbitrary base date and base value, not a measure of expense or quality.
- "Growth of ₹100" is the honest way to compare compounding across indices
  with different base dates and different inception years.
- Log scale is the honest way to compare compounding across *time*, since it
  neutralizes the visual bias toward whichever era has the largest absolute
  moves.
