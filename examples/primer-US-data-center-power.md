# US data-center power — primer

## Overview
- US data center electricity demand is projected to reach roughly 6.7% to 12% of total US electricity consumption by 2028, up from about 4.4% in 2023. — *Lawrence Berkeley National Laboratory, '2024 United States Data Center Energy Usage Report' (Dec 2024)*
- US data center power consumption was estimated at about 176 TWh in 2023 and is forecast to grow to 325-580 TWh by 2028, implying a 13-27% annual growth range. — *Lawrence Berkeley National Laboratory, '2024 United States Data Center Energy Usage Report' (Dec 2024)*
- Goldman Sachs estimates global data center power demand will grow ~165% by 2030 versus 2023, with AI a primary driver of the incremental load. — *Goldman Sachs Research, 'AI to drive 165% increase in data center power demand by 2030' (Feb 2025)*
- AI is expected to drive about 19% growth in data-center power demand in the US between 2023 and 2030, with US data centers reaching ~8% of total power demand by 2030. — *Goldman Sachs Research, 'AI is poised to drive 160% increase in power demand' (Apr 2024)*
- PJM Interconnection, which serves Virginia's 'Data Center Alley,' raised its 15-year peak load forecast significantly, with data centers cited as the dominant driver of demand growth. — *PJM Interconnection 2024 Long-Term Load Forecast*
- PJM's 2024/2025 capacity auction cleared at about $14.7 billion, roughly a 9x increase over the prior auction, reflecting tightening supply against rising data-center-driven demand. — *PJM Interconnection 2025/2026 Base Residual Auction results (July 2024)*
- Northern Virginia (Loudoun County) is the world's largest data center market, with over 25 million square feet of data center space and concentrated grid strain in Dominion's service territory. — *Northern Virginia Technology Council / Loudoun County Economic Development data (2024)*
- Dominion Energy reported a quadrupling of data center connection requests and projects Virginia electricity demand to nearly double over the next 15 years, driven largely by data centers. — *Dominion Energy 2024 Integrated Resource Plan*
- Interconnection queue backlogs are a key supply constraint, with over 2,600 GW of generation and storage capacity waiting in US interconnection queues at end of 2023. — *Lawrence Berkeley National Laboratory, 'Queued Up' (2024 edition)*
- Gas turbine supply is constrained, with major OEMs (GE Vernova, Siemens Energy, Mitsubishi) reporting multi-year backlogs and delivery lead times stretching to 2028 and beyond for large frame turbines. — *GE Vernova Q3 2024 earnings commentary; Siemens Energy FY2024 reporting*
- Hyperscalers are securing nuclear power directly: Microsoft signed a 20-year PPA to restart Three Mile Island Unit 1 (Crane Clean Energy Center) with Constellation Energy. — *Constellation Energy / Microsoft announcement (Sep 2024)*
- Amazon agreed to acquire a data center campus connected to Talen Energy's Susquehanna nuclear plant, signaling 'behind-the-meter' nuclear sourcing to bypass grid constraints. — *Talen Energy / AWS announcement (Mar 2024)*
- Grid equipment shortages are acute: lead times for large power transformers have extended to as long as 2-4 years, constraining new interconnection capacity. — *US Department of Energy, 'National Transformer Reserve' and grid supply chain assessments (2024)*
- Electricity demand growth in the US is accelerating after roughly two decades of flat consumption, with NERC flagging elevated reliability risks in multiple regions due to demand growth outpacing new supply. — *NERC 2024 Long-Term Reliability Assessment (Dec 2024)*
- McKinsey estimates US data center power demand could reach about 606 TWh by 2030, up from ~147 TWh in 2023, requiring a roughly 50 GW build-out of new capacity dedicated to data centers. — *McKinsey & Company, 'How data centers and the energy sector can sate AI's hunger for power' (2024)*

