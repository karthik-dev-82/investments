Drawdown
=========

The simple explanation
-----------------------

Drawdown answers one question: **"How far below its all-time high is the
index right now?"** It's always zero or negative — it can only improve back
to 0% (a new all-time high) or get worse.

.. code-block:: text

   running_peak[i] = max(close[0..i])
   drawdown[i]     = (close[i] / running_peak[i] − 1) × 100

Every day, the formula looks back over the *entire history so far*, finds
the highest close ever reached up to that point, and expresses today's close
as a percentage below it. This is sometimes called an "underwater curve" —
you're below the surface (0%) any time you're not at a fresh high.

Worked example: the 2020 crash
--------------------------------

The NIFTY 50 TRI peaked at **17,349.12** on **14 January 2020**, then fell to
**10,710.41** by **23 March 2020** as COVID-19 lockdowns hit — a drawdown of
**−38.3%** in about ten weeks. The index didn't reclaim its prior peak until
**6 November 2020**, 228 days after the trough. That 228-day gap is the
**recovery time**, a number drawdown makes visible that a simple return
chart does not. (The deepest fall in the Terminal's data is the 2008 financial
crisis: **−59.5%** from 8 January to 27 October 2008.)

Why it matters
---------------

- Drawdown is the closest thing to a **behavioral risk gauge**: it's the
  number that answers "how much of my money would I have watched
  disappear, and for how long, if I'd been invested through the worst
  stretch?" Volatility (:doc:`volatility`) tells you how bumpy the ride is
  day-to-day; drawdown tells you how bad the worst single fall actually got.
- Two indices can have similar volatility but very different maximum
  drawdowns, if one tends to have sharper, deeper crashes.
- Recovery time matters as much as depth: a −20% drawdown that recovers in
  three months is a very different experience from one that takes three
  years.

How to read it on the chart
-----------------------------

The Drawdown tab pins the top of the y-axis at 0% (an all-time high) and
plots how far under each index currently sits. Zoom into any crash period —
2008, 2011, 2020 — to compare how deep and how long each index's decline
was relative to the others. The stat tiles show each index's **current**
drawdown and the date its last peak was set, regardless of zoom.
