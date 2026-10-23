"""Exact finite discovery of the proposed A5 five-cycle pair ranks."""
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "results/a5-nondivisor-2026-10-23/discovery.json"


def matrix(pair):
    return s.Matrix([[int((h-j, ell-r) in pair)
                      for h in range(9) for r in range(5)]
                     for j in range(5) for ell in range(9)])


def main():
    cycles = [[((2*t) % 5, (offset+2*t) % 5) for t in range(5)]
              for offset in range(5)]
    assert len({vertex for cycle in cycles for vertex in cycle}) == 25
    records = []
    for cycle in cycles:
        edges = []
        for i in range(5):
            pair = (cycle[i], cycle[(i+1) % 5])
            rank = matrix(pair).rank()
            edges.append({"pair": pair, "rank": rank})
            print(pair, rank, flush=True)
        records.append({"cycle": cycle, "edges": edges})
    result = {"scope": "Finite discovery, not the complete theorem acceptance.",
              "cycles": records, "all_pair_ranks_at_least35": all(
                  e["rank"] >= 35 for c in records for e in c["edges"]),
              "improves_omega": False}
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2)+"\n")


if __name__ == "__main__":
    main()
