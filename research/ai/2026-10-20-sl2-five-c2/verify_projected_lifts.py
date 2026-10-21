"""Integer-only acceptance of saved binary and Farkas rejection certificates."""
import argparse
import gzip
import json
from pathlib import Path

from source_data import group, subgroup_certificate, central_projection
from binary_lift_system import pair_classes, verify_rejection
from verify_structured import verify_record


def replay(path):
    G = group()
    Q = central_projection(G, subgroup_certificate(G))
    pairs = pair_classes(G, Q)
    report = json.loads(path.read_text())
    if report['group'] != G['name']:
        raise ValueError('wrong source group')
    cuts_path = path.with_suffix('.cuts.jsonl')
    payload = (cuts_path.read_bytes() if cuts_path.exists() else
               gzip.decompress(Path(str(cuts_path)+'.gz').read_bytes()))
    counts = {'exact-capacity': 0, 'exact-parity': 0, 'exact-farkas': 0}
    for line in payload.splitlines():
        record = json.loads(line)
        if list(map(len, record['sets'])) != report['shape']:
            raise ValueError('wrong candidate shape')
        kind = record.get('type', 'exact-farkas')
        if kind in ('exact-capacity', 'exact-parity'):
            verify_rejection(pairs, record)
        elif kind == 'exact-farkas':
            verify_record(G, record)
        else:
            raise ValueError('unknown certificate type')
        counts[kind] += 1
    if (counts['exact-capacity']+counts['exact-parity'] != report.get('exact_binary_cuts', 0)
            or counts['exact-farkas'] != report['exact_farkas_cuts']):
        raise ValueError('certificate counts differ from the report')
    if report['witness']:
        from group_exact import verify_witness
        witness = report['witness']
        if list(map(len, witness['sets'])) != report['shape']:
            raise ValueError('wrong witness shape')
        verify_witness(G, witness['sets'], witness['potentials'])
    return {'counts_checked': counts, 'witness_checked': bool(report['witness']),
            'untraced_core_cuts_not_verified': report['untraced_core_cuts'],
            'budget_skipped_projections': report['budget_skipped_projections'],
            'complete_exclusion': False, 'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('report', type=Path)
    args = parser.parse_args()
    print(json.dumps(replay(args.report), indent=2))
