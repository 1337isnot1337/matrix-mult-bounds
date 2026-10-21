"""Integral A(5,6) restrictions to M10 and to M8 direct-sum M4.

All source coefficients and all output coefficients are checked with exact
Python integers.  These constructions do not improve an exponent bound.
"""

from __future__ import annotations

from itertools import product
import json
from pathlib import Path

import numpy as np

from parity_structure import apply_sparse, multiplication_tensor, source_tensor


A, B, M = 5, 6, 10
U = np.array([[1, 0, 0, 0, 0], [0, 0, 0, 0, 1]], dtype=np.int64)
V = np.array([[0, 1, 0, 0, -1, 0],
              [0, 0, 1, 0, 0, 0],
              [0, 0, 0, 1, 0, 0],
              [1, 0, 0, 0, 0, 1]], dtype=np.int64)
R = np.array([[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
              [-1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 1, 0, 0, 1, 0, 0, 0, 0, 0]], dtype=np.int64)
H = np.array([[-1, 0, 0, 0, 0, 1, 0, 0, 1, 0],
              [0, -1, 0, 0, -1, 0, 0, 0, 0, 1]], dtype=np.int64)
P = np.array([[0, 1, 0, 0, 0], [0, 0, 1, 0, 0]], dtype=np.int64)
Q = np.array([[0, -1, 0, 0, 1, 0],
              [-1, 0, 0, 0, 0, -1],
              [-1, 0, 0, 1, 0, -1],
              [0, 0, -1, 0, 0, 0]], dtype=np.int64)
Q_IN_V = np.array([[-1, 0, 0, 0], [0, 0, 0, -1],
                   [0, 0, 1, -1], [0, -1, 0, 0]], dtype=np.int64)


def product_matrix(u, v):
    return np.stack([np.convolve(left, right) for left, right in product(u, v)], axis=1)


def core_maps(u, v, r):
    """Cyclic outer-product maps; vertices have labels (alpha,beta)."""
    nu, nv = len(u), len(v)
    n = nu*nv
    vertices = list(product(range(nu), range(nv)))
    maps = [np.zeros((n*n, A*B*M), dtype=np.int64) for _ in range(3)]
    for i, (ai, bi) in enumerate(vertices):
        for j, (aj, bj) in enumerate(vertices):
            maps[0][n*i+j] = np.einsum('i,t,s->its', u[ai], r[nv*aj+bi], v[bj]).reshape(-1)
    for j, (aj, bj) in enumerate(vertices):
        for k, (ak, bk) in enumerate(vertices):
            maps[1][n*j+k] = np.einsum('j,p,t->jpt', v[bk], u[aj], r[nv*ak+bj]).reshape(-1)
    for k, (ak, bk) in enumerate(vertices):
        for i, (ai, bi) in enumerate(vertices):
            maps[2][n*k+i] = np.einsum('t,q,r->tqr', r[nv*ai+bk], v[bi], u[ak]).reshape(-1)
    return maps


def extra_m4_maps():
    """Cyclic maps from h_lambda(P_mu Q_nu,kappa)=delta_mu,nu delta_lambda,kappa."""
    vertices = list(product(range(2), repeat=2))
    maps = [np.zeros((16, A*B*M), dtype=np.int64) for _ in range(3)]
    for i, (ai, bi) in enumerate(vertices):
        for j, (aj, bj) in enumerate(vertices):
            maps[0][4*i+j] = np.einsum('i,t,s->its', P[aj], H[bi], Q[2*ai+bj]).reshape(-1)
    for j, (aj, bj) in enumerate(vertices):
        for k, (ak, bk) in enumerate(vertices):
            maps[1][4*j+k] = np.einsum('j,p,t->jpt', Q[2*aj+bk], P[ak], H[bj]).reshape(-1)
    for k, (ak, bk) in enumerate(vertices):
        for i, (ai, bi) in enumerate(vertices):
            maps[2][4*k+i] = np.einsum('t,q,r->tqr', H[bk], Q[2*ak+bi], P[ai]).reshape(-1)
    return maps


def direct_sum_maps():
    core = core_maps(U, V, R)
    extra = extra_m4_maps()
    return [np.vstack((left, right)) for left, right in zip(core, extra)]


def m10_data():
    v = np.array([[1, 0, 0, 0, 0, 1],
                  [0, 1, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 1, 0]], dtype=np.int64)
    r = np.zeros((10, 10), dtype=np.int64)
    r[0, 0] = r[1, 1] = r[2, 2] = r[3, 3] = r[4, 4] = 1
    r[4, 9] = -1
    r[5, 9] = r[6, 5] = r[7, 6] = r[8, 7] = r[9, 8] = 1
    r[6, 0] = -1
    return v, r, core_maps(U, v, r)


def direct_sum_tensor(sizes):
    result = {}
    offset = 0
    for n in sizes:
        result.update({tuple(index+offset for index in point): value
                       for point, value in multiplication_tensor(n).items()})
        offset += n*n
    return result


def verify():
    local_products = product_matrix(U, V)
    assert np.array_equal(R @ local_products, np.eye(8, dtype=np.int64))
    assert not np.any(H @ local_products)
    full_basis = np.column_stack((local_products, np.eye(10, dtype=np.int64)[:, 8:]))
    inverse = np.vstack((R, H))
    assert np.array_equal(inverse @ full_basis, np.eye(10, dtype=np.int64))
    assert np.array_equal(full_basis @ inverse, np.eye(10, dtype=np.int64))
    assert np.array_equal(Q_IN_V @ V, Q)
    for mu, ell, nu, kappa in product(range(2), repeat=4):
        value = int(H[ell] @ np.convolve(P[mu], Q[2*nu+kappa]))
        assert value == int(mu == nu and ell == kappa)

    source = source_tensor(A, B)
    assert len(source) == 27000
    direct_maps = direct_sum_maps()
    expected = direct_sum_tensor((8, 4))
    image = apply_sparse(source, direct_maps)
    assert image == expected
    assert len(image) == 8**3+4**3 == 576
    v10, r10, maps10 = m10_data()
    products10 = product_matrix(U, v10)
    assert np.array_equal(r10 @ products10, np.eye(10, dtype=np.int64))
    assert np.array_equal(products10 @ r10, np.eye(10, dtype=np.int64))
    image10 = apply_sparse(source, maps10)
    assert image10 == multiplication_tensor(10)

    return {'scope': 'exact integral restrictions, not an exponent improvement',
            'source': 'A(5,6)', 'source_format': [300]*3, 'source_terms': len(source),
            'direct_sum': {'blocks': [8, 4], 'target_format': [80]*3,
                           'terms': len(image), 'all_output_coefficients_exact': True,
                           'local_full_basis_inverse_both_sides_exact': True,
                           'complement_outer_product_identity_exact': True,
                           'mixed_block_coefficients_all_zero': True,
                           'map_nonzero_counts': [int(np.count_nonzero(v)) for v in direct_maps],
                           'map_max_absolute_entry': max(int(np.max(np.abs(v))) for v in direct_maps),
                           'U': U.tolist(), 'V': V.tolist(), 'R': R.tolist(),
                           'h': H.tolist(), 'P': P.tolist(), 'Q': Q.tolist(),
                           'Q_in_V': Q_IN_V.tolist()},
            'single_block': {'size': 10, 'target_format': [100]*3, 'terms': len(image10),
                             'all_output_coefficients_exact': True,
                             'local_inverse_both_sides_exact': True,
                             'map_nonzero_counts': [int(np.count_nonzero(v)) for v in maps10],
                             'V': v10.tolist(), 'R': r10.tolist()},
            'new_exponent_established': False}


if __name__ == '__main__':
    result = verify()
    prefix = Path(__file__).with_suffix('')
    prefix.with_name(prefix.name+'_certificate.json').write_text(json.dumps(result, indent=2)+'\n')
    direct = direct_sum_maps()
    np.savez_compressed(prefix.with_name(prefix.name+'_m8_m4_maps.npz'),
                        A=direct[0], B=direct[1], C=direct[2],
                        x=direct[0], y=direct[1], z=direct[2],
                        U=U, V=V, R=R, h=H, P=P, Q=Q, Q_in_V=Q_IN_V,
                        block_sizes=np.array([8, 4]), block_offsets=np.array([0, 64]))
    v10, r10, maps10 = m10_data()
    np.savez_compressed(prefix.with_name(prefix.name+'_m10_maps.npz'),
                        A=maps10[0], B=maps10[1], C=maps10[2],
                        x=maps10[0], y=maps10[1], z=maps10[2], U=U, V=v10, R=r10)
    print(json.dumps({key: value for key, value in result.items()
                      if key not in {'direct_sum', 'single_block'}}, indent=2))
    for label in ('direct_sum', 'single_block'):
        print(json.dumps({key: value for key, value in result[label].items()
                          if key not in {'U', 'V', 'R', 'h', 'P', 'Q', 'Q_in_V'}}, indent=2))
