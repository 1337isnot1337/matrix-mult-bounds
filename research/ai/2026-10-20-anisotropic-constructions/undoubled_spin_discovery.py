"""Optional finite-field discovery for the undoubled (2,8,8) spin source.

This records discovery candidates only. Rational reconstruction and complete
original-source coefficient checks are required before accepting a map.
"""

import argparse
import json
from pathlib import Path

import numpy as np

from spin_module_discovery import toolkit


ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "results/anisotropic-constructions-2026-10-20"


def matrices(m=8, n=8):
    J, K = [], []
    for shift in range(2):
        first = np.zeros(((m+1)*n, m*n), dtype=np.int64)
        second = np.zeros((m*n, m*(n+1)), dtype=np.int64)
        for a in range(m):
            for j in range(n):
                first[(a+shift)*n+j, a*n+j] = 1
                second[a*n+j, a*(n+1)+j+shift] = 1
        J.append(first)
        K.append(second)
    L = []
    for p, s in ((0, 0), (0, 1), (1, 0), (1, 1)):
        matrix = np.zeros((2*(m+1)*n, m*n), dtype=np.int64)
        matrix[p*(m+1)*n:(p+1)*(m+1)*n] = J[s]
        L.append(matrix)
    return J, K, L


def discover(trials=6):
    kit = toolkit()
    prime = kit['prime']
    rank, kernel, rref = kit['rank'], kit['kernel'], kit['rref']
    _, K, L = matrices()
    LP = [L[1], (L[0]-L[3])*pow(2, -1, prime) % prime, L[2]]
    profiles = [(7, 7, 6, 6), (7, 7, 7, 5), (8, 6, 6, 6),
                (8, 7, 6, 5), (8, 7, 7, 4), (8, 8, 5, 5),
                (8, 8, 6, 4), (8, 8, 7, 3), (8, 8, 8, 2)]
    records = []
    best = 0
    for pi, profile in enumerate(profiles):
        for density in (3, 5):
            for trial in range(trials):
                seed = 821000 + 10000*pi + 100*density + trial
                rng = np.random.default_rng(seed)
                generators, columns = [], []
                for length in profile:
                    generator = np.zeros((9-length, 8), dtype=np.int64)
                    positions = rng.choice(generator.size, min(density, generator.size), replace=False)
                    generator.ravel()[positions] = rng.choice([-1, 1], size=len(positions))
                    generators.append(generator.tolist())
                    for shift in range(length):
                        vector = np.zeros((8, 8), dtype=np.int64)
                        vector[shift:shift+9-length] = generator
                        columns.append(vector.ravel())
                U = np.asarray(columns).T
                udim = rank(U)
                record = {'profile': list(profile), 'density': density, 'trial': trial,
                          'seed': seed, 'U_dimension': udim}
                records.append(record)
                if udim != 26:
                    continue
                Q = kernel(U.T).T
                q0, q1 = Q@K[0] % prime, Q@K[1] % prime
                zero = np.zeros_like(q0)
                D = kernel(np.block([[q1, zero], [zero, q0], [q0, -q1]]) % prime)
                V = K[0]@D[:72] % prime
                Wfull = np.concatenate([matrix@U % prime for matrix in L], axis=1)
                wpivots = rref(Wfull)[1]
                W = Wfull[:, wpivots]
                full = np.concatenate([W]+[matrix@V % prime for matrix in LP], axis=1)
                join = rank(full)
                record.update(W_dimension=W.shape[1], D_dimension=D.shape[1], full_join_rank=join)
                if join > best:
                    best = join
                    print(json.dumps({'best_full_join': best, **record}), flush=True)
                if W.shape[1] != 60 or D.shape[1] < 28 or join < 144:
                    continue
                choices = [list(range(28)), list(range(D.shape[1]-28, D.shape[1]))]
                choices.extend(sorted(rng.choice(D.shape[1], 28, replace=False).tolist()) for _ in range(8))
                for selected in choices:
                    B = np.concatenate([W]+[matrix@V[:, selected] % prime for matrix in LP], axis=1) % prime
                    if rank(B) != 144:
                        continue
                    candidate = {'scope': 'finite-field candidate; rational acceptance missing',
                                 'source_parameters': [2, 8, 8], 'prime': prime,
                                 **record, 'generators': generators, 'D_basis_columns': selected,
                                 'W_basis_column_indices': wpivots, 'join_row_indices': list(range(144)),
                                 'target': [3, 3, 28], 'rational_map_verified': False,
                                 'new_exponent_established': False}
                    (RESULTS/'undoubled-spin-candidate.json').write_text(json.dumps(candidate, indent=2)+'\n')
                    report = {'scope': 'bounded finite-field discovery', 'records': records,
                              'candidate_found': True, 'new_exponent_established': False}
                    (RESULTS/'undoubled-spin-discovery.json').write_text(json.dumps(report, indent=2)+'\n')
                    print(json.dumps({'candidate_found': True, 'trial_count': len(records), **record}), flush=True)
                    return candidate
    report = {'scope': 'bounded finite-field discovery', 'records': records,
              'candidate_found': False, 'largest_full_join_rank': best,
              'rational_map_verified': False, 'new_exponent_established': False,
              'source_parameters': [2, 8, 8], 'prime': prime,
              'profiles_tested': len(profiles), 'densities': [3, 5],
              'trials_per_profile_density': trials,
              'verification_scope': 'bounded exact arithmetic over F65521; no characteristic-zero maps'}
    (RESULTS/'undoubled-spin-discovery.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k: v for k, v in report.items() if k != 'records'}), flush=True)
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--trials', type=int, default=6)
    args = parser.parse_args()
    discover(args.trials)
