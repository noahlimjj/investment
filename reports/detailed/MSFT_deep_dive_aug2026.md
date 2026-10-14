# Microsoft (MSFT) — Deep Dive

**Date:** 28 August 2026 · **Price:** $505.06 · **Market cap:** $3.75T · **EV:** $3.80T
*(Valuation tables below were built at $496.88 on 14 Aug; the +1.6% move since does not change any conclusion.)*
**Fiscal year:** FY2026 ended 30 June 2026 · **Primary source:** FY26 10-K (filed late July 2026)

> ⚠️ The existing [MSFT.md](MSFT.md) in this folder is stale — it is priced at $390.54 on a $2.9T cap and cites a PEG of 1.21. Every valuation conclusion in it is superseded by this file.

---

## 1. What actually happened in FY2026

Microsoft had an exceptional operating year and a poor cash year. Both are true, and the gap between them is the whole investment debate.

| ($B) | FY2024 | FY2025 | FY2026 | FY26 YoY |
|---|---|---|---|---|
| Revenue | 245.1 | 281.7 | **331.8** | +17.8% |
| Gross margin | 171.0 | 193.9 | 225.5 | +16.3% |
| Gross margin % | 69.8% | 68.8% | **67.9%** | −0.9pp |
| Operating income | 109.4 | 128.5 | **155.2** | +20.8% |
| Operating margin | 44.6% | 45.6% | **46.8%** | +1.2pp |
| Net income (GAAP) | 88.1 | 101.8 | **133.7** | +31.3% |
| Diluted EPS (GAAP) | $11.80 | $13.64 | **$17.95** | +31.6% |
| Operating cash flow | 118.5 | 136.2 | **182.9** | +34.3% |
| Capex (cash PP&E) | 44.5 | 64.6 | **115.9** | **+79.6%** |
| **Free cash flow** | **74.1** | **71.6** | **67.0** | **−6.5%** |
| Capex / revenue | 18.1% | 22.9% | **34.9%** | +12.0pp |
| D&A / revenue | 8.6% | 10.4% | 11.6% | +1.2pp |

**Free cash flow has now declined three years running** — $74.1B → $71.6B → $67.0B — while revenue grew 35% over the same span. That is the single most important number in this analysis.

### Segments (FY26)

| Segment | Revenue | YoY | Operating income | Margin | Δ margin |
|---|---|---|---|---|---|
| Productivity & Business Processes | $140.0B | +16% | $83.9B | 59.9% | +2.1pp |
| Intelligent Cloud | $137.8B | +30% | $57.0B | 41.3% | **−0.7pp** |
| More Personal Computing | $54.1B | −1% | $14.4B | 26.6% | +0.7pp |

Azure +41% for the year (+43% in Q4), crossing $100B of annual revenue. Microsoft Cloud $214.4B (+27%). M365 Copilot passed 30M paid seats. Commercial RPO **$678B, +84%** — a genuinely enormous backlog, though ~$250B of it is the OpenAI Azure commitment (see §7).

### Earnings quality: the headline overstates the business

GAAP net income grew 31.3%. Operating income grew 20.8%. The gap is `Other income (expense), net`, which swung from **−$4.9B in FY25 to +$10.7B in FY26** — a $15.6B pre-tax swing driven by investment marks, not operations:

- **OpenAI:** +$6.5B of net gains in FY26 (vs −$4.8B in FY25), "primarily the dilution gain from the OpenAI Recapitalization." Per the 10-K this added **$5.0B to net income and $0.67 to diluted EPS**; FY25 had a −$3.6B / −$0.49 drag. That is a **$1.16 EPS swing** from a non-cash accounting event.
- **Anthropic:** a separate ~$3.2B gain booked in Q4.

Strip the investment marks and tax the operating result: core net income went **$105.4B → $125.7B, +19.3%**, not +31.3%. Microsoft's own non-GAAP EPS of $17.28 (vs $17.95 GAAP) makes the same adjustment for OpenAI.

**Use ~19–20% as the real FY26 earnings growth rate.** Anything quoting 32% is quoting an accounting artifact.

---

