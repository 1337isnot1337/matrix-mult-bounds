"""Joint point/sign search by learning exact conditional parity equations."""
import argparse
from itertools import product
import json
from pathlib import Path
import sys
import time

from data import data, ROOT, SEVEN
sys.path.insert(0, str(SEVEN))
from projected_search import build_projection
from central_lift import lift_system, eliminate, lifted_sets
from verify_projected_reports import verify_parity, verify_farkas_record
from group_exact import pair_map, extra_relations, verify_witness, verify_farkas
from search import potential_or_circuit
from pair_capacity import violations, verify as verify_capacity, append_patterns
from parity_templates import read_verified


def run(output, seconds, control=False, capacity=False, reuse=(), full_capacity=False,
        split_cover=False, data_provider=None, target_shape=(10, 10, 10),
        known_control=None, normalizer=None):
    if data_provider is not None:
        G, Q, receipt = data_provider()
    elif split_cover:
        from split_source import split_data
        G, Q, receipt = split_data()
    else:
        G, Q, receipt = data()
    shape = list(target_shape)
    subgroup = {'members': receipt['subgroup_members'], 'anchors':
                [Q['representatives'][p] for p in receipt['first_pair_anchor_disjunction']]}
    known = None
    if control:
        control_path = known_control or (ROOT/'results/sl2-five-native-2026-10-20/split-control3.json'
                        if split_cover else ROOT/'results/group-potentials-2026-10-20/sl2-5-control3-3-3.json')
        known = json.loads(control_path.read_text())['witness']
        shape = list(map(len, known['sets']))
        subgroup['anchors'] = [g for g in known['sets'][0] if Q['projection'][g]]
    reused, sources = [], []
    for path in reuse:
        items, source = read_verified(Q, path)
        reused.extend(items)
        sources.append(source)
    solver, members, encoding = build_projection(Q, shape, subgroup, 20260513,
                                                reused_cuts=reused)
    if encoding['subgroup_index'] != receipt['subgroup_index']:
        raise ArithmeticError('normalization subgroup index differs from its certificate')
    top = encoding['variables']
    if full_capacity:
        top, encoding['complete_pair_capacity'] = append_patterns(Q, solver, members, top)
    variables, learned = {}, set()

    def variable(label):
        nonlocal top
        label = tuple(label)
        if label not in variables:
            top += 1
            variables[label] = top
        return variables[label]

    if normalizer is not None:
        encoding['canonicalization'] = normalizer(G, Q, receipt, members, variable, solver.add_clause)

    def learn(system):
        added = 0
        for row in system['rows']:
            ids = sorted(variable(label) for i, label in enumerate(system['variables'])
                         if row['mask'] >> i & 1)
            points = tuple(map(tuple, row['support']))
            key = tuple(ids), row['rhs'], points
            if key in learned:
                continue
            learned.add(key)
            guard = [-members[f][p] for f, p in points]
            for bits in product(range(2), repeat=len(ids)):
                if sum(bits) % 2 != row['rhs']:
                    solver.add_clause(guard+[v if not b else -v for v, b in zip(ids, bits)])
            added += 1
        return added

    if control:
        projected = [[Q['projection'][g] for g in row] for row in known['sets']]
        system = lift_system(Q, projected)
        rows = learn(system)
        fixed = [v if p in projected[f] else -v
                 for f, row in enumerate(members) for p, v in enumerate(row)]
        fixed += [variable(('sign', f, Q['projection'][g])) if Q['bits'][g]
                  else -variable(('sign', f, Q['projection'][g]))
                  for f, row in enumerate(known['sets']) for g in row]
        if not solver.solve(assumptions=fixed):
            raise ArithmeticError('conditional parity rejected the known exact witness')
        solver.delete()
        result = {'known_projection_and_signs_accepted': True, 'induced_rows_checked': rows,
                  'weighted_control': verify_witness(G, known['sets'], known['potentials'])}
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, indent=2)+'\n')
        return result
    output.parent.mkdir(parents=True, exist_ok=True)
    cut_path = output.with_suffix('.cuts.jsonl')
    cut_path.write_text('')
    started = time.monotonic()
    report = {'group': G['name'], 'shape': shape, 'encoding': encoding,
        'source_and_normalization': receipt, 'seconds_limit': seconds,
        'projected_model_events': 0, 'learned_parity_rows': 0, 'exact_parity_cuts': 0,
        'exact_pair_capacity_cuts': 0, 'pair_capacity_enabled': capacity,
        'reused_sources': sources,
        'pair_injective_models': 0, 'exact_farkas_cuts': 0, 'status': 'running', 'witness': None,
        'exponent_improvement': False, 'scope': 'Bounded discovery; model events need not '
        'have distinct projections. Untraced solver negatives are not exclusions.'}

    def checkpoint():
        report['elapsed_seconds'] = time.monotonic()-started
        report['sat_statistics'] = solver.accum_stats()
        tmp = output.with_suffix('.tmp')
        tmp.write_text(json.dumps(report, indent=2)+'\n')
        tmp.replace(output)

    def save(record):
        with cut_path.open('a') as stream:
            stream.write(json.dumps(record, separators=(',', ':'))+'\n')

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
        model = set(solver.get_model())
        projected = [[p for p, v in enumerate(row) if v in model] for row in members]
        report['projected_model_events'] += 1
        bad = violations(Q, projected) if capacity else []
        if bad:
            for record in bad:
                points = verify_capacity(Q, record)
                solver.add_clause([-members[f][p] for f, p in points])
                save(record)
                report['exact_pair_capacity_cuts'] += 1
            checkpoint()
            continue
        system = lift_system(Q, projected)
        for label in system['variables']:
            variable(label)
        assignment = sum(1 << i for i, label in enumerate(system['variables'])
                         if variables[tuple(label)] in model)
        added = learn(system)
        report['learned_parity_rows'] += added
        answer = eliminate(system)
        if not answer['consistent']:
            rows = [system['rows'][i] for i in answer['circuit']]
            points = sorted({tuple(p) for row in rows for p in row['support']})
            record = {'type': 'exact-parity', 'sets': projected, 'variables': system['variables'],
                      'rows': rows, 'blocked_points': points}
            verify_parity(Q, record)
            solver.add_clause([-members[f][p] for f, p in points])
            save(record)
            report['exact_parity_cuts'] += 1
        elif any((row['mask'] & assignment).bit_count() % 2 != row['rhs'] for row in system['rows']):
            if not added:
                raise ArithmeticError('SAT model violates a previously learned row')
            solver.set_phases([variable(label) if answer['assignment'] >> i & 1
                               else -variable(label) for i, label in enumerate(system['variables'])])
        else:
            sets = lifted_sets(G, Q, system, assignment, projected)
            for f in range(3):
                pair_map(G, sets[f], sets[(f+1) % 3])
            report['pair_injective_models'] += 1
            relations, _ = extra_relations(G, sets)
            decision = potential_or_circuit(relations, sum(shape))
            if 'potentials' in decision:
                report['witness'] = {'sets': sets, 'potentials': decision['potentials'],
                    'verification': verify_witness(G, sets, decision['potentials'])}
                report['status'] = 'exact-target-witness'
                break
            if not verify_farkas(relations, decision['indices'], decision['weights']):
                raise ArithmeticError('invalid Farkas discovery')
            points = set()
            for i in decision['indices']:
                s, t, tt, u, uu, ss = relations[i]['vertices']
                points.update(((0, sets[0][s]), (0, sets[0][ss]), (1, sets[1][t]),
                               (1, sets[1][tt]), (2, sets[2][u]), (2, sets[2][uu])))
            clause = []
            for f, g in sorted(points):
                p = Q['projection'][g]
                sign = variable(('sign', f, p))
                clause.extend((-members[f][p], sign if not Q['bits'][g] else -sign))
            solver.add_clause(clause)
            record = {'type': 'exact-farkas', 'sets': sets, 'relation_vertices':
                [relations[i]['vertices'] for i in decision['indices']], 'weights': decision['weights'],
                'blocked_lift_points': sorted(points)}
            verify_farkas_record(G, record)
            save(record)
            report['exact_farkas_cuts'] += 1
        checkpoint()
        if report['projected_model_events'] % 25 == 0:
            print(json.dumps({k: report[k] for k in ('projected_model_events', 'learned_parity_rows',
                  'exact_parity_cuts', 'pair_injective_models', 'exact_farkas_cuts', 'elapsed_seconds')}), flush=True)
    if report['status'] == 'running':
        report['status'] = 'time-limit'
    checkpoint()
    solver.delete()
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--seconds', type=float, default=600)
    parser.add_argument('--control', action='store_true')
    parser.add_argument('--capacity', action='store_true')
    parser.add_argument('--full-capacity', action='store_true')
    parser.add_argument('--split-cover', action='store_true')
    parser.add_argument('--reuse-report', action='append', type=Path, default=[])
    args = parser.parse_args()
    result = run(args.output, args.seconds, args.control, args.capacity,
                 args.reuse_report, args.full_capacity, args.split_cover)
    print(json.dumps({k: v for k, v in result.items() if k not in ('source_and_normalization', 'witness')}))
