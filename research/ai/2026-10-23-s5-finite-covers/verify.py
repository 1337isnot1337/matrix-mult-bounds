"""Replay the source certificate and grouped coordinates without the producer."""

import argparse
from collections import Counter
from functools import lru_cache
from hashlib import sha256
import importlib.util
from itertools import product
import json
from math import comb, isqrt, prod
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def coordinate_counts(layers, j, k, s, h):
    counts = Counter()
    grouped = 0
    for principal in product(range(len(layers)), repeat=j):
        multiplicity = prod(layers[d] for d in principal)
        for central in product((0, 1), repeat=k):
            counts[s*sum(principal)+h*sum(central)] += multiplicity
            grouped += 1
    return counts, grouped


def degree_triples(maximum):
    return [(a, b, c) for a in range(maximum+1)
            for b in range(maximum+1-a) for c in range(maximum+1-a-b)]


@lru_cache(None)
def replay_source(pins):
    # The caller checks every pin on every invocation, including cached calls.
    spec = importlib.util.spec_from_file_location(
        's5_finite_prior_blocks', ROOT/'research/ai/2026-10-21-s5-block-filtration/blocks.py')
    blocks = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(blocks)
    certificate = json.loads((ROOT/'results/s5-block-filtration-2026-10-21/certificate.json').read_text())
    return blocks.verify(certificate), certificate['block_layers']


def verify(report):
    require(report.get('schema') == 's5-finite-covers-v1', 'wrong schema')
    require(report.get('scope') == (
        'One-copy characteristic-two degenerations to a single matrix tensor; '
        'over C only the maintained coefficient-one coordinate/potential class.'), 'wrong scope')
    require(report.get('proof_status') == 'written proof; unreviewed; not formalized'
            and report.get('improves_omega') is False
            and report.get('optimal_cover_claimed') is False, 'unsupported status')
    required_pins = {
        'research/ai/2026-10-21-s5-block-filtration/blocks.py',
        'results/s5-block-filtration-2026-10-21/certificate.json',
        'research/ai/2026-10-21-s5-split/verify_radical.py',
        'results/s5-split-2026-10-21/radical-pilot.json',
        'results/s5-block-filtration-2026-10-21/frontier.json',
        'research/ai/2026-10-21-central-cover-finite-slices/proof.md',
    }
    require(set(report['source_pins']) == required_pins, 'missing source pins')
    for path, digest in report['source_pins'].items():
        require(sha256((ROOT/path).read_bytes()).hexdigest() == digest, 'changed source '+path)
    source_receipt, (layers, small) = replay_source(tuple(sorted(report['source_pins'].items())))
    require(small == [16, 16, 0, 0, 0, 0, 0], 'wrong small block')
    old = json.loads((ROOT/'results/s5-block-filtration-2026-10-21/frontier.json').read_text())
    require(len(report['sources']) == 2, 'wrong source count')
    receipts = []
    for r, source, previous in zip((1, 2), report['sources'], old['sources']):
        require(source['central_rank'] == r and source['source_dimension'] == 120*2**r
                and source['power'] == 3 and len(source['rows']) == 4, 'wrong source format')
        total = grouped = triples = coordinates = 0
        for j, row in enumerate(source['rows']):
            k = 3*(r+1)-j
            require(row['principal_factors'] == j and row['central_factors'] == k
                    and row['word_multiplicity'] == comb(3, j)
                    and row['matrix_multiplicity'] == 16**(3-j), 'wrong block word')
            s, h = row['weights']
            require(type(s) is int and type(h) is int and s > 0 and h > 0, 'bad weights')
            counts, number = coordinate_counts(layers, j, k, s, h)
            grouped += number
            require([counts[d] for d in range(6*j*s+k*h+1)]
                    == row['degree_counts_without_matrix'], 'coordinate histogram mismatch')
            dimension = 88**j * 16**(3-j) * 2**k
            require(sum(counts.values()) * 16**(3-j) == dimension
                    and row['whole_leg_slices'] == dimension, 'dimension mismatch')
            cuts = row['cutoffs']
            if cuts is None:
                cost = dimension
            else:
                require(len(cuts) == 3 and all(type(c) is int and c >= -1 for c in cuts), 'bad cutoffs')
                require(sum(cuts) >= 6*j*s+k*h-2, 'cutoffs do not cover total degree')
                # Independent exhaustive support-majorant check in both degrees.
                for principal in degree_triples(6*j):
                    for central in degree_triples(k):
                        require(any(s*principal[i]+h*central[i] <= cuts[i] for i in range(3)),
                                'uncovered source-degree triple')
                        triples += 1
                cost = 16**(3-j) * sum(count for d, count in counts.items()
                                      for cut in cuts if d <= cut)
            require(cost == row['selected_slices'] and cost <= dimension, 'slice count mismatch')
            total += comb(3, j)*cost
            coordinates += comb(3, j)*dimension
        require(coordinates == (120*2**r)**3, 'incomplete source coordinates')
        require(total == source['slice_upper_bound']
                and isqrt(total) == source['single_target_volume_upper_bound'], 'wrong volume bound')
        survivors = [row for row in previous['records'] if not row['complex_koszul_excluded']]
        require(len(survivors) == source['previous_complex_test_survivor_count'], 'wrong frontier size')
        new = [row['shape'] for row in survivors if prod(row['shape'])**2 > total
               and not row['coordinate_modular_excluded']]
        remaining = [row['shape'] for row in survivors if prod(row['shape'])**2 <= total]
        require(new == source['new_coordinate_exclusions'] and remaining == source['remaining_shapes'],
                'wrong frontier comparison')
        receipts.append({'central_rank': r, 'slice_upper_bound': total,
                         'grouped_coordinates_checked': grouped,
                         'coordinate_multiplicity_checked': coordinates,
                         'degree_triples_checked': triples,
                         'new_coordinate_exclusions': len(new), 'remaining_shapes': remaining})
    return {'source_replay': source_receipt, 'sources': receipts,
            'independent_mathematical_review': False, 'improves_omega': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--certificate', type=Path, required=True)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    receipt = verify(json.loads(args.certificate.read_text()))
    if args.output:
        args.output.write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt, indent=2))
