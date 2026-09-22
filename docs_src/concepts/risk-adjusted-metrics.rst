Risk-Adjusted Metrics: Beta, Alpha, Sharpe & Capture Ratios
================================================================

.. note::
   This page is not investment advice. The "good / bad" bands below are
   commonly used industry rules of thumb, not laws of nature — they exist to
   give a number somewhere to stand, not to replace judgment. Every number
   here is backward-looking; nothing on this page predicts what a fund does
   next.

The problem these metrics solve
------------------------------------

CAGR answers "how much did it grow?" It says nothing about *how it got
there* — a fund that returned 12% a year by holding steady, moderate
positions and one that returned 12% a year by swinging wildly between huge
gains and huge losses are not the same investment, even though their CAGR
is identical. Risk-adjusted metrics all do the same basic thing: they take a
return and divide it by, or compare it against, some measure of the risk
taken to get it — so two funds with the same return can be told apart, and
a fund's return can be judged against what its risk level should predict.

Every metric below is illustrated with real numbers from the Terminal's
Balanced Advantage fund data, against the NIFTY 50 Total Return Index (TRI)
as the benchmark — see :doc:`lumpsum-and-balanced-advantage` for the full
tables these are drawn from, and the caveats specific to that data (a flat
6.5% risk-free rate assumption, small sample, backward-looking).

Beta
------

**What it measures:** how much a fund moves *for a given move in the
benchmark* — its sensitivity to the market, not its overall riskiness.

.. code-block:: text

   Beta = Covariance(fund_returns, benchmark_returns) / Variance(benchmark_returns)

- **Beta = 1.0** — moves in step with the benchmark.
- **Beta > 1.0** — amplifies the benchmark's moves in both directions (a
  leveraged or high-beta equity fund).
- **Beta < 1.0** — dampens the benchmark's moves in both directions.
- **Beta near 0** — moves independently of the benchmark (unusual for a fund
  that holds any meaningful equity).

**Good or bad?** Beta isn't a report card — it's a dial, not a score. A high
beta isn't bad if you want full market exposure; a low beta isn't good if
you actually wanted equity-like returns. It only becomes informative
alongside what the fund is *supposed* to be: ICICI Prudential Balanced
Advantage Fund's beta of 0.42 (2021–2026) means it's taking under half the
NIFTY 50's market risk — which is the point of a Balanced Advantage Fund,
not a flaw in it. A pure NIFTY 50 index fund with a beta far from 1.0 would
be the concerning case, since that would mean it isn't tracking its own
benchmark.

Alpha
-------

**What it measures:** the return left over after Beta has explained its
share — the part of a fund's performance that isn't just "it held some
multiple of market risk."

.. code-block:: text

   Alpha = (fund_return − risk_free_rate) − Beta × (benchmark_return − risk_free_rate)

annualized, and expressed in percentage points per year.

- **Alpha > 0** — the fund beat what its own market exposure alone would
  predict. This is the closest of these metrics to "manager skill" —
  security selection, timing the equity/debt shift well, or (for a BAF
  specifically) income from the arbitrage/derivative positions many of them
  run.
- **Alpha ≈ 0** — the fund performed exactly as its beta would predict; no
  edge, no drag, beyond what market exposure explains.
- **Alpha < 0** — the fund underperformed what its beta would predict —
  costs, poor timing, or bad security selection ate into the return.

**Good or bad?** Positive is good, more positive is better — this is one of
the few metrics on this page that's unambiguously "higher is better," within
reason. The catch is persistence: alpha is measured over one historical
stretch and is not guaranteed to repeat. HDFC Balanced Advantage Fund's
+2.6%/year alpha (2013–2026) and ICICI Prudential's +2.9%/year over the same
window are both genuinely good numbers for that period; neither is a promise
about the next one.

Sharpe ratio
--------------

**What it measures:** return earned per unit of *total* volatility — the
oldest and most widely quoted risk-adjusted metric.

.. code-block:: text

   Sharpe = (fund_CAGR − risk_free_rate) / fund_annualized_volatility

**Common rule-of-thumb bands** (return per unit of volatility, annualized):

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Sharpe
     - Read as
   * - < 0
     - Underperformed the risk-free rate — taking risk for a worse-than-safe return.
   * - 0 – 1
     - Sub-par: some excess return, but not much per unit of risk taken.
   * - 1 – 2
     - Good — a widely used threshold for "acceptable" risk-adjusted return.
   * - 2 – 3
     - Very good.
   * - > 3
     - Excellent — rare over a long window; treat a very high Sharpe with
       some skepticism rather than taking it at face value.

Every Balanced Advantage fund tracked here sits in the 0.3–0.8 range across
both windows — a moderate reading, not a spectacular one, because BAFs give
up some upside to reduce volatility rather than maximizing return per unit
of risk in an unconstrained way.

**Limitation:** Sharpe penalizes upside volatility exactly as much as
downside volatility — a fund that only ever had spectacular up months would
still score lower than a boringly steady one with the same average return.
That's what Sortino fixes.

