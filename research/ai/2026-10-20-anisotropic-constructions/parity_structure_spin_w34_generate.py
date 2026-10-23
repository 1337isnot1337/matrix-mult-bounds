"""Optional rational reconstruction for the four-chain spin module.

The saved exact maps have a standard-library coefficient replay.  This
generator uses SymPy only for discovery and rational linear algebra.
"""

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / "results/anisotropic-constructions-2026-10-20"
DISCOVERY = DIRECTORY / "parity_structure_spin_w34_discovery.json"
WITNESS = DIRECTORY / "parity_structure_spin_w34_witness.json"


def reconstruct(path=DISCOVERY):
    import sympy as sp

    data = json.loads(Path(path).read_text())
    J, K = [], []
    for shift in range(2):
        first, second = sp.zeros(40, 32), sp.zeros(32, 36)
        for a in range(4):
            for j in range(8):
                first[8*(a+shift)+j, 8*a+j] = 1
                second[8*a+j, 9*a+j+shift] = 1
        J.append(first)
        K.append(second)
    columns = []
    for length, generator in zip(data["profile"], data["generators"]):
        for shift in range(length):
            column = sp.zeros(32, 1)
            for a, row in enumerate(generator):
                for j, value in enumerate(row):
                    column[8*(a+shift)+j] = value
            columns.append(column)
    U = sp.Matrix.hstack(*columns)
    Q = sp.Matrix.hstack(*U.T.nullspace()).T
    q0, q1 = Q*K[0], Q*K[1]
    zero = sp.zeros(Q.rows, 36)
    constraints = sp.Matrix.vstack(sp.Matrix.hstack(q1, zero),
                                  sp.Matrix.hstack(zero, q0),
                                  sp.Matrix.hstack(q0, -q1))
    D = sp.Matrix.hstack(*constraints.nullspace())
    if U.rank() != 13 or D.cols != 15:
        raise ArithmeticError("The rational intermediate dimensions changed")
    selected = D*sp.Matrix(data["D_subspace_matrix"])
    channels = selected.cols
    plus, minus = selected[:36, :], selected[36:, :]
    V = K[0]*plus
    L = []
    for index in range(4):
        p, s = divmod(index, 2)
        matrix = sp.zeros(80, 32)
        matrix[40*p:40*(p+1), :] = J[s]
        L.append(matrix)
    LP = [L[1], (L[0]-L[3])/2, L[2]]
    Wfull = sp.Matrix.hstack(*[matrix*U for matrix in L])
    W = Wfull[:, data["W_basis_column_indices"]]
    B = sp.Matrix.hstack(W, *[matrix*V for matrix in LP])
    square = B[data["join_row_indices"], :]
    if W.cols != 34 or B.cols != 76 or square.rows != square.cols:
        raise ArithmeticError("The four-chain join has the wrong dimensions")
    determinant = square.det(method="domain-ge")
    if not determinant:
        raise ArithmeticError("The saved join minor is singular over Q")
    inverse = square.inv(method="DM")
    left_inverse = sp.zeros(B.cols, 80)
    for j, row in enumerate(data["join_row_indices"]):
        left_inverse[:, row] = inverse[:, j]
    Y = left_inverse[W.cols:, :]
    Z0 = sp.Matrix.vstack(sp.zeros(36, channels), plus)
    Z1 = sp.Matrix.vstack(plus/2, -minus/2)
    Z2 = sp.Matrix.vstack(minus, sp.zeros(36, channels))
    Z = sp.Matrix.hstack(Z0, Z1, Z2).T
    if Y*B != sp.Matrix.hstack(sp.zeros(3*channels, W.cols), sp.eye(3*channels)):
        raise ArithmeticError("The exact join duality failed")

    def pack(matrix):
        denominator = int(sp.ilcm(*[value.q for value in matrix]))
        return {"shape": [matrix.rows, matrix.cols], "denominator": denominator,
                "entries": [[i, j, int(matrix[i, j]*denominator)]
                            for i in range(matrix.rows) for j in range(matrix.cols)
                            if matrix[i, j]]}

    spin = json.loads((DIRECTORY / "parity_balancing_spin1/scalar_witness.json").read_text())
    X = sp.Matrix(spin["base_common_map_numerator"])/2
    witness = {
        "source": "C(2,2) cyclic tensor C(2,4) cyclic tensor C(2,8)",
        "source_dimensions": [12, 80, 72], "target": "M(3,3,14)",
        "target_dimensions": [9, 42, 42], "field": "Q",
        "source_coordinate_orders": ["(i*3+k)*2+s", "(p*5+L)*8+j", "(q*4+a)*9+H"],
        "profile": data["profile"], "generators": data["generators"],
        "D_subspace_matrix": data["D_subspace_matrix"],
        "W_basis_column_indices": data["W_basis_column_indices"],
        "join_row_indices": data["join_row_indices"],
        "join_minor_determinant": str(determinant),
        "U_left_annihilator": pack(Q),
        "U_dimension": 13, "ignored_space_dimension": 34,
        "pair_space_dimension": 15, "join_dimension": 76,
        "X": pack(X), "Y": pack(Y), "Z": pack(Z),
        "new_exponent_established": False,
    }
    WITNESS.write_text(json.dumps(witness, indent=2)+"\n")
    print(json.dumps({"saved": str(WITNESS), "determinant": str(determinant),
                      "denominators": [witness[k]["denominator"] for k in "XYZ"],
                      "nonzeros": [len(witness[k]["entries"]) for k in "XYZ"]}), flush=True)
    return witness


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--discovery", default=str(DISCOVERY))
    args = parser.parse_args()
    reconstruct(args.discovery)
