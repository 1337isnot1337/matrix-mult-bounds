"""Exact spin-1 coefficient discovery for A22 with an optional scalar.

The original full diagonal-SL2 A22 -> M3 ansatz is already excluded by
the cyclic-equivariant package.  Here the scalar correction changes the
source to A22 direct sum <1>; a passing coefficient screen is not a map.
"""

import argparse
from itertools import combinations_with_replacement, product
import json
from pathlib import Path

import numpy as np
import sympy as sp

from dense_als import DenseProblem
from parity_balancing_maps import actual
from parity_balancing_spin1_verify import verify_certificate


def w_basis():
    basis = []
    for i, k, s in product(range(2), range(3), range(2)):
        m = sp.zeros(4)
        for p, q in product(range(2), repeat=2):
            if p + q == k:
                m[2 * i + q, 2 * p + s] = 1
        basis.append(m)
    return basis


def w_coordinates(matrix):
    result = []
    for i, k, s in product(range(2), range(3), range(2)):
        p = min(k, 1)
        q = k - p
        result.append(matrix[2 * i + q, 2 * p + s])
    coordinates = sp.Matrix(result)
    reconstructed = sp.zeros(4)
    for c, b in zip(coordinates, w_basis()):
        reconstructed += c * b
    if reconstructed != matrix:
        raise ArithmeticError('Matrix is outside W')
    return coordinates