## 2. Valuation multiples

At $496.88 with 7,453M diluted shares and net debt of $52.0B (bonds $40.3B + finance leases $66.6B + operating leases $21.9B − cash & ST investments $76.8B):

| Metric | Value | Comment |
|---|---|---|
| **P/E (trailing GAAP)** | **27.7x** | on $17.95 |
| P/E (trailing, non-GAAP) | 28.8x | on $17.28 — the cleaner number |
| **P/E (forward, FY27e ~$19.75)** | **25.2x** | matches third-party fwd P/E of 25.15x |
| P/E (FY28e ~$22.50) | 22.1x | |
| **EV/EBITDA (TTM)** | **19.4x** | EBITDA $193.8B (EBIT $155.2B + D&A $38.5B) |
| EV/EBIT | 24.2x | |
| EV/Sales | 11.3x | |
| **P/FCF** | **55x** | FCF $67.0B |
| **FCF yield** | **1.81%** | vs ~4% risk-free |
| Net debt / EBITDA | 0.27x | balance sheet still pristine |
| ROE | 34.0% | |
| ROIC | 25.4% | down from ~30%+ pre-buildout |
| Dividend yield | 0.71% | $3.56/sh |
| Buyback yield | 0.60% | $22.3B |
| **Total shareholder yield** | **1.32%** | and it consumed **73% of FCF** |

### PEG — and why the old 1.21 reading is gone

PEG is only as good as the growth number you feed it. Three defensible versions:

| Growth basis | Rate | PEG (on 25.2x fwd) |
|---|---|---|
| FY27 consensus profit growth | 9.9% | **2.55** |
| FY26→FY28 EPS CAGR | ~13% | **1.94** |
| Long-run consensus | ~16% | **1.57** |

**PEG is now roughly 1.6–2.5, not 1.2.** The near-term PEG is poor because FY27 earnings growth decelerates sharply — the depreciation from FY26's $116B of capex lands on the P&L just as the comparison base gets harder. The old report's PEG of 1.21 was computed on a $390 price against a growth rate that included the OpenAI mark. Both inputs have changed.

### EV/EBITDA is the flattering lens — treat it with suspicion

19.4x EV/EBITDA looks reasonable against MSFT's own 5-year average of ~20x. But EBITDA adds back depreciation, and depreciation is the mechanism by which a $116B/yr GPU buildout shows up as an economic cost. **For a company whose capex is 35% of revenue, EV/EBITDA systematically flatters.** EV/FCF at 56x is the honest version of the same picture. The truth sits between them, but investors anchoring on EV/EBITDA here are anchoring on the metric most insulated from the actual risk.

---

## 3. Capex — the core of the thesis

| | FY24 | FY25 | FY26 | FY27 guide |
|---|---|---|---|---|
| Cash capex (PP&E additions) | $44.5B | $64.6B | **$115.9B** | ~$160B+ |
| Total capex incl. finance leases | ~$55B | ~$88B | **~$145B** | "grows YoY"; Q1 alone >$50B |
| Capex / revenue | 18.1% | 22.9% | **34.9%** | ~42% |

Management would not give an FY27 dollar range on the call — only that capex "will grow year-over-year given demand signals," with Q1 FY27 above $50B. That annualises to a >$200B total run rate. (A widely-circulated $255–260B FY27 figure came from a pre-earnings analyst preview, **not** from company guidance.)

Three things in the 10-K deserve more attention than they get:

1. **PP&E net went from $205.0B to $313.1B in one year** (+53%). Accumulated depreciation rose from $93.7B to $118.7B.
2. **Depreciation lives were disclosed as "servers and network equipment, two to six years."** The explicit two-year floor is new language and matters: roughly two-thirds of recent capex is short-lived assets (CPUs/GPUs). The bear argument — that hyperscalers depreciate AI silicon over 5–6 years while its economic life is closer to 2–3 as Nvidia moved to an annual architecture cadence — is a real accounting risk, and Microsoft has partially conceded it in the disclosure.
3. **$329.1 billion of leases signed but not yet commenced**, primarily datacenters, commencing FY2027 through FY2033. This is *not* in the balance sheet, *not* in net debt, and *not* in any screening EV. On top of that: $34.6B of construction commitments and $88.5B of on-balance-sheet lease liabilities. Microsoft's committed future infrastructure spend is far larger than its reported leverage suggests.

