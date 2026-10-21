"""Independently replay every canonical structured-parent rejection; integers only."""
import argparse
import gzip
from itertools import product
import json
from pathlib import Path
import sys

from source_data import group, subgroup_certificate, SEVEN
from structured_sections import enumerate_sections
sys.path.insert(0, str(SEVEN))
from verify_projected_reports import verify_farkas_record


def verify_record(G, item):
    vertices = item['relation_vertices']
    if any(len(v) != 6 for v in vertices):
        raise ValueError('wrong relation width')
    points = set()
    for s, t, tt, u, uu, ss in vertices:
        for f, p in ((0, s), (0, ss), (1, t), (1, tt), (2, u), (2, uu)):
            if type(p) is not int or not 0 <= p < len(item['sets'][f]):
                raise ValueError('invalid vertex index')
            points.add((f, item['sets'][f][p]))
    checked = dict(item, blocked_lift_points=sorted(points))
    return verify_farkas_record(G, checked)


def replay(report_path):
    report = json.loads(report_path.read_text())
    if (report['group'] != 'SL(2,5) x C2' or report['shape'] != [10]*3
            or report['status'] != 'all-canonical-triples-rejected'
            or report['witness'] is not None):
        raise ValueError('not a completed structured-parent exclusion')
    G = group()
    choices, enumeration = enumerate_sections(G, subgroup_certificate(G))
    if report['enumeration'] != json.loads(json.dumps(enumeration)):
        raise ValueError('enumeration metadata changed')
    expected = set(product(*[list(map(tuple, row)) for row in choices]))
    cut_path = report_path.with_suffix('.cuts.jsonl')
    payload = (cut_path.read_bytes() if cut_path.exists() else
               gzip.decompress(Path(str(cut_path)+'.gz').read_bytes()))
    seen = set()
    for line in payload.splitlines():
        item = json.loads(line)
        key = tuple(map(tuple, item['sets']))
        if key not in expected or key in seen:
            raise ValueError('unexpected or repeated canonical triple')
        verify_record(G, item)
        seen.add(key)
    count = len(expected)
    if (seen != expected or any(report[k] != count for k in
            ('canonical_triples', 'tested', 'exact_cuts'))):
        raise ValueError('incomplete canonical triple coverage')
    return {'canonical_triples_checked': count, 'exact_integer_circuits_checked': count,
            'enumeration_recomputed': True, 'floating_point_used': False,
            'scope': report['scope'], 'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('report', type=Path)
    args = parser.parse_args()
    print(json.dumps(replay(args.report), indent=2))
