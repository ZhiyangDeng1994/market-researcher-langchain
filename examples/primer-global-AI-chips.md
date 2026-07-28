# global AI chips — primer

## Overview
- The global AI GPU chip market is forecast to grow by USD 145.06 billion at a CAGR of 32.4% from 2024 to 2029, driven by surging demand for generative AI and machine learning workloads. — *Technavio / GII Research, AI GPU Chip Market Growth Analysis 2025-2029*
- NVIDIA's total revenue reached a record $57 billion in Q3 FY2026 (quarter ending ~Oct 2025), up 62% year-over-year and 22% quarter-over-quarter, with all data center GPUs sold out during the period. The company projects Blackwell and Rubin GPU platform sales to hit $0.5 trillion by end of calendar 2026. — *Yahoo Finance / NVIDIA earnings report, November 2025*
- NVIDIA's full fiscal year 2025 revenue soared to $187.1 billion, and the company's market capitalization briefly eclipsed the $5 trillion mark during 2025, making it the most valuable company in the world at that point. — *Yahoo Finance, 'Nvidia dominated the headlines in 2025,' December 2025*
- TSMC confirmed that its advanced CoWoS packaging capacity — not wafer production — had become the primary supply bottleneck for AI accelerators by 2025. Global demand for CoWoS packaging capacity surged 113% year-over-year in 2025, while TSMC planned to roughly double capacity to ~50,000 wafers per month by year-end 2025, still below unconstrained demand. — *CrispIdea / TSMC executive statements, 'AI Server Bottlenecks: Memory, Packaging & Power Limits,' 2025*
- NVIDIA pre-booked approximately 800,000–850,000 CoWoS wafers for 2026, representing more than half of TSMC's projected total annual output. TSMC executives stated in Q3 2025 that CoWoS capacity was 'very tight and remains sold out through 2025 and into 2026,' with NVIDIA confirming 'ongoing limitations in HBM memory pose short-term challenges for Blackwell production.' — *Institute for Progress (IFP), 'When Do More AI Chips for China Mean Fewer for the United States?,' 2025*
- NVIDIA secured over 70% of TSMC's CoWoS-L advanced packaging capacity for 2025, with Blackwell GPU shipment volumes increasing more than 20% each quarter, targeting annual volumes exceeding 2 million units. — *Introl Blog, 'CoWoS and Advanced Packaging: How Chip Architecture Shapes Data Center Design,' December 2025*
- H100 SXM5 GPU nodes were seeing lead times of 36–52 weeks from resellers in 2026, a structural shortage rooted in fully allocated CoWoS packaging capacity at TSMC and HBM production from SK Hynix unable to keep pace with demand. — *Spheron Network, 'GPU Shortage 2026: How to Secure AI Compute When Hardware Is Scarce,' 2026*
- SK Hynix held a dominant 62% share of global HBM shipments as of Q2 2025, with Goldman Sachs forecasting it will maintain over 50% total HBM market share through at least 2026. SK Hynix management expects HBM supply to remain tight even in 2027. BofA estimates the 2026 HBM market will reach $54.6 billion, up 58% year-over-year. — *SK Hynix News / Counterpoint Research / BofA, '2026 Market Outlook: SK Hynix's HBM to Fuel AI Memory Supercycle,' 2026*
- Micron's HBM revenues reached nearly $2 billion in Q4 fiscal 2025, an annual run rate of ~$8 billion. Micron's total FY2025 revenues surged 49% to $37.4 billion, with its data center business accounting for 56% of total revenue. The company had already sold out its entire 2026 HBM3E supply. — *Yahoo Finance, 'Why Micron and SK Hynix Could Quietly Become the Real AI Winners,' 2025*
- US export controls imposed in April 2025 required NVIDIA to apply for a license to sell its H20 GPU in China. NVIDIA took a charge of over $5 billion to its quarterly earnings as a result. CEO Jensen Huang called the export controls 'a failure,' noting they accelerated Chinese domestic chip development. Analysts at Bernstein projected NVIDIA's market share in China's AI chip sector to decline from 66% in 2024 to 54% in 2025. — *Brookings Institution / AInvest / TechBlog ComSoc, April–August 2025*
- In December 2025, President Trump announced a one-year waiver of export restrictions on NVIDIA's H200 chips to China, marking a sharp policy pivot away from Biden's 'small yard, high fence' approach and treating advanced chips as bargaining instruments in broader geopolitical negotiations. — *IISS Strategic Comments, 'The US pivot on regulating AI diffusion,' December 2025*
- The four largest hyperscalers — Meta, Microsoft, Amazon, and Alphabet — are on track for a combined $5.3 trillion in capital expenditures from fiscal year 2025 through 2030, according to Goldman Sachs. For 2026 alone, the four are projected to spend over $635 billion on AI infrastructure, a ~67% spike from their combined $381 billion in 2025 expenditures. — *Goldman Sachs / Yahoo Finance, 'AI spending from 4 tech giants will exceed the GDP of Japan through 2030,' 2025–2026*
- Morgan Stanley reported hyperscaler customers requesting NVIDIA Blackwell GPU systems in blocks of 100,000 units, creating deep enterprise backlogs, with a $500 billion booking pipeline through 2026. NVIDIA management expects demand to outrun supply until late 2026. — *AI CERTs News, 'Nvidia Blackwell and the Chip Demand Forecast Crunch,' 2025*
- NVIDIA holds approximately 88% of all AI accelerators sold, underpinned by the CUDA software ecosystem. Competing accelerators — AMD MI325X, Intel Gaudi 3, Google TPU v6, Amazon Trainium 2 — are emerging alternatives but lag in ecosystem maturity; AMD MI325X achieves ~87% of H100 inference performance at ~78% of the price, while Intel Gaudi 3 offers 10%–2.5x performance-per-dollar advantages for certain workloads. — *DeployBase / dataku.ai / Science Array, 'AI Chip Comparison: NVIDIA vs AMD vs Intel vs Custom Silicon,' June 2025*
- New US tariffs on semiconductor imports, effective 2025, are prompting AI server GPU supply chain restructuring, including planned price adjustments in North America, alternative logistics strategies, and regional manufacturing pivots to minimize risk and maintain production continuity. — *Research and Markets, 'AI Server GPU Chips Market – Global Forecast 2025–2030,' 2025*

