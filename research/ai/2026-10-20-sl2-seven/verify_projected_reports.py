"""Replay projected-search parity cuts using only exact group arithmetic."""
import argparse
from collections import Counter
import gzip
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).with_name('imported')))
from group_exact import group, verify_witness, verify_farkas, pair_map
from central_lift import quotient, lift_system


def row_key(row):
    return row['mask'], row['rhs'], tuple(tuple(x) for x in row['support'])


def verify_parity(Q, item):
    system = lift_system(Q, item['sets'])
    if [tuple(x) for x in item['variables']] != system['variables']:
        raise ValueError('wrong parity variable labels')
    expected = Counter(map(row_key, system['rows']))
    actual = Counter(map(row_key, item['rows']))
    if not actual or any(count > expected[key] for key, count in actual.items()):
        raise ValueError('parity row not induced by the group configuration')
    mask, rhs = 0, 0
    for row in item['rows']:
        mask ^= row['mask']
        rhs ^= row['rhs']
    if mask or rhs != 1:
        raise ValueError('not a contradictory parity circuit')
    support = sorted({tuple(x) for row in item['rows'] for x in row['support']})
    if support != [tuple(x) for x in item['blocked_points']]:
        raise ValueError('wrong conditional point support')
    return True


def verify_farkas_record(G, item):
    sets = item['sets']
    shape = list(map(len, sets))
    for f in range(3):
        pair_map(G, sets[f], sets[(f+1) % 3])
    relations, support = [], set()
    for s, t, tt, u, uu, ss in item['relation_vertices']:
        if any(not 0 <= p < shape[f] for f, p in
               [(0, s), (1, t), (1, tt), (2, u), (2, uu), (0, ss)]):
            raise ValueError('invalid vertex index')
        if (s, t, u) == (ss, tt, uu):
            raise ValueError('intended term used in a strict constraint')
        x = G['mul'][G['inv'][sets[0][s]]][sets[1][t]]
        y = G['mul'][G['inv'][sets[1][tt]]][sets[2][u]]
        z = G['mul'][G['inv'][sets[2][uu]]][sets[0][ss]]
        if G['mul'][G['mul'][x][y]][z] != 0:
            raise ValueError('not a group support term')
        row = [0]*sum(shape)
        for f, p, sign in [(0, s, 1), (0, ss, -1), (1, tt, 1),
                           (1, t, -1), (2, uu, 1), (2, u, -1)]:
            row[sum(shape[:f])+p] += sign
            support.add((f, sets[f][p]))
        relations.append({'row': row})
    if not verify_farkas(relations, list(range(len(relations))), item['weights']):
        raise ValueError('not a positive integer dependence')
    if sorted(support) != [tuple(x) for x in item['blocked_lift_points']]:
        raise ValueError('wrong lifted point support')
    return True


def replay(report_path):
    G = group(7)
    Q = quotient(G, G['matrices'].index((6, 0, 0, 6)))
    report = json.loads(report_path.read_text())
    if report['group'] != 'SL(2,7)' or report['shape'] != [16, 16, 17]:
        raise ValueError('wrong source or target shape')
    counts = {'exact-parity': 0, 'exact-farkas': 0, 'untraced-solver': 0}
    cuts_path = report_path.with_suffix('.cuts.jsonl')
    payload = (cuts_path.read_text() if cuts_path.exists() else
               gzip.decompress(Path(str(cuts_path)+'.gz').read_bytes()).decode())
    for line in payload.splitlines():
        item = json.loads(line)
        if list(map(len, item['sets'])) != report['shape']:
            raise ValueError('wrong candidate shape')
        if item['type'] == 'exact-parity':
            verify_parity(Q, item)
            counts['exact-parity'] += 1
        elif item['type'] == 'exact-farkas':
            verify_farkas_record(G, item)
            counts['exact-farkas'] += 1
        elif item['type'] == 'solver-reported-lift-refutation; no proof trace':
            counts['untraced-solver'] += 1
        else:
            raise ValueError('unknown record type')
    if counts['exact-parity'] != report['exact_parity_cuts']:
        raise ValueError('parity cut count mismatch')
    if counts['exact-farkas'] != report['exact_farkas_cuts']:
        raise ValueError('Farkas cut count mismatch')
    if counts['untraced-solver'] != report['solver_reported_lift_refutations']:
        raise ValueError('untraced solver record count mismatch')
    if report['witness']:
        witness = report['witness']
        if list(map(len, witness['sets'])) != report['shape']:
            raise ValueError('wrong witness shape')
        verify_witness(G, witness['sets'], witness['potentials'])
    return {'report': str(report_path), 'checked': counts,
            'witness_checked': bool(report['witness']),
            'unsat_proof_checked': False, 'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('report', type=Path)
    args = parser.parse_args()
    print(json.dumps(replay(args.report), indent=2))