def intertwiner_basis():
    """Return all intertwiners End(sl2) -> W as integral 9 by 12 maps."""
    e = sp.Matrix([[0, 1], [0, 0]])
    f = e.T
    h = sp.diag(1, -1)
    triplet = (e, h, f)
    source_basis = w_basis()
    target_basis = []
    for i, j in product(range(3), repeat=2):
        matrix = sp.zeros(3)
        matrix[i, j] = 1
        target_basis.append(matrix)
    equations = []
    target_actions = []
    for generator in (e, f):
        physical_generator = sp.kronecker_product(generator, sp.eye(2)) - sp.kronecker_product(
            sp.eye(2), generator.T)
        source_action = sp.Matrix.hstack(*[w_coordinates(physical_generator * b - b * physical_generator)
                                          for b in source_basis])
        triplet_action = sp.Matrix.hstack(*[sp.Matrix([(generator * b - b * generator)[0, 1],
                                                     (generator * b - b * generator)[0, 0],
                                                     (generator * b - b * generator)[1, 0]])
                                          for b in triplet])
        target_action = sp.Matrix.hstack(*[sp.Matrix(list(triplet_action * b - b * triplet_action))
                                          for b in target_basis])
        target_actions.append(target_action)
        equations.append(sp.kronecker_product(sp.eye(9), source_action) -
                         sp.kronecker_product(target_action.T, sp.eye(12)))
    kernel = sp.Matrix.vstack(*equations).nullspace()
    if len(kernel) != 4:
        raise ArithmeticError(f'Expected four intertwiners, found {len(kernel)}')
    raw = []
    for vector in kernel:
        denominator = sp.ilcm(*[x.q for x in vector])
        raw.append(sp.Matrix(9, 12, [denominator * x for x in vector]))
    raising, lowering = target_actions
    cartan = raising * lowering - lowering * raising
    casimir = cartan ** 2 + 2 * (raising * lowering + lowering * raising)
    result = []
    for eigenvalue in (0, 8, 24):
        projection = sp.eye(9)
        for other in (0, 8, 24):
            if other != eigenvalue:
                projection = projection * (casimir - other * sp.eye(9)) / (eigenvalue - other)
        candidates = [projection.T * matrix for matrix in raw]
        flattened = sp.Matrix.hstack(*[sp.Matrix(list(matrix)) for matrix in candidates])
        _, pivots = flattened.rref()
        for index in pivots:
            vector = list(candidates[index])
            denominator = sp.ilcm(*[x.q for x in vector])
            integers = [int(denominator * x) for x in vector]
            divisor = abs(int(sp.igcd(*integers)))
            result.append(np.array([x // divisor for x in integers], dtype=np.int64).reshape(9, 12))
    if len(result) != 4:
        raise ArithmeticError('Irreducible projections did not recover all four intertwiners')
    return np.stack(result)


def physical_images(maps):
    basis = np.array([np.array(m).astype(np.int64) for m in w_basis()])
    return np.einsum('ax,xij->aij', maps, basis)


def source_maps(common_maps):
    permutation_y = [(p * 3 + k) * 2 + j for j, p, k in product(range(2), range(2), range(3))]
    permutation_z = [(r * 3 + k) * 2 + q for k, q, r in product(range(3), range(2), range(2))]
    return [common_maps[0], common_maps[1][:, permutation_y], common_maps[2][:, permutation_z]]


def coefficients(basis):
    matrices = [physical_images(m) for m in basis]
    return np.array([np.einsum('aij,bjk,cki->abc', matrices[i], matrices[j], matrices[k])
                     for i, j, k in product(range(4), repeat=3)]).reshape(4, 4, 4, 729)


def controls(basis, core):
    rng = np.random.default_rng(7442)
    maps = [rng.integers(-2, 3, size=(9, 12)) for _ in range(3)]
    physical = [physical_images(m) for m in maps]
    trace = np.einsum('aij,bjk,cki->abc', *physical)
    problem = DenseProblem(2, 2, (3, 3, 3), source_mode='full')
    image = actual(problem, source_maps(maps))
    if not np.array_equal(trace, image):
        raise ArithmeticError('Cyclic W trace identification failed')
    parameters = rng.integers(-2, 3, size=(3, 4))
    equivariant = [np.einsum('r,rax->ax', parameter, basis) for parameter in parameters]
    direct = actual(problem, source_maps(equivariant)).ravel()
    reduced = np.einsum('i,j,k,ijkt->t', *parameters, core)
    if not np.array_equal(direct, reduced):
        raise ArithmeticError('The intertwiner coefficient tensor failed its direct control')
    return {'w_dimension': 12, 'intertwiner_dimension': 4,
            'cyclic_W_trace_control_exact': True,
            'intertwiner_core_control_exact': True}


def symmetric_system(core, scalar_correction):
    monomials = list(combinations_with_replacement(range(4), 3))
    lookup = {term: i for i, term in enumerate(monomials)}
    design = np.zeros((729, len(monomials)), dtype=np.int64)
    for i, j, k in product(range(4), repeat=3):
        design[:, lookup[tuple(sorted((i, j, k)))]] += core[i, j, k]
    target = DenseProblem(2, 2, (3, 3, 3)).target.ravel().astype(np.int64)
    trace = np.eye(3).ravel().astype(np.int64)
    cube = np.einsum('i,j,k->ijk', trace, trace, trace).ravel()
    columns = [design, target[:, None]]
    if scalar_correction:
        columns.append(cube[:, None])
    _, row_indices = sp.Matrix(np.column_stack(columns)).T.rref()
    variables = sp.symbols('u0:4')
    correction = sp.Symbol('scalar')
    equations = []
    for row in row_indices:
        value = sum(int(design[row, j]) * sp.prod(variables[k] for k in term)
                    for j, term in enumerate(monomials)) - int(target[row])
        if scalar_correction:
            value += int(cube[row]) * correction
        equations.append(sp.expand(value))
    return equations, variables + ((correction,) if scalar_correction else ())


def export_witness(basis, output):
    numerator = (4 * basis[0] + 3 * basis[1] - 6 * basis[2] - basis[3])
    if np.any(numerator % 6):
        raise ArithmeticError('The selected intertwiner coefficients lost their common denominator')
    numerator //= 6
    denominator = 2
    base_maps = source_maps([numerator] * 3)
    trace = np.eye(3, dtype=np.int64).ravel()
    extended_maps = [np.column_stack((matrix, -denominator * trace)) for matrix in base_maps]
    p = sp.Matrix([[0, 1, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0], [0, -1, 0, 1]])
    wb = w_basis()
    for row in range(9):
        a = sp.zeros(3)
        a[row // 3, row % 3] = 1
        expected = sp.zeros(4)
        expected[:3, :3] = a
        expected[3, 0] = a[1, 0] - a[2, 1] / 2
        expected[3, 1] = -a[0, 0] + a[2, 2]
        expected[3, 2] = a[0, 1] / 2 - a[1, 2]
        expected[3, 3] = sp.trace(a)
        physical = sp.zeros(4)
        for col in range(12):
            physical += sp.Rational(int(numerator[row, col]), denominator) * wb[col]
        if p.inv() * physical * p != expected:
            raise ArithmeticError('The exact triangular block identity failed')
    certificate = {
        'source': 'A(2,2) direct sum one scalar tensor',
        'source_dimensions': [13, 13, 13], 'target': 'M3',
        'target_dimensions': [9, 9, 9], 'field': 'Q',
        'common_map_denominator': denominator,
        'map_numerators': {name: matrix.tolist() for name, matrix in zip('ABC', extended_maps)},
        'base_common_map_numerator': numerator.tolist(),
        'base_common_coordinate_order': '(i*3+k)*2+s; i,s in {0,1}, k in {0,1,2}',
        'source_coordinate_orders': ['(i*3+p+q)*2+s', '(j*2+p)*3+r+s',
                                     '((i+j)*2+q)*2+r'],
        'target_coordinate_orders': ['3*I+J', '3*J+K', '3*K+I'],
        'appended_scalar_coordinate': 12,
        'intertwiner_parameters': ['1/3', '1/4', '-1/2', '-1/12'],
        'intertwiner_target_degrees': [0, 2, 2, 4],
        'similarity_matrix_P': [list(map(int, p.row(i))) for i in range(4)],
        'triangular_identity': 'P^-1 J(A) P = [[A,0],[ell(A),tr(A)]]',
        'ell_A': ['A10-A21/2', '-A00+A22', 'A01/2-A12'],
        'scalar_source_column_on_each_leg': '-tr(A)',
        'base_source_image': 'M3 + tr(A)*tr(B)*tr(C)',
        'exact_witness_found_for_extended_source': True,
        'original_source_restriction_established': False,
        'new_exponent_established': False,
        'review_status': 'Author-checked exact certificate; no external independent review or formalization',
    }
    verification = verify_certificate(certificate)
    certificate['verification'] = verification
    (output / 'scalar_witness.json').write_text(json.dumps(certificate, indent=2) + '\n')
    np.savez_compressed(output / 'scalar_witness.npz',
                        **{name: matrix / denominator for name, matrix in zip('ABC', extended_maps)},
                        **{name + '_numerator': matrix for name, matrix in zip('ABC', extended_maps)},
                        denominator=denominator)
    np.savez_compressed(output / 'defect_maps.npz',
                        **{name: matrix / denominator for name, matrix in zip('ABC', base_maps)},
                        **{name + '_numerator': matrix for name, matrix in zip('ABC', base_maps)},
                        denominator=denominator)
    return verification


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--groebner', action='store_true')
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    basis = intertwiner_basis()
    core = coefficients(basis)
    report = {'controls': controls(basis, core),
              'source': 'full A(2,2), with a separately identified optional scalar direct summand',
              'target': 'M3 on the spin-1 vertex module',
              'map_class': 'cyclically equal diagonal-SL2 intertwiners for the symbolic systems',
              'intertwiner_basis': basis.tolist(),
              'intertwiner_target_degrees': [0, 2, 2, 4], 'systems': {},
              'exact_witness_found': False, 'new_exponent_established': False}
    np.savez_compressed(args.output / 'coefficient_core.npz', basis=basis, core=core)
    for scalar_correction in (False, True):
        equations, variables = symmetric_system(core, scalar_correction)
        record = {'variables': [str(v) for v in variables],
                  'equations': [str(v) for v in equations]}
        if args.groebner:
            gb = sp.groebner(equations, *variables, order='grevlex')
            record['groebner_basis'] = [str(p.as_expr()) for p in gb.polys]
            record['inconsistent'] = list(gb) == [1]
        report['systems']['with_scalar' if scalar_correction else 'original'] = record
        print('system', scalar_correction, record, flush=True)
    report['scalar_extended_witness'] = export_witness(basis, args.output)
    report['exact_witness_found'] = True
    report['exact_witness_source'] = 'A(2,2) direct sum one scalar tensor'
    report['original_source_restriction_established'] = False
    (args.output / 'report.json').write_text(json.dumps(report, indent=2) + '\n')


if __name__ == '__main__':
    main()
