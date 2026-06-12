"""LLM-as-Judge: dual evaluation of the generated primer.
Two independent models (Claude + GPT) score the output on 5 dimensions,
then results are shown side-by-side so disagreements are visible.

Requires: ANTHROPIC_API_KEY and OPENAI_API_KEY in .env
"""
import json
from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI


# ── Load primer from manifest ──

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "out" / "manifest.json"

assert MANIFEST.exists(), "out/manifest.json not found — run `python main.py` first"
manifest = json.loads(MANIFEST.read_text())

primer_path = ROOT / manifest["primer"]
assert primer_path.exists(), f"Primer not found: {primer_path}"
PRIMER = primer_path.read_text(encoding="utf-8")


# ── Rubric ──

RUBRIC = """You are a senior equity research analyst evaluating an AI-generated sector primer.

Score each dimension from 1 to 5 and give a one-line justification.

Scoring guide:
  1 = Unacceptable (missing or fundamentally broken)
  2 = Poor (major gaps or errors)
  3 = Adequate (covers basics, some issues)
  4 = Good (solid work, minor gaps)
  5 = Excellent (institutional quality)

Dimensions:

1. COVERAGE — Does the Overview cover market size, growth drivers, supply/demand
   dynamics, key players, and regulatory context? Missing major dimensions = 1-2.

2. SOURCING — Are claims attributed to specific, plausible sources? Are sources
   varied (not all from one provider)? Unsourced quantitative claims = 1.

3. DATA_INTEGRITY — Do the Comps numbers look plausible for these tickers?
   Are there obvious errors (negative EV for a profitable company, P/E of 1000x
   without explanation, uniform/stub data)? Uniform stub data = 1.

4. ANALYTICAL_QUALITY — Do the Ideas have clear theses, differentiated reasoning,
   and identified risks? Is the peer-relative valuation logic sound?

5. ACTIONABILITY — Could a junior analyst use this primer as a starting point
   for real work? Are next steps identified?

Respond with ONLY this JSON (no markdown fences, no preamble):
{
  "coverage":           {"score": N, "note": "..."},
  "sourcing":           {"score": N, "note": "..."},
  "data_integrity":     {"score": N, "note": "..."},
  "analytical_quality": {"score": N, "note": "..."},
  "actionability":      {"score": N, "note": "..."},
  "overall":            N,
  "summary":            "..."
}
"""


# ── Judges ──

JUDGES = {
    "Claude": ChatAnthropic(model="claude-opus-4-8"),
    "GPT": ChatOpenAI(model="gpt-5.4"),
}

DIMS = ["coverage", "sourcing", "data_integrity", "analytical_quality", "actionability"]


def parse_scores(raw_text: str) -> dict:
    """Extract JSON from model response, handling markdown fences."""
    text = raw_text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1]  # drop ```json line
        text = text.rsplit("```", 1)[0]  # drop closing ```
    return json.loads(text.strip())


def run_eval():
    results = {}

    for name, llm in JUDGES.items():
        print(f"\n{'=' * 25} {name} {'=' * 25}")
        try:
            raw = llm.invoke([
                {"role": "system", "content": RUBRIC},
                {"role": "user", "content": f"Evaluate this primer:\n\n{PRIMER}"},
            ])
            scores = parse_scores(raw.content)
            results[name] = scores

            for dim in DIMS:
                s = scores[dim]
                print(f"  {dim:22s}  {s['score']}/5  — {s['note']}")
            print(f"  {'OVERALL':22s}  {scores['overall']}/5")
            print(f"  Summary: {scores['summary']}")

        except Exception as e:
            print(f"  ERROR: {e}")
            results[name] = None

    # ── Side-by-side comparison ──

    valid = {k: v for k, v in results.items() if v is not None}
    if len(valid) < 2:
        print("\nNeed both judges to compare. Check API keys.")
        return results

    print(f"\n{'=' * 25} COMPARISON {'=' * 25}")
    print(f"  {'Dimension':22s}  {'Claude':>8s}  {'GPT':>8s}  {'Delta':>8s}")
    print(f"  {'-' * 22}  {'-' * 8}  {'-' * 8}  {'-' * 8}")

    for dim in DIMS:
        c = results["Claude"][dim]["score"]
        g = results["GPT"][dim]["score"]
        flag = "  [WARN]" if abs(c - g) >= 2 else ""
        print(f"  {dim:22s}  {c:>6}/5  {g:>6}/5  {g - c:>+6d}{flag}")

    c_all = results["Claude"]["overall"]
    g_all = results["GPT"]["overall"]
    flag = "  [WARN]" if abs(c_all - g_all) >= 2 else ""
    print(f"  {'OVERALL':22s}  {c_all:>6}/5  {g_all:>6}/5  {g_all - c_all:>+6d}{flag}")

    # ── Disagreement analysis ──

    disagreements = []
    for dim in DIMS:
        c = results["Claude"][dim]
        g = results["GPT"][dim]
        if abs(c["score"] - g["score"]) >= 2:
            disagreements.append((dim, c, g))

    if disagreements:
        print(f"\n{'=' * 25} DISAGREEMENTS (delta >= 2) {'=' * 25}")
        for dim, c, g in disagreements:
            print(f"\n  {dim}:")
            print(f"    Claude ({c['score']}/5): {c['note']}")
            print(f"    GPT ({g['score']}/5): {g['note']}")
    else:
        print("\n  [OK] No major disagreements (all deltas < 2)")

    # ── Save results ──

    out_path = ROOT / "out" / "eval_llm_as_judge.json"
    out_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\n  Scores saved to {out_path}")

    return results


if __name__ == "__main__":
    run_eval()