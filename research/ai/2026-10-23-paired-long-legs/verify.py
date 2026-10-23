"""Exact interpolation and finite controls for the paired-source long legs."""

from fractions import Fraction
from itertools import combinations
from math import comb
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
FRONTIER = ROOT / "results/paired-sources-2026-10-20/all-power-frontier.json"
FRONTIER_SHA256 = "3166e032019c24b0f3f4ba21ad2b23a62fdb357154169b91305ca7f0cb045d54"
ALL_RANKS = ROOT / "research/ai/2026-10-20-paired-sources/all_ranks.py"
ALL_RANKS_SHA256 = "1d63dfbcbb7fb34dd3b1d29fe0a41bd90e0db7295597189d1a7154c6e44d7dff"


def multiply_polynomials(left, right):
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    return out


def lagrange_basis(nodes):
    basis = []
    for i, node in enumerate(nodes):
        numerator = [Fraction(1)]
        denominator = 1
        for j, other in enumerate(nodes):
            if i == j:
                continue
            numerator = multiply_polynomials(numerator, [-other, 1])
            denominator *= node - other
        basis.append([value / denominator for value in numerator])
    return basis


def verify_interpolation(a):
    if a < 2:
        raise ValueError("a must be at least 2")
    d = a - 1
    m = 2 * d + 1
    nodes = tuple(range(m))
    basis = lagrange_basis(nodes)
    identities = 0
    for q in range(d + 1):
        for v in range(d + 1):
            degree = q + v
            reconstructed = [
                sum(Fraction(nodes[i] ** degree) * basis[i][j] for i in range(m))
                for j in range(m)
            ]
            expected = [Fraction(int(j == degree)) for j in range(m)]
            if reconstructed != expected:
                raise AssertionError((a, q, v, reconstructed, expected))
            identities += 1
    spark_sets = 0
    for subset in combinations(nodes, a):
        determinant = 1
        for i, left in enumerate(subset):
            for right in subset[i + 1 :]:
                determinant *= right - left
        if determinant == 0:
            raise AssertionError((a, subset, determinant))
        spark_sets += 1
    return {"a": a, "nodes": m, "product_coefficients": identities, "full_spark_subsets": spark_sets}


def verify_saved_frontier():
    digest = hashlib.sha256(FRONTIER.read_bytes()).hexdigest()
    if digest != FRONTIER_SHA256:
        raise AssertionError(f"frontier SHA-256 changed: {digest}")
    data = json.loads(FRONTIER.read_text())
    candidates = [
        (record["a"], item["shape"])
        for record in data["records"]
        if record["a"] >= 14
        for item in record["remaining_after_this_screen"]
    ]
    if len(candidates) != 28:
        raise AssertionError(f"expected 28 saved survivors, found {len(candidates)}")
    strict_short_leg = 0
    square_outer = 0
    by_a = {}
    for a, shape in candidates:
        by_a[a] = by_a.get(a, 0) + 1
        l, b, r = shape
        n = a * (2 * a - 1)
        dims = (l * r, l * b, b * r)
        if dims[0] > a * a or dims[1] > n or dims[2] > n:
            raise AssertionError((a, shape, dims, (a * a, n, n)))
        if dims[1] <= a * a or dims[2] <= a * a:
            raise AssertionError(("short-leg alignment is not forced", a, shape, dims))
        if dims[0] < a * a:
            strict_short_leg += 1
        else:
            if l != a or r != a:
                raise AssertionError(("unexpected equality case", a, shape, dims))
            square_outer += 1
    if (strict_short_leg, square_outer) != (22, 6):
        raise AssertionError((strict_short_leg, square_outer))
    return {
        "source": "results/paired-sources-2026-10-20/all-power-frontier.json",
        "source_sha256": FRONTIER_SHA256,
        "survivors": len(candidates),
        "survivors_by_a": by_a,
        "forced_short_leg_strict": strict_short_leg,
        "square_outer_equalities": square_outer,
    }


