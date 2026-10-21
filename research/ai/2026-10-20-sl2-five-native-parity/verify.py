"""Standard-library replay of parity, pair-capacity and Farkas certificates."""
import argparse
from collections import Counter
import gzip
import json
from pathlib import Path

from data import data
from pair_capacity import verify as verify_capacity
from verify_projected_reports import verify_parity, verify_farkas_record
from group_exact import verify_witness


def replay(path):
    G, Q, receipt = data()
    report = json.loads(path.read_text())
    if report['group'] != G['name'] or report['shape'] != [10]*3:
        raise ValueError('wrong group or target')
    # JSON serializes the integer-keyed histogram as strings.
    if report['source_and_normalization'] != json.loads(json.dumps(receipt)):
        raise ValueError('changed source or normalization receipt')
    cuts = path.with_suffix('.cuts.jsonl')
    payload = (cuts.read_bytes() if cuts.exists()
               else gzip.decompress(Path(str(cuts)+'.gz').read_bytes()))
    counts = Counter()
    for line in payload.splitlines():
        item = json.loads(line)
        if item['type'] == 'exact-parity':
            if list(map(len, item['sets'])) != [10]*3:
                raise ValueError('wrong projected shape')
            verify_parity(Q, item)
        elif item['type'] == 'exact-pair-capacity':
            verify_capacity(Q, item)
        elif item['type'] == 'exact-farkas':
            if list(map(len, item['sets'])) != [10]*3:
                raise ValueError('wrong lifted shape')
            verify_farkas_record(G, item)
        else:
            raise ValueError('unknown certificate type')
        counts[item['type']] += 1
    for label, key in [('exact-parity', 'exact_parity_cuts'),
                       ('exact-pair-capacity', 'exact_pair_capacity_cuts'),
                       ('exact-farkas', 'exact_farkas_cuts')]:
        if counts[label] != report.get(key, 0):
            raise ValueError('certificate count mismatch')
    if report['witness']:
        witness = report['witness']
        if list(map(len, witness['sets'])) != report['shape']:
            raise ValueError('wrong positive target shape')
        verify_witness(G, witness['sets'], witness['potentials'])
    return {'certificates': dict(counts), 'witness': bool(report['witness']),
            'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('report', type=Path)
    args = parser.parse_args()
    print(json.dumps(replay(args.report), indent=2))