**Working capital is quietly doing some lifting too.** Accounts payable jumped from $27.7B to $42.4B (+53%) — Microsoft is stretching payables against the capex ramp, which flatters operating cash flow. Unearned revenue contributed $9.4B.

The capital allocation math is now tight: FY26 FCF of $67.0B against $48.7B returned to shareholders (73% of FCF) plus ~$20B of net investing outflows for OpenAI/Anthropic. Cash and short-term investments fell $94.6B → $76.8B. Microsoft has not yet needed to issue debt — it repaid $3.0B and issued none — but at FY27's implied capex it is close to the point where buybacks, the balance sheet, or capex has to give.

---

## 4. Peer analysis

Verified market caps and consistently-sourced EV/EBITDA (all 16 Aug 2026):

| | Price | Market cap | EV/EBITDA | CY2026 capex | Recent FCF |
|---|---|---|---|---|---|
| **Microsoft** | $496.88 | **$3.68T** | **19.4x** | ~$175B | **+$67.0B (FY26)** |
| Alphabet | $343.54 | $4.20T | 23.9x | $195–205B | **−$5.9B (Q2)** |
| Amazon | $262.65 | $2.83T | 16.6x | ~$220B | **−$7.6B (TTM)** |
| Meta | $589.85 | $1.50T | 14.3x | $130–145B | barely positive |
| Oracle | $146.94 | ~$0.42T | 15.5x | ~$70B | negative; raised $43B debt in FY26 |

*Note: forward P/E figures circulating for Alphabet (~17.5x) are stale and internally inconsistent with its EV/EBITDA — I've excluded them rather than propagate them.*

**Four things fall out of this table:**

1. **Microsoft is the only US hyperscaler still generating meaningful positive free cash flow.** Alphabet's FCF went negative for the first time since its 2004 IPO. Amazon swung to −$7.6B TTM. Meta is scraping positive with a cash balance down 91% YoY. Oracle is funding its buildout with $43B of debt in FY26 and plans ~$40B more in FY27. On the metric that actually matters this cycle, Microsoft is winning — and by a wide margin.

2. **Microsoft is not the most expensive on EV/EBITDA — Alphabet is.** At 19.4x MSFT sits mid-pack, above Amazon (16.6x), Oracle (15.5x) and Meta (14.3x), below Alphabet (23.9x). Meta at 14.3x is the value name of the group, which reflects genuine skepticism about its capex having no cloud business to sell into.

3. **Alphabet has overtaken Microsoft in market cap** ($4.20T vs $3.68T) on the back of Google Cloud growing 82% in Q2 — roughly double Azure's rate. This is the first cycle in a decade where Microsoft is losing the cloud growth-rate contest, and it is losing it to a competitor with its own frontier models and its own silicon (TPUs). Azure's 41% is excellent in absolute terms and second-best in the group; it is no longer the differentiated story it was.

4. **Oracle is the cautionary tale for how this can reprice.** ORCL at $146.94 on a "possible value trap" forward P/E of ~14.5x, despite a $638B RPO up 363%. A gigantic AI backlog did not protect the multiple once the market decided the backlog was debt-financed and concentrated. Microsoft's $678B RPO is better funded and better diversified — but it is the same asset class of promise.

**Relative verdict:** Microsoft is the highest-quality asset in the group and the only one still self-funding. It is priced accordingly. If you want hyperscaler exposure with the least chance of a capital-structure accident, it is the obvious pick. It is not the cheapest way to own the theme.

---

## 5. DCF

**Method:** 10-year explicit FCFF forecast, terminal value with reinvestment tied to ROIC (`reinvestment = g / ROIC`) rather than an assumed multiple. Base FY26 actuals from the 10-K. Tax 19% (FY26 effective). Net debt $52.0B. 7,453M diluted shares. Unearned revenue credited as a structural working capital source at 4% of incremental revenue.