def support_low_count(a, p):
    """Count p-wedges using at most a-1 interpolation blocks."""
    if a < 2 or p < 0:
        raise ValueError("invalid a or exterior degree")
    m = 2 * a - 1
    counts = [[0] * (p + 1) for _ in range(a)]
    counts[0][0] = 1
    for _ in range(m):
        following = [[0] * (p + 1) for _ in range(a)]
        for support in range(a):
            for degree, value in enumerate(counts[support]):
                if not value:
                    continue
                following[support][degree] += value
                if support + 1 == a:
                    continue
                for occupancy in range(1, min(a, p - degree) + 1):
                    following[support + 1][degree + occupancy] += (
                        value * comb(a, occupancy)
                    )
        counts = following
    return sum(counts[support][p] for support in range(a))


def verify_support_dominance():
    """Compare the all-size support rank floor at p=a+1 to saved targets."""
    digest = hashlib.sha256(ALL_RANKS.read_bytes()).hexdigest()
    if digest != ALL_RANKS_SHA256:
        raise AssertionError(f"matrix-rank source SHA-256 changed: {digest}")
    spec = importlib.util.spec_from_file_location("paired_source_all_ranks", ALL_RANKS)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    data = json.loads(FRONTIER.read_text())
    records = []
    for record in data["records"]:
        a = record["a"]
        if a < 14:
            continue
        n = a * (2 * a - 1)
        p = a + 1
        source_floor = a * a * support_low_count(a, p)
        b_not_larger = []
        c_not_larger = []
        for item in record["remaining_after_this_screen"]:
            l, b, r = item["shape"]
            # Cyclically reorient the selected long target leg as the
            # first matrix leg before padding it to the source dimension.
            target_b = module.padded_matrix_rank((l, r, b), n, p)
            target_c = module.padded_matrix_rank((b, l, r), n, p)
            if target_b <= source_floor:
                b_not_larger.append(item["shape"])
            if target_c <= source_floor:
                c_not_larger.append(item["shape"])
        records.append({
            "a": a,
            "p": p,
            "survivors": len(record["remaining_after_this_screen"]),
            "source_rank_floor": source_floor,
            "source_domain": a * a * comb(n, p),
            "target_b_rank_not_larger": b_not_larger,
            "target_c_rank_not_larger": c_not_larger,
        })
    if sum(item["survivors"] for item in records) != 28:
        raise AssertionError("support comparison did not cover all 28 survivors")
    return {
        "method": "all-size interpolation-block support rank floor",
        "target_rank_formula": "padded matrix Koszul ranks from pinned all_ranks.py",
        "target_rank_source_sha256": ALL_RANKS_SHA256,
        "records": records,
        "improves_omega": False,
    }


def _rank_mod2(columns):
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


def verify_source_rank_mod2(a, p):
    """Independent sparse coefficient matrix rank control over F_2."""
    if a < 2 or not 0 <= p < a * (2 * a - 1):
        raise ValueError("invalid a or exterior degree")
    d = a - 1
    b_leg = [(y, j) for y in range(a) for j in range(2 * a - 1)]
    a_leg = [(x, q) for x in range(a) for q in range(a)]
    c_leg = [(z, v) for z in range(2 * a - 1) for v in range(a)]
    c_index = {value: i for i, value in enumerate(c_leg)}
    inputs = list(combinations(range(len(b_leg)), p))
    outputs = list(combinations(range(len(b_leg)), p + 1))
    output_index = {value: i for i, value in enumerate(outputs)}
    row_width = len(c_leg)
    columns = []
    for subset in inputs:
        occupied = set(subset)
        for x, q in a_leg:
            column = 0
            for b_index, (y, j) in enumerate(b_leg):
                if b_index in occupied:
                    continue
                z, v = x + y, j - q
                if not (0 <= z <= 2 * d and 0 <= v <= d):
                    continue
                output_wedge = tuple(sorted((*subset, b_index)))
                row = output_index[output_wedge] * row_width + c_index[(z, v)]
                column ^= 1 << row
            columns.append(column)
    rank = _rank_mod2(columns)
    domain = len(inputs) * len(a_leg)
    return {"a": a, "p": p, "rank_mod_2": rank, "domain": domain, "full_column_rank": rank == domain}