## Comps
| Ticker | EV ($mm) | EBITDA | Price | EPS |
|---|---|---|---|---|
| NVDA | 5,102,142 | 165,514.0 | 212.50 | 6.55 |
| AMD | 854,340 | 7,430.0 | 529.14 | 2.91 |
| INTC | 543,465 | 14,174.0 | 102.99 | -0.58 |
| TSM | 15,157,179 | 2,856,031.1 | 419.48 | 11.49 |
| ASML | 38,012,755 | 12,704.4 | 1815.27 | 30.13 |
| AMAT | 459,071 | 9,275.0 | 579.43 | 10.31 |
| LRCX | 418,463 | 7,847.8 | 335.43 | 5.13 |
| KLAC | 294,446 | 5,850.2 | 224.50 | 3.43 |
| ARM | 292,758 | 1,064.7 | 277.01 | 0.83 |
| AVGO | 1,921,098 | 42,084.0 | 394.28 | 6.07 |
| MU | 1,001,642 | 68,222.0 | 904.28 | 40.69 |
| SMCI | 24,018 | 1,578.6 | 26.89 | 1.85 |

Workbook with formula-driven multiples: `out/comps.xlsx`

## Ideas
# AI GPU Supply Constraint — Investment Shortlist

---

## 1. NVIDIA (NVDA)
*The irreplaceable GPU monopolist*

**Thesis Points**
- **Demand vastly exceeds supply through at least late 2026:** 36–52 week lead times on H100/Blackwell nodes; Morgan Stanley reports 100,000-unit block orders with a $500B booking pipeline — pricing power is structural, not cyclical
- **CUDA moat compounds annually:** 88% accelerator market share is underpinned by a software ecosystem competitors cannot replicate in a single product cycle; switching costs are enterprise-wide, not chip-level
- **Blackwell/Rubin revenue ramp is front-loaded:** Management projects $0.5T in Blackwell/Rubin platform sales by end-2026; hyperscaler capex of $635B in 2026 alone is effectively a guaranteed demand floor
- **Gross margin resilience despite CoWoS/HBM constraints:** Even with packaging bottlenecks, NVDA converts scarcity into ASP premium — constrained supply simply raises clearing price per unit shipped
- **Export control pivot is a near-term positive:** Trump's December 2025 H200 waiver to China partially reopens a market NVDA lost; China exposure remains optionality, not dependency

