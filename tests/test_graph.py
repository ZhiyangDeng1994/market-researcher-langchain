from market_researcher.graph import build_graph
from market_researcher.guardrails import flag_unsourced


def test_graph_compiles():
    assert build_graph() is not None


def test_all_nodes_present():
    nodes = build_graph().get_graph().nodes
    for name in [
        "scope", "sector_reader", "comps_spreader",
        "review_comps", "idea_generator", "note_writer", "review_note",
    ]:
        assert name in nodes


def test_guardrail_flags_unsourced_number():
    out = flag_unsourced("Demand will reach 40 GW by 2030.")
    assert "[UNSOURCED]" in out


def test_guardrail_passes_when_sourced():
    out = flag_unsourced("Demand will reach 40 GW by 2030. — *Goldman Sachs, 2024*")
    assert "[UNSOURCED]" not in out


def test_guardrail_skips_table_rows():
    out = flag_unsourced("| VST | Merchant Power | 12.5x | 20.1x |")
    assert "[UNSOURCED]" not in out