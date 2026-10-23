"""Optional rational discovery for changing the spin module's existing Y maps.

The exported maps require a separate complete integer replay.  NumPy and
SymPy are used only here, not by that replay.  The source first and Z
maps remain fixed, and the Y support keeps physical first index p<2.
"""

from collections import defaultdict
import hashlib
import json
from math import lcm
from pathlib import Path
import sys

import numpy as np
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from parity_structure_spin_endpoint import source_terms, coordinate


ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / "results/anisotropic-constructions-2026-10-20"
SOURCE = DIRECTORY / "spin-module14-full-maps.json"
OUTPUT = DIRECTORY / "parity_structure_spin_endpoint_maps.json"
DISCOVERY = DIRECTORY / "parity_structure_spin_endpoint_discovery.json"


def to_mod(matrix, prime):
    return np.array([[int(value.p)*pow(int(value.q), -1, prime) % prime
                      for value in row] for row in matrix.tolist()], dtype=np.int64)


def modular_toolkit(prime=65521):
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
    return {"prime": prime, "rref": rref}


def generate():
    kit = modular_toolkit()
    prime = kit["prime"]
    old = json.loads(SOURCE.read_text())["restrictions"][1]["maps"]
    maps = {"X": old["X"]["entries"], "Y": [], "Z": []}
    for name in ("Y", "Z"):
        for row, column, value in old[name]["entries"]:
            vertex, alpha = divmod(row, 28)
            if alpha < 27:
                maps[name].append([27*vertex+alpha, column, value])
    x_by_column, z_by_column = defaultdict(list), defaultdict(list)
    for row, column, value in maps["X"]:
        x_by_column[column].append((row, value))
    for row, column, value in maps["Z"]:
        z_by_column[column].append((row, value))
    fixed = np.zeros((9*81, 960), dtype=np.int64)
    endpoint = np.zeros((81, 960), dtype=np.int64)
    endpoint_column = coordinate(7, 0, 7)
    for x, y, z in source_terms():
        zs = z_by_column.get(z, ())
        for rx, vx in x_by_column.get(x, ()):
            for rz, vz in zs:
                fixed[81*rx+rz, y] += vx*vz
        if x == endpoint_column:
            for rz, vz in zs:
                endpoint[rz, y] += vz
    old_y = np.zeros((81, 960), dtype=np.int64)
    for row, column, value in maps["Y"]:
        old_y[row, column] = value

    # The fixed first map has only even final short indices. Consequently
    # its row-kernel computation splits into the two source parity copies.
    copies = [[coordinate(p, e+2*ell, j)
               for p in range(2) for ell in range(5) for j in range(8)]
              for e in range(2)]
    old_columns = sorted(copies[0]+copies[1])
    active = old_columns
    positions = {column: i for i, column in enumerate(active)}
    kernel_vectors = []
    copy_ranks = []
    for columns in copies:
        independent_rows = kit["rref"](fixed[:, columns].T)[1]
        small = sp.Matrix(fixed[np.ix_(independent_rows, columns)].tolist())
        nullspace = small.nullspace()
        copy_ranks.append(len(independent_rows))
        for vector in nullspace:
            lifted = sp.zeros(len(active), 1)
            for column, value in zip(columns, vector):
                lifted[positions[column]] = value
            kernel_vectors.append(lifted)
    kernel = sp.Matrix.hstack(*kernel_vectors)
    if sp.Matrix(fixed[:, active].tolist())*kernel != sp.zeros(729, kernel.cols):
        raise ArithmeticError("The rational deformation directions do not preserve the module")
    endpoint_matrix = sp.Matrix(endpoint[:, active].tolist())*kernel
    rhs = -sp.Matrix((endpoint@old_y.T).tolist())
    endpoint_mod = to_mod(endpoint_matrix, prime)
    columns = kit["rref"](endpoint_mod)[1]
    rows = kit["rref"](endpoint_mod[:, columns].T)[1]
    minor = endpoint_matrix.extract(rows, columns)
    selected_solution = minor.inv()*rhs.extract(rows, list(range(81)))
    solution = sp.zeros(kernel.cols, 81)
    for k, column in enumerate(columns):
        solution[column, :] = selected_solution[k, :]
    if endpoint_matrix*solution != rhs:
        raise ArithmeticError("The exact endpoint cancellation system is inconsistent")
    delta = kernel*solution
    if sp.Matrix(fixed[:, active].tolist())*delta != sp.zeros(729, 81):
        raise ArithmeticError("The actual correction changes a required module coefficient")
    dy = old["Y"]["denominator"]
    rational_entries = []
    denominator = 1
    for row in range(81):
        for j, column in enumerate(active):
            value = (sp.Rational(int(old_y[row, column]))+delta[j, row])/dy
            if value:
                denominator = lcm(denominator, int(value.q))
                rational_entries.append((row, column, value))
    y_entries = [[row, column, int(value*denominator)]
                 for row, column, value in rational_entries]
    answer = {"source": [8, 8], "target": [3, 3, 27], "field": "Q",
              "target_coordinate_orders": ["3*I+J", "27*J+alpha", "27*I+alpha"],
              "source_coordinate_order": "F(i,k,s) -> (15*i+k)*8+s on each leg",
              "last_leg_convention": "row27*I+alpha denotes Z_(alpha,I)",
              "vanishing_first_response_coordinate": [7, 0, 7],
              "maps": {
                  "X": {"shape": [9, 960], "denominator": old["X"]["denominator"], "entries": maps["X"]},
                  "Y": {"shape": [81, 960], "denominator": denominator, "entries": sorted(y_entries)},
                  "Z": {"shape": [81, 960], "denominator": old["Z"]["denominator"], "entries": maps["Z"]}},
              "new_exponent_established": False}
    record = {"starting_full_map_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              "deleted_original_channel": 27,
              "first_and_Z_maps_unchanged_after_channel_deletion": True,
              "Y_physical_first_indices": [0, 1],
              "copy_constraint_ranks": copy_ranks, "old_active_Y_columns": len(old_columns),
              "added_Y_columns": [], "all_active_Y_columns": len(active),
              "rational_correction_kernel_dimension": kernel.cols,
              "endpoint_linear_map_rank": len(columns),
              "exact_correction_preserves_all_core_coefficients": True,
              "exact_endpoint_matrix_annihilated": True,
              "new_Y_denominator": denominator, "new_Y_nonzero_entries": len(y_entries),
              "new_exponent_established": False}
    OUTPUT.write_text(json.dumps(answer, separators=(",", ":"))+"\n")
    DISCOVERY.write_text(json.dumps(record, indent=2)+"\n")
    return record


if __name__ == "__main__":
    print(json.dumps(generate(), indent=2))
