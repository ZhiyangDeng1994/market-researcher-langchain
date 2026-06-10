"""Data connectors. If CAPIQ_MCP_URL / FACTSET_MCP_URL are set, load real MCP
tools via MultiServerMCPClient; otherwise fall back to a local stub. 
But we use Yahoo Finance as our data source
"""
import os
import yfinance as yf
from langchain_core.tools import tool


@tool
def get_fundamentals(tickers: list[str]) -> dict:
    """Return EV, EBITDA, price, and EPS for the given tickers (Yahoo Finance)."""
    out = {}
    for t in tickers:
        info = yf.Ticker(t).info
        out[t] = {
            "ev": round((info.get("enterpriseValue") or 0) / 1e6, 0),   # $mm
            "ebitda": round((info.get("ebitda") or 0) / 1e6, 1),        # $mm
            "price": info.get("currentPrice") or 0,
            "eps": info.get("trailingEps") or 0,
            "source": f"Yahoo Finance ({t}), retrieved via yfinance",
        }
    return out


async def get_market_data_tools():
    servers = {}
    if os.getenv("CAPIQ_MCP_URL"):
        servers["capiq"] = {"url": os.environ["CAPIQ_MCP_URL"], "transport": "streamable_http"}
    if os.getenv("FACTSET_MCP_URL"):
        servers["factset"] = {"url": os.environ["FACTSET_MCP_URL"], "transport": "streamable_http"}

    if not servers:
        return [get_fundamentals]            # stub mode

    from langchain_mcp_adapters.client import MultiServerMCPClient
    client = MultiServerMCPClient(servers)
    return await client.get_tools()          # real MCP mode