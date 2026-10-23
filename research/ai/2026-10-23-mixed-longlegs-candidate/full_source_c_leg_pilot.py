"""Exact small C-leg ranks for canonical Full sums; finite controls only."""

from itertools import combinations
from math import comb
from pathlib import Path
import json


ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "results/mixed-longlegs-candidate-2026-10-23"


def rank_mod2(a, widths, p):
    n = sum(widths)
    m = sum(a+b-1 for b in widths)
    output_wedges = {value: i for i, value in enumerate(combinations(range(m), p+1))}
    columns_by_b = []
    offset = 0
    for b in widths:
        for j in range(b):
            columns_by_b.append([offset+i+j for i in range(a)])
        offset += a+b-1
    pivots = {}
    for wedge in combinations(range(m), p):
        occupied = set(wedge)
        for c_indices in columns_by_b:
            column = 0
            for i, c in enumerate(c_indices):
                if c not in occupied:
                    out = tuple(sorted((*wedge, c)))
                    row = a*output_wedges[out]+i
                    column ^= 1 << row
            while column:
                pivot = column.bit_length()-1
                old = pivots.get(pivot)
                if old is None:
                    pivots[pivot] = column
                    break
                column ^= old
    rank = len(pivots)
    return {"a": a, "widths": widths, "N": n, "M": m, "p": p,
            "rank_mod2": rank, "kernel_mod2": n*comb(m,p)-rank,
            "cokernel_mod2": a*comb(m,p+1)-rank}


def main():
    RESULTS.mkdir(parents=True, exist_ok=True)
    data = []
    for a, widths in [(2,[1,3]), (2,[2,2]), (3,[1,3]), (3,[2,2]),
                      (2,[1,1,3]), (2,[1,2,2]), (3,[1,1,3]), (3,[1,2,2]),
                      (3,[1,1]), (3,[2,2]), (4,[1,1]), (4,[1,2])]:
        m = sum(a+b-1 for b in widths)
        row = [rank_mod2(a,widths,p) for p in range(m)]
        data.extend(row)
        print(json.dumps({"a":a,"widths":widths,"kernels":[v["kernel_mod2"] for v in row],
                          "cokernels":[v["cokernel_mod2"] for v in row]}),flush=True)
    (RESULTS / "full_source_c_leg_pilot.json").write_text(json.dumps(data,indent=2)+"\n")


if __name__ == "__main__":
    main()
