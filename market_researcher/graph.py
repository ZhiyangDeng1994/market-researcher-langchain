from pathlib import Path
from .guardrails import flag_unsourced
from langgraph.graph import StateGraph, START, END
from langchain_anthropic import ChatAnthropic
from langchain.agents import create_agent
from langgraph.types import interrupt
from langgraph.checkpoint.memory import MemorySaver
from .state import ResearchState
from .prompt_loader import load_prompt
from .schemas import SectorReaderOutput
from .schemas import CompsTable
from .mcp_client import get_market_data_tools
from .tools.xlsx import build_comps_xlsx

SMART_MODEL = "claude-opus-4-8"
FAST_MODEL = "claude-sonnet-4-6"


def scope(state: ResearchState) -> dict:
    #print("-> scope")
    #return {"universe": ["NEE", "VST", "CEG"], "review_status": "scoped"}
    llm = ChatAnthropic(model=FAST_MODEL)
    message = llm.invoke([
        {"role": "system", "content": "You are a research assistant. "
        "Given a sector or theme, list 8-12 public-company tickers that best represent it. "
        "Return only the tickers, comma-separated, nothing else."},
        {"role": "user", "content": f"Sector: {state['sector']}; angle: {state.get('angle','')}"},
    ]).content

    tickers = [t.strip() for t in message.replace("\n", ",").split(",") if t.strip()]
    return {"universe": tickers, "review_status": "scoped"}

def sector_reader(state: ResearchState) -> dict:
    # print("-> sector_reader")
    # return {"overview": {"facts": ["Data center electricity demand is growing rapidly "]}, 
    #         "landscape": {}
    #         }
    llm = ChatAnthropic(model=SMART_MODEL).with_structured_output(SectorReaderOutput)
    system = (
        "You are producing a structured sector overview RIGHT NOW, headless, from your"
        " own knowledge. You CANNOT ask scoping questions and CANNOT produce Word/PPT/Excel."
        " Your only output is the schema: the sector name plus 8-15 concrete facts, each a"
        " specific claim with its best-known source, covering market size & growth, industry"
        " structure, key trends/drivers, and supply-demand dynamics. Use the methodology"
        " below only as a guide for WHAT to cover — ignore its scoping/workflow/document steps."
        " Every fact needs a source; omit any fact you cannot source.\n\n"
        "--- METHODOLOGY (reference only) ---\n"
        + load_prompt("sector_overview")
    )
    result = llm.invoke([
        {"role": "system", "content": system},
        {"role": "user", "content":
            f"Produce the sector overview for {state['sector']} (angle: {state.get('angle','')})."
            " Return 8-15 sourced facts now."},
    ])
    print("→ sector_reader |", len(result.facts), "facts")
    return {"overview": result.model_dump()}

# def comps_spreader(state: ResearchState) -> dict:
#     # print("→ comps_spreader")
#     # return {"comps": {"rows": "(stub) EV/EBITDA 12-15x"}}
#     print("→ comps_spreader")
#     tools = get_market_data_tools()
#     agent = create_agent(ChatAnthropic(model=FAST_MODEL), tools)
#     system = load_prompt("comps_analysis") + "\nUse only the provided data tools; never invent numbers."

