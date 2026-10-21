"""Bounded exact-field discovery for the balanced spin module.

Finite-field joins are discovery evidence only.  A rational construction
and a complete original-source replay are required for acceptance.
"""

import argparse
import json
from pathlib import Path

import numpy as np

from spin_module_discovery import toolkit
from undoubled_spin_discovery import matrices


ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / 'results/anisotropic-constructions-2026-10-20'


def discover(trials=4):
    kit = toolkit()
    prime = kit['prime']
    rank, rref, kernel = kit['rank'], kit['rref'], kit['kernel']
    _, K, L = matrices(4, 4)
    LP = [L[1], (L[0]-L[3])*pow(2, -1, prime) % prime, L[2]]
    profiles = ((3, 3), (4, 2), (3, 2, 1), (2, 2, 1), (3, 2), (4, 1))
    records = []
    for pi, profile in enumerate(profiles):
        target = 8 if sum(profile) == 6 else 7
        for trial in range(trials):
            seed = 202610214400 + 100*pi + trial
            rng = np.random.default_rng(seed)
            columns, generators = [], []
            for length in profile:
                generator = np.zeros((5-length, 4), dtype=np.int64)
                positions = rng.choice(generator.size, min(4, generator.size), replace=False)
                generator.ravel()[positions] = rng.choice([-1, 1], size=len(positions))
                generators.append(generator.tolist())
                for shift in range(length):
                    column = np.zeros((4, 4), dtype=np.int64)
                    column[shift:shift+5-length] = generator
                    columns.append(column.ravel())
            U = np.array(columns).T
            if rank(U) != sum(profile):
                records.append({'profile': list(profile), 'trial': trial,
                                'U_dimension': rank(U), 'rank_deficient_generators': True})
                continue
            Q = kernel(U.T).T
            q0, q1 = Q@K[0] % prime, Q@K[1] % prime
            zero = np.zeros_like(q0)
            D = kernel(np.block([[q1, zero], [zero, q0], [q0, -q1]]) % prime)
            V = K[0]@D[:20] % prime
            Wfull = np.concatenate([a@U % prime for a in L], axis=1)
            pivots = rref(Wfull)[1]
            W = Wfull[:, pivots]
            full = np.concatenate([W]+[a@V % prime for a in LP], axis=1)
            record = {'profile': list(profile), 'trial': trial, 'seed': seed,
                      'U_dimension': sum(profile), 'W_dimension': W.shape[1],
                      'D_dimension': D.shape[1], 'full_join_rank': rank(full),
                      'tested_target': [3, 3, target]}
            records.append(record)
            print(json.dumps(record), flush=True)
            if W.shape[1]+3*target > 40 or D.shape[1] < target:
                continue
            choices = [np.eye(D.shape[1], target, dtype=np.int64)]
            for choice in range(4):
                mixing = np.eye(D.shape[1], target, dtype=np.int64)
                if D.shape[1] > target:
                    mixing[target:] = rng.integers(-2, 3, size=(D.shape[1]-target, target))
                choices.append(mixing)
            for mixing in choices:
                selected = V@mixing % prime
                B = np.concatenate([W]+[a@selected % prime for a in LP], axis=1)
                if rank(B) != B.shape[1]:
                    continue
                rows = rref(B.T)[1]
                candidate = {'source_parameters': [2, 4, 4], 'source_format': [12, 40, 40],
                             'target': [3, 3, target], 'prime': prime, **record,
                             'generators': generators, 'D_subspace_matrix': mixing.tolist(),
                             'W_basis_column_indices': pivots, 'join_row_indices': rows,
                             'join_columns': B.shape[1], 'rational_map_verified': False,
                             'new_exponent_established': False}
                (DIRECTORY/'parity_balancing_spin44_candidate.json').write_text(json.dumps(candidate, indent=2)+'\n')
                (DIRECTORY/'parity_balancing_spin44_discovery.json').write_text(json.dumps({'records': records, 'candidate_found': True}, indent=2)+'\n')
                print(json.dumps({'finite_field_candidate': True, 'target': target,
                                  'join_columns': B.shape[1]}), flush=True)
                return candidate
    (DIRECTORY/'parity_balancing_spin44_discovery.json').write_text(json.dumps({'records': records, 'candidate_found': False}, indent=2)+'\n')
    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--trials', type=int, default=4)
    args = parser.parse_args()
    discover(args.trials)
