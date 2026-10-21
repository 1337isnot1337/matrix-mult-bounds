"""Bounded PSL(2,7) projection search with exact parity and Farkas cuts."""
import argparse
from itertools import combinations, product
import json
from pathlib import Path
import random
import sys
import time

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Cadical195

sys.path.insert(0, str(Path(__file__).with_name('imported')))
from group_exact import group, extra_relations, verify_witness, verify_farkas
from search import potential_or_circuit
from central_lift import quotient, lift_system, eliminate, lifted_sets
from subgroup_normalization import octahedral_certificate
from abelian_fiber_cuts import cyclic_subgroups, append_cuts
from parity_templates import read_verified, append_templates


def build_projection(Q, shape, subgroup, seed, fiber_records=None, reused_cuts=None):
    pool, clauses = IDPool(), []
    n = len(Q['representatives'])
    members = [[pool.id(('member', f, p)) for p in range(n)] for f in range(3)]
    owners = [{c: pool.id(('owner', f, c)) for c in Q['classes']} for f in range(3)]
    H = sorted({Q['projection'][g] for g in subgroup['members']})
    if n % len(H):
        raise ValueError('normalization subgroup index must be integral')
    index = n//len(H)
    anchors = sorted({Q['projection'][g] for g in subgroup['anchors']}-{0})
    for f in range(3):
        clauses.append([members[f][0]])
        clauses.extend(CardEnc.equals(members[f], shape[f], vpool=pool,
                                     encoding=EncType.seqcounter).clauses)
        clauses.extend(CardEnc.atleast([members[f][p] for p in H], (shape[f]+index-1)//index,
                                      vpool=pool, encoding=EncType.seqcounter).clauses)
        for (u, v), (c, _) in Q['pairs'].items():
            clauses.append([-members[f][u], -members[f][v], owners[f][c]])
    clauses.append([members[0][p] for p in anchors])
    for c in Q['classes']:
        for chosen in combinations(range(3), len(Q['fibers'][c])+1):
            clauses.append([-owners[f][c] for f in chosen])
    fiber_metadata = append_cuts(fiber_records, pool, members, owners, clauses) if fiber_records else None
    template_metadata = append_templates(Q, reused_cuts, pool, members, clauses) if reused_cuts else None
    rng = random.Random(seed)
    rng.shuffle(clauses)
    solver = Cadical195(bootstrap_with=clauses)
    solver.set_phases([v if rng.randrange(2) else -v for row in members for v in row])
    return solver, members, {'variables': pool.top, 'clauses': len(clauses),
                            'projected_order': n, 'inverse_classes': len(Q['classes']),
                            'subgroup_order': len(H), 'subgroup_index': index,
                            'abelian_fiber_cuts': fiber_metadata,
                            'reused_parity_templates': template_metadata,
                            'identity_fiber_lower': [(s+index-1)//index for s in shape]}


def parity_cnf(system):
    clauses = []
    for row in system['rows']:
        indices = [i for i in range(len(system['variables'])) if row['mask'] >> i & 1]
        for bits in product((0, 1), repeat=len(indices)):
            if sum(bits) % 2 != row['rhs']:
                clauses.append([-(i+1) if bit else i+1 for i, bit in zip(indices, bits)])
    return clauses


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seconds', type=float, default=600)
    parser.add_argument('--seed', type=int, default=20261320)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--fiber-cuts', action='store_true')
    parser.add_argument('--reuse-report', action='append', type=Path, default=[])
    args = parser.parse_args()
    G = group(7)
    z = G['matrices'].index((6, 0, 0, 6))
    Q = quotient(G, z)
    shape = [16, 16, 17]
    fiber_records = cyclic_subgroups(G, Q) if args.fiber_cuts else None
    reused_cuts, reused_sources = [], []
    for path in args.reuse_report:
        items, receipt = read_verified(Q, path)
        reused_cuts.extend(items)
        reused_sources.append(receipt)
    solver, members, encoding = build_projection(Q, shape, octahedral_certificate(G),
                                                args.seed, fiber_records, reused_cuts)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    cuts_path = args.output.with_suffix('.cuts.jsonl')
    started = time.monotonic()
    result = {'group': G['name'], 'shape': shape, 'seed': args.seed,
              'encoding': encoding, 'seconds_limit': args.seconds,
              'reused_sources': reused_sources,
              'projected_models': 0, 'exact_parity_cuts': 0, 'lift_models': 0,
              'exact_farkas_cuts': 0, 'solver_reported_lift_refutations': 0,
              'status': 'running', 'witness': None,
              'scope': 'Bounded discovery. Exact accepted witnesses only. '
                       'Solver refutations have no exported proof trace.'}

    def checkpoint():
        result['elapsed_seconds'] = time.monotonic()-started
        result['sat_statistics'] = solver.accum_stats()
        tmp = args.output.with_suffix('.tmp')
        tmp.write_text(json.dumps(result, indent=2)+'\n')
        tmp.replace(args.output)

    def record(item):
        with cuts_path.open('a') as out:
            out.write(json.dumps(item, separators=(',', ':'))+'\n')

    checkpoint()
    with cuts_path.open('w'):
        pass
    while time.monotonic()-started < args.seconds:
        solver.conf_budget(5000)
        solved = solver.solve_limited()
        if solved is None:
            checkpoint()
            continue
        if solved is False:
            result['status'] = 'solver-reported-projection-unsatisfiable; no proof trace'
            break
        model = {v for v in solver.get_model() if v > 0}
        sets = [[p for p, v in enumerate(row) if v in model] for row in members]
        result['projected_models'] += 1
        result['current_projected_sets'] = sets
        system = lift_system(Q, sets)
        decision = eliminate(system)
        if not decision['consistent']:
            support = sorted({tuple(p) for i in decision['circuit']
                              for p in system['rows'][i]['support']})
            solver.add_clause([-members[f][p] for f, p in support])
            record({'type': 'exact-parity', 'sets': sets, 'variables': system['variables'],
                    'rows': [system['rows'][i] for i in decision['circuit']],
                    'blocked_points': support})
            result['exact_parity_cuts'] += 1
            checkpoint()
            continue
        inner = Cadical195(bootstrap_with=parity_cnf(system))
        lookup = {v: i+1 for i, v in enumerate(system['variables'])}
        inner_refuted = False
        while time.monotonic()-started < args.seconds:
            inner.conf_budget(5000)
            solved_lift = inner.solve_limited()
            if solved_lift is None:
                checkpoint()
                continue
            if solved_lift is False:
                inner_refuted = True
                result['solver_reported_lift_refutations'] += 1
                break
            assignment = sum(1 << (v-1) for v in inner.get_model() if v > 0)
            actual = lifted_sets(G, Q, system, assignment, sets)
            relations, _ = extra_relations(G, actual)
            result['lift_models'] += 1
            answer = potential_or_circuit(relations, sum(shape))
            if 'potentials' in answer:
                receipt = verify_witness(G, actual, answer['potentials'])
                result['witness'] = {'sets': actual, 'potentials': answer['potentials'],
                                     'verification': receipt}
                result['status'] = 'exact-degeneration-witness'
                checkpoint()
                break
            if not verify_farkas(relations, answer['indices'], answer['weights']):
                raise ArithmeticError('invalid Farkas circuit')
            selected = set()
            for i in answer['indices']:
                s, t, tt, u, uu, ss = relations[i]['vertices']
                selected.update([(0, actual[0][s]), (0, actual[0][ss]),
                                 (1, actual[1][t]), (1, actual[1][tt]),
                                 (2, actual[2][u]), (2, actual[2][uu])])
            clause = [-lookup['sign', f, Q['projection'][g]] if Q['bits'][g]
                      else lookup['sign', f, Q['projection'][g]] for f, g in sorted(selected)]
            inner.add_clause(clause)
            record({'type': 'exact-farkas', 'sets': actual,
                    'relation_vertices': [relations[i]['vertices'] for i in answer['indices']],
                    'weights': answer['weights'], 'blocked_lift_points': sorted(selected)})
            result['exact_farkas_cuts'] += 1
            checkpoint()
        inner.delete()
        if result['witness']:
            break
        if inner_refuted:
            solver.add_clause([-members[f][p] for f in range(3) for p in sets[f]])
            record({'type': 'solver-reported-lift-refutation; no proof trace', 'sets': sets})
        checkpoint()
    if result['status'] == 'running':
        result['status'] = 'time-limit'
    checkpoint()
    solver.delete()
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
