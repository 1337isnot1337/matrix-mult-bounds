"""Projected local search, central-slice cuts, and conditional native color SAT."""
import argparse
import json
import math
from pathlib import Path
import random
import time

import numpy as np

from four_colors import data, build
from central_slice import find_match, verify_match, slice_control
from group_exact import pair_map, extra_relations, verify_witness, verify_farkas
from verify_projected_reports import verify_farkas_record
from search import potential_or_circuit


def run(output, seconds, seed, shape=(19, 19, 19), cooling_steps=500000):
    G, Q, receipt = data(shape)
    if receipt['conditional_gate']['strict_positive_margin_numerator'] <= 0:
        raise ValueError('this target does not pass the improving conditional gate')
    slice_control()
    solver, points, members, encoding = build(G, Q, receipt, shape, normalized=False)
    rng = random.Random(seed)
    sets = [[0]+rng.sample(range(1, 120), n-1) for n in shape]
    table, inverse = np.array(Q['mul'], dtype=np.int16), np.array(Q['inv'], dtype=np.int16)
    cuts = []

    def mask(S):
        return sum(1 << q for q in S)

    def energy():
        value = 0
        for f, h in ((0, 1), (0, 2), (1, 2)):
            labels = table[inverse[np.array(sets[f])][:, None], np.array(sets[h])[None, :]]
            counts = np.bincount(labels.ravel(), minlength=120)
            value += int(np.maximum(counts-4, 0).dot(np.maximum(counts-4, 0)))
        masks = [mask(S) for S in sets]
        value += 10*sum(all(masks[f] & C[f] == C[f] for f in range(3)) for C in cuts)
        return value

    current = energy()
    output.parent.mkdir(parents=True, exist_ok=True)
    cut_path = output.with_suffix('.cuts.jsonl')
    cut_path.write_text('')
    started = time.monotonic()
    report = {'group': G['name'], 'shape': list(shape), 'source_and_normalization': receipt,
        'encoding': encoding, 'method': 'Local projected capacity, modular central matching, native color SAT',
        'normalizations_used': 'Identity only in the sampler and conditional color solver',
        'seed': seed, 'seconds_limit': seconds, 'steps': 0, 'minimum_energy': current,
        'best_projected_sets': [list(S) for S in sets],
        'temperature': {'floor': 0.05, 'amplitude': 1.5, 'period_steps': cooling_steps},
        'inner_conflict_budget': 3000,
        'projected_model_events': 0, 'exact_central_slice_cuts': 0,
        'untraced_inner_refutations': 0, 'inner_budget_hits': 0, 'pair_injective_models': 0,
        'exact_farkas_cuts': 0, 'status': 'running', 'witness': None, 'exponent_improvement': False,
        'scope': 'Bounded stochastic discovery; conditional solver negatives are untraced and not exclusions.'}

    def save(item):
        with cut_path.open('a') as stream:
            stream.write(json.dumps(item, separators=(',', ':'))+'\n')

    def checkpoint():
        report['elapsed_seconds'] = time.monotonic()-started
        report['current_energy'] = current
        report['sat_statistics'] = solver.accum_stats()
        tmp = output.with_suffix('.tmp')
        tmp.write_text(json.dumps(report, indent=2)+'\n')
        tmp.replace(output)

    checkpoint()
    while time.monotonic()-started < seconds:
        report['steps'] += 1
        f = rng.randrange(3)
        i = rng.randrange(1, shape[f])
        q = rng.randrange(1, 120)
        if q in sets[f]:
            continue
        old = sets[f][i]
        sets[f][i] = q
        proposed = energy()
        temperature = 0.05+1.5*(1-(report['steps'] % cooling_steps)/cooling_steps)
        if proposed <= current or rng.random() < math.exp((current-proposed)/temperature):
            current = proposed
            if current < report['minimum_energy']:
                report['minimum_energy'] = current
                report['best_projected_sets'] = [list(S) for S in sets]
        else:
            sets[f][i] = old
        if not current:
            report['projected_model_events'] += 1
            record = find_match(Q, sets)
            if record is not None:
                verify_match(Q, record)
                record['sets'] = [list(S) for S in sets]
                save(record)
                cuts.append(tuple(mask([p for h, p in record['blocked_points'] if h == f]) for f in range(3)))
                current += 10
                report['exact_central_slice_cuts'] += 1
            else:
                selected = list(map(set, sets))
                assumptions = [v if q in selected[f] else -v
                               for f, row in enumerate(members) for q, v in enumerate(row)]
                solver.set_phases([points[f][q][rng.randrange(4)] for f, S in enumerate(sets) for q in S if q])
                solver.conf_budget(3000)
                solved = solver.solve_limited(assumptions=assumptions)
                if solved is None:
                    report['inner_budget_hits'] += 1
                elif solved is False:
                    report['untraced_inner_refutations'] += 1
                    save({'type': 'untraced-inner-unsat', 'sets': [list(S) for S in sets],
                          'independent_proof': False})
                else:
                    model = set(solver.get_model())
                    lifted = [[4*q+c for q, row in enumerate(leg) for c, v in enumerate(row) if v in model]
                              for leg in points]
                    for f in range(3):
                        pair_map(G, lifted[f], lifted[(f+1) % 3])
                    report['pair_injective_models'] += 1
                    relations, _ = extra_relations(G, lifted)
                    answer = potential_or_circuit(relations, sum(shape))
                    if 'potentials' in answer:
                        report['witness'] = {'sets': lifted, 'potentials': answer['potentials'],
                            'verification': verify_witness(G, lifted, answer['potentials'])}
                        report['status'] = 'exact-target-witness'
                        break
                    if not verify_farkas(relations, answer['indices'], answer['weights']):
                        raise ArithmeticError('invalid local four-color Farkas cut')
                    support = set()
                    for j in answer['indices']:
                        s, t, tt, u, uu, ss = relations[j]['vertices']
                        support.update(((0, lifted[0][s]), (0, lifted[0][ss]), (1, lifted[1][t]),
                                        (1, lifted[1][tt]), (2, lifted[2][u]), (2, lifted[2][uu])))
                    item = {'type': 'exact-farkas', 'sets': lifted, 'relation_vertices':
                        [relations[j]['vertices'] for j in answer['indices']], 'weights': answer['weights'],
                        'blocked_lift_points': sorted(support)}
                    verify_farkas_record(G, item)
                    save(item)
                    solver.add_clause([-points[f][g//4][g % 4] for f, g in support])
                    report['exact_farkas_cuts'] += 1
                # A sampling kick avoids treating any untraced negative as a proved cut.
                f = rng.randrange(3)
                i = rng.randrange(1, shape[f])
                q = rng.choice([p for p in range(1, 120) if p not in sets[f]])
                sets[f][i] = q
                current = energy()
        if report['steps'] % 1000 == 0:
            checkpoint()
    if report['status'] == 'running':
        report['status'] = 'time-limit'
    checkpoint()
    solver.delete()
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--seconds', type=float, default=600)
    parser.add_argument('--seed', type=int, default=2026102133)
    parser.add_argument('--shape', type=int, nargs=3, default=(19, 19, 19))
    parser.add_argument('--cooling-steps', type=int, default=500000)
    args = parser.parse_args()
    print(json.dumps({k: v for k, v in run(args.output, args.seconds, args.seed,
                      args.shape, args.cooling_steps).items()
                      if k not in ('source_and_normalization', 'witness')}))
