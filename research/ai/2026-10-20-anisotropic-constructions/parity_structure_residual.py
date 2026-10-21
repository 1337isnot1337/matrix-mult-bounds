"""Exact A(5,6) restriction to M8 direct-sum A(2,3).

Numerator maps are integral.  Divide each of their last 24 rows by two
to obtain the exact rational restriction.  Every coefficient is replayed.
"""

from __future__ import annotations

from itertools import product
import json
from pathlib import Path

import numpy as np

from parity_structure import apply_sparse, multiplication_tensor, source_tensor
from parity_structure_a56 import U, V, R, H, core_maps, product_matrix


P_NUMERATOR = np.array([[0, 1, 1, -1, 0],
                        [0, -1, -1, -1, 0],
                        [0, -1, 1, 1, 0]], dtype=np.int64)
Q_IN_V = np.array([[0, 0, 1, -1], [1, -1, 0, 0],
                   [1, 0, 1, 0], [0, -1, 0, 1]], dtype=np.int64)
Q = Q_IN_V @ V


def numerator_maps():
    core = core_maps(U, V, R)
    residual = [np.zeros((24, 300), dtype=np.int64) for _ in range(3)]
    for row, (i, t, s) in enumerate(product(range(2), range(4), range(3))):
        residual[0][row] = np.einsum('i,t,s->its', P_NUMERATOR[s], H[i], Q[t]).reshape(-1)
    for row, (j, p, t) in enumerate(product(range(3), range(2), range(4))):
        residual[1][row] = np.einsum('j,p,t->jpt', Q[t], P_NUMERATOR[j], H[p]).reshape(-1)
    for row, (t, q, r) in enumerate(product(range(4), range(3), range(2))):
        residual[2][row] = np.einsum('t,q,r->tqr', H[r], Q[t], P_NUMERATOR[q]).reshape(-1)
    return [np.vstack((left, right)) for left, right in zip(core, residual)]


def row_denominators():
    return np.array([1]*64+[2]*24, dtype=np.int64)


def verify():
    assert not np.any(H @ product_matrix(U, V))
    assert np.array_equal(Q_IN_V @ V, Q)
    for mu, lam, nu in product(range(3), range(2), range(4)):
        pairing = int(H[lam] @ np.convolve(P_NUMERATOR[mu], Q[nu]))
        assert pairing == 2*int(nu == mu+lam)
    source = source_tensor(5, 6)
    residual_source = source_tensor(2, 3)
    maps = numerator_maps()
    image = apply_sparse(source, maps)
    expected = multiplication_tensor(8)
    expected.update({tuple(index+64 for index in point): 8*value
                     for point, value in residual_source.items()})
    assert image == expected
    denominators = row_denominators()
    assert all(value == int(np.prod(denominators[list(point)]))
               for point, value in image.items())
    assert len(image) == 8**3+(2*3)**3 == 728
    return {'scope': 'exact ordinary restriction; no improved exponent',
            'source': 'A(5,6)', 'source_format': [300]*3,
            'source_terms': len(source), 'target': 'M8 direct-sum A(2,3)',
            'target_format': [88]*3, 'target_terms': len(image),
            'matrix_block_terms': 512, 'residual_terms': 216,
            'all_output_coefficients_exact': True,
            'all_mixed_coefficients_zero': True,
            'numerator_map_shapes': [[88, 300]]*3,
            'row_denominators': {'rows_0_through_63': 1, 'rows_64_through_87': 2},
            'numerator_nonzero_counts': [int(np.count_nonzero(matrix)) for matrix in maps],
            'numerator_max_absolute_entry': max(int(np.max(np.abs(matrix))) for matrix in maps),
            'P_numerator': P_NUMERATOR.tolist(), 'P_denominator': 2,
            'Q': Q.tolist(), 'Q_in_V': Q_IN_V.tolist(),
            'h': H.tolist(), 'local_convolution_identity_exact': True,
            'new_exponent_established': False}


if __name__ == '__main__':
    result = verify()
    prefix = Path(__file__).with_suffix('')
    prefix.with_name(prefix.name+'_certificate.json').write_text(json.dumps(result, indent=2)+'\n')
    numerators = numerator_maps()
    denominators = row_denominators()
    maps = [matrix/denominators[:, None] for matrix in numerators]
    np.savez_compressed(prefix.with_name(prefix.name+'_maps.npz'),
                        A=maps[0], B=maps[1], C=maps[2],
                        x=maps[0], y=maps[1], z=maps[2],
                        A_numerator=numerators[0], B_numerator=numerators[1],
                        C_numerator=numerators[2], row_denominators=denominators,
                        U=U, V=V, R=R, h=H, P_numerator=P_NUMERATOR,
                        P_denominator=2, Q=Q, Q_in_V=Q_IN_V)
    print(json.dumps({key: value for key, value in result.items()
                      if key not in {'P_numerator', 'Q', 'Q_in_V', 'h'}}, indent=2))
