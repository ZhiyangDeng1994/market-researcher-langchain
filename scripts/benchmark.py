"""Benchmark: run the pipeline across 20 sectors, collect absolute metrics.

Measures: wall-clock time, schema validity, format test pass rate,
fact-check verified rate.

Usage:  python scripts/benchmark.py
Results saved to out/benchmark_results.json
"""
import asyncio
import json
import subprocess
import sys
import time
import uuid
from pathlib import Path

from dotenv import load_dotenv
load_dotenv()

from langgraph.types import Command
from market_researcher.graph import build_graph


# ── 20 sectors across different industries ──

TASKS = [
    # Energy & Utilities
    ("US data-center power", "supply gap"),
    ("US residential solar", "policy and rate risk"),
    ("global LNG", "supply chain bottlenecks"),
    ("US nuclear power", "SMR commercialization"),
    ("US electric utilities", "grid modernization"),
    # Technology
    ("US semiconductors", "reshoring and CHIPS Act"),
    ("US cloud computing", "hyperscaler capex cycle"),
    ("US cybersecurity", "AI-driven threat landscape"),
    ("global AI chips", "GPU supply constraints"),
    # Healthcare
    ("US healthcare IT", "AI adoption"),
    ("US biotech", "GLP-1 obesity drugs"),
    ("US medical devices", "robotic surgery adoption"),
    # Industrials
    ("US defense and aerospace", "defense budget growth"),
    ("US industrial automation", "reshoring driven demand"),
    ("global shipping and logistics", "container rate normalization"),
    # Financials
    ("US regional banks", "commercial real estate exposure"),
    ("US fintech payments", "embedded finance growth"),
    # Consumer
    ("US quick-service restaurants", "margin pressure and automation"),
    ("US e-commerce", "logistics and fulfillment cost"),
    # Real Estate / Infrastructure
    ("US data center REITs", "supply demand imbalance"),
]

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "out"


async def run_single(sector: str, angle: str, run_id: int) -> dict:
    """Run one full pipeline with auto-approve."""
    graph = build_graph()
    config = {"configurable": {"thread_id": f"bench-{run_id}-{uuid.uuid4().hex[:8]}"}}

    record = {
        "run_id": run_id,
        "sector": sector,
        "angle": angle,
        "schema_valid": True,
        "error": None,
        "error_type": None,
        "wall_clock_seconds": 0,
        "format_tests_passed": 0,
        "format_tests_total": 0,
        "fact_check_verified": 0,
        "fact_check_total": 0,
        "fact_check_rate": 0.0,
    }

    start = time.time()

    try:
        result = await graph.ainvoke(
            {"sector": sector, "angle": angle}, config
        )

        while "__interrupt__" in result:
            result = await graph.ainvoke(Command(resume="approve"), config)

        record["note_path"] = result.get("note_path", "")
        record["comps_xlsx"] = result.get("comps_xlsx", "")

    except Exception as e:
        record["schema_valid"] = False
        record["error"] = str(e)[:200]
        if "ValidationError" in str(e):
            record["error_type"] = "schema_validation"
        elif "credit balance" in str(e).lower() or "rate limit" in str(e).lower():
            record["error_type"] = "api_limit"
        else:
            record["error_type"] = "runtime"

    record["wall_clock_seconds"] = round(time.time() - start, 1)
    return record


def run_format_tests() -> tuple[int, int]:
    """Run pytest on test_format.py, return (passed, total)."""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "tests/test_format.py", "-q", "--tb=no"],
            capture_output=True, text=True, cwd=str(ROOT),
        )
        output = result.stdout
        passed = 0
        total = 0
        for line in output.splitlines():
            if "passed" in line:
                parts = line.split()
                for i, p in enumerate(parts):
                    if p == "passed" and i > 0:
                        passed = int(parts[i - 1])
                    if p == "failed" and i > 0:
                        total += int(parts[i - 1])
                total += passed
                break
        return passed, total
    except Exception:
        return 0, 0


def run_fact_check() -> tuple[int, int]:
    """Run fact check, return (verified, total)."""
    try:
        subprocess.run(
            [sys.executable, "tests/eval_fact_check.py"],
            capture_output=True, text=True, cwd=str(ROOT),
        )
        fc_path = OUT / "eval_fact_check.json"
        if fc_path.exists():
            data = json.loads(fc_path.read_text())
            total = len(data)
            verified = sum(
                1 for r in data
                if r.get("scores", {}).get("overall_verdict", "").lower()
                in ("verified", "likely_accurate")
            )
            return verified, total
    except Exception:
        pass
    return 0, 0