**Key Risks**
- EV/EBITDA of ~31x leaves zero margin for error; any demand air pocket (hyperscaler capex pause, ROI skepticism) compresses multiple violently  `[UNSOURCED]`
- CoWoS and HBM constraints cap revenue upside regardless of order backlog — supply, not demand, is the binding constraint near-term
- AMD MI325X / Google TPU / Trainium 2 ecosystem maturation could erode 88% share at the margin over a 3–5 year horizon  `[UNSOURCED]`
- China export controls remain a political football — a reversal of the waiver could re-trigger a $5B+ inventory charge
- Concentration risk: ~4 hyperscaler customers represent the majority of revenue

---

## 2. SK Hynix (000660.KS / OTC: HXSCL)
*The HBM bottleneck owner*

**Thesis Points**
- **62% HBM market share in a product with no near-term substitute:** Every Blackwell GPU requires HBM3E; SK Hynix is NVIDIA's primary supplier and has supply agreements extending into 2026–2027
- **HBM supercycle is BofA's $54.6B market in 2026, +58% YoY:** SK Hynix captures the majority of incremental economics in the sharpest memory upcycle in a decade
- **Management explicitly guides supply tightness through 2027:** Unlike commodity DRAM, HBM capacity additions require 18–24 months of lead time — the moat is time, not just technology
- **Pricing power unprecedented in memory history:** HBM3E ASPs are 5–8x standard DRAM on a per-bit basis; margin structure is fundamentally different from commodity memory cycles
- **NVIDIA's CoWoS constraint means HBM is actually the deeper bottleneck:** Even if TSMC adds packaging capacity, insufficient HBM supply limits AI GPU output — SK Hynix is a co-equal chokepoint

**Key Risks**
- Samsung and Micron are investing aggressively; HBM share concentration erodes if Samsung resolves yield issues on HBM3E
- South Korea geopolitical exposure and potential US tariff/trade retaliation risk on semiconductor imports
- If AI capex cycle decelerates abruptly, HBM reverts toward commodity memory pricing dynamics
- OTC liquidity for US investors is limited; Korean won FX exposure adds volatility
- SK Hynix carries meaningful legacy DRAM/NAND exposure that can mask HBM earnings quality in down cycles

---

## 3. TSMC (TSM)
*The only fab that matters*

**Thesis Points**
- **Structural monopoly on advanced node + CoWoS packaging:** TSMC is the sole manufacturer capable of producing Blackwell/Rubin at scale; Intel Foundry and Samsung remain years behind on N3/N2 yields
- **CoWoS demand grew 113% YoY in 2025; TSMC still can't meet it:** Packaging capacity — not wafer starts — is the binding constraint, and TSMC is the only credible provider at volume, giving it extraordinary leverage over pricing
- **NVIDIA pre-booked >50% of 2026 CoWoS output:** This effectively de-risks TSMC's 2026 revenue in its highest-margin product line before the year begins
- **Arizona fab buildout reduces geopolitical discount over time:** As US domestic capacity comes online (N2/N3 Phoenix fabs), the Taiwan risk premium in the stock should structurally compress
- **Multiple hyperscaler custom silicon programs (Google TPU, Amazon Trainium, Apple) all run through TSMC:** Revenue diversification beyond NVIDIA is already embedded

**Key Risks**
- Taiwan invasion/strait conflict risk is an existential, unhedgeable tail risk — it is the single reason TSM trades at a discount to peers
- CoWoS capacity expansion (targeting ~50K WPM by end-2025) could eventually create oversupply in packaging if AI capex moderates
- US political pressure to accelerate domestic production could pressure margins at Arizona fabs (higher cost structure vs. Taiwan)
- Customer concentration: NVIDIA's ~50%+ CoWoS pre-booking means any NVIDIA demand shortfall flows directly to TSMC's utilization  `[UNSOURCED]`
- Currency (NTD appreciation) is a persistent headwind to USD-reported earnings

