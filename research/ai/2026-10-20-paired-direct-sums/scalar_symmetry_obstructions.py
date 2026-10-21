"""Exact data for two symmetry-restricted obstructions and a scalar repair.

The arguments are stated in scalar_and_symmetry.md.  No general
restriction or degeneration obstruction is inferred from these ansatzes.
"""
import argparse
from collections import Counter
from fractions import Fraction
import importlib.util
from itertools import product
import json
from pathlib import Path


SPEC = importlib.util.spec_from_file_location(
    "scalar_symmetry_dependency", Path(__file__).with_name("tetrahedral_search.py"))
TETRA = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(TETRA)


def weights(degree):
    return Counter(range(-degree, degree+1, 2))


def tensor_character(left, right):
    result = Counter()
    for a, n in weights(left).items():
        for b, m in weights(right).items():
            result[a+b] += n*m
    return result


def certificate():
    for pair, summands in (((2, 2), (4, 2, 0)), ((2, 4), (6, 4, 2))):
        character = Counter()
        for degree in summands:
            character.update(weights(degree))
        if character != tensor_character(*pair):
            raise ArithmeticError("An SL2 character identity failed")
    fixed_labels = [[0, 4, 8], [3, 9, 12], [9, 13, 8]]
    lookup = [{label: i for i, label in enumerate(axis)} for axis in fixed_labels]
    fixed = {}
    for point, value in TETRA.source_terms().items():
        if all(coordinate in lookup[k] for k, coordinate in enumerate(point)):
            fixed[tuple(lookup[k][coordinate] for k, coordinate in enumerate(point))] = value
    expected = {point: 1 for point in product(range(3), repeat=3) if len(set(point)) == 3}
    if fixed != expected:
        raise ArithmeticError("The exact fixed-sector tensor is not the six-term permanent")
    slices = [[[fixed.get((a, b, c), 0) for c in range(3)] for b in range(3)] for a in range(3)]
    l = [[Fraction(i != j, 2) for j in range(3)] for i in range(3)]
    minus_four_l = [[-4*v for v in row] for row in l]
    transformed = TETRA.coefficient_contraction(fixed, [l, l, minus_four_l])
    for point in product(range(3), repeat=3):
        desired = Fraction(len(set(point)) == 1)-1
        if transformed.get(point, 0) != desired:
            raise ArithmeticError("The exact 27-coefficient polarization defect failed")
    repaired = {point: transformed.get(point, 0)+1 for point in product(range(3), repeat=3)}
    if {point: value for point, value in repaired.items() if value} != {
            (i, i, i): Fraction(1) for i in range(3)}:
        raise ArithmeticError("The scalar polarization repair failed")
    return {
        "interpretation_field": "C", "coordinate_equivalence_field": "Q(i)",
        "full_sl2_source_first_leg_degrees": [0, 2, 4],
        "full_sl2_source_other_leg_degrees": [2, 4, 6],
        "full_sl2_target_leg_degrees": [0, 2, 4],
        "full_sl2_missing_trivial_long_leg_component": True,
        "full_sl2_target_identity_slice_rank": 9,
        "full_sl2_necessary_scalar_summands": 9,
        "full_sl2_trivial_scalar_identity_slice_rank_upper_bound": 1,
        "full_sl2_any_number_of_trivial_scalars_excluded": True,
        "klein_fixed_source_coordinate_labels": fixed_labels,
        "klein_fixed_source_terms": [[*point, value] for point, value in sorted(fixed.items())],
        "klein_fixed_source_slice_matrices": slices,
        "klein_fixed_source_slice_formula": [["0", "a2", "a1"], ["a2", "0", "a0"], ["a1", "a0", "0"]],
        "klein_fixed_nonzero_source_slice_minimum_rank": 2,
        "klein_fixed_target_slice_minimum_rank": 1,
        "a4_equivariant_p3_to_m3_ordinary_restriction_excluded": True,
        "polarization_map_a_b": [[str(v) for v in row] for row in l],
        "polarization_map_c": [[str(v) for v in row] for row in minus_four_l],
        "polarization_full_coefficient_positions_checked": 27,
        "polarization_original_source_defect": "minus the all-ones rank-one tensor",
        "polarization_scalar_summands": 1,
        "polarization_target": "D3 only",
        "checks_passed": True, "matrix_multiplication_construction": False,
        "improves_omega": False,
        "scope": "Specified equivariant ordinary maps only; nonsymmetric maps and singular degenerations are not excluded.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = certificate()
    if args.output:
        args.output.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))
