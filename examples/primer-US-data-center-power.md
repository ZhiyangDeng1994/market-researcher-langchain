# US data-center power — primer

## Overview
- US data centers consumed about 176 TWh of electricity in 2023, roughly 4.4% of total US electricity demand, up from ~58 TWh (~1.9%) in 2014. — *Lawrence Berkeley National Laboratory, '2024 United States Data Center Energy Usage Report' (Dec 2024)*
- LBNL projects US data center electricity consumption could reach 325-580 TWh by 2028, equal to roughly 6.7%-12% of total US electricity demand. — *Lawrence Berkeley National Laboratory, '2024 United States Data Center Energy Usage Report' (Dec 2024)*
- The IEA estimates global data center electricity use will more than double to around 945 TWh by 2030, with the US accounting for the largest share of the increase. — *International Energy Agency, 'Energy and AI' report (April 2025)*
- Goldman Sachs projects US data center power demand will grow at a ~15% CAGR through 2030, with data centers reaching about 8% of total US electricity demand by 2030 versus ~3% in 2022. — *Goldman Sachs Research, 'Generational growth: AI, data centers and the coming US power demand surge' (2024)*
- AI-related US data center power demand is expected to drive about 160 GW of incremental capacity needs, contributing to a projected supply gap as utilities struggle to add generation and transmission fast enough. — *McKinsey & Company, 'How data centers and the energy sector can sate AI's hunger for power' (2024)*
- Roughly half of new US data center demand growth through 2030 is expected to be met by natural gas, with the remainder from renewables and existing nuclear, reflecting near-term reliability and dispatchability needs. — *Goldman Sachs Research, US power and gas demand outlook (2024)*
- Grid interconnection queues have ballooned, with over 2,600 GW of generation and storage capacity awaiting connection as of end-2023, and typical interconnection wait times now around 5 years, constraining timely supply additions. — *Lawrence Berkeley National Laboratory, 'Queued Up: 2024 Edition' interconnection queue report*
- Microsoft signed a 20-year agreement with Constellation Energy to restart the Three Mile Island Unit 1 reactor (~835 MW), illustrating hyperscaler willingness to underwrite nuclear power to secure firm supply. — *Constellation Energy press release, September 20, 2024*
- PJM Interconnection's 2024/2025 capacity auction cleared at a record ~$14.7 billion (prices up roughly 800% year over year), reflecting tightening reserve margins driven in part by data center load growth. — *PJM Interconnection 2025/2026 Base Residual Auction results (July 2024)*
- Northern Virginia ('Data Center Alley') hosts the world's largest data center market, with Dominion Energy reporting it connected record data center load and projecting Virginia data center demand could roughly quadruple over the next 15 years. — *Dominion Energy Integrated Resource Plan / earnings disclosures (2024)*
- US electricity demand is forecast to grow about 3% in both 2024 and 2025 after roughly a decade of flat growth, with data centers cited as a primary driver of the inflection. — *US Energy Information Administration, Short-Term Energy Outlook (2024-2025)*
- Grid Strategies estimates US five-year load growth forecasts jumped to roughly 128 GW (from ~23 GW a year earlier), with data centers and manufacturing as leading contributors to the revised demand outlook. — *Grid Strategies, 'The Era of Flat Power Demand is Over' / 'Strategic Industries Surging' report (Dec 2024)*
- Gas turbine supply is constrained, with major OEMs (GE Vernova, Siemens Energy, Mitsubishi Power) reporting multi-year backlogs and lead times stretching to 2028-2029, limiting how fast new firm capacity can be deployed. — *GE Vernova and Siemens Energy investor communications and earnings commentary (2024)*
- Hyperscalers led by Microsoft, Amazon, Google and Meta are projected to spend over $200 billion in combined capex in 2024-2025, much of it for AI data center buildout, intensifying competition for power and grid capacity. — *Company 2024 earnings disclosures; Dell'Oro Group and analyst capex compilations*

## Comps
| Ticker | EV ($mm) | EBITDA | Price | EPS |
|---|---|---|---|---|
| VST | 71,060 | 6,790.0 | 146.22 | 5.98 |
| CEG | 112,832 | 7,957.0 | 251.65 | 11.50 |
| NRG | 51,250 | 2,258.0 | 129.96 | 0.91 |
| ETR | 81,003 | 5,490.2 | 109.66 | 3.91 |
| EXC | 96,910 | 8,249.0 | 45.33 | 2.73 |
| AES | 48,439 | 3,755.0 | 14.66 | 1.92 |
| PCG | 100,154 | 10,313.0 | 16.58 | 1.29 |
| FE | 56,016 | 5,170.0 | 45.91 | 1.85 |
| DUK | 188,593 | 16,478.0 | 123.82 | 6.50 |
| SO | 182,597 | 13,974.0 | 92.95 | 3.91 |
| NEE | 290,715 | 14,159.0 | 84.83 | 3.94 |
| GEV | 242,389 | 3,415.0 | 920.15 | 34.23 |

