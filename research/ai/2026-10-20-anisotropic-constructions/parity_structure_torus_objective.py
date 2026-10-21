"""Stream the full torus-conserving tensor objective and its adjoint.

This numerical discovery module stores sparse source/target support and
forms one charge block at a time. It imposes no quotient or fixed-border
equations. The denominator is the full positive target norm squared.
"""

import argparse
from collections import defaultdict
from itertools import product
import json
from pathlib import Path
import time

import numpy as np


class TorusDirectSumObjective:
    def __init__(self, a, b, block_vertex_charges):
        self.a, self.b, self.long = a, b, a + b - 1
        self.source_dimension = a * b * self.long
        self.block_vertex_charges = [list(block) for block in block_vertex_charges]
        self.block_sizes = [len(block) for block in self.block_vertex_charges]
        self.target_dimension = sum(size * size for size in self.block_sizes)
        self.normalization = sum(size ** 3 for size in self.block_sizes)
        if self.normalization <= 0:
            raise ValueError('The complete target must have positive norm')
        source_charges = [
            [i + s - k for i, k, s in product(range(a), range(self.long), range(b))],
            [j + p - u for j, p, u in product(range(b), range(a), range(self.long))],
            [q + r - v for v, q, r in product(range(self.long), range(b), range(a))]]
        target_charges = [i - j for block in self.block_vertex_charges for i in block for j in block]
        self.source_groups = [self._groups(charges) for charges in source_charges]
        self.target_groups = self._groups(target_charges)
        for leg in range(3):
            if any(len(rows) > len(self.source_groups[leg].get(weight, []))
                   for weight, rows in self.target_groups.items()):
                raise ValueError('A target charge space is larger than its source space')
        source_positions = [self._positions(groups) for groups in self.source_groups]
        target_positions = self._positions(self.target_groups)
        keys = [(x, y, -x - y) for x in self.target_groups for y in self.target_groups
                if -x - y in self.target_groups]
        self.keys = sorted(keys)
        support = {key: [] for key in self.keys}
        for i, j, p, q, r, s in product(range(a), range(b), range(a), range(b), range(a), range(b)):
            point = ((i * self.long + p + q) * b + s,
                     (j * a + p) * self.long + r + s,
                     ((i + j) * b + q) * a + r)
            entries = [source_positions[leg][column] for leg, column in enumerate(point)]
            key = tuple(entry[0] for entry in entries)
            if key in support:
                support[key].append(tuple(entry[1] for entry in entries))
        self.source_support = {key: np.asarray(rows, dtype=np.int16).reshape(-1, 3)
                               for key, rows in support.items()}
        target_support = {key: [] for key in self.keys}
        offset = 0
        for size in self.block_sizes:
            for i, j, k in product(range(size), repeat=3):
                point = (offset + i * size + j, offset + j * size + k, offset + k * size + i)
                entries = [target_positions[row] for row in point]
                key = tuple(entry[0] for entry in entries)
                target_support[key].append(tuple(entry[1] for entry in entries))
            offset += size * size
        self.target_support = {key: np.asarray(rows, dtype=np.int16).reshape(-1, 3)
                               for key, rows in target_support.items()}
        self._layout = []
        cursor = 0
        for leg in range(3):
            for weight, rows in self.target_groups.items():
                shape = len(rows), len(self.source_groups[leg][weight])
                length = int(np.prod(shape))
                self._layout.append((leg, weight, shape, slice(cursor, cursor + length)))
                cursor += length
        self.variables = cursor

    @staticmethod
    def _groups(charges):
        result = defaultdict(list)
        for index, charge in enumerate(charges):
            result[charge].append(index)
        return dict(sorted(result.items()))

    @staticmethod
    def _positions(groups):
        return {index: (weight, position) for weight, indices in groups.items()
                for position, index in enumerate(indices)}

    def source_block(self, key):
        shape = tuple(len(self.source_groups[leg][weight]) for leg, weight in enumerate(key))
        result = np.zeros(shape)
        support = self.source_support[key]
        if len(support):
            result[tuple(support.T)] = 1
        return result

    def from_dense(self, matrices):
        maps = []
        for leg, matrix in enumerate(matrices):
            if matrix.shape != (self.target_dimension, self.source_dimension):
                raise ValueError('A dense map has the wrong shape')
            reconstructed = np.zeros_like(matrix)
            blocks = {}
            for weight, rows in self.target_groups.items():
                columns = self.source_groups[leg][weight]
                block = matrix[np.ix_(rows, columns)].copy()
                blocks[weight] = block
                reconstructed[np.ix_(rows, columns)] = block
            if not np.array_equal(reconstructed, matrix):
                raise ValueError('A dense map mixes distinct torus charges')
            maps.append(blocks)
        return maps

    def pack(self, maps, complex_parameters=True):
        vector = np.empty(self.variables, dtype=complex if complex_parameters else float)
        for leg, weight, _, indices in self._layout:
            vector[indices] = maps[leg][weight].ravel()
        return np.concatenate((vector.real, vector.imag)) if complex_parameters else vector

    def unpack(self, vector, complex_parameters=True):
        if complex_parameters:
            vector = vector[:self.variables] + 1j * vector[self.variables:]
        maps = [{}, {}, {}]
        for leg, weight, shape, indices in self._layout:
            maps[leg][weight] = vector[indices].reshape(shape)
        return maps

    def evaluate(self, maps, gradient=True, return_block_errors=False):
        gradients = [{weight: np.zeros_like(block, dtype=np.result_type(block, float))
                      for weight, block in leg.items()}
                     for leg in maps] if gradient else None
        squared = 0.0
        block_errors = []
        for key in self.keys:
            matrices = [maps[leg][weight] for leg, weight in enumerate(key)]
            target_support = self.target_support[key]
            empty = [not np.any(matrix) for matrix in matrices]
            if (not gradient and any(empty)) or sum(empty) >= 2:
                error = float(len(target_support))
                squared += error
                if return_block_errors:
                    block_errors.append([list(key), error])
                continue
            left, middle, right = matrices
            tx, ty, tz = (matrix.shape[0] for matrix in matrices)
            source = self.source_block(key)
            sx, sy, sz = source.shape
            first = (left @ source.reshape(sx, sy * sz)).reshape(tx, sy, sz)
            first_flat = first.transpose(1, 0, 2).reshape(sy, tx * sz)
            second = (middle @ first_flat).reshape(ty, tx, sz).transpose(1, 0, 2)
            second_flat = second.reshape(tx * ty, sz)
            residual = (second_flat @ right.T).reshape(tx, ty, tz)
            if len(target_support):
                residual[tuple(target_support.T)] -= 1
            error = float(np.vdot(residual, residual).real)
            squared += error
            if return_block_errors:
                block_errors.append([list(key), error])
            if not gradient:
                continue
            residual_flat = residual.reshape(tx * ty, tz)
            gradients[2][key[2]] += residual_flat.T @ second_flat.conj()
            back_second = (residual_flat @ right.conj()).reshape(tx, ty, sz)
            back_second_flat = back_second.transpose(1, 0, 2).reshape(ty, tx * sz)
            gradients[1][key[1]] += back_second_flat @ first_flat.conj().T
            back_first = (middle.conj().T @ back_second_flat).reshape(sy, tx, sz).transpose(1, 0, 2)
            gradients[0][key[0]] += back_first.reshape(tx, sy * sz) @ source.reshape(sx, sy * sz).T
        if gradient:
            for leg in gradients:
                for weight in leg:
                    leg[weight] /= self.normalization
        result = {'half_squared_relative_residual': squared / (2 * self.normalization),
                  'squared_residual': squared, 'normalization': self.normalization}
        if return_block_errors:
            result['squared_errors_by_block'] = block_errors
        return (result, gradients) if gradient else result

    def objective(self, vector):
        report, gradient = self.evaluate(self.unpack(vector))
        return report['half_squared_relative_residual'], self.pack(gradient)

    def summary(self):
        return {'source_lengths': [self.a, self.b], 'target_blocks': self.block_sizes,
                'source_leg_dimension': self.source_dimension,
                'target_leg_dimension': self.target_dimension,
                'complex_map_parameters': self.variables,
                'conserving_charge_blocks': len(self.keys),
                'checked_target_coefficients': sum(np.prod([len(self.target_groups[w]) for w in key]).item()
                                                   for key in self.keys),
                'largest_source_block_entries': max(np.prod([len(self.source_groups[i][w])
                                                             for i, w in enumerate(key)]).item()
                                                   for key in self.keys),
                'full_target_coefficients': self.target_dimension ** 3,
                'positive_target_normalization': self.normalization,
                'source_support_terms_stored': sum(len(rows) for rows in self.source_support.values()),
                'quotient_equations_imposed': False, 'fixed_border_equations_imposed': False,
                'charge_masked_objective': False, 'full_target_witness': False}


