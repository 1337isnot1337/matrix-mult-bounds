"""Exact exterior-kernel and slice-cokernel controls for the frozen candidate.

These sufficient bounds are retained as independent partial controls. The
separate source_c_koszul.md theorem now proves that every output-leg degree
passes, without a target rank computation. Only the standard library is used.
"""
from __future__ import annotations

from itertools import combinations
from math import comb
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("mixed_candidate_shadow_base", HERE / "verify.py")
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
RESULTS = base.RESULTS


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def physical_blocks(counts):
    result = []
    b_offset = c_offset = 0
    for name, count in counts.items():
        b, c, _ = base.block(name)
        for _ in range(count):
            result.append((name, b, c, b_offset, c_offset))
            b_offset += b
            c_offset += c
    return result, b_offset, c_offset


def global_entries(counts):
    blocks, bdim, cdim = physical_blocks(counts)
    entries = [(i, bo + j, co + k)
               for name, _, _, bo, co in blocks
               for i, j, k in base.block(name)[2]]
    return bdim, cdim, entries


def degree_one_generators(counts):
    """Lift the independent block-incidence kernels to global B* tensor C.

    A generator is a sparse dictionary with keys (B index, C index). Its
    leading term is the largest key, with B index primary. No RREF or
    probabilistic nullspace calculation is used.
    """
    blocks, bdim, cdim = physical_blocks(counts)
    cached = {}
    result = []

    def components(key):
        if key not in cached:
            if len(key) == 1:
                n, rows = base.intrinsic_rows(key[0], True)
            else:
                n, rows = base.pair_rows(key[0], key[1], True)
            cached[key] = base.graph_certificate(n, rows)["kernel_components"]
        return cached[key]

    for index, (name, b, c, bo, co) in enumerate(blocks):
        for component in components((name,)):
            result.append({(bo + col // c, co + col % c): 1
                           for col in component})
        for other, d, e, other_bo, other_co in blocks[:index]:
            for component in components((other, name)):
                lifted = {}
                for column in component:
                    if column < d * c:
                        key = (other_bo + column // c, co + column % c)
                    else:
                        column -= d * c
                        key = (bo + column // e, other_co + column % e)
                    lifted[key] = 1
                result.append(lifted)
    seen = set()
    for relation in result:
        if seen.intersection(relation):
            raise ValueError("lifted kernel supports overlap")
        seen.update(relation)
    return bdim, cdim, result


def literal_koszul_image(relation, entries):
    """Apply the literal C-leg Koszul differential to a sparse vector."""
    by_b = {}
    for i, j, k in entries:
        by_b.setdefault(j, []).append((i, k))
    image = {}
    for (j, wedge), coefficient in relation.items():
        for i, k in by_b.get(j, ()):
            if k in wedge:
                continue
            output = tuple(sorted((k,) + wedge))
            sign = (-1) ** sum(v < k for v in wedge)
            base.add(image, (i, output), coefficient * sign)
    return image


def leading_variables(bdim, generators):
    variables = [set() for _ in range(bdim)]
    for relation in generators:
        j, k = max(relation)
        if k in variables[j]:
            raise ValueError("repeated leading monomial")
        variables[j].add(k)
    return [sorted(values) for values in variables]


def shadow_bound(cdim, degrees, p):
    return sum(choose(cdim, p) - choose(cdim - d, p) for d in degrees)


def shadow_products(bdim, cdim, generators, p):
    """Explicit witnesses for small controls; never expand the large case."""
    leading = {max(relation): relation for relation in generators}
    variables = leading_variables(bdim, generators)
    products = []
    for j, values in enumerate(variables):
        for wedge in combinations(range(cdim), p):
            intersection = sorted(set(wedge).intersection(values))
            if not intersection:
                continue
            k = intersection[0]
            multiplier = tuple(v for v in wedge if v != k)
            relation = {}
            for (other_j, other_k), coefficient in leading[j, k].items():
                if other_k in multiplier:
                    continue
                output = tuple(sorted((other_k,) + multiplier))
                sign = (-1) ** sum(v < other_k for v in multiplier)
                base.add(relation, (other_j, output), coefficient * sign)
            expected = (j, wedge)
            actual = max(relation, key=lambda key: (key[0], sum(1 << v for v in key[1])))
            if actual != expected:
                raise ValueError("exterior multiplication changed the expected leading term")
            products.append(relation)
    return products


def first_slice_ranks(coefficients):
    ranks = {}
    total = 0
    for name, count in base.COUNTS.items():
        b, _, entries = base.block(name)
        rows = [{} for _ in range(b)]
        for i, j, k in entries:
            base.add(rows[j], k, coefficients[i])
        ranks[name] = base.rational_rank(rows)
        total += count * ranks[name]
    return {"coefficients": list(coefficients), "block_ranks": ranks, "rank": total}


def projected_source_rank(p):
    """Rank of padded Full(5,100), obtained from the source by a C map."""
    return sum(min(100 * choose(104, j), 5 * choose(104, j + 1)) * choose(36, p - j)
               for j in range(104))


def report():
    bdim, cdim, generators = degree_one_generators(base.COUNTS)
    _, _, entries = global_entries(base.COUNTS)
    for relation in generators:
        lifted = {(j, (k,)): value for (j, k), value in relation.items()}
        if literal_koszul_image(lifted, entries):
            raise ValueError("lifted degree-one relation fails the unsplit literal map")
    if (bdim, cdim, len(generators)) != (100, 140, 428):
        raise ValueError("candidate kernel dimensions changed")
    leading = leading_variables(bdim, generators)
    degrees = [len(values) for values in leading]
    coordinates = [first_slice_ranks([int(i == j) for i in range(5)])
                   for j in range(5)]
    evaluations = [first_slice_ranks([t ** i for i in range(5)]) for t in range(5)]
    if [row["rank"] for row in coordinates] != [62, 68, 72, 68, 62]:
        raise ValueError("coordinate slice ranks changed")
    if [row["rank"] for row in evaluations] != [62] * 5:
        raise ValueError("evaluation slice ranks changed")

    comparisons = []
    for p in range(5, 40):
        source_lower = projected_source_rank(p)
        kernel_upper = 100 * comb(140, p) - source_lower
        cokernel_upper = 5 * comb(140, p + 1) - source_lower
        h = shadow_bound(140, degrees, p)
        coordinate_j = sum(choose(140 - row["rank"], p + 1) for row in coordinates)
        evaluation_j = 5 * choose(78, p + 1)
        comparisons.append({
            "degree": p,
            "projected_source_rank_lower_bound": source_lower,
            "source_kernel_upper_bound": kernel_upper,
            "target_shadow_kernel_lower_bound": h,
            "shadow_slack": h - kernel_upper,
            "shadow_certifies_pass": h >= kernel_upper,
            "source_cokernel_upper_bound": cokernel_upper,
            "target_coordinate_cokernel_lower_bound": coordinate_j,
            "coordinate_slack": coordinate_j - cokernel_upper,
            "coordinate_certifies_pass": coordinate_j >= cokernel_upper,
            "target_evaluation_cokernel_lower_bound": evaluation_j,
            "evaluation_slack": evaluation_j - cokernel_upper,
            "evaluation_certifies_pass": evaluation_j >= cokernel_upper,
        })
    shadow_pass = [row["degree"] for row in comparisons if row["shadow_certifies_pass"]]
    coordinate_pass = [row["degree"] for row in comparisons if row["coordinate_certifies_pass"]]
    evaluation_pass = [row["degree"] for row in comparisons if row["evaluation_certifies_pass"]]
    if shadow_pass != [5, 6] or coordinate_pass != list(range(12, 40)) or evaluation_pass != list(range(11, 40)):
        raise ValueError("sufficient-bound coverage changed")
    unresolved_by_these = [row["degree"] for row in comparisons
                           if not row["shadow_certifies_pass"] and not row["evaluation_certifies_pass"]]
    return {
        "status": "Independent sufficient controls; all C degrees now pass by the separate source theorem",
        "discovery_sha256": hashlib.sha256((HERE / "discovery_input.json").read_bytes()).hexdigest(),
        "scope": "Canonical target coefficients; source_c_koszul.md has stronger universal target scope",
        "global_degree_one_kernel_generators": len(generators),
        "all_generators_checked_on_unsplit_literal_map": True,
        "leading_order": "B index primary, then increasing colex C exterior monomial",
        "leading_C_variables_by_B_index": leading,
        "leading_counts_by_B_index": degrees,
        "sum_leading_counts": sum(degrees),
        "target_C5_kernel_lower_bound": shadow_bound(140, degrees, 5),
        "exact_source_C5_kernel": comb(105, 6),
        "coordinate_first_slices": coordinates,
        "evaluation_first_slices": evaluations,
        "evaluation_basis_parameters": list(range(5)),
        "source_projection": "Full(5,100) with 36 unused C coordinates",
        "comparisons": comparisons,
        "shadow_sufficient_degrees": shadow_pass,
        "coordinate_cokernel_sufficient_degrees": coordinate_pass,
        "evaluation_cokernel_sufficient_degrees": evaluation_pass,
        "degrees_not_decided_by_these_bounds_alone": unresolved_by_these,
        "current_unresolved_C_degrees": [],
        "current_all_degree_reason": "source_c_koszul.md proves generic maximum C-leg rank in every degree",
        "degeneration_constructed": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=RESULTS / "shadow_verification.json")
    args = parser.parse_args()
    result = report()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"kernel_generators": 428,
                      "shadow_sufficient_degrees": result["shadow_sufficient_degrees"],
                      "evaluation_sufficient_degrees": [11, 39],
                      "all_C_degrees_pass_by_separate_theorem": True,
                      "output": str(args.output)}, indent=2))
