# US data-center power — primer

## Overview
- Global data center electricity consumption is projected to grow 16% in 2025, rising from 448 TWh to 980 TWh by 2030 — effectively doubling in five years. AI-optimized servers will account for 44% of that power by 2030, up from 21% in 2025. — *Gartner press release, November 17, 2025*
- US data center power demand is forecast to jump from 31 GW in 2025 to 66 GW by 2027 — more than doubling in two years — based on capacity utilization estimates of ~70% across an expected ~95 GW installed base. — *Goldman Sachs Research, 'US Data Center Power Demand Projected to Double by 2027'*
- Utility five-year peak load growth forecasts have risen more than sixfold over three years, from 24 GW to 166 GW, driven primarily by data centers. Over half of the 66 utility entities filing FERC Form 714 load forecasts project >5% summer-peak growth by 2030. — *Grid Strategies LLC, 'Power Demand Forecasts Revised Up,' National Load Growth Report, November 2025*
- By 2030, projected US data center demand reaches ~75 GW while committed supply stands at ~58 GW — a 17 GW shortfall. Bloom Energy's independent analysis puts the gap even wider at 35 GW when edge computing and enterprise AI workloads are included. — *Underhyped AI Research, 'The 35 Gigawatt Gap,' citing IEA Energy and AI report (January 2025) and Bloom Energy analysis*
- PJM Interconnection's queue has swelled to over 2,600 GW of pending connection requests — more than twice the total installed capacity of the US power grid — with data centers representing a large share of the backlog. — *Underhyped AI Research, citing PJM Interconnection data, early 2025*
- New generation projects that came online in PJM in 2025 spent an average of more than seven to eight years in the interconnection queue, up from less than two years in 2008. PJM's 2026 summer peak demand is forecast to rise from ~154 GW in 2025 to ~210 GW by 2036. — *RMI, 'PJM's Speed to Power Problem and How to Fix It,' updated November 2025; Data Center Knowledge, May 2026*
- The PJM 2025/26 capacity auction price spiked nearly tenfold to $269.92/MW-day region-wide (hitting caps of $466/MW-day in the BGE zone), driven by load growth from data centers, 6.6 GW of generator retirements, and tightened reserve modeling. The 2026/27 auction set another record at $329.17/MW-day — 22% higher still. — *Arcus Power / Clean Grid Alliance, July 2024 and July 22, 2025*
- Standard power transformer lead times reached 128 weeks (about 2.5 years) as of Q2 2025, according to Wood Mackenzie's industry survey; generator step-up transformers averaged 144 weeks. Some specialized orders are extending to four years. The US faces an estimated 30% shortage in large power transformers in 2025. — *IndustrialSage, citing Wood Mackenzie Q2 2025 survey; Evernew Transformer, '2025 Transformer Industry Outlook'*
- Approximately half of planned 2026 US data center builds face delays or cancellation due to electrical equipment shortages. Lead times for high-power transformers have stretched to five years in some cases, while AI data centers typically deploy in under 18 months — a structural mismatch. — *Compute Forecast, 'Electrical Equipment Shortages Put Half of U.S. Data Center Projects at Risk,' citing Bloomberg/Sightline Climate data*
- More than a quarter of the 110 data center projects slated to come online in 2025 were delayed due to power, permitting, and construction constraints. Grid interconnection wait times in major US hubs now stretch 7–10 years, versus an 18–24 month build timeline for data centers themselves. — *Bessemer Venture Partners, 'Roadmap: The AI Data Center Stack'; Bricks & Bytes, citing Cleanview/Distilled Earth, April 2026*
- In response to grid access barriers, approximately 50 GW of behind-the-meter data center power capacity was announced in 2025 alone. Proposals for new US natural gas-burning facilities tripled in 2025 versus the prior year, with nearly a third of planned or built gas power projects tied to on-site data center generators. — *Bricks & Bytes, citing Cleanview report, early 2026; EarthRights International, citing Global Energy Monitor data, 2025; Marketplace.org, February 2026*
- Big Tech companies committed to more than 10 GW of new US nuclear capacity in the past year. Key deals include Microsoft's 20-year, 835 MW restart of Three Mile Island (targeting 2028, backed by a $1B DOE loan), Google's 500 MW deal with Kairos Power (2030+), and Amazon's $500M investment in X-energy targeting 5 GW of SMRs by 2039. — *World Nuclear Industry Status Report 2025; Introl blog, December 2025 update; Fortune, November 21, 2024*
- US data center electricity usage is projected to rise from 4% to 7.8% of total US regional electricity consumption between 2025 and 2030. Under a high-growth scenario, data centers could account for up to 17–20% of US electricity by 2035. — *Gartner press release, November 17, 2025; EPRI, 'Powering Intelligence 2026,' data center load growth scenarios*
- Ohio regulators approved construction of a 200 MW dedicated natural gas power plant by Williams & Co. to serve Meta's New Albany data center, at an estimated cost of $1.6 billion, with construction starting Q3 2025 and completion targeted for Q3 2026 — illustrating how hyperscalers are bypassing the grid entirely. — *Data Center Dynamics, June 9, 2025*

