# Market Researcher (LangGraph)

A runnable reimplementation of Anthropic's **Market Researcher** agent, built as a
stateful [LangGraph](https://github.com/langchain-ai/langgraph) pipeline. Given a
sector, it produces an equity-research **primer**: a sourced market overview, a peer
comparable-company table (with a formula-driven Excel workbook), and a long/short
idea shortlist.

> **Not investment advice.** Outputs are AI-generated and built on free,
> best-effort data (Yahoo Finance + web search). Verify every figure before relying on it.

## What it does

Running the agent for a sector (e.g. *US data-center power*) generates:

- **Overview**: 8-15 key facts on market size, structure, trends, and supply/demand,
  each sourced from real web search results via Tavily.
- **Comps**: a peer valuation table from live market data (Yahoo Finance), plus
  `out/comps.xlsx` where every multiple is an Excel **formula** (`=B5/C5`) and every
  input cell carries a **source comment**.
- **Ideas**: a long/short shortlist with thesis, risks, and peer-relative valuation.

Output lands in `out/` as a Markdown primer and an Excel workbook. Curated samples
live in [`examples/`](examples/).

## How it works

A linear LangGraph with two human-review checkpoints:

```
scope -> sector_reader -> comps_spreader -> [review] -> idea_generator -> note_writer -> [review]
```

| Node | Role | Notes |
|---|---|---|
| `scope` | List the ticker universe for the sector | Sonnet |
| `sector_reader` | Search the web, produce structured sourced facts | Tavily search + schema-constrained output |
| `comps_spreader` | Fetch fundamentals, build the Excel comps | tool-using agent; yfinance or MCP |
| `idea_generator` | Long/short idea shortlist | reasons over overview + comps |
| `note_writer` | Assemble the primer, write files | the only node that writes output |
| `review_comps` / `review_note` | Pause for human approval | LangGraph `interrupt()` + checkpointer |

Design properties carried over from the original agent:

- **Three-tier isolation**: a schema-constrained reader, read-only data access for
  comps, and a single write-capable node.
- **Web-sourced facts**: `sector_reader` searches the web via Tavily before producing
  facts, eliminating reliance on LLM memory and reducing hallucination risk.
- **Source quality rules**: the prompt prioritizes institutional sources (IEA, LBNL,
  SEC filings, Goldman Sachs) and rejects blogs and social posts. Each fact must come
  from a single search result to prevent misleading cross-source composites.
- **Guardrail**: `flag_unsourced` tags numeric prose lacking a source with
  `[UNSOURCED]`, a rule enforced in code, not just the prompt.
- **RAG-ready**: supports both classical RAG (one-shot retrieval) and agentic RAG
  (multi-step search with query refinement). Add PDFs to `data/reports/`, run
  `python scripts/build_rag.py`, and the pipeline automatically uses the report
  library before falling back to web search.
- **Verbatim skills**: the `sector-overview`, `comps-analysis`, and `idea-generation`
  methodologies are the original `SKILL.md` files from the Anthropic repo, with a
  per-node environment adaptation note.

## Setup

Requires Python 3.11+.

```bash
python3.11 -m venv .venv && source .venv/bin/activate
pip install langgraph langchain langchain-anthropic langchain-mcp-adapters \
            langchain-tavily langchain-chroma langchain-huggingface \
            pydantic python-dotenv openpyxl yfinance pytest
pip install -e .
```

Create a `.env` file with your API keys:

```dotenv
ANTHROPIC_API_KEY=sk-ant-...
TAVILY_API_KEY=tvly-...
CAPIQ_MCP_URL=
FACTSET_MCP_URL=
```

Get your Tavily key (free, 1000 searches/month) at https://app.tavily.com.

## Run

```bash
python main.py
```

The run pauses twice for review. Type `approve` to continue. Results appear in `out/`.

## Data sources

| Data | Source | Key required |
|---|---|---|
| Sector overview facts | Tavily web search | TAVILY_API_KEY (free tier) |
| Financial fundamentals | Yahoo Finance via yfinance | None |
| Report library (optional) | Local PDFs indexed via Chroma | None |
| Enterprise data (optional) | S&P CapIQ or FactSet MCP | CAPIQ_MCP_URL or FACTSET_MCP_URL |

If you have enterprise subscriptions, set the MCP URLs in `.env` and the pipeline
automatically switches from yfinance to those MCP servers with no code change.

## RAG (optional)

Two modes for searching a local library of institutional reports:

| Mode | How it works | Cost |
|---|---|---|
| Classical | One-shot vector search, returns top-k chunks | Fast, no extra LLM calls |
| Agentic | Agent searches multiple times, refines queries | Slower, extra LLM calls |

To enable:

```bash
# 1. Put PDFs in data/reports/
# 2. Build the index
python scripts/build_rag.py
# 3. Set RAG_MODE in graph.py: "classical" or "agentic"
# 4. Run as usual
python main.py
```

With no documents indexed, the pipeline uses web search only (current default).

## Evaluation

Three layers, from cheapest to most rigorous:

```bash
# Layer 1: deterministic format and structure checks (zero cost)
pytest

# Layer 2: LLM-as-Judge dual scoring with Claude + GPT (requires API keys)
python tests/eval_llm_judge.py

# Layer 3: web-search fact verification (requires TAVILY_API_KEY + OPENAI_API_KEY)
python tests/eval_fact_check.py
```

| Layer | What it checks | Cost |
|---|---|---|
| pytest (24 tests) | Graph structure, guardrail logic, output format, Excel formulas | Free |
| eval_llm_judge.py | Coverage, sourcing, data integrity, analytical quality, actionability | ~$0.10 |
| eval_fact_check.py | Fact accuracy verified against real web search results | ~$0.20 |

## Project layout

```
market_researcher/
  graph.py          # nodes + graph wiring
  state.py          # shared state (TypedDict)
  schemas.py        # structured-output schemas (Pydantic)
  guardrails.py     # flag_unsourced
  rag.py            # classical + agentic RAG interfaces
  mcp_client.py     # data tools: yfinance <-> real MCP auto-switch
  prompt_loader.py  # loads prompts/*.md
  prompts/          # verbatim SKILL.md methodologies
  tools/xlsx.py     # formula-driven comps workbook
main.py             # async entrypoint with interrupt/resume loop
scripts/
  build_rag.py      # index PDFs into Chroma vector database
data/
  reports/          # put institutional PDFs here
  vectordb/         # auto-generated by build_rag.py
tests/
  test_graph.py     # graph compilation + guardrail unit tests
  test_format.py    # output file quality checks
  eval_llm_judge.py # Claude + GPT dual scoring
  eval_fact_check.py # web-search fact verification
examples/           # sample outputs
```

## Credits

Reimplements the Market Researcher agent from Anthropic's
[financial-services](https://github.com/anthropics/financial-services) repository.
The methodology prompts (`SKILL.md`) are from that project.
