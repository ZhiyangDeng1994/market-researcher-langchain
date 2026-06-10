from typing import TypedDict

class ResearchState(TypedDict, total=False):
    """"
    The state of the market researcher agent.
    """
    #----- Inputs -----#
    sector: str
    angle: str
    universe: list[str]
    #----- Artifacts produced by each node -----#
    overview: dict
    landscape: dict
    comps: dict
    ideas: list
    note_path: str
    #----- Control flow -----#
    review_status: str
    mode: str