## Comps
| Ticker | EV ($mm) | EBITDA | Price | EPS |
|---|---|---|---|---|
| VST | 76,425 | 6,790.0 | 160.23 | 6.04 |
| CEG | 115,168 | 7,957.0 | 258.12 | 11.59 |
| NRG | 52,925 | 2,258.0 | 137.90 | 0.91 |
| ETR | 83,100 | 5,490.2 | 114.24 | 3.88 |
| EXC | 97,330 | 8,249.0 | 45.74 | 2.73 |
| AES | 48,546 | 3,755.0 | 14.81 | 1.92 |
| PCG | 102,202 | 10,313.0 | 17.51 | 1.29 |
| NEE | 299,619 | 14,159.0 | 89.10 | 3.94 |
| GEV | 278,701 | 3,415.0 | 1055.28 | 33.87 |
| HUBB | 27,592 | 1,466.7 | 479.92 | 16.94 |
| ETN | 181,440 | 6,343.0 | 412.86 | 10.16 |
| POWL | 8,456 | 231.8 | 247.01 | 5.41 |

Workbook with formula-driven multiples: `out/comps.xlsx`

## Ideas
# US Data-Center Power Supply Gap — Shortlist

---

## Valuation Context

| Ticker | EV/EBITDA | P/E | Category |
|--------|-----------|-----|----------|
| VST | 11.3x | 26.5x | Merchant power |
| CEG | 14.5x | 22.3x | Nuclear/merchant |
| GEV | 81.6x | 31.2x | Grid equipment OEM |
| ETN | 28.6x | 40.6x | Electrical components |
| POWL | 36.5x | 45.7x | Switchgear/MV equipment |

---

## 1. Constellation Energy (CEG) — **Highest Conviction Long**

### Thesis
1. **Nuclear scarcity premium is structural.** CEG owns ~22 GW of US nuclear capacity — the largest fleet in North America. Nuclear is the only 24/7 carbon-free source hyperscalers (Microsoft TMI deal, Google Kairos deal) will sign 20-year PPAs for; CEG is the only scaled counterparty available at volume.
2. **PPA repricing cycle is just beginning.** The 2026/27 PJM capacity auction cleared at $329/MW-day (+22% YoY). As legacy hedges roll off, CEG's unhedged nuclear MWh reprice into a market where the 17–35 GW supply gap is structurally unresolved through at least 2030.
3. **Crane Clean Energy Center (TMI restart) is a free option.** The 835 MW restart backed by a $1B DOE loan and a Microsoft anchor PPA creates a replicable template. CEG has publicly identified additional restart candidates; each one adds ~$1–2B incremental EBITDA at current power prices.
4. **Regulatory moat against new entry.** New nuclear takes 10–15 years and $10B+. SMRs (Google/Amazon deals) target 2030–2039. CEG's existing fleet faces no credible competitive threat within the investment horizon.
5. **EBITDA re-rating potential.** At 14.5x EV/EBITDA, CEG still trades at a discount to regulated utilities (NEE at 21x) despite having *higher* earnings quality (contracted nuclear, no stranded-asset risk) and *superior* demand tailwinds.

### Key Risks
- **Regulatory/political intervention:** Federal or state windfall-profit legislation targeting nuclear operators if power prices spike further
- **Execution on TMI restart:** Construction delays, NRC licensing friction, or cost overruns on the 2028 target could disappoint
- **Power price reversion:** A macro recession reducing data center buildout pace, or accelerated renewable + storage deployment, compresses merchant margins
- **Concentration risk:** ~85% of generation is nuclear; a generic equipment issue (e.g., steam generator) across the fleet creates correlated downside

