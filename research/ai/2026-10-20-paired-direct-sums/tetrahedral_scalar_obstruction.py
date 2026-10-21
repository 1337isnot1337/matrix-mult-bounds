"""Exact certificate against P3 plus trivial scalars -> M3 in the A4 model.

The Fourier classification and its hypotheses are proved in
scalar_and_symmetry.md.  All three resulting off-diagonal systems are
checked over Q.  No claim about nonequivariant maps is made.
"""
import argparse
from fractions import Fraction
import importlib.util
from itertools import product
import json
from pathlib import Path


SPEC = importlib.util.spec_from_file_location(
    "tetrahedral_scalar_obstruction_dependency", Path(__file__).with_name("tetrahedral_search.py"))
TETRA = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(TETRA)


def determinant(matrix):
    matrix = [[Fraction(value) for value in row] for row in matrix]
    value = Fraction(1)
    for column in range(len(matrix)):
        pivot = next((row for row in range(column, len(matrix)) if matrix[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            value *= -1
        entry = matrix[column][column]
        value *= entry
        for row in range(column+1, len(matrix)):
            if matrix[row][column]:
                multiplier = matrix[row][column]/entry
                matrix[row] = [a-multiplier*b for a, b in zip(matrix[row], matrix[column])]
    return value


def cyclotomic_sum(exponents):
    """Exact sums in Z[w]/(w²+w+1), represented by a+b*w."""
    powers = [(1, 0), (0, 1), (-1, -1)]
    result = [0, 0]
    for exponent in exponents:
        term = powers[exponent % 3]
        result[0] += term[0]
        result[1] += term[1]
    return result


def certificate():
    fourier = []
    for a, b, c in product(range(3), repeat=3):
        source = cyclotomic_sum(a*i+b*j+c*k for i, j, k in product(range(3), repeat=3)
                                if len({i, j, k}) == 3)
        target = cyclotomic_sum((a+b+c)*i for i in range(3))
        if (a+b+c) % 3:
            if source != [0, 0] or target != [0, 0]:
                raise ArithmeticError("An unsupported Fourier sector is nonzero")
        else:
            wanted = 6 if a == b == c else -3
            if source != [wanted, 0] or target != [3, 0]:
                raise ArithmeticError("The exact Fourier classification coefficients failed")
            fourier.append({"sector": [a, b, c], "source_coefficient": wanted, "target_coefficient": 3})
    # Native Cartesian source coordinates: A=(p,q), B=(y,quartic), C=(quartic,v).
    a_character = [5, 7]
    b_character = [0, 1, 7, 14]
    c_fixed = [9, 13, 8]
    source = TETRA.source_terms(1)
    matrices = []
    for diagonal_row in range(3):
        fixed_c = {coordinate: -2*int(diagonal_row != k) for k, coordinate in enumerate(c_fixed)}
        matrix = [[sum(value*fixed_c.get(c, 0) for (a, b, c), value in source.items()
                       if a == aa and b == bb) for bb in b_character] for aa in a_character]
        matrices.append(matrix)
    expected = [[[2, 2, 0, 0], [0, -2, 0, 0]],
                [[2, 2, 0, -2], [0, 0, -2, 0]],
                [[0, 0, 0, -2], [0, -2, -2, 0]]]
    if matrices != expected:
        raise ArithmeticError("The full source contraction gave unexpected sector matrices")
    targets = [[[0, 0], [0, 0]], [[0, 1], [0, 0]], [[0, 0], [1, 0]]]
    actual_targets = []
    for diagonal in (0, 4, 8):
        actual_targets.append([[TETRA.target_terms().get((a, b, diagonal), 0)
                                for b in a_character] for a in a_character])
    if actual_targets != targets:
        raise ArithmeticError("The matrix-tensor sector matrices changed")
    phases = []
    for phase in range(3):
        equations = []
        for k, i, j in product(range(3), range(2), range(2)):
            row = [0]*12
            # Unknown order: B00,B01,B02,B03,B10,B11,B12,B13,R00,R01,R10,R11.
            for ell in range(4):
                row[4*j+ell] += matrices[(k-phase) % 3][i][ell]
            for ell in range(2):
                row[8+2*i+ell] -= targets[k][ell][j]
            equations.append(row)
        det = determinant(equations)
        if det != (256 if phase == 0 else -256):
            raise ArithmeticError("A phase determinant certificate failed")
        phases.append({"phase": phase, "coefficient_matrix": equations,
                       "determinant": int(det), "rank": 12,
                       "only_homogeneous_solution": "B=0 and R=0"})
    return {
        "source": "P3 direct_sum r scalar tensors, each scalar carrying the trivial A4 action",
        "target": "M3 with all physical spaces carrying the standard tetrahedral 3D representation",
        "map_class": "ordinary A4-equivariant restriction", "interpretation_field": "C",
        "fourier_ring": "Z[w]/(w^2+w+1)", "fourier_sector_table": fourier,
        "forced_scalar_image_coefficient": 1,
        "normalized_fixed_sector_maps": "P^t L, P^t L, -4 P^t L; L=(J-I)/2; t=0,1,2",
        "normalization": "independent leg scalings with product one; all three phases checked separately",
        "a_nontrivial_character_coordinates": a_character,
        "b_nontrivial_character_coordinates": b_character,
        "c_fixed_coordinates": c_fixed,
        "source_sector_matrices": matrices, "target_sector_matrices": targets,
        "extension_equations": "S_(k-t) B^T = R T_k, where R is the inverse of the first-leg 2x2 character block",
        "unknown_order": ["B00", "B01", "B02", "B03", "B10", "B11", "B12", "B13", "R00", "R01", "R10", "R11"],
        "phase_certificates": phases, "all_phases_rejected": True,
        "coefficient_ring": "Q", "checks_passed": True,
        "construction_supplied": False, "improves_omega": False,
        "scope": "No exclusion of nonequivariant maps, nontrivial auxiliary representations, or singular degenerations.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = certificate()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key: value for key, value in result.items() if key != "phase_certificates"}, indent=2))
