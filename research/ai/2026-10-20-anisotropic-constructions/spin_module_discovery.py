"""Optional discovery and rational reconstruction of a spin-one module.

NumPy and SymPy are discovery dependencies only.  The independent saved
map replay will use standard-library integer arithmetic.
"""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / "results/anisotropic-constructions-2026-10-20"


def toolkit(prime=65521):
    """The small finite-field toolkit used only by this discovery script."""
    import numpy as np

    def rref(matrix):
        matrix = np.asarray(matrix, dtype=np.int64).copy() % prime
        pivots = []
        for column in range(matrix.shape[1]):
            candidates = np.flatnonzero(matrix[len(pivots):, column])
            if not len(candidates):
                continue
            row = len(pivots)
            other = row+int(candidates[0])
            matrix[[row, other]] = matrix[[other, row]]
            matrix[row] = matrix[row]*pow(int(matrix[row, column]), -1, prime) % prime
            factors = matrix[:, column].copy()
            factors[row] = 0
            matrix = (matrix-factors[:, None]*matrix[row][None, :]) % prime
            pivots.append(column)
            if len(pivots) == matrix.shape[0]:
                break
        return matrix[:len(pivots)], pivots

    def rank(matrix):
        return len(rref(matrix)[1])

    def kernel(matrix):
        matrix = np.asarray(matrix, dtype=np.int64)
        reduced, pivots = rref(matrix)
        free = [j for j in range(matrix.shape[1]) if j not in pivots]
        answer = np.zeros((matrix.shape[1], len(free)), dtype=np.int64)
        for j, column in enumerate(free):
            answer[column, j] = 1
            answer[pivots, j] = -reduced[:, column] % prime
        return answer

    J, K = [], []
    for shift in range(2):
        first = np.zeros((40, 32), dtype=np.int64)
        second = np.zeros((32, 36), dtype=np.int64)
        for a in range(4):
            for j in range(8):
                first[8*(a+shift)+j, 8*a+j] = 1
                second[8*a+j, 9*a+j+shift] = 1
        J.append(first)
        K.append(second)
    return {"rref": rref, "rank": rank, "kernel": kernel,
            "J": J, "K": K, "prime": prime}


def discover_sparse(limit=100):
    import numpy as np
    kit = toolkit()
    prime, J, K = kit["prime"], kit["J"], kit["K"]
    rank, kernel, rref = kit["rank"], kit["kernel"], kit["rref"]
    L = []
    for index in range(4):
        p, s = divmod(index, 2)
        matrix = np.zeros((80, 32), dtype=np.int64)
        matrix[40*p:40*(p+1)] = J[s]
        L.append(matrix)
    half = pow(2, -1, prime)
    LP = [L[1], (L[0]-L[3])*half % prime, L[2]]
    profile = (3, 3, 3, 2, 2)
    for density in (2, 3, 4):
        for trial in range(limit):
            rng = np.random.default_rng(710000 + 1000*density + trial)
            generators, columns = [], []
            for length in profile:
                generator = np.zeros((5-length, 8), dtype=np.int64)
                positions = rng.choice(generator.size, density, replace=False)
                generator.ravel()[positions] = rng.choice([-1, 1], size=density)
                generators.append(generator.tolist())
                for shift in range(length):
                    vector = np.zeros((4, 8), dtype=np.int64)
                    vector[shift:shift+5-length] = generator
                    columns.append(vector.ravel())
            U = np.asarray(columns).T
            if rank(U) != 13:
                continue
            Q = kernel(U.T).T
            q0, q1 = Q @ K[0] % prime, Q @ K[1] % prime
            zero = np.zeros_like(q0)
            D = kernel(np.block([[q1, zero], [zero, q0], [q0, -q1]]) % prime)
            if D.shape[1] != 15:
                continue
            V = K[0] @ D[:36] % prime
            W = np.concatenate([matrix @ U % prime for matrix in L], axis=1)
            wpivots = rref(W)[1]
            W = W[:, wpivots]
            if W.shape[1] != 36:
                continue
            if rank(np.concatenate([W]+[matrix @ V % prime for matrix in LP], axis=1)) < 78:
                continue
            for omitted in range(15):
                selected = [j for j in range(15) if j != omitted]
                B = np.concatenate([W]+[matrix @ V[:, selected] % prime for matrix in LP], axis=1) % prime
                row_pivots = rref(B.T)[1]
                if len(row_pivots) != 78:
                    continue
                answer = {"scope": "finite-field discovery requiring exact reconstruction",
                          "prime": prime, "profile": list(profile), "generators": generators,
                          "D_basis_columns": selected, "W_basis_column_indices": wpivots,
                          "join_row_indices": row_pivots, "density": density, "trial": trial,
                          "U_dimension": 13, "W_dimension": 36, "D_dimension": 15,
                          "middle_dimension": 14, "join_rank": 78}
                path = DIRECTORY / "spin-module14-sparse-discovery.json"
                path.write_text(json.dumps(answer, indent=2)+"\n")
                print(json.dumps({k: v for k, v in answer.items() if k not in
                                  ("generators", "D_basis_columns", "W_basis_column_indices", "join_row_indices")}), flush=True)
                return answer
    raise ArithmeticError("No sparse discovery point was found")


