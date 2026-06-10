from langgraph.graph import StateGraph, START, END
from .state import ResearchState

def scope(state: ResearchState) -> dict:
    print("-> scope")
    return {"universe": ["NEE", "VST", "CEG"], "review_status": "scoped"}

def sector_reader(state: ResearchState) -> dict:
    print("-> sector_reader")
    return {"overview": {"facts": ["Data center electricity demand is growing rapidly "]}, 
            "landscape": {}
            }

def comps_spreader(state: ResearchState) -> dict:
    print("→ comps_spreader")
    return {"comps": {"rows": "(stub) EV/EBITDA 12-15x"}}

def idea_generator(state: ResearchState) -> dict:
    print("→ idea_generator")
    return {"ideas": [{"ticker": "CEG", "thesis": "(stub)"}]}

def note_writer(state: ResearchState) -> dict:
    print("→ note_writer")
    return {"note_path": "out/primer-stub.md"}

def build_graph():
    g = StateGraph(ResearchState)
    for name, fn in [
        ("scope", scope),
        ("sector_reader", sector_reader),
        ("comps_spreader", comps_spreader),
        ("idea_generator", idea_generator),
        ("note_writer", note_writer),
    ]:
        g.add_node(name, fn)

    g.add_edge(START, "scope")
    g.add_edge("scope", "sector_reader")
    g.add_edge("sector_reader", "comps_spreader")
    g.add_edge("comps_spreader", "idea_generator")
    g.add_edge("idea_generator", "note_writer")
    g.add_edge("note_writer", END)
    return g.compile()