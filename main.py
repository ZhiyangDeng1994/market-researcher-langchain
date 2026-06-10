from dotenv import load_dotenv
load_dotenv()

from market_researcher.graph import build_graph

def main():
    new_graph = build_graph()
    result = new_graph.invoke(
        {"sector": "US data-center power", "angle": "supply gap"}
        )
    print("\nFinal State is:")
    for k, v in result.items():
        print(f"{k}: {v}")
    print(new_graph.get_graph().draw_ascii())


if __name__ == "__main__":
    main()