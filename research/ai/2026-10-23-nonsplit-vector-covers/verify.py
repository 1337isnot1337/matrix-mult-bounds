"""Offline exact replay; numerical optimizer bounds are never accepted."""
import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path

from cover_model import PRINCIPAL, verify_block
from weighted_discovery import run as weight_search

ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT/'results/nonsplit-vector-covers-2026-10-23'


def source_replay():
    saved = json.loads((RESULTS/'source-parity.json').read_text())
    for record in saved['source_files']:
        actual = hashlib.sha256((ROOT/record['path']).read_bytes()).hexdigest()
        if actual != record['sha256']:
            raise ValueError('pinned nonsplit source bytes changed')
    path = ROOT/saved['source_files'][0]['path']
    spec = importlib.util.spec_from_file_location('nonsplit_source', path)
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    certificate = json.loads((ROOT/saved['source_files'][1]['path']).read_text())
    source_report = source.verify(certificate)
    basis = [source.decode(text) for text in certificate['basis']]
    degrees = certificate['basis_degrees']
    if Counter(degrees[:88]) != Counter(dict(enumerate(PRINCIPAL))):
        raise ValueError('principal degree multiplicities changed')
    selected = [set(leg) & set(range(88))
                for leg in certificate['covers'][0]['selected_coordinates']]
    if not selected[0] == selected[1] == selected[2] or len(selected[0]) != 22:
        raise ValueError('principal coordinate cover changed')
    multiplication, inverse = source.source_group()
    principal = set()
    signatures = set()
    for a, b, c, value in source.coefficients(basis, multiplication, inverse):
        if max(a, b, c) < 88:
            ds = tuple(degrees[v] for v in (a, b, c))
            q = sum(v not in selected[0] for v in (a, b, c))
            if sum(ds) > 8 or sum(ds) % 2 or q > 2:
                raise ValueError('source violates claimed joint degree conditions')
            principal.add(ds)
            signatures.add((sum(ds), q))
    if sorted(map(list, principal)) != saved['principal_degree_triples']:
        raise ValueError('principal degree support changed')
    return certificate, {
        'basis_rank': source_report['basis_rank'],
        'coefficients_checked': source_report['original_group_coefficients_checked'],
        'nonzero_coefficients': source_report['original_group_nonzero_coefficients'],
        'principal_degree_triples': len(principal),
        'principal_total_even': True,
        'principal_degree_membership_signatures': sorted(map(list, signatures)),
        'principal_cover_size_per_leg': 22,
    }


def verify():
    certificate, source = source_replay()
    reports = []
    names = [f'discovery-{j}.json' for j in range(4)]
    names += [f'parity-discovery-{j}.json' for j in range(1, 4)]
    for name in names:
        discovery = json.loads((RESULTS/name).read_text())
        if discovery['optimality_certified'] is not False:
            raise ValueError('numerical optimality is not a certificate')
        replay = verify_block(discovery['principal_factors'],
                              discovery['selected_classes'],
                              discovery.get('even_principal', False))
        if replay['per_word_slices'] != discovery['exact_cover_replay']['per_word_slices']:
            raise ValueError('saved coordinate cover cost changed')
        reports.append({'file': name, **replay})
    saved = json.loads((RESULTS/'cover-weight-search.json').read_text())
    weighted = weight_search(certificate, saved['weight_limit'])
    if json.loads(json.dumps(weighted)) != saved:
        raise ValueError('bounded weight census changed')
    return {'source': source, 'degree_class_cover_replays': reports,
            'weight_limit': weighted['weight_limit'],
            'weight_vectors_checked': sum(row['weight_vectors_checked'] for row in weighted['rows']),
            'best_cube_slice_upper_bound': weighted['slice_upper_bound'],
            'improves_previous_cube_bound': False,
            'class_cover_optimality_certified': False,
            'scope': 'Fixed saved basis and cover, finite cube only; no global exclusion.',
            'exponent_improvement': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = verify()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
