Lump-Sum Timing & Balanced Advantage Funds
=============================================

.. note::
   This page is not tax or investment advice. Past performance of the funds
   named below is not a guarantee of future results — five funds over two
   historical windows is illustrative, not exhaustive, and an actively managed
   fund's future allocation calls can differ from its past ones. Verify
   current taxation treatment (see below) with an Australian tax adviser and
   an India-side AMC before acting on any of this.

The problem this page is about
----------------------------------

Every other page on this site treats money as if it arrives gradually — a
SIP, a series of contributions, dollar-cost-averaged in over years. That's
not this situation: the money referenced in :doc:`choosing-a-fund` arrives as
a **single lump sum on an unknown future date**. Whatever the market is doing
on that date is the price paid, in full, for the whole amount — there's no
averaging it out over time unless it's deliberately staggered in afterward.

That's **sequence-of-returns risk**: the same average return over ten years
can feel completely different depending on whether the first year is a crash
or a rally, simply because of *when* the money went in. A pure equity index
investment (:doc:`index-levels` onward) carries this risk fully — the
whole sum is exposed to whatever the index does from day one.

What a Balanced Advantage Fund does differently
----------------------------------------------------

A **Balanced Advantage Fund** (BAF, also called Dynamic Asset Allocation)
is an actively managed hybrid fund that shifts its own net equity exposure —
often anywhere from roughly 30% to 80% of the portfolio — up and down based
on a valuation model (P/E, P/B, or similar), rather than holding a fixed
allocation. The pitch: when equity markets are expensive, the fund
mechanically de-risks; when they're cheap, it adds equity back. For a
lump sum landing at an unpredictable moment, this is a structural answer to
sequence-of-returns risk that a pure index fund has no mechanism for at all.

This is a genuinely different instrument from everything else on this site.
NIFTY 50 / Next 50 / Midcap 150 index funds are passively managed and
low-cost because there's no manager judgment being paid for — a BAF is the
opposite: you're paying for, and depending on, a manager's allocation model.
There is no guarantee any given BAF's model continues to work as well as it
has.

What the data actually shows
--------------------------------

Five large Balanced Advantage Funds (Direct Plan, Growth Option) are tracked
here: HDFC, ICICI Prudential, Edelweiss, and Nippon India all have NAV
history back to January 2013; SBI Balanced Advantage Fund is newer, with
history only from September 2021. That split means two separate
apples-to-apples comparisons, not one table with a blank cell.

**2013–2026 (four funds, ~13.7 years)** — includes the 2013 taper-tantrum
selloff, the 2015–16 correction, and the 2020 COVID crash:

.. list-table::
   :header-rows: 1
   :widths: 30 18 18 18

   * - Fund
     - Max drawdown
     - CAGR
     - Ann. volatility
   * - NIFTY 50
     - −38.4%
     - 10.4%
     - 16.2%
   * - HDFC Balanced Advantage Fund
     - −34.2%
     - 13.6%
     - 14.5%
   * - ICICI Prudential Balanced Advantage Fund
     - −27.0%
     - 12.5%
     - 9.0%
   * - Edelweiss Balanced Advantage Fund
     - −16.2%
     - 12.1%
     - 9.0%
   * - Nippon India Balanced Advantage Fund
     - −22.8%
     - 11.9%
     - 11.3%

**2021–2026 (all five funds, 5.0 years)** — includes the 2022 rate-hike
correction and a 2026 drawdown, but no COVID-style crash:

.. list-table::
   :header-rows: 1
   :widths: 30 18 18 18

   * - Fund
     - Max drawdown
     - CAGR
     - Ann. volatility
   * - NIFTY 50
     - −17.2%
     - 6.0%
     - 13.8%
   * - HDFC Balanced Advantage Fund
     - −10.2%
     - 14.6%
     - 9.9%
   * - ICICI Prudential Balanced Advantage Fund
     - −8.2%
     - 10.7%
     - 6.4%
   * - Edelweiss Balanced Advantage Fund
     - −11.1%
     - 9.3%
     - 8.7%
   * - Nippon India Balanced Advantage Fund
     - −8.6%
     - 9.7%
     - 7.4%
   * - SBI Balanced Advantage Fund
     - −7.4%
     - 10.2%
     - 6.3%

