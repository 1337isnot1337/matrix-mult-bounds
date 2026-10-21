"""Full torus objective for unrelated charge lists on the three vertex spaces.

This optional NumPy discovery module reuses the frozen streaming contraction
and adjoint. Its constructor, target indexing, and affine solver support
different leg dimensions. No numerical residual is an exact witness.
"""

import argparse
from copy import deepcopy
import hashlib
from itertools import product
import json
from pathlib import Path
from tempfile import TemporaryDirectory

import numpy as np

from parity_structure_torus_objective import TorusDirectSumObjective


class UnequalTorusDirectSumObjective(TorusDirectSumObjective):
    """A cyclic direct sum with vertex_charges[vertex][matrix_block].

    Leg i is Hom(V_(i+1), V_i). A block can be rectangular: if its three
    vertex dimensions are (n0,n1,n2), the three leg dimensions are
    (n0*n1,n1*n2,n2*n0) and its squared target norm is n0*n1*n2.
    """

    def __init__(self, a, b, vertex_charges):
        if a < 1 or b < 1 or len(vertex_charges) != 3:
            raise ValueError("Positive source lengths and exactly three vertex spaces are required")
        if not vertex_charges[0] or any(len(v) != len(vertex_charges[0]) for v in vertex_charges):
            raise ValueError("Every vertex space must have the same positive number of matrix blocks")
        self.vertex_charges = [[list(block) for block in vertex] for vertex in vertex_charges]
        if any(not block or any(not isinstance(c, (int, np.integer)) for c in block)
               for vertex in self.vertex_charges for block in vertex):
            raise ValueError("Each vertex block requires a nonempty integer charge list")
        self.a, self.b, self.long = int(a), int(b), int(a + b - 1)
        self.source_dimension = self.a * self.b * self.long
        self.block_shapes = [tuple(len(self.vertex_charges[v][block]) for v in range(3))
                             for block in range(len(self.vertex_charges[0]))]
        self.target_dimensions = tuple(sum(shape[leg] * shape[(leg + 1) % 3]
                                           for shape in self.block_shapes) for leg in range(3))
        self.normalization = sum(n0 * n1 * n2 for n0, n1, n2 in self.block_shapes)
        if self.normalization <= 0:
            raise ValueError("The complete target must have positive norm")
        self.target_offsets = [[], [], []]
        for leg in range(3):
            offset = 0
            for shape in self.block_shapes:
                self.target_offsets[leg].append(offset)
                offset += shape[leg] * shape[(leg + 1) % 3]
        source_charges = [
            [i + s - k for i, k, s in product(range(a), range(self.long), range(b))],
            [j + p - u for j, p, u in product(range(b), range(a), range(self.long))],
            [q + r - v for v, q, r in product(range(self.long), range(b), range(a))],
        ]
        target_charges = [[x - y
                           for block in range(len(self.block_shapes))
                           for x in self.vertex_charges[leg][block]
                           for y in self.vertex_charges[(leg + 1) % 3][block]]
                          for leg in range(3)]
        self.source_groups = [self._groups(charges) for charges in source_charges]
        self.target_groups = [self._groups(charges) for charges in target_charges]
        for leg in range(3):
            if any(len(rows) > len(self.source_groups[leg].get(weight, ()))
                   for weight, rows in self.target_groups[leg].items()):
                raise ValueError("A target weight space exceeds its corresponding source space")
        source_positions = [self._positions(groups) for groups in self.source_groups]
        target_positions = [self._positions(groups) for groups in self.target_groups]
        self.keys = sorted((x, y, -x - y)
                           for x in self.target_groups[0] for y in self.target_groups[1]
                           if -x - y in self.target_groups[2])
        support = {key: [] for key in self.keys}
        for i, j, p, q, r, s in product(range(a), range(b), range(a), range(b), range(a), range(b)):
            point = ((i * self.long + p + q) * b + s,
                     (j * a + p) * self.long + r + s,
                     ((i + j) * b + q) * a + r)
            entries = [source_positions[leg][column] for leg, column in enumerate(point)]
            key = tuple(entry[0] for entry in entries)
            if key in support:
                support[key].append(tuple(entry[1] for entry in entries))
        self.source_support = {key: np.asarray(rows, dtype=np.int32).reshape(-1, 3)
                               for key, rows in support.items()}
        target_support = {key: [] for key in self.keys}
        for block, (n0, n1, n2) in enumerate(self.block_shapes):
            offsets = [self.target_offsets[leg][block] for leg in range(3)]
            for i, j, k in product(range(n0), range(n1), range(n2)):
                point = (offsets[0] + i * n1 + j,
                         offsets[1] + j * n2 + k,
                         offsets[2] + k * n0 + i)
                entries = [target_positions[leg][row] for leg, row in enumerate(point)]
                key = tuple(entry[0] for entry in entries)
                target_support[key].append(tuple(entry[1] for entry in entries))
        self.target_support = {key: np.asarray(rows, dtype=np.int32).reshape(-1, 3)
                               for key, rows in target_support.items()}
        if sum(map(len, self.target_support.values())) != self.normalization:
            raise ArithmeticError("The target support does not contain every desired coefficient")
        self._layout = []
        cursor = 0
        for leg in range(3):
            for weight, rows in self.target_groups[leg].items():
                shape = (len(rows), len(self.source_groups[leg][weight]))
                length = shape[0] * shape[1]
                self._layout.append((leg, weight, shape, slice(cursor, cursor + length)))
                cursor += length
        self.variables = cursor

    def from_dense(self, matrices):
        if len(matrices) != 3:
            raise ValueError("Exactly three source maps are required")
        maps = []
        for leg, raw in enumerate(matrices):
            matrix = np.asarray(raw)
            if matrix.shape != (self.target_dimensions[leg], self.source_dimension):
                raise ValueError("A dense map has the wrong leg-specific shape")
            reconstructed = np.zeros_like(matrix)
            blocks = {}
            for weight, rows in self.target_groups[leg].items():
                columns = self.source_groups[leg][weight]
                blocks[weight] = matrix[np.ix_(rows, columns)].copy()
                reconstructed[np.ix_(rows, columns)] = blocks[weight]
            if not np.array_equal(reconstructed, matrix):
                raise ValueError("A dense map mixes distinct source and target weights")
            maps.append(blocks)
        return maps

    def to_dense(self, maps):
        result = []
        for leg in range(3):
            dtype = np.result_type(*(block.dtype for block in maps[leg].values()), float)
            matrix = np.zeros((self.target_dimensions[leg], self.source_dimension), dtype=dtype)
            for weight, rows in self.target_groups[leg].items():
                matrix[np.ix_(rows, self.source_groups[leg][weight])] = maps[leg][weight]
            result.append(matrix)
        return result

    def summary(self):
        return {
            "source_lengths": [self.a, self.b],
            "target_block_vertex_dimensions": [list(shape) for shape in self.block_shapes],
            "source_leg_dimensions": [self.source_dimension] * 3,
            "target_leg_dimensions": list(self.target_dimensions),
            "complex_map_parameters": self.variables,
            "conserving_charge_blocks": len(self.keys),
            "checked_target_coefficients": sum(int(np.prod([len(self.target_groups[leg][weight])
                                                             for leg, weight in enumerate(key)]))
                                               for key in self.keys),
            "full_target_coefficients": int(np.prod(self.target_dimensions)),
            "positive_target_normalization": self.normalization,
            "source_support_terms_stored": sum(map(len, self.source_support.values())),
            "all_target_terms_stored": sum(map(len, self.target_support.values())),
            "unequal_vertex_charge_lists_supported": True,
            "rectangular_target_blocks_supported": True,
            "quotient_equations_imposed": False,
            "charge_masked_objective": False,
            "full_target_witness": False,
        }


