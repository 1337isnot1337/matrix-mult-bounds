"""An exact finite-symmetry kernel obstruction for Q_(3,2).

This checks one forced Klein-four/tetrahedral equivariant compression.
It does not exclude arbitrary kernels or singular degenerations.
"""
import argparse
from collections import Counter
import importlib.util
from itertools import product
import json
from pathlib import Path


SPEC = importlib.util.spec_from_file_location(
    "tetrahedral_kernel_dependency", Path(__file__).with_name("kernel_algebra_search.py"))
ALGEBRA = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ALGEBRA)


def generators():
    """Actions of quaternion i,j on native tensor coordinate vectors.

    Q_(3,2) has modules A=S2* tensor S2*, B=S1* tensor S3,
    C=S3 tensor S1*.  Every total degree is even, so these actions
    factor through the commuting involutions of the Klein four group.
    """
    labels = [list(product(range(3), repeat=2)),
              list(product(range(2), range(4))),
              list(product(range(4), range(2)))]
    actions = []
    for which in ("i", "j"):
        axes = []
        for axis, coordinates in enumerate(labels):
            lookup = {point: k for k, point in enumerate(coordinates)}
            action = []
            for x, y in coordinates:
                sign = (-1)**(x+y+(which == "i" and axis != 0))
                if which == "i":
                    image = (x, y)
                else:
                    image = ((2-x, 2-y) if axis == 0 else
                             (1-x, 3-y) if axis == 1 else (3-x, 1-y))
                action.append((sign, lookup[image]))
            axes.append(action)
        actions.append(axes)
    return actions


def action_matrix(action):
    matrix = [[0]*len(action) for _ in action]
    for column, (sign, row) in enumerate(action):
        matrix[row][column] = sign
    return matrix


def certificate():
    shape, source, _, _ = ALGEBRA.NARROW.coordinates(3, 2)
    actions = generators()
    original = Counter(source)
    for axes in actions:
        transformed = Counter()
        for point in source:
            images = [axes[axis][coordinate] for axis, coordinate in enumerate(point)]
            transformed[tuple(image for _, image in images)] += images[0][0]*images[1][0]*images[2][0]
        if transformed != original:
            raise ArithmeticError("The full native source covariance check failed")
    kernel_b = [[int(k == 1)-int(k == 6) for k in range(8)],
                [int(k == 3)-int(k == 4) for k in range(8)]]
    kernel_c = [[int(k == 2)-int(k == 5) for k in range(8)],
                [int(k == 6)-int(k == 1) for k in range(8)]]
    for axis, kernel in ((1, kernel_b), (2, kernel_c)):
        equations = []
        for axes in actions:
            matrix = action_matrix(axes[axis])
            for i in range(8):
                matrix[i][i] -= 1
            equations.extend(matrix)
            if any(sum(matrix[i][j]*vector[j] for j in range(8))
                   for i in range(8) for vector in kernel):
                raise ArithmeticError("A proposed kernel vector is not invariant")
        if 8-len(ALGEBRA.rref(equations)[1]) != 2:
            raise ArithmeticError("The joint invariant kernel does not have dimension two")
    b_ids = [0, 1, 2, 3, 3, 4, 1, 5]
    c_ids = [0, 1, 2, 3, 4, 2, 1, 5]
    slices = [[[0]*6 for _ in range(6)] for _ in range(9)]
    for a, b, c in source:
        slices[a][c_ids[c]][b_ids[b]] += 1
    ranks = [len(ALGEBRA.rref(matrix)[1]) for matrix in slices]
    if ranks != [4, 3, 4, 3, 3, 3, 4, 3, 4]:
        raise ArithmeticError("Unexpected compressed slice ranks")
    witness = slices[1]
    support = [[i, j, witness[i][j]] for i, j in product(range(6), repeat=2) if witness[i][j]]
    if support != [[0, 1, 1], [1, 2, 1], [2, 4, 1], [3, 1, 1]]:
        raise ArithmeticError("The rank-three witness changed")
    return {
        "source": "Q_(3,2)", "source_shape": shape,
        "source_terms_checked_per_generator": len(source), "generators_checked": 2,
        "native_source_covariance": True,
        "kernel_b_columns": kernel_b, "kernel_c_columns": kernel_c,
        "joint_invariant_dimensions": [2, 2],
        "b_quotient_coordinate_ids": b_ids, "c_quotient_coordinate_ids": c_ids,
        "compressed_shape": [9, 6, 6], "compressed_first_slice_ranks": ranks,
        "rank_three_witness_first_coordinate": [0, 1],
        "rank_three_witness_matrix": witness,
        "rank_three_witness_nonzero_positions": support,
        "rank_three_minor_rows": [0, 1, 2], "rank_three_minor_columns": [1, 2, 4],
        "rank_three_minor_determinant": 1,
        "matrix_target": "M(3,2,3)", "every_matrix_target_first_slice_rank_is_even": True,
        "candidate_rejected": True, "coefficient_ring": "Q",
        "scope": "The forced Klein-four invariant-plane quotient only; arbitrary kernels and singular degenerations remain open.",
        "construction_supplied": False, "improves_omega": False,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = certificate()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps(result, indent=2))
