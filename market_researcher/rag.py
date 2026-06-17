"""RAG module: provides both Classical and Agentic retrieval interfaces.
Classical RAG: one-shot retrieve -> return chunks (fast, cheap)
Agentic RAG:  agent-controlled multi-step search with query refinement (flexible, costly)
If no vector database exists, both return None -> sector_reader falls back to web-only.
"""
from pathlib import Path
from langchain_core.tools import tool
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

VECTORDB_DIR = Path("data/vectordb")


def _load_retriever(k: int = 5):
    """Load Chroma retriever if the vector DB exists, else return None."""
    if not VECTORDB_DIR.exists() or not any(VECTORDB_DIR.iterdir()):
        return None
    try:
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        db = Chroma(
            persist_directory=str(VECTORDB_DIR),
            embedding_function=embeddings,
        )
        return db.as_retriever(search_kwargs={"k": k})
    except Exception as e:
        print(f"  [RAG] Failed to load vector DB: {e}")
        return None


# ═══════════════════════════════════════════
#  Classical RAG
# ═══════════════════════════════════════════
#  Flow:  query -> vector search -> return top-k chunks as text

def get_classical_rag_tool(k: int = 5):
    """Return a simple retrieval tool, or None if no vector DB."""
    retriever = _load_retriever(k)
    if retriever is None:
        return None

    @tool
    def search_reports(query: str) -> str:
        """[Classical RAG] Search the curated report library.
        Returns the top-k most relevant chunks from indexed institutional reports.
        Use this BEFORE web search for higher-quality sourcing."""
        results = retriever.invoke(query)
        if not results:
            return "No relevant results found in report library."
        return "\n\n---\n\n".join(
            f"[Source: {r.metadata.get('source', 'unknown')}, "
            f"page {r.metadata.get('page', '?')}]\n{r.page_content}"
            for r in results
        )

    return search_reports


# ═══════════════════════════════════════════
#  Agentic RAG
# ═══════════════════════════════════════════
#  Flow:  agent gets retrieval tool -> searches -> reads -> decides
#         "not enough" -> refines query -> searches again -> ... -> returns

def get_agentic_rag_tool(llm=None):
    """Return an agent-as-tool that can search the report library multiple times
    with query refinement. Returns None if no vector DB or no LLM provided."""
    retriever = _load_retriever(k=3)
    if retriever is None or llm is None:
        return None

    # The inner retrieval tool (used by the agent internally)
    @tool
    def _retrieve(query: str) -> str:
        """Search the report library for a specific query."""
        results = retriever.invoke(query)
        if not results:
            return "No results found. Try a different query."
        return "\n\n---\n\n".join(
            f"[Source: {r.metadata.get('source', 'unknown')}, "
            f"page {r.metadata.get('page', '?')}]\n{r.page_content}"
            for r in results
        )

    try:
        from langchain.agents import create_agent

        rag_agent = create_agent(
            model=llm,
            tools=[_retrieve],
            system_prompt=(
                "You are a research retrieval agent. You have a tool that searches"
                " a library of institutional reports (IEA, LBNL, SEC filings, etc.)."
                "\n\nYour workflow:"
                "\n1. Search for the requested information"
                "\n2. Read the results — if they don't answer the question, refine"
                "   your query and search again (up to 3 attempts)"
                "\n3. Return a concise summary of what you found, with source citations"
                "\n4. If nothing relevant is found after 3 attempts, say so clearly"
                "\n\nAlways cite the source file and page number from the results."
            ),
        )

        @tool
        async def search_reports_deep(query: str) -> str:
            """[Agentic RAG] Deep search of the report library with query refinement.
            An AI agent searches multiple times, refining queries to find the best data.
            Use for complex or multi-faceted questions."""
            res = await rag_agent.ainvoke(
                {"messages": [{"role": "user", "content": query}]},
                {"recursion_limit": 10},
            )
            return res["messages"][-1].content

        return search_reports_deep

    except Exception as e:
        print(f"  [Agentic RAG] Failed to create agent: {e}")
        return None

def get_rag_tools(llm=None):
    """Return a dict of available RAG tools.

    Returns:
        {"classical": tool_or_None, "agentic": tool_or_None}
    """
    return {
        "classical": get_classical_rag_tool(),
        "agentic": get_agentic_rag_tool(llm),
    }