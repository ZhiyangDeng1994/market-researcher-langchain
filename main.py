import uuid
from dotenv import load_dotenv
load_dotenv()

from langgraph.types import Command
from market_researcher.graph import build_graph


def main():
    graph = build_graph()
    config = {"configurable": {"thread_id": str(uuid.uuid4())}}
    result = graph.invoke(
        {"sector": "US data-center power", "angle": "supply gap"}, config
    )

    while "__interrupt__" in result:
        prompt = result["__interrupt__"][0].value
        print(f"\n⏸  {prompt}")
        answer = input("> ") or "approve"
        result = graph.invoke(Command(resume=answer), config)

    print("\n✅ Done:", result.get("note_path"))


if __name__ == "__main__":
    main()