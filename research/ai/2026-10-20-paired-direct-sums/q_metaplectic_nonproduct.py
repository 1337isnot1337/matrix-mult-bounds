"""One Fourier/chirp-dominant start in the already tested operator space."""
from itertools import product
from pathlib import Path
import json

import numpy as np

import q_metaplectic_blocks as base


def initialize(n, seed, perturbation):
    basis, names, _, _ = base.operators(n)
    r, m, count = n-1, n+3, len(basis)
    index = np.arange(m)
    f = np.exp(2j*np.pi*np.outer(index, index)/m)/np.sqrt(m)
    g = np.diag(np.exp(1j*np.pi*index*index/m))
    operators = [f[:r], f.conj().T[:r], (f@g)[:r], (f@g.conj().T)[:r],
                 (g@f)[:r], (g.conj().T@f)[:r]]
    x, z = [np.zeros((4, 4, count), complex) for _ in range(2)]
    for alpha, y in product(range(4), repeat=2):
        raw = (1j)**(alpha*y)*operators[(alpha+2*y) % 6]/2
        x[alpha, y] = np.einsum('is,lis->l', raw, basis.conj())
    for beta, v in product(range(4), repeat=2):
        raw = (1j)**(-beta*v)*operators[(2*beta+v+3) % 6]/2
        z[beta, v] = np.einsum('is,lis->l', raw, basis.conj())
    rng = np.random.default_rng(seed)
    for coefficient in [x, z]:
        noise = rng.normal(size=coefficient[:, :, 2:].shape)+1j*rng.normal(size=coefficient[:, :, 2:].shape)
        coefficient[:, :, 2:] += perturbation*noise/np.sqrt(2*noise.size)
        coefficient *= np.sqrt(4*r)/np.linalg.norm(coefficient)
    source, target = base.problem(n)
    first = np.zeros((r*r, n*n), complex)
    environment, wanted = base.designs(base.expand(first, x, z, basis), source, target, basis, axis=0)
    gram = environment@environment.conj().T
    cross = wanted@environment.conj().T
    first, _ = base.bounded_step(np.broadcast_to(gram, (r*r, *gram.shape)), cross, 25)
    return first, x, z, basis, names


if __name__ == '__main__':
    print(json.dumps({'control': base.control()}), flush=True)
    base.initialize = initialize
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prefix', type=Path, required=True)
    args = parser.parse_args()
    prefix = args.prefix
    result = base.fit(6, 202610463, 1000, 25, 0.03, prefix)
    result['initialization'] = {
        'kind': 'Fourier/chirp-dominant nonproduct blocks',
        'raw_operator_order': ['F', 'F_inverse', 'F_G', 'F_G_inverse', 'G_F', 'G_inverse_F'],
        'B_raw_block': 'i^(alpha*y)/2 times operator[(alpha+2*y) mod6]',
        'C_raw_block': 'i^(-beta*v)/2 times operator[(2*beta+v+3) mod6]',
        'small_symmetry_breaking_perturbation_scale': 0.03,
        'first_map': 'bounded linear least squares against the complete target',
        'product_inverse_maps_used_in_initialization': False,
        'product_inverse_directions_still_allowed_during_fit': True}
    prefix.with_name(prefix.name+'-result.json').write_text(json.dumps(result, indent=2)+'\n')
