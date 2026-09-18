Choosing a Fund
=================

.. note::
   This page explains the filters used on the Terminal's **Funds** tab. It is not tax
   or legal advice — verify anything below with an Australian tax adviser and an
   India-side AMC/RTA before acting on it, especially the points on Growth vs. IDCW
   and NRI/OCI eligibility, both of which depend on your specific circumstances.

The simple explanation
-----------------------

Two funds tracking the same index (say, NIFTY 50) are not interchangeable products —
they differ in **plan** (Direct vs. Regular), **option** (Growth vs. IDCW), and
sometimes carry a **lock-in** most people don't notice until they try to sell. The
Funds tab filters on all three, and this page explains why each filter is there.

Direct vs. Regular
---------------------

- **Direct plan** — bought straight from the AMC (or a platform that doesn't take a
  commission), no distributor involved.
- **Regular plan** — bought through a distributor/advisor, who is paid an ongoing
  trail commission baked into the plan's expense ratio.

Same portfolio, same fund manager, same index — the *only* difference is who else is
being paid out of your returns every year. For a passively managed index fund, where
there's no manager skill to pay for in the first place, that gap is pure cost. The
Funds tab shows **Direct plan only**.

Growth vs. IDCW — and why it matters more for an Australian tax resident
----------------------------------------------------------------------------

- **Growth option** — all gains stay inside the fund; the NAV simply rises. Nothing
  is paid out until you redeem units.
- **IDCW option** (Income Distribution cum Capital Withdrawal, the renamed
  "Dividend" option) — the fund periodically pays out a distribution, reducing the
  NAV by the amount paid. Reinvesting it (buying more units with the payout) does not
  undo the fact that a distribution occurred.

For someone taxed only in India, this is a minor preference. For an **Australian tax
resident**, it's a materially different tax outcome:

- Under Growth, no income is paid out — nothing is assessable in Australia until you
  actually sell your units, at which point it's a capital gain (and, if held over 12
  months, eligible for the CGT discount).
- Under IDCW, each distribution is assessable Australian income in the year it's
  paid — including the ones you never touched because they were auto-reinvested. You'd
  owe tax on cash you didn't receive as cash.

This is why the Terminal treats **Growth option** as a hard requirement, not a
preference, for anyone in this situation. When you actually invest, double-check the
scheme you're buying is explicitly the **Growth** variant — Direct and Growth are two
independent choices on the same order form, and it's easy to select Direct/IDCW by
mistake.

Lock-in: why ELSS variants are excluded
------------------------------------------

Several AMCs sell an **ELSS Tax Saver** version of their Nifty 50 index fund — same
index, same portfolio, but wrapped in India's Section 80C tax-saving structure, which
carries a **mandatory 3-year lock-in** from the date of each purchase (each SIP
instalment locks in separately).

If you want to **control the timing of your own exit completely** — redeem some now,
redeem more later, or leave the whole position untouched for a future date you haven't
picked yet — a 3-year lock-in works against that, and the 80C tax deduction it exists
for is an India-resident income-tax benefit that doesn't obviously help an Australian
tax resident's return anyway. The Funds tab excludes every ELSS/tax-saver variant by
name, regardless of its expense ratio.

Why AUM is shown at all
-------------------------

Expense ratio is a known, fixed cost. AUM (assets under management) is a rough proxy
for two things that matter more the longer you expect to hold something and the more
likely it is to eventually be administered by someone else (a nominee, in this case a
daughter, rather than you):

- **Liquidity and continuity** — a fund with ₹25,000 Cr under management is
  overwhelmingly unlikely to be shut down or merged away; a fund with ₹20 Cr is a
  much smaller, newer bet, however cheap its expense ratio looks today.
- **Operational maturity** — a large, established AMC has run its transmission
  (the process of moving a deceased or gifting investor's units to a nominee) process
  many times before. A newer, smaller AMC may not have.

Neither of these is a reason to always pick the largest fund — but when two funds are
close on cost, size and the AMC's track record are a reasonable tie-breaker for a
holding you might not personally manage the end of.

The NRO → NRE route
----------------------

This money is **India-sourced** — not funds remitted from Australia — so under
FEMA it lands in an **NRO** (Non-Resident Ordinary) account first, not NRE. The plan
is to then transfer it into an **NRE** (Non-Resident External) account before
investing:

- **NRO** is for India-sourced income (rent, dividends, sale proceeds, and similar).
  Repatriating money *out* of India from NRO is capped at USD 1 million per financial
  year and requires a CA to certify (Form 15CA/15CB) that applicable Indian taxes
  have been settled on it.
- **NRE** is for money remitted *from abroad*. Once funds are properly transferred in
  (the NRO → NRE route is permitted, subject to the same USD 1 million/year cap and CA
  certification), they carry none of that repatriation friction going forward.

The practical upshot for fund selection: which account the investment is ultimately
made *from* (NRO-linked vs. NRE-linked folio) affects how freely the eventual proceeds
can move out of India later — relevant given the stated intent to possibly redeem, or
possibly leave the position untouched for a daughter who may not be India-resident
either. This page doesn't verify any of the current caps, certification steps, or
timelines — confirm the live rules with a FEMA-aware CA before moving the money
at all.

What this page doesn't cover
--------------------------------

- **Whether a given AMC accepts an Australia-resident NRI/OCI investor at all.** Most
  do; a handful historically restrict certain overseas jurisdictions (this has mostly
  affected US/Canada-resident investors specifically, due to FATCA compliance costs,
  not Australia) — but confirm directly with the AMC before investing, don't assume
  from this page.
- **Which index, or how much to put where.** That's an asset-allocation decision, not
  a fund-selection one — the Funds tab helps you pick the cheapest, most durable
  vehicle *once* you've decided you want NIFTY 50, Next 50, or Midcap 150 exposure at
  all.
- **Whether to put the whole lump sum into an index fund at all, on day one.** See
  :doc:`lumpsum-and-balanced-advantage` for the timing-risk angle and how Balanced
  Advantage Funds fit against the same Direct/Growth/no-lock-in rules above.