def controls():
    problem = TorusDirectSumObjective(2, 2, [[0, 2], [0]])
    dense = [np.zeros((5, 12)) for _ in range(3)]
    points = ((0, 1, 1), (0, 2, 0), (1, 0, 1), (1, 1, 0))
    for row, (i, middle, s) in enumerate(points):
        dense[0][row, (i * 3 + middle) * 2 + s] = 1
        dense[1][row, (s * 2 + i) * 3 + middle] = 1
        dense[2][row, (middle * 2 + s) * 2 + i] = 1
    report = problem.evaluate(problem.from_dense(dense), gradient=False)
    if report['squared_residual'] != 1:
        raise ArithmeticError('The exact M2 plus zero scalar control failed')
    rng = np.random.default_rng(202610212701)
    vector = rng.normal(size=2 * problem.variables) / 5
    direction = rng.normal(size=len(vector))
    direction /= np.linalg.norm(direction)
    _, gradient = problem.objective(vector)
    source = np.zeros((12, 12, 12))
    for i, j, p, q, r, s in product(range(2), repeat=6):
        source[(i * 3 + p + q) * 2 + s, (j * 2 + p) * 3 + r + s,
               ((i + j) * 2 + q) * 2 + r] = 1
    random_maps = problem.unpack(vector)
    dense_random = [np.zeros((5, 12), dtype=complex) for _ in range(3)]
    for leg, matrix in enumerate(dense_random):
        for weight, rows in problem.target_groups.items():
            matrix[np.ix_(rows, problem.source_groups[leg][weight])] = random_maps[leg][weight]
    direct = np.einsum('abc,ia,jb,kc->ijk', source, *dense_random, optimize=True)
    for i, j, k in product(range(2), repeat=3):
        direct[2 * i + j, 2 * j + k, 2 * k + i] -= 1
    direct[4, 4, 4] -= 1
    direct_value = float(np.vdot(direct, direct).real) / 18
    streamed_value = problem.objective(vector)[0]
    direct_error = abs(direct_value - streamed_value)
    if direct_error > 1e-12:
        raise ArithmeticError('The streamed objective differs from the full dense contraction')
    step = 1e-6
    finite = (problem.objective(vector + step * direction)[0]
              - problem.objective(vector - step * direction)[0]) / (2 * step)
    analytic = float(gradient @ direction)
    error = abs(finite - analytic) / max(1, abs(finite), abs(analytic))
    if error > 1e-7:
        raise ArithmeticError('The streaming adjoint failed its complex derivative check')
    return {'small_exact_partial_target_squared_residual': 1,
            'small_positive_normalization': 9, 'complex_gradient_error': error,
            'full_dense_objective_error': direct_error}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--large-seed', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = {'controls': controls(), 'full_target_witness': False,
              'new_exponent_established': False}
    if args.large_seed:
        here = Path(__file__).resolve().parent
        witness = json.loads((here / 'parity_structure_torus_seed_sparse.json').read_text())
        began = time.monotonic()
        problem = TorusDirectSumObjective(8, 8, witness['full_target_vertex_charges'])
        dense = [np.zeros((778, 960)) for _ in range(3)]
        for matrix, entries in zip(dense, witness['embedded_maps']):
            for row, column, value in entries:
                matrix[row, column] = value
        result, gradient = problem.evaluate(problem.from_dense(dense), gradient=True)
        if result['squared_residual'] != 18271:
            raise ArithmeticError('The full-format exact partial seed failed')
        gradient_squared = sum(float(np.vdot(block, block).real)
                               for leg in gradient for block in leg.values())
        if gradient_squared != 0:
            raise ArithmeticError('The exact partial matrix target should be stationary')
        report['large_seed'] = {**problem.summary(), **result,
                                'exact_partial_seed_gradient_norm': gradient_squared ** 0.5,
                                'elapsed_seconds': time.monotonic() - began}
    if args.output:
        args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