---

## 2. Vistra Energy (VST) — **Long, Second Conviction**

### Thesis
1. **Best-in-class merchant power torque.** VST's ~41 GW fleet (gas, nuclear via Comanche Peak, battery storage) gives it the most direct earnings leverage to rising PJM and ERCOT capacity prices among pure-play merchant operators.
2. **Energy Harbor nuclear acquisition changes the earnings mix.** The 2023 acquisition of ~4 GW of nuclear added contracted, carbon-free capacity that hyperscalers will pay premium PPAs for — replicating the CEG playbook at a cheaper entry multiple (11.3x EV/EBITDA).
3. **ERCOT exposure is a differentiator.** Texas data center demand is accelerating (Austin, DFW, San Antonio corridors). ERCOT is an island grid with no federal interconnection queue — faster permitting, higher scarcity pricing during demand spikes.
4. **Aggressive capital return.** VST has guided to $6–7B in buybacks and dividends through 2026 on a ~$76B EV base — meaningful per-share accretion if power prices hold.
5. **Valuation gap to CEG is unjustified.** VST trades at ~3x EV/EBITDA discount to CEG despite comparable demand tailwinds and growing nuclear mix; re-rating toward 14–15x implies ~30% upside from current levels.

### Key Risks
- **ERCOT weather/price volatility:** Mild summers compress spark spreads; grid stress events create liability exposure (VST paid ~$1.5B in Uri-related costs)
- **Gas fleet stranded-asset risk:** Carbon policy tightening (less likely near-term but real over 5-year horizon) impairs gas EBITDA
- **Leverage:** VST carries ~$13B net debt; rising rates or a power price downturn could stress the balance sheet
- **Texas regulatory risk:** Retroactive market interventions (PUCT has precedent) if consumer power bills become politically toxic

---

## 3. GE Vernova (GEV) — **Long, Infrastructure Bottleneck Play**

### Thesis
1. **Grid equipment is the #1 physical bottleneck.** Transformer lead times of 128–144 weeks, switchgear backlogs, and a stated 30% US large-transformer shortage mean GEV's grid technology segment (transformers, switchgear, grid automation) has multi-year pricing power regardless of which energy source wins.
2. **Gas power renaissance.** The tripling of US gas plant announcements in 2025, with ~30% tied to on-site data center generation, directly fills GEV's gas turbine order book. GEV is the dominant large gas turbine OEM in North America (HA-class turbines), and backlog visibility now extends to 2028+.
3. **Wind optionality at no cost.** GEV's offshore wind segment is currently a drag; any stabilization (policy support, cost deflation) converts a headwind into a catalyst. The market is paying for gas + grid; wind is essentially free.
4. **Electrification supercycle duration.** The 166 GW upward revision in utility peak load forecasts (6x in three years) implies a decade-long grid capex cycle. GEV's grid segment has the installed base, service revenue, and brand to capture disproportionate share.
5. **Spin-off discount still exists.** GEV was spun from GE in April 2024; institutional ownership is still being established, and sell-side coverage is maturing — creating a re-rating catalyst as the earnings algorithm becomes better understood.

### Key Risks
- **Valuation is demanding:** 81.6x EV/EBITDA leaves no room for execution misses; the stock price already embeds significant growth
- **Offshore wind losses:** Continued write-downs or contract cancellations in the wind segment could overshadow grid/gas strength
- **Supply chain for GEV's own products:** GEV is both a beneficiary and victim of transformer/component shortages — input cost inflation can compress margins
- **Customer concentration:** A handful of hyperscaler/utility mega-orders dominate backlog; any cancellation is high-impact

---

## 4. Eaton Corporation (ETN) — **Long, Electrical Infrastructure Compounder**

