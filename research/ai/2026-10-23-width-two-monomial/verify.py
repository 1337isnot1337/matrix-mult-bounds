"""Replay every width-two support against the frozen original scorer."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
from itertools import product
import json
from math import comb
from pathlib import Path

PACKAGE = Path(__file__).resolve().parent
ROOT = PACKAGE.parents[2]
ARCHIVE = ROOT / 'research/ai/2026-10-20/search_degenerations.py'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_scorer():
    sources = json.loads((PACKAGE / 'sources.json').read_text())
    for source in sources['local_dependencies']:
        data = (ROOT / source['path']).read_bytes()
        require(hashlib.sha256(data).hexdigest() == source['sha256'],
                'source hash mismatch: ' + source['path'])
    spec = importlib.util.spec_from_file_location('width_two_archive', ARCHIVE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sign(value):
    return (value > 0) - (value < 0)


def short_shared_prediction(wx, wy):
    """Use only the path intervals, independently of the archived graph code."""
    require(len(wx) == 2 and len(wy) >= 2, 'expected C(2,b), b>=2')
    b = len(wy)
    delta = wx[1] - wx[0]
    signs = [sign(wy[k] - wy[k - 1] - delta) for k in range(1, b)]
    start = 0
    active = one_endpoint_vertices = 0
    components = []
    for end in range(b):
        if end < b - 1 and signs[end] == 0:
            continue
        size = end - start + 1
        endpoints = int(start == 0 or signs[start - 1] < 0)
        endpoints += int(end == b - 1 or signs[end] > 0)
        if size > 1 or endpoints:
            components.append({'start': start, 'size': size, 'endpoints': endpoints})
            active += size
            if endpoints == 1:
                one_endpoint_vertices += size
        start = end + 1
    deficit = Fraction(2 * (b - active) + one_endpoint_vertices, 3)
    return {
        'components': components,
        'inactive_y': b - active,
        'one_endpoint_vertices': one_endpoint_vertices,
        'score': Fraction(4 * b + 2, 3) - deficit,
        'deficit': deficit,
    }


def short_second_prediction(wx, wy):
    require(len(wy) == 2 and len(wx) >= 2, 'expected C(b,2), b>=2')
    b = len(wx)
    delta = wy[1] - wy[0]
    signs = [sign(wx[k] - wx[k - 1] - delta) for k in range(1, b)]
    if all(value == 0 for value in signs):
        return Fraction(4 * b + 2, 3)
    if all(value != 0 for value in signs):
        return Fraction(b + 1)
    return Fraction(max(2, 1 + sum(value <= 0 for value in signs),
                        1 + sum(value >= 0 for value in signs)))


def weights_for_signs(signs):
    values = [0]
    for value in signs:
        require(value in (-1, 0, 1), 'invalid sign')
        values.append(values[-1] + value)
    return tuple(values)


def equality_count(b):
    require(b >= 1, 'positive size required')
    return sum(comb(b - r - 1, 2 * r) for r in range((b - 1) // 3 + 1))


def original_score(scorer, wx, wy, h):
    groups, _ = scorer.components(wx, wy)
    blocks = [scorer.recognize(group) for group in groups]
    return sum((scorer.profile(block['a'], block['b'], h) for block in blocks),
               Fraction(0)), groups


def census(max_b=10):
    require(max_b >= 2, 'max_b must be at least two')
    scorer = load_scorer()
    h = scorer.slopes(max_b + 1)
    rows = []
    for b in range(2, max_b + 1):
        source = Fraction(4 * b + 2, 3)
        shared_histogram, second_histogram = Counter(), Counter()
        for signs in product((-1, 0, 1), repeat=b - 1):
            weights = weights_for_signs(signs)
            predicted = short_shared_prediction((0, 0), weights)
            score, groups = original_score(scorer, (0, 0), weights, h)
            require(score == predicted['score'], 'short-shared score mismatch')
            actual_components = sorted(
                (min(t[1] for t in group), len({t[1] for t in group}),
                 len({t[2] for t in group}) - len({t[1] for t in group}) + 1)
                for group in groups)
            expected_components = [(c['start'], c['size'], c['endpoints'])
                                   for c in predicted['components']]
            require(actual_components == expected_components, 'path partition mismatch')
            require(score <= source, 'short-shared score exceeds profile')
            shared_histogram[source - score] += 1

            score, _ = original_score(scorer, weights, (0, 0), h)
            require(score == short_second_prediction(weights, (0, 0)),
                    'short-second score mismatch')
            require(score <= source, 'short-second score exceeds profile')
            second_histogram[source - score] += 1
        require(shared_histogram[0] == equality_count(b), 'equality count mismatch')
        require(second_histogram[0] == 1, 'transposed equality count mismatch')
        require(min(d for d in shared_histogram if d) == Fraction(1, 3),
                'short-shared gap is not sharp')
        require(min(d for d in second_histogram if d) == Fraction(b - 1, 3),
                'short-second gap is not sharp')
        rows.append({
            'b': b,
            'supports_per_orientation': 3 ** (b - 1),
            'source_exact': str(source),
            'short_shared_equalities': equality_count(b),
            'short_second_equalities': 1,
            'short_shared_deficit_histogram': {str(k): v for k, v in sorted(shared_histogram.items())},
            'short_second_deficit_histogram': {str(k): v for k, v in sorted(second_histogram.items())},
        })
    return {
        'schema': 'width-two-monomial-census-v1',
        'max_b': max_b,
        'orientation_support_checks': 2 * sum(3 ** (b - 1) for b in range(2, max_b + 1)),
        'rows': rows,
        'scope': 'Every sign word in both orientations for 2<=b<=max_b; no weight cutoff.',
        'universal_proof_status': 'proof-written-unreviewed',
        'improves_omega': False,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-b', type=int, default=10)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--check', type=Path)
    args = parser.parse_args()
    report = census(args.max_b)
    if args.check:
        require(report == json.loads(args.check.read_text()), 'recorded census mismatch')
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'max_b': report['max_b'],
                      'orientation_support_checks': report['orientation_support_checks'],
                      'recorded_report_checked': bool(args.check)}))


if __name__ == '__main__':
    main()
