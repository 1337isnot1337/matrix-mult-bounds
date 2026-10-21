"""Optional complete-map and source-row-space diagnostics for nonlocal pilots."""
from hashlib import sha256
import json
from pathlib import Path

import numpy as np

from q_metaplectic_blocks import expand


def diagnose(path):
    raw = Path(path).read_bytes()
    point = json.loads(raw)
    n, r, m = point['n'], point['target_outer'], point['n']+3
    maps = [np.array(a)+1j*np.array(b) for a, b in zip(point['maps_real'], point['maps_imag'])]
    basis = np.array(point['operator_basis_real'])+1j*np.array(point['operator_basis_imag'])
    coefficients = [np.array(point[f'{side}_operator_coefficients_real'])+
                    1j*np.array(point[f'{side}_operator_coefficients_imag']) for side in ['B', 'C']]
    reconstructed = expand(maps[0], *coefficients, basis)
    map_discrepancies = [float(np.max(np.abs(a-b))) for a, b in zip(reconstructed, maps)]
    if max(map_discrepancies) > 1e-10:
        raise ArithmeticError('The saved operator coefficients do not reconstruct the long maps.')
    rowspaces, singulars, ranks = [], [], []
    for matrix in maps:
        _, singular, vh = np.linalg.svd(matrix, full_matrices=False)
        rank = int(np.count_nonzero(singular > 1e-8*singular[0]))
        singulars.append(singular)
        ranks.append(rank)
        rowspaces.append(vh[:rank])
    a = rowspaces[0].reshape(-1, n, n)
    b = rowspaces[1].reshape(-1, 4, m)
    c = rowspaces[2].reshape(-1, m, 4)
    partial = {
        'A_first_outer': np.linalg.svd(a.transpose(1, 0, 2).reshape(n, -1), compute_uv=False),
        'A_second_outer': np.linalg.svd(a.transpose(2, 0, 1).reshape(n, -1), compute_uv=False),
        'B_inner': np.linalg.svd(b.transpose(1, 0, 2).reshape(4, -1), compute_uv=False),
        'B_output': np.linalg.svd(b.transpose(2, 0, 1).reshape(m, -1), compute_uv=False),
        'C_inner': np.linalg.svd(c.transpose(2, 0, 1).reshape(4, -1), compute_uv=False),
        'C_output': np.linalg.svd(c.transpose(1, 0, 2).reshape(m, -1), compute_uv=False)}
    coefficient_norms = [float(np.linalg.norm(c[:, :, 2:])) for c in coefficients]
    plateau = np.sqrt(1-(n+3)**2/(4*(n-1)**2))
    return {'artifact': Path(path).name, 'artifact_sha256': sha256(raw).hexdigest(),
            'operator_to_complete_map_maximum_discrepancies': map_discrepancies,
            'complete_map_singular_values': [s.tolist() for s in singulars],
            'complete_map_numerical_ranks_relative_1e_minus_8': ranks,
            'orthonormal_source_rowspace_partial_singular_values': {key: value.tolist() for key, value in partial.items()},
            'A_product_subspace_tail_norms_after_n_minus_1':
                [float(np.linalg.norm(partial[key][r:])) for key in ['A_first_outer', 'A_second_outer']],
            'long_inner_subspace_tail_norms_after2':
                [float(np.linalg.norm(partial[key][2:])) for key in ['B_inner', 'C_inner']],
            'nonproduct_operator_coefficient_norms': coefficient_norms,
            'exact_reference_projection_error_decimal': float(plateau),
            'saved_error_difference_from_reference': float(point['relative_coefficient_error']-plateau),
            'partial_singular_values_do_not_prove_exact_factorization': True,
            'matching_error_does_not_certify_the_saved_maps': True,
            'exact_coefficient_certificate': False, 'improves_omega': False}


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('checkpoints', type=Path, nargs='+')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    report = {'diagnostics': [diagnose(path) for path in args.checkpoints]}
    if args.output:
        args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
