"""Executa suíte de traps contra LLM."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from src.traps import TRAPS
from src.evaluator import evaluate_response


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--model", default="stub")
    p.add_argument("--vllm-url", default="http://localhost:8000/v1")
    args = p.parse_args()

    results = []
    for trap in TRAPS:
        # TODO: call vLLM OpenAI-compatible API
        response = f"[stub response to {trap.id}]"
        label = evaluate_response(trap, response)
        results.append({"id": trap.id, "category": trap.category, "pass": label})

    out = Path("output/confusion_matrix.json")
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(results, indent=2), encoding="utf-8")
    passed = sum(1 for r in results if r["pass"])
    print(f"passed {passed}/{len(results)} — see {out}")


if __name__ == "__main__":
    main()
