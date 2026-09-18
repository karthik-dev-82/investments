# Handover — NIFTY Index Terminal / inheritance investment plan

Paste this into a new chat to pick up where this session left off. It's also committed
at the repo root, so `git log` and the code itself stay the source of truth if this
drifts out of date.

## What this project is

An investment research tool for an **inheritance the user (an OCI, Australian tax
resident) will receive in India at some future date**. The money is India-sourced —
lands in an **NRO** account first (FEMA route for India-sourced income), gets
transferred to **NRE** before investing. Full reasoning is in the persistent project
memory (`project_overarching_directive.md`, auto-loaded every session in this working
directory) and in `docs_src/concepts/choosing-a-fund.rst`. The short version:

- **Growth option only, never IDCW/Dividend** — an IDCW distribution is assessable
  Australian income the year it's paid, even if auto-reinvested. Growth defers
  everything to actual redemption (then it's a CGT event, with the 12-month discount).
- **No lock-in, ever** — user wants to fully control exit timing (redeem some, redeem
  later, or leave it untouched for their daughter). This rules out ELSS/tax-saver
  fund variants (3-year statutory lock-in), even though some AMCs sell an
  "ELSS Tax Saver" flavor of the exact same index.
- **Direct plan only** (not Regular) — confirmed explicitly, reversing an earlier
  momentary ask mid-session.
- Nothing in this repo is tax/legal advice; that's stated everywhere it matters and
  should stay that way.

## Live site

- **Dashboard**: https://karthik-dev-82.github.io/investments/
- **Notes site**: https://karthik-dev-82.github.io/investments/notes/
- **Repo**: `git@github.com:karthik-dev-82/investments.git`, branch `main`, Pages
  serves from `main` / `/docs`.

## What's built

1. **Historical index data** (`data/indices/*.csv`) — daily OHLC for NIFTY 50 (from
   1990-07-03), NIFTY Next 50 (1996-11-04), NIFTY Midcap 150 (2005-04-01), through
   the index's base date / back-tested history. Fetched via `download_indices.py`
   (uses the `jugaad-data` PyPI package — NSE's and AMFI's own sites are unreachable
   from this environment, direct connections just time out).

2. **Fund comparison data** (`data/index_funds_india.csv`) — 113 index funds/ETFs
   across the three indices, with Direct/Regular Total Expense Ratio, AUM, and
   source. TER mostly from AMFI's actual disclosure (~Jul-2025 snapshot, reached via
   a Hugging Face mirror since AMFI's site itself is unreachable here); a handful of
   newer AMCs (JioBlackRock, Groww, etc., not yet in that snapshot) filled in from
   INDmoney instead — tagged per-row in the `direct_ter_source` column.

   **Known gaps** — 10 funds have no TER data anywhere I could find (Bajaj Finserv,
   Choice, IDBI, L&T across Nifty 50/Next 50; Baroda BNP Paribas for Midcap 150).
   Tracking error is essentially unobtainable in bulk — Value Research has it but
   blocks all automated access (403 even via fetch tools); only one fund (UTI Nifty
   50, 0.02%) was found via a lucky indexed comparison article.

3. **The dashboard** (`web/index_terminal.template.html` → built into
   `web/index_terminal.html` and `docs/index.html` by `build_dashboard.py`) — six
   tabs: Price (zoomable/pannable, raw or rebased-to-₹100, linear/log), Drawdown,
   Rolling Return (1/3/5/7/10Y), Volatility (1M/3M/6M/1Y), Calendar Returns (year ×
   index heatmap table), and **Funds** (direct-plan/growth-option funds per index,
   sorted by AUM, ELSS variants excluded, color-coded by expense ratio). Custom
   canvas charting, no chart library. Design follows the `dataviz` and
   `artifact-design` skill conventions (categorical palette, dark/light theme via CSS
   custom properties, etc.).

   **To rebuild after editing the template or the CSVs:**
   ```bash
   .venv/bin/python3 build_dashboard.py
   ```
   This regenerates both `web/index_terminal.html` (dev copy) and `docs/index.html`
   (published copy) from the template + data. The Funds tab's filtering rules
   (Direct only, exclude ELSS, sort by AUM) are applied in `build_dashboard.py` at
   build time, not hand-curated — editing `index_funds_india.csv` and re-running the
   script is enough to update the dashboard.

4. **Notes site** (`docs_src/` → Sphinx + `sphinx_rtd_theme`, built into
   `docs/notes/`) — matches the theme/structure of the user's other docs site,
   `karthik-dev-82.github.io/system-notes` (same RTD theme, same
   reference-table-on-the-index-page pattern, full-width content column via
   `docs_src/_static/custom.css` overriding RTD's default 800px cap). Seven pages:
   Index Levels & Rebasing, Base Dates, Drawdown, Rolling Returns, Volatility,
   Calendar-Year Returns, and **Choosing a Fund** (explains all the fund-selection
   rules above, plus the NRO→NRE route). Cross-linked both directions with the
   dashboard.

   **To rebuild after editing `docs_src/*.rst`:**
   ```bash
   cd docs_src && ../.venv/bin/python -m sphinx -b html . _build/html
   cd .. && rm -rf docs/notes && cp -r docs_src/_build/html docs/notes
   rm -rf docs/notes/.doctrees docs/notes/.buildinfo.bak
   ```

5. **Python env**: `.venv/` (gitignored) has `jugaad-data`, `pandas`, `sphinx`,
   `sphinx_rtd_theme` installed. Recreate with
   `python3 -m venv .venv && .venv/bin/pip install jugaad-data pandas sphinx sphinx_rtd_theme`
   if starting fresh.

## Gotchas learned this session (don't re-discover these)

- **GitHub Pages runs Jekyll by default**, which silently drops any folder starting
  with `_` (`_static/`, `_sources/`) — this broke the Sphinx site's CSS/JS entirely
  until `docs/.nojekyll` was added. That file must stay.
- **AMFI, NSE, Value Research, HDFC's own fund site, Moneycontrol** (via direct
  `curl`/fetch) are all unreachable or actively block this environment — either
  timeout or 403. Only workarounds found: `jugaad-data` (Python package) for NSE
  index history; a Hugging Face mirror (`Na-Rajan/IndianMutualFundsTER`) for AMFI's
  TER disclosure; `WebSearch`/`WebFetch` tools (which somehow get through where raw
  `curl` doesn't) for INDmoney and a few comparison articles.
- **RTD theme caps content width at ~800px** by default — fixed via
  `docs_src/_static/custom.css` (`max-width: none`), matching what the user's other
  Sphinx site already does.
- Puppeteer needed an older version (`puppeteer@21`, not latest) to get a Chrome
  build compatible with this environment's Node 18.

## Open items (not yet done, flagged not silently skipped)

- **NRI/OCI eligibility per AMC** — which specific AMCs actually accept an
  Australia-resident investor is unverified. Documented as an open question, not
  assumed either way.
- **Current NRO→NRE mechanics** (exact caps, Form 15CA/15CB process) — stated in the
  notes page in general terms, not verified against current rules.
- **10 funds with zero TER data** (listed above) — could pursue AMC factsheets
  directly if the user wants full coverage.
- **Tracking error** — essentially unavailable in bulk; would need per-fund manual
  lookup if the user decides it's worth the effort.
- Nothing beyond these three indices has been built yet (no Smallcap 250, Bank
  Nifty, sectoral indices, etc.) — mentioned as a future option early on, never
  requested since.