class UnequalAffineTorusALS:
    """Complete block least squares with leg-specific fixed coefficients."""

    def __init__(self, problem, fixed_source_columns=None, fixed_target_rows=None):
        self.problem = problem
        fixed_source_columns = [[], [], []] if fixed_source_columns is None else fixed_source_columns
        fixed_target_rows = [[], [], []] if fixed_target_rows is None else fixed_target_rows
        if len(fixed_source_columns) != 3 or len(fixed_target_rows) != 3:
            raise ValueError("Fixed source columns and target rows require one list per leg")
        self.fixed_source_columns = [set(columns) for columns in fixed_source_columns]
        self.fixed_target_rows = [set(rows) for rows in fixed_target_rows]
        self.free, self.fixed = [], []
        for leg in range(3):
            if any(not 0 <= column < problem.source_dimension for column in self.fixed_source_columns[leg]):
                raise ValueError("A fixed source column is out of range")
            if any(not 0 <= row < problem.target_dimensions[leg] for row in self.fixed_target_rows[leg]):
                raise ValueError("A fixed target row is out of range")
            free, fixed = {}, {}
            for weight in problem.target_groups[leg]:
                columns = problem.source_groups[leg][weight]
                free[weight] = np.asarray([j for j, col in enumerate(columns)
                                          if col not in self.fixed_source_columns[leg]], dtype=int)
                fixed[weight] = np.asarray([j for j, col in enumerate(columns)
                                           if col in self.fixed_source_columns[leg]], dtype=int)
            self.free.append(free)
            self.fixed.append(fixed)

    def normal_equations(self, maps, leg, weight):
        problem = self.problem
        source_size = len(problem.source_groups[leg][weight])
        target_size = len(problem.target_groups[leg][weight])
        dtype = np.result_type(*(block.dtype for chart in maps for block in chart.values()), float)
        gram = np.zeros((source_size, source_size), dtype=dtype)
        target_cross = np.zeros((target_size, source_size), dtype=dtype)
        other, last = (leg + 1) % 3, (leg + 2) % 3
        for key in problem.keys:
            if key[leg] != weight:
                continue
            middle, right = maps[other][key[other]], maps[last][key[last]]
            if not np.any(middle) or not np.any(right):
                continue
            source = problem.source_block(key).transpose(leg, other, last)
            sx, sy, sz = source.shape
            ty, tz = middle.shape[0], right.shape[0]
            first = middle @ source.transpose(1, 0, 2).reshape(sy, sx * sz)
            first = first.reshape(ty, sx, sz).transpose(1, 0, 2)
            kernel = (first.reshape(sx * ty, sz) @ right.T).reshape(sx, ty, tz)
            flat = kernel.reshape(sx, ty * tz)
            gram += flat @ flat.conj().T
            support = problem.target_support[key]
            for target_row, middle_row, last_row in support[:, [leg, other, last]]:
                target_cross[target_row] += kernel[:, middle_row, last_row].conj()
        return (gram + gram.conj().T) / 2, target_cross

    def update_block(self, maps, leg, weight, ridge=0.0, relative_cutoff=1e-12):
        if ridge < 0 or relative_cutoff < 0:
            raise ValueError("The ridge and numerical cutoff must be nonnegative")
        free, fixed = self.free[leg][weight], self.fixed[leg][weight]
        rows = self.problem.target_groups[leg][weight]
        active = np.asarray([j for j, row in enumerate(rows)
                             if row not in self.fixed_target_rows[leg]], dtype=int)
        if not len(free) or not len(active):
            return None
        gram, target_cross = self.normal_equations(maps, leg, weight)
        block = maps[leg][weight]
        restricted = gram[np.ix_(free, free)]
        rhs = target_cross[:, free].copy()
        if len(fixed):
            rhs -= block[:, fixed] @ gram[np.ix_(fixed, free)]
        values, vectors = np.linalg.eigh(restricted)
        scale = max(1.0, float(np.max(values, initial=0.0)))
        cutoff, penalty = relative_cutoff * scale, ridge * scale
        if float(np.min(values, initial=0.0)) < -1e-9 * scale:
            raise ArithmeticError("The streamed Gram matrix has a materially negative eigenvalue")
        values = np.maximum(values, 0)
        old = block[np.ix_(active, free)]
        numerator = rhs[active] + penalty * old
        denominators = values + penalty
        inverse = np.zeros_like(denominators)
        keep = denominators > (0 if penalty else cutoff)
        inverse[keep] = 1 / denominators[keep]
        updated = ((numerator @ vectors) * inverse) @ vectors.conj().T
        if not np.all(np.isfinite(updated)):
            raise ArithmeticError("The least-squares update became nonfinite")
        block[np.ix_(active, free)] = updated
        return {"leg": leg, "weight": weight, "free_source_coordinates": len(free),
                "active_target_rows": len(active), "gram_numerical_rank": int(np.sum(values > cutoff)),
                "largest_gram_eigenvalue": float(np.max(values, initial=0.0)),
                "ridge_penalty": penalty}

    def update_leg(self, maps, leg, ridge=0.0, relative_cutoff=1e-12):
        return [result for weight in self.problem.target_groups[leg]
                if (result := self.update_block(maps, leg, weight, ridge, relative_cutoff)) is not None]

    def fixed_entries_unchanged(self, reference, maps):
        for leg in range(3):
            for weight, rows in self.problem.target_groups[leg].items():
                fixed = self.fixed[leg][weight]
                frozen = [j for j, row in enumerate(rows) if row in self.fixed_target_rows[leg]]
                if not np.array_equal(reference[leg][weight][:, fixed], maps[leg][weight][:, fixed]):
                    return False
                if not np.array_equal(reference[leg][weight][frozen], maps[leg][weight][frozen]):
                    return False
        return True

    def free_gradient_norm(self, gradient):
        squared = 0.0
        for leg in range(3):
            for weight, rows in self.problem.target_groups[leg].items():
                active = [j for j, row in enumerate(rows) if row not in self.fixed_target_rows[leg]]
                values = gradient[leg][weight][np.ix_(active, self.free[leg][weight])]
                squared += float(np.vdot(values, values).real)
        return squared ** 0.5