def reconstruct(path):
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
    print(json.dumps({"exact_U": U.rank(), "exact_D": D.cols}), flush=True)
    if D.cols != 15:
        raise ArithmeticError("The rational nullspace disagrees with discovery")
    chosen = D[:, data["D_basis_columns"]]
    plus, minus = chosen[:36, :], chosen[36:, :]
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
    inverse = square.inv(method="DM")
    left_inverse = sp.zeros(78, 80)
    for j, row in enumerate(data["join_row_indices"]):
        left_inverse[:, row] = inverse[:, j]
    Y = left_inverse[36:, :]
    Z0 = sp.Matrix.vstack(sp.zeros(36, 14), plus)
    Z1 = sp.Matrix.vstack(plus/2, -minus/2)
    Z2 = sp.Matrix.vstack(minus, sp.zeros(36, 14))
    Z = sp.Matrix.hstack(Z0, Z1, Z2).T
    if Y*B != sp.Matrix.hstack(sp.zeros(42, 36), sp.eye(42)):
        raise ArithmeticError("The exact join duality failed")

    def pack(matrix):
        denominator = int(sp.ilcm(*[value.q for value in matrix]))
        entries = [[i, j, int(matrix[i, j]*denominator)]
                   for i in range(matrix.rows) for j in range(matrix.cols) if matrix[i, j]]
        return {"shape": [matrix.rows, matrix.cols], "denominator": denominator, "entries": entries}

    spin = json.loads((DIRECTORY / "parity_balancing_spin1/scalar_witness.json").read_text())
    X = sp.Matrix(spin["base_common_map_numerator"])/2
    witness = {"source": "C(2,2) cyclic tensor C(2,4) cyclic tensor C(2,8)",
               "source_dimensions": [12, 80, 72], "target": "M(3,3,14)",
               "target_dimensions": [9, 42, 42], "field": "Q",
               "source_coordinate_orders": ["(i*3+k)*2+s", "(p*5+L)*8+j", "(q*4+a)*9+H"],
               "profile": data["profile"], "generators": data["generators"],
               "D_basis_columns": data["D_basis_columns"],
               "W_basis_column_indices": data["W_basis_column_indices"],
               "join_row_indices": data["join_row_indices"],
               "join_minor_determinant": str(square.det(method="domain-ge")),
               "X": pack(X), "Y": pack(Y), "Z": pack(Z), "U_left_annihilator": pack(Q),
               "new_exponent_established": False}
    path = DIRECTORY / "spin-module14-witness.json"
    path.write_text(json.dumps(witness, indent=2)+"\n")
    print(json.dumps({"saved": str(path), "denominators": [witness[k]["denominator"] for k in "XYZ"],
                      "nonzeros": [len(witness[k]["entries"]) for k in "XYZ"],
                      "join_minor_determinant": witness["join_minor_determinant"]}), flush=True)
    return witness


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--reconstruct")
    args = parser.parse_args()
    if args.reconstruct:
        reconstruct(args.reconstruct)
    else:
        discover_sparse()