async def main():
    all_results = []
    n_runs = len(TASKS)

    print(f"\n{'=' * 60}")
    print(f"  BENCHMARK: {n_runs} sectors")
    print(f"{'=' * 60}\n")

    for i, (sector, angle) in enumerate(TASKS, 1):
        print(f"[{i}/{n_runs}] {sector} ({angle})")
        print(f"  Running pipeline...", end=" ", flush=True)

        record = await run_single(sector, angle, i)

        if record["error"]:
            print(f"ERROR: {record['error'][:80]}")
            # Stop early if API credits ran out
            if record["error_type"] == "api_limit":
                print("\n  API limit hit. Stopping benchmark early.")
                all_results.append(record)
                break
        else:
            print(f"done in {record['wall_clock_seconds']}s")

            print(f"  Running format tests...", end=" ", flush=True)
            passed, total = run_format_tests()
            record["format_tests_passed"] = passed
            record["format_tests_total"] = total
            print(f"{passed}/{total} passed")

            print(f"  Running fact check...", end=" ", flush=True)
            verified, fc_total = run_fact_check()
            record["fact_check_verified"] = verified
            record["fact_check_total"] = fc_total
            record["fact_check_rate"] = round(verified / fc_total, 2) if fc_total > 0 else 0
            print(f"{verified}/{fc_total} verified")

        all_results.append(record)
        print()

    # ── Summary ──

    successful = [r for r in all_results if r["error"] is None]
    failed = [r for r in all_results if r["error"] is not None]

    print(f"{'=' * 60}")
    print(f"  SUMMARY ({len(all_results)} runs)")
    print(f"{'=' * 60}")

    print(f"\n  Completed: {len(successful)}/{len(all_results)}")

    if successful:
        times = [r["wall_clock_seconds"] for r in successful]
        print(f"\n  Wall-clock time (excluding HITL waits):")
        print(f"    Mean:   {sum(times)/len(times):.0f}s ({sum(times)/len(times)/60:.1f} min)")
        print(f"    Min:    {min(times):.0f}s")
        print(f"    Max:    {max(times):.0f}s")
        print(f"    Total:  {sum(times):.0f}s ({sum(times)/60:.1f} min)")

        schema_valid = sum(1 for r in all_results if r["schema_valid"])
        print(f"\n  Schema validity: {schema_valid}/{len(all_results)} ({100*schema_valid//len(all_results)}%)")

        ft_passed = sum(r["format_tests_passed"] for r in successful)
        ft_total = sum(r["format_tests_total"] for r in successful)
        if ft_total > 0:
            print(f"  Format tests: {ft_passed}/{ft_total} passed ({100*ft_passed//ft_total}%)")

        fc_verified = sum(r["fact_check_verified"] for r in successful)
        fc_total = sum(r["fact_check_total"] for r in successful)
        if fc_total > 0:
            print(f"  Fact-check verified: {fc_verified}/{fc_total} ({100*fc_verified//fc_total}%)")

        # Per-sector breakdown
        print(f"\n  Per-sector breakdown:")
        print(f"  {'Sector':<40s} {'Time':>6s} {'Schema':>8s} {'Format':>8s} {'Facts':>8s}")
        print(f"  {'-'*40} {'-'*6} {'-'*8} {'-'*8} {'-'*8}")
        for r in all_results:
            status = "OK" if r["schema_valid"] else "FAIL"
            ft = f"{r['format_tests_passed']}/{r['format_tests_total']}" if r["format_tests_total"] > 0 else "n/a"
            fc = f"{r['fact_check_verified']}/{r['fact_check_total']}" if r["fact_check_total"] > 0 else "n/a"
            t = f"{r['wall_clock_seconds']:.0f}s" if r["error"] is None else "err"
            print(f"  {r['sector']:<40s} {t:>6s} {status:>8s} {ft:>8s} {fc:>8s}")

    if failed:
        print(f"\n  Errors:")
        for r in failed:
            print(f"    [{r['run_id']}] {r['sector']}: [{r['error_type']}] {r['error'][:80]}")

    # ── Resume-ready numbers ──

    if successful:
        schema_pct = 100 * schema_valid // len(all_results)
        fc_pct = 100 * fc_verified // fc_total if fc_total > 0 else 0
        avg_time = sum(times) / len(times)

        print(f"\n{'=' * 60}")
        print(f"  RESUME-READY NUMBERS")
        print(f"{'=' * 60}")
        print(f"  Sectors tested:    {len(all_results)}")
        print(f"  Success rate:      {len(successful)}/{len(all_results)} ({100*len(successful)//len(all_results)}%)")
        print(f"  Schema valid:      {schema_pct}% across {len(all_results)} runs")
        print(f"  Format tests:      {ft_passed}/{ft_total} passed ({100*ft_passed//ft_total}%)")
        print(f"  Fact-check rate:   {fc_pct}% of claims web-verified")
        print(f"  Avg time/report:   {avg_time:.0f}s / {avg_time/60:.1f} min (excluding HITL)")

    # ── Save ──

    out_path = OUT / "benchmark_results.json"
    out_path.write_text(json.dumps(all_results, indent=2, ensure_ascii=False))
    print(f"\n  Full results saved to {out_path}")


if __name__ == "__main__":
    asyncio.run(main())