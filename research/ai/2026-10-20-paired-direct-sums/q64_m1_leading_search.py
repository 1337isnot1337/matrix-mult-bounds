"""Optional bounded numerical Q64 searches with an M1 leading block.

NumPy is a discovery dependency, not a maintained verification dependency.
Both pilot initializations allow every leading B/C source column to move.
Floating-point residuals never constitute exact coefficient certificates.
"""
import argparse
from itertools import product
import json
from pathlib import Path
import numpy as np

import q64_complete_flag_search as solver
from q64_m1_leading_exact import embedded_product_maps, powers
from q64_parabolic_gauge import pair
from narrow_rectangle_balanced import balance_pair


GAUGE = 'upper physical outer gauges and unrestricted middle gauge'


def setup(_):
    weights = [np.array(w) for w in powers()]
    target = np.zeros((25, 20, 20))
    for i, j, k in product(range(5), range(4), range(5)):
        target[5*i+k, 4*i+j, 5*j+k] = 1
    degree = weights[0][:, None, None]+weights[1][None, :, None]+weights[2][None, None, :]
    assert np.count_nonzero(degree <= 0) == 7568
    assert not np.any(target[degree != 0])
    return weights, target, degree


def gauge(maps):
    a = maps[0].reshape(5, 5, -1)
    b = maps[1].reshape(5, 4, -1)
    c = maps[2].reshape(4, 5, -1)
    for _ in range(2):
        a, b = pair(a, 0, b, 0)
        b, c = balance_pair(b, 1, c, 0)
        a, c = pair(a, 1, c, 1)
    return [x.reshape(old.shape) for x, old in zip([a, b, c], maps)]


def initial(seed_kind, seed):
    rng = np.random.default_rng(seed)
    if seed_kind == 'sparse':
        maps = [np.zeros((rows, 36), complex) for rows in [25, 20, 20]]
        a, b, c = maps
        a[0, 0] = 1
        for y, v in product(range(2), repeat=2):
            j = 2*y+v
            b[j, 9*y+v] = 1
            c[5*j, 4*y+v] = 1
        for i, k in product(range(5), repeat=2):
            if i or k:
                p, q = (k+1 if k else 0), (i+1 if i else 0)
                a[5*i+k, 6*p+q] = 1
        new_outer = range(1, 5)
    elif seed_kind == 'product':
        maps = [np.array(m, complex) for m in embedded_product_maps()]
        a, b, c = maps
        u = np.zeros((5, 6), complex)
        u[0, 1] = u[1, 2] = u[2, 3] = u[3, 0] = u[4, 5] = 1
        u[3, 4] = -1
        for i, k in product(range(5), repeat=2):
            if i == 4 or k == 4:
                a[5*i+k] = np.outer(u[k], u[i]).ravel()
        new_outer = [4]
    else:
        raise ValueError('Unknown exact leading-point initialization.')
    for i, j in product(new_outer, range(4)):
        b[4*i+j] = 0.2*(rng.normal(size=36)+1j*rng.normal(size=36))/np.sqrt(72)
    for j, k in product(range(4), new_outer):
        c[5*j+k] = 0.2*(rng.normal(size=36)+1j*rng.normal(size=36))/np.sqrt(72)
    return maps


def run(seed_kind, seed, iterations, norm_budget, prefix):
    # Reuse the already maintained rowwise trust-region ALS implementation;
    # replace only its weights and its allowed target stabilizer gauge.
    solver.setup = setup
    solver.gauge = gauge
    maps = initial(seed_kind, seed)
    initial_path = prefix.with_name(prefix.name+'-initial.json')
    initial_path.write_text(json.dumps({
        'maps_real': [m.real.tolist() for m in maps],
        'maps_imag': [m.imag.tolist() for m in maps], 'seed': seed,
        'auxiliary_rank': 0, 'source': 'Q(6,4)',
        'leading_target': 'M(1,4,1)', 'seed_kind': seed_kind,
        'exact_full_target_certificate': False}, separators=(',', ':'))+'\n')
    checkpoint = prefix.with_name(prefix.name+'-checkpoint.json')
    result = solver.fit('m1-leading', seed, iterations, initial_path,
                        checkpoint, norm_budget, 'diagonal')
    _, _, degree = setup(None)
    final = result['history'][-1]
    stop = ('iteration_budget' if result['iterations_completed'] == iterations
            else 'coefficient_tolerance' if final['relative_nonpositive_coefficient_error'] < 1e-12
            else 'nonfinite_or_norm_guard')
    result.update({
        'target_gauge': GAUGE, 'seed_kind': seed_kind,
        'actual_stop_reason': stop,
        'coefficient_counts': {str(k): int(np.count_nonzero(degree == k)) for k in range(-2, 3)},
        'leading_seed_pre_A_rank': 4,
        'leading_seed_first_edge_source_ranks': [10, 10] if seed_kind == 'sparse' else [32, 32],
        'all_old_source_columns_can_move': True})
    point = json.loads(checkpoint.read_text())
    point['target_gauge'] = GAUGE
    point['seed_kind'] = seed_kind
    point['completed_run'] = result
    checkpoint.write_text(json.dumps(point, separators=(',', ':'))+'\n')
    prefix.with_name(prefix.name+'-result.json').write_text(json.dumps(result, indent=2)+'\n')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seed-kind', choices=['sparse', 'product'], required=True)
    parser.add_argument('--seed', type=int, required=True)
    parser.add_argument('--iterations', type=int, default=1500)
    parser.add_argument('--norm-budget', type=float, default=30)
    parser.add_argument('--prefix', type=Path, required=True)
    args = parser.parse_args()
    result = run(args.seed_kind, args.seed, args.iterations, args.norm_budget, args.prefix)
    print(json.dumps({key: value for key, value in result.items() if key != 'history'}, indent=2))
