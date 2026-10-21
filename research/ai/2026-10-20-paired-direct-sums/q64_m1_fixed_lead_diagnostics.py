"""Optional numerical diagnostics for the fixed-endpoint M1 pilot.

Every contraction uses all source coefficients.  Singular values and
minimum-norm gauges are diagnostics, not exact restriction certificates.
NumPy is an optional discovery dependency and is not imported by default tests.
"""
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

import numpy as np

from q64_m1_leading_exact import embedded_product_maps, powers


def orthonormal_spaces():
    vectors = np.zeros((6, 6))
    vectors[0, 1] = 1
    vectors[1, 0] = vectors[1, 4] = 1/np.sqrt(2)
    vectors[2, 0] = 1/np.sqrt(2)
    vectors[2, 4] = -1/np.sqrt(2)
    vectors[3, 2] = vectors[4, 3] = vectors[5, 5] = 1
    kernel = np.array([np.outer(vectors[i], vectors[j]).ravel()
                       for i, j in product(range(6), repeat=2) if i >= 2 or j >= 2])
    natural_corner = np.array([np.outer(u, v).ravel()
                               for u, v in product(vectors[2:], repeat=2)])
    return kernel, natural_corner


def fixed_lead_characters():
    """Physical diagonal gauges with x0=z0=0 and the middle factor fixed."""
    rows = []
    for i, k in product(range(5), repeat=2):
        row = np.zeros(8)
        if i:
            row[i-1] = 1
        if k:
            row[3+k] = 1
        rows.append(row)
    for i, j in product(range(5), range(4)):
        row = np.zeros(8)
        if i:
            row[i-1] = -1
        rows.append(row)
    for j, k in product(range(4), range(5)):
        row = np.zeros(8)
        if k:
            row[3+k] = -1
        rows.append(row)
    return np.array(rows)


def normalize_fixed_lead(maps, tolerance=1e-13):
    """Minimize total squared map norm over the eight stated real gauges."""
    characters = fixed_lead_characters()
    raw = np.concatenate(maps, axis=0)
    energy = np.sum(np.abs(raw)**2, axis=1)
    if np.any(energy == 0):
        raise ValueError('This numerical normalizer requires nonzero target rows.')
    parameters = np.zeros(8)
    for iteration in range(100):
        weighted = energy*np.exp(2*(characters@parameters))
        objective = float(np.sum(weighted))
        moment = characters.T@weighted
        gram = characters.T@(weighted[:, None]*characters)
        stationarity = float(np.max(np.abs(moment))/objective)
        if stationarity < tolerance:
            break
        direction = -0.5*np.linalg.solve(gram, moment)
        derivative = float(2*moment@direction)
        fraction = 1.0
        for _ in range(60):
            trial = parameters+fraction*direction
            trial_value = float(np.sum(energy*np.exp(2*(characters@trial))))
            if np.isfinite(trial_value) and trial_value <= objective+1e-4*fraction*derivative:
                parameters = trial
                break
            fraction *= 0.5
        else:
            if stationarity < 1e-11:
                break
            raise ArithmeticError('The fixed-leading diagonal normalizer did not descend.')
    else:
        raise ArithmeticError('The fixed-leading diagonal normalizer did not converge.')
    normalized = raw*np.exp(characters@parameters)[:, None]
    final_energy = np.sum(np.abs(normalized)**2, axis=1)
    stationarity = float(np.max(np.abs(characters.T@final_energy))/np.sum(final_energy))
    return [normalized[:25], normalized[25:45], normalized[45:]], {
        'log_parameters_x1_to_x4_z1_to_z4': parameters.tolist(),
        'iterations': iteration,
        'relative_stationarity': stationarity,
        'combined_map_norm_before': float(np.linalg.norm(raw)),
        'combined_map_norm_after': float(np.linalg.norm(normalized)),
        'fixed_leading_rows_change_norm': float(np.linalg.norm(
            (normalized-raw)[[0, 25, 26, 27, 28, 45, 50, 55, 60]]))}