---

## 4. Broadcom (AVGO)
*The custom silicon dark horse*

**Thesis Points**
- **ASIC/XPU business is a direct beneficiary of hyperscaler desire to diversify away from NVDA:** Google TPU v6 and Meta's MTIA are both Broadcom-designed; as hyperscalers build proprietary AI silicon, Broadcom captures the design and manufacturing revenue
- **Networking is the underappreciated AI infrastructure play:** Broadcom's Ethernet switching/routing silicon (Tomahawk, Jericho) is essential plumbing for every GPU cluster — demand scales with GPU unit count regardless of who wins the accelerator war
- **Revenue visibility is high:** Broadcom operates on multi-year ASIC design contracts with hyperscalers; unlike NVDA, revenue is contracted, not order-backlog dependent
- **EV/EBITDA of ~46x is rich but justifiable** given the combination of infrastructure software (VMware) generating recurring revenue alongside the AI silicon growth engine
- **VMware integration provides margin expansion runway:** Post-acquisition cost synergies are still being realized; software mix shift structurally improves EBITDA margins

**Key Risks**
- ASIC wins are hyperscaler-specific and lumpy; loss of a single large customer (e.g., Google shifting strategy) creates meaningful revenue discontinuity
- VMware integration execution risk remains — enterprise software transitions of this scale have historically produced customer churn
- Custom silicon competes with NVDA's own NVLink/networking portfolio; NVIDIA has shown willingness to vertically integrate into networking (Mellanox acquisition)
- At current multiples, the stock prices in near-perfect execution on both AI silicon and VMware synergies simultaneously
- Regulatory risk: Broadcom's acquisition history has drawn antitrust scrutiny; future M&A optionality may be constrained

---

## 5. Super Micro Computer (SMCI)
*Distressed re-rating candidate with binary risk*

**Thesis Points**
- **Trades at EV/EBITDA of ~15x vs. AI infrastructure peers at 30–50x** — the accounting/governance discount is already in the price; if remediation is successful, multiple re-rating alone is a 2–3x from current levels
- **Systems integrator with direct exposure to Blackwell GPU server demand:** SMCI assembles and ships complete GPU server racks; as NVIDIA Blackwell volumes ramp 20%+ per quarter, SMCI's addressable unit count scales in lockstep
- **Liquid cooling expertise is a genuine differentiation:** SMCI's direct liquid cooling (DLC) technology is increasingly mandatory for high-density Blackwell/GB200 NVL72 rack deployments — thermal management is becoming a competitive moat
- **Hyperscaler and cloud provider customer relationships are intact:** Despite audit/governance issues, SMCI has not lost material customer contracts, suggesting the product offering remains competitive
- **Short squeeze / re-rating catalyst is finite and identifiable:** Successful auditor appointment and restated financials filing would be a discrete, near-term positive catalyst

**Key Risks**
- **Governance and accounting risk is unresolved and binary:** Failure to file restated financials or appointment of a credible auditor could trigger Nasdaq delisting — permanent capital loss scenario
- Gross margins are structurally thin (systems integrator model); SMCI has limited pricing power relative to component suppliers (NVDA, Samsung, Intel)
- Revenue is highly concentrated in AI GPU servers — a demand air pocket or NVIDIA supply disruption flows directly to SMCI revenue with minimal buffer
- Competition from Dell, HPE, and hyperscaler in-house rack assembly intensifies as the market matures
- **This is a high-risk, catalyst-dependent position — sizing must reflect binary outcome distribution**

---

## Summary Ranking by Risk/Reward Profile

| Name | Thesis Type | Risk Level | Key Catalyst |
|---|---|---|---|
| **TSMC** | Structural monopoly, defensive | Medium | CoWoS pricing + Arizona de-risking |
| **SK Hynix** | Supply bottleneck owner | Medium-High | HBM3E contract renewals 2026–27 |
| **NVDA** | Compounding monopoly | Medium-High | Blackwell/Rubin ramp execution |
| **AVGO** | Diversified AI infrastructure | Medium | ASIC wins + VMware margins |
| **SMCI** | Distressed re-rating | Very High | Audit resolution / re-listing |