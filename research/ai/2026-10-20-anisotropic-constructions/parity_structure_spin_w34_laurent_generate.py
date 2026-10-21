"""Optional exact reconstruction of a coupled channel/fiber Laurent repair."""

import json
import math
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crossed_module11 import unpack
from spin_module14 import column_entries, full_terms
from spin_module_discovery import toolkit

ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / "results/anisotropic-constructions-2026-10-20"
BASE = DIRECTORY / "parity_structure_spin_w34_full_maps.json"
OUTPUT = DIRECTORY / "parity_structure_spin_w34_laurent_maps.json"


def reconstruct():
    import numpy as np
    import sympy as sp

    data = json.loads(BASE.read_text())["restrictions"][1]["maps"]
    arrays, denominators = [], []
    for name, shape in zip("XYZ", ((9, 960), (84, 960), (84, 960))):
        matrix, denominator = unpack(data[name], shape)
        arrays.append(np.asarray(matrix, dtype=np.int64))
        denominators.append(denominator)
    X, Y, Z = arrays
    dx, dy, dz = denominators
    columns = [(p*15+L)*8+j for p in range(2) for L in range(10) for j in range(8)]
    column_position = {column: index for index, column in enumerate(columns)}
    retained = [28*vertex+channel for vertex in range(3) for channel in range(1, 28)]
    deleted = [0, 28, 56]
    alpha = 16
    selected = [28*vertex+alpha+1 for vertex in range(3)]
    inverse_x, inverse_z = column_entries(X.tolist()), column_entries(Z.tolist())
    constraints = np.zeros((9*84, 160), dtype=np.int64)
    for x, y, z in full_terms(8, 8):
        if y not in column_position:
            continue
        for tx, vx in inverse_x.get(x, ()):
            for tz, vz in inverse_z.get(z, ()):
                constraints[84*tx+tz, column_position[y]] += vx*vz
    rref = toolkit()["rref"]
    rows = rref(constraints.T)[1]
    exact_constraints = sp.Matrix(constraints[rows].tolist())
    fiber_columns = []
    for vector in exact_constraints.nullspace():
        denominator = int(sp.ilcm(*[value.q for value in vector]))
        values = [int(value*denominator) for value in vector]
        divisor = math.gcd(*values)
        values = [value//divisor for value in values]
        if next(value for value in values if value) < 0:
            values = [-value for value in values]
        fiber_columns.append(sp.Matrix(values))
    fibers = sp.Matrix.hstack(*fiber_columns)
    if fibers.cols != 8 or sp.Matrix(constraints.tolist())*fibers != sp.zeros(756, 8):
        raise ArithmeticError("The eight full-Z fibers changed")

    # Endpoint F(7,0,7): p=q=0, Y=(0,r+7,j), Z=(r,7+j,0).
    endpoint = np.zeros((81, 160), dtype=np.int64)
    for r in range(8):
        for j in range(8):
            column = (r+7)*8+j
            if column in column_position:
                endpoint[:, column_position[column]] = Z[retained, (r*15+7+j)*8]
    E = sp.Matrix(endpoint.tolist())
    YR = sp.Matrix(Y[np.ix_(retained, columns)].tolist())/dy
    YD = sp.Matrix(Y[np.ix_(deleted, columns)].tolist())/dy
    YA = sp.Matrix(Y[np.ix_(selected, columns)].tolist())/dy
    S, D, A, R = E*fibers, E*YD.T, E*YA.T, E*YR.T

    def exact_solve(matrix, rhs):
        _, pivots = matrix.rref()
        independent = matrix[:, list(pivots)]
        _, selected_rows = independent.T.rref()
        selected_rows = list(selected_rows)
        square = independent[selected_rows, :]
        coefficients = square.inv(method="DM")*rhs[selected_rows, :]
        solution = sp.zeros(matrix.cols, rhs.cols)
        for row, column in enumerate(pivots):
            solution[column, :] = coefficients[row, :]
        if matrix*solution != rhs:
            raise ArithmeticError("An endpoint correction system is inconsistent over Q")
        return solution, len(pivots)

    T, rank_s = exact_solve(S, -D)
    N0 = YD+T.T*fibers.T
    coefficients, rank_joint = exact_solve(sp.Matrix.hstack(S, A), R)
    C, B = coefficients[:8, :].T, coefficients[8:, :].T
    Y0 = YR-C*fibers.T-B*YA
    Yminus = B*N0
    if E*Y0.T != sp.zeros(81, 81) or E*N0.T != sp.zeros(81, 3):
        raise ArithmeticError("The endpoint cancellation is not exact")

    def embed(matrix):
        answer = sp.zeros(matrix.rows, 960)
        for local, original in enumerate(columns):
            answer[:, original] = matrix[:, local]
        return answer

    Z0 = sp.Matrix(Z[retained].tolist())/dz
    Z1 = sp.zeros(81, 960)
    for vertex in range(3):
        Z1[27*vertex+alpha, :] = sp.Matrix(Z[28*vertex].tolist()).T/dz

    def pack(matrix):
        denominator = int(sp.ilcm(*[value.q for value in matrix]))
        return {"shape": [matrix.rows, matrix.cols], "denominator": denominator,
                "entries": [[i, j, int(matrix[i, j]*denominator)]
                            for i in range(matrix.rows) for j in range(matrix.cols)
                            if matrix[i, j]]}

    answer = {
        "field": "Q(t)", "source": [8, 8], "target": [3, 3, 27],
        "source_coordinate_order": "(i*15+k)*8+s on every leg",
        "target_coordinate_orders": ["3*I+J", "27*J+alpha", "27*I+alpha"],
        "deleted_original_middle_channel": 0,
        "mixed_retained_middle_channel": alpha,
        "mixed_original_middle_channel": alpha+1,
        "endpoint_coordinate": [7, 0, 7],
        "maps": {"X": {"0": pack(sp.Matrix(X.tolist())/dx)},
                 "Y": {"-1": pack(embed(Yminus)), "0": pack(embed(Y0))},
                 "Z": {"0": pack(Z0), "1": pack(Z1)}},
        "auxiliary": {"full_Z_fibers": pack(embed(fibers.T)),
                      "endpoint_zero_deleted_Y_rows": pack(embed(N0)),
                      "pole_row_coefficients_B": pack(B)},
        "fiber_constraint_rank": len(rows), "full_Z_fiber_dimension": 8,
        "endpoint_fiber_rank": rank_s, "endpoint_join_rank": rank_joint,
        "pole_map_rank": int(Yminus.rank()),
        "new_exponent_established": False,
    }
    OUTPUT.write_text(json.dumps(answer, indent=2)+"\n")
    print(json.dumps({"saved": str(OUTPUT), "fiber_rank": rank_s,
                      "endpoint_join_rank": rank_joint, "pole_rank": answer["pole_map_rank"],
                      "map_terms": {name: {power: {"denominator": item["denominator"],
                                                   "nonzeros": len(item["entries"])}
                                            for power, item in values.items()}
                                    for name, values in answer["maps"].items()}}), flush=True)
    return answer


if __name__ == "__main__":
    reconstruct()
