"""Exact finite controls for the one-scalar endpoint-corner obstruction."""

import argparse
import importlib.util
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location("endpoint_corner", HERE / "m1_endpoint_corner.py")
CORNER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CORNER)


def verify():
    tensor = CORNER.canonical_tensor()
    # A_R is the identity and the scalar A vector is the first vector of F.
    # B and C scalar vectors occupy a new coordinate, outside both endpoint spaces.
    fibre = []
    for q in range(4):
        matrix = [[tensor.get((12+q, b, c), 0) for c in range(19)] for b in range(19)]
        matrix[18][18] = int(q == 0)
        fibre.append(matrix)
    b_flat = [[fibre[a][b][c] for a in range(4) for c in range(19)] for b in range(19)]
    c_flat = [[fibre[a][b][c] for a in range(4) for b in range(19)] for c in range(19)]
    support_dimensions = [CORNER.rank(b_flat), CORNER.rank(c_flat)]
    basis_ranks = [CORNER.rank(matrix) for matrix in fibre]
    assert support_dimensions == [15, 5]
    assert basis_ranks == [5, 4, 4, 4]
    # The singular A_R branch: kill source A15 and put the scalar on target A15.
    scalar_slice = [[int(b == 18 and c == 18) for c in range(19)] for b in range(19)]
    assert CORNER.rank(scalar_slice) == 1
    return {
        "corner_dimensions": [16, 18, 18],
        "source_with_scalar_dimensions": [17, 19, 19],
        "auxiliary_scalar_rank": 1,
        "invertible_A_R_control": {
            "A_R": "identity",
            "scalar_A_image": "A_(p3,p0), first basis direction of t5 tensor P",
            "scalar_B_C_images": "new coordinate18 on each long leg",
            "four_fibre_matrices": fibre,
            "basis_slice_ranks": basis_ranks,
            "uniform_slice_rank_upper_bound": 5,
            "aggregate_long_support_dimensions": support_dimensions,
        },
        "singular_A_R_control": {
            "A_R": "identity except source A15 is killed",
            "scalar_A_image": "target A15",
            "target_A15_slice_rank": 1,
        },
        "target": "M(4,4,4)",
        "target_nonzero_slice_ranks": [4, 8, 12, 16],
        "target_four_dimensional_rank_one_fibre_support_options": [[16, 4], [4, 16]],
        "one_scalar_degeneration_excluded": True,
        "two_scalar_degeneration_excluded": False,
        "general_Q64_degeneration_excluded": False,
        "improves_omega": False,
        "review_scope": "same-session controls; no external review",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify()
    if args.output:
        args.output.write_text(json.dumps(result, indent=2)+"\n")
    compact = dict(result)
    compact["invertible_A_R_control"] = {key: value for key, value in result["invertible_A_R_control"].items()
                                         if key != "four_fibre_matrices"}
    print(json.dumps(compact, indent=2))


if __name__ == "__main__":
    main()