## Comps
| Ticker | EV ($mm) | EBITDA | Price | EPS |
|---|---|---|---|---|
| VST | 68,470 | 6,790.0 | 146.38 | 5.98 |
| CEG | 111,048 | 7,957.0 | 246.71 | 11.51 |
| NRG | 49,929 | 2,258.0 | 123.70 | 0.90 |
| ETR | 81,378 | 5,490.2 | 109.89 | 3.92 |
| EXC | 97,197 | 8,249.0 | 45.51 | 2.73 |
| AES | 48,446 | 3,755.0 | 14.67 | 1.92 |
| PCG | 100,616 | 10,313.0 | 16.79 | 1.29 |
| FE | 56,455 | 5,170.0 | 46.67 | 1.84 |
| NEE | 290,735 | 14,159.0 | 84.84 | 3.94 |
| DUK | 188,881 | 16,478.0 | 124.19 | 6.50 |
| SO | 182,957 | 13,974.0 | 93.27 | 3.91 |
| AWK | 39,829 | 2,836.0 | 124.45 | 5.64 |

Workbook with formula-driven multiples: `out/comps.xlsx`

## Ideas
# US Data-Center Power — Idea Shortlist

*Supply-gap angle: own the scarce electrons, not the demand*

---

## Framing the Screen

The structural edge here is **generation scarcity, not data center growth**. The right names are those that (a) sell power into markets where data-center load is tightest, (b) own dispatchable/baseload capacity that cannot be quickly replicated, and (c) have pricing leverage as capacity markets reprice. The comps data lets us sort by EV/EBITDA to separate the re-rating candidates from names already priced for perfection.

**Computed multiples from the comps table:**

| Ticker | EV/EBITDA | P/E | Category |
|--------|-----------|-----|----------|
| VST | **10.1x** | 24.5x | Merchant gen |
| CEG | **14.0x** | 21.4x | Nuclear merchant |
| NRG | **22.1x** | 137x | Retail/merchant |
| ETR | **14.8x** | 28.0x | Regulated utility |
| EXC | **11.8x** | 16.7x | Regulated T&D |
| AES | **12.9x** | 7.6x | IPP/renewables |
| PCG | **9.8x** | 13.0x | Regulated utility |
| FE | **10.9x** | 25.4x | Regulated T&D |
| NEE | **20.5x** | 21.5x | Regulated + renewables |
| DUK | **11.5x** | 19.1x | Regulated utility |
| SO | **13.1x** | 23.9x | Regulated utility |
| AWK | **14.0x** | 22.1x | Water utility |

**Screened out immediately:** NRG (22x EBITDA, P/E near 140x — priced for flawless execution), NEE (20x, primarily Florida regulated + wind, limited PJM merchant exposure), AWK (water — different thesis entirely).

---

## The Shortlist

---

### 1. **Vistra Energy (VST) — Long**
**"The largest merchant generator in PJM, at the cheapest multiple in the group"**

| Metric | Value |
|--------|-------|
| EV | $68.5B |
| EV/EBITDA | 10.1x |
| P/E | 24.5x |
| Key markets | PJM, ERCOT |

**Thesis:**
- Largest competitive power generator in the US with ~41 GW of capacity, heavily weighted to PJM — the exact grid where data-center load is exploding (Virginia, Ohio, Illinois). Every capacity auction reprice flows directly to Vistra's margin  `[UNSOURCED]`
- PJM's 2024/25 capacity auction cleared ~9x higher than the prior year. Vistra is a price-taker on the upside — its fixed-cost fleet harvests the margin expansion with no incremental capex  `[UNSOURCED]`
- Nuclear fleet (via Vistra Vision, ~6 GW) provides carbon-free baseload at a time when hyperscalers are paying premiums for clean PPAs; optionality to replicate CEG-style corporate PPA structures is underpriced  `[UNSOURCED]`
- Trading at a 4-turn discount to CEG on EV/EBITDA despite comparable merchant exposure and arguably better geographic positioning in ERCOT (tight market) plus PJM
- Buyback-driven capital return: management has been aggressively repurchasing shares, a discipline unusual in the power sector

**Key Risks:**
- Merchant power is cyclical — a mild winter, gas price collapse, or demand miss compresses spark spreads fast
- Regulatory risk: FERC market reform could cap capacity prices
- Texas exposure (ERCOT) means weather volatility can swing earnings ±$500M in a given year
- Already up significantly from 2023 lows; not a deep value entry

**Next Steps:** Model forward capacity auction scenarios with sensitivity to PJM clearing prices; stress-test EBITDA under $2/mmBtu gas

