"""S5 x C2^2: four-color source and an exact native pair-map encoding."""
import argparse
import hashlib
from itertools import combinations, permutations, product
import json
from pathlib import Path
import time

from s5_source import group, data as two_data, ROOT
from symmetry import append as append_symmetry, canonical_control
from source_certificate import exponent_gate
from group_exact import pair_map, extra_relations, verify_farkas, verify_witness

RESULTS = ROOT/'results/s5-split-2026-10-21'


def certificate():
    path = RESULTS/'source-certificate.json'
    base = json.loads(path.read_text())['first_factor_rational_certificate']
    degrees = base['complex_degrees']*4
    if base['order'] != 120 or sum(d*d for d in degrees) != 480:
        raise ArithmeticError('incorrect four-color source accounting')
    return {'group': 'S5 x C2^2', 'order': 480, 'complex_degrees': degrees,
            'source_factor_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'derivation': 'The verified S5 factor times the four linear characters of C2^2.',
            'conditional_gate': exponent_gate(degrees, shape=(19, 19, 19)),
            'degeneration_constructed': False, 'exponent_improvement': False}


def data():
    base = group()
    M, inv = base['mul'], base['inv']
    G = {'name': 'S5 x C2^2', 'identity': 0,
         'matrices': [(p, c) for p in base['matrices'] for c in range(4)],
         'mul': [[4*M[q][r]+(a ^ b) for r in range(120) for b in range(4)]
                 for q in range(120) for a in range(4)],
         'inv': [4*inv[q]+a for q in range(120) for a in range(4)]}
    classes = sorted({min(q, inv[q]) for q in range(1, 120)})
    Q = {'representatives': [4*q for q in range(120)],
         'projection': [g//4 for g in range(480)], 'colors': [g % 4 for g in range(480)],
         'mul': M, 'inv': inv, 'classes': classes,
         'fibers': {c: [4*c+a for a in range(4)] for c in classes},
         'pairs': {(u, v): (min(M[u][inv[v]], inv[M[u][inv[v]]]), 0)
                   for u, v in combinations(range(120), 2)}, 'central_colors': 4}
    _, _, original = two_data()
    H = [4*q+c for q in original['projected_subgroup'] for c in range(4)]
    if len(H) != 96 or any(G['mul'][g][h] not in H for g in H for h in H):
        raise ArithmeticError('incorrect four-color normalization subgroup')
    coverage = []
    for row in original['anchor_coverage']:
        item = dict(row)
        g = 4*(item['conjugator']//2)
        q = item['projected_quotient']
        if Q['projection'][G['mul'][G['mul'][g][4*q]][G['inv'][g]]] != item['anchor']:
            raise ArithmeticError('incorrect four-color anchor coverage')
        item['conjugator'] = g
        coverage.append(item)
    path = RESULTS/'four-source-certificate.json'
    source = json.loads(path.read_text())
    if source != certificate():
        raise ArithmeticError('four-color source certificate changed')
    receipt = {'group': G['name'], 'projected_order': 120, 'central_colors': 4,
               'subgroup_order': 96, 'subgroup_index': 5, 'subgroup_members': H,
               'projected_subgroup': original['projected_subgroup'],
               'first_pair_anchor_disjunction': original['first_pair_anchor_disjunction'],
               'anchor_coverage': coverage,
               'complex_degrees': source['complex_degrees'],
               'source_certificate_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
               'conditional_gate': source['conditional_gate'], 'exponent_improvement': False}
    return G, Q, receipt


def build(G, Q, receipt, shape, trades=True, normalized=True):
    from pysat.formula import IDPool
    from pysat.card import CardEnc, EncType
    from pysat.solvers import Cadical195
    pool, clauses = IDPool(), []
    points = [[[pool.id(('colored-point', f, q, c)) for c in range(4)]
               for q in range(120)] for f in range(3)]
    members = [[pool.id(('member', f, q)) for q in range(120)] for f in range(3)]
    owners = [{4*q+c: pool.id(('owner', f, q, c)) for q in Q['classes'] for c in range(4)}
              for f in range(3)]
    for f in range(3):
        clauses.append([points[f][0][0]])
        clauses.extend(CardEnc.equals(members[f], shape[f], vpool=pool, encoding=EncType.seqcounter).clauses)
        if normalized:
            clauses.extend(CardEnc.atleast([members[f][q] for q in receipt['projected_subgroup']],
                           (shape[f]+4)//5, vpool=pool, encoding=EncType.seqcounter).clauses)
        for q in range(120):
            colors = points[f][q]
            clauses.append([-members[f][q]]+colors)
            clauses.extend([[-v, members[f][q]] for v in colors])
            clauses.extend([[-v, -w] for v, w in combinations(colors, 2)])
        for (u, v), (c, _) in Q['pairs'].items():
            for a, b in product(range(4), repeat=2):
                clauses.append([-points[f][u][a], -points[f][v][b], owners[f][4*c+(a ^ b)]])
    for c in owners[0]:
        for f, h in combinations(range(3), 2):
            clauses.append([-owners[f][c], -owners[h][c]])
    if normalized and shape[0] > 5:
        clauses.append([members[0][q] for q in receipt['first_pair_anchor_disjunction']])
    trade_clauses = set()
    if trades:
        for x in range(1, 120):
            for y in range(1, 120):
                z = Q['mul'][x][y]
                if not z or z != Q['mul'][y][x]:
                    continue
                cx, cy, cz = [min(q, Q['inv'][q]) for q in (x, y, z)]
                for a, b in product(range(4), repeat=2):
                    for f, h, k in permutations(range(3)):
                        trade_clauses.add(tuple(sorted((-owners[f][4*cz+(a ^ b)],
                                                       -owners[h][4*cx+a], -owners[k][4*cy+b]))))
        clauses.extend(sorted(trade_clauses))
    before = len(clauses)
    symmetry = append_symmetry(G, Q, receipt, members, pool.id, clauses.append) if normalized else None
    solver = Cadical195(bootstrap_with=clauses)
    return solver, points, members, {'variables': pool.top, 'clauses': len(clauses),
            'full_inverse_classes': len(owners[0]), 'central_colors': 4,
            'commuting_trade_clauses': len(trade_clauses),
            'symmetry_clauses': len(clauses)-before, 'canonicalization': symmetry}


def control():
    G, Q, receipt = data()
    solver, points, _, encoding = build(G, Q, receipt, [2]*3, trades=False)
    q = min(p for p in receipt['projected_subgroup'] if p)
    checked = accepted = 0
    for colors in product(range(4), repeat=3):
        sets = [[0, 4*q+c] for c in colors]
        fixed = [v if 4*p+c in sets[f] else -v for f, row in enumerate(points)
                 for p, choices in enumerate(row) for c, v in enumerate(choices)]
        expected = True
        try:
            for f in range(3):
                pair_map(G, sets[f], sets[(f+1) % 3])
        except ValueError:
            expected = False
        actual = solver.solve(assumptions=fixed)
        if actual != expected:
            raise ArithmeticError('native four-color pair-map control failed')
        checked += 1
        accepted += actual
    solver.delete()
    known = canonical_control()['witness']
    sets = [[4*(g//2)+g % 2 for g in S] for S in known['sets']]
    verification = verify_witness(G, sets, known['potentials'])
    solver, points, _, encoding = build(G, Q, receipt, [3]*3)
    fixed = [v if 4*p+c in sets[f] else -v for f, row in enumerate(points)
             for p, choices in enumerate(row) for c, v in enumerate(choices)]
    if not solver.solve(assumptions=fixed):
        raise ArithmeticError('native four-color encoding rejected the weighted control')
    solver.delete()
    return {'signed_configurations': checked, 'accepted': accepted, 'rejected': checked-accepted,
            'weighted_control': verification, 'encoding': encoding, 'exponent_improvement': False}


def search(output, seconds):
    from search import potential_or_circuit
    G, Q, receipt = data()
    shape = [19]*3
    solver, points, _, encoding = build(G, Q, receipt, shape)
    started = time.monotonic()
    report = {'group': G['name'], 'shape': shape, 'source_and_normalization': receipt,
              'encoding': encoding, 'seconds_limit': seconds, 'pair_injective_models': 0,
              'exact_farkas_cuts': 0, 'status': 'running', 'witness': None,
              'exponent_improvement': False, 'scope': 'Bounded native four-color discovery. '
              'Untraced SAT negatives and timeouts are not exclusions.'}
    output.parent.mkdir(parents=True, exist_ok=True)
    cut_path = output.with_suffix('.cuts.jsonl')
    cut_path.write_text('')
    def checkpoint():
        report['elapsed_seconds'] = time.monotonic()-started
        report['sat_statistics'] = solver.accum_stats()
        tmp = output.with_suffix('.tmp')
        tmp.write_text(json.dumps(report, indent=2)+'\n')
        tmp.replace(output)
    checkpoint()
    while time.monotonic()-started < seconds:
        solver.conf_budget(10000)
        solved = solver.solve_limited()
        if solved is None:
            checkpoint()
            continue
        if solved is False:
            report['status'] = 'solver-reported-unsat; no proof trace'
            break
        values = set(solver.get_model())
        sets = [[4*q+c for q, row in enumerate(leg) for c, v in enumerate(row) if v in values]
                for leg in points]
        for f in range(3):
            pair_map(G, sets[f], sets[(f+1) % 3])
        report['pair_injective_models'] += 1
        relations, _ = extra_relations(G, sets)
        answer = potential_or_circuit(relations, sum(shape))
        if 'potentials' in answer:
            report['witness'] = {'sets': sets, 'potentials': answer['potentials'],
                'verification': verify_witness(G, sets, answer['potentials'])}
            report['status'] = 'exact-target-witness'
            break
        if not verify_farkas(relations, answer['indices'], answer['weights']):
            raise ArithmeticError('invalid four-color Farkas cut')
        support = set()
        for i in answer['indices']:
            s, t, tt, u, uu, ss = relations[i]['vertices']
            support.update(((0, sets[0][s]), (0, sets[0][ss]), (1, sets[1][t]),
                            (1, sets[1][tt]), (2, sets[2][u]), (2, sets[2][uu])))
        solver.add_clause([-points[f][g//4][g % 4] for f, g in support])
        item = {'type': 'exact-farkas', 'sets': sets, 'relation_vertices':
                [relations[i]['vertices'] for i in answer['indices']], 'weights': answer['weights'],
                'blocked_lift_points': sorted(support)}
        with cut_path.open('a') as stream:
            stream.write(json.dumps(item, separators=(',', ':'))+'\n')
        report['exact_farkas_cuts'] += 1
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
    parser.add_argument('--source', action='store_true')
    parser.add_argument('--control', action='store_true')
    args = parser.parse_args()
    if args.source:
        result = certificate()
    elif args.control:
        result = control()
    else:
        result = search(args.output, args.seconds)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items()
                      if k not in ('source_and_normalization', 'witness')}))
