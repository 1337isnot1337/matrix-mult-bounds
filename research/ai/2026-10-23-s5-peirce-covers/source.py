"""Construct and replay a full binary S5 basis from retained Peirce candidates."""

import argparse
from collections import Counter
from hashlib import sha256
import importlib.util
from itertools import permutations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DISCOVERY = ROOT/'research/ai/2026-10-21-s5-block-filtration/discovery/support.json'
BLOCKS = ROOT/'research/ai/2026-10-21-s5-block-filtration/blocks.py'
BLOCK_CERTIFICATE = ROOT/'results/s5-block-filtration-2026-10-21/certificate.json'
RADICAL = ROOT/'results/s5-split-2026-10-21/radical-pilot.json'


def bits(value):
    while value:
        bit = value & -value
        yield bit.bit_length()-1
        value ^= bit


def insert(value, pivots):
    while value:
        p = value.bit_length()-1
        if p not in pivots:
            pivots[p] = value
            return True
        value ^= pivots[p]
    return False


def construct():
    spec = importlib.util.spec_from_file_location('s5_peirce_prior_blocks', BLOCKS)
    blocks = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(blocks)
    discovery = json.loads(DISCOVERY.read_text())
    block_report = json.loads(BLOCK_CERTIFICATE.read_text())
    radical = json.loads(blocks.BASELINE.read_text())
    e = int(block_report['central_idempotent_32'], 16)
    small, degree, pivots = [], [], {}
    for value in radical['power_bases'][0]:
        candidate = blocks.multiply(e, int(value, 16))
        if insert(candidate, pivots):
            small.append(candidate)
            degree.append(1)
    if len(small) != 16:
        raise ValueError('small-block radical rank is not sixteen')
    for g in range(120):
        candidate = blocks.multiply(e, 1 << g)
        if insert(candidate, pivots):
            small.append(candidate)
            degree.append(0)
    if len(small) != 32:
        raise ValueError('small block rank is not thirty-two')
    return {'schema': 's5-full-peirce-source-v1', 'field': 'F2',
            'basis': discovery['vectors'] + [hex(v) for v in small],
            'principal_types': discovery['types'], 'principal_labels': discovery['labels'],
            'small_degrees': degree, 'common_cover_types': [6, 7, 10, 11, 18],
            'source_pins': {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest()
                            for p in (DISCOVERY, BLOCKS, BLOCK_CERTIFICATE, RADICAL)},
            'improves_omega': False}


def degree_family(u, v):
    return [12*u, 10*u+2*v, 8*u-2*v, 6*u, 6*u, 4*u+2*v, 2*u-2*v, 0,
            10*u-v, 8*u+v, 4*u-v, 2*u+v, 10*u-v, 8*u+v, 4*u-v, 2*u+v,
            12*u, 6*u, 0]


def replay(certificate):
    if certificate['schema'] != 's5-full-peirce-source-v1' or certificate['field'] != 'F2':
        raise ValueError('unsupported source')
    if certificate.get('improves_omega') is not False:
        raise ValueError('unsupported exponent status')
    if set(certificate['source_pins']) != {str(p.relative_to(ROOT))
                                         for p in (DISCOVERY, BLOCKS, BLOCK_CERTIFICATE, RADICAL)}:
        raise ValueError('missing source pins')
    for name, digest in certificate['source_pins'].items():
        if sha256((ROOT/name).read_bytes()).hexdigest() != digest:
            raise ValueError('changed source candidate')
    basis = [int(v, 16) for v in certificate['basis']]
    pivots = {}
    if len(basis) != 120 or any(not 0 < v < 1 << 120 for v in basis):
        raise ValueError('invalid full basis')
    if not all(insert(v, pivots) for v in basis):
        raise ValueError('singular full basis')
    labels = certificate['principal_labels']
    small_degrees = certificate['small_degrees']
    if (len(labels) != 88 or any(type(t) is not int or not 0 <= t < 19 for t in labels)
            or len(small_degrees) != 32 or Counter(small_degrees) != {0: 16, 1: 16}):
        raise ValueError('incorrect coordinate types')
    elements = list(permutations(range(5)))
    lookup = {p: i for i, p in enumerate(elements)}
    table = [[lookup[tuple(p[q[i]] for i in range(5))] for q in elements] for p in elements]
    inverse = [row.index(0) for row in table]
    inverse_basis = [sum(1 << inverse[g] for g in bits(v)) for v in basis]
    translations = []
    for g in range(120):
        translations.append([sum(1 << table[g][h] for h in bits(v)) for v in basis])
    support = set()
    counts = Counter()
    cover = set(certificate['common_cover_types'])
    if cover != {6, 7, 10, 11, 18}:
        raise ValueError('wrong stated common cover')
    endpoints = [degree_family(1, v) for v in (-1, 1)]
    for a in range(120):
        for b in range(120):
            product_value = 0
            for g in bits(basis[a]):
                product_value ^= translations[g][b]
            for c in range(120):
                if not (product_value & inverse_basis[c]).bit_count() % 2:
                    continue
                if max(a, b, c) < 88:
                    types = tuple(sorted((labels[a], labels[b], labels[c])))
                    support.add(types)
                    counts['principal_terms'] += 1
                    if not set(types) & cover:
                        raise ValueError('common cover misses an actual source term')
                    if any(sum(d[t] for t in types) > 12 for d in endpoints):
                        raise ValueError('weight family fails on actual source')
                elif min(a, b, c) >= 88:
                    counts['small_terms'] += 1
                    if small_degrees[a-88]+small_degrees[b-88]+small_degrees[c-88] > 1:
                        raise ValueError('small degree bound fails on actual source')
                else:
                    raise ValueError('nonzero cross-block coefficient')
    return {'basis_rank': len(pivots), 'original_coefficients_checked': 120**3,
            'principal_terms': counts['principal_terms'], 'small_terms': counts['small_terms'],
            'principal_type_counts': [labels.count(i) for i in range(19)],
            'principal_type_support': [list(edge) for edge in sorted(support)],
            'common_cover_coordinate_count': sum(t in cover for t in labels),
            'weight_family_endpoints': endpoints,
            'independent_mathematical_review': False, 'improves_omega': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--verification', type=Path, required=True)
    args = parser.parse_args()
    report = construct()
    receipt = replay(report)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.verification.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    args.verification.write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps({k: v for k, v in receipt.items() if k != 'principal_type_support'}, indent=2))
