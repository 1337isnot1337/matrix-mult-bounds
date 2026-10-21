"""Incremental projected-capacity search with exact parity/potential acceptance."""
import argparse
import gzip
import hashlib
from itertools import combinations
import json
import math
from pathlib import Path
import random
import time

from s5_source import data
from central_lift import lift_system, eliminate, lifted_sets
from pair_capacity import violations
from verify_projected_reports import verify_parity, verify_farkas_record
from group_exact import pair_map, extra_relations, verify_witness, verify_farkas
from search import potential_or_circuit


def run(output, seconds, seed=2026102114, start_report=None):
    G, Q, receipt = data()
    rng, shape, n = random.Random(seed), [13, 14, 14], 120
    inherited, reused = [], None
    if start_report is not None:
        if start_report.resolve() == output.resolve():
            raise ValueError('reuse requires a different output path')
        parent = json.loads(start_report.read_text())
        if parent['group'] != G['name'] or parent['shape'] != shape:
            raise ValueError('wrong reused source or shape')
        path = start_report.with_suffix('.cuts.jsonl')
        payload = path.read_bytes() if path.exists() else gzip.decompress(Path(str(path)+'.gz').read_bytes())
        for line in payload.splitlines():
            item = json.loads(line)
            if item['type'] != 'exact-parity':
                continue
            verify_parity(Q, item)
            if list(map(len, item['sets'])) != shape:
                raise ValueError('wrong reused candidate shape')
            inherited.append(item)
        if not inherited:
            raise ValueError('no verified parity candidate to warm-start')
        sets = [list(S) for S in inherited[-1]['sets']]
        reused = {'report': str(start_report), 'sha256': hashlib.sha256(start_report.read_bytes()).hexdigest(),
                  'verified_parity_circuits': len(inherited)}
    else:
        sets = [[0]+rng.sample(range(1, n), size-1) for size in shape]
    present = [set(S) for S in sets]
    inverse = Q['inv']
    classes = [[min(Q['mul'][g][inverse[h]], inverse[Q['mul'][g][inverse[h]]])
                for h in range(n)] for g in range(n)]
    frequencies = [[0]*n for _ in range(3)]
    pairs = [(0, 1), (0, 2), (1, 2)]
    labels = [[0]*n for _ in pairs]
    for f, S in enumerate(sets):
        for g, h in combinations(S, 2):
            frequencies[f][classes[g][h]] += 1
    for i, (f, h) in enumerate(pairs):
        for g in sets[f]:
            for k in sets[h]:
                labels[i][Q['mul'][inverse[g]][k]] += 1
    cuts, cut_counts, memberships, seen_lifts = [], [], {}, set()
    for item in inherited:
        support = list(map(tuple, item['blocked_points']))
        j = len(cuts)
        cuts.append(support)
        cut_counts.append(sum(p in present[f] for f, p in support))
        for point in support:
            memberships.setdefault(point, []).append(j)

    def energy():
        return (2*sum(max(0, sum(frequencies[f][c] > 0 for f in range(3))-2)**2 for c in Q['classes'])
                + sum(max(0, value-2)**2 for row in labels for value in row)
                + 10*sum(count == len(cut) for cut, count in zip(cuts, cut_counts)))

    current = energy()
    output.parent.mkdir(parents=True, exist_ok=True)
    cut_path = output.with_suffix('.cuts.jsonl')
    cut_path.write_text('')
    started = time.monotonic()
    report = {'group': G['name'], 'shape': shape, 'source_and_normalization': receipt,
              'method': 'Incremental projected capacities with exact conditional parity cuts',
              'seed': seed, 'seconds_limit': seconds, 'steps': 0, 'minimum_energy': current,
              'projected_model_events': 0, 'exact_parity_cuts': 0, 'exact_farkas_cuts': 0,
              'pair_injective_models': 0, 'witness': None, 'status': 'running',
              'best_projected_sets': [list(S) for S in sets],
              'reused': reused,
              'normalizations_used': 'Identity points fixed; subgroup quotas and anchor constraints not imposed.',
              'exponent_improvement': False, 'scope': 'Bounded stochastic discovery. '
              'Only exported exact witnesses/circuits are accepted. No exclusion claim.'}

    def save(item):
        with cut_path.open('a') as stream:
            stream.write(json.dumps(item, separators=(',', ':'))+'\n')

    def checkpoint():
        report['elapsed_seconds'] = time.monotonic()-started
        report['current_energy'] = current
        tmp = output.with_suffix('.tmp')
        tmp.write_text(json.dumps(report, indent=2)+'\n')
        tmp.replace(output)

    checkpoint()
    while time.monotonic()-started < seconds:
        report['steps'] += 1
        f = rng.randrange(3)
        index = rng.randrange(1, len(sets[f]))
        old = sets[f][index]
        new = rng.randrange(1, n)
        if new in present[f]:
            continue
        changes, delta = [], 0
        for other in sets[f]:
            if other != old:
                changes += [('class', f, classes[old][other], -1),
                            ('class', f, classes[new][other], 1)]
        for i, (left, right) in enumerate(pairs):
            if f == left:
                for other in sets[right]:
                    changes += [('pair', i, Q['mul'][inverse[old]][other], -1),
                                ('pair', i, Q['mul'][inverse[new]][other], 1)]
            elif f == right:
                for other in sets[left]:
                    changes += [('pair', i, Q['mul'][inverse[other]][old], -1),
                                ('pair', i, Q['mul'][inverse[other]][new], 1)]

        def adjust(kind, i, c, amount):
            if kind == 'class':
                before = max(0, sum(frequencies[h][c] > 0 for h in range(3))-2)**2
                frequencies[i][c] += amount
                after = max(0, sum(frequencies[h][c] > 0 for h in range(3))-2)**2
                return 2*(after-before)
            before = max(0, labels[i][c]-2)**2
            labels[i][c] += amount
            return max(0, labels[i][c]-2)**2-before

        for change in changes:
            delta += adjust(*change)
        cut_changes = {}
        for j in memberships.get((f, old), []):
            cut_changes[j] = cut_changes.get(j, 0)-1
        for j in memberships.get((f, new), []):
            cut_changes[j] = cut_changes.get(j, 0)+1
        for j, amount in cut_changes.items():
            delta += 10*(int(cut_counts[j]+amount == len(cuts[j]))-int(cut_counts[j] == len(cuts[j])))
        temperature = 0.08+1.5*(1-(report['steps'] % 40000)/40000)
        accepted = delta <= 0 or rng.random() < math.exp(-delta/temperature)
        if not accepted:
            for kind, i, c, amount in reversed(changes):
                adjust(kind, i, c, -amount)
        else:
            current += delta
            sets[f][index] = new
            present[f].remove(old)
            present[f].add(new)
            for j, amount in cut_changes.items():
                cut_counts[j] += amount
            if current < report['minimum_energy']:
                report['minimum_energy'] = current
                report['best_projected_sets'] = [list(S) for S in sets]
        if current == 0:
            if violations(Q, sets):
                raise ArithmeticError('incremental pair capacity energy is incorrect')
            report['projected_model_events'] += 1
            system = lift_system(Q, sets)
            answer = eliminate(system)
            if not answer['consistent']:
                rows = [system['rows'][i] for i in answer['circuit']]
                support = sorted({tuple(p) for row in rows for p in row['support']})
                item = {'type': 'exact-parity', 'sets': [list(S) for S in sets],
                        'variables': system['variables'], 'rows': rows, 'blocked_points': support}
                verify_parity(Q, item)
                save(item)
                j = len(cuts)
                cuts.append(support)
                cut_counts.append(len(support))
                for point in support:
                    memberships.setdefault(point, []).append(j)
                current += 10
                report['exact_parity_cuts'] += 1
            else:
                lifted = lifted_sets(G, Q, system, answer['assignment'], sets)
                key = tuple(tuple(sorted(S)) for S in lifted)
                if key in seen_lifts:
                    continue
                seen_lifts.add(key)
                for h in range(3):
                    pair_map(G, lifted[h], lifted[(h+1) % 3])
                report['pair_injective_models'] += 1
                relations, _ = extra_relations(G, lifted)
                result = potential_or_circuit(relations, sum(shape))
                if 'potentials' in result:
                    report['witness'] = {'sets': lifted, 'potentials': result['potentials'],
                        'verification': verify_witness(G, lifted, result['potentials'])}
                    report['status'] = 'exact-target-witness'
                    break
                if not verify_farkas(relations, result['indices'], result['weights']):
                    raise ArithmeticError('invalid exact local-search Farkas circuit')
                points = set()
                for i in result['indices']:
                    s, t, tt, u, uu, ss = relations[i]['vertices']
                    points.update(((0, lifted[0][s]), (0, lifted[0][ss]), (1, lifted[1][t]),
                                   (1, lifted[1][tt]), (2, lifted[2][u]), (2, lifted[2][uu])))
                item = {'type': 'exact-farkas', 'sets': lifted, 'relation_vertices':
                        [relations[i]['vertices'] for i in result['indices']],
                        'weights': result['weights'], 'blocked_lift_points': sorted(points)}
                verify_farkas_record(G, item)
                save(item)
                report['exact_farkas_cuts'] += 1
                # Sampling moves on; this does not assert that the projection has no other lift.
        if report['steps'] % 10000 == 0:
            if current != energy():
                raise ArithmeticError('incremental energy drift')
            checkpoint()
    report['status'] = report['status'] if report['witness'] else 'time-limit'
    checkpoint()
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--seconds', type=float, default=120)
    parser.add_argument('--seed', type=int, default=2026102114)
    parser.add_argument('--start-report', type=Path)
    args = parser.parse_args()
    print(json.dumps({k: v for k, v in run(args.output, args.seconds, args.seed, args.start_report).items()
                      if k not in ('source_and_normalization', 'witness')}))
