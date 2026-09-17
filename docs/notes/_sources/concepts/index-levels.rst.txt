Index Levels & Rebasing
========================

The simple explanation
-----------------------

An index level (e.g. "NIFTY 50 = 23,217.60") is not a price you can buy — it's
a weighted average of its constituent stocks' prices, scaled so that on the
index's **base date** it equals a round number, usually 1,000. Everything
after that is relative: "23,217.60" means the index is about 23x its base-date
value.

That scaling is exactly why you **cannot compare three indices by raw level**.
On the Terminal's Price tab, NIFTY Next 50 currently trades around 70,000
while NIFTY 50 is around 23,000 — that difference says nothing about which
index performed better. It mostly reflects that each index was independently
re-based to 1,000 on a *different* date (see :doc:`base-dates`), so their raw
levels were never on the same footing to begin with.

The fix: rebasing
------------------

"Growth of ₹100" (the other toggle on the Price tab) fixes this by dividing
every point in a series by that series' own first value and multiplying by
100:

.. code-block:: text

   rebased[i] = close[i] / close[0] × 100

Now every line starts at the same place (₹100), and the *shape* of each line
directly shows compounding growth — a line that reaches 800 turned every ₹100
into ₹800. This is the only fair way to eyeball which index compounded faster
over a given stretch, because the starting point is identical for all three.

Log scale
---------

Over a 35-year span, an index that compounds at a roughly constant annual
rate traces an ever-steepening curve on a normal ("linear") y-axis — the
1990s look flat next to 2020s moves that are numerically much larger but
proportionally similar. Flipping on **Log scale** makes equal *percentage*
moves take up equal vertical space, so a doubling in 1995 looks the same size
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