def verify_small_source_rank_over_q(a, p):
    """Exact rational rank for the small first-unproved-degree control."""
    if (a, p) != (2, 3):
        raise ValueError("the dense rational control is pinned to a=2, p=3")
    d = a - 1
    b_leg = [(y, j) for y in range(a) for j in range(2 * a - 1)]
    a_leg = [(x, q) for x in range(a) for q in range(a)]
    c_leg = [(z, v) for z in range(2 * a - 1) for v in range(a)]
    c_index = {value: i for i, value in enumerate(c_leg)}
    inputs = list(combinations(range(len(b_leg)), p))
    outputs = list(combinations(range(len(b_leg)), p + 1))
    output_index = {value: i for i, value in enumerate(outputs)}
    row_width = len(c_leg)
    columns = len(inputs) * len(a_leg)
    matrix = [[0] * columns for _ in range(len(outputs) * row_width)]
    for input_index, subset in enumerate(inputs):
        occupied = set(subset)
        for a_index, (x, q) in enumerate(a_leg):
            column = input_index * len(a_leg) + a_index
            for b_index, (y, j) in enumerate(b_leg):
                if b_index in occupied:
                    continue
                z, v = x + y, j - q
                if not (0 <= z <= 2 * d and 0 <= v <= d):
                    continue
                output_wedge = tuple(sorted((*subset, b_index)))
                sign = -1 if sum(index < b_index for index in subset) % 2 else 1
                row = output_index[output_wedge] * row_width + c_index[(z, v)]
                matrix[row][column] += sign

    rank = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(rank, len(matrix)) if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        pivot_value = matrix[rank][column]
        for row in range(rank + 1, len(matrix)):
            entry = matrix[row][column]
            if not entry:
                continue
            factor = Fraction(entry, pivot_value)
            matrix[row][column] = 0
            for other in range(column + 1, columns):
                matrix[row][other] -= factor * matrix[rank][other]
        rank += 1
    return {
        "a": a,
        "p": p,
        "rank_over_q": rank,
        "domain": columns,
        "kernel_dimension": columns - rank,
        "evidence": "exact rational elimination of the original coefficient matrix",
    }


def verify(maximum_a=6, rank_controls=False):
    if maximum_a < 2:
        raise ValueError("maximum_a must be at least 2")
    report = {
        "status": "finite exact controls only; the all-size proof is in long_leg_low_degrees.md",
        "interpolation": [verify_interpolation(a) for a in range(2, maximum_a + 1)],
        "saved_frontier": verify_saved_frontier(),
        "support_dominance_p_a_plus_1": verify_support_dominance(),
        "improves_omega": False,
    }
    if rank_controls:
        report["rank_controls"] = [
            verify_source_rank_mod2(a, p)
            for a in (2, 3)
            for p in range(a + 1)
        ]
        report["higher_degree_pilots"] = [
            verify_small_source_rank_over_q(2, 3),
            verify_source_rank_mod2(3, 4),
        ]
        if not all(item["full_column_rank"] for item in report["rank_controls"]):
            raise AssertionError(report["rank_controls"])
        if report["higher_degree_pilots"][0]["rank_over_q"] != 70:
            raise AssertionError(report["higher_degree_pilots"][0])
        if not report["higher_degree_pilots"][1]["full_column_rank"]:
            raise AssertionError(report["higher_degree_pilots"][1])
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        default="results/paired-long-legs-2026-10-23/verification.json",
    )
    args = parser.parse_args()
    report = verify(rank_controls=True)
    output = ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    try:
        display_output = output.relative_to(ROOT)
    except ValueError:
        display_output = output
    print(
        json.dumps(
            {
                "output": str(display_output),
                "interpolation_sizes": len(report["interpolation"]),
                "exact_product_coefficient_checks": sum(
                    item["product_coefficients"] for item in report["interpolation"]
                ),
                "full_spark_subsets": sum(
                    item["full_spark_subsets"] for item in report["interpolation"]
                ),
                "mod2_rank_controls": len(report["rank_controls"]),
                "higher_degree_pilots": len(report["higher_degree_pilots"]),
                "saved_survivors": report["saved_frontier"]["survivors"],
                "p_a_plus_1_comparisons": len(
                    report["support_dominance_p_a_plus_1"]["records"]
                ),
                "improves_omega": False,
            },
            sort_keys=True,
        )
    )
