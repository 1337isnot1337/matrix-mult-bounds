"""Exact finite Koszul ranks, split by the original bidegree conservation."""

from collections import defaultdict
from itertools import combinations
from math import comb

from sympy.polys.domains import QQ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.sdm import SDM


def rank_mod_2(columns):
    pivots = {}
    rank = 0
    for column in columns:
        while column:
            pivot = column.bit_length() - 1
            if pivot in pivots:
                column ^= pivots[pivot]
            else:
                pivots[pivot] = column
                rank += 1
                break
    return rank


def exact_rank(a, p):
    if a < 2 or not 0 <= p < a * (2 * a - 1):
        raise ValueError("invalid a or exterior degree")

    b_leg = [(y, j) for y in range(a) for j in range(2 * a - 1)]
    a_leg = [(x, q) for x in range(a) for q in range(a)]
    c_leg = [(z, v) for z in range(2 * a - 1) for v in range(a)]
    c_index = {value: index for index, value in enumerate(c_leg)}
    n = len(b_leg)
    inputs = list(combinations(range(n), p))
    outputs = list(combinations(range(n), p + 1))
    output_index = {value: index for index, value in enumerate(outputs)}

    columns_by_grade = defaultdict(list)
    for subset in inputs:
        sum_y = sum(b_leg[index][0] for index in subset)
        sum_j = sum(b_leg[index][1] for index in subset)
        occupied = set(subset)
        for x, q in a_leg:
            grade = (sum_y - x, sum_j + q)
            columns_by_grade[grade].append((subset, x, q, occupied))

    rank_mod2_total = 0
    rank_q_total = 0
    deficient_blocks = []
    maximum_block_columns = 0
    maximum_block_rows = 0

    for grade, columns in columns_by_grade.items():
        row_index = {}
        sparse_rows = {}
        mod2_columns = []
        for column_index, (subset, x, q, occupied) in enumerate(columns):
            vector = 0
            for b_index, (y, j) in enumerate(b_leg):
                if b_index in occupied:
                    continue
                z, v = x + y, j - q
                if not (0 <= z <= 2 * (a - 1) and 0 <= v <= a - 1):
                    continue

                output_wedge = tuple(sorted((*subset, b_index)))
                output_row = (
                    output_index[output_wedge] * len(c_leg) + c_index[(z, v)]
                )
                local_row = row_index.setdefault(output_row, len(row_index))
                sign = -1 if sum(index < b_index for index in subset) % 2 else 1
                sparse_rows.setdefault(local_row, {})[column_index] = sign
                vector ^= 1 << local_row
            mod2_columns.append(vector)

        rank2 = rank_mod_2(mod2_columns)
        rank_mod2_total += rank2
        maximum_block_columns = max(maximum_block_columns, len(columns))
        maximum_block_rows = max(maximum_block_rows, len(row_index))
        if rank2 == len(columns):
            rank_q = len(columns)
        else:
            matrix = DomainMatrix.from_rep(
                SDM(sparse_rows, (len(row_index), len(columns)), QQ)
            )
            rank_q = matrix.rank()
        rank_q_total += rank_q
        if rank_q < len(columns):
            deficient_blocks.append({
                "grade": list(grade),
                "columns": len(columns),
                "rows": len(row_index),
                "rank_mod_2": rank2,
                "rank_over_q": rank_q,
            })

    domain = a * a * comb(n, p)
    return {
        "a": a,
        "p": p,
        "domain": domain,
        "rank_mod_2": rank_mod2_total,
        "rank_over_q": rank_q_total,
        "kernel_dimension_over_q": domain - rank_q_total,
        "bigrade_blocks": len(columns_by_grade),
        "max_block_columns": maximum_block_columns,
        "max_block_rows": maximum_block_rows,
        "rationally_deficient_blocks": deficient_blocks,
    }


def atlas(a, powers):
    records = [exact_rank(a, p) for p in powers]
    return {
        "method": "exact block decomposition by the original bidegree invariants",
        "field": "Q",
        "modular_control": "F_2 full column rank certifies full rank over Q",
        "records": records,
        "improves_omega": False,
    }


if __name__ == "__main__":
    import argparse
    import json
    from pathlib import Path

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--a", type=int, required=True)
    parser.add_argument("--powers", type=int, nargs="+", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = atlas(args.a, args.powers)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "output": str(args.output),
        "records": [
            {"a": x["a"], "p": x["p"], "rank_over_q": x["rank_over_q"],
             "domain": x["domain"]}
            for x in report["records"]
        ],
    }, sort_keys=True))
