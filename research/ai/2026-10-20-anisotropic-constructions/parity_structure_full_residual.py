"""Exact A(a,a+1) -> M(2a-2) direct-sum A(2,a-2), for a>=5.

The all-size proof is in the companion Markdown note.  This verifier uses
only Python exact fractions and integers for acceptance.  Exported floating
maps are conveniences; numerator matrices and row denominators are the
authoritative rational witness.  No improved exponent is claimed.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
import json
from math import lcm
from pathlib import Path

import numpy as np

from parity_structure import apply_sparse, multiplication_tensor, source_tensor


def exact_inverse(matrix):
    """Return an integer numerator and common positive denominator."""
    n = len(matrix)
    rows = [[Fraction(int(matrix[i, j])) for j in range(n)]
            + [Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = next(row for row in range(col, n) if rows[row][col])
        rows[col], rows[pivot] = rows[pivot], rows[col]
        value = rows[col][col]
        rows[col] = [entry/value for entry in rows[col]]
        for row in range(n):
            if row == col or not rows[row][col]:
                continue
            value = rows[row][col]
            rows[row] = [left-value*right for left, right in zip(rows[row], rows[col])]
    inverse = [row[n:] for row in rows]
    denominator = lcm(*(value.denominator for row in inverse for value in row))
    numerator = np.array([[int(value*denominator) for value in row]
                          for row in inverse], dtype=np.int64)
    assert np.array_equal(numerator @ matrix, denominator*np.eye(n, dtype=np.int64))
    assert np.array_equal(matrix @ numerator, denominator*np.eye(n, dtype=np.int64))
    return numerator, denominator


def exact_determinant(matrix):
    """Fraction-free Bareiss elimination, including row pivots."""
    entries = [[int(value) for value in row] for row in matrix]
    n, sign, previous = len(entries), 1, 1
    for col in range(n-1):
        pivot = next((row for row in range(col, n) if entries[row][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            entries[col], entries[pivot] = entries[pivot], entries[col]
            sign = -sign
        value = entries[col][col]
        for row in range(col+1, n):
            for j in range(col+1, n):
                numerator = entries[row][j]*value-entries[row][col]*entries[col][j]
                assert numerator % previous == 0
                entries[row][j] = numerator//previous
            entries[row][col] = 0
        previous = value
    return sign*entries[-1][-1]


def kernel_coefficients(d, gamma):
    """Rows are q_1(t),...,q_(d-1)(t),q_*(t), in increasing degree."""
    assert d >= 4 and gamma >= 1
    epsilon = (-1)**(d-3)
    result = np.zeros((d, d), dtype=np.int64)
    result[0, 1] = 1
    result[0, d-2] -= epsilon*gamma**(d-1)
    for j in range(2, d):
        degree = d-1-j
        result[j-1, degree] = gamma*(-gamma)**degree
        result[j-1, degree+2] = gamma**2*(-gamma)**degree
    result[-1, 0] = -1
    result[-1, d-1] = -epsilon*gamma**d
    return result


def determinant_magnitude(d, gamma):
    if d % 2 == 0:
        quotient = 1+gamma**(d+1)
    else:
        quotient = (1+(-1)**((d-1)//2)*gamma**((d+1)//2))**2
    return gamma**((d-2)*(d+1)//2)*quotient


def local_data(a, gamma=None):
    assert a >= 5
    d, b, m = a-1, a+1, 2*a
    if gamma is None:
        gamma = 2 if d % 4 == 3 else 1
    assert gamma >= 1 and determinant_magnitude(d, gamma)
    u = np.zeros((2, a), dtype=np.int64)
    u[0, 0] = u[1, d] = 1
    v = np.zeros((d, b), dtype=np.int64)
    for j in range(1, d):
        v[j-1, j] = 1
    v[0, d] = -gamma
    v[-1, 0] = v[-1, d+1] = 1
    r = np.zeros((2*d, m), dtype=np.int64)
    for j in range(1, d):
        r[j-1, j] = r[d+j-1, d+j] = 1
    r[d-1, 0] = 1
    r[d, 0] = -1
    r[-1, 1], r[-1, d] = gamma, 1
    h = np.zeros((2, m), dtype=np.int64)
    h[0, 0], h[0, d+1], h[0, 2*d] = -gamma, gamma, 1
    h[1, 1], h[1, d], h[1, 2*d+1] = -gamma, -1, 1
    p_old = np.eye(a, dtype=np.int64)[1:d]
    pencil = np.array([[[int(functional @ np.convolve(left, right))
                        for right in v] for left in p_old] for functional in h],
                      dtype=np.int64)
    coefficients = kernel_coefficients(d, gamma)
    assert abs(exact_determinant(coefficients)) == determinant_magnitude(d, gamma)
    d0q, d1q = pencil[0] @ coefficients, pencil[1] @ coefficients
    assert not np.any(d1q[:, 0]) and not np.any(d0q[:, -1])
    assert np.array_equal(d1q[:, 1:], d0q[:, :-1])
    basis = d0q[:, :-1]
    left_numerator, denominator = exact_inverse(basis)
    p_numerator = left_numerator @ p_old
    q = coefficients.T @ v
    identity = np.eye(d-1, dtype=np.int64)
    zero = np.zeros((d-1, 1), dtype=np.int64)
    assert np.array_equal(left_numerator @ d0q, denominator*np.hstack((identity, zero)))
    assert np.array_equal(left_numerator @ d1q, denominator*np.hstack((zero, identity)))
    return {'a': a, 'b': b, 'd': d, 'gamma': gamma, 'U': u, 'V': v,
            'R': r, 'h': h, 'P_old': p_old, 'P_numerator': p_numerator,
            'P_denominator': denominator, 'Q': q, 'Q_in_V': coefficients.T,
            'kernel_coefficients': coefficients, 'pencil': pencil,
            'pencil_basis': basis}


def core_maps(data):
    a, b, d = data['a'], data['b'], data['d']
    u, v, r = data['U'], data['V'], data['R']
    n, size = 2*d, a*b*(a+b-1)
    result = [np.zeros((n*n, size), dtype=np.int64) for _ in range(3)]
    vertices = list(product(range(2), range(d)))
    for i, (ai, bi) in enumerate(vertices):
        for j, (aj, bj) in enumerate(vertices):
            result[0][n*i+j] = np.einsum('i,t,s->its', u[ai], r[d*aj+bi], v[bj]).reshape(-1)
    for j, (aj, bj) in enumerate(vertices):
        for k, (ak, bk) in enumerate(vertices):
            result[1][n*j+k] = np.einsum('j,p,t->jpt', v[bk], u[aj], r[d*ak+bj]).reshape(-1)
    for k, (ak, bk) in enumerate(vertices):
        for i, (ai, bi) in enumerate(vertices):
            result[2][n*k+i] = np.einsum('t,q,r->tqr', r[d*ai+bk], v[bi], u[ak]).reshape(-1)
    return result


def numerator_maps(data):
    a, b, d = data['a'], data['b'], data['d']
    p, h, q = data['P_numerator'], data['h'], data['Q']
    size, residual_size = a*b*(a+b-1), 2*d*(d-1)
    extra = [np.zeros((residual_size, size), dtype=np.int64) for _ in range(3)]
    for row, (i, t, s) in enumerate(product(range(2), range(d), range(d-1))):
        extra[0][row] = np.einsum('i,t,s->its', p[s], h[i], q[t]).reshape(-1)
    for row, (j, p_index, t) in enumerate(product(range(d-1), range(2), range(d))):
        extra[1][row] = np.einsum('j,p,t->jpt', q[t], p[j], h[p_index]).reshape(-1)
    for row, (t, q_index, r) in enumerate(product(range(d), range(d-1), range(2))):
        extra[2][row] = np.einsum('t,q,r->tqr', h[r], q[t], p[q_index]).reshape(-1)
    return [np.vstack((left, right)) for left, right in zip(core_maps(data), extra)]


def row_denominators(data):
    d = data['d']
    return np.array([1]*(4*d*d)+[data['P_denominator']]*(2*d*(d-1)), dtype=np.int64)


def verify_local(a, gamma=None):
    data = local_data(a, gamma)
    d, denominator = data['d'], data['P_denominator']
    products = np.stack([np.convolve(left, right)
                         for left, right in product(data['U'], data['V'])], axis=1)
    basis = np.column_stack((products, np.eye(2*a, dtype=np.int64)[:, -2:]))
    inverse = np.vstack((data['R'], data['h']))
    assert np.array_equal(inverse @ basis, np.eye(2*a, dtype=np.int64))
    assert np.array_equal(basis @ inverse, np.eye(2*a, dtype=np.int64))
    for mu, lam, nu in product(range(d-1), range(2), range(d)):
        pairing = int(data['h'][lam] @ np.convolve(data['P_numerator'][mu], data['Q'][nu]))
        assert pairing == denominator*int(nu == mu+lam)
    return {'a': a, 'b': a+1, 'gamma': data['gamma'],
            'kernel_coefficient_determinant': exact_determinant(data['kernel_coefficients']),
            'pencil_basis_determinant': exact_determinant(data['pencil_basis']),
            'P_denominator': denominator,
            'both_core_inverse_identities_exact': True,
            'polynomial_kernel_identity_exact': True,
            'full_residual_convolution_identity_exact': True}


def verify_full(a, gamma=None):
    result = verify_local(a, gamma)
    data = local_data(a, gamma)
    d, denominator = data['d'], data['P_denominator']
    source, residual = source_tensor(a, a+1), source_tensor(2, d-1)
    matrices = numerator_maps(data)
    image = apply_sparse(source, matrices)
    expected = multiplication_tensor(2*d)
    expected.update({tuple(index+4*d*d for index in point): denominator**3*value
                     for point, value in residual.items()})
    assert image == expected
    denominators = row_denominators(data)
    assert all(value == int(denominators[point[0]])*int(denominators[point[1]])
               *int(denominators[point[2]]) for point, value in image.items())
    assert len(image) == (2*d)**3+(2*(d-1))**3
    result.update({'source_format': [a*(a+1)*2*a]*3, 'source_terms': len(source),
                   'matrix_block': 2*d, 'residual_parameters': [2, d-1],
                   'target_format': [6*d*d-2*d]*3, 'target_terms': len(image),
                   'matrix_block_terms': (2*d)**3, 'residual_terms': len(residual),
                   'all_output_coefficients_exact': True,
                   'all_mixed_coefficients_zero': True,
                   'numerator_nonzero_counts': [int(np.count_nonzero(matrix)) for matrix in matrices],
                   'numerator_max_absolute_entry': max(int(np.max(np.abs(matrix))) for matrix in matrices)})
    return result


def export(a, path, gamma=None):
    data = local_data(a, gamma)
    numerators = numerator_maps(data)
    denominators = row_denominators(data)
    matrices = [matrix/denominators[:, None] for matrix in numerators]
    np.savez_compressed(path, A=matrices[0], B=matrices[1], C=matrices[2],
                        x=matrices[0], y=matrices[1], z=matrices[2],
                        A_numerator=numerators[0], B_numerator=numerators[1],
                        C_numerator=numerators[2], row_denominators=denominators,
                        **{key: value for key, value in data.items()
                           if isinstance(value, np.ndarray) or isinstance(value, int)})


def export_sparse_a78(path):
    data = local_data(7)
    matrices = numerator_maps(data)
    witness = {'source_parameters': [7, 8], 'matrix_block': 12,
               'residual_parameters': [2, 5],
               'source_coordinate_order': ['i,t,s', 'j,p,u', 'v,q,r'],
               'target_order': 'M12 matrix-index rows, then A25 lexicographic rows',
               'row_denominators': row_denominators(data).tolist(),
               'numerator_maps': [[[int(col), int(row[col])] for col in np.flatnonzero(row)]
                                  for matrix in matrices for row in matrix]}
    # The outermost map axis is restored explicitly to keep row storage compact.
    witness['numerator_maps'] = [witness['numerator_maps'][204*axis:204*(axis+1)]
                                 for axis in range(3)]
    Path(path).write_text(json.dumps(witness, separators=(',', ':'))+'\n')


if __name__ == '__main__':
    full_examples = []
    for a in (5, 6, 7, 8):
        example = verify_full(a)
        full_examples.append(example)
        print(json.dumps(example), flush=True)
    local_examples = [verify_local(a, 2) for a in range(5, 12)]
    # This failure is a property of gamma=1, not of the all-size family.
    assert exact_determinant(kernel_coefficients(7, 1)) == 0
    result = {'claim': 'A(a,a+1) -> M(2a-2) direct-sum A(2,a-2), all a>=5',
              'evidence': 'written all-size proof and exact finite coefficient replays',
              'full_examples': full_examples, 'gamma_two_local_examples': local_examples,
              'original_gamma_one_d7_coefficient_basis_singular': True,
              'new_exponent_established': False}
    prefix = Path(__file__).with_suffix('')
    prefix.with_name(prefix.name+'_certificate.json').write_text(json.dumps(result, indent=2)+'\n')
    export(7, prefix.with_name(prefix.name+'_a78_maps.npz'))
    export_sparse_a78(prefix.with_name(prefix.name+'_a78_sparse.json'))
    print(json.dumps({'certificate': str(prefix.with_name(prefix.name+'_certificate.json')),
                      'a78_export': str(prefix.with_name(prefix.name+'_a78_maps.npz')),
                      'new_exponent_established': False}), flush=True)
