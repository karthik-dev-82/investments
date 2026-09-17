Rolling Returns
=================

The simple explanation
-----------------------

A single "5-year return" figure (e.g. "NIFTY 50 returned 45% over the last 5
years") only tells you about *one specific* 5-year window — the one that
happens to end today. **Rolling returns** fix that by asking the same
question on *every* trading day: "if someone had bought on this day and
held for exactly N years, what annualized return would they have earned?"
Plotting the answer for every day produces a continuous line instead of one
number.

.. code-block:: text

   lookback_days      = N years ≈ N × 365.25 days
   start_price        = close on (today − lookback_days)
   elapsed_days        = today − that start date (actual calendar days)
   rolling_return[i]  = ( close[i] / start_price ) ^ (365.25 / elapsed_days) − 1

The result is **annualized** — expressed as "% per year", not "% over the
whole period" — so a 3-year window and a 10-year window are directly
comparable numbers, even though the raw compounding happened over very
different lengths of time.

Why N = 1, 3, 5, 7, 10 years
------------------------------

The Terminal offers five lookback periods because each answers a
different practical question, and they tend to disagree with each other —
which is itself the point:

.. list-table::
   :header-rows: 1
   :widths: 12 88

   * - Window
     - What it's good for
   * - **1Y**
     - The noisiest, most reactive view. Dominated by whatever regime the
       market is in *right now* — a single bad quarter can swing it by
       double digits. Useful for "how has the last year felt," not for
       judging an index's long-run character.
   * - **3Y**
     - Short enough to still reflect a specific bull or bear phase, long
       enough to smooth out single-quarter noise. Common horizon for
       reviewing a recent SIP or lump-sum decision.
   * - **5Y**
     - A common "did this investment work out" horizon — long enough to
       usually span at least one meaningful drawdown, short enough to still
       feel personally relevant.
   * - **7Y**
     - Starts to average across more than one market cycle (a cycle from
       peak to peak has historically run roughly 5–8 years in NIFTY 50).
       Less sensitive to *when exactly* you started than 3Y or 5Y.
   * - **10Y**
     - The steadiest of the five — by this length, most single crashes and
       rallies have been averaged into the number. Closest of the five to
       a read on long-run compounding character rather than market timing.

Worked example
----------------

As of 16 Sep 2026, NIFTY 50 closed at **23,217.60**. Five years earlier, on
16 Sep 2021, it closed at **17,629.50**. That's 5.00 years apart, so:

.. code-block:: text

   (23,217.60 / 17,629.50) ^ (1/5.00) − 1 = 5.7% per year

That +5.7% is the 5Y rolling return plotted for 16 Sep 2026. The point
*immediately to its left* on the chart is the same calculation done for
15 Sep 2026 vs. 15 Sep 2021 — a different pair of dates entirely, which is
why the line moves at all even though "5 years" never changes.

Why it matters: sequence-of-returns risk
-------------------------------------------

If you only ever look at *one* trailing return (e.g. "the 10-year return as
of today"), you can't tell whether that number is typical or a fluke of
exactly when the window happens to start and end — an investor who bought
right before a crash and one who bought right after can have wildly
different 5-year outcomes from the *same* index. Rolling returns expose
this "sequence-of-returns risk" directly: a wide, choppy band of 1Y rolling
returns next to a much calmer band of 10Y rolling returns is the chart
telling you that short holding periods in that index carry much more luck
(good or bad) than long ones.

How to read it on the chart
-----------------------------

Switch the lookback with the chip row (1Y/3Y/5Y/7Y/10Y) and watch how much
the line calms down as the window lengthens — that calming is the
sequence-of-returns effect shrinking. The dashed line at 0% separates
periods where that holding length would have lost money from periods where
it wouldn't have. The stat tile shows the *latest* rolling return plus the
average rolling return across whatever range you've zoomed into.

Caveat
-------

A point on the rolling-return line only exists once enough history has
accumulated behind it — a 10Y line can't start until 10 years after an
index's first data point. That's why NIFTY Midcap 150's 10Y rolling-return
line only begins in 2015, a decade after its 2005 base date.