def diagnose(path):
    raw = Path(path).read_bytes()
    point = json.loads(raw)
    if not point['leading_B_C_fixed'] or not point['corner_kernel_free']:
        raise ValueError('This diagnostic is for the fixed-leading, free-kernel pilot.')
    maps = [np.array(r)+1j*np.array(i) for r, i in zip(point['maps_real'], point['maps_imag'])]
    fixed = [np.array(m) for m in embedded_product_maps()]
    if not (np.array_equal(maps[0][0], fixed[0][0]) and
            np.array_equal(maps[1][:4], fixed[1][:4]) and
            np.array_equal(maps[2][[0, 5, 10, 15]], fixed[2][[0, 5, 10, 15]])):
        raise ArithmeticError('The declared fixed leading rows changed.')
    source = np.zeros((36, 36, 36))
    target = np.zeros((25, 20, 20))
    for p, q, y, v in product(range(6), range(6), range(4), range(4)):
        source[6*p+q, 9*y+q+v, 4*(p+y)+v] = 1
    for i, j, k in product(range(5), range(4), range(5)):
        target[5*i+k, 4*i+j, 5*j+k] = 1
    weights = [np.array(w) for w in powers()]
    degree = weights[0][:, None, None]+weights[1][None, :, None]+weights[2][None, None, :]
    kernel, natural_corner = orthonormal_spaces()
    corner_rows = [5*i+k for i, k in product(range(1, 5), repeat=2)]
    new_c_rows = [5*j+k for j, k in product(range(4), range(1, 5))]
    old_c_rows = [0, 5, 10, 15]
    h0 = np.einsum('bs,ct,ast->abc', maps[1][:4], maps[2][old_c_rows], source,
                   optimize=True).reshape(36, 16)
    h1b = np.einsum('bs,ct,ast->abc', maps[1][4:], maps[2][old_c_rows], source,
                    optimize=True).reshape(36, 64)
    h1c = np.einsum('bs,ct,ast->abc', maps[1][:4], maps[2][new_c_rows], source,
                    optimize=True).reshape(36, 64)
    h1 = np.concatenate([h1b, h1c], axis=1)
    jet_singular = np.linalg.svd(kernel@h1, compute_uv=False)
    _, corner_singular, corner = np.linalg.svd(maps[0][corner_rows], full_matrices=False)
    if corner_singular[-1] <= 1e-12*corner_singular[0]:
        raise ArithmeticError('The saved corner does not have a stable 16-dimensional row span.')
    constraint_b = np.einsum('ua,jt,ast->suj', corner, maps[2][old_c_rows], source,
                             optimize=True).reshape(36, 64)
    constraint_c = np.einsum('ua,js,ast->tuj', corner, maps[1][:4], source,
                             optimize=True).reshape(36, 64)
    constraint_singular = [np.linalg.svd(m, compute_uv=False)
                           for m in [constraint_b, constraint_c]]

    def metrics(mm):
        actual = np.einsum('is,jt,ku,stu->ijk', *mm, source, optimize=True)
        error = actual-target
        derivative = 2*sum(float(np.dot(w, np.sum(np.abs(m)**2, axis=1)))
                           for w, m in zip(weights, mm))
        denominator = 2*sum(float(np.dot(np.abs(w), np.sum(np.abs(m)**2, axis=1)))
                            for w, m in zip(weights, mm))
        return {'relative_nonpositive_coefficient_error': float(np.linalg.norm(error[degree <= 0])/10),
                'negative_coefficient_norm': float(np.linalg.norm(actual[degree < 0])),
                'constant_coefficient_error_norm': float(np.linalg.norm(error[degree == 0])),
                'positive_coefficient_norm': float(np.linalg.norm(actual[degree > 0])),
                'map_norms': [float(np.linalg.norm(m)) for m in mm],
                'grading_norm_derivative': derivative,
                'relative_grading_norm_derivative': derivative/denominator}

    normal, normalizer = normalize_fixed_lead(maps)
    return {'artifact': Path(path).name, 'artifact_sha256': sha256(raw).hexdigest(),
            'fixed_leading_rows_match_exact_seed': True,
            'all_source_terms_reconstructed': 576,
            'all_target_positions_accounted': 10000,
            'all_nonpositive_positions_checked': int(np.count_nonzero(degree <= 0)),
            'raw': metrics(maps),
            'minimum_norm_fixed_leading_diagonal_representative': metrics(normal),
            'normalizer': normalizer,
            'all_A_B_C_map_singular_values': [np.linalg.svd(m, compute_uv=False).tolist() for m in maps],
            'A_non_old_times_H0_norm': float(np.linalg.norm(maps[0][1:]@h0)),
            'H1_on_K0_singular_values': jet_singular.tolist(),
            'H1_on_K0_tail_after16': float(np.linalg.norm(jet_singular[16:])),
            'corner_A_singular_values': corner_singular.tolist(),
            'orthonormal_corner_first_jet_norm': float(np.linalg.norm(corner@h1)),
            'coefficient_weighted_corner_first_jet_norm': float(np.linalg.norm(maps[0][corner_rows]@h1)),
            'natural_corner_principal_cosines': np.linalg.svd(corner@natural_corner.conj().T,
                                                               compute_uv=False).tolist(),
            'B_C_corner_constraint_singular_values': [s.tolist() for s in constraint_singular],
            'B_C_corner_constraint_numerical_ranks_relative_1e_minus_8':
                [int(np.count_nonzero(s > 1e-8*s[0])) for s in constraint_singular],
            'B_C_corner_constraint_tails_after16': [float(np.linalg.norm(s[16:])) for s in constraint_singular],
            'B_C_corner_constraint_tails_after20': [float(np.linalg.norm(s[20:])) for s in constraint_singular],
            'necessary_H1_on_K0_rank_upper_bound': 16,
            'necessary_B_C_corner_constraint_rank_upper_bound': 16,
            'rank_gate_scope': 'This fixed leading point and these monomial row powers; all 20 long-map rows must be independent.',
            'singular_values_are_numerical_diagnostics_only': True,
            'exact_coefficient_certificate': False, 'improves_omega': False}


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