#     res = agent.invoke({"messages": [
#         {"role": "system", "content": system},
#         {"role": "user", "content": f"Spread comps for: {state.get('universe')}"},
#     ]})
#     return {"comps": {"summary": res["messages"][-1].content}}
async def comps_spreader(state: ResearchState) -> dict:
    print("→ comps_spreader")
    tools = await get_market_data_tools()
    system = (
        load_prompt("comps_analysis")
        + "\n\nENVIRONMENT ADAPTATION (overrides anything conflicting above):"
        + " You are running headless inside a pipeline. You CANNOT build Excel"
        + " yourself and CANNOT ask the user questions — ignore the Office JS /"
        + " openpyxl / step-by-step user verification instructions. Your only job:"
        + " fetch raw inputs (EV, EBITDA, price, EPS) for every ticker using the"
        + " provided data tools, then return them as structured rows with sources."
        + " Never invent numbers."
    )
    agent = create_agent(
        model=ChatAnthropic(model=FAST_MODEL),
        tools=tools,
        system_prompt=system,
        response_format=CompsTable,
    )
    res = await agent.ainvoke({"messages": [
        {"role": "user", "content": f"Get fundamentals for: {state.get('universe')}"},
    ]})
    table: CompsTable = res["structured_response"]

    xlsx_path = build_comps_xlsx(table.rows, state.get("sector", "sector"))

    md = ["| Ticker | EV ($mm) | EBITDA | Price | EPS |", "|---|---|---|---|---|"]
    md += [f"| {r.ticker} | {r.ev:,.0f} | {r.ebitda:,.1f} | {r.price:.2f} | {r.eps:.2f} |"
           for r in table.rows]
    md.append(f"\nWorkbook with formula-driven multiples: `{xlsx_path}`")

    return {"comps": {"rows": [r.model_dump() for r in table.rows],
                      "summary": "\n".join(md)},
            "comps_xlsx": xlsx_path}

def idea_generator(state: ResearchState) -> dict:
    # print("→ idea_generator")
    # return {"ideas": [{"ticker": "CEG", "thesis": "(stub)"}]}
    print("→ idea_generator")
    llm = ChatAnthropic(model=FAST_MODEL)
    system = load_prompt("idea_generation") + "\nGive 3-5 thesis points plus key risks per name. Max 5 names."
    message = llm.invoke([
        {"role": "system", "content": system},
        {"role": "user", "content": f"Overview: {state.get('overview')}\nComps: {state.get('comps')}\nGive a shortlist."},
    ])
    return {"ideas": [{"writeup": message.content}]}

def note_writer(state: ResearchState) -> dict:
    print("→ note_writer")
    sector = state.get("sector", "sector")

    overview = state.get("overview", {})
    facts = overview.get("facts", []) if isinstance(overview, dict) else []
    fact_lines = [f"- {f['claim']} — *{f['source']}*" for f in facts]

    comps = state.get("comps", {})
    comps_md = comps.get("summary", "") if isinstance(comps, dict) else str(comps)

    ideas = state.get("ideas", [])
    ideas_md = ideas[0].get("writeup", "") if ideas and isinstance(ideas[0], dict) else str(ideas)

    parts = [
        f"# {sector} — primer",
        "",
        "## Overview",
        *fact_lines,
        "",
        "## Comps",
        comps_md,
        "",
        "## Ideas",
        ideas_md,
    ]

    out = Path("out")
    out.mkdir(exist_ok=True)
    fname = f"primer-{sector[:24].replace(' ', '-')}.md"
    path = out / fname
    body = flag_unsourced("\n".join(parts))
    path.write_text(body, encoding="utf-8")
    return {"note_path": str(path)}

def review_comps(state: ResearchState) -> dict:
    decision = interrupt("Comps spread is ready. Type 'approve' to continue to idea generation.")
    return {"review_status": f"comps:{decision}"}

def review_note(state: ResearchState) -> dict:
    decision = interrupt(f"Draft written to {state.get('note_path')}. Type 'approve' to finish.")
    return {"review_status": f"note:{decision}"}

def build_graph():
    g = StateGraph(ResearchState)
    for name, fn in [
        ("scope", scope),
        ("sector_reader", sector_reader),
        ("comps_spreader", comps_spreader),
        ("review_comps", review_comps),
        ("idea_generator", idea_generator),
        ("note_writer", note_writer),
        ("review_note", review_note),
    ]:
        g.add_node(name, fn)

    g.add_edge(START, "scope")
    g.add_edge("scope", "sector_reader")
    g.add_edge("sector_reader", "comps_spreader")
    g.add_edge("comps_spreader", "review_comps")
    g.add_edge("review_comps", "idea_generator")
    g.add_edge("idea_generator", "note_writer")
    g.add_edge("note_writer", "review_note")
    g.add_edge("review_note", END)
    return g.compile(checkpointer=MemorySaver())