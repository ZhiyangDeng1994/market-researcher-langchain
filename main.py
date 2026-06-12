import asyncio
import uuid
from dotenv import load_dotenv
load_dotenv()

from langgraph.types import Command
from market_researcher.graph import build_graph


async def main():
    graph = build_graph()
    config = {"configurable": {"thread_id": str(uuid.uuid4())}}
    result = await graph.ainvoke(
        {"sector": "US data-center power", "angle": "supply gap"}, config
    )

    while "__interrupt__" in result:
        prompt = result["__interrupt__"][0].value
        print(f"\n⏸  {prompt}")
        answer = input("> ") or "approve"
        result = await graph.ainvoke(Command(resume=answer), config)

    print("\n[OK] Done:", result.get("note_path"), "|", result.get("comps_xlsx"))


if __name__ == "__main__":
    asyncio.run(main())