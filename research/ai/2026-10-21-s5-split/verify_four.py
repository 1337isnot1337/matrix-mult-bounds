"""Standard-dependency replay of the four-color S5 source search."""
import argparse
from collections import Counter
import gzip
import importlib.util
import json
from pathlib import Path

from four_colors import data
from central_slice import verify_match, slice_control
from group_exact import verify_witness
from verify_projected_reports import verify_farkas_record
from s5_source import NATIVE

spec = importlib.util.spec_from_file_location('s5_four_search_replayer', NATIVE/'verify.py')
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)


def replay(path):
    report = json.loads(path.read_text())
    if 'exact_central_slice_cuts' not in report:
        return helper.replay(path, data_provider=data, target_shape=(19, 19, 19))
    G, Q, receipt = data()
    slice_control()
    if (report['group'] != G['name'] or report['shape'] != [19]*3
            or report['source_and_normalization'] != json.loads(json.dumps(receipt))):
        raise ValueError('wrong four-color source or shape')
    cuts = path.with_suffix('.cuts.jsonl')
    payload = cuts.read_bytes() if cuts.exists() else gzip.decompress(Path(str(cuts)+'.gz').read_bytes())
    counts = Counter()
    for line in payload.splitlines():
        item = json.loads(line)
        if list(map(len, item['sets'])) != [19]*3:
            raise ValueError('wrong saved candidate shape')
        if item['type'] == 'exact-central-slice':
            verify_match(Q, item)
            if any(q not in item['sets'][f] for f, q in item['blocked_points']):
                raise ValueError('cut support is not present in its candidate')
        elif item['type'] == 'exact-farkas':
            verify_farkas_record(G, item)
        elif item['type'] == 'untraced-inner-unsat':
            if item['independent_proof'] is not False:
                raise ValueError('an untraced solver negative is not a proof')
        else:
            raise ValueError('unknown four-color discovery record')
        counts[item['type']] += 1
    for label, key in [('exact-central-slice', 'exact_central_slice_cuts'),
                       ('exact-farkas', 'exact_farkas_cuts'),
                       ('untraced-inner-unsat', 'untraced_inner_refutations')]:
        if counts[label] != report[key]:
            raise ValueError('four-color record count mismatch')
    if report['witness']:
        w = report['witness']
        if list(map(len, w['sets'])) != [19]*3:
            raise ValueError('wrong positive target shape')
        verify_witness(G, w['sets'], w['potentials'])
    return {'records': dict(counts), 'untraced_refutations_are_proofs': False,
            'witness': bool(report['witness']), 'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('report', type=Path)
    args = parser.parse_args()
    print(json.dumps(replay(args.report), indent=2))