---

### 2. **Constellation Energy (CEG) — Long (higher conviction, higher multiple)**
**"The only scaled nuclear fleet with a repeatable hyperscaler PPA playbook"**

| Metric | Value |
|--------|-------|
| EV | $111B |
| EV/EBITDA | 14.0x |
| P/E | 21.4x |
| Key markets | PJM, Mid-Atlantic, Midwest |

**Thesis:**
- Owns the largest nuclear fleet in the US (~32 GW), producing 24/7 carbon-free baseload — precisely what Microsoft, Google, and Amazon are willing to pay above-market rates to secure  `[UNSOURCED]`
- Three Mile Island restart (Crane Clean Energy Center) is a proof of concept that idle nuclear capacity has option value others can't replicate; pipeline of similar restart/uprate opportunities is real
- Nuclear PPA structure insulates CEG from spot price volatility while capturing the scarcity premium hyperscalers will pay; this is a qualitatively different revenue stream than commodity merchant power
- Inflation Reduction Act production tax credits (~$15/MWh) for nuclear provide a durable earnings floor regardless of market prices — this subsidy alone covers a significant portion of operating cost
- The moat is structural: you cannot build new nuclear in under 10 years; CEG's existing fleet is irreplaceable and appreciating

**Key Risks:**
- Already the consensus "data-center power" trade — multiple has re-rated significantly; much of the thesis is in the price
- Nuclear operations carry event risk (unplanned outages can be materially expensive)
- PPA negotiations are complex and slow; hyperscaler demand doesn't automatically convert to signed contracts
- Regulatory/IRA policy risk if political environment shifts on nuclear subsidies

**Next Steps:** Diligence the PPA pipeline beyond TMI; model IRA PTC sensitivity; compare uprate economics at other plants

---

### 3. **Entergy (ETR) — Long (asymmetric/under-the-radar)**
**"Regulated utility with an underappreciated data-center load boom in its own backyard"**

| Metric | Value |
|--------|-------|
| EV | $81.4B |
| EV/EBITDA | 14.8x |
| P/E | 28.0x |
| Key markets | Louisiana, Mississippi, Texas, Arkansas |

**Thesis:**
- Entergy's service territory (Gulf Coast) is an emerging second-wave data center destination — lower land costs, available industrial power, and proximity to gas supply are attracting hyperscaler investment away from the saturated Virginia/Northern NJ markets
- As a regulated utility, every incremental data-center load translates into a rate base expansion opportunity, which is the most durable, low-risk way to monetize the demand surge — earnings grow with capital deployed, not with commodity prices
- Mississippi and Louisiana are seeing industrial load growth (LNG exports, onshoring, now data centers) that is driving one of the stronger rate base growth profiles in the regulated sector
- Trades at a discount to NEE and SO on EV/EBITDA despite a cleaner earnings profile (no major storm-liability tail like PCG, no Florida rate case risk like NEE)
- Management has been executing on a multi-year simplification/improvement story that is not yet fully reflected

**Key Risks:**
- Regulated returns are capped — this is a rate base growth story, not a margin expansion story; upside is slower and more predictable
- Gulf Coast weather exposure (hurricane season) can create large one-time costs and political friction
- Higher P/E (28x) relative to other regulated utilities limits the valuation cushion  `[UNSOURCED]`
- Data center development in the Gulf Coast is earlier-stage; the load may be slower to materialize than the Virginia thesis

**Next Steps:** Request IRP and rate case filings; model rate base CAGR under data-center load scenarios; compare against DUK and SO on growth capex pipeline

---

### 4. **FirstEnergy (FE) — Long (deep value / catalyst-driven)**
**"Discounted PJM utility with a clean-up story and direct exposure to the capacity price surge"**

| Metric | Value |
|--------|-------|
| EV | $56.5B |
| EV/EBITDA | 10.9x |
| P/E | 25.4x |
| Key markets | Ohio, Pennsylvania, New Jersey, West Virginia |

