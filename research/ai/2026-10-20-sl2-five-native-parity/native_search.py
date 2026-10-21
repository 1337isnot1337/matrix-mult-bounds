"""Joint projected-point and central-sign search with exact positive acceptance."""
import argparse
from itertools import combinations, permutations, product
import json
from pathlib import Path
import random
import sys
import time

from data import data, ROOT, SEVEN
sys.path.insert(0, str(SEVEN/'imported'))
from group_exact import pair_map, extra_relations, verify_witness, verify_farkas
from search import potential_or_circuit
from pysat.formula import IDPool
from pysat.card import CardEnc
from pysat.solvers import Cadical195


def build(G, Q, receipt, shape, trades=True):
    pool = IDPool()
    n = len(Q['representatives'])
    members = [[pool.id(('point', f, q)) for q in range(n)] for f in range(3)]
    signs = [[pool.id(('sign', f, q)) for q in range(n)] for f in range(3)]
    classes = sorted({v for fiber in Q['fibers'].values() for v in fiber})
    owners = [{q: pool.id(('full-inverse-class', f, q)) for q in classes} for f in range(3)]
    clauses = []
    for f, size in enumerate(shape):
        clauses.extend(([members[f][0]], [-signs[f][0]]))
        clauses.extend(CardEnc.equals(members[f], size, vpool=pool).clauses)
        clauses.extend(CardEnc.atleast([members[f][q] for q in receipt['projected_subgroup']],
                                       (size+4)//5, vpool=pool).clauses)
        for (u, v), (c, offset) in Q['pairs'].items():
            fiber = Q['fibers'][c]
            guard = [-members[f][u], -members[f][v]]
            if len(fiber) == 1:
                clauses.append(guard+[owners[f][fiber[0]]])
            else:
                for a, b in product(range(2), repeat=2):
                    clauses.append(guard+[signs[f][u] if not a else -signs[f][u],
                                          signs[f][v] if not b else -signs[f][v],
                                          owners[f][fiber[offset ^ a ^ b]]])
    for f, h in combinations(range(3), 2):
        for c in classes:
            clauses.append([-owners[f][c], -owners[h][c]])
    if shape[0] > 5:
        clauses.append([members[0][q] for q in receipt['first_pair_anchor_disjunction']])
    trade_clauses = set()
    if trades:
        for x in range(1, 120):
            if not Q['projection'][x]:
                continue
            for y in range(1, 120):
                z = G['mul'][x][y]
                if (not Q['projection'][y] or not Q['projection'][z]
                        or z != G['mul'][y][x]):
                    continue
                qx, qy, qz = [min(v, G['inv'][v]) for v in (x, y, z)]
                for fs, ft, fu in permutations(range(3)):
                    trade_clauses.add(tuple(sorted((-owners[fs][qz],
                                                   -owners[ft][qx], -owners[fu][qy]))))
        clauses.extend(sorted(trade_clauses))
    solver = Cadical195(bootstrap_with=clauses)
    return solver, members, signs, {'variables': pool.top, 'clauses': len(clauses),
        'projected_points_per_leg': n, 'full_inverse_classes': len(classes),
        'commuting_trade_clauses': len(trade_clauses),
        'pair_map_encoding': 'Exact inverse classes with joint projected membership and central signs'}


def decode(G, Q, members, signs, model):
    values = set(model)
    projected = [[q for q, v in enumerate(row) if v in values] for row in members]
    sets = [[G['mul'][Q['z']][Q['representatives'][q]] if signs[f][q] in values
             else Q['representatives'][q] for q in row] for f, row in enumerate(projected)]
    for f in range(3):
        pair_map(G, sets[f], sets[(f+1) % 3])
    return projected, sets


def controls(G, Q, receipt):
    solver, members, signs, _ = build(G, Q, receipt, [2]*3, trades=False)
    randomizer = random.Random(20260512)
    checked = accepted = 0
    narrow = min(c for c in Q['classes'] if len(Q['fibers'][c]) == 1)
    broad = min(c for c in Q['classes'] if len(Q['fibers'][c]) == 2)
    configurations = [[[0, narrow]]*3, [[0, broad]]*3,
                      [[0, broad], [0, broad], [0, narrow]],
                      [[0, broad], [0, Q['inv'][broad]], [0, narrow]]]
    configurations += [[[0, randomizer.randrange(1, 60)] for f in range(3)] for _ in range(30)]
    for projected in configurations:
        fixed = [v if q in projected[f] else -v
                 for f, row in enumerate(members) for q, v in enumerate(row)]
        for colors in product(range(2), repeat=3):
            assumptions = fixed+[signs[f][projected[f][1]] if colors[f]
                                 else -signs[f][projected[f][1]] for f in range(3)]
            sets = [[0, G['mul'][Q['z']][Q['representatives'][row[1]]] if colors[f]
                     else Q['representatives'][row[1]]] for f, row in enumerate(projected)]
            try:
                for f in range(3):
                    pair_map(G, sets[f], sets[(f+1) % 3])
                expected = True
            except ValueError:
                expected = False
            actual = solver.solve(assumptions=assumptions)
            if actual != expected:
                raise ArithmeticError('native CNF differs from exact small pair maps')
            checked += 1
            accepted += actual
    solver.delete()
    if not 0 < accepted < checked:
        raise ArithmeticError('small-lift control must exercise both outcomes')
    known = json.loads((ROOT/'results/group-potentials-2026-10-20/'
                        'sl2-5-control3-3-3.json').read_text())['witness']
    solver, members, signs, _ = build(G, Q, receipt, [3]*3, trades=True)
    projected = [[Q['projection'][g] for g in row] for row in known['sets']]
    assumptions = [v if q in projected[f] else -v
                   for f, row in enumerate(members) for q, v in enumerate(row)]
    assumptions += [signs[f][Q['projection'][g]] if Q['bits'][g]
                    else -signs[f][Q['projection'][g]] for f, row in enumerate(known['sets']) for g in row]
    if not solver.solve(assumptions=assumptions):
        raise ArithmeticError('native encoding rejected the known weighted control')
    solver.delete()
    return {'small_lifts_checked': checked, 'pair_injective_small_lifts': accepted,
            'weighted_control': verify_witness(G, known['sets'], known['potentials'])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--seconds', type=float, default=600)
    parser.add_argument('--control', action='store_true')
    args = parser.parse_args()
    G, Q, receipt = data()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.control:
        result = controls(G, Q, receipt)
        args.output.write_text(json.dumps(result, indent=2)+'\n')
        print(json.dumps(result))
        return
    solver, members, signs, encoding = build(G, Q, receipt, [10]*3)
    started = time.monotonic()
    report = {'group': G['name'], 'shape': [10]*3, 'source_and_normalization': receipt,
        'encoding': encoding, 'seconds_limit': args.seconds, 'pair_injective_models': 0,
        'exact_farkas_cuts': 0, 'status': 'running', 'witness': None,
        'exponent_improvement': False, 'scope': 'Bounded exact-acceptance discovery. '
        'Timeouts and untraced SAT negatives are not nonexistence proofs.'}
    cut_path = args.output.with_suffix('.cuts.jsonl')
    cut_path.write_text('')

    def checkpoint():
        report['elapsed_seconds'] = time.monotonic()-started
        report['sat_statistics'] = solver.accum_stats()
        tmp = args.output.with_suffix('.tmp')
        tmp.write_text(json.dumps(report, indent=2)+'\n')
        tmp.replace(args.output)

    checkpoint()
    while time.monotonic()-started < args.seconds:
        solver.conf_budget(10000)
        solved = solver.solve_limited()
        if solved is None:
            checkpoint()
            continue
        if solved is False:
            report['status'] = 'solver-reported-unsat; no proof trace'
            break
        projected, sets = decode(G, Q, members, signs, solver.get_model())
        report['pair_injective_models'] += 1
        relations, _ = extra_relations(G, sets)
        answer = potential_or_circuit(relations, 30)
        if 'potentials' in answer:
            report['witness'] = {'sets': sets, 'potentials': answer['potentials'],
                                 'verification': verify_witness(G, sets, answer['potentials'])}
            report['status'] = 'exact-target-witness'
            break
        if not verify_farkas(relations, answer['indices'], answer['weights']):
            raise ArithmeticError('refusing an invalid Farkas cut')
        points = set()
        for i in answer['indices']:
            s, t, tt, u, uu, ss = relations[i]['vertices']
            points.update(((0, sets[0][s]), (0, sets[0][ss]), (1, sets[1][t]),
                           (1, sets[1][tt]), (2, sets[2][u]), (2, sets[2][uu])))
        clause = []
        for f, g in sorted(points):
            q = Q['projection'][g]
            clause.extend((-members[f][q], signs[f][q] if not Q['bits'][g] else -signs[f][q]))
        solver.add_clause(clause)
        record = {'sets': sets, 'relation_vertices':
                  [relations[i]['vertices'] for i in answer['indices']], 'weights': answer['weights']}
        with cut_path.open('a') as stream:
            stream.write(json.dumps(record, separators=(',', ':'))+'\n')
        report['exact_farkas_cuts'] += 1
        checkpoint()
    if report['status'] == 'running':
        report['status'] = 'time-limit'
    checkpoint()
    solver.delete()
    print(json.dumps({k: v for k, v in report.items()
                      if k not in ('source_and_normalization', 'witness')}), flush=True)


if __name__ == '__main__':
    main()