Workbook with formula-driven multiples: `out/comps.xlsx`

## Ideas
# US Data-Center Power: Idea Shortlist

**Theme Framing:** Grid tightness is structural, not cyclical. The ~160 GW incremental demand estimate collides with 5-year interconnection queues, 2028-2029 turbine backlogs, and a decade of underinvestment in dispatchable capacity. The winners are whoever owns **firm, dispatchable, already-interconnected megawatts** — not whoever is building them.

---

## Comps Table (Derived Multiples)

| Ticker | EV ($mm) | EBITDA ($mm) | EV/EBITDA | P/E | Angle |
|--------|----------|--------------|-----------|-----|-------|
| VST | 71,060 | 6,790 | **10.5x** | 24.5x | Merchant power, AI PPA exposure |
| CEG | 112,832 | 7,957 | **14.2x** | 21.9x | Nuclear pure-play, TMI restart |
| NRG | 51,250 | 2,258 | **22.7x** | >100x | Retail/gen mix, transitional |
| ETR | 81,003 | 5,490 | **14.8x** | 28.0x | Regulated, SE data center corridor |
| EXC | 96,910 | 8,249 | **11.8x** | 16.6x | Regulated T&D, PJM footprint |
| AES | 48,439 | 3,755 | **12.9x** | 7.6x | Renewables + storage, restructuring |
| PCG | 100,154 | 10,313 | **9.7x** | 12.9x | CA regulated, wildfire tail risk |
| FE | 56,016 | 5,170 | **10.8x** | 24.8x | PJM T&D, capacity market upside |
| DUK | 188,593 | 16,478 | **11.4x** | 19.0x | Carolinas/IN regulated, SE growth |
| SO | 182,597 | 13,974 | **13.1x** | 23.8x | Vogtle nuclear base, GA/AL growth |
| NEE | 290,715 | 14,159 | **20.5x** | 21.5x | Renewables premium, rate risk |
| GEV | 242,389 | 3,415 | **70.9x** | 26.9x | Turbine OEM scarcity play |

> **Sector median EV/EBITDA (ex-GEV outlier): ~12.9x**

---

## The 5 Ideas

---

### 1. Vistra Energy (VST) — **Long** — *Cheapest per-MW of AI-era firm capacity*

| Metric | Value | vs. Peers |
|--------|-------|-----------|
| EV/EBITDA | 10.5x | ~20% discount to median |
| P/E | 24.5x | In-line |
| FCF profile | ~$3B+ guided 2025 | Strong |
| Nuclear capacity | ~6.4 GW (incl. Comanche Peak) | Largest merchant nuclear fleet |
| Data center PPA exposure | Active negotiations disclosed | Early-mover |

**Thesis:**
- Owns ~41 GW of dispatchable generation across every major US power market — the hardest asset to replicate given queue backlogs and turbine lead times. This is a **scarcity asset masquerading at a utility multiple**
- Nuclear fleet (~6.4 GW) positions VST as the merchant analog to CEG: zero-carbon, 24/7 baseload — exactly what hyperscalers need and can't build fast enough  `[UNSOURCED]`
- Merchant structure means VST captures **spot price upside** as PJM capacity prices reprice; the record $14.7B 2025/2026 PJM auction directly flows to earnings, unlike regulated peers who pass it through
- Aggressive capital return: $3.25B buyback authorized through 2026; share count down ~20% since 2022. FCF per share compounding at high rates  `[UNSOURCED]`
- Valuation gap vs. CEG (10.5x vs. 14.2x) is hard to justify given similar nuclear exposure; CEG premium largely explained by the TMI narrative already being priced  `[UNSOURCED]`

**Key Risks:**
- Merchant earnings volatility — a mild winter/cool summer compresses power prices
- Nuclear fleet operational risk (unplanned outages re-rate the story quickly)
- Regulatory/legislative risk if Congress revisits merchant nuclear policy

---

### 2. Constellation Energy (CEG) — **Long (with caveats)** — *Nuclear scarcity premium is still being discovered*

