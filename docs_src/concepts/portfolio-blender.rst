Portfolio Blender
====================

.. note::
   This page is not investment advice. All computation happens in your
   browser — the amount and fund mix you enter are never sent anywhere.
   Past performance of any blend shown is not a guarantee of future results.

What it answers
------------------

Every other page on this site looks at one fund, or one index, at a time.
The **Portfolio** tab on the `Index Terminal <../index.html>`_ answers a
different question: if you split a lump sum across several of them — some
index, some :doc:`Balanced Advantage <lumpsum-and-balanced-advantage>`, some
:doc:`Multi Asset <multi-asset-funds>` — what did *that specific mix*
actually do?

Pick any combination of the indices and funds already on this site, give
each a weight and an amount, and it computes the blend's CAGR, max drawdown,
annualized volatility, and the same :doc:`risk-adjusted metrics
<risk-adjusted-metrics>` (Beta, Alpha, Sharpe, Sortino, Calmar, capture
ratios) used everywhere else — against NIFTY 50 TRI, with a growth chart and
a drawdown chart for the blend itself.

The method
------------

.. code-block:: text

   units_per_leg  = (amount × leg_weight) / leg_price on the common start date
   portfolio[day] = Σ  units_per_leg × leg_price[day]

- **Buy-and-hold, no rebalancing.** The split is applied once, on the common
  start date, and never adjusted afterward — each leg's unit count is fixed
  from day one. A leg that grows faster becomes a larger share of the
  portfolio over time; this is deliberate, not a simplification, matching a
  lump sum that's invested once and left alone.
- **Common start date.** A blend can only be computed from the date every
  selected leg has data — set by whichever fund in the mix launched most
  recently. Add SBI Balanced Advantage Fund (data from Sep 2021) to a blend
  with funds running since 2013, and the whole blend's history shortens to
  Sep 2021 onward. The page states the actual window used every time.
- **Weights are normalized to 100%** for the calculation regardless of what
  you enter — if your legs sum to 90% or 110%, a note says so, but the
  relative split between legs is preserved.
- Beta, Alpha, Sharpe, Sortino, Calmar and the capture ratios use the exact
  same formulas as the Funds tab (daily returns for the first five, monthly
  returns for capture, a flat 6.5% risk-free rate) — see
  :doc:`risk-adjusted-metrics` for what each one means.

Why buy-and-hold, not periodic rebalancing
-----------------------------------------------

A portfolio that's rebalanced back to its target weights every year behaves
differently from one that's never touched — rebalancing systematically sells
what went up and buys what went down, which usually (not always) helps
long-run returns. This tool models the *un-rebalanced* case on purpose,
because it matches a specific plan: invest a lump sum once, and don't
actively manage it afterward. If you intend to rebalance periodically, treat
every number here as an approximation of a somewhat different strategy.

How to read it
-----------------

- The **preset buttons** (100% Index, 50/50 Index + BAF, Equal thirds) load
  a starting mix — change any fund or weight afterward, or add/remove legs
  with **+ Add fund**.
- The **growth chart** plots the blend's ₹ value alongside what the same
  amount would have become in 100% NIFTY 50 TRI over the same window, so you
  can see whether the mix actually helped.
- The **drawdown chart** is the blend's own underwater curve — see
  :doc:`drawdown` for how to read one.
- Numbers update as you type; there's no separate "calculate" step.

What it doesn't do
----------------------

- No tax modeling — a real redemption has capital-gains consequences the
  blend doesn't account for.
- No partial or staggered deployment (e.g. an STP into equity over several
  months) — the whole amount goes in on day one, in every leg, at once.
- No allocation drift limits or bands — weights can drift arbitrarily far
  from their starting split over a long enough window, since nothing
  rebalances them back.
