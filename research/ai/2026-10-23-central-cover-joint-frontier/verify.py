"""Replay both source certificates and the complete stated finite frontier."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

from frontier import DEGREES, ROOT, frontier
from fourier_certificate import source_certificate
import cube_cover

HERE = Path(__file__).resolve().parent
RESULTS = ROOT/'results/central-cover-joint-frontier-2026-10-23'


def verify():
    sources = json.loads((HERE/'SOURCES.json').read_text())
    for record in sources['local']:
        if hashlib.sha256((ROOT/record['path']).read_bytes()).hexdigest() != record['sha256']:
            raise ValueError('adopted source bytes changed')
    complex_source = source_certificate()
    if complex_source['irreducible_degrees'] != DEGREES:
        raise ValueError('complex source degree certificate changed')
    path = ROOT/'research/ai/2026-10-21-sl2-finite-slices/verify_cover.py'
    spec = importlib.util.spec_from_file_location('joint_nonsplit_source', path)
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    certificate = json.loads((ROOT/'results/sl2-finite-slices-2026-10-21/cover-certificate.json').read_text())
    modular = source.verify(certificate)
    if modular['covers'][0]['slice_upper_bound'] != 98:
        raise ValueError('modular source slice certificate changed')
    cube = json.loads((RESULTS/'cube-certificate.json').read_text())
    cube_report = cube_cover.verify(cube, certificate['basis_degrees'])
    if cube_report['slice_upper_bound'] != 1012332:
        raise ValueError('source cube bound changed')
    actual = json.loads(json.dumps(frontier()))
    if actual != json.loads((RESULTS/'frontier.json').read_text()):
        raise ValueError('finite frontier or conditional gate changed')
    return {'complex_source_dimension': complex_source['order'],
            'complex_central_idempotent_products_checked': complex_source['pairwise_idempotent_products_verified'],
            'modular_source_basis_rank': modular['basis_rank'],
            'modular_source_coefficients_checked': modular['original_group_coefficients_checked'],
            'modular_source_slice_upper_bound': 98,
            'source_cube': cube_report,
            'sorted_shapes_checked': actual['sorted_shapes_checked'],
            'dimension_compatible_family_members': actual['dimension_compatible_family_members'],
            'improving_survivors': [{'shape': row['shape'], 'scalar_outputs': row['scalar_outputs']}
                                    for row in actual['improving_survivors']],
            'excluded_after_earlier_screens': actual['cube_exclusions'],
            'conditional_gates': actual['conditional_gates'],
            'independent_mathematical_review': False,
            'all_targets_constructed': False, 'improves_omega': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = verify()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))