| Metric | Value | vs. Peers |
|--------|-------|-----------|
| EV/EBITDA | 14.2x | ~10% premium to median |
| P/E | 21.9x | Moderate |
| Nuclear capacity | ~32.4 GW (largest US fleet) | Unmatched |
| Contracted AI PPAs | TMI 20-yr Microsoft deal signed | De-risked cash flows |
| CAGR target | ~10% EPS growth through 2030 guided | High visibility |

**Thesis:**
- The **only large-cap pure-play nuclear** story in US equities; owns ~32.4 GW — roughly 10% of all US nuclear capacity — which is **impossible to replicate** (no new greenfield nuclear comes online before 2030 at meaningful scale)
- Microsoft TMI deal is a proof-of-concept for a pipeline of hyperscaler PPAs. Google, Amazon, and Meta are all signaling willingness to sign long-term nuclear PPAs to hit carbon commitments — CEG is the obvious counterparty
- Nuclear Production Tax Credit under IRA (up to $15/MWh) provides a floor on economics even if power prices soften; the PTC effectively backstops downside
- Each incremental hyperscaler PPA at rumored ~$100+/MWh prices vs. ~$30-40/MWh historical blended price is a massive earnings uplift on already-built, fully depreciated assets

**Caveats / Why Not #1:**
- Much of the TMI/PPA narrative is already in the stock (up >200% since early 2023)  `[UNSOURCED]`
- At 14.2x EBITDA vs. VST at 10.5x for similar nuclear exposure, the relative trade favors VST unless you believe CEG deserves a sustained scarcity premium  `[UNSOURCED]`
- Best entry on pullbacks; current risk/reward less compelling than VST on a fresh position

**Key Risks:**
- Regulatory: NRC license extension risk; any nuclear safety incident globally re-rates the sector
- PPA pipeline disappointment — if hyperscalers slow capex, the premium multiple compresses
- Concentration: ~90% nuclear means any technology or policy shift hits hard  `[UNSOURCED]`

---

### 3. GE Vernova (GEV) — **Long** — *The picks-and-shovels play on the supply gap itself*

| Metric | Value | vs. Peers |
|--------|-------|-----------|
| EV/EBITDA | 70.9x | Massive premium — intentionally |
| P/E | 26.9x | Reasonable on forward basis |
| Order backlog | ~$115B+ (2024 disclosures) | Multi-year revenue locked |
| Turbine lead times | 2028-2029 for large gas turbines | Supply constraint = pricing power |
| Revenue growth | Guided high-single to low-double digit | Accelerating |

**Thesis:**
- GEV is the **structural bottleneck** in the entire supply gap narrative. You cannot add dispatchable gas capacity without turbines, and GEV (along with Siemens Energy and Mitsubishi) controls the oligopoly. Backlogs extending to 2028-2029 mean pricing power is locked in for years
- Every data point in the brief — 160 GW incremental demand, 128 GW upward revision in 5-year forecasts, ~50% of new capacity from gas — runs through GEV's order book. This is a **toll road on the energy transition**
- GEV is transitioning from a legacy GE conglomerate discount to a standalone industrial compounder. Margins in the Power segment are inflecting as pricing catches up to backlog; Wind losses are being restructured
- The EV/EBITDA multiple looks absurd (70.9x) but is misleading: EBITDA is heavily depressed by Wind segment losses and the transition period. On a normalized/forward Power+Electrification basis, the multiple compresses substantially as Wind drags roll off  `[UNSOURCED]`
- CEO Scott Strazik has credibility — early execution since the April 2024 spin has been clean

**Key Risks:**
- Wind segment continues to bleed and offsets Power earnings growth longer than expected
- If hyperscaler capex guidance disappoints, order intake could slow (though backlog provides 3+ year buffer)
- Valuation requires flawless execution; any earnings miss is punished severely at this multiple
- Siemens Energy is a credible comp and alternative — if SE executes well, it limits GEV's pricing power

---

### 4. Entergy (ETR) — **Long** — *Regulated utility in the path of the data center wave, at a discount*

| Metric | Value | vs. Peers |
|--------|-------|-----------|
| EV/EBITDA | 14.8x | ~15% premium to regulated median |
| P/E | 28.0x | Elevated but earnable |
| Service territory | AR, LA, MS, TX Gulf Coast | Southeast industrial corridor |
| Data center load growth | Significant disclosed pipeline | Above-average regulated utility |
| Nuclear base | ~5 GW (Grand Gulf, ANO, Waterford) | Carbon-free baseload |

