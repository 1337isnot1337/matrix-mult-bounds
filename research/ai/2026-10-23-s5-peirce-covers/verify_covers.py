"""Full S5 source replay and independent finite coordinate count verification."""

import argparse
from collections import Counter
from hashlib import sha256
import importlib.util
from itertools import product
import json
from math import comb, isqrt, prod
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKAGE = Path(__file__).resolve().parent


def verify(source_certificate, certificate):
    spec = importlib.util.spec_from_file_location('s5_peirce_source_replay', PACKAGE/'source.py')
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    receipt = source.replay(source_certificate)
    if (certificate.get('schema') != 's5-peirce-finite-covers-v1'
            or certificate.get('improves_omega') is not False
            or certificate.get('arbitrary_complex_exclusion') is not False):
        raise ValueError('wrong cover schema or scope')
    if certificate['source_sha256'] != sha256(json.dumps(source_certificate, sort_keys=True).encode()).hexdigest():
        raise ValueError('wrong source certificate pin')
    if certificate['source_coefficients_checked'] != receipt['original_coefficients_checked']:
        raise ValueError('incorrect source replay coverage')
    type_counts = receipt['principal_type_counts']
    support = receipt['principal_type_support']
    prior_path = 'results/s5-finite-covers-2026-10-23/certificate.json'
    frontier_path = 'results/s5-block-filtration-2026-10-21/frontier.json'
    if set(certificate['prior_pins']) != {prior_path, frontier_path}:
        raise ValueError('missing prior frontier pin')
    for path, digest in certificate['prior_pins'].items():
        if sha256((ROOT/path).read_bytes()).hexdigest() != digest:
            raise ValueError('changed prior frontier')
    prior = json.loads((ROOT/prior_path).read_text())
    frontier = json.loads((ROOT/frontier_path).read_text())
    summaries = []
    if [s['central_rank'] for s in certificate['sources']] != [1, 2]:
        raise ValueError('wrong central-source list')
    for source_report in certificate['sources']:
        r = source_report['central_rank']
        if source_report['power'] != 3 or len(source_report['rows']) != 4:
            raise ValueError('wrong source power or block count')
        total = grouped = coordinates = 0
        for j, row in enumerate(source_report['rows']):
            if row['principal_factors'] != j:
                raise ValueError('wrong block-word order')
            degrees = row['principal_degrees']
            h = row['central_weight']
            if (len(degrees) != 19 or any(type(d) is not int or d < 0 for d in degrees)
                    or type(h) is not int or h <= 0):
                raise ValueError('invalid source weights')
            D = max(sum(degrees[t] for t in edge) for edge in support)
            if D != row['source_degree_bound']:
                raise ValueError('source degree budget does not match full support')
            k = 3*(r+1)-j
            histogram = Counter()
            for types in product(range(19), repeat=j):
                multiplicity = prod(type_counts[t] for t in types)
                principal = sum(degrees[t] for t in types)
                for central in product((0, 1), repeat=k):
                    histogram[principal+h*sum(central)] += multiplicity
                    grouped += 1
            scale = 16**(3-j)
            dimension = 88**j * 2**k * scale
            if sum(histogram.values())*scale != dimension:
                raise ValueError('missing coordinate multiplicity')
            cuts = row['cutoffs']
            if len(cuts) != 3 or any(type(c) is not int or c < -1 for c in cuts):
                raise ValueError('invalid cutoff')
            if sum(cuts) < j*D+k*h-2:
                raise ValueError('cutoffs fail the actual source degree budget')
            cost = scale*sum(count for degree, count in histogram.items() for c in cuts if degree <= c)
            if cost != row['selected_slices'] or cost > dimension:
                raise ValueError('wrong finite slice count')
            total += comb(3, j)*cost
            coordinates += comb(3, j)*dimension
        if total != source_report['slice_upper_bound'] or coordinates != (120*2**r)**3:
            raise ValueError('incorrect cube sum or full source dimension')
        if isqrt(total) != source_report['single_target_volume_upper_bound']:
            raise ValueError('wrong target-volume cap')
        old_bound = prior['sources'][r-1]['slice_upper_bound']
        previous_shapes = [row['shape'] for row in frontier['sources'][r-1]['records']
                           if not row['complex_koszul_excluded'] and prod(row['shape'])**2 <= old_bound]
        if previous_shapes != prior['sources'][r-1]['remaining_shapes']:
            raise ValueError('previous frontier does not match its saved bound')
        additional = [s for s in previous_shapes if prod(s)**2 > total]
        remaining = [s for s in previous_shapes if prod(s)**2 <= total]
        if (additional != source_report['additional_coordinate_exclusions']
                or remaining != source_report['remaining_shapes']):
            raise ValueError('incorrect target classification')
        summaries.append({'central_rank': r, 'slice_upper_bound': total,
                          'grouped_coordinates_checked': grouped,
                          'coordinate_multiplicity_checked': coordinates,
                          'single_target_volume_upper_bound': isqrt(total),
                          'additional_coordinate_exclusions': additional,
                          'remaining_shapes': remaining})
    return {'source_replay': receipt, 'sources': summaries,
            'independent_mathematical_review': False, 'improves_omega': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--certificate', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    receipt = verify(json.loads(args.source.read_text()), json.loads(args.certificate.read_text()))
    args.output.write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt['sources'], indent=2))
