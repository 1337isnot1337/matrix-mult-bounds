"""Optional full-spectrum diagnostics for the completed partial-M4 pilot."""
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

import numpy as np

from reduced_corner_replay import SOURCE, source_terms


def diagnose(path):
    raw = Path(path).read_bytes()
    point = json.loads(raw)
    pairs = [(i, k) for i, k in product(range(4), repeat=2) if i != k]
    if point['target_A_pairs'] != [list(p) for p in pairs] or point['auxiliary_rank'] != 0:
        raise ValueError('The target or scalar cost changed.')
    maps = [np.array(r)+1j*np.array(i) for r, i in zip(point['maps_real'], point['maps_imag'])]
    source = np.zeros((16, 18, 18))
    target = np.zeros((12, 16, 16))
    for a, b, c, value in source_terms():
        source[a, b, c] += value
    for a, (i, k) in enumerate(pairs):
        for j in range(4):
            target[a, 4*i+j, 4*j+k] = 1
    actual = np.einsum('is,jt,ku,stu->ijk', *maps, source, optimize=True)
    map_singular = [np.linalg.svd(m, compute_uv=False) for m in maps]
    tensor_singular = [np.linalg.svd(np.moveaxis(actual, axis, 0).reshape(actual.shape[axis], -1),
                                    compute_uv=False) for axis in range(3)]
    target_singular = [np.linalg.svd(np.moveaxis(target, axis, 0).reshape(target.shape[axis], -1),
                                    compute_uv=False) for axis in range(3)]
    numerical_ranks = [int(np.count_nonzero(s > 1e-8*s[0])) for s in tensor_singular]
    return {'artifact': Path(path).name, 'artifact_sha256': sha256(raw).hexdigest(),
            'source_certificate_sha256': sha256(SOURCE.read_bytes()).hexdigest(),
            'all_source_terms_reconstructed': 90,
            'all_target_positions_checked': 3072,
            'map_singular_values': [s.tolist() for s in map_singular],
            'map_numerical_ranks_relative_1e_minus_8':
                [int(np.count_nonzero(s > 1e-8*s[0])) for s in map_singular],
            'actual_tensor_flattening_singular_values': [s.tolist() for s in tensor_singular],
            'actual_tensor_numerical_ranks_relative_1e_minus_8': numerical_ranks,
            'target_flattening_singular_values': [s.tolist() for s in target_singular],
            'relative_error_floor_if_that_numerical_rank_were_exact':
                [float(np.linalg.norm(s[rank:])/np.sqrt(48)) for s, rank in zip(target_singular, numerical_ranks)],
            'relative_full_coefficient_error': float(np.linalg.norm(actual-target)/np.sqrt(48)),
            'rank_floor_is_conditional_on_exact_rank': True,
            'small_singular_values_do_not_prove_exact_rank': True,
            'no_rank14_claim_for_the_long_maps': True,
            'auxiliary_rank': 0, 'exact_coefficient_certificate': False,
            'nonexistence_proved': False, 'improves_omega': False}


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('checkpoint', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = diagnose(args.checkpoint)
    if args.output:
        args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