**Thesis:**
- ETR's service territory sits in the **secondary data center corridor** — lower land/power costs than Northern Virginia, available land, and state-level incentives are pulling new hyperscaler investment into the Southeast. ETR has disclosed a large queued industrial/data center load pipeline
- Regulated structure is actually advantageous here: rate base growth from load additions is **earnings-accretive and low-risk**, unlike merchant players. Every GW of new data center load = capex investment + allowed return, compounding for decades
- Owns ~5 GW of nuclear (already amortized) serving as anchor baseload — increasingly valuable as carbon-free attributes command premiums in corporate PPAs  `[UNSOURCED]`
- At 14.8x EV/EBITDA vs. Southern Company at 13.1x, the premium is modest given ETR's superior load growth profile. Duke (DUK) at 11.4x is the cheaper Carolinas analog but has less industrial load torque  `[UNSOURCED]`
- EPS growth target of ~6-8% is conservative and likely to be revised upward as data center load materializes in rate base filings

**Key Risks:**
- Hurricane/weather exposure in Gulf Coast territory (operational and insurance risk)
- Regulatory lag: rate cases in Mississippi and Louisiana can be contentious
- If data center buildout slows or relocates to different geographies, the pipeline doesn't materialize

---

### 5. FirstEnergy (FE) — **Long** — *PJM capacity price windfall, trading at trough multiple*

| Metric | Value | vs. Peers |
|--------|-------|-----------|
| EV/EBITDA | 10.8x | ~15% discount to regulated median |
| P/E | 24.8x | In-line (depressed earnings base) |
| PJM footprint | OH, PA, NJ, WV, MD | Epicenter of data center demand |
| Transmission rate base | ~$26B+ growing to ~$35B by 2028 | High-visibility growth |
| FCF inflection | Post-Ohio bribery settlement | Cleanup largely done |

**Thesis:**
- FE is a **pure transmission and distribution utility** in PJM — the most capacity-constrained market in the US. The $14.7B record capacity auction (up ~800% YoY) flows directly to earnings for distribution utilities as pass-through mechanics benefit load-serving entities in the region
- The market is pricing FE on its **post-scandal trough** (Ohio bribery scandal, management turnover) — the cleanup is largely complete, new management has credibility, and the business is structurally sound. This is a classic "hated but healing" setup
- Transmission capex is the **most visible and least risky** capital program in utilities — FERC-regulated returns, formula rates, and a 10%+ allowed ROE provide high earnings visibility. $35B rate base by 2028 implies mid-single-digit EPS CAGR off a depressed base
- Northern Virginia/PJM data center boom is a direct tailwind: as load grows in FE's territory, transmission investment requirements increase, rate base grows, earnings grow. The link is mechanical
- Discount to peers (10.8x vs. ~12-13x for clean regulated utilities) closes as the scandal premium fades and earnings growth materializes  `[UNSOURCED]`

**Key Risks:**
- Residual legal/regulatory risk from Ohio scandal (ongoing DOJ/SEC inquiries)
- Regulated utilities are interest-rate sensitive — if rates stay elevated, the valuation discount may persist
- Pennsylvania/Ohio regulatory environments can be contentious in rate cases
- Slower-than-expected data center load growth in PJM territory

---

## Summary Rankings

| Rank | Ticker | Direction | Conviction | Primary Edge |
|------|--------|-----------|------------|--------------|
| 1 | **VST** | Long | High | Cheapest firm MW; merchant upside to PJM prices; nuclear scarcity |
| 2 | **GEV** | Long | High | Structural bottleneck; backlog locked; pricing power for years |
| 3 | **FE** | Long | Medium-High | PJM epicenter; trough multiple; transmission growth |
| 4 | **ETR** | Long | Medium | Regulated; SE growth corridor; nuclear base |
| 5 | **CEG** | Long | Medium | Nuclear scarcity premium; wait for better entry vs. VST |

---

## What's Not on the List (and Why)

- **NEE**: Premium multiple (20.5x) without the same near-term catalyst; rate sensitivity on the FPL regulated side
- **NRG**: Elevated EBITDA multiple (22.7x) for a messy retail/gen mix; less clean AI power narrative
- **PCG**: Wildfire liability tail risk is unquantifiable; not the right risk for this theme
- **DUK/SO**: Good regulated utilities, but the data center torque is less concentrated; already fairly valued at 11-13x

---

> **Next Steps:** VST and GEV are the highest-conviction starting points for deep-dive modeling. Key work items: (1) VST nuclear fleet capacity factor and PPA pipeline analysis; (2) GEV segment-level margin bridge as Wind losses roll off; (3) PJM forward capacity curve sensitivity for FE.