Sortino ratio
---------------

**What it measures:** the same idea as Sharpe, but only downside deviation
counts as "risk" — upside swings are excluded entirely.

.. code-block:: text

   Sortino = (fund_CAGR − risk_free_rate) / fund_annualized_downside_deviation

Because the denominator only counts bad moves, Sortino is almost always
higher than Sharpe for the same fund — HDFC Balanced Advantage Fund reads
0.49 Sharpe vs. 0.68 Sortino over 2013–2026, for example. The same bands
used for Sharpe are commonly applied to Sortino too, but because it's
measuring a narrower kind of risk, a "good" Sortino number runs a bit higher
than a "good" Sharpe number for a similar fund.

**Good or bad?** Same direction as Sharpe (higher is better), but compare
Sortino to Sortino and Sharpe to Sharpe — the two aren't on the same scale,
so a fund's 0.9 Sortino isn't directly comparable to another fund's 0.7
Sharpe.

Calmar ratio
--------------

**What it measures:** CAGR divided by the single worst drawdown actually
experienced — return per unit of the worst pain, rather than per unit of
day-to-day wobble.

.. code-block:: text

   Calmar = fund_CAGR / |fund_max_drawdown|

**Common rule-of-thumb bands:**

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Calmar
     - Read as
   * - < 1
     - Weak — the worst drawdown was large relative to the return earned.
   * - 1 – 3
     - Good — a widely used range for "acceptable to strong."
   * - > 3
     - Excellent.

This is the metric where the Balanced Advantage funds look best: several
sit above 1.0, and HDFC Balanced Advantage Fund reaches 1.45 over
2021–2026, against NIFTY 50 TRI's own Calmar of roughly 0.3–0.45 across the
two windows. It's also the metric most dominated by a single historical
event — change the worst drawdown and the whole number moves, unlike
Sharpe/Sortino which reflect the whole return distribution.

Up-capture and down-capture ratios
--------------------------------------

**What it measures:** what fraction of the benchmark's *typical* gain a fund
captured during the benchmark's up months, and what fraction of its typical
loss it captured during the benchmark's down months.

.. code-block:: text

   Up-capture   = fund's geometric-average monthly return in the benchmark's up months
                  ÷ the benchmark's geometric-average monthly return in those months
   Down-capture = the same ratio, over the benchmark's down months

- **Up-capture > 100%** — the fund gained *more* than the benchmark, on
  average, in the benchmark's good months.
- **Down-capture < 100%** — the fund lost *less* than the benchmark, on
  average, in the benchmark's bad months.

**Good or bad?** Look at the two together, not either alone — the gap
between them (sometimes called the "capture spread") is what tells you
whether a fund's risk-reduction is real or just a slower version of the same
ride. ICICI Prudential Balanced Advantage Fund's 64% up-capture and 26%
down-capture (2021–2026) is a wide, favorable spread: participating in
roughly two-thirds of the rallies while giving back only a quarter of the
falls. HDFC Balanced Advantage Fund's 92%/47% over the same window is a
narrower spread at a higher level — it captures nearly all of the upside,
but also more of the downside, than ICICI Prudential does. Neither pattern
is objectively better; they're different tradeoffs between smoothing the
ride and keeping pace with the market.

A fund with a *negative* spread — down-capture higher than up-capture —
would be a red flag: it would mean the fund participates more in the
benchmark's bad months than its good ones, the opposite of what an
actively-managed defensive fund should do.

Reading them together
------------------------

No single metric here tells the whole story, and the Terminal's own data
makes that concrete:

- **HDFC Balanced Advantage Fund** — high beta (0.82 / 0.64 across the two
  windows), high up-*and*-down capture, but also positive alpha. It behaves
  close to the market on both sides, and adds a genuine edge on top — which
  is how it ends up beating NIFTY 50 TRI outright despite being a "defensive"
  category fund. See :doc:`lumpsum-and-balanced-advantage` for the full
  numbers.
- **ICICI Prudential Balanced Advantage Fund** — low beta (0.52 / 0.42),
  a wide up/down capture spread, and volatility around half the index's.
  It doesn't need to match the index's average return to match its
  long-run outcome, because it avoids much of the volatility drag that a
  higher-volatility path pays in lost compounding.

Reading Beta, Alpha, Sharpe/Sortino, Calmar and the capture ratios side by
side, for the same fund, is what turns "the fund did well" into "the fund
did well *because* of this, and gave up *that* to do it" — which is the
actual decision a lump-sum allocation has to make.

How to read this on the Terminal
-------------------------------------

The Funds tab's Balanced Advantage risk table on the `Index Terminal
<../index.html>`_ shows Beta, Alpha, Sharpe, Sortino, Calmar, Up-cap and
Down-cap for every fund switched on in the legend, for either of the two
comparison windows — hover any column header for a one-line reminder of
what it means. This page is the longer explanation;
:doc:`lumpsum-and-balanced-advantage` is the applied discussion of what
these numbers say about deploying a lump sum.
