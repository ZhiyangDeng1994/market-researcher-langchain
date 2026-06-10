# Market Researcher (LangGraph)

A runnable reimplementation of Anthropic's **Market Researcher** agent, built as a
stateful [LangGraph](https://github.com/langchain-ai/langgraph) pipeline. Given a
sector, it produces an equity-research **primer**: a sourced market overview, a peer
comparable-company table (with a formula-driven Excel workbook), and a long/short
idea shortlist.

> ⚠️ **Not investment advice.** Outputs are AI-generated and built on free,
> best-effort data (Yahoo Finance). Verify every figure before relying on it.

## What it does

Running the agent for a sector (e.g. *US data-center power*) generates:

- **Overview** — 8–15 key facts on market size, structure, trends, and supply/demand,
  each with a source.
- **Comps** — a peer valuation table from live market data, plus `out/comps.xlsx`
  where every multiple is an Excel **formula** (`=B5/C5`) and every input cell carries
  a **source comment**.
- **Ideas** — a long/short shortlist with thesis, risks, and peer-relative valuation.

Output lands in `out/` as a Markdown primer + an Excel workbook. Curated samples live
in [`examples/`](examples/).

## How it works

A linear LangGraph with two human-review checkpoints:

```
scope -> sector_reader -> comps_spreader -> [review] -> idea_generator -> note_writer -> [review]
```

| Node | Role | Notes |
|---|---|---|
| `scope` | List the ticker universe for the sector | |
| `sector_reader` | Produce structured, sourced facts | schema-constrained, **no tools** (untrusted-reader isolation) |
| `comps_spreader` | Fetch fundamentals, build the Excel comps | tool-using agent; **read-only** data access |
| `idea_generator` | Long/short idea shortlist | reasons over overview + comps |
| `note_writer` | Assemble the primer, write files | the **only** node that writes output |
| `review_comps` / `review_note` | Pause for human approval | LangGraph `interrupt()` + checkpointer |

Reasoning-heavy nodes (`sector_reader`, `idea_generator`) use Claude Opus; lighter
nodes use Claude Sonnet, via the Anthropic API.

Design properties carried over from the original agent:

- **Three-tier isolation** — a schema-constrained reader (no tools), read-only data
  access for comps, and a single write-capable node.
- **Guardrail** — `flag_unsourced` tags numeric prose lacking a source with
  `[UNSOURCED]`; a rule enforced in code, not just the prompt.
- **Verbatim skills** — the `sector-overview`, `comps-analysis`, and `idea-generation`
  methodologies are the original `SKILL.md` files, with a small per-node note adapting
  them to a headless pipeline.

## Setup

Requires Python 3.11+.

```bash
python3.11 -m venv .venv && source .venv/bin/activate
pip install langgraph langchain langchain-anthropic langchain-mcp-adapters \
            pydantic python-dotenv openpyxl yfinance pytest
pip install -e .
```

Add your Anthropic API key to a `.env` file:

```dotenv
ANTHROPIC_API_KEY=sk-ant-...
CAPIQ_MCP_URL=
FACTSET_MCP_URL=
```

## Run

```bash
python main.py
```

The run pauses twice for review — type `approve` to continue. Results appear in `out/`.

## Data sources

By default, fundamentals come from **Yahoo Finance** (free, no key). If you have
enterprise subscriptions, set `CAPIQ_MCP_URL` / `FACTSET_MCP_URL` in `.env` and the
pipeline automatically switches to those MCP servers — no code change required.

## Tests

```bash
pytest
```

Covers graph compilation, node presence, and guardrail behavior — fast, deterministic,
and no API calls.

## Project layout

```
market_researcher/
  graph.py          # nodes + graph wiring
  state.py          # shared state (TypedDict)
  schemas.py        # structured-output schemas (Pydantic)
  guardrails.py     # flag_unsourced
  mcp_client.py     # data tools: yfinance stub <-> real MCP auto-switch
  prompt_loader.py  # loads prompts/*.md
  prompts/          # verbatim SKILL.md methodologies
  tools/xlsx.py     # formula-driven comps workbook
main.py             # async entrypoint (interrupt / resume loop)
tests/
examples/           # sample outputs
```

## Credits

Reimplements the Market Researcher agent from Anthropic's
[financial-services](https://github.com/anthropics/financial-services) repository.
The methodology prompts (`SKILL.md`) are from that project.