Capex paths are anchored to guidance: FY27 cash capex ~$160B (~42% of revenue, consistent with Q1 >$50B total), then fading toward a post-buildout steady state. D&A ramps with the capital base — this is what compresses EBIT even as EBITDA margin holds.

| Scenario | Rev CAGR (10y) | Terminal EBITDA margin | Terminal capex/rev | WACC | g | Terminal ROIC | **Value/share** | vs $496.88 |
|---|---|---|---|---|---|---|---|---|
| **Bear** | 6.3% | 53.5% | 21.0% | 9.5% | 3.0% | 14% | **$171** | −66% |
| **Base** | 9.9% | 60.0% | 19.5% | 8.5% | 4.0% | 18% | **$422** | **−15%** |
| **Bull** | 11.8% | 64.0% | 18.0% | 8.0% | 4.5% | 24% | **$739** | +49% |

Probability-weighted (25/50/25): **$439, −12%**.

**Base case FCF path** ($B): FY27 33 → FY28 58 → FY29 94 → FY30 135 → FY31 172 → FY36 279. Note the trough: even in the base case, FCF **halves in FY27** to ~$33B before the capex/revenue ratio starts falling. Free cash flow does not exceed its FY24 peak of $74.1B until FY2029.

**Terminal value is 69% of base-case EV** — high, and unavoidable when near-term FCF is suppressed by a buildout. It also means the answer is highly sensitive to the terminal assumptions:

**Value/share, WACC × terminal growth (base case):**

| WACC \ g | 3.0% | 3.5% | 4.0% | 4.5% | 5.0% |
|---|---|---|---|---|---|
| 7.5% | 479 | 511 | 552 | 606 | 682 |
| 8.0% | 426 | 450 | 479 | 516 | 566 |
| **8.5%** | 383 | 401 | **422** | 449 | 483 |
| 9.0% | 347 | 361 | 377 | 396 | 420 |
| 9.5% | 317 | 327 | 340 | 354 | 372 |

**Value/share, WACC × terminal ROIC (g = 4%):**

| WACC \ ROIC | 12% | 15% | 18% | 22% | 26% |
|---|---|---|---|---|---|
| 7.5% | 492 | 528 | 552 | 573 | 588 |
| **8.5%** | 380 | 405 | **422** | 437 | 448 |
| 9.5% | 308 | 327 | 340 | 351 | 359 |

You need WACC ≤7.5% *and* terminal growth ≥4.5% to justify today's price on base-case operating assumptions.

### Reverse DCF — what is priced in

Holding the base-case margin and capex paths and solving for the growth rate that yields $496.88:

> **The market is discounting a ~12.1% revenue CAGR for ten years — Microsoft reaching ~$1.04 trillion of revenue by FY2036.**

For context, Microsoft compounded revenue at ~13% over the last five years and grew 17.8% in FY26. So the market is asking for slightly *below* recent growth, sustained for a decade, off a base four times larger — with margins recovering to 60% EBITDA and capex intensity falling by half. That is demanding but not absurd. It is emphatically not a bargain.

### Sum-of-parts sanity floor

The bear DCF's $171 is below what the non-AI business is independently worth, so treat it as a stress bound rather than a target:

| Segment | FY26 NOPAT | Multiple | Value |
|---|---|---|---|
| Productivity & Business Processes | $67.9B | 22x | $1,495B |
| More Personal Computing | $11.7B | 14x | $163B |
| Intelligent Cloud | $46.1B | 20x | $923B |

- **Non-cloud only, less net debt: ~$215/share.** This is the practical floor — M365, Office, LinkedIn and Dynamics are asset-light, wide-moat and would be worth this even if every AI dollar were written off.
- Full SOTP, less net debt: ~$339/share.
- The ~27% OpenAI stake is carried inside $36.3B of equity investments; marked at the October 2025 recapitalisation valuation of $135B it would be ~$18/share.

**Practical downside anchor: ~$215–260, not $171.**

---

## 6. Bull case