def load_sparse_seed(path, fixed_source_columns=None, fixed_target_rows=None):
    """Read balancing's actual export; no common-charge reconstruction occurs."""
    path = Path(path)
    raw = path.read_bytes()
    data = json.loads(raw)
    problem = UnequalTorusDirectSumObjective(*data["source_lengths"], data["vertex_charges"])
    supplied_dimensions = data.get("target_dimensions")
    if supplied_dimensions is not None and tuple(supplied_dimensions) != problem.target_dimensions:
        raise ValueError("The exported target dimensions disagree with the vertex lists")
    entries = data.get("partial_maps", data.get("maps"))
    if not isinstance(entries, list) or len(entries) != 3:
        raise ValueError("The export has no three actual sparse maps")
    denominator = data.get("map_denominator", 1)
    if not isinstance(denominator, int) or denominator <= 0:
        raise ValueError("The sparse-map denominator must be a positive integer")
    dense = [np.zeros((dim, problem.source_dimension), dtype=complex) for dim in problem.target_dimensions]
    for leg, terms in enumerate(entries):
        occupied = set()
        for row, column, numerator in terms:
            if not (isinstance(row, int) and isinstance(column, int)
                    and 0 <= row < problem.target_dimensions[leg]
                    and 0 <= column < problem.source_dimension):
                raise ValueError("A sparse-map entry is out of range")
            if (row, column) in occupied:
                raise ValueError("A sparse map repeats the same coefficient")
            occupied.add((row, column))
            dense[leg][row, column] = numerator / denominator
    maps = problem.from_dense(dense)
    solver = UnequalAffineTorusALS(problem, fixed_source_columns, fixed_target_rows)
    metadata = {"seed_path": str(path), "seed_sha256": hashlib.sha256(raw).hexdigest(),
                "seed_format": data.get("format"), "map_denominator": denominator,
                "actual_sparse_entries_by_leg": [len(leg) for leg in entries]}
    return problem, maps, solver, metadata


