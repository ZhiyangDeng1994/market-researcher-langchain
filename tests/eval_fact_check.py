"""Fact-checker: sample 3 Overview facts and ask GPT to verify each.
Cross-model verification (Claude generates, GPT checks) reduces same-family bias.

Run:  python tests/eval_fact_check.py
Requires: OPENAI_API_KEY in .env
"""
import json
import random
import re
from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI


# -- Load primer from manifest --

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "out" / "manifest.json"

assert MANIFEST.exists(), "out/manifest.json not found -- run `python main.py` first"
manifest = json.loads(MANIFEST.read_text())

primer_path = ROOT / manifest["primer"]
assert primer_path.exists(), f"Primer not found: {primer_path}"
PRIMER = primer_path.read_text(encoding="utf-8")


# -- Extract Overview facts --

overview = PRIMER.split("## Overview")[1].split("## Comps")[0]
facts = [l.strip() for l in overview.splitlines() if l.strip().startswith("- ")]
assert facts, "No facts found in Overview"

SAMPLE_SIZE = max(1, int(len(facts) * 0.9))
sample = random.sample(facts, SAMPLE_SIZE)


# -- Fact-check prompt --

PROMPT = """You are a financial research fact-checker. Your job is to verify the
following claim that appears in an AI-generated sector primer.

Evaluate these 4 dimensions:

1. SOURCE_EXISTS -- Is the cited source a real, identifiable publication or dataset?
   (e.g., "Lawrence Berkeley National Laboratory, 2024" -- does LBNL publish such reports?)

2. NUMBER_ACCURATE -- Is the specific number roughly correct (within ~20% of the
   real figure)? If you are not sure, say "uncertain" rather than guessing.

3. DATE_CURRENT -- Is the data point reasonably current, or is it outdated/superseded
   by newer data?

4. MISLEADING -- Is the claim misleading in context, even if technically true?
   (e.g., cherry-picked, conflating different metrics, missing crucial caveats)

Respond with ONLY this JSON (no markdown fences, no preamble):
{{
  "source_exists":    {{"verdict": "yes/no/uncertain", "note": "..."}},
  "number_accurate":  {{"verdict": "yes/no/uncertain", "note": "..."}},
  "date_current":     {{"verdict": "yes/no/uncertain", "note": "..."}},
  "misleading":       {{"verdict": "yes/no/uncertain", "note": "..."}},
  "overall_verdict":  "verified/likely_accurate/uncertain/likely_inaccurate/false",
  "confidence":       "high/medium/low"
}}

Claim to verify:
{claim}
"""


def parse_response(raw_text: str) -> dict:
    text = raw_text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1]
        text = text.rsplit("```", 1)[0]
    return json.loads(text.strip())


def verdict_tag(v: str) -> str:
    return {
        "yes": "[OK]", "no": "[FAIL]", "uncertain": "[?]",
        "verified": "[OK]", "likely_accurate": "[OK]",
        "likely_inaccurate": "[WARN]", "false": "[FAIL]",
    }.get(v.lower(), "[?]")


def run_fact_check():
    llm = ChatOpenAI(model="gpt-5.4")
    results = []

    print(f"\n>> Sampling {SAMPLE_SIZE} facts from Overview ({len(facts)} total)\n")

    for i, fact in enumerate(sample, 1):
        source_match = re.search(r"-- \*(.+?)\*", fact)
        if not source_match:
            source_match = re.search(r"— \*(.+?)\*", fact)
        source = source_match.group(1) if source_match else "(no source found)"
        claim_short = fact[:100].replace("- ", "") + "..."

        print(f"{'=' * 60}")
        print(f"  Fact {i}/{SAMPLE_SIZE}")
        print(f"  Claim:  {claim_short}")
        print(f"  Source: {source}")
        print(f"{'=' * 60}")

        try:
            raw = llm.invoke([
                {"role": "user", "content": PROMPT.format(claim=fact)},
            ])
            scores = parse_response(raw.content)
            results.append({"fact": fact, "source": source, "scores": scores})

            dims = ["source_exists", "number_accurate", "date_current", "misleading"]
            for dim in dims:
                s = scores[dim]
                if dim == "misleading":
                    if s["verdict"] == "no":
                        tag = "[OK]"
                        label = "NOT misleading"
                    elif s["verdict"] == "yes":
                        tag = "[FAIL]"
                        label = "misleading"
                    else:
                        tag = "[?]"
                        label = "misleading?"
                else:
                    tag = verdict_tag(s["verdict"])
                    label = dim
                print(f"    {tag:8s} {label:20s} -- {s['note']}")

            v = scores["overall_verdict"]
            c = scores["confidence"]
            print(f"\n    Overall: {verdict_tag(v)} {v} (confidence: {c})")

        except Exception as e:
            print(f"    ERROR: {e}")
            results.append({"fact": fact, "source": source, "scores": None})

        print()

    # -- Summary table --

    print(f"{'=' * 60}")
    print("  SUMMARY")
    print(f"{'=' * 60}")

    verified = 0
    uncertain = 0
    flagged = 0

    for r in results:
        if r["scores"] is None:
            flagged += 1
            continue
        v = r["scores"]["overall_verdict"].lower()
        if v in ("verified", "likely_accurate"):
            verified += 1
        elif v == "uncertain":
            uncertain += 1
        else:
            flagged += 1

    total = len(results)
    print(f"  [OK]   Verified / likely accurate:  {verified}/{total}")
    print(f"  [?]    Uncertain:                   {uncertain}/{total}")
    print(f"  [FAIL] Flagged / inaccurate:        {flagged}/{total}")

    if verified == total:
        print("\n  >> All sampled facts check out!")
    elif flagged > 0:
        print("\n  [!] Some facts flagged -- review the claims above.")
        print("      (Remember: the checker itself can be wrong. Cross-check manually.)")
    else:
        print("\n  >> Some uncertain results -- consider manual verification.")

    # -- Hallucination rate estimate --

    print(f"\n  Estimated hallucination rate: ~{flagged}/{total} sampled")
    print(f"  (Based on {SAMPLE_SIZE} random samples from {len(facts)} total facts)")

    # -- Save results --

    out_path = ROOT / "out" / "eval_fact_check.json"
    out_path.write_text(
        json.dumps(results, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"\n  Results saved to {out_path}")

    return results


if __name__ == "__main__":
    run_fact_check()