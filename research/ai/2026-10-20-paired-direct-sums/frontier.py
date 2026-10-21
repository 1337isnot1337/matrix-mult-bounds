"""Exact paired-source frontiers for at most two matrix blocks.

Passing these necessary tests does not construct a tensor degeneration.
The source and matrix rank formulas are imported from the earlier paired
package; no new all-power rank formula is claimed here.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
from functools import lru_cache
import hashlib
import importlib.util
import json
from math import comb, isqrt, prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RANK_PATH = ROOT / "research/ai/2026-10-20-paired-sources/all_ranks.py"
SPEC = importlib.util.spec_from_file_location("paired_direct_sum_rank_dependency", RANK_PATH)
RANKS = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RANKS)
SELECTED_A = 10
SELECTED_SHAPES = ((4, 11, 10), (10, 12, 6))


def format_of(shape):
    l, b, r = shape
    return l*r, l*b, b*r


def source_format(a):
    return a*a, a*(2*a-1), a*(2*a-1)


def all_shapes(a):
    ambient, n, _ = source_format(a)
    for l in range(1, ambient+1):
        for r in range(1, ambient//l+1):
            for b in range(1, n//max(l, r)+1):
                yield l, b, r


@lru_cache(None)
def basic_padded_ranks(l, r, ambient):
    """The padded rank vector for middle dimension one."""
    padding = ambient-l*r
    if padding < 0:
        raise ValueError("negative first-leg padding")
    basic = [RANKS.matrix_basic_rank(l, r, p) for p in range(l*r)]
    return tuple(sum(comb(padding, p-q)*basic[q]
                     for q in range(max(0, p-padding), min(l*r-1, p)+1))
                 for p in range(ambient))


def block_ranks(shape, ambient):
    l, b, r = shape
    return tuple(b*x for x in basic_padded_ranks(l, r, ambient))


def first_obstruction(a, shapes):
    ambient = a*a
    vectors = [block_ranks(tuple(shape), ambient) for shape in shapes]
    for p in range(ambient):
        source = RANKS.source_rank(a, p)
        target = sum(vector[p] for vector in vectors)
        if target > source:
            return {"power": p, "source_rank": source, "target_rank": target}
    return None


def root_interval(volume, bits=32):
    """Integer endpoints for volume^(3/4), with denominator 2^bits."""
    if volume < 1 or bits < 1:
        raise ValueError("positive volume and precision required")
    fourth_power = volume**3 << (4*bits)
    lower = isqrt(isqrt(fourth_power))
    upper = lower + (lower**4 < fourth_power)
    return lower, upper


def improves_endpoint(a, volumes):
    """Decide sum(volume^(3/4)) > (6a-2)^2 / 6^(3/2)."""
    for bits in (32, 64, 128, 256):
        intervals = [root_interval(v, bits) for v in volumes]
        lower, upper = (sum(endpoints) for endpoints in zip(*intervals))
        right = (6*a-2)**4 << (2*bits)
        if 216*lower**2 > right:
            return True
        if 216*upper**2 <= right:
            return False
    raise ArithmeticError("root intervals do not decide this comparison")


def canonical_pair(shapes):
    direct = tuple(sorted(tuple(s) for s in shapes))
    exchanged = tuple(sorted((r, b, l) for l, b, r in shapes))
    return min(direct, exchanged)


def frontier_one_size(a):
    if a < 2:
        raise ValueError("this source formula requires a >= 2")
    ambient, n, _ = source_format(a)
    source = [RANKS.source_rank(a, p) for p in range(ambient)]
    accepted = []
    excluded = 0
    singles = []
    for shape in all_shapes(a):
        ranks = block_ranks(shape, ambient)
        if any(x > y for x, y in zip(ranks, source)):
            excluded += 1
            continue
        volume = prod(shape)
        accepted.append((shape, format_of(shape), ranks,
                         volume, root_interval(volume)[1]))
        if improves_endpoint(a, (volume,)):
            singles.append(list(shape))

    # All arithmetic in this prefilter is integral. An upper score below
    # this floor cannot pass the endpoint inequality.
    threshold_floor = isqrt(((6*a-2)**4 << 64)//216)
    dimension_pairs = 0
    improving_pairs = 0
    rank_rejections = 0
    raw_survivors = 0
    survivors = {}
    for i, (s1, d1, k1, v1, upper1) in enumerate(accepted):
        left = ambient-d1[0], n-d1[1], n-d1[2]
        for s2, d2, k2, v2, upper2 in accepted[i:]:
            if any(x > y for x, y in zip(d2, left)):
                continue
            dimension_pairs += 1
            if upper1+upper2 <= threshold_floor:
                continue
            if not improves_endpoint(a, (v1, v2)):
                continue
            improving_pairs += 1
            if any(x+y > z for x, y, z in zip(k1, k2, source)):
                rank_rejections += 1
                continue
            raw_survivors += 1
            key = canonical_pair((s1, s2))
            survivors[key] = {"shapes": [list(s) for s in key],
                              "volumes": [prod(s) for s in key],
                              "format": [sum(d[j] for d in map(format_of, key))
                                         for j in range(3)]}
    return {
        "a": a,
        "source_format": [ambient, n, n],
        "dimension_compatible_ordered_shapes": len(accepted)+excluded,
        "individually_rank_excluded_shapes": excluded,
        "individually_admissible_shapes": len(accepted),
        "improving_single_block_survivors": singles,
        "dimension_compatible_unordered_pairs_after_individual_screen": dimension_pairs,
        "improving_pairs_after_individual_screen": improving_pairs,
        "pairs_excluded_by_sum_of_padded_ranks": rank_rejections,
        "raw_surviving_unordered_pairs": raw_survivors,
        "surviving_pairs_modulo_BC_exchange": [survivors[key] for key in sorted(survivors)],
    }


def frontier(maximum=10, minimum=2):
    return {
        "scope": "At most two positive matrix blocks; complete finite formats; every first-leg Koszul power.",
        "minimum_a": minimum,
        "maximum_a": maximum,
        "records": [frontier_one_size(a) for a in range(minimum, maximum+1)],
        "rank_dependency_sha256": hashlib.sha256(RANK_PATH.read_bytes()).hexdigest(),
        "acceptance_arithmetic": "integers only; certified root intervals",
        "improves_omega": False,
        "construction_supplied": False,
    }


def integer_nth_root(number, exponent):
    if number < 0 or exponent < 1:
        raise ValueError("invalid root arguments")
    low, high = 0, 1 << ((number.bit_length()+exponent-1)//exponent)
    while high-low > 1:
        middle = (low+high)//2
        if middle**exponent <= number:
            low = middle
        else:
            high = middle
    return low


def conditional_gate(a, shapes, omega=Fraction(1121, 500), denominator=20):
    """An exponent comparison CONDITIONAL on an unconstructed degeneration."""
    t = omega/3
    bases = [36*prod(shape) for shape in shapes]
    roots = []
    for base in bases:
        power = base**t.numerator * denominator**t.denominator
        lower = integer_nth_root(power, t.denominator)
        if not lower**t.denominator <= power < (lower+1)**t.denominator:
            raise ArithmeticError("invalid root interval")
        roots.append(lower)
    if sum(roots) <= (6*a-2)**2 * denominator:
        raise ArithmeticError("these intervals do not certify the conditional gate")
    return {"conditional_omega_upper": str(omega), "t_test": str(t),
            "bases": bases, "rhs": (6*a-2)**2,
            "lower_numerators": roots, "lower_denominator": denominator,
            "strict_sum_comparison": True,
            "premise": "The stated complex tensor degeneration exists; it is not constructed here.",
            "improves_omega": False}


def selected_certificate():
    a = SELECTED_A
    shapes = SELECTED_SHAPES
    ambient, n, _ = source_format(a)
    vectors = [block_ranks(shape, ambient) for shape in shapes]
    records = [{"power": p, "source_rank": RANKS.source_rank(a, p),
                "target_rank": sum(vector[p] for vector in vectors)}
               for p in range(ambient)]
    if any(record["target_rank"] > record["source_rank"] for record in records):
        raise ArithmeticError("selected target fails the first-leg rank screen")
    target_format = [sum(format_of(s)[j] for s in shapes) for j in range(3)]
    lower = a*a-(n-target_format[1])-(n-target_format[2])
    minimum_target_slice = min(b for _, b, _ in shapes)
    if lower <= minimum_target_slice:
        raise ArithmeticError("the recorded ordinary-map obstruction no longer holds")
    return {
        "a": a, "shapes": [list(s) for s in shapes],
        "source_format": list(source_format(a)), "target_format": target_format,
        "all_first_leg_powers": records,
        "constant_restriction_obstruction": {
            "source_minimum_nonzero_first_slice_rank": a*a,
            "other_leg_kernel_dimensions": [n-target_format[1], n-target_format[2]],
            "projected_source_minimum_rank_lower_bound": lower,
            "target_minimum_nonzero_first_slice_rank": minimum_target_slice,
        },
        "conditional_gate": conditional_gate(a, shapes),
        "rank_dependency_sha256": hashlib.sha256(RANK_PATH.read_bytes()).hexdigest(),
        "construction_supplied": False, "improves_omega": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--maximum-a", type=int, default=10)
    parser.add_argument("--minimum-a", type=int, default=2)
    parser.add_argument("--selected", action="store_true")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = selected_certificate() if args.selected else frontier(args.maximum_a, args.minimum_a)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+"\n")
    if args.selected:
        print("Selected conditional target: all first-leg powers pass; ordinary maps are excluded; no degeneration constructed.")
    else:
        print(json.dumps([{"a": r["a"], "surviving_pair_orbits": len(r["surviving_pairs_modulo_BC_exchange"])}
                          for r in report["records"]]))
