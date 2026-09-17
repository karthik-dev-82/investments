Volatility
===========

The simple explanation
-----------------------

Volatility measures **how much daily returns swing around**, not which
direction the index is heading. A high-volatility index isn't necessarily
a bad one — it's one whose day-to-day path is bumpier, up and down alike.
This is the one metric on the Terminal that is never "good" or "bad" by
sign, which is why its stat tiles show a plain number with no ▲/▼ arrow,
unlike every other tab.

.. code-block:: text

   daily_log_return[i] = ln( close[i] / close[i−1] )

   rolling_std         = standard deviation of the last W daily log returns
   volatility[i]        = rolling_std × √252 × 100

Two things are doing work in that formula that are worth unpacking:

**Log returns, not simple returns.** ``ln(close[i]/close[i-1])`` is used
instead of the simple ``close[i]/close[i-1] - 1`` because log returns are
symmetric and additive — a +10% day and a −10% day are not mirror images
under simple returns (going up 10% then down 10% doesn't get you back to
where you started), but they are under log returns. That symmetry is what
makes standard deviation a meaningful summary of "typical daily swing."

**The √252 annualization.** A single day's return has some standard
deviation; if daily moves were independent of each other, variance would
add up over T trading days, so standard deviation scales with the
*square root* of T. There are about 252 trading days in a year on NSE, so
multiplying the daily standard deviation by √252 rescales "how much a
single day typically moves" into "how much a full year's worth of those
moves would compound to" — putting it on the same annualized footing as
the return figures elsewhere in the Terminal.

Choosing a window
-------------------

.. list-table::
   :header-rows: 1
   :widths: 12 88

   * - Window
     - What it's good for
   * - **1M (21d)**
     - The most reactive — spikes hard around a single sharp event (a
       budget announcement, a global shock) and fades just as fast once
       that event rolls out of the trailing window.
   * - **3M (63d)**
     - A middle ground: still responsive to a changing regime within a
       quarter, but not whipsawed by any single day.
   * - **6M (126d)**
     - Smoother still; mostly reflects whether the last two quarters have
       been calm or turbulent, rather than any one event.
   * - **1Y (252d)**
     - The steadiest reading — closest to "this index's typical annual
       character" rather than its current mood. Good for comparing the
       three indices' baseline riskiness against each other.

Worked example
----------------

Using NIFTY 50's last 21 trading days as of 16 Sep 2026, the standard
deviation of daily log returns, annualized, comes out to **7.5%**. Over the
last 252 trading days (roughly the last year), it's **13.2%** — the shorter
window happened to catch a calmer recent stretch than the index's typical
year.

Why it matters
---------------

- Volatility is the standard proxy for **risk** in most portfolio theory —
  not risk of loss specifically, but of uncertainty in outcome.
- Comparing the three indices' volatility (rather than just their returns)
  is how you judge whether NIFTY Midcap 150's typically higher returns are
  compensation for genuinely bumpier ride, or a free lunch.
- A rising volatility line, even with the index flat or up, is often an
  early tell that a market regime is shifting — big up days and big down
  days both raise it.

How to read it on the chart
-----------------------------

The Volatility tab has no zero line and no directional color, by design —
higher on the chart always just means "bigger daily swings lately,"
regardless of whether those swings were up or down moves.
