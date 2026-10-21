"""Integral family A(a,a+1) -> M(2a-2) direct-sum M(2 floor((a-1)/2)).

Valid for a>=5.  Includes an exact A(7,8) seed with M12 and M6 blocks.
No improved exponent is claimed.
"""

from __future__ import annotations

from itertools import product
import json
from pathlib import Path

import numpy as np

from parity_structure import apply_sparse, multiplication_tensor, source_tensor


def local_data(a):
    assert a >= 5
    d, b, m = a-1, a+1, 2*a
    c = d//2
    u = np.zeros((2, a), dtype=np.int64)
    u[0, 0] = u[1, d] = 1
    v = np.zeros((d, b), dtype=np.int64)
    for j in range(1, d):
        v[j-1, j] = 1
    v[0, d] = -1
    v[-1, 0] = v[-1, d+1] = 1
    r = np.zeros((2*d, m), dtype=np.int64)
    for j in range(1, d):
        r[j-1, j] = 1
        r[d+j-1, d+j] = 1
    r[d-1, 0] = 1
    r[d, 0] = -1
    r[-1, 1] = r[-1, d] = 1
    h = np.zeros((2, m), dtype=np.int64)
    h[0, 0] = -1
    h[0, d+1] = h[0, 2*d] = 1
    h[1, 1] = h[1, d] = -1
    h[1, 2*d+1] = 1
    p = np.zeros((c, a), dtype=np.int64)
    p[0, 1] = 1
    for mu in range(1, c):
        p[mu, 2*mu] = 1
    q_mix = np.zeros((2*c, d), dtype=np.int64)
    q_mix[0, 0] = q_mix[1, -1] = -1
    for mu in range(1, c):
        q_mix[2*mu, d-2*mu] = 1
        q_mix[2*mu+1, d-2*mu-1] = -1
    q_mix[2, -1] = -1
    q = q_mix @ v
    return u, v, r, h, p, q, q_mix


def maps(a):
    u, v, r, h, p, q, _ = local_data(a)
    b, m = a+1, 2*a
    d, c = a-1, (a-1)//2
    n_core, n_extra, size = 2*d, 2*c, a*b*m
    core = [np.zeros((n_core*n_core, size), dtype=np.int64) for _ in range(3)]
    vertices = list(product(range(2), range(d)))
    for i, (ai, bi) in enumerate(vertices):
        for j, (aj, bj) in enumerate(vertices):
            core[0][n_core*i+j] = np.einsum('i,t,s->its', u[ai], r[d*aj+bi], v[bj]).reshape(-1)
    for j, (aj, bj) in enumerate(vertices):
        for k, (ak, bk) in enumerate(vertices):
            core[1][n_core*j+k] = np.einsum('j,p,t->jpt', v[bk], u[aj], r[d*ak+bj]).reshape(-1)
    for k, (ak, bk) in enumerate(vertices):
        for i, (ai, bi) in enumerate(vertices):
            core[2][n_core*k+i] = np.einsum('t,q,r->tqr', r[d*ai+bk], v[bi], u[ak]).reshape(-1)
    extra = [np.zeros((n_extra*n_extra, size), dtype=np.int64) for _ in range(3)]
    vertices = list(product(range(c), range(2)))
    for i, (ai, bi) in enumerate(vertices):
        for j, (aj, bj) in enumerate(vertices):
            extra[0][n_extra*i+j] = np.einsum('i,t,s->its', p[aj], h[bi], q[2*ai+bj]).reshape(-1)
    for j, (aj, bj) in enumerate(vertices):
        for k, (ak, bk) in enumerate(vertices):
            extra[1][n_extra*j+k] = np.einsum('j,p,t->jpt', q[2*aj+bk], p[ak], h[bj]).reshape(-1)
    for k, (ak, bk) in enumerate(vertices):
        for i, (ai, bi) in enumerate(vertices):
            extra[2][n_extra*k+i] = np.einsum('t,q,r->tqr', h[bk], q[2*ak+bi], p[ai]).reshape(-1)
    return [np.vstack((left, right)) for left, right in zip(core, extra)]


def target(n_core, n_extra):
    result = multiplication_tensor(n_core)
    result.update({tuple(index+n_core*n_core for index in point): value
                   for point, value in multiplication_tensor(n_extra).items()})
    return result


def verify(a):
    d, c = a-1, (a-1)//2
    u, v, r, h, p, q, q_mix = local_data(a)
    products = np.stack([np.convolve(left, right) for left, right in product(u, v)], axis=1)
    full_basis = np.column_stack((products, np.eye(2*a, dtype=np.int64)[:, -2:]))
    inverse = np.vstack((r, h))
    assert np.array_equal(inverse @ full_basis, np.eye(2*a, dtype=np.int64))
    assert np.array_equal(full_basis @ inverse, np.eye(2*a, dtype=np.int64))
    assert np.array_equal(q_mix @ v, q)
    for mu, lam, nu, kap in product(range(c), range(2), range(c), range(2)):
        assert int(h[lam] @ np.convolve(p[mu], q[2*nu+kap])) == int(mu == nu and lam == kap)
    matrices = maps(a)
    source = source_tensor(a, a+1)
    image = apply_sparse(source, matrices)
    assert image == target(2*d, 2*c)
    return {'a': a, 'b': a+1, 'source_format': [2*a*a*(a+1)]*3,
            'source_terms': len(source), 'square_blocks': [2*d, 2*c],
            'target_format': [4*d*d+4*c*c]*3,
            'target_terms': len(image), 'all_output_coefficients_exact': True,
            'all_mixed_coefficients_zero': True,
            'both_local_inverse_identities_exact': True,
            'complement_outer_product_identity_exact': True,
            'map_nonzero_counts': [int(np.count_nonzero(matrix)) for matrix in matrices],
            'map_max_absolute_entry': max(int(np.max(np.abs(matrix))) for matrix in matrices)}


def cropped_a78_maps():
    original = maps(7)
    rows = list(range(144))+[144+6*i+j for i, j in product(range(5), repeat=2)]
    return [matrix[rows] for matrix in original]


if __name__ == '__main__':
    examples = [verify(a) for a in (5, 6, 7)]
    cropped = cropped_a78_maps()
    assert apply_sparse(source_tensor(7, 8), cropped) == target(12, 5)
    result = {'claim': 'A(a,a+1) -> M(2a-2) direct-sum M(2 floor((a-1)/2)), a>=5',
              'examples': examples, 'a78_cropped_blocks': [12, 5],
              'a78_cropped_all_coefficients_exact': True,
              'new_exponent_established': False}
    prefix = Path(__file__).with_suffix('')
    prefix.with_name(prefix.name+'_certificate.json').write_text(json.dumps(result, indent=2)+'\n')
    full = maps(7)
    u, v, r, h, p, q, q_mix = local_data(7)
    np.savez_compressed(prefix.with_name(prefix.name+'_a78_maps.npz'),
                        A=full[0], B=full[1], C=full[2],
                        x=full[0], y=full[1], z=full[2],
                        A_cropped=cropped[0], B_cropped=cropped[1], C_cropped=cropped[2],
                        U=u, V=v, R=r, h=h, P=p, Q=q, Q_in_V=q_mix,
                        block_sizes=np.array([12, 6]), cropped_block_sizes=np.array([12, 5]))
    print(json.dumps(result, indent=2))
