"""Literal small-source controls for the long-leg exterior rank formula."""

from itertools import combinations
from math import comb
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "results/mixed-longlegs-candidate-2026-10-23"


def choose(n, q):
    return comb(n, q) if 0 <= q <= n else 0


def exact_mod2_rank(a, widths, p):
    n = sum(widths)
    long_c = sum(a + b - 1 for b in widths)
    b_coordinates = []
    c_offset = 0
    for block, width in enumerate(widths):
        b_coordinates.extend((block, j, c_offset) for j in range(width))
        c_offset += a + width - 1
    outputs = {w: k for k, w in enumerate(combinations(range(n), p))}
    pivots = {}
    for i in range(a):
        for wedge in combinations(range(n), p + 1):
            column = 0
            for k, b_index in enumerate(wedge):
                _, j, offset = b_coordinates[b_index]
                smaller = wedge[:k] + wedge[k + 1:]
                row = long_c * outputs[smaller] + offset + i + j
                column ^= 1 << row
            while column:
                pivot = column.bit_length() - 1
                old = pivots.get(pivot)
                if old is None:
                    pivots[pivot] = column
                    break
                column ^= old
    expected = a * choose(n, p + 1) - max(a - p - 1, 0) * choose(n - len(widths), p + 1)
    actual = len(pivots)
    if actual != expected:
        raise AssertionError((a, widths, p, actual, expected))
    return {"a": a, "widths": widths, "p": p,
            "rank_mod2": actual, "rank_formula": expected}


def main():
    RESULTS.mkdir(parents=True, exist_ok=True)
    controls = []
    for a in range(1, 6):
        for widths in ([1], [2], [4], [1, 1], [1, 3], [2, 3], [1, 2, 3]):
            for p in range(sum(widths)):
                controls.append(exact_mod2_rank(a, widths, p))
    report = {
        "status": "exact finite F2 controls; all-size upper and exact formula proved separately",
        "control_count": len(controls),
        "controls": controls,
        "new_candidate_source": {"a": 5, "N": 100, "c": 10,
            "exterior_ranks_p_0_through_3": [
                5 * choose(100, p + 1) - max(4-p, 0) * choose(90, p + 1)
                for p in range(4)
            ]},
        "improves_omega": False,
    }
    (RESULTS / "full_source_exterior_controls.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"control_count": len(controls), "candidate": report["new_candidate_source"]}))


if __name__ == "__main__":
    main()