1. **The buildout is demand-constrained, not speculative.** $678B of commercial RPO, +84%, is contracted revenue. Microsoft is not building into hope; it is building into signed backlog. Amy Hood's framing is credible: two-thirds of capex is short-lived assets with short lead times, so if demand softens the spend can be throttled within quarters, while land and buildings — the genuinely illiquid part — are a small and timing-flexible share.
2. **Copilot is inflecting.** 30M paid seats, up from 20M the prior quarter. At ~$30/user/month, each incremental 10M seats is ~$3.6B of near-pure-margin annual revenue layered onto an existing M365 relationship with no incremental sales cost. PBP margin already expanded 2.1pp to 59.9%, which is what this looks like in the numbers.
3. **Microsoft is the last hyperscaler standing on cash.** Every competitor is FCF-negative or debt-funding. If the AI capex cycle turns into a funding crunch, Microsoft acquires share cheaply while Oracle refinances and Meta explains itself. Net debt/EBITDA of 0.27x is an option on other people's distress.
4. **Operating leverage is real and already visible.** FY26 opex grew 8% against 18% revenue growth. Operating margin *expanded* 1.2pp in the heaviest capex year in company history. Management guides FY27 margin down less than one point despite the depreciation wave.
5. **The capex ratio mean-reverts mechanically.** Capex/revenue at 35% cannot persist. In the base case, simply fading it to ~20% by FY33 while revenue compounds at ~10% produces $279B of FCF by FY36 — 4x today. The bull case is mostly "this normalises a year or two earlier than feared."

**Bull target: $739** (11.8% revenue CAGR, 64% terminal EBITDA margin, 8.0% WACC).

---

## 7. Bear case

1. **Free cash flow has fallen for three consecutive years and P/FCF is 55x.** This is the fact that resists all narrative. You are paying 55x for cash generation that is shrinking. The bull answer — "it recovers in FY29" — requires you to underwrite six years of execution on a technology cycle nobody can forecast two years out.
2. **The depreciation schedule may be flattering earnings.** Servers depreciated over "two to six years"; Nvidia now ships a new architecture annually. If economic life is nearer 3 years than 6, reported EPS overstates true earnings materially — estimates of the industry-wide understatement run to ~$176B across 2026–2028. This does not hit cash flow (it is already spent) but it would hit the multiple, hard, the moment the market decides to reprice on cash rather than EPS.
3. **$329.1B of leases not yet commenced.** Signed, off-balance-sheet, commencing FY27–FY33. No screen captures this. Microsoft's true committed obligations are far above its 0.27x net-debt/EBITDA optics, and these commitments were struck at peak-cycle datacenter pricing.
4. **The OpenAI relationship got worse, not better.** In the October 2025 recapitalisation Microsoft took a ~27% stake ($135B mark) and a $250B Azure purchase commitment — but **lost its right of first refusal on OpenAI cloud workloads** and gave up AGI-clause exclusivity. Microsoft generated $24.1B of revenue from OpenAI in FY26. So a meaningful chunk of the celebrated $678B RPO is a commitment from a counterparty that Microsoft partly owns, that is heavily loss-making, and that is now free to spend elsewhere. That is circularity, and the market has already punished Oracle for a version of it.
5. **Earnings quality is deteriorating.** The FY26 EPS headline of +32% was +19% at the operating line; the difference is a non-cash dilution gain on OpenAI. That gain reverses as easily as it appeared — Q4 already carried a ~$600M OpenAI markdown. Investors extrapolating 30% growth are extrapolating a mark.
6. **Azure is no longer the fastest horse.** Google Cloud grew 82% in Q2 against Azure's 41%, and Alphabet has passed Microsoft in market cap. Google owns its models *and* its silicon; Microsoft rents its frontier models from a partner that no longer owes it exclusivity. The strategic premium Microsoft enjoyed in 2023–24 has narrowed.
7. **Gross margin is eroding.** 69.8% → 68.8% → 67.9%. Intelligent Cloud's operating margin fell 0.7pp despite 30% revenue growth. AI revenue is structurally lower-margin than software revenue, and the mix is shifting toward it every quarter.

**Bear target: $171 from the DCF; ~$215–260 as the realistic floor** given the standalone value of the non-AI franchise.

