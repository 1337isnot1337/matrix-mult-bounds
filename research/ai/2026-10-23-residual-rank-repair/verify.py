"""Exact controls for conditional repair gates; this constructs no paired maps."""

from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
from itertools import product
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def floor_root(value: int, degree: int) -> int:
    """Return the exact floor of a nonnegative integer's positive root."""
    if not isinstance(value, int) or value < 0:
        raise ValueError("value must be a nonnegative integer")
    if not isinstance(degree, int) or degree < 1:
        raise ValueError("degree must be a positive integer")
    low = 0
    high = 1 << ((value.bit_length() + degree - 1) // degree)
    while low < high:
        middle = (low + high + 1) // 2
        if middle**degree <= value:
            low = middle
        else:
            high = middle - 1
    return low


def root_interval(value: Fraction | int, degree: int, bits: int = 80):
    """A proved dyadic interval, with exact singleton intervals when possible."""
    value = Fraction(value)
    if value < 0 or bits < 1:
        raise ValueError("need a nonnegative value and positive precision")
    scale = 1 << bits
    numerator = value.numerator * scale**degree
    denominator = value.denominator
    floor = floor_root(numerator // denominator, degree)
    low = Fraction(floor, scale)
    high = low if floor**degree * denominator == numerator else low + Fraction(1, scale)
    assert low**degree <= value <= high**degree
    return low, high


def pair_product(ranks):
    ranks = tuple(ranks)
    if len(ranks) != 3 or any(not isinstance(r, int) or r < 0 for r in ranks):
        raise ValueError("three nonnegative integer rank bounds are required")
    return min(ranks[0] * ranks[1], ranks[0] * ranks[2], ranks[1] * ranks[2])


def gate_from_products(n, b, left, middle, right, residual_products=(), bits=80):
    """Certify a numerical gate, separately from its missing tensor premise."""
    if any(not isinstance(x, int) or x < 1 for x in (n, b, left, middle, right)):
        raise ValueError("source and target dimensions must be positive integers")
    residual_products = tuple(residual_products)
    if any(not isinstance(d, int) or d < 0 for d in residual_products):
        raise ValueError("residual pair products must be nonnegative integers")
    volume = left * middle * right
    target = root_interval(volume**3, 4, bits)
    source = root_interval(Fraction(2 * b * (2 * n + b - 1)**3, 9), 2, bits)
    repairs = [root_interval(d**3, 4, bits) for d in residual_products]
    gap_low = target[0] - source[1] - sum((r[1] for r in repairs), Fraction(0))
    gap_high = target[1] - source[0] - sum((r[0] for r in repairs), Fraction(0))
    if gap_low > 0:
        outcome = "strict-gate-certified"
    elif gap_high <= 0:
        outcome = "gate-not-satisfied"
    else:
        outcome = "interval-undecided"
    return {
        "source": [n, b],
        "target": [left, middle, right],
        "target_volume": volume,
        "residual_pair_products": list(residual_products),
        "source_cost_squared": fraction_json(Fraction(2 * b * (2 * n + b - 1)**3, 9)),
        "gap_interval": [fraction_json(gap_low), fraction_json(gap_high)],
        "outcome": outcome,
        "construction_certified": False,
        "improves_omega": False,
    }


def finite_gate(n, b, left, middle, right, residual_ranks=(), bits=80):
    return gate_from_products(n, b, left, middle, right,
                              [pair_product(r) for r in residual_ranks], bits)


def largest_single_product(n, b, left, middle, right):
    """Largest integer D passing the gate; None if even D=0 fails."""
    def accepts(d):
        return gate_from_products(n, b, left, middle, right, [d])["outcome"] == "strict-gate-certified"
    if not accepts(0):
        return None
    low, high = 0, left * middle * right
    while low < high:
        mid = (low + high + 1) // 2
        if accepts(mid):
            low = mid
        else:
            high = mid - 1
    return low


def fraction_json(value):
    value = Fraction(value)
    return [value.numerator, value.denominator]


def matrix_rank(rows):
    rows = [list(map(Fraction, row)) for row in rows]
    if not rows:
        return 0
    rank = 0
    for col in range(len(rows[0])):
        pivot = next((r for r in range(rank, len(rows)) if rows[r][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        value = rows[rank][col]
        rows[rank] = [x / value for x in rows[rank]]
        for r in range(rank + 1, len(rows)):
            value = rows[r][col]
            if value:
                rows[r] = [x - value * y for x, y in zip(rows[r], rows[rank])]
        rank += 1
        if rank == len(rows):
            break
    return rank


def flattening_ranks(tensor, shape):
    result = []
    for leg in range(3):
        others = [i for i in range(3) if i != leg]
        rows = []
        for i in range(shape[leg]):
            row = []
            for j, k in product(range(shape[others[0]]), range(shape[others[1]])):
                index = [0, 0, 0]
                index[leg], index[others[0]], index[others[1]] = i, j, k
                row.append(tensor.get(tuple(index), 0))
            rows.append(row)
        result.append(matrix_rank(rows))
    return result


def outer_product_replay(tensor, shape, output_leg):
    """Expand an independent outer-product source and its one nonidentity map."""
    inputs = [i for i in range(3) if i != output_leg]
    image = {}
    for i, j in product(range(shape[inputs[0]]), range(shape[inputs[1]])):
        for k in range(shape[output_leg]):
            index = [0, 0, 0]
            index[inputs[0]], index[inputs[1]], index[output_leg] = i, j, k
            index = tuple(index)
            coefficient = tensor.get(index, 0)
            if coefficient:
                image[index] = image.get(index, 0) + coefficient
    return image


def missing_corner_residual(size, kept, middle=4):
    """The exact missing products after retaining a principal matrix corner."""
    if not (0 < kept < size):
        raise ValueError("need a proper positive corner")
    tensor = {}
    for i, j, h in product(range(size), range(size), range(middle)):
        if i >= kept or j >= kept:
            tensor[(i * size + j, i * middle + h, h * size + j)] = 1
    return tensor, [size * size, size * middle, middle * size]


def verify():
    source_record = json.loads((HERE / "sources.json").read_text())
    for source in source_record["local_dependencies"]:
        assert hashlib.sha256((ROOT / source["path"]).read_bytes()).hexdigest() == source["sha256"]

    # Arbitrary integer tensors: all three outer-product envelopes are replayed.
    controls = []
    for shape in [(2, 3, 4), (3, 2, 3), (2, 2, 2)]:
        tensor = {index: ((17 * index[0] + 11 * index[1] + 5 * index[2] +
                           7 * index[0] * index[1] * index[2]) % 13) - 6
                  for index in product(*[range(d) for d in shape])}
        tensor = {key: value for key, value in tensor.items() if value}
        for leg in range(3):
            assert outer_product_replay(tensor, shape, leg) == tensor
        ranks = flattening_ranks(tensor, shape)
        controls.append({"shape": shape, "ranks": ranks,
                         "pair_product": pair_product(ranks),
                         "coefficient_positions_per_orientation": shape[0] * shape[1] * shape[2]})

    # Recover the exact first no-residual thresholds without decimal decisions.
    thresholds = []
    for deficit, expected in [(0, 38), (1, 64)]:
        first = next(n for n in range(max(4, deficit + 1), 150)
                     if finite_gate(n, 4, n-deficit, 4, n-deficit)["outcome"] == "strict-gate-certified")
        assert first == expected
        thresholds.append({"outer_deficit": deficit, "first_source_n": first})

    tables = []
    for n in [64, 100, 200, 500, 1000, 10000]:
        d = largest_single_product(n, 4, n - 1, 4, n - 1)
        assert d is not None
        assert gate_from_products(n, 4, n-1, 4, n-1, [d])["outcome"] == "strict-gate-certified"
        assert gate_from_products(n, 4, n-1, 4, n-1, [d+1])["outcome"] == "gate-not-satisfied"
        tables.append({"source_n": n, "outer_target": n-1,
                       "largest_single_residual_pair_product": d,
                       "largest_first_rank_if_long_ranks_are_4_outer": d // (4*(n-1))})

    # Quantitative localization factorization, checked as an exact polynomial.
    grid = 0
    for gamma in [Fraction(k, 10) for k in range(10)]:
        for root_delta in [Fraction(k, 100) for k in range(51)]:
            direct = root_delta**2 - Fraction(4-gamma, 2)*root_delta + Fraction(3, 4)*(1-gamma)
            factored = (root_delta - (1-gamma)/2)*(root_delta-Fraction(3, 2))
            assert direct == factored
            if root_delta < (1-gamma)/2:
                assert direct > 0
            grid += 1
    gamma_examples = []
    for gamma in [Fraction(1, 2), Fraction(7, 10), Fraction(3, 4), Fraction(9, 10)]:
        bound = Fraction(9, 4) - (1-gamma)**2/4
        gamma_examples.append({"first_rank_power": fraction_json(gamma),
                               "localization_bound": fraction_json(bound),
                               "below_existing_b4_rational_ceiling": bound < Fraction(30000,13433)})

    # Exact recovered-source control: Q(5,4) gives M4, embedded in M5.
    # This residual is explicitly known, but its finite repair gate fails.
    corner, shape = missing_corner_residual(5, 4)
    ranks = flattening_ranks(corner, shape)
    assert ranks == [9, 20, 20]
    assert len(corner) == 36
    corner_gate = finite_gate(5, 4, 5, 4, 5, [ranks])
    assert corner_gate["outcome"] == "gate-not-satisfied"
    return {
        "claim_ids": ["AI-RESIDUAL-RANK-FINITE-GATE-001", "AI-RESIDUAL-RANK-ASYMPTOTIC-GATE-002"],
        "local_dependency_hashes_checked": len(source_record["local_dependencies"]),
        "outer_product_controls": controls,
        "first_no_residual_thresholds": thresholds,
        "single_residual_product_budgets": tables,
        "localization_factorization_controls": grid,
        "quantitative_examples": gamma_examples,
        "recovered_q54_corner_control": {"missing_scalar_products": len(corner),
                                         "residual_ranks": ranks, "gate": corner_gate},
        "finite_gate_is_only_a_conditional_search_criterion": True,
        "successful_paired_map_constructed": False,
        "improves_omega": False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = verify()
    encoded = json.dumps(report, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(encoded)
    else:
        print(encoded, end="")


if __name__ == "__main__":
    main()