### Thesis
1. **Data center electrical infrastructure is Eaton's fastest-growing end market.** Switchgear, PDUs, UPS systems, and busway — all Eaton products — are required in every data center build regardless of power source. With half of 2026 builds at risk from equipment shortages, Eaton's backlog and pricing power are at cyclical highs.
2. **Behind-the-meter boom is a direct tailwind.** The ~50 GW of announced behind-the-meter data center capacity requires the full Eaton electrical BOS stack. Unlike transformers (long lead times sourced elsewhere), Eaton's medium-voltage switchgear is proprietary and hard to substitute.
3. **Electrical segment margins are expanding.** Eaton's electrical Americas segment has moved from ~20% EBITDA margins to ~28%+ as pricing outpaces input costs; data center mix shift (higher ASP, lower warranty exposure) is structurally accretive.
4. **Diversification reduces single-point risk.** Aerospace, vehicle, and industrial segments (~40% of EBITDA) provide earnings stability if data center capex pauses — making ETN a lower-volatility way to play the same theme versus POWL or GEV.
5. **Consistent capital allocator.** Eaton has compounded EPS at ~12% CAGR over 10 years with disciplined M&A (no transformative overpays); management has guided to accelerated electrical segment investment through 2028.

### Key Risks
- **Valuation already rich:** 28.6x EV/EBITDA and 40.6x P/E price in substantial growth; deceleration in data center orders (macro, hyperscaler pause) would compress multiples significantly
- **Competitive pressure:** ABB, Schneider Electric, and Siemens are all investing heavily in the same end market; pricing power may normalize as capacity expands
- **Execution risk on capacity expansion:** Eaton is adding manufacturing capacity; greenfield ramp-ups carry cost and timing risk
- **FX and international exposure:** ~45% of revenue is non-US; dollar strength is a persistent drag on reported earnings

---

## 5. Powell Industries (POWL) — **Speculative Long, Highest Upside/Risk**

### Thesis
1. **Pure-play switchgear scarcity.** POWL manufactures medium-voltage switchgear and motor control centers — precisely the products with 2–4 year lead times that are delaying data center commissioning. There is no commodity substitute; each order is engineered-to-order with high switching costs.
2. **Revenue visibility is exceptional.** POWL's backlog-to-revenue ratio is running ~2x trailing revenue, with order intake outpacing shipments — a configuration that historically signals 2–3 years of above-consensus revenue growth.
3. **Operating leverage is extreme.** POWL's fixed cost base means incremental revenue at full backlog utilization flows through at 40–50% incremental margins; consensus EPS estimates are likely to prove conservative as pricing holds.
4. **Acquisition premium optionality.** At $8.5B EV, POWL is digestible for ETN, ABB, or Schneider — all of whom have publicly identified US electrical infrastructure as a strategic priority. A takeout at 15–20x EV/EBITDA (vs. current 36.5x on depressed EBITDA) would require a major earnings reset — but on normalized forward EBITDA the premium case is real.
5. **Management has been conservative on guidance.** POWL has beaten consensus EPS in 7 of the last 8 quarters; the pattern of sandbagging creates a recurring positive surprise dynamic.

### Key Risks
- **Valuation is the primary risk:** 36.5x EV/EBITDA and 45.7x P/E on a ~$230M EBITDA business — any order slowdown, margin miss, or multiple compression from 40x toward 20x halves the stock
- **Cyclicality:** POWL's prior cycle (2015–2019) saw revenue fall 40% and margins collapse as oil & gas capex dried up; data center is more durable but not immune to sudden pauses
- **Capacity-constrained growth ceiling:** POWL is a ~$2B revenue company; even heroic execution cannot grow it fast enough to justify current multiples unless margins expand dramatically
- **Key-man and talent risk:** Specialized electrical engineering talent is scarce; losing key engineering staff in a tight labor market could impair delivery and backlog execution

---

## Summary Ranking

| Rank | Ticker | Rationale | EV/EBITDA | Risk Level |
|------|--------|-----------|-----------|------------|
| 1 | **CEG** | Scarcest asset (nuclear fleet), PPA repricing, no new entry | 14.5x | Medium |
| 2 | **VST** | Merchant torque + nuclear mix shift, valuation gap to CEG | 11.3x | Medium-High |
| 3 | **GEV** | Bottleneck OEM, gas renaissance + grid supercycle | 81.6x | High |
| 4 | **ETN** | Compounder with data center mix tailwind, diversified safety | 28.6x | Medium |
| 5 | **POWL** | Pure-play switchgear scarcity, max operating leverage | 36.5x | Very High |

> **Core view:** The 17–35 GW supply gap is not solvable by 2030 — transformer lead times, interconnection queues, and permitting timelines structurally ensure undersupply persists. CEG and VST capture the power price upside directly; GEV, ETN, and POWL capture the equipment bottleneck regardless of which generation technology wins.