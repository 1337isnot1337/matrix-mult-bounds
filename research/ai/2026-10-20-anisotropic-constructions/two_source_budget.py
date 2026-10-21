"""Exact two-source capacity bounds and a sharp majority-block control.

The capacity theorem concerns arbitrary source tensors. The finite source
scans only identify targets not excluded by necessary conditions; they
are not matrix multiplication constructions from convolution sources.
"""

from collections import Counter
from itertools import product
import json
from math import isqrt
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUTPUT = ROOT / "results/anisotropic-constructions-2026-10-20/two-source-budget.json"


def capacity_passes(n, first_dimension, second_dimension):
    """Exact test sqrt(max(0,n^2-N))+sqrt(max(0,n^2-M)) <= n."""
    d = max(0, n*n-first_dimension)
    e = max(0, n*n-second_dimension)
    remaining = n*n-d-e
    return remaining >= 0 and 4*d*e <= remaining*remaining


def equal_source_minimum(n):
    return n*n-(n*n//4)


def majority_control(first_vertices, second_vertices):
    """Contract two explicit block-zero trace sources onto full M_n."""
    r, s = first_vertices, second_vertices
    if r < 1 or s < 1:
        raise ValueError("Both vertex blocks must be nonempty")
    n = r+s
    units = list(product(range(n), repeat=2))
    allowed = [[(i, j) for i, j in units if not (i < r and j < r)],
               [(i, j) for i, j in units if not (i >= r and j >= r)]]
    indices = [{unit: k for k, unit in enumerate(part)} for part in allowed]
    image = Counter()
    counts = []
    for part, index in zip(allowed, indices):
        count = 0
        for i, j, k in product(range(n), repeat=3):
            triple = ((i, j), (j, k), (k, i))
            if all(unit in index for unit in triple):
                source_point = tuple(index[unit] for unit in triple)
                # The source coordinate maps send an allowed matrix unit
                # to the identically labelled target matrix unit.
                target_point = tuple(n*part[v][0]+part[v][1] for v in source_point)
                image[target_point] += 1
                count += 1
        counts.append(count)
    target = {(n*i+j, n*j+k, n*k+i): 1 for i, j, k in product(range(n), repeat=3)}
    if dict(image) != target:
        raise ArithmeticError("Majority-block coefficient identity failed")
    dimensions = [len(part) for part in allowed]
    if dimensions != [n*n-r*r, n*n-s*s]:
        raise ArithmeticError("Incorrect majority-block dimensions")
    if not capacity_passes(n, *dimensions):
        raise ArithmeticError("Sharp control failed the capacity inequality")
    return {"vertex_blocks": [r, s], "matrix_target": n,
            "source_leg_dimensions": dimensions,
            "source_term_counts": counts, "checked_target_terms": len(target),
            "complete_coefficient_identity": True,
            "capacity_square_root_deficits": [r, s],
            "capacity_equality": r+s == n}


def formats(maximum_dimension):
    a = 2
    while a*a*(2*a-1) <= maximum_dimension:
        b = a
        while a*b*(a+b-1) <= maximum_dimension:
            yield a, b
            b += 1
        a += 1


def critical_pair_score_passes(a, b, n):
    c = 3*(a+b)-2
    return (6*n)**9 > 16*c**12


def pair_frontier(maximum_dimension=2904):
    records = []
    for a, b in formats(maximum_dimension):
        dimension = a*b*(a+b-1)
        largest = isqrt((4*dimension)//3)
        if not capacity_passes(largest, dimension, dimension):
            raise ArithmeticError("Largest dimension-admissible square is incorrect")
        if capacity_passes(largest+1, dimension, dimension):
            raise ArithmeticError("Dimension-admissible square was not maximal")
        records.append({"a": a, "b": b, "source_dimension": dimension,
                        "largest_capacity_admissible_square": largest,
                        "passes_critical_pair_score": critical_pair_score_passes(a, b, largest)})
    records.sort(key=lambda x: (x["source_dimension"], x["a"], x["b"]))
    passing = [record for record in records if record["passes_critical_pair_score"]]
    return {"maximum_source_dimension": maximum_dimension, "source_formats": len(records),
            "records": records, "first_relaxed_survivor": passing[0] if passing else None,
            "ordinary_and_singular_source_maps_constructed": False}


def majority_obstructions(a, b, s):
    """Necessary ordinary conditions from a cross-block rank-one parameter."""
    dimension = a*b*(a+b-1)
    target_dimension = 3*s*s
    if target_dimension > dimension:
        return [{"kind": "leg_dimension", "source": dimension, "target": target_dimension}]
    loss = dimension-target_dimension
    upper = s+2*loss
    answer = []
    if upper < a*b:
        answer.append({"kind": "minimum_source_slice_rank", "lift_upper": upper,
                       "source_lower": a*b})
    m = a+b-1
    for rank in range(1, min(a, b)):
        if 3*rank <= m:
            cap, theorem = rank, "fixed_support"
        elif rank >= 2 and 3*rank-1 == m:
            cap, theorem = max(rank, 4), "first_boundary"
        else:
            continue
        if s*s > cap*a*b and upper < (rank+1)*a*b:
            answer.append({"kind": "Hankel_symbol_Segre_dimension", "theorem": theorem,
                           "rank_level": rank, "symbol_dimension_cap": cap,
                           "matrix_block_dimension": s*s, "coefficient_dimension_cap": cap*a*b,
                           "lift_upper": upper, "strict_slice_threshold": (rank+1)*a*b})
    return answer


def majority_frontier(maximum_dimension=14364):
    records = []
    for a, b in formats(maximum_dimension):
        dimension = a*b*(a+b-1)
        score_eligible = []
        for s in range(2, isqrt(dimension//3)+1):
            if critical_pair_score_passes(a, b, 2*s):
                reasons = majority_obstructions(a, b, s)
                score_eligible.append({"s": s, "target_dimension": 3*s*s,
                                       "ordinary_obstructions": reasons})
        if score_eligible:
            records.append({"a": a, "b": b, "source_dimension": dimension,
                            "score_eligible_majority_targets": score_eligible})
    records.sort(key=lambda x: (x["source_dimension"], x["a"], x["b"]))
    first = None
    for record in records:
        allowed = [item for item in record["score_eligible_majority_targets"]
                   if not item["ordinary_obstructions"]]
        if allowed:
            first = {key: record[key] for key in ("a", "b", "source_dimension")}
            first.update(allowed[0])
            break
    return {"maximum_source_dimension": maximum_dimension,
            "scope": "ordinary restrictions A(a,b) to the balanced majority tensor T_s only",
            "records": records, "first_relaxed_survivor": first,
            "singular_maps_excluded_by_ordinary_tests": False,
            "source_to_majority_construction_found": False}


def build_report():
    pair = pair_frontier()
    if pair["first_relaxed_survivor"] != {
            "a": 11, "b": 12, "source_dimension": 2904,
            "largest_capacity_admissible_square": 62, "passes_critical_pair_score": True}:
        raise ArithmeticError("Unexpected two-copy frontier")
    majority = majority_frontier()
    if majority["first_relaxed_survivor"]["a"] != 18 or majority["first_relaxed_survivor"]["b"] != 21:
        raise ArithmeticError("Unexpected majority frontier")
    conditional = 372**2249 > 601526**1000
    if not conditional:
        raise ArithmeticError("Conditional finite-score arithmetic failed")
    return {"equal_copy_capacity": "N >= ceil(3*n^2/4)",
            "unequal_capacity": "sqrt(max(0,n^2-N_T))+sqrt(max(0,n^2-N_U)) <= n",
            "capacity_scope": "ordinary restrictions and algebraic degenerations",
            "sharp_positive_controls": [majority_control(r, s) for r, s in [(1, 1), (2, 2), (2, 3), (3, 4)]],
            "two_equal_source_frontier": pair,
            "conditional_pair_target": {"source": "two copies of A(11,12)", "target": "M62",
                                        "exponent_numerator": 2249, "exponent_denominator": 1000,
                                        "integer_inequality": "372^2249 > 601526^1000",
                                        "integer_inequality_verified": conditional, "map_constructed": False},
            "ordinary_A1112_to_T31_obstructions": majority_obstructions(11, 12, 31),
            "ordinary_majority_frontier": majority,
            "new_exponent_established": False}


def main():
    report = build_report()
    OUTPUT.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"report": str(OUTPUT), "two_source_first": report["two_equal_source_frontier"]["first_relaxed_survivor"],
                      "ordinary_majority_first": report["ordinary_majority_frontier"]["first_relaxed_survivor"],
                      "new_exponent_established": False}, indent=2))


if __name__ == "__main__":
    main()
