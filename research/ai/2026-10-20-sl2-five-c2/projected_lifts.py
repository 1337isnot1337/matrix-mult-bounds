"""Search projected sets first, then solve their two-bit central lifts.

Optional SAT/LP discovery. Only the unchanged integer verifier accepts a
degeneration. Untraced solver cores and search budgets are not exclusions.
"""
import argparse
from itertools import combinations, product
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace

from source_data import group, subgroup_certificate, central_projection, SEVEN
sys.path.insert(0, str(SEVEN/'imported'))
from group_exact import pair_map, extra_relations, verify_witness
from search import potential_or_circuit
from verify_structured import verify_record
from binary_lift_system import pair_classes, reject, verify_rejection
from pysat.card import CardEnc
from pysat.formula import IDPool
from pysat.solvers import Cadical195


def limited(solver, deadline, assumptions=()):
    while time.monotonic() < deadline:
        solver.conf_budget(10000)
        result = solver.solve_limited(assumptions=list(assumptions))
        if result is not None:
            return result
    return None


def lift_solver(G, Q, center, sets):
    pool = IDPool()
    variables = [[[pool.id(('color', f, i, b)) for b in range(2)]
                  for i in range(len(row))] for f, row in enumerate(sets)]
    active = [[pool.id(('active', f, i)) for i in range(len(row))]
              for f, row in enumerate(sets)]
    owners = {}
    clauses = []
    for f, row in enumerate(sets):
        zero = row.index(0)
        clauses.extend([[-v] for v in variables[f][zero]])
        for i, j in combinations(range(len(row)), 2):
            for colors in product(range(4), repeat=2):
                lifts = [G['mul'][center[c]][Q['representatives'][row[k]]]
                         for c, k in zip(colors, (i, j))]
                g = G['mul'][lifts[0]][G['inv'][lifts[1]]]
                q = min(g, G['inv'][g])
                key = (f, q)
                if key not in owners:
                    owners[key] = pool.id(('owner',)+key)
                clause = [-active[f][i], -active[f][j]]
                for k, c in zip((i, j), colors):
                    clause.extend(v if not (c >> b) & 1 else -v
                                  for b, v in enumerate(variables[f][k]))
                clauses.append(clause+[owners[key]])
    for f, h in combinations(range(3), 2):
        for q in range(1, len(G['matrices'])):
            if (f, q) in owners and (h, q) in owners:
                clauses.append([-owners[f, q], -owners[h, q]])
    return Cadical195(bootstrap_with=clauses), variables, active