The same pattern holds in both windows, over two periods with different
crash shapes (a five-week COVID crash vs. a slower 2022 grind and a 2026
dip): every BAF's worst drawdown was shallower than NIFTY 50's, every BAF
ran at meaningfully lower annualized volatility, and every BAF's CAGR came
out ahead of NIFTY 50's too. That last point is the one to be most skeptical
of: it's not a structural guarantee of balanced advantage funds in general,
it's what happened to these managers' models over the specific stretches
they've been live for. A slower, grinding bear market with no sharp trigger
to react to, or a straight-line bull run with no crash to sidestep, would
tell a different story — and moving out of equity ahead of a rally is
exactly the failure mode of the same de-risking mechanism that helps in a
crash.

The Drawdown tab on the `Index Terminal <../index.html>`_ has all five
funds as toggleable series (off by default, under "Balanced Advantage
(Direct, Growth)" in the legend) alongside the three NIFTY indices, using
the same underwater-curve calculation described in :doc:`drawdown` — turn
them on to see the shape of each fund's declines directly, not just the
summary numbers above. The Price, Rolling Return, Volatility, and Calendar
Returns tabs carry the same five series for the same reason.

Risk-adjusted performance: beta, alpha, Sharpe, and capture ratios
------------------------------------------------------------------------

CAGR, drawdown, and volatility describe a fund on its own. The metrics below
describe it *relative to NIFTY 50* — how much of the index's risk it's
actually taking on, and whether the return it delivers is worth that risk.
All are computed from daily NAV/index returns against a flat **6.5%
annualized risk-free rate** (a simplifying assumption standing in for the
actual historical T-bill path — treat the absolute Sharpe/Sortino/alpha
numbers as approximate, and the *ranking between funds* as the more reliable
signal, since a different Rf mostly shifts every fund's numbers together).

.. code-block:: text

   Beta        = Cov(fund_returns, NIFTY_returns) / Var(NIFTY_returns)
   Alpha       = (fund_return − Rf) − Beta × (NIFTY_return − Rf)     [annualized]
   Sharpe      = (fund_CAGR − Rf) / fund_annualized_volatility
   Sortino     = (fund_CAGR − Rf) / fund_annualized_downside_deviation
   Calmar      = fund_CAGR / |fund_max_drawdown|
   Up-capture  = fund's compounded return over NIFTY's positive months
                 ÷ NIFTY's compounded return over those same months
   Down-capture = the same ratio, over NIFTY's negative months

- **Beta** — sensitivity to NIFTY 50's moves. A beta of 0.5 means the fund
  has historically moved roughly half as much as the index, in either
  direction; it's a blend of the fund's actual net equity level and how
  that level correlates with market direction.
- **Alpha** — the annualized return left over after Beta explains its share.
  A positive alpha means the fund beat what its own market exposure alone
  would predict; this is closer to "manager skill," separate from just
  holding less equity.
- **Sharpe ratio** — return per unit of *total* volatility. Higher is
  better; it doesn't distinguish an upside swing from a downside one.
- **Sortino ratio** — the same idea, but only penalizes downside volatility.
  Usually higher than Sharpe for the same fund, since upside swings are
  excluded from the risk side entirely.
- **Calmar ratio** — CAGR divided by the worst drawdown actually
  experienced. Unlike Sharpe/Sortino, it's anchored to the single worst
  historical event rather than the whole return distribution — closest in
  spirit to "how did it do in the one moment that would have hurt the most."
- **Up-/down-capture ratio** — computed on **monthly** returns (the
  standard convention here; daily compounding of a subset of days distorts
  the ratio) — what fraction of NIFTY's gain the fund captured during the
  index's up months, and what fraction of NIFTY's loss it captured during
  down months. A fund with 50% up-capture and 30% down-capture is
  participating in half the rally but only a third of the fall — exactly
  the asymmetry a Balanced Advantage Fund is designed to produce.

**2013–2026 (four funds):**

.. list-table::
   :header-rows: 1
   :widths: 20 10 10 10 10 10 10 10 10

   * - Fund
     - Beta
     - Alpha
     - Corr.
     - Sharpe
     - Sortino
     - Calmar
     - Up-cap
     - Down-cap
   * - HDFC BAF
     - 0.82
     - 3.6%
     - 0.91
     - 0.49
     - 0.68
     - 0.40
     - 87.8%
     - 90.8%
   * - ICICI Pru BAF
     - 0.52
     - 3.5%
     - 0.94
     - 0.66
     - 0.92
     - 0.46
     - 28.7%
     - 57.9%
   * - Edelweiss BAF
     - 0.50
     - 3.2%
     - 0.91
     - 0.62
     - 0.89
     - 0.74
     - 33.4%
     - 67.3%
   * - Nippon India BAF
     - 0.62
     - 2.6%
     - 0.89
     - 0.47
     - 0.66
     - 0.52
     - 48.0%
     - 81.3%

**2021–2026 (all five funds):**

.. list-table::
   :header-rows: 1
   :widths: 20 10 10 10 10 10 10 10 10

   * - Fund
     - Beta
     - Alpha
     - Corr.
     - Sharpe
     - Sortino
     - Calmar
     - Up-cap
     - Down-cap
   * - HDFC BAF
     - 0.64
     - 7.8%
     - 0.89
     - 0.82
     - 1.14
     - 1.43
     - 82.5%
     - 47.2%
   * - ICICI Pru BAF
     - 0.42
     - 4.0%
     - 0.92
     - 0.65
     - 0.96
     - 1.29
     - 52.5%
     - 31.6%
   * - Edelweiss BAF
     - 0.59
     - 2.8%
     - 0.94
     - 0.31
     - 0.44
     - 0.83
     - 65.0%
     - 55.2%
   * - Nippon India BAF
     - 0.51
     - 3.1%
     - 0.94
     - 0.42
     - 0.59
     - 1.12
     - 58.8%
     - 45.8%
   * - SBI BAF
     - 0.42
     - 3.6%
     - 0.91
     - 0.57
     - 0.82
     - 1.37
     - 55.5%
     - 39.4%

Read across the two windows together, not just down a single column: HDFC
BAF runs the highest beta and the highest up-capture of the group *and* the
highest down-capture — it behaves the most like a lower-volatility equity
fund. ICICI Prudential and SBI sit at the other end — the lowest beta and
the widest gap between up-capture and down-capture (in 2021–2026, ICICI
Pru captured 52.5% of NIFTY's gains but only 31.6% of its losses) — the
shape a Balanced Advantage Fund is supposed to have, at the cost of giving
up more of the upside too. Neither is "the correct" answer on its own; it's
a real tradeoff between smoothing the ride and keeping pace with equity
returns, and it's visible directly in these numbers rather than needing to
be taken on faith.

How this fits the project's fund rules
-------------------------------------------

Everything in :doc:`choosing-a-fund` still applies:

- **Growth option only** — same reasoning as index funds: an IDCW payout is
  assessable Australian income the year it's paid, Growth defers it to
  redemption. All five funds above are Direct Plan, Growth Option.
- **No lock-in** — BAFs are open-ended funds, same as the index funds
  already covered; none of the five above carry a lock-in.
- **NRO → NRE route** — unchanged. Which product the money eventually buys
  doesn't change how it lands in India or how it's moved between accounts.

What's different from the index-fund comparison
------------------------------------------------------

- **Cost is not the deciding factor here.** Direct-plan TER for these five
  runs 0.46%–0.85% (source: AMFI TER disclosure, ~Jul-2025 snapshot) —
  several times a NIFTY 50 index fund's ~0.15–0.2%, because you're paying for
  active allocation decisions, not just index replication. A higher TER
  here isn't a red flag the way it would be on the Funds tab.
- **No tracking error concept applies** — there's no index being tracked, so
  the entire cost/quality tradeoff for an index fund doesn't transfer.
  Manager tenure and the fund's actual net-equity history (not shown here)
  matter more than they do for a passive fund.
- **Taxation is a genuine open question, not a settled rule.** Many BAFs
  maintain equity-oriented tax treatment by keeping *gross* equity exposure
  (including derivative/hedge positions) above the ~65% threshold even while
  their *net* equity exposure swings much lower — but the exact mechanism,
  and India's capital-gains rules for hybrid/specified funds, have changed
  more than once in recent years and should be checked against current law
  at the time of investing, not assumed from this page.

Why this isn't just "add balanced advantage funds to the Funds tab"
-------------------------------------------------------------------------

The Funds tab's whole model — Direct plan, sorted by AUM, excluding
lock-in variants — assumes every row is a substitutable way to buy exposure
to the *same* index at the lowest cost. BAFs aren't substitutes for each
other or for an index fund in that sense: each one is a distinct, actively
managed strategy with its own track record. They're deliberately kept out of
that comparison and shown instead as their own overlay series on the
analytical tabs, where their actual behavior — not just a cost figure — is
what's being compared.
