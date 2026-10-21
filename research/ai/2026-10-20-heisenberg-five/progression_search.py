"""Larger Heisenberg coset-progressions with exact trade and streaming acceptance."""
import argparse
import json
from pathlib import Path
import random
import sys
import time

from source import group, source_gate, RESEARCH
from verify import verify_cut
sys.path.insert(0, str(RESEARCH/'2026-10-20-group-potentials'))
from stream_potentials import discover


def quotient_map(G, points):
    result = {}
    for i, g in enumerate(points):
        for j, h in enumerate(points):
            if i != j:
                result[G['mul'][g][G['inv'][h]]] = i, j
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--p', type=int, default=11)
    parser.add_argument('--cosets', type=int, default=3)
    parser.add_argument('--seconds', type=float, default=300)
    parser.add_argument('--parameter-limit', type=int, default=20000)
    parser.add_argument('--pair-limit', type=int, default=5000)
    args = parser.parse_args()
    p, k = args.p, args.cosets
    if p not in (5, 7, 11, 13, 17, 19) or not 2 <= k < p:
        raise ValueError('supported odd prime and positive proper coset count required')
    G = group(p)
    M, inv = G['mul'], G['inv']
    index = {g: i for i, g in enumerate(G['matrices'])}
    first = tuple(sorted(index[a, b, 0] for a in range(p) for b in range(k)))
    QS = quotient_map(G, first)
    subgroups = set()
    for g, (a, b, c) in enumerate(G['matrices']):
        if a == b == 0:
            continue
        powers = [0]
        for _ in range(p-1):
            powers.append(M[powers[-1]][g])
        subgroups.add(tuple(sorted(powers)))
    parameters = []
    for L in sorted(subgroups):
        if set(L)-{0} & QS.keys():
            continue
        a, b, c = G['matrices'][next(h for h in L if h)]
        if b == 0:
            continue  # Two full fibers in the same abelian direction violate the coset bound.
        for g, (x, y, z) in enumerate(G['matrices']):
            if (a*y-b*x) % p:
                parameters.append((L, g))
    random.Random(20261133).shuffle(parameters)
    shape = [p*k]*3
    report = {'group': G['name'], 'shape': shape, 'source': source_gate(p, tuple(shape)),
        'cosets_per_set': k, 'seed': 20261133, 'first_set': first,
        'first_quotient_count': len(QS), 'available_parameters': len(parameters),
        'parameters_checked': 0, 'eligible_other_sets': 0, 'pair_tests': 0,
        'pair_injective_triples': 0, 'exact_two_trade_cuts': 0, 'exact_long_farkas_cuts': 0,
        'unresolved': [], 'witness': None, 'status': 'running', 'exponent_improvement': False,
        'seconds_limit': args.seconds, 'parameter_limit': args.parameter_limit,
        'pair_limit': args.pair_limit, 'scope': 'Bounded coset-progression construction search; '
        'no complete source or arbitrary-degeneration exclusion.'}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    cut_path = args.output.with_suffix('.cuts.jsonl')
    cut_path.write_text('')
    started = time.monotonic()
    eligible, seen = [], set()

    def checkpoint():
        report['elapsed_seconds'] = time.monotonic()-started
        tmp = args.output.with_suffix('.tmp')
        tmp.write_text(json.dumps(report, indent=2)+'\n')
        tmp.replace(args.output)

    checkpoint()
    for L, g in parameters[:args.parameter_limit]:
        if time.monotonic()-started >= args.seconds or report['pair_tests'] >= args.pair_limit:
            break
        report['parameters_checked'] += 1
        powers = [0]
        for _ in range(k-1):
            powers.append(M[powers[-1]][g])
        T = tuple(sorted({M[v][l] for v in powers for l in L}))
        if len(T) != p*k or T in seen:
            continue
        seen.add(T)
        QT = quotient_map(G, T)
        if QS.keys() & QT.keys():
            continue
        report['eligible_other_sets'] += 1
        for U, QU in eligible:
            report['pair_tests'] += 1
            if time.monotonic()-started >= args.seconds or report['pair_tests'] >= args.pair_limit:
                break
            if QT.keys() & QU.keys():
                continue
            sets = [list(first), list(T), list(U)]
            report['pair_injective_triples'] += 1
            vertices = None
            for x, (ss, s) in QS.items():
                for y, (t, tt) in QT.items():
                    z = inv[M[x][y]]
                    if z in QU and M[x][y] == M[y][x]:
                        u, uu = QU[z]
                        vertices = [s, t, tt, u, uu, ss]
                        break
                if vertices:
                    break
            if vertices:
                s, t, tt, u, uu, ss = vertices
                record = {'sets': sets, 'relation_vertices':
                          [vertices, [ss, tt, t, uu, u, s]], 'weights': [1, 1]}
                report['exact_two_trade_cuts'] += 1
            else:
                answer = discover(G, sets, max_rounds=30, violation_batch=500, seed=20261133)
                if answer['complete']:
                    report['witness'] = {'sets': sets, 'potentials': answer['decision']['potentials'],
                                         'verification': answer['verification']}
                    report['status'] = 'exact-target-witness'
                    break
                if answer['decision'] is None:
                    report['unresolved'].append({'sets': sets, 'rounds': answer['rounds']})
                    continue
                decision = answer['decision']
                record = {'sets': sets, 'relation_vertices':
                          [answer['relations'][i]['vertices'] for i in decision['indices']],
                          'weights': decision['weights']}
                report['exact_long_farkas_cuts'] += 1
            verify_cut(G, record)
            with cut_path.open('a') as stream:
                stream.write(json.dumps(record, separators=(',', ':'))+'\n')
        eligible.append((T, QT))
        checkpoint()
        if report['witness']:
            break
    if report['status'] == 'running':
        report['status'] = 'bounded-search-ended; no witness'
    checkpoint()
    print(json.dumps({key: value for key, value in report.items()
                      if key not in ('source', 'first_set', 'witness', 'unresolved')}), flush=True)


if __name__ == '__main__':
    main()
