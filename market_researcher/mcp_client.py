from langchain_core.tools import tool

@tool
def get_multiples(tickers: list[str]) -> dict:
    """(dev stub) Return EV/EBITDA and P/E multiples for the given tickers."""
    return {t: {"ev_ebitda": 12.5, "pe": 20.1} for t in tickers}


def get_market_data_tools():
    # No MCP credentials yet → use the local stub so the pipeline runs.
    # Later (with real CapIQ/FactSet), connect via MultiServerMCPClient instead.
    return [get_multiples]