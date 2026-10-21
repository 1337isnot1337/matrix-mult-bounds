"""Necessary two-bit parity equations for saturated projected pair fibers."""
import argparse
from collections import defaultdict
import gzip
import json
from pathlib import Path

from source_data import group, subgroup_certificate, central_projection
from binary_lift_system import (pair_classes, necessary_system, reject,
                               verify_rejection, verify_parity_record, eliminate)
from verify_structured import verify_record


def pair_data(G, Q, center):
    if [z & 1 for z in center] != [0, 1, 0, 1]:
        raise ArithmeticError('the first central bit must be the direct C2 coordinate')
    if any(G['mul'][center[a]][center[b]] != center[a ^ b]
           for a in range(4) for b in range(4)):
        raise ArithmeticError('center must have the recorded xor coordinates')
    index = {g: c for c, g in enumerate(center)}
    data = {}
    for s, rs in enumerate(Q['representatives']):
        for t, rt in enumerate(Q['representatives']):
            g = G['mul'][G['inv'][rs]][rt]
            q = Q['projection'][g]
            z = G['mul'][g][G['inv'][Q['representatives'][q]]]
            if z not in index:
                raise ArithmeticError('projected pair has a noncentral offset')
            data[s, t] = q, index[z]
    return data


def extend(system, data, sets):
    variables, rows = list(system['variables']), list(system['rows'])
    lookup = {v: i for i, v in enumerate(variables)}

    def add(labels, rhs, points):
        mask = 0
        for label in labels:
            if label not in lookup:
                lookup[label] = len(variables)
                variables.append(label)
            mask ^= 1 << lookup[label]
        rows.append({'mask': mask, 'rhs': rhs, 'support': sorted(set(points))})

    for f in range(3):
        h = (f+1) % 3
        fibers = defaultdict(list)
        for s in sorted(sets[f]):
            for t in sorted(sets[h]):
                q, offset = data[s, t]
                fibers[q].append((s, t, offset))
        for q, fiber in sorted(fibers.items()):
            if len(fiber) > 4:
                return {'pair_capacity_core': sorted({p for s, t, _ in fiber[:5]
                                                      for p in ((f, s), (h, t))})}
            if len(fiber) != 4:
                continue
            for bit, label in enumerate(('bit', 'twist')):
                labels, rhs, points = [], 0, []
                for s, t, offset in fiber:
                    labels.extend(((label, f, s), (label, h, t)))
                    rhs ^= (offset >> bit) & 1
                    points.extend(((f, s), (h, t)))
                add(labels, rhs, points)
    return {'variables': variables, 'rows': rows}


def saturated_reject(pairs, data, sets):
    system = necessary_system(pairs, sets)
    if 'capacity_core' in system:
        return reject(pairs, sets)
    system = extend(system, data, sets)
    if 'pair_capacity_core' in system:
        return {'type': 'exact-pair-capacity', 'sets': sets,
                'blocked_points': system['pair_capacity_core']}
    answer = eliminate(system)
    if answer['consistent']:
        return None
    rows = [system['rows'][i] for i in answer['circuit']]
    return {'type': 'exact-parity', 'sets': sets, 'saturated_pair_equations': True,
            'variables': system['variables'], 'rows': rows,
            'blocked_points': sorted({p for row in rows for p in row['support']})}


def verify_saturated(pairs, data, record):
    if record['type'] != 'exact-pair-capacity' and not record.get('saturated_pair_equations'):
        return verify_rejection(pairs, record)
    system = necessary_system(pairs, record['sets'])
    if 'capacity_core' in system:
        raise ValueError('wrong saturated rejection type')
    system = extend(system, data, record['sets'])
    if record['type'] == 'exact-pair-capacity':
        if ('pair_capacity_core' not in system or system['pair_capacity_core'] !=
                list(map(tuple, record['blocked_points']))):
            raise ValueError('wrong projected pair-fiber capacity support')
        return True
    if 'pair_capacity_core' in system:
        raise ValueError('wrong saturated parity type')
    return verify_parity_record(system, record)


def replay(path):
    G = group()
    cert = subgroup_certificate(G)
    Q = central_projection(G, cert)
    pairs, data = pair_classes(G, Q), pair_data(G, Q, cert['center'])
    report = json.loads(path.read_text())
    cut_path = path.with_suffix('.cuts.jsonl')
    payload = (cut_path.read_bytes() if cut_path.exists() else
               gzip.decompress(Path(str(cut_path)+'.gz').read_bytes()))
    counts = defaultdict(int)
    for line in payload.splitlines():
        record = json.loads(line)
        if list(map(len, record['sets'])) != report['shape']:
            raise ValueError('wrong candidate shape')
        if 'relation_vertices' in record:
            verify_record(G, record)
            counts['exact-farkas'] += 1
        else:
            verify_saturated(pairs, data, record)
            counts[record['type']] += 1
            if record.get('saturated_pair_equations'):
                counts['saturated-parity-subtotal'] += 1
    binary = sum(counts[k] for k in ('exact-capacity', 'exact-parity', 'exact-pair-capacity'))
    if binary != report['exact_binary_cuts'] or counts['exact-farkas'] != report['exact_farkas_cuts']:
        raise ValueError('certificate counts differ from report')
    return {'counts_checked': dict(counts), 'untraced_cores_not_verified': report['untraced_core_cuts'],
            'complete_exclusion': False, 'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('report', type=Path)
    args = parser.parse_args()
    print(json.dumps(replay(args.report), indent=2))