def dense_source(a, b):
    """Independent full source array for SMALL numerical controls only."""
    middle, size = a + b - 1, a * b * (a + b - 1)
    result = np.zeros((size, size, size))
    for i, j, p, q, r, s in product(range(a), range(b), range(a), range(b), range(a), range(b)):
        result[(i * middle + p + q) * b + s,
               (j * a + p) * middle + r + s,
               ((i + j) * b + q) * a + r] = 1
    return result


def dense_target(block_shapes):
    """Build all target coefficients independently of the charge-block storage."""
    dimensions = [sum(shape[leg] * shape[(leg + 1) % 3] for shape in block_shapes)
                  for leg in range(3)]
    result = np.zeros(dimensions)
    offsets = [0, 0, 0]
    for n0, n1, n2 in block_shapes:
        for i, j, k in product(range(n0), range(n1), range(n2)):
            result[offsets[0] + n1 * i + j, offsets[1] + n2 * j + k,
                   offsets[2] + n0 * k + i] = 1
        offsets = [offsets[0] + n0 * n1, offsets[1] + n1 * n2, offsets[2] + n2 * n0]
    return result


def controls():
    """Exact nonsquare seed, full dense contraction, adjoint, and affine solves."""
    charges = [[[0, 0], [0]], [[0, 0], [0]], [[0, -1, -2], [0]]]
    problem = UnequalTorusDirectSumObjective(2, 3, charges)
    dense = [np.zeros((dim, 24)) for dim in problem.target_dimensions]
    # Integral A(2,3) -> M(2,2,3), leaving the extra scalar input zero.
    for i, j in product(range(2), repeat=2):
        dense[0][2 * i + j, (i * 4 + i + j) * 3 + j] = 1
    for j, k in product(range(2), range(3)):
        dense[1][3 * j + k, (k * 2 + j) * 4 + j] = 1
    for k, i in product(range(3), range(2)):
        dense[2][2 * k + i, ((i + k) * 3 + i) * 2] = 1
    exact_maps = problem.from_dense(dense)
    exact = problem.evaluate(exact_maps, gradient=False)
    if exact["squared_residual"] != 1 or exact["normalization"] != 13:
        raise ArithmeticError("The exact rectangular partial-target control failed")
    source = dense_source(2, 3)
    target = dense_target(problem.block_shapes)
    exact_image = np.einsum("abc,ia,jb,kc->ijk", source, *dense, optimize=True)
    if np.count_nonzero(exact_image) != 12 or np.sum((exact_image - target) ** 2) != 1:
        raise ArithmeticError("The full coefficient replay of the rectangular seed failed")
    export = {"format": "unequal-rectangular-control-v1", "source_lengths": [2, 3],
              "vertex_charges": charges, "target_dimensions": [5, 7, 7],
              "partial_maps": [[[int(row), int(column), int(matrix[row, column])]
                                 for row, column in zip(*np.nonzero(matrix))] for matrix in dense]}
    with TemporaryDirectory(prefix="unequal-torus-control-") as temporary:
        path = Path(temporary) / "seed.json"
        path.write_text(json.dumps(export))
        loaded_problem, loaded_maps, _, _ = load_sparse_seed(path)
        if loaded_problem.target_dimensions != problem.target_dimensions:
            raise ArithmeticError("The unequal sparse export changed its rectangular dimensions")
        if any(not np.array_equal(left, right)
               for left, right in zip(loaded_problem.to_dense(loaded_maps), dense)):
            raise ArithmeticError("The unequal sparse export changed an actual map coefficient")
    rng = np.random.default_rng(202610217827)
    vector = rng.normal(size=2 * problem.variables) / 5
    maps = problem.unpack(vector)
    full_maps = problem.to_dense(maps)
    image = np.einsum("abc,ia,jb,kc->ijk", source, *full_maps, optimize=True)
    direct = float(np.vdot(image - target, image - target).real) / (2 * problem.normalization)
    streamed, gradient = problem.objective(vector)
    dense_error = abs(direct - streamed)
    if dense_error > 1e-12:
        raise ArithmeticError("The unequal streamed objective differs from the full dense contraction")
    direction = rng.normal(size=len(vector))
    direction /= np.linalg.norm(direction)
    step = 1e-6
    finite = (problem.objective(vector + step * direction)[0]
              - problem.objective(vector - step * direction)[0]) / (2 * step)
    analytic = float(gradient @ direction)
    derivative_error = abs(finite - analytic) / max(1, abs(finite), abs(analytic))
    if derivative_error > 1e-7:
        raise ArithmeticError("The unequal complex adjoint failed its directional derivative control")
    # Fix different target rows and different source coordinates on each leg.
    fixed_columns = [[columns[leg % len(columns)] for columns in chart.values() if len(columns) > 1]
                     for leg, chart in enumerate(problem.source_groups)]
    fixed_rows = [[0], [1], [2]]
    solver = UnequalAffineTorusALS(problem, fixed_columns, fixed_rows)
    solve_controls = []
    for leg, weight in ((0, 0), (1, 1), (2, -2)):
        trial = deepcopy(maps)
        other, last = (leg + 1) % 3, (leg + 2) % 3
        kernel = np.einsum("abc,jb,kc->ajk", source.transpose(leg, other, last),
                           full_maps[other], full_maps[last], optimize=True)
        rows = problem.target_groups[leg][weight]
        columns = problem.source_groups[leg][weight]
        free, fixed = solver.free[leg][weight], solver.fixed[leg][weight]
        active = [j for j, row in enumerate(rows) if row not in solver.fixed_target_rows[leg]]
        flat = kernel[columns].reshape(len(columns), -1)
        rhs = target.transpose(leg, other, last)[rows].reshape(len(rows), -1).astype(complex)
        rhs -= trial[leg][weight][:, fixed] @ flat[fixed]
        expected = trial[leg][weight].copy()
        expected[np.ix_(active, free)] = np.linalg.lstsq(flat[free].T, rhs[active].T, rcond=1e-12)[0].T
        before = problem.evaluate(trial, gradient=False)["squared_residual"]
        solver.update_block(trial, leg, weight)
        after, block_gradient = problem.evaluate(trial)
        difference = float(np.max(np.abs(expected - trial[leg][weight]), initial=0))
        stationarity = float(np.max(np.abs(block_gradient[leg][weight][np.ix_(active, free)]), initial=0))
        if difference > 1e-9 or stationarity > 1e-9:
            raise ArithmeticError("An unequal block solve disagrees with dense least squares")
        if after["squared_residual"] > before + 1e-10 or not solver.fixed_entries_unchanged(maps, trial):
            raise ArithmeticError("An unequal block solve moved fixed entries or increased the loss")
        for axis in range(3):
            for key in problem.target_groups[axis]:
                if (axis, key) != (leg, weight) and not np.array_equal(trial[axis][key], maps[axis][key]):
                    raise ArithmeticError("A single-block solve modified another block")
        solve_controls.append({"leg": leg, "weight": weight, "full_dense_qr_map_difference": difference,
                               "free_block_gradient_maximum": stationarity,
                               "before_squared_residual": before,
                               "after_squared_residual": after["squared_residual"]})
    reference, trial = deepcopy(maps), deepcopy(maps)
    for leg in range(3):
        before = problem.evaluate(trial, gradient=False)["squared_residual"]
        solver.update_leg(trial, leg, ridge=1e-8)
        after = problem.evaluate(trial, gradient=False)["squared_residual"]
        if after > before + 1e-9:
            raise ArithmeticError("A regularized unequal full-leg update increased the complete residual")
    if not solver.fixed_entries_unchanged(reference, trial):
        raise ArithmeticError("A regularized unequal update moved a fixed coefficient")
    return {"problem": problem.summary(), "exact_rectangular_partial_target_terms": 12,
            "exact_partial_squared_residual": 1, "full_dense_objective_error": dense_error,
            "exact_sparse_export_roundtrip": True,
            "complex_directional_gradient_error": derivative_error,
            "single_block_controls_all_three_legs": solve_controls,
            "all_three_regularized_leg_updates_monotone": True,
            "all_leg_specific_fixed_coefficients_unchanged": True,
            "numerical_discovery_only": True, "full_target_witness": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = {"controls": controls(), "full_target_witness": False,
              "new_exponent_established": False, "numerical_discovery_only": True}
    if args.seed is not None:
        problem, maps, solver, metadata = load_sparse_seed(args.seed)
        evaluated, gradient = problem.evaluate(maps)
        report.update({**metadata, "problem": problem.summary(), "initial_evaluation": evaluated,
                       "initial_gradient_norm": solver.free_gradient_norm(gradient),
                       "optimization_steps_run": 0})
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