**Thesis flipper:** two consecutive quarters of Azure growth decelerating below ~30% while capex guidance stays elevated. That combination would mean the spending is not converting, and the multiple would compress toward Meta's 14x EV/EBITDA — roughly $330/share.

---

## 8. Verdict

### HOLD — quality is intact, price is not attractive

| | |
|---|---|
| **Base-case fair value** | **$422** (−15%) |
| Probability-weighted (25/50/25) | $439 (−12%) |
| Bull / Bear | $739 / $171 (floor ~$215–260) |
| Priced-in growth | ~12.1% revenue CAGR for 10 years |
| **Accumulate below** | **$400** (≈5% margin of safety to base) |
| **Strong buy below** | **$340** (≈20% margin of safety) |
| **Trim above** | **$600** |

**Reasoning.** Microsoft remains the highest-quality business in this analysis — 34% ROE, 25% ROIC, 46.8% operating margins that *expanded* during the heaviest capex year in its history, a pristine balance sheet, and the only positive free cash flow among US hyperscalers. Nothing in the FY26 filing damages the moat. Productivity & Business Processes grew 16% at a 59.9% margin, and Copilot's move from 20M to 30M seats in a single quarter is the clearest AI monetisation in enterprise software.

The problem is arithmetic, not quality. Free cash flow has declined three years running while the share price sits at 55x it, and today's price requires a decade of ~12% revenue compounding *plus* a halving of capital intensity *plus* margin recovery to 60% EBITDA. My base case grants most of that and still lands 15% below spot. There is no margin of safety at $497.

Two specific concerns keep me from Buy at this price. First, **earnings quality**: FY26's headline 32% EPS growth was 19% at the operating line, with the difference a non-cash OpenAI dilution gain that can reverse. Second, the **$329.1B of leases not yet commenced** — signed obligations, invisible to every screen, struck at peak datacenter pricing, landing FY27–FY33.

**On the timing.** The stock fell from $553.72 (Oct 2025) to $349.20 (Jun 2026) — a 37% drawdown — and has since rallied 42%. Buying the AI-capex panic worked; the panic is over. At $349 this was a clear Buy against my base case. At $497 it is not. If you already own it, hold: the franchise compounds and the downside is genuinely protected by ~$215/share of non-AI business. If you are initiating, wait — a capex-panic re-run of the kind we saw two months ago is more likely than not somewhere in the next four quarters, and that is where the entry is.

**Positioning:** core holding, hold existing at full weight, no new capital above $400. Do not add on strength.

**What would change my mind, upward:** Azure holding ≥40% for two more quarters *with* FY27 capex guidance coming in below $180B — that combination would mean the buildout is nearly complete and the FCF recovery arrives a year early, taking base case toward $520.

---

### Watch list

- **Q1 FY27 (late Oct 2026):** actual capex vs the >$50B signal; first FY27 dollar range if given
- Azure growth rate — the ~30% line is the thesis flipper
- Copilot seat count (30M → ?) and whether M365 ARPU uplift is visible in PBP revenue
- Free cash flow: does it trough in FY27 as modelled, or keep falling?
- Any debt issuance — the first bond deal since FY24 would signal the balance sheet is now funding capex
- OpenAI: further recapitalisations, the size of Azure consumption vs the $250B commitment, and mark direction
- Depreciation life disclosure — any further shortening of the "two to six years" server range

---

*Model: `msft_dcf.py` (scratchpad). Sources: Microsoft FY2026 Form 10-K, Q4 FY26 press release and earnings call, companiesmarketcap.com, valueinvesting.io, CNBC, Investing.com.*

---

```
VERDICT:        HOLD
AS_OF:          2026-08-28
PRICE:          $505.06 USD
FAIR_VALUE:     $422
UPSIDE:         -16%
ENTRY_BELOW:    $400
EXIT_ABOVE:     $600
CONVICTION:     MEDIUM
KEY_RISK:       Free cash flow has fallen 3 years running; $329.1B of leases not yet commenced sit off balance sheet
DATA_WARNINGS:  0
```