def build_outer(G, Q, binary_pairs, args):
    pool = IDPool()
    members = [[pool.id(('point', f, q)) for q in range(60)] for f in range(3)]
    clauses = []
    for f, size in enumerate(args.shape):
        clauses.append([members[f][0]])
        clauses.extend(CardEnc.equals(members[f], size, vpool=pool).clauses)
    first = None
    if args.first_projection:
        first = json.loads(args.first_projection.read_text())
        if len(first) != args.shape[0] or len(set(first)) != args.shape[0] or 0 not in first:
            raise ValueError('wrong fixed projection')
        clauses.extend([[v if q in first else -v] for q, v in enumerate(members[0])])
    if args.pair_capacity:
        table = [[Q['projection'][G['mul'][p][q]] for q in Q['representatives']]
                 for p in Q['representatives']]
        for f in range(3):
            h = (f+1) % 3
            for q in range(60):
                occurrences = []
                for s in range(60):
                    t = table[s][q]
                    if first is not None and f == 0:
                        if s in first:
                            occurrences.append(members[h][t])
                    elif first is not None and h == 0:
                        if t in first:
                            occurrences.append(members[f][s])
                    else:
                        both = pool.id(('pair', f, q, s))
                        clauses.append([-members[f][s], -members[h][t], both])
                        occurrences.append(both)
                if len(occurrences) > 4:
                    clauses.extend(CardEnc.atmost(occurrences, 4, vpool=pool).clauses)
    binary_bits = None
    if args.inverse_capacity or args.native_binary:
        classes = sorted(set(binary_pairs.values()))
        owners = [{c: pool.id(('binary-owner', f, c)) for c in classes} for f in range(3)]
        for f in range(3):
            for (p, q), c in binary_pairs.items():
                clauses.append([-members[f][p], -members[f][q], owners[f][c]])
        for c in classes:
            clauses.append([-owners[f][c] for f in range(3)])
        if args.native_binary:
            binary_bits = [[pool.id(('direct-bit', f, p)) for p in range(60)] for f in range(3)]
            colors = [{c: pool.id(('direct-owner-color', f, c)) for c in classes} for f in range(3)]
            clauses.extend([[-row[0]] for row in binary_bits])
            for f, h in combinations(range(3), 2):
                for c in classes:
                    guard = [-owners[f][c], -owners[h][c]]
                    clauses.extend([guard+[colors[f][c], colors[h][c]],
                                    guard+[-colors[f][c], -colors[h][c]]])
            for f in range(3):
                for (p, q), c in binary_pairs.items():
                    variables = [binary_bits[f][p], binary_bits[f][q], colors[f][c]]
                    for h in range(3):
                        if h == f:
                            continue
                        guard = [-members[f][p], -members[f][q], -owners[h][c]]
                        for values in product(range(2), repeat=3):
                            if sum(values) % 2:
                                clauses.append(guard+[v if not b else -v
                                                       for v, b in zip(variables, values)])
    outer = Cadical195(bootstrap_with=clauses)
    return outer, members, binary_bits


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--seconds', type=float, default=300)
    parser.add_argument('--first-projection', type=Path)
    parser.add_argument('--lift-models', type=int, default=50)
    parser.add_argument('--binary-filter', action='store_true')
    parser.add_argument('--pair-capacity', action='store_true')
    parser.add_argument('--inverse-capacity', action='store_true')
    parser.add_argument('--native-binary', action='store_true')
    parser.add_argument('--shape', type=int, nargs=3, default=[13, 13, 15])
    parser.add_argument('--control', action='store_true')
    args = parser.parse_args()
    G = group()
    cert = subgroup_certificate(G)
    Q = central_projection(G, cert)
    binary_pairs = pair_classes(G, Q)
    center = cert['center']
    # The color encoding requires the table of Z to be bitwise xor.
    if any(G['mul'][center[a]][center[b]] != center[a ^ b]
           for a, b in product(range(4), repeat=2)):
        raise ArithmeticError('central color coordinates are not xor')
    if args.control:
        root = Path(__file__).resolve().parents[3]
        known = json.loads((root/'results/group-potentials-2026-10-20/'
                            'sl2-5-control3-3-3.json').read_text())['witness']
        sets = [[2*g for g in row] for row in known['sets']]
        projected = [[Q['projection'][g] for g in row] for row in sets]
        solver, bits, active = lift_solver(G, Q, center, projected)
        assumptions = [v for row in active for v in row]
        for f, row in enumerate(sets):
            for i, g in enumerate(row):
                c = next(c for c, z in enumerate(center)
                         if G['mul'][z][Q['representatives'][projected[f][i]]] == g)
                assumptions.extend(v if (c >> b) & 1 else -v
                                   for b, v in enumerate(bits[f][i]))
        if solver.solve(assumptions=assumptions) is not True:
            raise ArithmeticError('lift encoding rejected a known exact witness')
        receipt = {'known_lift_accepted': True,
                   'integer_witness': verify_witness(G, sets, known['potentials'])}
        solver.delete()
        control_args = SimpleNamespace(shape=[3]*3, first_projection=None,
            pair_capacity=True, inverse_capacity=True, native_binary=True)
        outer, members, binary_bits = build_outer(G, Q, binary_pairs, control_args)
        assumptions = [v if p in projected[f] else -v
                       for f, row in enumerate(members) for p, v in enumerate(row)]
        assumptions += [binary_bits[f][p] if g & 1 else -binary_bits[f][p]
                        for f, row in enumerate(sets) for p, g in zip(projected[f], row)]
        if not outer.solve(assumptions=assumptions):
            raise ArithmeticError('projected encoding rejected the known witness')
        outer.delete()
        receipt['known_projection_accepted_with_all_pruning'] = True
        q, r = sorted(set(binary_pairs.values()))[:2]
        control_projection = [[0, q], [0, q], [0, r]]
        control_args.shape = [2]*3
        outer, members, binary_bits = build_outer(G, Q, binary_pairs, control_args)
        fixed = [v if p in control_projection[f] else -v
                 for f, row in enumerate(members) for p, v in enumerate(row)]
        for choices in product(range(4), repeat=3):
            lifted = [[0, G['mul'][center[c]][Q['representatives'][row[1]]]]
                      for c, row in zip(choices, control_projection)]
            try:
                for f in range(3):
                    pair_map(G, lifted[f], lifted[(f+1) % 3])
                expected = True
            except ValueError:
                expected = False
            assumptions = fixed+[binary_bits[f][row[1]] if lifted[f][1] & 1
                                 else -binary_bits[f][row[1]]
                                 for f, row in enumerate(control_projection)]
            if outer.solve(assumptions=assumptions) != expected:
                raise ArithmeticError('binary CNF disagrees with a small exact lift')
        outer.delete()
        receipt['binary_CNF_small_lifts_checked'] = 64
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(receipt, indent=2)+'\n')
        print(json.dumps(receipt))
        return
    outer, members, binary_bits = build_outer(G, Q, binary_pairs, args)
    started = time.monotonic()
    deadline = started+args.seconds
    report = {'group': G['name'], 'shape': args.shape,
              'seconds_limit': args.seconds, 'lift_models_limit': args.lift_models,
              'fixed_first_projection': str(args.first_projection),
              'projected_candidates': 0, 'lifted_candidates': 0,
              'untraced_core_cuts': 0, 'exact_farkas_cuts': 0,
              'exact_binary_cuts': 0, 'binary_filter': args.binary_filter,
              'pair_capacity': args.pair_capacity,
              'inverse_capacity': args.inverse_capacity,
              'native_binary': args.native_binary,
              'budget_skipped_projections': 0, 'status': 'running', 'witness': None,
              'scope': 'Discovery only. Untraced SAT cores and skipped projections are not exclusions.',
              'exponent_improvement': False}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    cut_path = args.output.with_suffix('.cuts.jsonl')
    cut_path.write_text('')

    def checkpoint():
        report['elapsed_seconds'] = time.monotonic()-started
        tmp = args.output.with_suffix('.tmp')
        tmp.write_text(json.dumps(report, indent=2)+'\n')
        tmp.replace(args.output)

    checkpoint()
    while time.monotonic() < deadline:
        solved = limited(outer, deadline)
        if solved is not True:
            report['status'] = ('outer-untraced-unsat' if solved is False else 'time-limit')
            break
        model = set(outer.get_model())
        projected = [[q for q, v in enumerate(row) if v in model] for row in members]
        report['projected_candidates'] += 1
        rejection = reject(binary_pairs, projected) if args.binary_filter else None
        if rejection:
            verify_rejection(binary_pairs, rejection)
            outer.add_clause([-members[f][q] for f, q in rejection['blocked_points']])
            with cut_path.open('a') as stream:
                stream.write(json.dumps(rejection, separators=(',', ':'))+'\n')
            report['exact_binary_cuts'] += 1
            checkpoint()
            continue
        inner, bits, active = lift_solver(G, Q, center, projected)
        assumptions = [v for row in active for v in row]
        point_for = {v: (f, q) for f, row in enumerate(active)
                     for q, v in zip(projected[f], row)}
        exhausted = False
        for _ in range(args.lift_models):
            lifted = limited(inner, deadline, assumptions)
            if lifted is not True:
                if lifted is False:
                    core = [point_for[v] for v in inner.get_core()]
                    outer.add_clause([-members[f][q] for f, q in core])
                    report['untraced_core_cuts'] += 1
                    exhausted = True
                break
            solution = set(inner.get_model())
            colors = [[sum((1 << b) for b, v in enumerate(pair) if v in solution)
                       for pair in row] for row in bits]
            sets = [[G['mul'][center[c]][Q['representatives'][q]]
                     for q, c in zip(row, colors[f])] for f, row in enumerate(projected)]
            for f in range(3):
                pair_map(G, sets[f], sets[(f+1) % 3])
            relations, _ = extra_relations(G, sets)
            answer = potential_or_circuit(relations, sum(args.shape))
            report['lifted_candidates'] += 1
            if 'potentials' in answer:
                report['witness'] = {'sets': sets, 'potentials': answer['potentials'],
                    'verification': verify_witness(G, sets, answer['potentials'])}
                report['status'] = 'exact-degeneration-witness'
                break
            points = set()
            for index in answer['indices']:
                s, t, tt, u, uu, ss = relations[index]['vertices']
                points.update(((0, s), (0, ss), (1, t), (1, tt), (2, u), (2, uu)))
            inner.add_clause([-active[f][i] for f, i in sorted(points)]+
                             [v if not (colors[f][i] >> b) & 1 else -v
                              for f, i in sorted(points) for b, v in enumerate(bits[f][i])])
            record = {'sets': sets, 'relation_vertices':
                [relations[i]['vertices'] for i in answer['indices']], 'weights': answer['weights']}
            verify_record(G, record)
            with cut_path.open('a') as stream:
                stream.write(json.dumps(record, separators=(',', ':'))+'\n')
            report['exact_farkas_cuts'] += 1
        inner.delete()
        if report['witness']:
            break
        if not exhausted:
            outer.add_clause([-members[f][q] for f, row in enumerate(projected) for q in row])
            report['budget_skipped_projections'] += 1
        checkpoint()
        if report['projected_candidates'] % 25 == 0:
            print(json.dumps(report), flush=True)
    if report['status'] == 'running':
        report['status'] = 'time-limit'
    outer.delete()
    checkpoint()
    print(json.dumps(report), flush=True)


if __name__ == '__main__':
    main()