**Thesis:**
- Cheapest regulated utility in PJM on EV/EBITDA (10.9x vs. sector median ~13-14x) — the discount reflects legacy legal/regulatory overhangs (Ohio bribery scandal), not operational deterioration  `[UNSOURCED]`
- PJM capacity prices are clearing at multi-year highs driven by data-center load in Virginia and the broader PJM footprint; FE's regulated distribution network in Ohio/Pennsylvania is the pipe that connects that load growth to customers
- Management has been executing a credibility restoration program since 2021; incremental re-rating toward peer multiples implies meaningful upside — a 2-turn multiple expansion on current EBITDA is worth ~$10/share
- Pending equity raise / minority stake sale in transmission subsidiary would crystallize value and reduce holding-company discount
- 4%+ dividend yield provides a paid-to-wait dynamic while the re-rating plays out  `[UNSOURCED]`

**Key Risks:**
- The Ohio political/regulatory risk is real and not fully resolved; a new adverse ruling could overhang the stock for another 12-18 months
- FE is a T&D utility — it doesn't own generation, so it doesn't directly capture capacity price upside (unlike VST/CEG)
- Execution risk on the balance sheet repair; any equity dilution is a near-term headwind
- P/E of 25x is not cheap — the valuation argument rests on EV/EBITDA and normalized earnings, not trailing P/E  `[UNSOURCED]`

**Next Steps:** Review Ohio regulatory docket; model holding company discount scenarios; timeline clarity on transmission stake transaction

---

### 5. **AES Corporation (AES) — Contrarian Long / Watch**
**"Potential deep value if renewables narrative stabilizes — but needs a catalyst"**

| Metric | Value |
|--------|-------|
| EV | $48.4B |
| EV/EBITDA | 12.9x |
| P/E | **7.6x** |
| Key markets | US + international IPP |

**Thesis:**
- Trading at 7.6x P/E — the cheapest earnings multiple in the entire comp set by a wide margin, and below typical regulated utility floors. This is either a value trap or a significant mispricing  `[UNSOURCED]`
- AES has a large US renewables pipeline with data-center-focused PPAs; has signed or announced clean energy contracts with hyperscalers directly, positioning it as a contracted supplier to the AI power build-out
- The market is discounting AES for (a) international exposure/currency risk, (b) balance sheet concerns, and (c) renewables sector sentiment collapse post-2022. None of these are new news
- If AES executes on its US clean energy pipeline and the market re-rates the contracted portion at utility multiples, there is substantial gap to close
- Possible catalyst: asset sales / simplification toward a pure US contracted clean energy model

**Key Risks:**
- The low P/E may reflect genuine earnings quality concerns — AES has complex international operations with FX/political risk that reduce cash earnings visibility
- Balance sheet is levered; rising rates pressure project finance economics
- Renewables supply chain (solar panels, equipment) remains unpredictable; development timelines slip
- This is a "show me" stock — the catalyst for re-rating is unclear and timing is uncertain. Do not size aggressively without deeper diligence

**Next Steps:** Decompose earnings between US contracted and international operations; stress-test FCF conversion; identify specific catalyst timeline

---

## Ranking by Conviction

| Rank | Name | Direction | Conviction | Why |
|------|------|-----------|------------|-----|
| 1 | **VST** | Long | High | Cheapest merchant, direct PJM capacity leverage, nuclear optionality |
| 2 | **CEG** | Long | High | Structural moat, hyperscaler PPA machine, IRA floor — but buy the dips |
| 3 | **FE** | Long | Medium-High | Re-rating catalyst, PJM exposure, deep discount to peers |
| 4 | **ETR** | Long | Medium | Gulf Coast second-wave, regulated upside, under-owned |
| 5 | **AES** | Long | Low-Medium | Needs more work; optionality is real but catalyst is unclear |

---

## What's Missing from This Screen

- **Gas turbine OEMs** (GE Vernova): the supply bottleneck facts suggest GEV deserves its own screen — turbine backlogs extending to 2028+ is a separate but related idea
- **Transformer/grid equipment** (Hubbell, Atkore, Quanta Services): the 2-4 year transformer lead time is a bottleneck play worth screening separately
- **Nuclear fuel** (Cameco, Centrus): if the nuclear-restart thesis is right, uranium enrichment is a leveraged derivative
- **Short idea**: Any data-center developer pricing in power access they don't yet have — interconnection queue backlogs mean announced projects ≠ powered projects